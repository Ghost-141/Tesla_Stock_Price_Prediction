# Tesla Stock Price Prediction

This project predicts the next-day closing price of Tesla stock (TSLA) using various machine learning and deep learning models. It provides a simple API built with FastAPI and a user-friendly interface with Streamlit. 

## Features

-   **Multiple Models**: Supports a variety of ML models (Linear Regression, Random Forest, SVR, Decision Tree, Gradient Boosting).
-   **API**: A robust API to get predictions from the models.
-   **UI**: An intuitive user interface to interact with the models and get predictions.

## Project Structure
```
├── data/
│   ├── Scaler/
│   │   ├── feature_scaler.pkl
│   │   └── targer_scaler.pkl
│   └── Tesla 2024 Stock Data/
│       └── tesla_sotck_price_2024.csv
├── models/
│   └── ml/
│       ├── tesla_dt.pkl
│       ├── tesla_gb.pkl
│       ├── tesla_linear.pkl
│       ├── tesla_rf.pkl
│       └── tesla_svm.pkl
├── schemas/
│   └── request_response.py
├── src/
│   ├── api.py
│   ├── ml_models.py
│   └── ui.py
├── main.py
├── README.md
└── requirements.txt
```

## Setup

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/ImtiazAdar/Tesla-Stock-Price-Prediction.git
    cd Tesla-Stock-Price-Prediction
    ```

2.  **Install the dependencies:**

    1. Using `Anaconda`:

    ```bash
    conda create -n tesla_stock python=3.10
    conda activate tesla_stock
    pip install -r requirements.txt 
    ```

    2. Using `pip`:

    ```bash
    python3.10 -m venv tesla_stock
    tesla_stock\Scripts\activate #for windows
    source tesla_stock/bin/activate #for mac/linux
    pip install -r requirements.txt
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

## How to Use:

To test the model for prediction follow the following steps to run the api and the ui to interact with the model easily:

The [main.py](./main.py) includes both the `api.py` and `ui.py` files. To run both of them you only need to run the `main.py` file and it will redirect you to the api docs and ui page.

Use the [tesla_sotck_price_2024.csv](./data/Tesla%202024%20Stock%20Data/tesla_sotck_price_2024.csv) file to test the model.

## Models Used

The following machine learning model has been used in this project:

-   Linear Regression
-   Random Forest
-   Support Vector Regressor (SVR)
-   Decision Tree
-   Gradient Boosting
