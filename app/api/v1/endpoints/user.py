from typing import Dict, Any

from dependency_injector import providers
from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends, Header, HTTPException
from starlette import status

from app.core.container import Container
from app.db.models import User
from app.schemas.user import CreateUserSchema, UserSchema
from app.services.user import UserService
from ..deps import get_current_user_access

router = APIRouter(tags=['User'], prefix='/users')


@router.post('/', status_code=status.HTTP_201_CREATED, response_model=UserSchema)
@inject
async def register_user(
        create_user_schema: CreateUserSchema,
        user_service: UserService = Depends(Provide[Container.user_service]),
) -> UserSchema:
    user = await user_service.create_user(obj_in=create_user_schema)
    user_schema = UserSchema(
        id=user.id,
        username=user.username,
        email=user.email
    )
    return user_schema


@router.get('/me', status_code=status.HTTP_200_OK, response_model=UserSchema)
@inject
async def get_user_info(
        user: User = Depends(get_current_user_access),
) -> UserSchema:
    user_schema = UserSchema(
        id=user.id,
        username=user.username,
        email=user.email
    )
    return user_schema
