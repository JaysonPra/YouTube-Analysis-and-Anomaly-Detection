from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
import joblib
from preproccessing.preprocess_core import preprocessor

def build_anomaly_model():
    df = preprocessor()

    features = ["views", "likes", "comments", "duration"]
    X = df[features].copy()
    
    pipeline = Pipeline([
        ("scaler", RobustScaler()),
        ("isolation", IsolationForest(contamination=0.05, random_state=42))
    ])

    pipeline.fit(X)

    joblib.dump(pipeline, "saves/isolation_pipeline.pkl")