import pandas as pd
import pytest
from unittest.mock import patch

from src.pipelines.predict_pipeline import run_prediction_pipeline

@patch("src.pipelines.predict_pipeline.predict")
@patch("src.pipelines.predict_pipeline.preprocess_input")
@patch("src.pipelines.predict_pipeline.load_model")
def test_prediction_pipeline_success(
    mock_load_model,
    mock_preprocess_input,
    mock_predict,
):
    input_data = pd.DataFrame({
        "Gender": ["male"],
        "Age": [25],
        "Height": [175],
        "Weight": [70],
        "Duration": [30],
        "Heart_Rate": [110],
        "Body_Temp": [37.2],
    })

    processed_data = pd.DataFrame({"processed": [1]})

    mock_load_model.return_value = "mock_model"
    mock_preprocess_input.return_value = processed_data
    mock_predict.return_value = [123.45]

    prediction = run_prediction_pipeline(input_data)

    assert prediction == [123.45]

    mock_load_model.assert_called_once_with("xgb_model.pkl")
    mock_preprocess_input.assert_called_once_with(input_data)
    mock_predict.assert_called_once_with(
        "mock_model",
        processed_data,
    )
    
@patch("src.pipelines.predict_pipeline.load_model")
def test_pipeline_load_model_failure(mock_load_model):

    input_data = pd.DataFrame()

    mock_load_model.side_effect = FileNotFoundError("Model not found")

    with pytest.raises(FileNotFoundError):
        run_prediction_pipeline(input_data)
        
@patch("src.pipelines.predict_pipeline.preprocess_input")
@patch("src.pipelines.predict_pipeline.load_model")
def test_pipeline_preprocessing_failure(
    mock_load_model,
    mock_preprocess_input,
):

    input_data = pd.DataFrame()

    mock_load_model.return_value = "mock_model"
    mock_preprocess_input.side_effect = ValueError(
        "Preprocessing failed"
    )

    with pytest.raises(ValueError):
        run_prediction_pipeline(input_data)
        
@patch("src.pipelines.predict_pipeline.predict")
@patch("src.pipelines.predict_pipeline.preprocess_input")
@patch("src.pipelines.predict_pipeline.load_model")
def test_pipeline_prediction_failure(
    mock_load_model,
    mock_preprocess_input,
    mock_predict,
):

    input_data = pd.DataFrame()

    mock_load_model.return_value = "mock_model"
    mock_preprocess_input.return_value = input_data
    mock_predict.side_effect = RuntimeError(
        "Prediction failed"
    )

    with pytest.raises(RuntimeError):
        run_prediction_pipeline(input_data)                    