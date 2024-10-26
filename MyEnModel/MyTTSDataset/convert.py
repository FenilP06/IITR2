from pydub import AudioSegment
import os

# Path to folder containing audio files
input_folder = "C:/Users/fenil/OneDrive/Desktop/HIndi_dataset/cv-corpus-19.0-delta-2024-09-13/hi/clips"  # Change this to your input folder
output_folder = "C:/Users/fenil/OneDrive/Desktop/HIndi_dataset/output"  # Change this to your desired output folder

# Ensure output folder exists
os.makedirs(output_folder, exist_ok=True)

# Convert all .mp3 files to .wav
for file in os.listdir(input_folder):
    if file.endswith(".mp3"):
        audio = AudioSegment.from_mp3(os.path.join(input_folder, file))
        audio = audio.set_frame_rate(16000)  # Set to 16kHz sample rate
        audio.export(os.path.join(output_folder, file.replace(".mp3", ".wav")), format="wav")
        print(f"Converted {file} to .wav format")


