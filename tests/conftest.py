import pytest

import pandas as pd
from app.schemas.request import PredictionRequest
from app.services.prediction_service import PredictionService



@pytest.fixture
def valid_payload():
    return {
        "gender": "male",
        "age": 25,
        "height": 175,
        "weight": 70,
        "duration": 30,
        "heart_rate": 110,
        "body_temp": 37.2,
    }

@pytest.fixture
def prediction_request():
    return PredictionRequest(
        gender="male",
        age=25,
        height=175,
        weight=70,
        duration=30,
        heart_rate=110,
        body_temp=37.2,
    )    
 
@pytest.fixture
def sample_dataframe():
    return pd.DataFrame(
        {
            "User_ID": [1],
            "Gender": ["male"],
            "Age": [25],
            "Height": [175],
            "Weight": [70],
            "Duration": [30],
            "Heart_Rate": [110],
            "Body_Temp": [37.2],
            "Calories": [250],
        }
    )

    