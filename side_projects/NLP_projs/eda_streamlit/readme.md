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

The file **depression_prediction.ipynb** contains the code for image depression prediction using deep learning, online dataset, XAI (Explainable Artificial Intelligence), and deploy it into Streamlit and TensorFlow, you can follow these steps:

Data Collection: Gather a large, diverse, and labeled dataset of facial images representing different levels of depression. Online datasets like the 'AffectNet' or 'FAD' (Facial Affective Dataset) can be used.

Data Preprocessing: Preprocess the images by resizing, normalization, and data augmentation to increase the model's performance and prevent overfitting.

Model Architecture: Use a deep learning model based on Convolutional Neural Networks (CNNs) or Transfer Learning (e.g., VGG16, ResNet, or Inception) for facial expression recognition.

Training: Train the model using the preprocessed dataset and optimize the model's hyperparameters using techniques like Grid Search or Random Search.

Explainability: Implement XAI techniques like GradCAM, SHAP, or LIME to provide insights into the model's decision-making process and improve its interpretability.

Streamlit Integration: Create a user-friendly Streamlit app that allows users to upload facial images, preprocess them, and predict the level of depression using the trained model. Display the XAI visualizations to explain the model's predictions.

## Medical images detection using streamlit and tensorflow

The file **Image_detection.ipynb** contains an example of how to use Streamlit, TensorFlow, and an online medical image dataset to create a deep learning model for medical image detection. I will use the "MedNIST" dataset, a large-scale dataset of labeled clinical images, for this example.

TensorFlow Deployment: Deploy the model and the Streamlit app on TensorFlow using TensorFlow Serving or TensorFlow Hub for easy integration with other applications.

## Code to web scrapping and crawling using streamlit, Flask and Django

The code for web scraping and crawling using Streamlit, you can create a user interface that allows users to input search queries and filter results. 

Web scraping and crawling using Flask & Django, you can create a Django application that utilizes Scrapy for scraping data and integrates it into Django views to return the scraped data as JSON responses.

# Text-to-image web app using streamlit and tensorflow

The following file **text_to_image.ipynb** is for a text-to-image web app using Streamlit and TensorFlow, I've made modifications to the original code to include text input, a text classification model, and a function to generate images based on the classified text. I'm using the InceptionV3 model for text classification.

# NLP methods on cryptocurrency data using streamlit

The following file **NLP_methods_cryptocurrency.ipynb** contains enhancing NLP methods for cryptocurrency data. I will provide some guidance on how to approach this problem using Python.

First, let's gather the necessary data. You can use APIs to collect cryptocurrency data from various sources like CoinMarketCap, CoinGecko, or Binance. For social media data, you can use APIs from platforms like Twitter, Reddit, or Telegram.

Once you have collected the data, preprocess it to make it suitable for NLP tasks. This may include:

Tokenization: Splitting text into words, phrases, or other meaningful elements.
Stopwords removal: Removing common words like 'the', 'is', 'at', etc., that do not carry much meaning.
Lemmatization or stemming: Reducing words to their base or root form.
Removing URLs, numbers, and special characters.
Lowercasing: Convert all text to lowercase for consistency.

# Book summarization using streamlit and tensorflow

The file **book_sum.ipynb** contains a code to summarize a book using Streamlit and TensorFlow, you can create a user-friendly web application that allows users to upload a book, preprocess the text data, and then generate a summary using a trained summarization model. 

# Video summarization using reinforcement learning, GANs and streamlit and tensorflow

The file **video_sum.ipynb** contains an existing code for video summarization using reinforcement learning, GANs, Streamlit, and TensorFlow, we can add a reward system based on user feedback to improve the summarization model over time. 

# Outlier detection using streamlit and tensorflow

The following file **outlier_detect.ipynb** contains the code for outlier detection using Streamlit and TensorFlow, you can create a user-friendly app that allows users to upload a dataset, preprocess the data, train an autoencoder for anomaly detection, and display the results.

# Outlier detection of online price prediction dataset using streamlit and tensorflow

The following file **out_det2.ipynb** contains the code for outlier detection of an online price prediction dataset using Streamlit and TensorFlow, you can create a user-friendly app that allows users to upload their dataset, preprocess the data, and visualize the outliers. 

# Face and age detection using online dataset, streamlit and tensorflow

The file **face_age_detection.ipynb** code for face and age detection using online dataset, Streamlit, and TensorFlow, I would suggest incorporating an age detection model in addition to the existing face detection and verification functionality. You can use the Indico's "age-detection-1" model, which is available in their TensorFlow model library.

# Cars classification and counting using online dataset, streamlit and tensorflow

The following file **cars_class_counting.ipynb** contains code for cars classification and counting using an online dataset, Streamlit, and TensorFlow, I will provide an example of how to build a simple web app that allows users to upload a dataset, train a model for cars classification, and display the trained model's accuracy and confusion matrix using Streamlit and TensorFlow.
