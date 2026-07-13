# 🔥 Calories Burnt Prediction ML System

A production-ready Machine Learning project that predicts the number of calories burned during exercise using an **XGBoost Regression model**.

The project follows a modular machine learning architecture with separate components for data processing, feature engineering, model training, prediction, and deployment.

The system provides two ways to interact with the trained model:

- **FastAPI REST API** for backend prediction services
- **Streamlit Web Application** for an interactive user interface

---

# ✨ Features

- Modular machine learning pipeline
- XGBoost Regression model
- Automated data preprocessing
- Feature engineering pipeline
- Model evaluation with MAE, RMSE, and R² Score
- Model persistence using Pickle
- FastAPI REST API
- Interactive Swagger UI documentation
- Streamlit prediction application
- Structured logging
- Configurable project settings
- Clean and scalable project architecture

---

# 📂 Project Structure

```text
calories-prediction-ml/
│
├── app/                         # FastAPI application
│   ├── api/                     # API routes
│   ├── core/                    # Configuration
│   ├── schemas/                 # Request/response schemas
│   ├── services/                # Prediction services
│   ├── utils/                   # API utilities
│   └── main.py                  # FastAPI entry point
│
├── app.py                       # Streamlit web application
│
├── data/
│   ├── raw/                     # Original datasets
│   ├── processed/               # Processed datasets
│   └── external/                # External data sources
│
├── models/
│   ├── trained/                 # Saved trained models
│   ├── checkpoints/
│   └── metrics/                 # Evaluation results
│
├── notebooks/
│   └── burnt_calories.ipynb     # Exploratory Data Analysis
│
├── scripts/
│   ├── train.py                 # Model training script
│   └── predict.py               # Prediction script
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

The datasets are merged during the data loading process to create the final training dataset.

---

# ⚙️ Machine Learning Pipeline

```
Raw Data
    │
    ▼
Load Dataset
    │
    ▼
Data Preprocessing
    │
    ▼
Feature Engineering
    │
    ▼
Train/Test Split
    │
    ▼
Train XGBoost Regression Model
    │
    ▼
Model Evaluation
    │
    ▼
Save Trained Model
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

Clone the repository:

```bash
git clone https://github.com/ShahvezAli784/calories-prediction-ml.git

cd calories-prediction-ml
```

Create virtual environment:

```bash
python -m venv .venv
```

Activate environment:

### Windows

```bash
.venv\Scripts\activate
```

### Linux / macOS

```bash
source .venv/bin/activate
```

Install dependencies:

```bash
pip install -r requirements.txt
```

---

# 🏋️ Train the Model

Run:

```bash
python -m scripts.train
```

This will:

- Load datasets
- Perform preprocessing
- Create training and testing datasets
- Train the XGBoost model
- Evaluate model performance
- Save trained model
- Save evaluation metrics

---

# 🔮 Run Prediction Script

Run:

```bash
python -m scripts.predict
```

Example output:

```
Prediction
--------------------
Predicted Calories Burned: 189.35
```

---

# 🌐 Run FastAPI Application

Start the API server:

```bash
uvicorn app.main:app --reload
```

Open:

```
http://127.0.0.1:8000/docs
```

Swagger UI documentation.

or:

```
http://127.0.0.1:8000/redoc
```

ReDoc documentation.

---

# 🎨 Run Streamlit Application

The project includes an interactive Streamlit interface that allows users to predict calories burned through a simple web interface.

Run:

```bash
streamlit run app.py
```

The application will open at:

```
http://localhost:8501
```

Streamlit features:

- Interactive user input form
- Real-time calorie prediction
- Uses the trained XGBoost model
- No API knowledge required

---

# 📮 API Endpoints

## Predict Calories

### POST

```
/predict
```

Example Request:

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

Example Response:

```json
{
    "predicted_calories": 227.05
}
```

---

## Health Check

### GET

```
/health
```

Response:

```json
{
    "status": "healthy"
}
```

---

# 📝 Exploratory Data Analysis

The notebook contains only exploratory analysis:

- Dataset overview
- Missing value analysis
- Duplicate analysis
- Distribution analysis
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
- Streamlit
- Pydantic
- Uvicorn
- Matplotlib
- Seaborn

---

# 📌 Future Improvements

- Docker containerization
- CI/CD with GitHub Actions
- Model versioning
- Experiment tracking
- Cloud deployment
- Unit and integration testing
- Request logging middleware

---

# 👨‍💻 Author

**Shahvez Memon**

- GitHub: https://github.com/ShahvezAli784
- LinkedIn: https://linkedin.com/in/shahvez-memon-528a18405
