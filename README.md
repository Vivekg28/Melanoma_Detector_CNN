<!DOCTYPE html>
<html lang="en">
<head>
  <meta charset="UTF-8">
</head>
<body>

<h1>🧠 Melanoma Cancer Detection using CNN</h1>

<h2>📖 Introduction</h2>
<p>
Melanoma is one of the most aggressive forms of skin cancer, and <b>early detection is critical</b> for improving survival rates. 
This project develops a <b>Convolutional Neural Network (CNN)</b> model to classify skin lesion images as 
<b>Benign (non-cancerous)</b> or <b>Melanoma (cancerous)</b>.
</p>

<p>The project includes:</p>
<ul>
  <li>Data preprocessing and augmentation</li>
  <li>Model training with CNN</li>
  <li>Evaluation using multiple metrics</li>
  <li>Deployment using a Gradio web interface</li>
</ul>

<hr>

<h2>🎯 Model Objective — Prioritizing Recall while Handling Precision</h2>
<p>
In medical diagnosis tasks, <b>Recall (Sensitivity)</b> is often more important than Precision.
</p>
<ul>
  <li><b>High Recall</b> ensures most melanoma cases are detected (minimizing false negatives).</li>
  <li><b>Precision</b> ensures predictions are reliable (minimizing false positives).</li>
</ul>

<p>
Our model is tuned to <b>maximize Recall without severely compromising Precision</b>, because:
</p>
<ul>
  <li>Missing a melanoma case (false negative) can be life-threatening.</li>
  <li>High Recall ensures fewer undetected cancerous cases, even if some benign cases are flagged incorrectly.</li>
</ul>

<hr>

<h2>💡 Future Work</h2>
<ul>
  <li>⚡ <b>Transfer Learning</b>: Use ResNet, EfficientNet for better accuracy.</li>
  <li>📈 <b>Threshold Tuning</b>: Adjust thresholds for better Precision-Recall trade-off.</li>
  <li>🧪 <b>Explainability</b>: Integrate Grad-CAM / SHAP for interpretability.</li>
  <li>🌐 <b>Deployment</b>: Extend Gradio app into Streamlit/Flask for production use.</li>
  <li>📱 <b>Mobile App</b>: Lightweight mobile integration for dermatologists and patients.</li>
</ul>

<hr>

<h2>👨‍💻 Author</h2>
<p>
<b>Vivek Gautam</b><br>
MSc Data Science @ DAIICT<br>
</p>

</body>
</html>
