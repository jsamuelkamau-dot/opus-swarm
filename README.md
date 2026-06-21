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
| Phase 5 | Database Schemas and Migrations | 🔄 In Progress |
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
Executor agents run each step, the Verifier checks every output,
and the Reporter assembles the final result.

---

## System Architecture

```
Ingest Layer      → emails, PDFs, APIs, databases
Orchestration     → LangGraph stateful multi-agent graph
Agent Layer       → Supervisor / Planner / Executor / Verifier / Researcher / Reporter
Memory Layer      → PostgreSQL + Redis + Vector DB
Audit Layer       → structured logging, decision trail, human escalation
Observability     → Prometheus, Grafana, OpenTelemetry
Deployment        → Docker, Kubernetes, GitHub Actions CI/CD
Dashboard         → React frontend
```

---

## Tech Stack

| Layer | Technology |
|-------|-----------|
| Language | Python 3.11+ |
| API Framework | FastAPI |
| Agent Orchestration | LangGraph |
| Structured DB | PostgreSQL |
| Cache / Queue | Redis |
| Vector Memory | ChromaDB (local) → Pinecone (cloud) |
| Containerization | Docker + Docker Compose |
| Orchestration | Kubernetes |
| CI/CD | GitHub Actions |
| Frontend | React |
| Monitoring | Prometheus + Grafana |
| Error Tracking | Sentry |
| Eval Tracking | MLflow |

---

## Project Structure

```
opus-swarm/
├── agents/          # Agent definitions (Supervisor, Planner, Executor, etc.)
├── api/             # FastAPI routes and request handlers
├── core/            # Shared config, logging, and base utilities
│   └── config.py    # ✅ Settings loader — reads .env into typed config
├── memory/          # PostgreSQL, Redis, and vector DB clients
├── tools/           # Agent-callable tools (web search, file ops, APIs)
├── dashboard/       # React frontend
├── tests/           # Pytest test suite
├── docs/            # Architecture diagrams and documentation
├── scripts/         # Dev and ops utility scripts
├── infra/           # Docker, Kubernetes, Terraform configs
├── pyproject.toml   # ✅ Project identity and tool configuration
├── requirements.txt # ✅ Pinned Python dependencies
└── .env.example     # ✅ Environment variable template
```

---

## Engineering Domains Covered

1. Git / Version Control
2. Project Structure and Build Systems
3. Environment Variables and Secrets
4. Logging and Observability
5. Database Schemas and Migrations
6. Backend Routing and APIs
7. Authentication and Authorization
8. Frontend State and Routing
9. Styling Systems
10. Containerization and Deployment
11. CI/CD Pipelines
12. Monitoring and Alerting
13. Agent Orchestration Patterns
14. Testing Strategy
