### Dog Breed Classification with EfficientNetB0

This project is a Computer Vision application that classifies dog images into 70 different breeds using Transfer Learning with EfficientNetB0.
It includes data preprocessing, model training, evaluation, and a Streamlit app for easy deployment.

------------------------------------------------------------
## Project Structure
------------------------------------------------------------
├── App.py               # Streamlit app for deployment
├── dog_project.keras    # Trained EfficientNetB0 model (saved)
├── data/                # Dataset (train/valid images)
│   ├── train/
│   └── valid/
└── README.txt           # Project documentation

------------------------------------------------------------
## Installation
------------------------------------------------------------
Clone the repository and install dependencies:

git clone https://github.com/mennareda123/dog-breed-classification.git
cd dog-breed-classification
pip install -r requirements.txt


------------------------------------------------------------
## Usage
------------------------------------------------------------
1. Run the Streamlit app:
   streamlit run app.py

2. Open the provided local URL in your browser (or use the ngrok link if deployed).
3. Upload a dog image — the app will predict the breed from the 70 available classes.

------------------------------------------------------------
## Model Details
------------------------------------------------------------
- Base model: EfficientNetB0 (pretrained on ImageNet)
- Top layers: GlobalAveragePooling -> Dense(512, ReLU) -> Dense(70, Softmax)
- Loss function: Categorical Crossentropy
- Optimizer: Adam (learning rate = 1e-4)
- Training strategy: transfer learning → freeze base weights, train top classifier; optionally fine-tune last N layers.

------------------------------------------------------------
## Try It on Google Colab
------------------------------------------------------------
You can run the training and prediction code directly on Google Colab:

Open In Colab: [https://colab.research.google.com/drive/1nqY3A3nFuQ7U0F01ULT70LxA2rBGM1o8]

------------------------------------------------------------
## Notes on Data & Preprocessing
------------------------------------------------------------
- Images resized to 224x224 (matching EfficientNetB0 input).
- Use ImageDataGenerator for augmentation during training (rotation, shift, zoom, flip, brightness).
- flow_from_dataframe or flow_from_directory with class_mode='categorical' (70 classes).

------------------------------------------------------------
## Results & Tips
------------------------------------------------------------
- Use data augmentation and early stopping to improve generalization.
- If training on CPU is slow, try EfficientNetB0 with reduced batch size or switch to GPU/TPU for faster training.
- Save checkpoints with model.save() and reload with tf.keras.models.load_model() to resume training.

------------------------------------------------------------
## Future Work
------------------------------------------------------------
- Add more breeds and balance classes.
- Use learning-rate scheduling and more aggressive fine-tuning.
- Deploy on Streamlit Cloud or Hugging Face Spaces for public use.

------------------------------------------------------------
## Requirements (example)
------------------------------------------------------------
- Python 3.8+
- TensorFlow / Keras
- Streamlit
- pandas, numpy, Pillow

(Provide an explicit requirements.txt in the repo for exact versions.)

------------------------------------------------------------
### Author
------------------------------------------------------------
Developed by Menna Reda
LinkedIn: https://www.linkedin.com/in/menna-reda-6048182a3
