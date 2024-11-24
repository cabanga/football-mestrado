"""
---
"""
from fastapi import APIRouter
from app.api.v1 import conexion

from .endpoints import (
    activities,
)


api_router_v1 = APIRouter()

api_router_v1.include_router(conexion.router)
api_router_v1.include_router(
    activities.router, 
    prefix="/activities", 
    tags=["activities"]
)
