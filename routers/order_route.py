from fastapi import APIRouter
from routers.login_route import get_current_user_from_token
from sqlalchemy.orm import Session
from fastapi import Depends,HTTPException,status
from db.models import User
from typing import List
from db.session import get_db
from schemas.order import OrderModel, OrderCreate, OrderShow
from db.repository.order import list_orders, create_orders, retreive_order

router = APIRouter()


@router.get("/all")
async def order_list(db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    user_id = user.id
    current_user = db.query(User).filter(User.id == user_id).first()
    if current_user.is_staff:
        orders = list_orders(db=db)
        return orders
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This user is not superuser")


@router.post("/create", status_code = status.HTTP_201_CREATED )
async def order_create(order:OrderCreate, db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    order = create_orders(order = order, db = db, user_id = user.id)
    return order


@router.get("/get/{id}")
async def order_retrieve(id:str, db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    user_id = user.id
    current_user = db.query(User).filter(User.id == user_id).first()
    if current_user.is_staff:
        order = retreive_order(id=id,db=db)
        if not order:
            raise HTTPException(status_code=status.HTTP_404_NOT_FOUND,detail=f"Order with this id {id} does not exist")
        return order
    raise HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This user is not superuser")
    

@router.get("/user/orders")
async def user_orders(db:Session = Depends(get_db), user:User = Depends(get_current_user_from_token)):
    user_id = user.id
    current_user = db.query(User).filter(User.id == user_id).first()
    return current_user.orders