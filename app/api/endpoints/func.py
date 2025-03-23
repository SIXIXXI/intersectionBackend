from typing import List, final
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.utils.screenshot import take_screenshot, overallInfo, raw_data

deviceList = ""

router = APIRouter()

@router.get("")
def getInfo():
  take_screenshot()
  return(raw_data)

# @router.put(""):