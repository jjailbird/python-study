from fastapi import FastAPI
from pydantic import BaseModel, Field

app = FastAPI()

class DataInput(BaseModel):
    name: str
    age: int
    address: str

class PredictOutput(BaseModel):
  prob: float
  prediction: int

@app.post("/predict", response_model=PredictOutput)
def pydantic_post(req: DataInput):
   return {"prob": 0.5, "prediction": 1}
