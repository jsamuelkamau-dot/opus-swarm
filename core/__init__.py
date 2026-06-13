"""
Opus Swarm — Core Package
This package exposes the shared configuration and logging used across all agents.
"""

from core.config import get_settings, Settings
from core.logging import get_logger, setup_logging

__all__ = [
    "get_settings",
    "Settings",
    "get_logger",
    "setup_logging",
]
