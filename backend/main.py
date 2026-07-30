from fastapi import FastAPI
from src.api.routers.root import router as root_router

app = FastAPI()

# Add the Router Instance
app.include_router(root_router, prefix="/api/v1")