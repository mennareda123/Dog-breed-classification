#  Dog Breed Classification with ResNet50

This project is a **Computer Vision application** that classifies dog images into **70 different breeds** using **Transfer Learning with ResNet50**.  
It includes data preprocessing, model training, evaluation, and a **Streamlit app** for deployment.

---

##  Project Structure
```
├── App.py                 # Streamlit app for deployment
├── dog_project.keras      # Trained ResNet50 model
├── requirements.txt       # Dependencies
├── README.md              # Project documentation
├── ResNet full code
└── dataset/               # Dog breed dataset
```

---

##  Features
- Preprocessing and augmentation of dog images.
- Transfer Learning with **ResNet50** pretrained on ImageNet.
- Fine-tuning for **70 dog breeds**.
- Model evaluation with accuracy, loss curves, and classification report.
- **Streamlit app** for interactive prediction.

---

##  Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/mennareda123/Dog-breed-classification.git
   cd Dog-breed-classification
   ```

2. Create and activate a virtual environment (optional but recommended):
   ```bash
   python -m venv venv
   source venv/bin/activate   # On Linux/Mac
   venv\Scripts\activate      # On Windows
   ```

3. Install dependencies:
   ```bash
   pip install -r requirements.txt
   ```

---

##  Dataset
- The dataset consists of **images of 70 dog breeds**.  
- Images are resized to **224×224** before feeding into the model.  
- Data is split into **training, validation, and test sets**.

---

##  Model
- **Base Model:** ResNet50 (pretrained on ImageNet)  
- **Architecture Modifications:**  
  - Global Average Pooling  
  - Dense(256, ReLU) + Dropout(0.5)  
  - Softmax output for 70 classes  

---

##  Results
- Training & validation accuracy plotted during training.
- Final accuracy: **~XX%** (replace with your actual result).
- Confusion matrix & classification report included in notebooks.

---

## 🎮 Usage

### Run the Streamlit App
```bash
streamlit run App.py
```

1. Upload a dog image.
2. The model predicts the **breed** with probability score.

---

##  Requirements
Main dependencies:
- Python 3.8+
- TensorFlow / Keras
- NumPy
- Streamlit
- Pillow

Full list in `requirements.txt`.


---

##  Contributing
Pull requests are welcome!  
For major changes, please open an issue first to discuss what you’d like to improve.


---

##  Author
**Menna Reda**  
🔗 [LinkedIn](https://www.linkedin.com/in/menna-reda-6048182a3) | 🔗 [GitHub](https://github.com/mennareda123)
