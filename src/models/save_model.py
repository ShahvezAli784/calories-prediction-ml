"""
Model persistence utilities.

This module is responsible for:
- Saving trained models
- Loading trained models
"""

import pickle
from pathlib import Path
from typing import Any

from src.config import TRAINED_MODEL_DIR,DEFAULT_MODEL_NAME
from src.utils.logger import logger





def save_model(
    model: Any,
    model_name: str = DEFAULT_MODEL_NAME,
) -> Path:
    """
    Save a trained model to disk.

    Args:
        model: Trained machine learning model.
        model_name: Output filename.

    Returns:
        Path to the saved model.
    """

    TRAINED_MODEL_DIR.mkdir(parents=True, exist_ok=True)

    model_path = TRAINED_MODEL_DIR / model_name

    logger.info("Saving model to %s", model_path)

    with open(model_path, "wb") as file:
        pickle.dump(model, file)

    logger.info("Model saved successfully.")

    return model_path


def load_model(
    model_name: str = DEFAULT_MODEL_NAME,
):
    """
    Load a trained model.

    Args:
        model_name: Model filename.

    Returns:
        Loaded model.

    Raises:
        FileNotFoundError:
            If the model file does not exist.
    """

    model_path = TRAINED_MODEL_DIR / model_name

    if not model_path.exists():
        raise FileNotFoundError(
            f"Model not found: {model_path}"
        )

    logger.info("Loading model from %s", model_path)

    with open(model_path, "rb") as file:
        model = pickle.load(file)

    logger.info("Model loaded successfully.")

    return model