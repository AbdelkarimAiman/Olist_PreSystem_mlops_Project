import yaml
import os
import logging

logging.basicConfig(level=logging.INFO, format='%(asctime)s - %(levelname)s - %(message)s')

def load_config(config_path: str = "config/config.yaml") -> dict:
    """Load configuration from YAML file."""
    if not os.path.exists(config_path):
        logging.error(f"Configuration file not found at {config_path}")
        raise FileNotFoundError(f"Config file missing: {config_path}")
    
    with open(config_path, 'r') as file:
        config = yaml.safe_load(file)
        logging.info("Configuration loaded successfully.")
        return config