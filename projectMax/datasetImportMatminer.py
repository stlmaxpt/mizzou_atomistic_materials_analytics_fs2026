from matminer.datasets import load_dataset

steels = load_dataset("matbench_steels")

print(steels.head())

