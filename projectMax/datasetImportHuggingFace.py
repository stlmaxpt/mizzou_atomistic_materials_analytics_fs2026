from huggingface_hub import hf_hub_download
import pandas as pd
import numpy as np

file_path = hf_hub_download(
    repo_id="cooperzvegintzov/OpenPoly",
    filename="experiment_polymer_data.xlsx",
    repo_type="dataset"
)

polymer_data = pd.read_excel(file_path)

print(polymer_data.head())
print(polymer_data.columns)

# Inspect your column names from Cell 1 and replace these
# with the exact names in the spreadsheet.
target_columns = ["Tg_K", "Tm_K", "Td_K"]

# Convert invalid numerical entries to NaN
targets = polymer_data[target_columns].apply(
    pd.to_numeric, errors="coerce"
).replace([np.inf, -np.inf], np.nan)

print("Total datapoints:", len(polymer_data))

for col in target_columns:
    print(f"Viable {col} datapoints:", targets[col].notna().sum())

print(
    "Datapoints with at least one target:",
    targets.notna().any(axis=1).sum()
)

print(
    "Datapoints with all three targets:",
    targets.notna().all(axis=1).sum()
)

print(
    "Duplicate rows:",
    polymer_data.duplicated().sum()
)