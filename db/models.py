from sqlalchemy import Column, Date, ForeignKey,  String,  Text, Boolean
from sqlalchemy.orm import relationship
from sqlalchemy_utils.types import ChoiceType
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()
metadata = Base.metadata


class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String(25), unique=True)
    password = Column(String(255))
    email = Column(String(80), unique=True)
    first_name = Column(Text, nullable = True)
    is_staff = Column(Boolean, default = False)
    gender = Column(String(1))
    create_at = Column(String(50))
    orders = relationship('Order', back_populates = 'user')

    def __repr__(self):
        return f"<User {self.username}>"
    

class Order(Base):
    __tablename__ = 'orders'

    id = Column(String, primary_key=True)
    quantity = Column(String, nullable = True)
    order_status = Column(String, nullable = True)
    pizza_size = Column(String, nullable = True)
    create_at = Column(String, nullable = True)
    user_id = Column(String, ForeignKey('users.id'))
    user = relationship('User', back_populates = 'orders')

    def __repr__(self):
        return f"<Order {self.id}>"