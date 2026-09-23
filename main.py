import logging
from src.preprocessing import OlistDataProcessor
from src.feature_engineering import FeatureEngineer
from src.train import ModelTrainer

# Configure main logging
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def run_pipeline():
    logging.info("Starting Olist Late Delivery Prediction Pipeline...")
    
    # Step 1: Data Processing
    processor = OlistDataProcessor("data/raw/olist_orders_dataset.csv")
    df = processor.load_data()
    df = processor.clean_data(df)
    
    # Step 2: Feature Engineering
    engineer = FeatureEngineer(df)
    df = engineer.create_target_variable()
    df = engineer.extract_date_features()
    
    # Save processed data temporarily for training reference if needed
    processed_path = "data/processed/final_processed_data.csv"
    df.to_csv(processed_path, index=False)
    logging.info(f"Processed data saved to {processed_path}")
    
    # Step 3: Model Training
    logging.info("Starting Model Training phase...")
    trainer = ModelTrainer(processed_path)
    trainer.train_model()
    
    logging.info("Pipeline execution completed successfully!")

if __name__ == "__main__":
    run_pipeline()