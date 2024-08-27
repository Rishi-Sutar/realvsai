
# Real vs AI-Generated Image Classifier

This project is a deep learning classifier that distinguishes between real images and AI-generated images. It utilizes a ResNet34 model fine-tuned on a dataset of real and AI-generated images and is deployed using Streamlit for easy interaction.


## Features

- Classifies images as either "Real" or "AI-Generated"
- Uses a ResNet34 architecture fine-tuned for high accuracy
- Provides an interactive web interface using Streamlit
- Visualization of data and model performance using Seaborn


## Installation

To set up the project, follow these steps:

- Clone the repository:

```bash
git clone https://github.com/yourusername/real-vs-ai-image-classifier.git
cd real-vs-ai-image-classifier
```

- Create and activate a Conda environment:

```bash
conda create --n image_classifier python=3.9
conda activate image_classifier
```

- Install required packages:

```bash
pip install -r requirements.txt
```
- Train and save the model

In order to train and save the model run all the cells from real-vs-ai.ipynb

```bash
streamlit run app.py
```


## Model Details

- **Architecture:** ResNet34
- **Dataset:** https://www.kaggle.com/datasets/cashbowman/ai-generated-images-vs-real-images
- **Accuracy:** Achieves a high accuracy of 84% after fine-tuning