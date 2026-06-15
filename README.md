
# Shopper Spectrum: Customer Segmentation and Product Recommendations in E-Commerce

## Project Overview

This project focuses on analyzing customer purchasing behavior in an e-commerce environment using transaction-level retail data. The primary goal is to identify meaningful customer segments through RFM (Recency, Frequency, Monetary) analysis and develop an item-based collaborative filtering recommendation system.

The project combines Exploratory Data Analysis (EDA), Customer Segmentation, Product Recommendation, Machine Learning, and Streamlit deployment to generate actionable business insights.

---

## Business Problem

E-commerce businesses generate large volumes of transactional data daily. Understanding customer purchasing behavior and recommending relevant products are critical for:

* Personalized marketing campaigns
* Customer retention strategies
* Inventory optimization
* Product recommendation systems
* Revenue growth initiatives

---
## Dataset link :https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view
## Dataset Information

The dataset contains online retail transaction records including:

* Invoice Number
* Product Code
* Product Description
* Quantity Purchased
* Transaction Date
* Unit Price
* Customer ID
* Customer Country

---

## Project Workflow

### 1. Data Preprocessing

* Handle missing values
* Remove cancelled transactions
* Remove invalid quantities and prices
* Feature engineering

### 2. Exploratory Data Analysis

* Country-wise transaction analysis
* Product popularity analysis
* Revenue trends
* Customer spending analysis
* RFM distribution analysis

### 3. Customer Segmentation

* RFM Feature Creation
* Data Standardization
* K-Means Clustering
* Elbow Method
* Silhouette Score Evaluation
* Cluster Interpretation

### 4. Product Recommendation System

* Customer-Product Matrix
* Cosine Similarity
* Item-Based Collaborative Filtering
* Top Product Recommendations

### 5. Streamlit Application

#### Product Recommendation Module

Input:

* Product Name

Output:

* Top 5 Similar Products

#### Customer Segmentation Module

Input:

* Recency
* Frequency
* Monetary

Output:

* Customer Segment Label

---

## Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* KMeans Clustering
* Cosine Similarity
* Streamlit

---

## Customer Segments

* High-Value Customers
* Regular Customers
* Occasional Customers
* At-Risk Customers

---

## Expected Business Impact

* Better customer targeting
* Improved retention strategies
* Personalized shopping experiences
* Enhanced inventory planning
* Increased revenue opportunities

---

## Future Enhancements

* Hybrid Recommendation Systems
* Real-Time Customer Analytics
* Dynamic Pricing Models
* Advanced Deep Learning Recommenders
