#!/usr/bin/env python3
"""
Demo script that simulates downloading ML models or large files
"""
import os
import time

def download_models():
    """Simulate downloading models"""
    models_dir = "models"
    os.makedirs(models_dir, exist_ok=True)
    
    models = [
        "model1.pkl",
        "model2.pkl", 
        "weights.bin"
    ]
    
    for model in models:
        model_path = os.path.join(models_dir, model)
        if not os.path.exists(model_path):
            print(f"Downloading {model}...")
            # Simulate download time
            time.sleep(1)
            # Create dummy file
            with open(model_path, "w") as f:
                f.write(f"# Dummy {model} file\n")
            print(f"✓ Downloaded {model}")
        else:
            print(f"✓ {model} already exists")

if __name__ == "__main__":
    download_models()