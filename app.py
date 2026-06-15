import streamlit as st
import pandas as pd
import pickle

# ==========================

# PAGE CONFIGURATION

# ==========================

st.set_page_config(
page_title="Shopper Spectrum",
page_icon="🛒",
layout="wide"
)

# ==========================

# LOAD MODELS

# ==========================

@st.cache_resource
def load_models():
    kmeans = pickle.load(open("kmeans_model.pkl", "rb"))
    scaler = pickle.load(open("scaler.pkl", "rb"))
    similarity_df = pickle.load(open("similarity_matrix_small.pkl", "rb"))

    return kmeans, scaler, similarity_df
# ==========================

# SIDEBAR

# ==========================

st.sidebar.title("Navigation")

page = st.sidebar.radio(
"Choose Module",
[
"Home",
"Customer Segmentation",
"Product Recommendation"
]
)

# ==========================

# HOME PAGE

# ==========================

if page == "Home":

```
st.title("🛒 Shopper Spectrum")

st.markdown("""
### Customer Segmentation and Product Recommendation System

This application helps businesses:

- Identify customer segments using RFM Analysis and K-Means Clustering
- Generate personalized product recommendations using Collaborative Filtering
- Support customer retention and targeted marketing strategies

---
""")

col1, col2 = st.columns(2)

with col1:
    st.info("""
    ### 👥 Customer Segmentation

    Enter:

    - Recency
    - Frequency
    - Monetary Value

    Predict customer segment:
    - High-Value
    - Regular
    - Occasional
    - At-Risk
    """)

with col2:
    st.success("""
    ### 🎯 Product Recommendation

    Select a product and get:

    - Top 5 Similar Products
    - Personalized Product Suggestions
    - Cross-Selling Opportunities
    """)
```

# ==========================

# CUSTOMER SEGMENTATION

# ==========================

elif page == "Customer Segmentation":

```
st.title("👥 Customer Segmentation")

st.write("Enter customer RFM values.")

recency = st.number_input(
    "Recency (Days)",
    min_value=0.0,
    value=30.0
)

frequency = st.number_input(
    "Frequency",
    min_value=0.0,
    value=5.0
)

monetary = st.number_input(
    "Monetary Value",
    min_value=0.0,
    value=1000.0
)

if st.button("Predict Segment"):

    data = [[recency, frequency, monetary]]

    scaled_data = scaler.transform(data)

    cluster = kmeans.predict(scaled_data)[0]

    segment_mapping = {
        0: "Occasional",
        1: "At-Risk",
        2: "High-Value",
        3: "Regular"
    }

    segment = segment_mapping.get(cluster)

    st.success(f"Predicted Customer Segment: {segment}")
```

# ==========================

# PRODUCT RECOMMENDATION

# ==========================

elif page == "Product Recommendation":

```
st.title("🎯 Product Recommendation System")

product = st.selectbox(
    "Select Product",
    similarity_df.columns
)

if st.button("Get Recommendations"):

    recommendations = (
        similarity_df[product]
        .sort_values(ascending=False)
        .iloc[1:6]
    )

    st.success("Top 5 Recommended Products")

    for i, item in enumerate(recommendations.index, start=1):
        st.write(f"{i}. {item}")

    st.balloons()
```

# ==========================

# FOOTER

# ==========================

st.markdown("---")
st.caption(
"Developed by Sita Bharatula | MCA | Chandigarh University"
)
