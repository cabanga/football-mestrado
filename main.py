"""
---
"""

import os
from fastapi import FastAPI
from fastapi.staticfiles import StaticFiles
from fastapi.middleware.cors import CORSMiddleware
from fastapi.openapi.docs import (
    get_redoc_html,
    get_swagger_ui_html,
    get_swagger_ui_oauth2_redirect_html,
)
from app.api.v1.base import api_router_v1

def include_router(app_server):
    """---"""
    app_server.include_router(api_router_v1)


def configure_static(app_server):
    """---"""

    base_dir = os.path.dirname(__file__)
    print(StaticFiles(directory=base_dir + "/static/uploads").all_directories)
    app_server.mount(
        "/static", StaticFiles(directory=base_dir + "/static/uploads"), name="static"
    )

def start_application():
    """---"""
    origins = ["*"]
    app_server = FastAPI(
        docs_url=None,
        redoc_url=None,
        title='ACTIVITY PROVIDER - FOOTBALL',
        version='V001',
        description='Provedor de Actividade da UC - Mestrado em Eng. Informatica e Aplicações Web',
    )
    app_server.add_middleware(
        CORSMiddleware,
        allow_origins=origins,
        allow_credentials=True,
        allow_methods=["*"],
        allow_headers=["*"],
    )
    include_router(app_server)
    return app_server


app = start_application()

app.mount("/static", StaticFiles(directory="static"), name="static")

@app.get("/docs", include_in_schema=False)
async def custom_swagger_ui_html():
    return get_swagger_ui_html(
        openapi_url=app.openapi_url,
        title=app.title + " - Swagger UI",
        oauth2_redirect_url=app.swagger_ui_oauth2_redirect_url,
        swagger_js_url="/static/swagger-ui-bundle.js",
        swagger_css_url="/static/swagger-ui.css",
    )

@app.get(app.swagger_ui_oauth2_redirect_url, include_in_schema=False)
async def swagger_ui_redirect():
    return get_swagger_ui_oauth2_redirect_html()

@app.get("/redoc", include_in_schema=False)
async def redoc_html():
    return get_redoc_html(
        openapi_url=app.openapi_url,
        title=app.title + " - ReDoc",
        redoc_js_url="https://unpkg.com/redoc@next/bundles/redoc.standalone.js",
    )

if __name__ == "__main__":
    import uvicorn

    uvicorn.run("main:app", host="0.0.0.0", port='5050', log_level="info", reload=True)
