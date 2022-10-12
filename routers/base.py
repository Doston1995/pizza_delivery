import imp
from fastapi import APIRouter
from routers import user_route, order_route, login_route

api_router = APIRouter()


api_router.include_router(user_route.router,  prefix="/auth",tags=["auths"])
api_router.include_router(order_route.router,  prefix="/order",tags=["orders"])
api_router.include_router(login_route.router,  prefix="/login",tags=["login"])