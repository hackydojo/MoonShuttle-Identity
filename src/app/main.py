from fastapi import FastAPI
from starlette.middleware.cors import CORSMiddleware
from starlette.requests import Request
from starlette.responses import Response
from app.http_resource_routers import root_resource
from app.db import SessionLocal, engine
from app.persistence import entities


entities.Base.metadata.create_all(bind=engine)

microservice_title = 'moon_shuttle'

# -----------------------------------------------------------------------------
# Instance of FastAPI Application
# -----------------------------------------------------------------------------
app = FastAPI(
    title="MoonShuttle Microservice Template",
    description="A FastAPI-based template for Python-based microservices",
    version="1.0.0",
    openapi_url="/{}/api/openapi.json".format(microservice_title),
    docs_url="/{}/api/docs".format(microservice_title),
    redoc_url=None
)


# -----------------------------------------------------------------------------
# Add database session middleware
# -----------------------------------------------------------------------------
@app.middleware("http")
async def db_session_middleware(request: Request, call_next):
    response = Response("Cannot establish connection with persistence provider", status_code=500)
    try:
        request.state.db = SessionLocal()
        response = await call_next(request)
    finally:
        request.state.db.close()
    return response


# -----------------------------------------------------------------------------
# CORS RULES
# -----------------------------------------------------------------------------
origins = [
    "*"
]

# Default configuration is to ALLOW ALL from EVERYWHERE. You might want to
# restrict this.
app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# -----------------------------------------------------------------------------
# ADD ROUTERS
# -----------------------------------------------------------------------------
app.include_router(root_resource.router, prefix="/api/v1")

