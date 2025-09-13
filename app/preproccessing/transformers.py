from sklearn.base import BaseEstimator, TransformerMixin
import pandas as pd

class DTypeConverter(BaseEstimator, TransformerMixin):
    def fit(self, X, y=None):
        return self
    
    def transform(self, X):
        X = X.copy()
        X["category"] = X["category"].astype("category")
        return X
    