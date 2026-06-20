from sqlalchemy import Column
from sqlalchemy import Integer
from sqlalchemy import String
from sqlalchemy import Boolean
from sqlalchemy import Date
from sqlalchemy import ForeignKey
from sqlalchemy.orm import relationship

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

class HabitModel(Base):

    __tablename__ = "habits"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    name = Column(
        String,
        nullable=False
    )

    category = Column(
        String,
        nullable=True
    )

    active = Column(
        Boolean,
        default=True
    )

class HabitLogModel(Base):

    __tablename__ = "habit_logs"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    habit_id = Column(
        Integer,
        ForeignKey("habits.id"),
        nullable=False
    )

    date = Column(
        Date,
        nullable=False
    )

    completed = Column(
        Boolean,
        default=False
    )