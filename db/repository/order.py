from sqlalchemy.orm import Session
from db.models import Order
from schemas.order import OrderModel, OrderCreate,OrderStatusModel
import datetime, uuid



def list_orders(db : Session):
    orders = db.query(Order).all()
    return orders


def create_orders(order: OrderCreate, db: Session, user_id = str):
    order_date = str(datetime.datetime.now())
    order_id   = str(uuid.uuid1())
    order_object = Order(
        id           = order_id,
        quantity     = order.quantity,
        order_status = order.order_status,
        create_at    = order_date,
        pizza_size   = order.pizza_size,
        user_id      = user_id
    )
    db.add(order_object)
    db.commit()
    db.refresh(order_object)
    return order_object



def retreive_order(id:str,db:Session):
    order = db.query(Order).filter(Order.id == id).first()
    return order



def update_order(ord_id:str, order: OrderCreate, db: Session):
    order_update = db.query(Order).filter(Order.id == ord_id)
    order_update.update(order.__dict__)
    db.commit()
    return 1



def update_order_status(ord_id:str, order: OrderStatusModel, db: Session):
    order_update = db.query(Order).filter(Order.id == ord_id).first()
    order_update.order_status = order.order_status
    db.commit()
    return 1


def delete_order(id:str,db: Session):
    order_delete = db.query(Order).filter(Order.id == id)
    order_delete.delete(synchronize_session=False)
    db.commit()
    return 1