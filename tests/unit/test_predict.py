import pandas as pd
import pytest
from unittest.mock import Mock

from src.models.predict import predict

def test_predict_success():

    X = pd.DataFrame(
        {
            "Age": [25],
            "Height": [175],
        }
    )

    mock_model = Mock()

    mock_model.predict.return_value = [123.45]

    predictions = predict(mock_model, X)

    assert predictions == [123.45]

    mock_model.predict.assert_called_once_with(X)


def test_predict_failure():

    X = pd.DataFrame(
        {
            "Age": [25],
        }
    )

    mock_model = Mock()

    mock_model.predict.side_effect = RuntimeError(
        "Prediction failed"
    )

    with pytest.raises(RuntimeError):
        predict(mock_model, X)
    