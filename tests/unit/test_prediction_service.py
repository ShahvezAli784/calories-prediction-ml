import pytest

from unittest.mock import patch

from app.schemas.request import PredictionRequest
from app.services.prediction_service import PredictionService


def test_predict_returns_float(prediction_request):

    request = prediction_request

    with patch(
        "app.services.prediction_service.run_prediction_pipeline"
    ) as mock_pipeline:

        mock_pipeline.return_value = [123.45]

        service = PredictionService()

        prediction = service.predict(request)

        assert isinstance(prediction, float)
        assert prediction == 123.45
 

def test_prediction_pipeline_called_once(prediction_request):

    request = prediction_request

    with patch(
        "app.services.prediction_service.run_prediction_pipeline"
    ) as mock_pipeline:

        mock_pipeline.return_value = [100]

        service = PredictionService()

        service.predict(request)

        mock_pipeline.assert_called_once()        

from unittest.mock import patch

from app.schemas.request import PredictionRequest
from app.services.prediction_service import PredictionService


def test_dataframe_columns(prediction_request):

    request = prediction_request

    with patch(
        "app.services.prediction_service.run_prediction_pipeline"
    ) as mock_pipeline:

        mock_pipeline.return_value = [120]

        service = PredictionService()

        service.predict(request)

        dataframe = mock_pipeline.call_args.args[0]

        assert list(dataframe.columns) == [
            "Gender",
            "Age",
            "Height",
            "Weight",
            "Duration",
            "Heart_Rate",
            "Body_Temp",
        ]


def test_pipeline_exception(prediction_request):

    request = prediction_request

    with patch(
        "app.services.prediction_service.run_prediction_pipeline"
    ) as mock_pipeline:

        mock_pipeline.side_effect = RuntimeError("Pipeline failed")

        service = PredictionService()

        with pytest.raises(RuntimeError):
            service.predict(request)                