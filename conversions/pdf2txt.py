import os
from PyPDF2 import PdfReader
import logging

# Set up logging
logging.basicConfig(filename='pdf_to_txt_conversion.log', level=logging.INFO,
                    format='%(asctime)s:%(levelname)s:%(message)s')

# Define input and output folders here
INPUT_FOLDER = r'/home/REDACTED/Documents/Code/dataset-stuff/caduceus/pdf-files'
OUTPUT_FOLDER = r'/home/REDACTED/Documents/Code/dataset-stuff/caduceus/txt-files'

def pdf_to_txt(pdf_path, txt_path):
    try:
        with open(pdf_path, 'rb') as pdf_file:
            pdf_reader = PdfReader(pdf_file)
            text = ''
            for page in pdf_reader.pages:
                text += page.extract_text()
        
        with open(txt_path, 'w', encoding='utf-8') as txt_file:
            txt_file.write(text)
        logging.info(f"Successfully converted {pdf_path} to {txt_path}")
    except Exception as e:
        logging.error(f"Error converting {pdf_path}: {str(e)}")

def batch_convert(input_folder, output_folder):
    if not os.path.exists(output_folder):
        os.makedirs(output_folder)

    for filename in os.listdir(input_folder):
        if filename.endswith('.pdf'):
            pdf_path = os.path.join(input_folder, filename)
            txt_path = os.path.join(output_folder, filename[:-4] + '.txt')
            pdf_to_txt(pdf_path, txt_path)

if __name__ == "__main__":
    if not os.path.exists(INPUT_FOLDER):
        print(f"Error: Input folder '{INPUT_FOLDER}' does not exist.")
    else:
        batch_convert(INPUT_FOLDER, OUTPUT_FOLDER)
        print(f"Conversion complete. TXT files saved in '{OUTPUT_FOLDER}'.")