from typing import Annotated

from fastapi import APIRouter, Depends, status, HTTPException
from sqlalchemy.orm import Session
from sqlalchemy import insert, select, update, delete
from slugify import slugify

from app.backend.db_depends import get_db
from app.models.user import User
from app.schemas import CreateUser, UpdateUser


router = APIRouter(prefix='/user', tags=['user'])
db_sess = Annotated[Session, Depends(get_db)]

@router.get("/")
async def all_user(db: db_sess):
    users = db.scalars(select(User)).all()
    if users is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="No Users ")
    else:
        return users


@router.get("/{user_id}")
async def user_by_id(user_id: int, db: db_sess):
    user = db.scalar(select(User).where(User.id == user_id))
    if user is None:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail="User was not found")
    return user


@router.post("/create")
async def create_user(db: db_sess, user_create_model: CreateUser):
    db.execute(insert(User).values(username=user_create_model.username,
                                   firstname=user_create_model.firstname,
                                   lastname=user_create_model.lastname,
                                   age=user_create_model.age,
                                   slug=slugify(user_create_model.username)))
    db.commit()
    return  {'status_code': status.HTTP_201_CREATED,
             'transaction': 'Successful'}




@router.put("/update")
async def update_user(user_id: int, updated_user: UpdateUser, db: db_sess):
    query = select(User).where(User.id == user_id)
    user = db.scalar(query)
    if user:
        db.execute(update(User).where(User.id == user_id).values(**updated_user.dict()))
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "User update is successful!"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User was not found")


@router.delete("/delete")
async def delete_user(user_id: int, db: db_sess):
    query = select(User).where(User.id == user_id)
    user = db.scalar(query)
    if user:
        db.execute(delete(User).where(User.id == user_id))
        db.commit()
        return {"status_code": status.HTTP_200_OK, "transaction": "User deletion successful!"}
    raise HTTPException(
        status_code=status.HTTP_404_NOT_FOUND,
        detail="User was not found")
