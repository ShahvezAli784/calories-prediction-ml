"""
Prediction utilities.

This module is responsible for generating predictions
from a trained machine learning model.
"""

from typing import Any

import pandas as pd

from src.utils.logger import logger


def predict(
    model: Any,
    X: pd.DataFrame,
)-> pd.Series:
    """
    Generate predictions using a trained model.

    Args:
        model: Trained machine learning model.
        X: Feature matrix.

    Returns:
        Predicted values.
    """

    logger.info("Generating predictions...")

    predictions = model.predict(X)

    logger.info("Predictions generated successfully.")

    return predictions