# DJ AI — AI Documentary Studio

A free-first, provider-independent workspace for turning a story idea into a researched script, connected scene prompts, generated media assets, review feedback, and an editable documentary package.

## Current scope

The first milestone is an orchestration MVP, not an unlimited free video generator.

- Story and project creation
- Structured scene planning and prompt versioning
- Human approval checkpoints
- Provider adapter interfaces (mock provider first)
- Asset and generation-job tracking
- Feedback and creator preference memory
- RAG-ready project memory
- Local FFmpeg assembly integration (later milestone)

## Important provider constraints

- Google Flow is treated as a manual/optional provider unless Google documents a supported public API for the required workflow.
- Text/image model free tiers have quotas and may have data-use conditions.
- High-quality video generation is not assumed to be unlimited or free.
- No Gmail passwords, browser-session scraping, or account-limit workarounds.
- API keys are supplied by the repository owner through environment variables and are never committed.

## Architecture

- Frontend: React + Vite (planned)
- Backend: Python + FastAPI
- Initial persistence: SQLite
- Later retrieval: ChromaDB or FAISS
- Media assembly: FFmpeg
- Provider strategy: adapters with mock/local-first fallbacks

## Run the backend

```bash
cd backend
python -m venv .venv
# Windows PowerShell: .venv\Scripts\Activate.ps1
# macOS/Linux: source .venv/bin/activate
pip install -r requirements.txt
uvicorn app.main:app --reload
```

Open http://127.0.0.1:8000/docs

## Configuration

Copy `.env.example` to `.env`. The initial backend does not require any external API key.

## Roadmap

See [docs/ARCHITECTURE.md](docs/ARCHITECTURE.md) and [docs/API_MATRIX.md](docs/API_MATRIX.md).
