from fastapi import APIRouter


order_router = APIRouter()


@order_router.get('/')
async def order():
    return {'message':"Order page"}