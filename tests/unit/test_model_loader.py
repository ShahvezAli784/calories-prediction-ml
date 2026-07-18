import pickle

import pytest

from src.models.save_model import save_model, load_model

def test_save_model(tmp_path, monkeypatch):

    monkeypatch.setattr(
        "src.models.save_model.TRAINED_MODEL_DIR",
        tmp_path,
    )

    model = {"name": "dummy model"}

    model_path = save_model(model, "test_model.pkl")

    assert model_path.exists()
    assert model_path.name == "test_model.pkl"
    
def test_load_model_success(tmp_path, monkeypatch):

    monkeypatch.setattr(
        "src.models.save_model.TRAINED_MODEL_DIR",
        tmp_path,
    )

    model = {"accuracy": 0.95}

    model_path = tmp_path / "test_model.pkl"

    with open(model_path, "wb") as file:
        pickle.dump(model, file)

    loaded_model = load_model("test_model.pkl")

    assert loaded_model == model
 
def test_load_model_file_not_found(tmp_path, monkeypatch):

    monkeypatch.setattr(
        "src.models.save_model.TRAINED_MODEL_DIR",
        tmp_path,
    )

    with pytest.raises(FileNotFoundError):
        load_model("missing.pkl")        