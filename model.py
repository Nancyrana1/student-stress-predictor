from pathlib import Path

from fastapi import FastAPI
from pydantic import BaseModel
import pickle
import numpy as np

_BASE = Path(__file__).resolve().parent
_PICKLE = _BASE / "picklefiles"

with open(_PICKLE / "model.pkl", "rb") as f:
    model = pickle.load(f)

with open(_PICKLE / "scaler.pkl", "rb") as f:
    scaler = pickle.load(f)

app = FastAPI(
    title="Student Stress Level Predictor",
    description="API for predicting student stress from lifestyle and academic inputs.",
    version="1.0.0",
)


class StudentInput(BaseModel):
    Study_Hours_Per_Day: float
    Extracurricular_Hours_Per_Day: float
    Sleep_Hours_Per_Day: float
    Social_Hours_Per_Day: float
    Physical_Activity_Hours_Per_Day: float
    GPA: float


@app.get("/")
def home():
    return {
        "service": "Student Stress Level Predictor",
        "status": "running",
        "docs": "/docs",
        "predict_endpoint": "POST /predict",
    }


@app.post("/predict")
def predict(data: StudentInput):
    input_array = np.array(
        [
            [
                data.Study_Hours_Per_Day,
                data.Extracurricular_Hours_Per_Day,
                data.Sleep_Hours_Per_Day,
                data.Social_Hours_Per_Day,
                data.Physical_Activity_Hours_Per_Day,
                data.GPA,
            ]
        ]
    )

    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)[0]

    stress_map = {0: "Low", 1: "Medium", 2: "High"}

    return {
        "stress_level_code": int(prediction),
        "stress_level_label": stress_map.get(int(prediction), "Unknown"),
    }
