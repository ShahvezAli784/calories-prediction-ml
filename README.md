# 🔥 Calories Burnt Prediction API

A production-ready Machine Learning project that predicts the number of calories burned during exercise using an XGBoost regression model. The project follows a modular architecture with separate components for data processing, model training, prediction, and a FastAPI-powered REST API.

---

## ✨ Features

- Modular machine learning pipeline
- XGBoost Regression model
- Automated data preprocessing
- Model evaluation with MAE, RMSE, and R²
- Model persistence using Pickle
- FastAPI REST API
- Interactive Swagger UI
- Structured logging
- Configurable project settings
- Clean project architecture

---

## 📂 Project Structure

```text
calories-prediction-ml/
│
├── app/                         # FastAPI application
│   ├── api/
│   ├── core/
│   ├── schemas/
│   ├── services/
│   ├── utils/
│   └── main.py
│
├── data/
│   ├── raw/
│   ├── processed/
│   └── external/
│
├── models/
│   ├── trained/
│   ├── checkpoints/
│   └── metrics/
│
├── notebooks/
│   └── burnt_calories.ipynb     # Exploratory Data Analysis only
│
├── scripts/
│   ├── train.py
│   └── predict.py
│
├── src/
│   ├── config.py
│   ├── data/
│   ├── features/
│   ├── models/
│   ├── pipelines/
│   └── utils/
│
├── tests/
│
├── requirements.txt
└── README.md
```

---

# 📊 Dataset

The project uses two datasets:

- **exercise.csv**
- **calories.csv**

Both datasets are merged during loading to create the final training dataset.

---

# ⚙️ Machine Learning Pipeline

```
Raw Data
    │
    ▼
Load Dataset
    │
    ▼
Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Train/Test Split
    │
    ▼
Train XGBoost Model
    │
    ▼
Evaluate Model
    │
    ▼
Save Model
```

---

# 📈 Model Performance

| Metric | Score |
|---------|-------|
| MAE | **1.2242** |
| RMSE | **1.7514** |
| R² Score | **0.9992** |

---

# 🚀 Installation

Clone the repository

```bash
git clone https://github.com/ShahvezAli784/calories-prediction-ml.git

cd calories-prediction-ml
```

Create virtual environment

```bash
python -m venv .venv
```

Activate environment

Windows

```bash
.venv\Scripts\activate
```

Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

```bash
python -m scripts.train
```

This command will:

- Load datasets
- Preprocess data
- Split train/test
- Train the XGBoost model
- Evaluate performance
- Save the trained model
- Save evaluation metrics

---

# 🔮 Run Prediction Script

```bash
python -m scripts.predict
```

Example output

```
Prediction
--------------------
Predicted Calories Burned: 189.35
```

---

# 🌐 Run FastAPI

```bash
uvicorn app.main:app --reload
```

Open

```
http://127.0.0.1:8000/docs
```

Swagger UI

or

```
http://127.0.0.1:8000/redoc
```

ReDoc Documentation

---

# 📮 API Endpoints

## Predict Calories

**POST**

```
/predict
```

Example Request

```json
{
    "gender": "male",
    "age": 24,
    "height": 180,
    "weight": 75,
    "duration": 30,
    "heart_rate": 110,
    "body_temp": 40.0
}
```

Example Response

```json
{
    "predicted_calories": 227.05
}
```

---

## Health Check

**GET**

```
/health
```

Response

```json
{
    "status": "healthy"
}
```

---

# 📝 Exploratory Data Analysis

The notebook contains only:

- Dataset overview
- Missing value analysis
- Duplicate analysis
- Distribution plots
- Correlation analysis
- Feature relationships
- Key insights

Model training and prediction logic are implemented inside the modular `src/` package.

---

# 🛠️ Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- XGBoost
- FastAPI
- Pydantic
- Uvicorn
- Matplotlib
- Seaborn

---

# 📌 Future Improvements

- Docker support
- CI/CD with GitHub Actions
- Model versioning
- Experiment tracking
- Cloud deployment
- Unit and integration tests
- Request logging middleware

---

# 👨‍💻 Author

**Shahvez Memon**

- GitHub: https://github.com/ShahvezAli784
- LinkedIn: https://linkedin.com/in/shahvez-memon-528a18405
