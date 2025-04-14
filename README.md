# 🏭 Error Detection in Manufacturing using Deep Learning

This project aims to build a deep learning model to detect errors or defects in manufacturing processes using computer vision techniques. We use TensorFlow and Keras for model training, and scikit-learn, NumPy, and pandas for preprocessing and evaluation.

## 📂 Project Structure

project_root/ │ ├── train_images/ # Folder containing training images │ ├── error/ # Images with defects │ └── normal/ # Images without defects │ ├── model/ # Saved model weights and architecture │ ├── train.py # Script to train the model ├── predict.py # Script to make predictions ├── requirements.txt # Dependencies └── README.md # This file

## 🚀 Getting Started

### 1. Clone the Repository

```bash
git clone https://github.com/your-username/error_maintain_manufacturing.git
cd error_maintain_manufacturing
```

### 2. Install Dependencies

```bash
pip install -r requirements.txt
```

### 3. Dataset Structure
Place your training images inside the train_images/ directory with the following structure:

```css
train_images/
├── error/
│   ├── error1.jpg
│   ├── error2.jpg
│   └── ...
└── normal/
    ├── normal1.jpg
    ├── normal2.jpg
    └── ...
```

### 4. Train the Model
```bash
python train.py
```

The script uses ImageDataGenerator for data augmentation and trains a CNN model using Keras.

### 5. Predict New Images
Use the predict.py script to classify new images:

```bash
python predict.py --image path_to_image.jpg
```
## 🧠 Libraries Used
- TensorFlow / Keras

- Scikit-learn

- NumPy

- Pandas

- Matplotlib (for visualization)

- Pillow (for image processing)

## 🏆 Model Performance
Accuracy, precision, recall, and confusion matrix are printed after training. You can modify the evaluation in train.py.

## 📈 Future Work
- Add more defect classes

- Integrate into real-time camera pipeline

- Use transfer learning (e.g. ResNet, RetuNet, ElasticNet)

## 👨‍💻 Author
- Developed by An from UIT

- Contact: dangthienan1207@gmail.com




