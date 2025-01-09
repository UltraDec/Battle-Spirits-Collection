import csv
import os
import requests

# Configurations
csv_file = './CB22.csv'  # Your CSV file name
output_folder = './CB22jpg'  # Folder to save the images

# Create the output folder if it doesn't exist
os.makedirs(output_folder, exist_ok=True)


# Read the CSV and download images
with open(csv_file, mode='r', newline='', encoding='utf-8') as file:
    reader = csv.DictReader(file)
    for row in reader:
        image_url = row['Link']
        image_name = row['Name'].replace(' ', '_') + os.path.splitext(image_url)[1]  # Use card name as filename
        output_path = os.path.join(output_folder, image_name)

        try:
            # Download the image
            response = requests.get(image_url, stream=True)
            response.raise_for_status()  # Raise an error for bad responses
            with open(output_path, 'wb') as img_file:
                for chunk in response.iter_content(1024):
                    img_file.write(chunk)
            print(f"Downloaded: {image_name}")
        except Exception as e:
            print(f"Failed to download {image_url}: {e}")
