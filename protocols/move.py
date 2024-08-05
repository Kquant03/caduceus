import os
import csv
import shutil

# Define the paths
CSV_FILE = '/home/REDACTED/Documents/Code/dataset-stuff/caduceus/logs/word_counts_and_measurements.csv'  # Update this to your CSV file path
PDF_FOLDER = r'/home/REDACTED/Documents/Code/dataset-stuff/caduceus/pdf-files'  # Update this to your PDF folder path
SUBSET_FOLDER = r'/home/REDACTED/Documents/Code/dataset-stuff/caduceus/subset-pdfs'  # Update this to the desired subset folder path
UNUSED_FOLDER = r'/home/REDACTED/Documents/Code/dataset-stuff/caduceus/unused-pdfs'  # Update this to the desired unused folder path

def move_unused_pdfs(csv_file, pdf_folder, subset_folder, unused_folder, ratio_threshold=0.02, word_count_threshold=1000):
    # Create the subset and unused folders if they don't exist
    os.makedirs(subset_folder, exist_ok=True)
    os.makedirs(unused_folder, exist_ok=True)
    
    # Read the CSV file
    with open(csv_file, 'r', newline='', encoding='utf-8') as file:
        reader = csv.DictReader(file)
        for row in reader:
            measurements_ratio = float(row['Measurements Ratio'])
            word_count = int(row['Word Count'])
            file_name = row['File Name'].replace('.txt', '.pdf')
            
            pdf_path = os.path.join(pdf_folder, file_name)
            
            if os.path.exists(pdf_path):
                if measurements_ratio > ratio_threshold and word_count > word_count_threshold:
                    # Move the PDF to the subset folder
                    subset_path = os.path.join(subset_folder, file_name)
                    shutil.move(pdf_path, subset_path)
                    print(f"Moved {file_name} to the subset folder.")
                else:
                    # Move the PDF to the unused folder
                    unused_path = os.path.join(unused_folder, file_name)
                    shutil.move(pdf_path, unused_path)
                    print(f"Moved {file_name} to the unused folder.")
            else:
                print(f"PDF file {file_name} not found.")

if __name__ == "__main__":
    move_unused_pdfs(CSV_FILE, PDF_FOLDER, SUBSET_FOLDER, UNUSED_FOLDER)