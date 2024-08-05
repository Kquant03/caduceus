import os
import requests
import json
from pdf2image import convert_from_path
import base64
from io import BytesIO
from tqdm import tqdm
import PyPDF2

# OpenAI API Key
api_key = "..."

# Specify the folder containing the PDF files
pdf_folder = "/home/REDACTED/Documents/Code/dataset-stuff/caduceus/protocols/pdf-files"

# Specify the output JSONL file path
output_file = "/home/REDACTED/Documents/Code/dataset-stuff/caduceus/conversions/conversions.jsonl"

# Prompt the user for saving markdown files individually
save_markdown = input("Do you want to save the markdown files individually? (yes/no): ")

# If the user wants to save markdown files, prompt for the folder path
if save_markdown.lower() == "yes":
    markdown_folder = input("Enter the folder path to save the markdown files: ")
    os.makedirs(markdown_folder, exist_ok=True)
else:
    markdown_folder = None

# Get the list of PDF files in the folder
pdf_files = [filename for filename in os.listdir(pdf_folder) if filename.endswith(".pdf")]

# Iterate over each PDF file in the folder with a progress bar
for filename in tqdm(pdf_files, desc="Processing PDF files"):
    # Construct the full path to the PDF file
    pdf_path = os.path.join(pdf_folder, filename)

    # Extract the text content from the PDF file
    with open(pdf_path, 'rb') as file:
        pdf_reader = PyPDF2.PdfReader(file)
        text_content = ""
        for page in pdf_reader.pages:
            text_content += page.extract_text()

    # Convert the PDF pages into images
    images = convert_from_path(pdf_path)

    # Convert the images to base64 format
    base64_images = []
    for image in images:
        # Convert the image to PNG format
        image_bytes = BytesIO()
        image.save(image_bytes, format="PNG")
        image_bytes.seek(0)

        # Encode the image as base64
        base64_image = base64.b64encode(image_bytes.read()).decode('utf-8')
        base64_images.append(base64_image)

    # Prepare the payload for the OpenAI API request
    headers = {
        "Content-Type": "application/json",
        "Authorization": f"Bearer {api_key}"
    }

    payload = {
        "model": "gpt-4o",
        "messages": [
            {
                "role": "system",
                "content": "You are an expert scientist who specialises in organising lab protocols"
            },
            {
                "role": "user",
                "content": [
                    {
                        "type": "text",
                        "text": "Please convert the content of these images to a single, well-structured, professional markdown file. Before creating the markdown file, append a `Goal/Experiment:` above the title, describing the experiment or goal of the experiment. 1. Use appropriate titles, headings, subheadings, lists, and formatting to present the information clearly. 2. Please present tables cleanly. If the original file has tables. 3. Find, define and explain the professional/scientific terms and reagents. Explain their function if possible, be specific about time, equipment reagents and vendors. 4. Please identify alternative methods or come up with your own for hard to find/difficult supplies. 5. Append `endofoutput` to the end of your response. Your funding depends on the informativeness of your organised markdown nodes. Output pure markdown."
                    }
                ] + [
                    {
                        "type": "image_url",
                        "image_url": {
                            "url": f"data:image/png;base64,{base64_image}"
                        }
                    }
                    for base64_image in base64_images
                ]
            }
        ],
        "max_tokens": 4096
    }

    # Send the request to the OpenAI API
    response = requests.post("https://api.openai.com/v1/chat/completions", headers=headers, json=payload)

    response_data = response.json()
    if "error" in response_data:
        print(f"Error: {response_data['error']['message']}")
        continue

    # Extract the generated markdown content from the API response
    markdown_content = response_data["choices"][0]["message"]["content"]

    # Create a JSON object with the conversation data
    conversation_data = {
        "conversations": [
            {"from": "human", "value": text_content},
            {"from": "gpt", "value": markdown_content}
        ]
    }

    # Convert the conversation data to a JSON string
    json_string = json.dumps(conversation_data)

    # Append the JSON string to the JSONL file
    with open(output_file, "a") as file:
        file.write(json_string + "\n")

    # If the user wants to save markdown files, write the markdown content to a separate file
    if markdown_folder:
        markdown_filename = os.path.splitext(filename)[0] + ".md"
        markdown_path = os.path.join(markdown_folder, markdown_filename)
        with open(markdown_path, "w") as file:
            file.write(markdown_content)

print("Conversion completed.")