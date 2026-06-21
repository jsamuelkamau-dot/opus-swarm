"""
Opus Swarm — Logging Tests
Engineering Domain 4: Logging and Observability

These tests verify that the logging system is correctly configured
and that get_logger returns a usable structured logger.
"""

import pytest
from unittest.mock import patch, MagicMock


def test_get_logger_returns_logger():
    """get_logger should return a structlog BoundLogger."""
    from core.logging import get_logger
    logger = get_logger("test_module")
    assert logger is not None


def test_get_logger_has_info_method():
    """The logger returned must have an .info() method."""
    from core.logging import get_logger
    logger = get_logger("test_module")
    assert hasattr(logger, "info")


def test_setup_logging_runs_without_error():
    """setup_logging() should complete without raising any exception."""
    from core.logging import setup_logging
    try:
        setup_logging()
    except Exception as e:
        pytest.fail(f"setup_logging() raised an exception: {e}")
