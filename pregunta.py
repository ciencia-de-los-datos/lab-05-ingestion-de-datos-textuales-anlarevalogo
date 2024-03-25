"""
Laboratorio ingestion de datos textuales
-----------------------------------------------------------------------------------------

Realice la limpieza del dataframe. Los tests evaluan si la limpieza fue realizada 
correctamente. Tenga en cuenta datos faltantes y duplicados.

"""
import os
import csv
import pandas as pd

def create_training_testing_set():
    paths = [("/train/", "train_dataset.csv"), ("/test/", "test_dataset.csv")]
    categories = ["negative", "positive", "neutral"]
    
    for path, output_file in paths:
        with open(output_file, "w", newline="") as csv_file:
            csv_writer = csv.writer(csv_file)
            csv_writer.writerow(["phrase", "sentiment"])
        
        for category in categories:
            folder_path = os.path.join("data", path, category)
            with open(output_file, "a", newline="") as csv_file:
                csv_writer = csv.writer(csv_file)
                for file in os.listdir(folder_path):
                    if file.endswith(".txt"):
                        file_path = os.path.join(folder_path, file)
                        with open(file_path, "r") as text_file:
                            content = text_file.read()
                            csv_writer.writerow([content, category])

create_training_testing_set()