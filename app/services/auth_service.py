import os
from jose import jwt
from datetime import datetime, timedelta, timezone

SECRET_KEY = os.getenv("SECRET_KEY", "dev-only-secret")
ALGORITHM = "HS256"


def create_access_token(username: str) -> str:

    expire = datetime.now(timezone.utc) + timedelta(hours=24)

    payload = {
        "sub": username,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )