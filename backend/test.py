import gdown
import pickle
import os
import pandas as pd

# === Define the base path relative to the script ===
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
MODELS_DIR = os.path.join(BASE_DIR, "model")

# === Create models directory if it doesn't exist ===
os.makedirs(MODELS_DIR, exist_ok=True)

# === Google Drive file links ===
vectors_drive = "https://drive.google.com/uc?id=1B2yXv1mvsj86Tbmh3_zwG9C4LvIaMjnX"
similarity_drive = "https://drive.google.com/uc?id=1BqMwZTXQSLsr5Y-6gFIRjkTyGY0lTOUz"
data_drive = "https://drive.google.com/uc?id=1pwTW9svCRtAmqJxoWQjQ10_qWJBPXKEL"

# === Download files if they don't exist ===
data_path = os.path.join(MODELS_DIR, "cleaned_data.csv")
if not os.path.exists(data_path):
    gdown.download(data_drive, data_path, quiet=False)

# === Load dataset ===
movies = pd.read_csv(data_path)

# === Use the data ===
mine = movies["title"]
print(mine[:10])
