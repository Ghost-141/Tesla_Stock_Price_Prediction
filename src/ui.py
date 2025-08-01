import streamlit as st
import requests

def run_ui():

    st.set_page_config(page_title="Tesla Stock Price Predictor", layout="centered")

    st.title("Tesla Stock Price Predictor Using (ML Models)")
    st.markdown("Use machine learning models to predict the **next day's closing price** based on today's OHLC data.")

    st.subheader("Choose a Machine Learning Model")
    model = st.selectbox(
        "Select model for prediction",
        options=[
            "linear_regression",
            "random_forest",
            "svr",
            "decision_tree",
            "gradient_boost"
        ]
    )

    st.subheader("Input following information of previous day's market")

    col1, col2 = st.columns(2)
    with col1:
        open_val = st.text_input("Open Price", placeholder="e.g., 260.00")
        low_val = st.text_input("Low Price", placeholder="e.g., 258.00")

    with col2:
        high_val = st.text_input("High Price", placeholder="e.g., 265.00")
        close_val = st.text_input("Close Price", placeholder="e.g., 262.00")

    if st.button("Predict Next Day's Price"):
        payload = {
            "model": model,
            "features": [open_val, high_val, low_val, close_val]
        }

        try:
            response = requests.post("http://127.0.0.1:8000/ml/predict", json=payload)

            if response.status_code == 200:
                result = response.json()
                st.success(f"Predicted Close Price: **${result['predicted_price']}**")
                st.info(f"Model Used: `{result['model_used']}`")
            else:
                st.error(f"API Error: {response.json().get('detail', 'Unknown error')}")
        except Exception as e:
            st.error(f"Failed to connect to API: {e}")
run_ui()            