import streamlit as st
from tensorflow.keras.models import load_model
from tensorflow.keras.preprocessing import image
import numpy as np
from PIL import Image

# Load model
model = load_model("melanoma_model.h5")
img_size = (128, 128)

# Prediction function
def predict_melanoma(img):
    img = img.resize(img_size)
    img_array = image.img_to_array(img) / 255.0
    img_array = np.expand_dims(img_array, axis=0)
    prediction = model.predict(img_array)[0][0]
    label = "Melanoma" if prediction >= 0.5 else "Benign"
    return label, prediction

# Streamlit UI
st.title("Melanoma Cancer Detection")

uploaded_file = st.file_uploader("Upload a skin lesion image", type=["jpg", "png", "jpeg"])
if uploaded_file:
    img = Image.open(uploaded_file)
    st.image(img, caption='Uploaded Image', use_column_width=True)
    
    label, confidence = predict_melanoma(img)
    st.write(f"**Prediction:** {label}")
    st.write(f"**Confidence:** {confidence:.2f}")