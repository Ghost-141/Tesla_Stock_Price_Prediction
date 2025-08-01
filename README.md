# Tesla Stock Price Prediction

This project predicts the next-day closing price of Tesla stock (TSLA) using various machine learning and deep learning models. It provides a simple API built with FastAPI and a user-friendly interface with Streamlit. 

## Features

-   **Multiple Models**: Supports a variety of ML models (Linear Regression, Random Forest, SVR, Decision Tree, Gradient Boosting) and DL models (LSTM, GRU).
-   **API**: A robust API to get predictions from the models.
-   **UI**: An intuitive user interface to interact with the models and get predictions.

## Project Structure

```
├── feature_scaler.pkl
├── main.py
├── models
│   ├── dl
│   │   ├── tesla_gru.h5
│   │   └── tesla_lstm.h5
│   └── ml
│       ├── tesla_decision_tree.pkl
│       ├── tesla_gradient_boost.pkl
│       ├── tesla_linear_regression.pkl
│       ├── tesla_random_forest.pkl
│       └── tesla_svr.pkl
├── requirements.txt
├── schemas
│   └── request_response.py
├── src
│   ├── dl_models.py
│   └── ml_models.py
├── target_scaler.pkl
└── ui.py
```

## How to Run

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ImtiazAdar/Tesla-Stock-Price-Prediction.git
    cd Tesla-Stock-Price-Prediction
    ```

2.  **Install the dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the API:**

    ```bash
    uvicorn main:app --reload
    ```

4.  **Run the UI:**

    ```bash
    streamlit run ui.py
    ```

## API Endpoint

-   **POST** `/ml/predict`
    -   **Request Body:**
        ```json
        {
          "model": "random_forest",
          "features": [260.0, 265.0, 258.0, 262.0]
        }
        ```
    -   **Response:**
        ```json
        {
          "model_used": "random_forest",
          "predicted_price": 263.50
        }
        ```

## Models Used

### Machine Learning

-   Linear Regression
-   Random Forest
-   Support Vector Regressor (SVR)
-   Decision Tree
-   Gradient Boosting

### Deep Learning (Sequential) 

-   Long Short-Term Memory (LSTM)
-   Gated Recurrent Unit (GRU)

