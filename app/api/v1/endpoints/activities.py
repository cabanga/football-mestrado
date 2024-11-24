from typing import Dict
from fastapi import APIRouter, status, Depends, HTTPException
from fastapi.responses import JSONResponse
from fastapi.encoders import jsonable_encoder


from app.schemas.activity import ActivitySchema

router = APIRouter()


@router.post("/", status_code=201)
async def create_activity(
    data: ActivitySchema,
):
    """
    CREATE ACTIVITY

    * Required field:

        - name
        - config_url
        - json_params_url
        - user_url
        - analytics_url
        - analytics_list_url
    """

    return JSONResponse(
        content=jsonable_encoder(
            data
        ),
        status_code=status.HTTP_200_OK,
    )
