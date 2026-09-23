import pandas as pd
import logging

# Configure logging to track data processing steps
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class OlistDataProcessor:
    def __init__(self, data_path: str):
        self.data_path = data_path

    def load_data(self) -> pd.DataFrame:
        """Load the raw dataset from the specified path."""
        logging.info("Loading dataset...")
        df = pd.read_csv(self.data_path)
        return df

    def clean_data(self, df: pd.DataFrame) -> pd.DataFrame:
        """Perform data cleaning and handle missing values."""
        logging.info("Cleaning dataset...")
        df = df.dropna()
        return df

if __name__ == "__main__":
    # Quick local test for the module
    processor = OlistDataProcessor("data/raw/olist_orders_dataset.csv")
    print("Data Processor initialized successfully!")