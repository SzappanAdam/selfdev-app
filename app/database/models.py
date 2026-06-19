from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean

from app.database.database import Base


class TaskModel(Base):

    __tablename__ = "tasks"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        default="general"
    )

    priority = Column(
        String,
        default="medium"
    )

    due_date = Column(
        String,
        nullable=True
    )

    done = Column(
        Boolean,
        default=False
    )