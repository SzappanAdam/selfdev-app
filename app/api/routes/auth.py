from fastapi import APIRouter

from app.services.auth_service import create_access_token
from app.services.security_service import hash_password
from app.repositories.user_repository import UserRepository

router = APIRouter(prefix="/auth", tags=["Auth"])

user_repo = UserRepository()


@router.post("/register")
def register(username: str, email: str, password: str):
    hashed = hash_password(password)

    user_repo.create_user(username, email, hashed)

    return {"message": "User created"}


@router.post("/login")
def login(username: str, password: str):
    token = create_access_token(username)

    return {"access_token": token}