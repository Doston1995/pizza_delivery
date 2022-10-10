from sqlalchemy import Column, Date, String, Text, Boolean
from sqlalchemy.orm import relationship
from db.models.base import Base



class User(Base):
    __tablename__ = 'users'

    id = Column(String, primary_key=True)
    username = Column(String(25), unique=True)
    email = Column(String(80), unique=True)
    first_name = Column(Text, nullable = True)
    is_staff = Column(Boolean, default = False)
    gender = Column(Boolean, default = False)
    create_at = Column(Date)
    orders = relationship('Order', back_populates = 'user')

    def __repr__(self):
        return f"<User {self.username}>"