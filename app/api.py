from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
import pickle
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
model_path = config['paths']['model_output_path']

# Load the trained model safely
model = None
if os.path.exists(model_path):
    with open(model_path, 'rb') as f:
        model = joblib.load(model_path)

# Define request body schema using Pydantic
class OrderRequest(BaseModel):
    order_item_id: int
    price: float
    freight_value: float
    product_name_lenght: float = 0.0
    product_description_lenght: float = 0.0
    product_photos_qty: float = 0.0

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
        raise HTTPException(status_code=500, status_log="Model not found or not trained yet.")
    
    # Convert input data to DataFrame format expected by the model
    input_data = pd.DataFrame([order.dict()])
    
    try:
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