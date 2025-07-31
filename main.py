from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from typing import list

app = FastAPI()

@app.get("/")
def root():
  return {'message': 'Welcome to Neo banking'}