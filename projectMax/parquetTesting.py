import pandas as pd
from rdkit import Chem
from rdkit.Chem import Descriptors3D
from rdkit import RDLogger
import numpy as np
from rdkit.Chem import Descriptors
from rdkit.Chem import rdFingerprintGenerator
import matplotlib.pyplot as plt

morgan_generator = rdFingerprintGenerator.GetMorganGenerator(
    radius=2,
    fpSize=2048
)

RDLogger.DisableLog('rdApp.warning')

df = pd.read_parquet("CompoundDataFuncsFingerprints.parquet")

# First few rows
#print(df.head())

# Dimensions
#print(df.shape)

# Column names and data types
#print(df.columns)

#mol_string = df['mol3D'].iloc[0]

#mol = Chem.MolFromMolBlock(mol_string, removeHs=False)

#print(Descriptors3D.RadiusOfGyration(mol))

# Radius of Gyration calculation:

radius_of_gyration = []
count_none = 0
for i in range(df.shape[0]):
    mol_string = df['mol3D'].iloc[i]
    mol = Chem.MolFromMolBlock(mol_string, removeHs=False, strictParsing=False, sanitize=False)
    if mol is None:
        radius_of_gyration.append(np.nan)
        count_none += 1
    else:
        radius_of_gyration.append(Descriptors3D.RadiusOfGyration(mol))

df["Radius of Gyration"] = radius_of_gyration

# Number of Rotatable Bonds calculation:

rot_bonds = []
count_none = 0
for i in range(df.shape[0]):
    mol = Chem.MolFromSmiles(df['SMILES'].iloc[i])
    if mol is None:
        rot_bonds.append(np.nan)
        count_none += 1
    else:
        rot_bonds.append(Descriptors.NumRotatableBonds(mol))

df["Number of Rotatable Bonds"] = rot_bonds

# Morgan Fingerprint calculation:

morg_prints = []
count_none = 0
for i in range(df.shape[0]):
    mol = Chem.MolFromSmiles(df['SMILES'].iloc[i])
    if mol is None:
        morg_prints.append(np.nan)
        count_none += 1
    else:
        morg_prints.append(morgan_generator.GetFingerprint(mol))

df["Morgan Fingerprints"] = morg_prints

print(type(df['Fingerprint'].iloc[0]))
print(df['Fingerprint'].iloc[0])

print(df.columns)

# Plotting:
# Simple scatter plot for radius of gyration:

plt.scatter(df["Radius of Gyration"], df['BP'], c=df['MW'], alpha=0.5)
plt.xlabel("Radius of Gyration")
plt.ylabel("Boiling Point")
plt.title("Radius of Gyration vs Boiling Point")

plt.show()