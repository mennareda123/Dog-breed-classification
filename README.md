#  Dog Breed Classification with VGG19

This project is a **Computer Vision application** that classifies dog images into **70 different breeds** using **Transfer Learning with VGG19**.  
It includes data preprocessing, model training, evaluation, and a **Streamlit app** for easy deployment.

---

##  Project Structure
```

├── App.py                 # Streamlit app for deployment
├── dog\_project.keras      # Trained model
├── requirements.txt       # Dependencies
├── data/                  # Dataset (train/valid images)
│   ├── train/
│   └── valid/
└── README.md              # Project documentation

````

---

##   Installation
Clone the repository and install dependencies:

```bash
git clone https://github.com/USERNAME/dog-breed-classification.git
cd dog-breed-classification
pip install -r requirements.txt
````

---

##  Usage

1. Run the Streamlit app:

   ```bash
   streamlit run App.py
   ```
2. Upload a dog image.
3. The app will display the predicted breed from the 70 classes.

---

##  Model Details

* **Base model:** ResNet50 (pretrained on ImageNet)
* **Top layers:** GlobalAveragePooling + Dense(512, ReLU) + Dense(70, Softmax)
* **Loss function:** Categorical Crossentropy
* **Optimizer:** Adam (lr=1e-4)

---

##  Results

* Accuracy improves significantly with data augmentation and fine-tuning.
* The model achieves good generalization on unseen images.

---

##  Future Work

* Add more breeds to the dataset.
* Optimize training with learning rate schedules.
* Deploy the app on **Streamlit Cloud / Hugging Face Spaces**.

---

##  Requirements

* Python 3.8+
* TensorFlow / Keras
* Streamlit
* Pandas, NumPy, Pillow

---

## 👩‍💻 Author

Developed by **Menna Reda**
🔗 [LinkedIn](https://www.linkedin.com/in/menna-reda-6048182a3?utm_source=share&utm_campaign=share_via&utm_content=profile&utm_medium=android_app)
