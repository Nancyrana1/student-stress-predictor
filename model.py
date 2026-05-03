from fastapi import FastAPI
from pydantic import BaseModel, AnyUrl, Field, computed_field
from typing import Literal, Annotated
import pickle
import pandas as pd
import numpy as np


with open("picklefiles\model.pkl",'rb') as f:
    model = pickle.load(f)

with open("picklefiles/scaler.pkl", "rb") as f:
    scaler = pickle.load(f)


app=FastAPI(title="Student stress Level Predictor")


# input schema

class StudentInput(BaseModel):
    Study_Hours_Per_Day: float
    Extracurricular_Hours_Per_Day: float
    Sleep_Hours_Per_Day: float
    Social_Hours_Per_Day: float
    Physical_Activity_Hours_Per_Day: float
    GPA: float


@app.get('/')
def home():
    return {"message":"Student stress predictor is runningggg hahaha"}

@app.post('/predict')

def predict(data:StudentInput):
    input_array = np.array([[
        data.Study_Hours_Per_Day,
        data.Extracurricular_Hours_Per_Day,
        data.Sleep_Hours_Per_Day,
        data.Social_Hours_Per_Day,
        data.Physical_Activity_Hours_Per_Day,
        data.GPA
    ]])

    scaled_input = scaler.transform(input_array)
    prediction = model.predict(scaled_input)[0]

    stress_map = {0:'Low',1:"Medium",2:"High"}


    return{
        "stress_level_code": int(prediction),
        "stress_level_label" : stress_map.get(int(prediction),"Unknown")
    }