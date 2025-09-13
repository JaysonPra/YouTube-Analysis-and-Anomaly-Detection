from sklearn.ensemble import IsolationForest
from sklearn.preprocessing import RobustScaler
from sklearn.pipeline import Pipeline
from preproccessing.preprocess_core import preprocessor

def build_anomaly_model(df):
    features = ["views", "likes", "comments", "duration"]
    X = df[features]
    
    pipeline = Pipeline([
        ("scaler", RobustScaler()),
        ("isolation", IsolationForest(contamination=0.05, random_state=42))
    ])

    df["is_anomaly"] = pipeline.fit_predict(features)

    return df