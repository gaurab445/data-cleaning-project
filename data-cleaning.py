# clean_data.py
import pandas as pd

# The working URL for the Iris Flower dataset
data_url = "https://raw.githubusercontent.com/uiuc-cse/data-fa14/gh-pages/data/iris.csv"

print("1. Loading data from the internet...")
df = pd.read_csv(data_url) # type: ignore

print("2. First look at the data:")
print(df.head()) # Shows the first 5 rows
print("\n3. Data info:")
print(df.info()) # Shows the data types and if there's missing data

print("\n4. Checking for missing values:")
print(df.isnull().sum()) # Counts missing values in each column

print("\n5. Checking for duplicate rows:")
duplicate_count = df.duplicated().sum()
print(f"Number of duplicate rows: {duplicate_count}")

print("\n6. Cleaning data...")
# Let's remove duplicates instead of missing values for this dataset
df_clean = df.drop_duplicates()

print("\n7. Data after cleaning:")
print(f"New shape of the data: {df_clean.shape}")
print(f"Duplicates removed: {duplicate_count}")

# to save the new clear data 
clean_filename='iris_clean.csv' 
df_clean.to_csv(clean_filename,index= False)
print(f"\n8. All done! Cleaned data saved to '{clean_filename}'.")