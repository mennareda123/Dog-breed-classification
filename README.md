```markdown
#  Dog Breed Classification with ResNet50

This project is a **Computer Vision application** that classifies dog images into **70 different dog breeds** using **Transfer Learning with ResNet50**.  
It covers **data preprocessing, model training, evaluation, and deployment** with a user-friendly **Streamlit app**.

---

##  Project Structure
```
├── App.py               # Streamlit app for deployment
├── dog_project.keras    # Trained ResNet50 model
├── data/                # Dataset (train/valid images)
│   ├── train/
│   └── valid/
└── README.md            # Project documentation
```

---

##  How to Use

1. Run the Streamlit app:

   ```bash
   streamlit run App.py
   ```

2. Upload a dog image.  
3. The app will instantly predict the breed from the **70 available classes**.

---

##  Model Details

- **Base model:** ResNet50 (pretrained on ImageNet)  
- **Top layers:** GlobalAveragePooling → Dense(512, ReLU) → Dense(70, Softmax)  
- **Loss function:** Categorical Crossentropy  
- **Optimizer:** Adam (learning rate = 1e-4)  

---

##  Results

- With **data augmentation** and fine-tuning, the model improves accuracy significantly.  
- The ResNet50 backbone helps achieve **robust generalization** on unseen dog images.  

---

##  Future Improvements

- Add more breeds for even broader classification.  
- Use learning rate schedules for faster convergence.  
- Deploy the app on **Streamlit Cloud** or **Hugging Face Spaces** for public access.  

---

##  Author

Developed by **Menna Reda**  
🔗 [LinkedIn](https://www.linkedin.com/in/menna-reda-6048182a3)  
```
