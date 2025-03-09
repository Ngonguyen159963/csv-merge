import pandas as pd
import os

# Folder containing CSV files
csv_folder = "CSV"
output_file = "merged_activities.csv"

# Get all CSV files in folder
csv_files = [f for f in os.listdir(csv_folder) if f.endswith(".csv")]

# Merge all files
df_list = [pd.read_csv(os.path.join(csv_folder, file)) for file in csv_files]
merged_df = pd.concat(df_list, ignore_index=True)

# Save merged file
merged_df.to_csv(output_file, index=False)

print(f"✅ All CSV files merged into {output_file}")
