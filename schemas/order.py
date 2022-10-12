from pydantic import BaseModel
from typing import Optional, List
from db.models import Order


class OrderModel(BaseModel):
    id           :Optional[str]
    quantity     :Optional[str]
    order_status :Optional[str]
    pizza_size   :Optional[str]
    create_at    :Optional[str]
    user_id      :Optional[str]
    
    class Config:
        orm_mode = True


class OrderShow(BaseModel):
    id           :Optional[str]
    quantity     :Optional[str]
    order_status :Optional[str]
    pizza_size   :Optional[str]
    create_at    :Optional[str]
    user_id      :Optional[str]
    
    class Config:
        orm_mode = True


class OrderCreate(BaseModel):
    quantity     :str
    order_status :str ='PENDING'
    pizza_size   :str = "SMALL"
    
    class Config:
        orm_mode = True