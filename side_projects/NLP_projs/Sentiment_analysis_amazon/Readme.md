# Sentiment Analysis -- Amazon dataset

Amazon gives a platform to small businesses and companies with modest resources to grow larger. And Because of its popularity, people actually spend time and write detailed reviews, about the brand and the product. So, by analyzing that data we can tell companies a lot about their products and also the ways to enhance the quality of the product. But that large amount of data can not be analyzed by a person.

Amazon Product Reviews Sentiment Analysis in Python So here comes the Machine learning part, i.e. Natural Language Processing (NLP) to overcome the problem of large datasets and analyze it. Our task is to predict whether the review given is positive or negative. The real dataset after scraping the website might include millions of reviews. So we preprocessed the data for you,

> Before starting the code, download the dataset by clicking the [link](https://s3.amazonaws.com/amazon-reviews-pds/tsv/amazon_reviews_us_PC_v1_00.tsv.gz).

In this project, I introduced various methods for preprocessing, visualizing and training the nlp data. For the preprocessing, cleaning, I used one the the two proposed methods because the second one takes a long time to clean the data. In the training section, I used three well know models namely SVM, XGboost (Twice), and BERT.

> In case the file named product_review_sa.ipynb is enable to render the notebook. You can access the notebook using this [link](https://colab.research.google.com/drive/13cRZ-0hPVgqy4sVLTV0lxNYAe9ThXpTT#scrollTo=_uhB9ERnmpbZ).


