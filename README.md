# TTS Model Installation and Usage Guide

This document provides instructions for installing and using the Text-to-Speech (TTS) model.

## Table of Contents
1. [Prerequisites](#prerequisites)
2. [Installation Steps](#installation-steps)
3. [Commandline TTS](#commandline-tts)
4. [Read Docs](#read-docs)
5. [Train Your own Model](#train-model)

## 1. Prerequisites

Before installing the TTS model, ensure you have the following:

- Python 3.8 or higher
- pip (Python package manager)
- A compatible GPU (recommended) with CUDA installed (for faster inference)
- Required libraries (listed in the `requirements.txt` file)

## 2. Installation Steps

```bash
git clone https://github.com/coqui-ai/TTS
pip install -e .[all,dev,notebooks]  # Select the relevant extras
```

If you are on Ubuntu (Debian), you can also run following commands for installation.

```bash
$ make system-deps  # intended to be used on Ubuntu (Debian). Let us know if you have a different OS.
$ make install
```

Clone this repositry

```bash
git clone https://github.com/FenilP06/IITR_2
```

## 3. Commandline TTS

Synthesize speech on command line.

You can either use your trained model or choose a model from the provided list.

If you don't specify any models, then it uses LJSpeech based English model.

#### Single Speaker Models

- List provided models:

  ```
  $ tts --list_models
  ```


- Run TTS with default models:

  ```
  $ tts --text "Text for TTS" --out_path output/path/speech.wav
  ```

- Run your own TTS model (Using Griffin-Lim Vocoder):

  ```
  $ tts --text "Text for TTS" --model_path path/to/model.pth --config_path path/to/config.json --out_path output/path/speech.wav
  ```

- Run your own TTS model (Using server.py):

  ```
  $ python ./TTS/server/server.py --config_path path/to/config.json --model_path path/to/model.pth 
  ```

## 4. Read Docs 

| Type                            | Links                               |
| ------------------------------- | --------------------------------------- |
| 💼 **Documentation**            | [ReadTheDocs](https://tts.readthedocs.io/en/latest/)
| 📌 **Road Map**                 | [Main Development Plans](https://github.com/coqui-ai/TTS/issues/378)
| 🚀 **Released Models**          | [TTS Releases](https://github.com/coqui-ai/TTS/releases) and [Experimental Models](https://github.com/coqui-ai/TTS/wiki/Experimental-Released-Models)|
| 📰 **Papers**                   | [TTS Papers](https://github.com/erogol/TTS-papers)|

## 5. Train Your Own Model

Choose your model from TTS Model Library
You can list model

  ```
  $ tts --list_models
  ```
Go To TTS/recipes fodeer and choose train file accordig to your need.
Manifest specific model train file.

```
python recipes/<dataset>/<model_name>/train.py
```
