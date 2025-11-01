import pickle
from fastapi import FastAPI
from pydantic import BaseModel

# Define the data model (input structure)
class Lead(BaseModel):
    lead_source: str
    number_of_courses_viewed: int
    annual_income: float
    

# Load the pipeline
with open("pipeline_v1.bin", "rb") as f_in:
    pipeline = pickle.load(f_in)

# Initialize FastAPI app
app = FastAPI()

@app.get("/")
def home():
    return {"message": "Lead Scoring Model is running!"}

@app.post("/predict")
def predict(lead: Lead):
    record = lead.model_dump()
    X = [record]
    prob = pipeline.predict_proba(X)[0, 1]
    return {"conversion_probability": prob}

