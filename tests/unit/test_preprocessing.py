import pandas as pd
import pytest

from src.data.preprocessing import (
    validate_dataframe,
    encode_gender,
    create_features_and_target,
    preprocess_data,
    preprocess_input,
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


def test_validate_dataframe_success(sample_dataframe):
    validate_dataframe(sample_dataframe)


def test_validate_dataframe_missing_columns(sample_dataframe):

    df = sample_dataframe.drop(columns=["Calories"])

    with pytest.raises(ValueError):
        validate_dataframe(df)


def test_encode_gender_male(sample_dataframe):

    encoded_df = encode_gender(sample_dataframe)

    assert encoded_df["Gender"].iloc[0] == 0


def test_encode_gender_female(sample_dataframe):

    df = sample_dataframe.copy()
    df["Gender"] = "female"

    encoded_df = encode_gender(df)

    assert encoded_df["Gender"].iloc[0] == 1


def test_encode_gender_uppercase(sample_dataframe):

    df = sample_dataframe.copy()
    df["Gender"] = "MALE"

    encoded_df = encode_gender(df)

    assert encoded_df["Gender"].iloc[0] == 0


def test_create_features_and_target(sample_dataframe):

    X, y = create_features_and_target(sample_dataframe)

    assert "User_ID" not in X.columns
    assert "Calories" not in X.columns

    assert y.iloc[0] == 250


def test_preprocess_data_success(sample_dataframe):

    X, y = preprocess_data(sample_dataframe)

    assert "User_ID" not in X.columns
    assert "Calories" not in X.columns

    assert X["Gender"].iloc[0] == 0
    assert y.iloc[0] == 250


def test_preprocess_data_missing_columns(sample_dataframe):

    df = sample_dataframe.drop(columns=["Weight"])

    with pytest.raises(ValueError):
        preprocess_data(df)


def test_preprocess_input_success(sample_dataframe):

    input_df = sample_dataframe.drop(columns=["User_ID", "Calories"])

    processed = preprocess_input(input_df)

    assert list(processed.columns) == [
        "Gender",
        "Age",
        "Height",
        "Weight",
        "Duration",
        "Heart_Rate",
        "Body_Temp",
    ]

    assert processed["Gender"].iloc[0] == 0


def test_preprocess_input_missing_columns(sample_dataframe):

    input_df = sample_dataframe.drop(
        columns=["User_ID", "Calories", "Weight"]
    )

    with pytest.raises(ValueError):
        preprocess_input(input_df)