# 🐶 Dog Breed Classification with ResNet50

This project is a **Computer Vision application** that classifies dog images into **70 different breeds** using **Transfer Learning with ResNet50**.  
It includes data preprocessing, model training, evaluation, and a **Streamlit app** for easy deployment.

---

## 📂 Project Structure
├── App.py # Streamlit app for deployment
├── dog_project.keras # Trained model
├── data/ # Dataset (train/valid images)
│ ├── train/
│ └── valid/
└── README.md # Project documentation

yaml
Copy code

---

## 🚀 Usage

1. Run the Streamlit app:
   ```bash
   streamlit run App.py
Upload a dog image.

The app will display the predicted breed from the 70 classes.

🧠 Model Details
Base model: ResNet50 (pretrained on ImageNet)

Top layers: GlobalAveragePooling + Dense(512, ReLU) + Dense(70, Softmax)

Loss function: Categorical Crossentropy

Optimizer: Adam (lr=1e-4)

📊 Results
Accuracy improves significantly with data augmentation and fine-tuning.

The model achieves good generalization on unseen images.

🔮 Future Work
Add more breeds to the dataset.

Optimize training with learning rate schedules.

Deploy the app on Streamlit Cloud / Hugging Face Spaces.

👩‍💻 Author
Developed by Menna Reda
🔗 LinkedIn