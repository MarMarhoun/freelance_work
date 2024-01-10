'''
python -m venv venv
source venv/bin/activate
pip install streamlit
'''
# pip install pandas sklearn numpy matplotlib seaborn nltk wordcloud streamlit

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from nltk.corpus import stopwords
from wordcloud import WordCloud
import streamlit as st
from sklearn.feature_extraction._stop_words import ENGLISH_STOP_WORDS

# Uploading and Reading the Custom Dataset:

uploaded_file = st.file_uploader("Choose a custom dataset...", type=["csv", "txt"])

if uploaded_file is not None:
    # For csv file
    if uploaded_file.name.endswith('.csv'):
        df = pd.read_csv(uploaded_file)

    # For txt file
    elif uploaded_file.name.endswith('.txt'):
        df = pd.read_csv(uploaded_file, sep="\t")

    # For other types of files
    else:
        st.write("Unsupported File Format. Please upload a csv or txt file.")


# Basic Exploratory Data Analysis (EDA):

if st.button("Perform Basic EDA"):
    st.write("Number of Rows and Columns: ", df.shape)

    st.write("Column Names: ", df.columns)

    st.write("First 5 Rows of the Dataset:")
    st.write(df.head())

    st.write("Summary Statistics:")
    st.write(df.describe())

    st.write("Number of Missing Values in Each Column:")
    st.write(df.isnull().sum())

# Visualizing the Correlation Matrix:

if st.button("Visualize Correlation Matrix"):
    plt.figure(figsize=(12, 10))
    sns.heatmap(df.corr(), annot=True, cmap='coolwarm')
    st.pyplot(plt)

# Creating a Word Cloud for a Text Column:

st.write("Word Cloud for a Text Column:")
text_column = st.selectbox("Select a text column for word cloud:", df.columns)

if text_column:
    text = ' '.join(df[text_column].dropna().tolist())
    stopwords = set(ENGLISH_STOP_WORDS)

    wc = WordCloud(background_color='white', max_words=200, stopwords=stopwords)
    wc.generate(text)

    plt.figure(figsize=(10, 5))
    plt.imshow(wc, interpolation='bilinear')
    plt.axis('off')
    st.pyplot(plt)

# Plotting the Distribution of a Variable:

st.write("Distribution of a Variable:")
variable = st.selectbox("Select a variable for distribution plot:", df.columns)

if variable:
    st.write(df[variable].value_counts(normalize=True))

    plt.figure(figsize=(12, 6))
    sns.countplot(x=variable, data=df)
    st.pyplot(plt)

