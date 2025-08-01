from pydantic import BaseModel, Field
from typing import List

class MLRequest(BaseModel):
    model: str = Field(..., description="Name of the ML model")
    features: List[float] = Field(..., min_items=4, max_items=4, description="Features: [Open, High, Low, Close]")

class MLPredictionResponse(BaseModel):
    model_used: str
    predicted_price: float
