import streamlit as st
from PIL import Image
import numpy as np
import tensorflow as tf
from tensorflow.keras.models import load_model


MODEL_PATH = "VGG19_github.keras"  
model = load_model(MODEL_PATH)

IMG_SIZE = (224, 224) 

st.title("🍎 Fruit vs Vegetable Classifier")
st.write("Upload an image and the model will predict whether it is a Fruit or a Vegetable.")

uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption='Uploaded Image', use_container_width=True) 

    img = image.resize(IMG_SIZE)
    img_array = np.array(img) / 255.0  # normalize
    img_array = np.expand_dims(img_array, axis=0)  # batch dimension

    # prediction
    prediction = model.predict(img_array)
    if prediction[0][0] > 0.5:
        st.success("🟢 Prediction: Vegetable")
    else:
        st.success("🟢 Prediction: Fruit")
