"""
Opus Swarm — Application Entry Point
Engineering Domain 5: Backend Routing and APIs

This is the root file that starts the entire Opus Swarm system.
It creates the FastAPI application, registers all routes,
and wires up configuration and logging at startup.
"""

from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from contextlib import asynccontextmanager

from api import tasks_router
from core import get_settings, setup_logging

settings = get_settings()


@asynccontextmanager
async def lifespan(app: FastAPI):
    """
    Startup and shutdown lifecycle manager.
    Everything before 'yield' runs at startup.
    Everything after 'yield' runs at shutdown.
    """
    # --- STARTUP ---
    setup_logging()
    logger = __import__("core").get_logger(__name__)
    logger.info(
        "opus_swarm_starting",
        version=settings.app_version,
        env=settings.app_env,
    )
    yield
    # --- SHUTDOWN ---
    logger.info("opus_swarm_stopping")


app = FastAPI(
    title="Opus Swarm",
    description="Production-Grade Autonomous Enterprise Operations Agent Swarm",
    version=settings.app_version,
    docs_url="/docs",
    redoc_url="/redoc",
    lifespan=lifespan,
)

# --- CORS Middleware ---
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"] if settings.app_env == "development" else [],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# --- API Routers ---
app.include_router(tasks_router)


@app.get("/health", tags=["System"])
async def health_check():
    """
    Health check endpoint.
    Used by load balancers and Kubernetes to verify the service is alive.
    """
    return {
        "status": "healthy",
        "version": settings.app_version,
        "env": settings.app_env,
    }


@app.get("/", tags=["System"])
async def root():
    """Root endpoint — confirms the API is running."""
    return {"message": "Opus Swarm is running", "docs": "/docs"}
