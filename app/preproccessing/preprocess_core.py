import pandas as pd
from data_loader import load_data

# Conversion of data types for optimization
def convert_dtypes(df):
    df["category"] = df["category"].astype('category')

    return df

# Creation / Modififcation of new features
def feature_engineering(df):
    df["engagement_score"] = (( df["likes"] + df["comments"] )/ df["views"])

    return df

# Main function for preprocessing and returning cleaned DataFrame
def preprocessor():
    df = load_data()
    
    df = convert_dtypes(df)
    df = feature_engineering(df)