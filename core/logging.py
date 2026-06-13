"""
Opus Swarm — Structured Logging
Engineering Domain 4: Logging and Observability

This module configures structured JSON logging for the entire system.
Every agent action, decision, and error is recorded through this logger.
"""

import logging
import sys
import structlog
from core.config import get_settings


def setup_logging() -> None:
    """
    Configure structured logging for Opus Swarm.
    Call this once at application startup before any agents run.
    """
    settings = get_settings()

    log_level = getattr(logging, settings.log_level.upper(), logging.INFO)

    structlog.configure(
        processors=[
            structlog.contextvars.merge_contextvars,
            structlog.stdlib.add_log_level,
            structlog.stdlib.add_logger_name,
            structlog.processors.TimeStamper(fmt="iso"),
            structlog.processors.StackInfoRenderer(),
            structlog.processors.format_exc_info,
            structlog.dev.ConsoleRenderer()
            if settings.app_env == "development"
            else structlog.processors.JSONRenderer(),
        ],
        wrapper_class=structlog.make_filtering_bound_logger(log_level),
        context_class=dict,
        logger_factory=structlog.PrintLoggerFactory(),
    )

    # Also configure stdlib logging to route through structlog
    logging.basicConfig(
        format="%(message)s",
        stream=sys.stdout,
        level=log_level,
    )


def get_logger(name: str) -> structlog.BoundLogger:
    """
    Return a named structured logger for a given module or agent.

    Usage:
        logger = get_logger(__name__)
        logger.info("agent_started", agent="supervisor", task_id="abc123")
    """
    return structlog.get_logger(name)
