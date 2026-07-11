"""
Opus Swarm — Task API Router
Engineering Domain 6: Backend Routing and APIs

This router receives task requests from clients and hands them to the
agent orchestrator. The API layer stays thin: it validates input, calls the
coordination layer, and returns a clean response.
"""

from fastapi import APIRouter, HTTPException
from pydantic import BaseModel, Field

from agents.orchestrator import AgentOrchestrator


router = APIRouter(prefix="/tasks", tags=["Tasks"])
orchestrator = AgentOrchestrator()


class TaskRequest(BaseModel):
    """Request body for creating an orchestrated task."""

    task: str = Field(
        ...,
        min_length=1,
        description="The task the swarm should complete.",
    )


class TaskResponse(BaseModel):
    """Response returned after the swarm processes a task."""

    task: str
    selected_agent: str
    status: str
    output: str
    events: list[str]


@router.post("", response_model=TaskResponse)
async def create_task(request: TaskRequest) -> TaskResponse:
    """
    Create a task and run it through the agent orchestrator.

    Flow:
    1. Receive a task from the client.
    2. Clean and validate the text.
    3. Ask the orchestrator to choose and run an agent.
    4. Return the orchestration result to the client.
    """
    cleaned_task = request.task.strip()

    if not cleaned_task:
        raise HTTPException(status_code=400, detail="Task text cannot be empty.")

    result = orchestrator.orchestrate(cleaned_task)

    return TaskResponse(
        task=result.task,
        selected_agent=result.selected_agent,
        status=result.status,
        output=result.output,
        events=result.events,
    )
