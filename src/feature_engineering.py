import pandas as pd
import logging

# Configure logging for feature engineering steps
logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

class FeatureEngineer:
    def __init__(self, df: pd.DataFrame):
        self.df = df

    def create_target_variable(self) -> pd.DataFrame:
        """Create the binary target variable 'is_late' based on delivery dates."""
        logging.info("Creating target variable 'is_late'...")
        
        # Ensure date columns are converted to datetime format
        if 'order_estimated_delivery_date' in self.df.columns and 'order_delivered_customer_date' in self.df.columns:
            self.df['order_estimated_delivery_date'] = pd.to_datetime(self.df['order_estimated_delivery_date'])
            self.df['order_delivered_customer_date'] = pd.to_datetime(self.df['order_delivered_customer_date'])
            
            # 1 if delivered after estimated date, else 0
            self.df['is_late'] = (
                self.df['order_delivered_customer_date'] > self.df['order_estimated_delivery_date']
            ).astype(int)
        
        return self.df

    def extract_date_features(self) -> pd.DataFrame:
        """Extract useful time-based features from order timestamps."""
        logging.info("Extracting time-based features...")
        
        if 'order_purchase_timestamp' in self.df.columns:
            self.df['order_purchase_timestamp'] = pd.to_datetime(self.df['order_purchase_timestamp'])
            self.df['purchase_hour'] = self.df['order_purchase_timestamp'].dt.hour
            self.df['purchase_dayofweek'] = self.df['order_purchase_timestamp'].dt.dayofweek
            
        return self.df

if __name__ == "__main__":
    print("Feature Engineer module template ready!")