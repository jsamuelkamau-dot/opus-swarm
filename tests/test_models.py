"""
Opus Swarm — Tests for Database Models
Engineering Domain 5: Database Schemas and Migrations

These tests check that our model classes are correctly defined —
right table names, right columns, right relationships.
We test the structure here, not the live database connection.
"""

import pytest
from core.models import Task, AgentLog


# ─────────────────────────────────────────────
# Task Model Tests
# ─────────────────────────────────────────────

def test_task_has_correct_tablename():
    """Task must map to the 'tasks' table in PostgreSQL."""
    assert Task.__tablename__ == "tasks"


def test_task_has_required_columns():
    """Task must have id, title, status, and created_at columns."""
    columns = [col.name for col in Task.__table__.columns]
    assert "id" in columns
    assert "title" in columns
    assert "status" in columns
    assert "created_at" in columns


def test_task_default_status_is_pending():
    """A new Task should default to 'pending' status."""
    task = Task(title="Test task")
    assert task.status == "pending"


def test_task_repr_contains_title():
    """The repr of a Task should show its title and status."""
    task = Task(title="Q2 Report", status="pending")
    result = repr(task)
    assert "Q2 Report" in result
    assert "pending" in result


# ─────────────────────────────────────────────
# AgentLog Model Tests
# ─────────────────────────────────────────────

def test_agentlog_has_correct_tablename():
    """AgentLog must map to the 'agent_logs' table in PostgreSQL."""
    assert AgentLog.__tablename__ == "agent_logs"


def test_agentlog_has_required_columns():
    """AgentLog must have id, task_id, agent_name, action, success columns."""
    columns = [col.name for col in AgentLog.__table__.columns]
    assert "id" in columns
    assert "task_id" in columns
    assert "agent_name" in columns
    assert "action" in columns
    assert "success" in columns


def test_agentlog_default_success_is_true():
    """A new AgentLog should default to success=True."""
    log = AgentLog(task_id=1, agent_name="Planner", action="decompose_task")
    assert log.success is True


def test_agentlog_repr_contains_agent_name():
    """The repr of an AgentLog should show the agent name and action."""
    log = AgentLog(task_id=1, agent_name="Executor", action="run_query", success=False)
    result = repr(log)
    assert "Executor" in result
    assert "run_query" in result
