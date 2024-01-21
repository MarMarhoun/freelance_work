# Projects using the Streamlit, Gradio & Flask frameworks 

## Basic EDA and the word cloud using streamlit 

The **app.py** file contains a basic EDA and the word cloud using streamlit library.
By running the above code in a Streamlit environment, you can perform basic EDA and visualize word clouds for your custom dataset. Remember to replace 'your_file.csv' with the path to your actual file.


## Projects using the Streamlit, Gradio & Flask frameworks 

The **EDA_streamlit.ipynb** file contains several tasks for various tools but mostly using Streamlit framework.

## Sentiment analysis task using deep learning and the xai for interpretation and deploy it using streamlit, Gradio and tensorflow

The **ml_streamlit.ipynb** file describes how you can train a multiclassification task using PyTorch and then deploy the model using Gradio. First, let's start with training the model. We will use the FashionMNIST dataset, which is a dataset of 60,000 28x28 grayscale images of 10 fashion categories, along with a test set of 10,000 images. We will use a simple convolutional neural network (CNN) architecture for this task. 

## Medical images segmentation using deep learning model and streamlit and TensorFlow

This example demonstrates how to train a deep learning model for medical image segmentation using TensorFlow and the U-Net architecture, and how to deploy it using Streamlit. Note that you may need to adjust the code to fit your specific use case and dataset. Implement a more sophisticated data augmentation pipeline using Albumentations. Use a learning rate scheduler to adjust the learning rate during training. Add a callback to save the best model based on validation loss. Implement a sliding window approach for inference on high-resolution images.

## Web App to deploy a resume parser model using streamlit

The **resume_parser.ipynb** contains a Web App to deploy a resume parser model using streamlit.

To create a web app to deploy a resume parser model using Streamlit, you need to have the following:

A trained resume parser model (e.g., using Named Entity Recognition or Information Extraction techniques)
Streamlit library installed in your Python environment.

## Image depression prediction using deep learning, online dataset, XAI and deploy it into streamlit and tensorflow

The code for image depression prediction using deep learning, online dataset, XAI (Explainable Artificial Intelligence), and deploy it into Streamlit and TensorFlow, you can follow these steps:

Data Collection: Gather a large, diverse, and labeled dataset of facial images representing different levels of depression. Online datasets like the 'AffectNet' or 'FAD' (Facial Affective Dataset) can be used.

Data Preprocessing: Preprocess the images by resizing, normalization, and data augmentation to increase the model's performance and prevent overfitting.

Model Architecture: Use a deep learning model based on Convolutional Neural Networks (CNNs) or Transfer Learning (e.g., VGG16, ResNet, or Inception) for facial expression recognition.

Training: Train the model using the preprocessed dataset and optimize the model's hyperparameters using techniques like Grid Search or Random Search.

Explainability: Implement XAI techniques like GradCAM, SHAP, or LIME to provide insights into the model's decision-making process and improve its interpretability.

Streamlit Integration: Create a user-friendly Streamlit app that allows users to upload facial images, preprocess them, and predict the level of depression using the trained model. Display the XAI visualizations to explain the model's predictions.

TensorFlow Deployment: Deploy the model and the Streamlit app on TensorFlow using TensorFlow Serving or TensorFlow Hub for easy integration with other applications.
