"""
Opus Swarm — API Package

This package exposes FastAPI routers used by the application entry point.
"""

from api.tasks import router as tasks_router

__all__ = ["tasks_router"]
