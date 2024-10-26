import pandas as pd

# Read the CSV file
file_path = 'C:/Users/fenil/OneDrive/Desktop/IITR2/MyHindiModel/MYTTSDataset/metadata.csv'  # Update this to your file path
df = pd.read_csv(file_path, delimiter='|', header=None)

# Function to clean the text data
def clean_text(text):
    # Remove unwanted characters
    cleaned_text = text.replace('‘', '') \
                        .replace('’', '') \
                        .replace('“', '') \
                        .replace('”', '') \
                        .replace('\ufeff', '')  # This removes the BOM if present
    return cleaned_text

# Apply the cleaning function to the relevant columns
df[1] = df[1].apply(clean_text)  # Clean the second column
df[2] = df[2].apply(clean_text)  # Clean the third column

# Save the cleaned DataFrame to a new CSV file
cleaned_file_path = 'C:/Users/fenil/OneDrive/Desktop/IITR2/MyHindiModel/MYTTSDataset/metadata1.csv'  # Update this to your desired output path
df.to_csv(cleaned_file_path, sep='|', header=False, index=False)
