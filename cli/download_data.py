import kagglehub
import shutil

destination = "data/raw"

path = kagglehub.dataset_download("blastchar/telco-customer-churn")

dest = shutil.move(path, destination)

print("Path to dataset files:", dest)
