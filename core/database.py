"""
Opus Swarm — Core Database Connection
Engineering Domain 5: Database Schemas and Migrations

This module creates the async SQLAlchemy engine and session factory
that every part of the system uses to talk to PostgreSQL.
"""

from sqlalchemy.ext.asyncio import create_async_engine, AsyncSession, async_sessionmaker
from sqlalchemy.orm import DeclarativeBase
from core.config import get_settings

# ─────────────────────────────────────────────
# Engine
# The engine is the single connection to the database.
# Think of it like a phone line — one line shared by the whole system.
# ─────────────────────────────────────────────
settings = get_settings()

engine = create_async_engine(
    settings.postgres_url,
    echo=False,        # Set to True locally to see every SQL query printed
    pool_size=10,      # How many connections to keep open at once
    max_overflow=20,   # Extra connections allowed during traffic spikes
)

# ─────────────────────────────────────────────
# Session Factory
# A session is one conversation with the database.
# The factory creates a fresh session whenever we need one.
# ─────────────────────────────────────────────
AsyncSessionLocal = async_sessionmaker(
    bind=engine,
    class_=AsyncSession,
    expire_on_commit=False,
)

# ─────────────────────────────────────────────
# Base Model
# All database table definitions (models) will inherit from this.
# SQLAlchemy uses it to know which classes map to which tables.
# ─────────────────────────────────────────────
class Base(DeclarativeBase):
    pass


# ─────────────────────────────────────────────
# Dependency: get_db
# Used by FastAPI routes to get a fresh database session per request.
# It opens a session, yields it to the route, then closes it cleanly.
# ─────────────────────────────────────────────
async def get_db() -> AsyncSession:
    async with AsyncSessionLocal() as session:
        try:
            yield session
            await session.commit()
        except Exception:
            await session.rollback()
            raise
        finally:
            await session.close()
