import kagglehub

path = kagglehub.dataset_download(
    "shrutimechlearn/churn-modelling",
    output_dir="/home/rishi/projects/Customer-Engagement-Product-Utilization-Analytics-for-Retention-Strategy/data/raw",
    force_download=True
)

print("Dataset saved at:", path)