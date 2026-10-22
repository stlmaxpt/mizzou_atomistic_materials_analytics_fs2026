import pandas as pd

df_full = pd.read_parquet("CompoundData_WithEngineeredFeatures.parquet")

print(df_full.shape)
