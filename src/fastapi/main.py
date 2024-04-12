from enum import Enum

from fastapi import FastAPI
from pydantic import BaseModel, Field

class ModelName(str, Enum):
    alexnet = "alexnet"
    resnet = "resnet"
    lenet = "lenet"

fake_items_db = [{"item_name": "Foo"}, {"item_name": "Bar"}, {"item_name": "Baz"}]
class DataInput(BaseModel):
    name: str
    age: int
    address: str

app = FastAPI()

@app.get("/")
def root():
    return {"message": "Hello World"}

@app.get("/home")
def home():
    return {"message": "Home Page"}

@app.get("/home/{name}")
def home_name(name: str):
    return {"message": f"Hello, {name}"}

@app.get("/home_err/{name}")
def read_name_err(name:int):
    return {'name' : name}
    
@app.get("/models/{model_name}")
def get_model(model_name: ModelName):
    if model_name == ModelName.alexnet:
        return {"model_name": model_name, "message": "Deep Learning FTW!"}
    
    if model_name.value == "lenet":
        return {"model_name": model_name, "message": "LeCNN all the images"}
    
    return {"model_name": model_name, "message": "Have some residuals"}

@app.get("/items/{item_id}")
def read_item(item_id: str, skip: int = 0, limit: int = 10):
    return fake_items_db[skip : skip + limit]


@app.post("/")
def home_post(msg: str):
    return {"message": msg}

@app.post("/input")
def home_input(input: DataInput):
    return {"name": input.name}