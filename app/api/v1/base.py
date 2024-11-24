"""
---
"""
from fastapi import APIRouter
from app.api.v1 import conexion

#from .endpoints import (
#    addresses,
#    costs,
#    orders,
#    payments_methods,
#    products,
#    units,
#    users,
#    wiza,
#    emis,
#    reports
#)


api_router_v1 = APIRouter()

api_router_v1.include_router(conexion.router)

#api_router_v1.include_router(users.router, prefix="/users", tags=["users"])
