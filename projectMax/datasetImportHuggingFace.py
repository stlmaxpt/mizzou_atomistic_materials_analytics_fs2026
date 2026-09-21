from huggingface_hub import hf_hub_download
import pandas as pd

file_path = hf_hub_download(
    repo_id="cooperzvegintzov/OpenPoly",
    filename="experiment_polymer_data.xlsx",
    repo_type="dataset"
)

polymer_data = pd.read_excel(file_path)

print(polymer_data.head())
print(polymer_data.columns)
