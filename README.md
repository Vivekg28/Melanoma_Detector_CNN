<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
  <title>Melanoma Cancer Detection using CNN</title>
</head>
<body>

<h1>🧠 Melanoma Cancer Detection using CNN</h1>

<p>This project builds a Convolutional Neural Network (CNN) to classify skin lesion images as <b>Benign</b> or <b>Melanoma</b>.  
It covers data preprocessing, training, evaluation, and a Gradio web app for deployment.</p>

<h2>📌 Features</h2>
<ul>
  <li>Data preprocessing and augmentation</li>
  <li>CNN architecture using TensorFlow/Keras</li>
  <li>Evaluation: Accuracy, Precision, Recall, AUC, Confusion Matrix, ROC Curve</li>
  <li>~88% accuracy on test set</li>
  <li>Gradio-based web interface for real-time predictions</li>
</ul>

<h2>📂 Project Structure</h2>
<pre>
Melanoma-CNN-Detection/
├─ data/                     # dataset
├─ melanoma_model.h5         # trained model
├─ melanoma_cancer_nb.ipynb  # Jupyter Notebook
├─ melanoma_train.py         # training script
├─ melanoma_app.py           # Gradio app
└─ README.html               # this file
</pre>

<h2>⚙️ Installation</h2>
<pre>
git clone https://github.com/yourusername/Melanoma-CNN-Detection.git
cd Melanoma-CNN-Detection
pip install -r requirements.txt
</pre>

<h2>🚀 Usage</h2>
<pre>
# Train model
python melanoma_train.py

# Launch Gradio app
python melanoma_app.py
# Runs at http://127.0.0.1:7861
</pre>

<h2>📊 Model Performance</h2>
<ul>
  <li>Validation Accuracy: ~85%</li>
  <li>Test Accuracy: ~88%</li>
  <li>AUC Score: ~0.94</li>
</ul>

<h2>💡 Future Work</h2>
<ul>
  <li>Transfer Learning (ResNet, EfficientNet, etc.)</li>
  <li>Streamlit/Flask/Cloud Deployment</li>
  <li>Mobile-friendly interface for dermatologists</li>
</ul>

<h2>👨‍💻 Author</h2>
<p><b>Vivek Gautam</b><br>
MSc Data Science @ DAIICT<br>
GitHub: <a href="https://github.com/yourusername">yourusername</a> | 
LinkedIn: <a href="https://linkedin.com/in/yourprofile">yourprofile</a>
</p>

</body>
</html>
