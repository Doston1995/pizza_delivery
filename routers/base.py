import imp
from fastapi import APIRouter
from routers.auth_route import auth_router
from routers.order_route import order_router

api_router = APIRouter()


api_router.include_router(auth_router,  prefix="/auth",tags=["auths"])
api_router.include_router(order_router,  prefix="/order",tags=["orders"])