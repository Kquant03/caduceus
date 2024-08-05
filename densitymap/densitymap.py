import os
import matplotlib.pyplot as plt
import numpy as np
import csv
import re

# Define the folder containing your txt files
TXT_FOLDER = r'/home/REDACTED/Documents/Code/dataset-stuff/caduceus/txt-files'

# Define the units of measurement to search for
UNITS = ['μL', 'uL', 'ul', 'μl', 'μL', 'μg']

def count_words(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        words = text.split()
        return len(words)

def count_units(file_path):
    with open(file_path, 'r', encoding='utf-8') as file:
        text = file.read()
        unit_count = sum(text.count(unit) for unit in UNITS)
        return unit_count

def get_word_counts(folder_path):
    word_counts = []
    unit_counts = []
    file_names = []
    for filename in os.listdir(folder_path):
        if filename.endswith('.txt'):
            file_path = os.path.join(folder_path, filename)
            word_count = count_words(file_path)
            unit_count = count_units(file_path)
            word_counts.append(word_count)
            unit_counts.append(unit_count)
            file_names.append(filename)
    return word_counts, unit_counts, file_names

def save_word_counts_to_csv(word_counts, unit_counts, file_names, output_file):
    with open(output_file, 'w', newline='', encoding='utf-8') as csvfile:
        writer = csv.writer(csvfile)
        writer.writerow(['File Name', 'Word Count', 'Unit Count', 'Measurements Ratio'])  # Header
        for name, word_count, unit_count in zip(file_names, word_counts, unit_counts):
            measurements_ratio = unit_count / word_count if word_count != 0 else 0
            writer.writerow([name, word_count, unit_count, measurements_ratio])
    print(f"Word counts and measurements ratios saved to {output_file}")

def create_density_map(word_counts, file_names, title, xlabel, ylabel, filename):
    plt.figure(figsize=(12, 8))
    plt.hist(word_counts, bins=30, density=True, alpha=0.7)
    plt.title(title)
    plt.xlabel(xlabel)
    plt.ylabel(ylabel)
    plt.grid(True, alpha=0.3)
    
    # Add mean and median lines
    mean = np.mean(word_counts)
    median = np.median(word_counts)
    plt.axvline(mean, color='r', linestyle='dashed', linewidth=2, label=f'Mean: {mean:.2f}')
    plt.axvline(median, color='g', linestyle='dashed', linewidth=2, label=f'Median: {median:.2f}')
    
    plt.legend()
    plt.tight_layout()
    plt.savefig(filename)
    plt.close()

    # Print some statistics
    print(f"Total files: {len(word_counts)}")
    print(f"Mean {xlabel.lower()}: {mean:.2f}")
    print(f"Median {xlabel.lower()}: {median:.2f}")
    print(f"Min {xlabel.lower()}: {min(word_counts)} ({file_names[word_counts.index(min(word_counts))]})")
    print(f"Max {xlabel.lower()}: {max(word_counts)} ({file_names[word_counts.index(max(word_counts))]})")

if __name__ == "__main__":
    word_counts, unit_counts, file_names = get_word_counts(TXT_FOLDER)
    
    # Save word counts and measurements ratios to CSV
    csv_file = 'word_counts_and_measurements.csv'
    save_word_counts_to_csv(word_counts, unit_counts, file_names, csv_file)
    
    # Calculate measurements ratios
    measurements_ratios = [unit_count / word_count if word_count != 0 else 0 for word_count, unit_count in zip(word_counts, unit_counts)]
    
    create_density_map(word_counts, file_names, 'Density Map of Word Counts', 'Word Count', 'Density', 'word_count_density_map.png')
    print("Word count density map has been saved as 'word_count_density_map.png'")
    
    create_density_map(measurements_ratios, file_names, 'Density Map of Nanoliter Ratios', 'Measurements Ratio', 'Density', 'nanoliter_ratio_density_map.png')
    print("Measurements ratio density map has been saved as 'measurements_ratio_density_map.png'")