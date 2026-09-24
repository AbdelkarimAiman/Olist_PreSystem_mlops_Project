import os
import pytest
from src.config_loader import load_config
from src.preprocessing import OlistDataProcessor

def test_config_loading():
    """Test if configuration loads successfully and contains required keys."""
    config = load_config()
    assert config is not None
    assert 'paths' in config
    assert 'raw_data_path' in config['paths']

def test_raw_data_exists():
    """Test if raw data file exists before running processor."""
    config = load_config()
    raw_path = config['paths']['raw_data_path']
    assert os.path.exists(raw_path), f"Raw data file not found at {raw_path}"

def test_data_processor_loading():
    """Test data loading function from OlistDataProcessor."""
    config = load_config()
    processor = OlistDataProcessor(config['paths']['raw_data_path'])
    df = processor.load_data()
    assert df is not None
    assert not df.empty