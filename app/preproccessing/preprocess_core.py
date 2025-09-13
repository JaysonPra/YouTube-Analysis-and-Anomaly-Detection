import pandas as pd
from data_loader import load_data

# Conversion of data types for optimization
def convert_dtypes(df):
    # Conversion of category feature from str to category
    df["category"] = df["category"].astype('category')

    # Conversion of hashtags feature from str to list of tags
    df["hashtags"] = df["hashtags"].apply(
        lambda x: [tag.strip() for tag in x.split(',') if tag.strip()]
        if pd.notna(x) else []    
    )

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

    return df