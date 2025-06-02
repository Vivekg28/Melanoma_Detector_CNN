import gradio as gr
import numpy as np
import cv2
from tensorflow.keras.models import load_model

# Load the trained model
from keras.models import load_model
model = load_model("melanoma_model.h5", compile=False)

img_size = (128, 128)

def predict(image):
    # Resize and preprocess
    img = cv2.resize(image, img_size)
    img = img.astype("float32") / 255.0
    img = np.expand_dims(img, axis=0)

    # Predict
    prediction = model.predict(img)[0][0]
    confidence = prediction * 100

    if prediction >= 0.5:
        label = "🧠 Prediction: Melanoma (Cancer)"
        confidence_display = confidence
    else:
        label = "🧠 Prediction: Benign (Non-Cancer)"
        confidence_display = 100 - confidence

    return f"{label}\n📊 Detection Likelihood: {confidence_display:.2f}%"

# Gradio Interface
demo = gr.Interface(
    fn=predict,
    inputs=gr.Image(type="numpy", label="Upload Skin Image"),
    outputs=gr.Textbox(label="Prediction Result"),
    title="Melanoma Cancer Detection",
    description="Upload a skin lesion image. The model predicts whether it's Melanoma (cancer) or Benign (non-cancer), with confidence."
)

if __name__ == "__main__":
    demo.launch()
