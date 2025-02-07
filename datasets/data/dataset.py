"""
This script reads data from a JSON file and appends it to a CSV file.
The JSON file is expected to contain a list of dictionaries, each with the
keys:
- 'transcript': A string representing the transcript text.
- 'is_fraudulent': An integer (0 or 1) indicating whether the transcript is
  fraudulent.
The CSV file will be appended with rows containing:
- The transcript text.
- The integer value indicating if the transcript is fraudulent.
File paths:
- JSON file: dataset.json
- CSV file: transcripts.csv
"""
import json
import csv

# Paths to the files
JSON_FILE_PATH = './dataset.json'
CSV_FILE_PATH = './transcripts.csv'

# Read data from JSON file
with open(JSON_FILE_PATH, 'r', encoding='utf-8') as json_file:
    data = json.load(json_file)

# Open the CSV file in append mode
with open(CSV_FILE_PATH, 'a', newline='', encoding='utf-8') as csv_file:
    csv_writer = csv.writer(csv_file)

    # Write data to CSV file
    for entry in data:
        csv_writer.writerow([entry['transcript'], int(entry['is_fraudulent'])])
