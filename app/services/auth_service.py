from jose import jwt
from datetime import datetime
from datetime import timedelta

SECRET_KEY = (
    "CHANGE_ME_LATER"
)

ALGORITHM = "HS256"

def create_access_token(
    username
):

    expire = (
        datetime.utcnow()
        + timedelta(hours=24)
    )

    payload = {
        "sub": username,
        "exp": expire
    }

    return jwt.encode(
        payload,
        SECRET_KEY,
        algorithm=ALGORITHM
    )