# Opus Swarm

**Production-Grade Autonomous Enterprise Operations Agent Swarm**

Opus Swarm is a self-evaluating, production-hardened multi-agent AI system
for enterprise business process automation.

---

## Build Status

| Phase | Domain | Status |
|-------|--------|--------|
| Phase 1 | Git / Version Control | ✅ Complete |
| Phase 2 | Project Structure and Build Systems | ✅ Complete |
| Phase 3 | Environment Variables and Secrets | ✅ Complete |
| Phase 4 | Logging and Observability | ✅ Complete |
| Phase 5 | Database Schemas and Migrations | ✅ Complete |
| Phase 6 | Backend Routing and APIs | ⏳ Upcoming |
| Phase 7 | Agent Orchestration | ⏳ Upcoming |
| Phase 8 | Authentication and Authorization | ⏳ Upcoming |
| Phase 9 | Frontend State and Routing | ⏳ Upcoming |
| Phase 10 | Containerization and Deployment | ⏳ Upcoming |

---

## What This System Does

Opus Swarm ingests enterprise data (emails, tickets, documents, invoices, APIs)
and uses a coordinated team of AI agents to:

- Decompose complex business tasks into executable steps
- Assign work to specialized agents (Supervisor, Planner, Executor, Verifier, Researcher, Reporter)
- Execute safely through controlled tools
- Verify outputs and self-correct failures
- Log every decision with full audit trails
- Escalate to human review when confidence is low

---

## Example Task

```
"Handle Q2 financial reporting, vendor invoice reconciliation, and compliance check."
```

The Supervisor agent receives this task, the Planner breaks it into steps,
Executor agents run each step, and the Verifier confirms the outputs before
the Reporter generates the final summary.

---

## Architecture

```
External Input
      │
      ▼
┌─────────────┐
│  Supervisor │  ← Receives task, delegates work
└──────┬──────┘
       │
       ▼
┌─────────────┐
│   Planner   │  ← Breaks task into steps
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Executor   │  ← Runs each step with tools
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Verifier   │  ← Checks output quality
└──────┬──────┘
       │
       ▼
┌─────────────┐
│  Reporter   │  ← Generates final output
└─────────────┘
```

---

## Project Structure

```
opus-swarm/
├── agents/          # Agent definitions (Supervisor, Planner, Executor, etc.)
├── api/             # FastAPI routes and request handlers
├── core/            # Shared config, logging, database models
├── dashboard/       # Frontend UI (Phase 9)
├── docs/            # Architecture and API documentation
├── infra/           # Docker, deployment configs
├── tests/           # All test files
├── main.py          # Application entry point
├── requirements.txt # Python dependencies
└── pyproject.toml   # Build and tool configuration
```

---

## Phase Progress

### ✅ Phase 1 — Git / Version Control
- Git repository initialized
- `.gitignore` configured for Python, secrets, IDE files
- Initial commit established

### ✅ Phase 2 — Project Structure and Build Systems
- Folder structure created: agents/, api/, core/, dashboard/, docs/, infra/, tests/
- `pyproject.toml` configured with pytest, black, ruff, mypy
- `requirements.txt` pinned with all production dependencies

### ✅ Phase 3 — Environment Variables and Secrets
- `.env.example` created with all required keys documented
- `core/config.py` implemented with Pydantic Settings
- `.env` excluded from Git via `.gitignore`

### ✅ Phase 4 — Logging and Observability
- `core/logging.py` implemented with structlog
- JSON-structured logging with context binding
- 3 tests passing

### ✅ Phase 5 — Database Schemas and Migrations
- `core/database.py` — async SQLAlchemy engine and session factory
- `core/models.py` — Task and AgentLog table definitions
- `tests/test_models.py` — 8 tests passing
- Alembic configured for database migrations

### ⏳ Phase 6 — Backend Routing and APIs
- FastAPI route structure
- Health check endpoint
- Task CRUD endpoints

### ⏳ Phase 7 — Agent Orchestration
### ⏳ Phase 8 — Authentication and Authorization
### ⏳ Phase 9 — Frontend State and Routing
### ⏳ Phase 10 — Containerization and Deployment
