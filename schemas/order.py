from pydantic import BaseModel
from typing import Optional, List
from db.models import Order
from enum import Enum



class Order_status(str, Enum):
        PENDING    = 'PENDING'
        IN_TRANSIT = 'IN_TRANSIT'
        DELIVERED  = 'DELIVERED'
        
        
class Pizza_size(str, Enum):
        SMALL       = 'SMALL'
        MEDIUM      = 'MEDIUM'
        LARGE       = 'LARGE'
        EXTRA_LARGE = 'EXTRA_LARGE'

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
    order_status :Order_status 
    pizza_size   :Pizza_size
    
    class Config:
        orm_mode = True
        

class OrderStatusModel(BaseModel):
    order_status : Order_status 
    
    class Config:
        orm_mode = True