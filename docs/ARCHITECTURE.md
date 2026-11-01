# DJ AI — Architecture and Delivery Scope

## Product goal

A user supplies a documentary idea/story. DJ AI structures it into a research plan, narration script, visual bible, scene-by-scene prompts and media jobs. The user approves the script/prompts and each generated asset. The user can then download scene assets for manual editing; automatic assembly is a later milestone.

## MVP boundary

### Included first
1. Create and list documentary projects.
2. Store original story input.
3. Create structured scenes and prompts.
4. Version prompts instead of overwriting them.
5. Human approval/rejection checkpoints.
6. Track generation jobs and asset metadata.
7. Store explicit feedback and creator preferences.
8. Provide mock providers so the complete workflow can be tested without API keys.

### Not promised in the free MVP
- Unlimited Flow-quality video generation.
- Direct Google Flow API integration without a documented supported API.
- Fully autonomous publishing to YouTube.
- True model fine-tuning or reinforcement learning from a handful of ratings.
- Always-on cloud GPU generation under free hosting.

## Logical architecture

React UI -> FastAPI -> workflow orchestrator -> capability interfaces:
- ResearchProvider
- LLMProvider
- ImageProvider
- VideoProvider
- AudioProvider
- MediaAssembler

Persistence:
- SQLite initially for projects, scenes, prompts, jobs, assets, feedback and preferences.
- Vector retrieval (ChromaDB or FAISS) is a later module. Store source records and feedback as structured data first; embeddings must not replace the source of truth.

## Workflow states

Project:
DRAFT -> SCRIPT_REVIEW -> SCENE_REVIEW -> GENERATING -> ASSET_REVIEW -> READY_FOR_EXPORT

Scene:
DRAFT -> PROMPT_REVIEW -> APPROVED -> QUEUED -> GENERATING -> GENERATED -> ACCEPTED / REJECTED

Generation jobs must be asynchronous in production. The initial mock provider can complete synchronously for development.

## Feedback and learning

Do not call basic memory "reinforcement learning".
- Store each rating/comment with project, scene, prompt version, provider/model and asset.
- Convert explicit feedback into structured preferences only after user confirmation or high-confidence extraction.
- Retrieve relevant past preferences and successful examples with RAG.
- Rank assets using measurable criteria plus user rating.
- Consider a contextual-bandit/provider-selection experiment only after enough labelled feedback exists.
- Preserve history so improvements can be measured and reverted.

## Continuity model

Each project stores a visual bible:
- subject/character identity
- location and time period
- clothing/props
- palette and lighting
- camera language
- visual style
- previous-scene ending state
- next-scene starting state

Prompts reference the same visual bible. Where a video provider supports reference images or first/last frames, the adapter may pass them. Continuity is not guaranteed by text prompts alone.

## Security
- Never store Gmail passwords or scrape browser sessions.
- Keep API credentials server-side in environment variables/secrets.
- Do not commit .env files.
- Use explicit provider configuration and prevent accidental paid calls.
- Add request limits, file-size limits and safe file handling before public deployment.

## Milestones
1. Foundation API and mock workflow.
2. React dashboard and human approval.
3. LLM adapter for script/scene generation.
4. Research sources and citations.
5. Video/image provider adapters, only after verifying API access, quotas and terms.
6. RAG, preference retrieval and ranking.
7. FFmpeg packaging and export.
8. Deployment, monitoring and security hardening.
