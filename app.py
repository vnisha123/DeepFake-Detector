import streamlit as st
import numpy as np
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing.image import img_to_array, load_img
import cv2


model = load_model("deepfake_model.keras")


st.title("🧠 Deepfake Image Detector")
st.write("Upload an image and the model will predict whether it's **Real** or **Fake**.")


uploaded_file = st.file_uploader("Choose an image...", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    
    st.image(uploaded_file, caption="Uploaded Image", use_container_width=True)

    
    image = load_img(uploaded_file, target_size=(128, 128))
    image = img_to_array(image)
    image = image / 255.0
    image = np.expand_dims(image, axis=0)

    
    prediction = model.predict(image)[0][0]

    
    if prediction >= 0.5:
        st.error("🔴 Prediction: **Fake**")
    else:
        st.success("🟢 Prediction: **Real**")

    st.write(f"Confidence Score: `{prediction:.4f}`")
