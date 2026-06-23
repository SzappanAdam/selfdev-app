from app.database.database import (
    SessionLocal
)

from app.database.models import (
    UserModel
)

class UserRepository:

    def __init__(self):

        self.db = SessionLocal()

    def create_user(
        self,
        username,
        email,
        password_hash
    ):

        user = UserModel(
            username=username,
            email=email,
            password_hash=password_hash
        )

        self.db.add(user)

        self.db.commit()

        self.db.refresh(user)

        return user