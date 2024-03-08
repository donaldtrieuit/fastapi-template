from fastapi import APIRouter

from routes import user_routes

api_router = APIRouter()
api_router.include_router(user_routes.router, tags=["auth"])
