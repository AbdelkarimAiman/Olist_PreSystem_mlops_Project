import pandas as pd
import joblib
import logging
from sklearn.ensemble import RandomForestClassifier
from sklearn.model_selection import train_test_split
from sklearn.metrics import accuracy_score, classification_report

# Configure logging for the training process
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class ModelTrainer:
    def __init__(self, data_path: str):
        self.data_path = data_path
        self.model = RandomForestClassifier(n_estimators=100, random_state=42)

    def train_model(self) -> None:
        """Load data, split into train/test, train the Random Forest model, and save it."""
        logging.info("Loading dataset for training...")
        df = pd.read_csv(self.data_path)
        
        # Assuming 'is_late' is our target variable and dropping non-feature columns
        if 'is_late' in df.columns:
            X = df.drop(columns=['is_late'])
            y = df['is_late']
            
            # Simple handling of numeric columns for the baseline script
            X = X.select_dtypes(include=['number'])
            
            # Split data into training and testing sets
            X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
            
            logging.info("Training the Random Forest model...")
            self.model.fit(X_train, y_train)
            
            # Evaluate the model
            predictions = self.model.predict(X_test)
            acc = accuracy_score(y_test, predictions)
            logging.info(f"Model trained successfully! Test Accuracy: {acc:.4f}")
            
            # Save the trained model to disk
            model_path = "models/random_forest_model.pkl"
            joblib.dump(self.model, model_path)
            logging.info(f"Model saved successfully to {model_path}")
        else:
            logging.error("Target column 'is_late' not found in the dataset.")

if __name__ == "__main__":
    # Test training pipeline locally
    trainer = ModelTrainer("data/processed/final_data.csv")
    print("Model Trainer module template ready!")