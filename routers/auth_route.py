from fastapi import APIRouter
from sqlalchemy.orm import Session
from fastapi import Depends, HTTPException, status
from db.session import get_db
from typing import List
from db.models import User
from schemas.auth import SignUpModel
from db.repository.auth import list_users, create_user


router = APIRouter()


@router.get("/all", response_model=List[SignUpModel])
def get_all_users(db:Session = Depends(get_db)):
    users = list_users(db=db)
    return users


@router.post("/create/",status_code = status.HTTP_201_CREATED )
def create_users(user: SignUpModel, db: Session = Depends(get_db)):
    db_username = db.query(User).filter(User.username == user.username).first()
    db_email = db.query(User).filter(User.email == user.email).first()
    if db_username or db_email is not None:
        return HTTPException(status_code = status.HTTP_400_BAD_REQUEST,
            detail = "This username or email address already exist")
    user = create_user(user=user, db=db)
    return user
