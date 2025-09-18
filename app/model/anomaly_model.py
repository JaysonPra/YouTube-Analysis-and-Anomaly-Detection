from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
import joblib
import sys
import os

project_root = os.path.abspath(os.path.join(os.path.dirname(__file__), '..'))
sys.path.insert(0, project_root)

from preprocessing.preprocess_core import preprocessor

def build_anomaly_model():
    df = preprocessor()

    features = ["views", "likes", "comments", "duration"]
    X = df[features].copy()

    X = X[(X != 0).all(axis=1)]
    
    pipeline = Pipeline([
        ("scaler", RobustScaler()),
        ("isolation", IsolationForest(contamination=0.05, random_state=42))
    ])

    pipeline.fit(X)

    save_path = os.path.join(os.path.dirname(__file__), "saves", "isolation_pipeline.pkl")
    joblib.dump(pipeline, save_path)