import pandas as pd
import os

# Load raw data
df = pd.read_csv("raw_data.csv")

# Clean data (remove rows with missing values)
df_cleaned = df.dropna()

# Save processed data
df_cleaned.to_csv("processed_data.csv", index=False)
print("--- Data Cleaning Complete ---")
