from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from slugify import slugify
from sqlalchemy import insert, select, update, delete
from sqlalchemy.orm import Session

from app.backend.db_depends import get_db
from app.models.user import User
from app.schemas import CreateUser, UpdateUser

router = APIRouter(prefix="/user", tags=["User"])
db_sesssion = Annotated[Session, Depends(get_db)]

@router.get("/")
async def all_users(db: db_sesssion):
    users = db.scalars(select(User)).all()
    return users


@router.get("/user_id")
async def user_by_id(db: db_sesssion, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_Found, detail="User was not found")
    return user


@router.post("/create")
async def create_user(db: db_sesssion, create_user: CreateUser):
    db.execute(insert(User).values(username=create_user.username,
                                   firstname=create_user.firstname,
                                   lastname=create_user.lastname,
                                   age=create_user.age,
                                   slug=slugify(create_user.username)))
    db.commit()
    return {
        'status_code': status.HTTP_201_CREATED,
        'transaction': 'Successful'
    }


@router.put("/update")
async def update_user(db: db_sesssion, user_id: int, update_user: UpdateUser):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(status_code=status.HTTP_404_NOT_Found, detail="User was not found")
    db.execute(update(User).values(firstname=update_user.firstname,
                                   lastname=update_user.lastname,
                                   age=update_user.age))
    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}


@router.delete("/delete")
async def delete_user(db: db_sesssion, user_id: int):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_Found,
            detail="User was not found"
        )
    db.execute(delete(User).where(User.id == user_id))

    db.commit()
    return {'status_code': status.HTTP_201_CREATED, 'transaction': 'Successful'}
