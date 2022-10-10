from sqlalchemy import Column, Date, ForeignKey,  String
from sqlalchemy.orm import relationship
from db.models.base import Base
from sqlalchemy_utils.types import ChoiceType



class Order(Base):
    __tablename__ = 'orders'

    ORDER_STATUS = (
        ('PENDING','pending'),
        ('IN_TRANSIT', 'in-transit'),
        ('DELIVERED','delivered')
    )
    PIZZA_SIZE = (
        ('SMALL', 'small'),
        ('MEDIUM', 'medium'),
        ('LARGE', 'large'),
        ('EXTRA-LARGE', 'extra-large')
    )

    id = Column(String, primary_key=True)
    quantity = Column(String, nullable = True)
    order_status = Column(ChoiceType(choices=ORDER_STATUS), default='PENDING')
    pizza_size = Column(ChoiceType(choices=PIZZA_SIZE), default='SMALL')
    create_at = Column(Date)
    user_id = Column(String, ForeignKey('user.id'))
    user = relationship('User', back_populates = 'orders')

    def __repr__(self):
        return f"<Order {self.id}>"