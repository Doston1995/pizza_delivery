import imp
from fastapi import APIRouter
from routers import auth_route
from routers import order_route

api_router = APIRouter()


api_router.include_router(auth_route.router,  prefix="/auth",tags=["auths"])
api_router.include_router(order_route.router,  prefix="/order",tags=["orders"])