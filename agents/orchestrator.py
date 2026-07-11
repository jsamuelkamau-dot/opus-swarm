"""
Opus Swarm — Agent Orchestrator
Engineering Domain 7: Agent Orchestration

The orchestrator is the coordination layer for the swarm.
It receives a task, selects the right agent, runs that agent,
and tracks the status of the work from start to finish.
"""

from dataclasses import dataclass, field
from datetime import datetime, timezone
from typing import Callable


AgentHandler = Callable[[str], str]


@dataclass
class OrchestrationResult:
    """
    The final receipt for one orchestrated task.

    Think of this like the tracking slip for a delivery:
    who handled it, what happened, and whether it finished successfully.
    """

    task: str
    selected_agent: str
    status: str
    output: str
    started_at: datetime
    completed_at: datetime | None = None
    events: list[str] = field(default_factory=list)


class AgentOrchestrator:
    """
    Coordinates agent work for Opus Swarm.

    Responsibilities:
    1. Accept a task from the backend/API layer.
    2. Pick the best available agent for that task.
    3. Run the selected agent.
    4. Track status events for debugging and audit trails.
    """

    def __init__(self) -> None:
        self.agents: dict[str, AgentHandler] = {
            "Planner": self._planner_agent,
            "Executor": self._executor_agent,
            "Reporter": self._reporter_agent,
        }

    def orchestrate(self, task: str) -> OrchestrationResult:
        """
        Run one task through the orchestration flow.

        The flow is:
        task comes in -> agent is selected -> agent runs -> result is returned.
        """
        started_at = datetime.now(timezone.utc)
        events: list[str] = ["task_received"]

        selected_agent = self.select_agent(task)
        events.append(f"agent_selected:{selected_agent}")

        try:
            output = self.agents[selected_agent](task)
            status = "completed"
            events.append("task_completed")
        except Exception as exc:
            output = str(exc)
            status = "failed"
            events.append("task_failed")

        return OrchestrationResult(
            task=task,
            selected_agent=selected_agent,
            status=status,
            output=output,
            started_at=started_at,
            completed_at=datetime.now(timezone.utc),
            events=events,
        )

    def select_agent(self, task: str) -> str:
        """
        Pick an agent based on the task text.

        This is intentionally simple for the first version.
        Later, this can become scoring, routing rules, or model-based planning.
        """
        normalized_task = task.lower()

        if "plan" in normalized_task or "break down" in normalized_task:
            return "Planner"

        if "report" in normalized_task or "summary" in normalized_task:
            return "Reporter"

        return "Executor"

    def _planner_agent(self, task: str) -> str:
        """Create a simple plan for a task."""
        return f"Planner created a step-by-step plan for: {task}"

    def _executor_agent(self, task: str) -> str:
        """Perform the default execution work for a task."""
        return f"Executor completed the task: {task}"

    def _reporter_agent(self, task: str) -> str:
        """Create a simple report for a task."""
        return f"Reporter generated a summary for: {task}"
