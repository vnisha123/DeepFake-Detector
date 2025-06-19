# DeepFake-Detector

This project detects whether an image is real or fake (deepfake) using a Convolutional Neural Network (CNN) model. It includes a simple user interface made with Streamlit where users can upload an image and see the prediction.

- Deepfake image classification using CNN
- Streamlit web app for testing images
- Model trained on a dataset of 7000 images resized to 128x128
- Predicts in real-time if an image is "Real" or "Fake"

### 🛠️ What I Did
- **Preprocessing**: Read images, checked sizes, counted them using custom functions and `collections.Counter`.
- **Color Conversion**: Converted BGR to RGB for compatibility with CNNs.
- **Labeling**: Assigned labels manually.
- **Normalization**: For better computation.
- **Shuffling**: Used `zip()` to shuffle images + labels without losing alignment.
- **Resizing**: Resized images to 128×128 because converting full sets to NumPy crashed Kaggle kernels.
- **Modeling**: Trained a CNN (achieved ~76% accuracy).
- **Tried Alternatives**: MobileNet, ResNet (performed worse).
- **Tuning**: Added more CNN layers. Set random seed to get consistent results.

---

### 🐛 Challenges I Faced
- Kernel crashing on NumPy conversion → fixed by resizing images.
- Path variable in quotes caused string iteration → fixed using `os.listdir()`.
- TensorFlow version mismatch with Python (v3.12.0 not supported by TF 2.19) → created virtual environment with Python 3.11.6 → realized Kaggle used TF 2.18, finally installed matching version.
