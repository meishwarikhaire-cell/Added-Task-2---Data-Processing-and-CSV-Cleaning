import json

# Step 1: JSON file open
with open("data/trends_20260406.json", "r") as file:
    data = json.load(file)

# Step 2: Data check 
print("Total records:", len(data))

# Step 3: First record 
print(data[0])
import pandas as pd

# JSON data DataFrame me convert 
df = pd.DataFrame(data)

# First 5 rows 
print(df.head())

# Duplicate 
df = df.drop_duplicates(subset="title")

# Missing values fill
df["score"] = df["score"].fillna(0)
df["num_comments"] = df["num_comments"].fillna(0)

# Title clean
df["title"] = df["title"].str.lower().str.strip()

print("Data cleaned successfully!")

# CSV me save
df.to_csv("data/cleaned_trends.csv", index=False)

print("CSV file saved!")
