# 🐶 Dog Breed Classification with VGG19

This project is a **Deep Learning application** that classifies dog images into **70 different breeds** using **Transfer Learning with VGG19**.  
It includes data preprocessing, model training, evaluation, and a **Streamlit app** for deployment.

---

## 📂 Project Structure
├── App.py # Streamlit app for deployment
├── dog_project.keras # Trained model
├── requirements.txt # Dependencies
├── README.md # Project documentation
├── notebooks/ # Jupyter notebooks for training & experiments
└── dataset/ # Dog breed dataset (images)

yaml
Copy code

---

## 🚀 Features
- Preprocessing and augmentation of dog images.
- Transfer Learning with **VGG19** pretrained on ImageNet.
- Fine-tuning for **70 dog breeds**.
- Model evaluation with accuracy, loss curves, and classification report.
- **Streamlit app** for interactive prediction.

---

## ⚙️ Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/Dog-breed-classification.git
   cd Dog-breed-classification
Create and activate a virtual environment (optional but recommended):

bash
Copy code
python -m venv venv
source venv/bin/activate   # On Linux/Mac
venv\Scripts\activate      # On Windows
Install dependencies:

bash
Copy code
pip install -r requirements.txt
📊 Dataset
The dataset consists of images of 70 dog breeds.

Images are resized to 224×224 before feeding into the model.

Data is split into training, validation, and test sets.

🧠 Model
Base Model: VGG19 (pretrained on ImageNet)

Modifications:

Frozen convolutional base

Added fully-connected layers for classification

Softmax output for 70 classes

📈 Results
Training & validation accuracy plotted during training.

Final accuracy: ~XX% (replace with your actual result).

Confusion matrix & classification report included in notebooks.

🎮 Usage
Run the Streamlit App
bash
Copy code
streamlit run App.py
Upload a dog image.

The model predicts the breed with probability score.

🛠️ Requirements
Main dependencies:

Python 3.8+

TensorFlow / Keras

NumPy, Pandas

Matplotlib, Seaborn

Streamlit

Pillow

Full list in requirements.txt.

📸 Demo
(Add screenshots/gifs of your Streamlit app here for better presentation)

🤝 Contributing
Pull requests are welcome!
For major changes, please open an issue first to discuss what you’d like to improve.

📜 License
This project is licensed under the MIT License.

👩‍💻 Author
Menna Reda
🔗 LinkedIn | 🔗 GitHub