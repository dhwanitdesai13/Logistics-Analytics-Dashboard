# predictor.py
from sklearn.ensemble import RandomForestRegressor
import pandas as pd

class DelayPredictor:
    def __init__(self, historical):
        self.model = RandomForestRegressor(n_estimators=100)
        X = historical[['Distance_KM', 'weight_kg', 'traffic_index', 'hour', 'is_rain', 'priority_encoded']].fillna(0)
        y = historical['delay_min'].clip(0).fillna(0)
        self.model.fit(X, y)
        self.priority_map = {'Economy': 0, 'Standard': 1, 'Express': 2}

    def predict_batch(self, orders):
        X = orders.copy()
        X['hour'] = X['Order_Date'].dt.hour
        X['priority_encoded'] = X['Priority'].map(self.priority_map)
        X['traffic_index'] = X['Traffic_Delay_Minutes'] / (X['Distance_KM'] / 50 * 60)
        X['is_rain'] = X['Weather_Impact'].str.contains('Rain', na=False).astype(int)
        X['delay_risk_score'] = self.model.predict(X[['Distance_KM', 'weight_kg', 'traffic_index', 'hour', 'is_rain', 'priority_encoded']].fillna(0))
        X['delay_risk_score'] = (X['delay_risk_score'] - X['delay_risk_score'].min()) / (X['delay_risk_score'].max() - X['delay_risk_score'].min() + 1e-6) * 100
        return X