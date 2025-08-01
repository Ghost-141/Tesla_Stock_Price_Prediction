import pandas as pd
import joblib
from schemas.request_response import MLRequest, MLPredictionResponse

models = {
    "linear_regression": joblib.load("./models/ml/tesla_linear.pkl"),
    "random_forest":joblib.load("./models/ml/tesla_rf.pkl"),
    "svr":joblib.load("./models/ml/tesla_svm.pkl"),
    "decision_tree":joblib.load("./models/ml/tesla_dt.pkl"),
    "gradient_boost":joblib.load("./models/ml/tesla_gb.pkl")
}

feature_scaler = joblib.load("./data/Scaler/feature_scaler.pkl")
target_scaler = joblib.load("./data/Scaler/target_scaler.pkl")

def predict_single_day_price(model, single_day_input_raw, feat_scale, tg_scale):
    feature_names = ["Open", "High", "Low", "Close"]
    input_df = pd.DataFrame([single_day_input_raw], columns=feature_names)
    input_scaled = feat_scale.transform(input_df)
    pred_scaled = model.predict(input_scaled)
    pred_price = tg_scale.inverse_transform(pred_scaled.reshape(-1, 1))[0, 0]
    return pred_price

def ml_model_predict(data: MLRequest) -> MLPredictionResponse:
    if data.model not in models:
        raise ValueError(f"Model '{data.model}' not available.")
    
    pred_price = predict_single_day_price(models[data.model], 
                                          single_day_input_raw=data.features,
                                          feat_scale=feature_scaler,
                                          tg_scale=target_scaler)
    
    return MLPredictionResponse(model_used=data.model, predicted_price=round(pred_price, 2))
