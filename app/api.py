from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pandas as pd
import os
import joblib
from src.config_loader import load_config

# Initialize FastAPI app
app = FastAPI(
    title="Olist Late Delivery Prediction API",
    description="API service for predicting late deliveries in e-commerce orders.",
    version="1.0.0"
)

# Load configuration and model path
config = load_config()
model_path = "models/random_forest_model.pkl"

# Load the trained model safely
model = joblib.load(model_path) if os.path.exists(model_path) else None

# Define request body schema matching model features
class OrderRequest(BaseModel):
    total_payment: float = 0.0
    total_price: float = 0.0
    purchase_dayofweek: int = 0
    purchase_hour: int = 0

@app.get("/")
def home():
    return {"message": "Welcome to Olist MLOps Prediction API!"}

@app.get("/health")
def health_check():
    """Health check route to verify service status."""
    return {
        "status": "healthy",
        "model_loaded": model is not None
    }

@app.post("/predict")
def predict_delivery(order: OrderRequest):
    """Predict if an order will be late based on input features."""
    if model is None:
        raise HTTPException(status_code=500, detail="Model not found or not trained yet.")
    
    try:
        # تحويل المدخلات إلى DataFrame
        input_data = pd.DataFrame([order.dict()])
        
        # مطابقة أعمدة الموديل مباشرة بدون سكيلر خارجي
        if hasattr(model, "feature_names_in_"):
            input_data = input_data.reindex(columns=model.feature_names_in_, fill_value=0)

        prediction = model.predict(input_data)
        probability = model.predict_proba(input_data)[:, 1][0]
        
        result = "Late" if prediction[0] == 1 else "On Time"
        
        return {
            "prediction": result,
            "probability": float(probability),
            "model_version": "v1.0"
        }
    except Exception as e:
        raise HTTPException(status_code=400, detail=str(e))