# DeepFake Image Dectector

The DeepFake Image Detector classifies images as real or fake. 
Streamlit Interface is built for users to upload images and see the prediction.

## Dataset:
- Dataset is taken from kaggle : https://www.kaggle.com/datasets/sachchitkunichetty/rvf10k
- This Dataset contains total 10000 images divided into ``train`` and ``valid`` directories.
- The ``train`` directory contains 7000 images further divided into ``fake`` and ``real`` containg 3500 images each.
- The ``valid`` directory contains 3000 images further divided into ``fake`` and ``real`` containing 1500 images each.

## Libraries used:
- Numpy
- Opencv
- Matplotlib
- os

## Preprocessing:
- Created a function Color conversion to convert images from BGR to RGB.
- Used Normalisation to the images to standardize the data.
- Created labels for the training and testing images manually.
- Shuffled the data for better training.
- Resized the images into 128 x 128.

## Model: 
- Convolutional Neural Network (CNN) is built to classify the images.
- This model is trained on 7000 images.
- Used Batch Normalization
- Used Dropout to prevent overfitting.

## Evaluation:
- Accuracy: Achieved accuracy approximately between 81% - 83%.
- Confusion matrix

## Interface:
- Built a streamlit interface.
- Enables uploading of images.
- Predicts whether the image is real or fake.
