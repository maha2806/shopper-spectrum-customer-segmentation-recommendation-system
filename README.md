# 🛒 Shopper Spectrum: Customer Segmentation and Product Recommendation System

## 📌 Project Overview

This project focuses on analyzing customer purchasing behavior in an e-commerce environment. Using transaction data, customers are segmented through RFM (Recency, Frequency, Monetary) analysis and K-Means clustering. Additionally, an item-based collaborative filtering recommendation system is developed to provide personalized product recommendations.

The project helps businesses improve customer retention, targeted marketing, and product recommendation strategies.

---

## 🎯 Business Objective

The primary objective of this project is to identify meaningful customer segments and recommend relevant products based on historical purchasing behavior.

The solution supports:

* Customer Segmentation for targeted marketing
* Personalized Product Recommendations
* Customer Retention Strategies
* Cross-Selling and Upselling Opportunities
* Inventory and Demand Planning

---
## Dataset link :https://drive.google.com/file/d/1rzRwxm_CJxcRzfoo9Ix37A2JTlMummY-/view
 ---

## 📂 Dataset Information

The dataset contains e-commerce transaction records including:

| Column      | Description                |
| ----------- | -------------------------- |
| InvoiceNo   | Transaction Number         |
| StockCode   | Product Code               |
| Description | Product Name               |
| Quantity    | Quantity Purchased         |
| InvoiceDate | Transaction Date           |
| UnitPrice   | Product Price              |
| CustomerID  | Unique Customer Identifier |
| Country     | Customer Country           |

---

## ⚙️ Technologies Used

* Python
* Pandas
* NumPy
* Matplotlib
* Seaborn
* Scikit-Learn
* Streamlit
* K-Means Clustering
* Collaborative Filtering
* Cosine Similarity

---

## 🧹 Data Preprocessing

The following preprocessing steps were performed:

* Removed missing Customer IDs
* Removed cancelled invoices
* Removed negative quantities
* Removed invalid prices
* Removed duplicate records
* Created Revenue feature
* Generated RFM metrics

---

## 📊 Exploratory Data Analysis

EDA was performed to identify:

* Transaction volume by country
* Top-selling products
* Purchase trends over time
* Revenue distribution
* Customer spending behavior
* RFM distributions

---

## 🤖 Customer Segmentation

### RFM Analysis

Customers were segmented using:

* Recency
* Frequency
* Monetary Value

### Clustering Approach

* StandardScaler
* K-Means Clustering
* Elbow Method
* Silhouette Score

### Customer Segments

| Segment    | Description                                   |
| ---------- | --------------------------------------------- |
| High-Value | Frequent, recent, and high-spending customers |
| Regular    | Consistent customers with moderate spending   |
| Occasional | Infrequent customers with lower spending      |
| At-Risk    | Customers inactive for a long period          |

### Model Evaluation

The optimal number of clusters was selected using:

* Elbow Method
* Silhouette Score Analysis

Final Model:

* Algorithm: K-Means
* Number of Clusters: 4
* Silhouette Score: 0.6162

---

## 🎯 Product Recommendation System

An Item-Based Collaborative Filtering approach was implemented using Cosine Similarity.

Features:

* Product similarity calculation
* Top 5 product recommendations
* Recommendation heatmap visualization

---

## 📱 Streamlit Application

### Product Recommendation Module

Users can:

* Select a product
* Generate top 5 similar product recommendations

### Customer Segmentation Module

Users can enter:

* Recency
* Frequency
* Monetary Value

The application predicts the customer segment:

* High-Value
* Regular
* Occasional
* At-Risk

---

## 📁 Repository Structure

Shopper-Spectrum/

├── Shopper_Spectrum.ipynb

├── app.py

├── requirements.txt

├── kmeans_model.pkl

├── scaler.pkl

├── similarity_matrix_small.pkl

├── README.md

├── LICENSE

└── .gitignore

---

## 🚀 Future Improvements

* Hybrid Recommendation System
* Real-Time Customer Analytics
* Deep Learning-Based Recommendations
* Automated Marketing Campaign Suggestions

---

## 👩‍💻 Author

Sita Bharatula

Master of Computer Applications (MCA)

Chandigarh University
