import csv

# Function to convert CSV to TXT
def csv_to_txt(csv_file, txt_file):
    with open(csv_file, 'r', encoding='utf-8') as csv_f, open(txt_file, 'w', encoding='utf-8') as txt_f:
        csv_reader = csv.reader(csv_f)
        
        for row in csv_reader:
            # Join columns in a row by space and write to the TXT file
            txt_f.write(' '.join(row) + '\n')

# Example usage
csv_file = 'C:/Users/fenil/OneDrive/Desktop/IITR2/MyHindiModel/MYTTSDataset/metadata.csv'  # Replace with your CSV file path
txt_file = 'metadata.txt'  # Replace with your desired TXT file path

csv_to_txt(csv_file, txt_file)
