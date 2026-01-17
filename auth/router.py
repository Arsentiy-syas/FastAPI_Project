from typing import Annotated
from fastapi import APIRouter, HTTPException, Depends, Response
from sqlalchemy.ext.asyncio import AsyncSession
from sqlalchemy import select
from .schemas import UserCreate
from .config import get_password_hash, create_access_token
from .models import UsersORM
from database_main.database import get_db


router_users = APIRouter(prefix='/users', tags=['users'])


SessionDep = Annotated[AsyncSession, Depends(get_db)]


@router_users.post('/register')
async def register_user(user: UserCreate, db: SessionDep):
    result = await db.execute(select(UsersORM).where(UsersORM.username == user.username))
    existing_user = result.scalar_one_or_none()
    if existing_user:
        raise HTTPException(status_code=400, detail='Username already register')
    
    hashed_pwd = get_password_hash(user.password)
    new_user = UsersORM(
        username=user.username,
        password=hashed_pwd
    )
    db.add(new_user)
    await db.commit()
    await db.refresh(new_user)
    
    return {'message': 'Success register!'}
    

@router_users.post('/login')
async def login_user(response: Response, user: UserCreate, db: SessionDep):
    result = await db.execute(select(UsersORM).where(UsersORM.username == user.username))
    existing_user = result.scalar_one_or_none()
    if existing_user is None:
        raise HTTPException(status_code=401, detail="Invalid credentials")
    
    access_token = create_access_token(data={'sub': user.username})
    response.set_cookie(
        key='access_token',
        value=access_token,
        httponly=True,
        secure=False,
        samesite='lax',
        max_age=1800,
    )

    return {'message': 'Login seccess!'}

    
    