from typing import List, final
from fastapi import APIRouter, Depends, HTTPException, FastAPI
from pydantic import BaseModel
from fastapi.middleware.cors import CORSMiddleware
from app.utils.screenshot import take_screenshot, prodata, device_to_pull, deviceInfo, overallInfo

deviceList = ""


router = APIRouter()

@router.get("")
def getInfo():
  take_screenshot()
  return(overallInfo)

# @router.put(""):