<h1 align="center">The Caduceus Project</h1>

<p align="center">
  <img src="https://github.com/user-attachments/assets/8ae905f3-6884-45cb-bd50-0838a5c8e3db" alt="Caduceus Project Logo" width="300">
</p>

The Caduceus Project is an initiative aimed at improving the conversion of complex scientific and medical PDF files to well-structured markdown format. By utilizing the power of OpenAI's GPT-4o model, this project aims to enhance the accessibility and usability of scientific and medical information. The PDF files used were taken from [protocols.io](https://github.com/protocolsio/protocols), an open source repository of medical and scientific protocols.

## Dataset Creation

The dataset is created through the following steps:

1. **PDF to Text Conversion**: The `pdf2txt.py` script is used to convert PDF files in a specified input folder to plain text format. It extracts the text content from each page of the PDF files using the `PyPDF2` library and saves the extracted text as individual text files in a specified output folder.

2. **Text Analysis**: The `densitymap.py` script processes the converted text files to calculate word counts, the occurrence of specific units of measurement, and the ratio of measurements to word count for each file. It saves this data to a CSV file named `word_counts_and_measurements.csv` and creates density maps for word counts and measurements ratios using matplotlib.

3. **Data Filtering**: The `scatterplot.py` script reads the data from the `word_counts_and_measurements.csv` file and creates an interactive scatter plot using Plotly. This plot visualizes the relationship between "Measurements Ratio" and "Word Count" for the dataset. The script filters the data based on thresholds for these two metrics, allowing for the selection of high-quality content.

4. **PDF to Markdown Conversion**: The `pdf2md.py` script converts the filtered PDF files to markdown format. It uses the `pdf2image` library to convert PDF pages to images and sends these images along with a prompt to the OpenAI API for conversion to markdown. The generated markdown content is saved in a JSONL file and optionally as individual markdown files.

5. **Dataset Cleaning**: The `move.py` script is used to clean the dataset by moving PDF files based on the "Measurements Ratio" and "Word Count" thresholds. Files meeting the thresholds are moved to a subset folder, while files not meeting the thresholds are moved to an unused folder.

## Code Versatility

This code can be modified in order to convert any type of PDF files to markdown format.

Certainly! Here's an alternative way to write the "Usage" section without using so many backticks, making it easier to read:

## Usage

To use the Caduceus Project scripts, follow these steps:

1. Install the required dependencies by running the following command:
   
   <pre>
   pip install -r requirements.txt
   </pre>

2. Update the file paths and API key in the scripts:
   - In `pdf2txt.py`:
     - Set `INPUT_FOLDER` to the directory containing the PDF files you want to convert.
     - Set `OUTPUT_FOLDER` to the directory where you want to save the converted text files.
   - In `densitymap.py`:
     - Set `TXT_FOLDER` to the directory containing the converted text files.
   - In `scatterplot.py`:
     - Set `CSV_FILE` to the path of the `word_counts_and_measurements.csv` file generated by `densitymap.py`.
     - Adjust `ratio_threshold` and `word_count_threshold` variables according to your desired filtering criteria.
   - In `pdf2md.py`:
     - Set `pdf_folder` to the directory containing the filtered PDF files you want to convert to markdown.
     - Set `output_file` to the path where you want to save the JSONL file containing the converted markdown content.
     - If you want to save individual markdown files, provide the `markdown_folder` when prompted.
   - In `move.py`:
     - Set `CSV_FILE` to the path of the `word_counts_and_measurements.csv` file.
     - Set `PDF_FOLDER` to the directory containing the original PDF files.
     - Set `SUBSET_FOLDER` to the directory where you want to move the PDF files meeting the thresholds.
     - Set `UNUSED_FOLDER` to the directory where you want to move the PDF files not meeting the thresholds.
     - Adjust `ratio_threshold` and `word_count_threshold` variables to match the values used in `scatterplot.py`.

3. Run the scripts in the following order:
   - `pdf2txt.py`: Converts the PDF files in the `INPUT_FOLDER` to text format and saves the converted files in the `OUTPUT_FOLDER`.
     <pre>
     python pdf2txt.py
     </pre>

   - `densitymap.py`: Analyzes the converted text files in the `TXT_FOLDER`, calculates word counts, unit counts, and measurements ratios, and creates density maps. Saves the data to the `word_counts_and_measurements.csv` file.
     <pre>
     python densitymap.py
     </pre>

   - `scatterplot.py`: Reads the data from the `word_counts_and_measurements.csv` file and creates an interactive scatter plot for data filtering. Filters the data based on the specified `ratio_threshold` and `word_count_threshold` and saves the filtered data to `interactive_scatter_plot_subset.html`.
     <pre>
     python scatterplot.py
     </pre>

   - `move.py`: Cleans the dataset by moving the PDF files based on the thresholds specified in `scatterplot.py`. Moves the PDF files meeting the thresholds to the `SUBSET_FOLDER` and the files not meeting the thresholds to the `UNUSED_FOLDER`.
     <pre>
     python move.py
     </pre>

   - `pdf2md.py`: Converts the filtered PDF files in the `SUBSET_FOLDER` to markdown format using the OpenAI API. Saves the converted markdown content to the specified `output_file` in JSONL format. If prompted, provide the `markdown_folder` to save individual markdown files.
     <pre>
     python pdf2md.py
     </pre>

4. After running the scripts, you will have a cleaned dataset of PDF files in the `SUBSET_FOLDER` and their corresponding markdown conversions in the `output_file` and optionally in the `markdown_folder`.

5. Use the generated dataset for model fine-tuning or further analysis as needed.

Remember to replace the placeholders (e.g., `INPUT_FOLDER`, `OUTPUT_FOLDER`, `TXT_FOLDER`, etc.) with the actual paths on your system and set the appropriate thresholds in `scatterplot.py` and `move.py` based on your requirements.
## Contributions

Contributions to the Caduceus Project are welcome! If you have any ideas, suggestions, or improvements, please feel free to open an issue or submit a pull request on the project's GitHub repository.

## License

The Caduceus Project is open-source and available under the [Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/).

Under this license, you are free to:
- Share: Copy and redistribute the material in any medium or format.
- Adapt: Remix, transform, and build upon the material for any purpose, even commercially.

The licensor cannot revoke these freedoms as long as you follow the license terms.

You must give appropriate credit, provide a link to the license, and indicate if changes were made. You may do so in any reasonable manner, but not in any way that suggests the licensor endorses you or your use.

Please see the [Creative Commons Attribution 4.0 International (CC BY 4.0) License](https://creativecommons.org/licenses/by/4.0/) for more details.
