# API and Provider Matrix

This document separates required integrations from optional integrations. The application must remain usable in mock/local mode without paid credentials.

## Required for the first MVP

| Capability | Initial implementation | External API required? |
|---|---|---|
| Story intake | FastAPI endpoint | No |
| Script/scene workflow | Orchestrator interface + mock implementation | No |
| Project/scene/job tracking | SQLite | No |
| Feedback/preferences | SQLite | No |
| Prompt history/versioning | SQLite | No |
| RAG | Start with SQLite metadata; add local Chroma/FAISS later | No hosted API |
| Media assembly | FFmpeg integration in a later phase | No API |

## Optional model integrations

### LLM for story, script and prompts
- Candidate: Gemini Developer API via Google AI Studio (free access is limited to eligible models and quotas).
- Candidate: OpenAI API.
- Local alternative: Ollama with a small instruction model, subject to laptop speed and memory.
- Important: ChatGPT subscription access does not automatically include OpenAI API credits. API billing/entitlements are separate.
- Gemini free-tier availability is model-specific and quota-limited. Google's pricing page says free-tier content may be used to improve products; do not send sensitive material.

### Research/search
- Add a search provider only when source-backed research is implemented.
- Store source URL, title, publisher, publication date, retrieval date and claim-to-source links.
- Do not present model-generated facts as verified facts.

### Image generation
- Provider adapter only. Free hosted credits are optional and may change.
- Local open-weight image generation is possible only if compatible hardware/resources are available; the user's 16 GB laptop should not be assumed capable of fast high-resolution generation.

### Video generation
- Google Flow is a browser-based product; do not assume it exposes a supported public API for automating its workspace.
- Google's current Gemini API video guide documents Gemini Omni Flash (`gemini-omni-1.1-flash`) for video generation and conversational editing. The Veo 3.1 Preview Gemini API model IDs were shut down on October 22, 2026. Do not code against the retired preview IDs. Check current model access, pricing, quotas and region eligibility before enabling this adapter.
- Hosted high-quality video generation must be treated as quota-limited or paid unless the provider explicitly documents otherwise.
- Open-weight video models can be evaluated for local/self-hosted use, but GPU requirements make them unsuitable as a guaranteed free local path on a 16 GB RAM laptop.
- Browser automation is a fragile optional adapter, not the core architecture. It must respect provider terms and account security.

### Voice and music
- First choice: user's own recorded narration.
- Optional local TTS: Piper or Kokoro, subject to voice/model licence.
- Music: YouTube Audio Library or other properly licensed tracks. Track-specific attribution and usage terms must be checked.

## Secrets and security
- API keys belong in local environment variables or a secret manager, never in source control.
- Never collect Gmail passwords.
- Never create multiple accounts to evade quotas.
- Show estimated provider cost/credit use before generation where provider data is available.
- Require human approval before expensive generation and before final export.

## Official references
- Gemini API pricing: https://ai.google.dev/gemini-api/docs/pricing
- Gemini API video generation: https://ai.google.dev/gemini-api/docs/video
- OpenAI API pricing: https://openai.com/api/pricing/
- Ollama: https://ollama.com/
- FFmpeg: https://ffmpeg.org/
