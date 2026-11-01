import kagglehub

# Download latest version
path = kagglehub.dataset_download("datascikhan/e-commerce-customer-behavior-dataset-2026")

print("Path to dataset files:", path)