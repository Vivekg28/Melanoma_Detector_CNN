<!doctype html>
<html lang="en">
<head>
  <meta charset="utf-8" />
  <meta name="viewport" content="width=device-width,initial-scale=1" />
  <title>Melanoma Cancer Detection using CNN — README</title>
  <style>
    :root{
      --bg:#0f1724; --card:#0b1220; --muted:#98a0b3; --accent:#4f46e5; --glass: rgba(255,255,255,0.03);
      --mono: 'Courier New', monospace;
    }
    body{
      margin:0; font-family: Inter, system-ui, -apple-system, "Segoe UI", Roboto, "Helvetica Neue", Arial;
      background: linear-gradient(180deg,#071028 0%, #071827 100%); color:#e6eef8; line-height:1.6;
      padding:32px;
    }
    .container{max-width:980px; margin:0 auto;}
    header{display:flex; gap:16px; align-items:center; margin-bottom:22px;}
    .logo{
      width:64px; height:64px; border-radius:12px; display:grid; place-items:center;
      background:linear-gradient(135deg,var(--accent), #06b6d4); font-weight:700; color:white;
      box-shadow:0 6px 20px rgba(79,70,229,0.18);
    }
    h1{margin:0; font-size:1.6rem;}
    p.lead{color:var(--muted); margin-top:8px;}
    .card{background:var(--card); border-radius:12px; padding:20px; box-shadow:0 8px 30px rgba(2,6,23,0.6); margin-bottom:18px;}
    pre{background:var(--glass); padding:12px; border-radius:8px; overflow:auto; color:#dfefff; font-family:var(--mono); font-size:0.95rem;}
    code{background:rgba(255,255,255,0.02); padding:2px 6px; border-radius:6px;}
    ul{margin-top:8px;}
    .badge{display:inline-block; padding:6px 10px; border-radius:999px; background:rgba(255,255,255,0.03); color:var(--muted); font-size:0.85rem;}
    .grid{display:grid; grid-template-columns:1fr 1fr; gap:12px;}
    .full{grid-column:1/-1;}
    a { color: #9fc9ff; text-decoration:none; }
    footer{color:var(--muted); font-size:0.9rem; margin-top:18px;}
    @media (max-width:720px){ .grid{grid-template-columns:1fr} header{gap:12px} }
  </style>
</head>
<body>
  <div class="container">
    <header>
      <div class="logo">MC</div>
      <div>
        <h1>Melanoma Cancer Detection using CNN</h1>
        <p class="lead">A Convolutional Neural Network to classify skin lesion images as <strong>Benign</strong> or <strong>Melanoma</strong>. Includes preprocessing, training, evaluation and a Gradio demo.</p>
      </div>
    </header>

    <section class="card">
      <h2>Features</h2>
      <ul>
        <li>Data preprocessing & augmentation using <code>ImageDataGenerator</code>.</li>
        <li>Custom CNN implemented with <code>TensorFlow / Keras</code>.</li>
        <li>Evaluation metrics: Accuracy, Precision, Recall, AUC, Confusion Matrix & ROC Curve.</li>
        <li>Gradio-based web interface for live predictions.</li>
      </ul>
    </section>

    <section class="card">
      <h2>Project Structure</h2>
      <pre>
Melanoma-CNN-Detection/
├─ data/                     # dataset split into train/val/test
├─ melanoma_model.h5         # trained model
├─ melanoma_cancer_nb.ipynb  # Jupyter Notebook (training + eval)
├─ melanoma_train.py         # optional training script
├─ melanoma_app.py           # Gradio web app script
└─ README.html               # this file
      </pre>
    </section>

    <section class="card grid">
      <div>
        <h3>Quick Install</h3>
        <pre>
git clone https://github.com/yourusername/Melanoma-CNN-Detection.git
cd Melanoma-CNN-Detection
pip install -r requirements.txt
        </pre>
      </div>

      <div>
        <h3>Recommended Packages</h3>
        <ul>
          <li>python >= 3.8</li>
          <li>tensorflow</li>
          <li>numpy, pandas, matplotlib, seaborn</li>
          <li>scikit-learn, opencv-python</li>
          <li>gradio (for web demo)</li>
        </ul>
      </div>

      <div class="full">
        <h3>Usage</h3>
        <pre>
# train (if you have training script)
python melanoma_train.py

# or open and run the notebook
jupyter notebook melanoma_cancer_nb.ipynb

# launch the Gradio app (local demo)
python melanoma_app.py
# default local URL: http://127.0.0.1:7861
        </pre>
      </div>
    </section>

    <section class="card">
      <h2>Model Performance (example)</h2>
      <ul>
        <li><strong>Validation accuracy:</strong> ≈ 85%</li>
        <li><strong>Test accuracy:</strong> ≈ 88%</li>
        <li><strong>Test AUC:</strong> ≈ 0.94</li>
      </ul>
      <p class="badge">Results depend on dataset split & training configuration — your values may vary.</p>
    </section>

    <section class="card">
      <h2>Notes & Suggestions (Future Work)</h2>
      <ul>
        <li>Use transfer learning (ResNet / EfficientNet) to boost accuracy.</li>
        <li>Experiment with focal loss or class balancing if dataset is imbalanced.</li>
        <li>Deploy to cloud (Heroku/GCP/AWS) or convert model to TF SavedModel / TensorFlow Serving.</li>
        <li>Add unit tests and CI (GitHub Actions) for reproducibility.</li>
      </ul>
    </section>

    <section class="card">
      <h2>Author</h2>
      <p><strong>Vivek Gautam</strong><br/>
        MSc Data Science — DAIICT<br/>
        GitHub: <a href="https://github.com/yourusername" target="_blank" rel="noopener">yourusername</a> • LinkedIn: <a href="https://linkedin.com/in/yourprofile" target="_blank" rel="noopener">yourprofile</a>
      </p>
    </section>

    <footer>
      <p>© <span id="year"></span> Melanoma CNN — For educational/demo purposes only. Not a medical diagnostic tool.</p>
    </footer>
  </div>

  <script>
    document.getElementById('year').innerText = new Date().getFullYear();
  </script>
</body>
</html>
