from typing import List, final
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware

deviceList = ""

app = FastAPI()

# Enable CORS for frontend communication
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Adjust in production for security
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)
router = APIRouter()

@router.get("")
def ipInput(deviceList):
  deviceList = ""
  return(deviceList)

# @router.put(""):