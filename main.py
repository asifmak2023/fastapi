from fastapi import FastAPI, HTTPException
from models import ItemPayload

app = FastAPI()

grocery_list: dict[int, ItemPayload] = {}



@app.get("/")
def root():
    return {"message": "Hello World"}

