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

    due_date = Column(Date, nullable=True)
    created_at = Column(DateTime, default=datetime.utcnow)

    done = Column(
        Boolean,
        default=False
    )

from sqlalchemy import ForeignKey

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

    goal_id = Column(Integer, ForeignKey("goals.id"))

    goal = relationship("GoalModel", back_populates="habits")

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

    habit = relationship("HabitModel")

from sqlalchemy import Date

class GoalModel(Base):

    __tablename__ = "goals"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    title = Column(
        String,
        nullable=False
    )

    description = Column(
        String,
        nullable=True
    )

    target_date = Column(
        Date,
        nullable=True
    )

    completed = Column(
        Boolean,
        default=False
    )

    habits = relationship("HabitModel", back_populates="goal")

    created_at = Column(DateTime, default=datetime.utcnow)

class UserModel(Base):

    __tablename__ = "users"

    id = Column(
        Integer,
        primary_key=True,
        index=True
    )

    username = Column(
        String,
        unique=True,
        nullable=False
    )

    email = Column(
        String,
        unique=True,
        nullable=False
    )

    password_hash = Column(
        String,
        nullable=False
    )