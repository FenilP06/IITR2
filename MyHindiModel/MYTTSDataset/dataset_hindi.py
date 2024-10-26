import csv
import os
import re

# Path to the .tsv file and the folder containing .wav files
tsv_file = "C:/Users/fenil/OneDrive/Desktop/HIndi_dataset/cv-corpus-19.0-delta-2024-09-13/hi/other.tsv"  # Replace with the actual path
audio_folder = "C:/Users/fenil/OneDrive/Desktop/HIndi_dataset/output"  # Replace with the folder containing converted .wav files
metadata_file = "metadata.csv"

# Load available .wav files into a set for fast lookup
available_files = set(os.listdir(audio_folder))

# Function to normalize the transcription for Hindi
def normalize_transcription(transcription):
    # Example normalization rules for Hindi
    transcription = re.sub(r'\d+', lambda x: num_to_hindi(x.group()), transcription)  # Convert numbers to Hindi
    transcription = transcription.replace('%', ' प्रतिशत')  # Convert symbols
    transcription = transcription.replace('API', 'ए पी आई')  # Convert abbreviations (customize for other abbreviations)
    # Add more rules as needed for specific technical terms or characters
    return transcription

# Function to convert numbers to Hindi words
def num_to_hindi(number):
    hindi_numbers = {
        '0': 'शून्य', '1': 'एक', '2': 'दो', '3': 'तीन', '4': 'चार',
        '5': 'पांच', '6': 'छह', '7': 'सात', '8': 'आठ', '9': 'नौ'
    }
    return ''.join(hindi_numbers[digit] for digit in number)

with open(tsv_file, 'r', encoding='utf-8') as tsv, open(metadata_file, 'w', newline='', encoding='utf-8') as csvfile:
    reader = csv.DictReader(tsv, delimiter='\t')
    writer = csv.writer(csvfile, delimiter='|')

    for row in reader:
        # Extract the audio filename and transcription from the .tsv file
        audio_file = f"{row['path'].replace('.mp3', '.wav')}"
        transcription = row['sentence'].strip()

        # Normalize the transcription for Hindi
        normalized_transcription = normalize_transcription(transcription)

        # Only include the row if the corresponding .wav file exists
        if audio_file in available_files:
            writer.writerow([audio_file, transcription, normalized_transcription])
            print(f"Processed: {audio_file} | {transcription} | {normalized_transcription}")
