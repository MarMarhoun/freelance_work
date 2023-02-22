# Customer churn prediction using SVM, XGBoost and Random forest models.

## Project description:

Customer churn is a term used when a customer decides to stop using the services of the business. Businesses do customer churn analysis all the time because it is very helpful for a company if they learn which customers are about to leave.

This aim of this project is to train machine learning models on the available data, that will predict a high accuracy which customers are about to churn, which in turn will help the business owner in making useful marketing decisions.

> You can find the original project/challenge details on [Kaggle](https://www.kaggle.com/c/customer-churn-prediction-2020/overview)

## Data description:

### **Context**

"Predict behavior to retain customers. You can analyze all relevant customer data and develop focused customer retention programs." [IBM Sample Data Sets]

### **Content**

Each row represents a customer, each column contains customer’s attributes described on the column Metadata.

The data set includes information about:

Customers who left within the last month – the column is called Churn
Services that each customer has signed up for – phone, multiple lines, internet, online security, online backup, device protection, tech support, and streaming TV and movies
Customer account information – how long they’ve been a customer, contract, payment method, paperless billing, monthly charges, and total charges
Demographic info about customers – gender, age range, and if they have partners and dependents.

### **Columns**

* 'customerID'
* 'gender'
* 'SeniorCitizen' : Whether the customer is a senior citizen or not (1, 0)
* 'Partner' : Whether the customer has a partner or not (Yes, No)
* 'Dependents' : Whether the customer has dependents or not (Yes, No)
* 'tenure': Number of months the customer has stayed with the company
* 'PhoneService': Whether the customer has a phone service or not (Yes, No)
* 'MultipleLines': Whether the customer has multiple lines or not (Yes, No, No phone service)
* 'InternetService': Whether the customer has multiple lines or not (Yes, No, No phone service)
* 'OnlineSecurity': Whether the customer has online security or not (Yes, No, No internet service)
* 'OnlineBackup': Whether the customer has online backup or not (Yes, No, No internet service)
* 'DeviceProtection':Whether the customer has device protection or not (Yes, No, No internet service)
* 'TechSupport': Whether the customer has tech support or not (Yes, No, No internet service)
* 'StreamingTV': Whether the customer has streaming TV or not (Yes, No, No internet service)
* 'StreamingMovies' : Whether the customer has streaming movies or not (Yes, No, No internet service)
* 'Contract': The contract term of the customer (Month-to-month, One year, Two year)
* 'PaperlessBilling': Whether the customer has paperless billing or not (Yes, No)
* 'PaymentMethod': The customer’s payment method (Electronic check, Mailed check, Bank transfer (automatic), Credit card (automatic))
* 'MonthlyCharges': The amount charged to the customer monthly
* 'TotalCharges': The total amount charged to the customer
* 'Churn': Whether the customer churned or not (Yes or No)

