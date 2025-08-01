from fastapi import FastAPI, HTTPException
from typing import Any
from fastapi.responses import RedirectResponse
from schemas.request_response import MLRequest, MLPredictionResponse
from src.ml_models import ml_model_predict

app = FastAPI(
    title="Tesla Stock Price Prediction with different ML & DL Models",
    description="Predict next-day Tesla stock price using selected ML model and OHLC data.",
    version="1.0.0"
)

def run_api():
    
    @app.get("/")
    def redirect_to_docs():
        return RedirectResponse(url="/docs")
    
    @app.post("/ml/predict", response_model=MLPredictionResponse)
    def predict_stock_price(data: MLRequest) -> Any:
        """
        Predict next-day Tesla stock price using an ML model and input features [Open, High, Low, Close]
        """
        try:
            result = ml_model_predict(data)
            return result
        except ValueError as ve:
            raise HTTPException(status_code=400, detail=str(ve))
        except Exception as e:
            raise HTTPException(status_code=500, detail=f"Prediction failed: {str(e)}")

run_api()