from app.database.models import UserModel


class UserRepository:

    def __init__(self, db):
        self.db = db

    def create_user(self, username, email, password_hash):

        existing = (
            self.db.query(UserModel)
            .filter(UserModel.email == email)
            .first()
        )

        if existing:
            raise ValueError("Email already exists")

        user = UserModel(
            username=username,
            email=email,
            password_hash=password_hash
        )

        try:
            self.db.add(user)
            self.db.commit()
            self.db.refresh(user)
            return user

        except Exception:
            self.db.rollback()
            raise

    def get_by_email(self, email):

        return (
            self.db.query(UserModel)
            .filter(UserModel.email == email)
            .first()
        )

    def get_by_id(self, user_id):

        return (
            self.db.query(UserModel)
            .filter(UserModel.id == user_id)
            .first()
        )