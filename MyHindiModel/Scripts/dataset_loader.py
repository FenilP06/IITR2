import os
from TTS.tts.datasets import load_tts_samples
from TTS.tts.configs.shared_configs import BaseDatasetConfig
from TTS.tts.datasets import HinData

# Dataset configuration
dataset_config = BaseDatasetConfig(
    formatter= HinData,  # Use your custom formatter
    meta_file_train="metadata.csv",  # Metadata file created in previous step
    language="hi",  # Specify the language code
    path="C:/Users/fenil/OneDrive/Desktop/IITR2/MyHindiModel/MyTTSDataset"  # Path to dataset directory
)

# Load the dataset
train_samples, eval_samples = load_tts_samples(dataset_config, eval_split=True, formatter=HinData)
 
