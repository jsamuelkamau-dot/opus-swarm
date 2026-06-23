"""
Opus Swarm — Database Models
Engineering Domain 5: Database Schemas and Migrations

Each class here = one table in PostgreSQL.
SQLAlchemy reads these classes and creates the actual database columns.
"""

from datetime import datetime, timezone
from sqlalchemy import String, Text, DateTime, Boolean, Integer, ForeignKey
from sqlalchemy.orm import Mapped, mapped_column, relationship
from core.database import Base


# ─────────────────────────────────────────────
# Task Model
# Represents one business task given to the swarm.
# Example: "Handle Q2 financial reporting"
# ─────────────────────────────────────────────
class Task(Base):
    __tablename__ = "tasks"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    title: Mapped[str] = mapped_column(String(255), nullable=False)
    description: Mapped[str] = mapped_column(Text, nullable=True)
    status: Mapped[str] = mapped_column(String(50), default="pending")
    created_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )
    completed_at: Mapped[datetime] = mapped_column(DateTime(timezone=True), nullable=True)

    # One Task can have many AgentLogs
    logs: Mapped[list["AgentLog"]] = relationship("AgentLog", back_populates="task")

    def __init__(self, **kwargs):
        # Apply Python-level defaults before SQLAlchemy sees the object
        kwargs.setdefault("status", "pending")
        kwargs.setdefault("created_at", datetime.now(timezone.utc))
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<Task id={self.id} title='{self.title}' status='{self.status}'>"


# ─────────────────────────────────────────────
# AgentLog Model
# Records every action taken by an agent on a task.
# This is the audit trail — what happened, who did it, when.
# ─────────────────────────────────────────────
class AgentLog(Base):
    __tablename__ = "agent_logs"

    id: Mapped[int] = mapped_column(Integer, primary_key=True, autoincrement=True)
    task_id: Mapped[int] = mapped_column(Integer, ForeignKey("tasks.id"), nullable=False)
    agent_name: Mapped[str] = mapped_column(String(100), nullable=False)
    action: Mapped[str] = mapped_column(String(255), nullable=False)
    result: Mapped[str] = mapped_column(Text, nullable=True)
    success: Mapped[bool] = mapped_column(Boolean, default=True)
    logged_at: Mapped[datetime] = mapped_column(
        DateTime(timezone=True),
        default=lambda: datetime.now(timezone.utc),
    )

    # Each AgentLog belongs to one Task
    task: Mapped["Task"] = relationship("Task", back_populates="logs")

    def __init__(self, **kwargs):
        # Apply Python-level defaults before SQLAlchemy sees the object
        kwargs.setdefault("success", True)
        kwargs.setdefault("logged_at", datetime.now(timezone.utc))
        super().__init__(**kwargs)

    def __repr__(self) -> str:
        return f"<AgentLog agent='{self.agent_name}' action='{self.action}' success={self.success}>"
