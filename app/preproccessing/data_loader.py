from pathlib import Path
import yaml
from joblib import Memory
import pandas as pd

memory = Memory(location="cache_dir", verbose=0)

# Getting the root path of the project
def get_project_root():
    return Path(__file__).resolve().parents[2]

# Loading config.yaml file from configs directory
def load_config():
    config_path = get_project_root() / "config" / "config.yaml"
    with open(config_path, "r") as f:
        return yaml.safe_load(f)
    
@memory.cache
def load_data():
    # Loading the CSV
    config = load_config()
    csv_path = get_project_root() / config['data']['youtube_csv']
    df = pd.read_csv(csv_path)
    return df