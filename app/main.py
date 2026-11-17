"""Track 1 assistant — minimal skeleton. Implement your assistant here.

See README.md for the full contract (endpoints, docker run command, tools).
"""

import json
import os
import time
import urllib.request

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Track 1 assistant")

CORPUS_DIR = os.environ.get("CORPUS_DIR", "/corpus")

# Inference endpoint (OpenAI-compatible) — see inference.env.example.
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("MODEL")  # default chat model, used when a request has no `model`

# A request may ask for any model the inference endpoint serves, in its optional
# `model` field. We check it against the endpoint's /models list, cached for a
# few minutes so the check does not eat into your rate limit.
MODELS_TTL_SECONDS = 600
_models_cache: tuple[float, set[str]] = (0.0, set())


def available_models() -> set[str]:
    global _models_cache
    fetched_at, models = _models_cache
    if time.monotonic() - fetched_at < MODELS_TTL_SECONDS:
        return models
    try:
        req = urllib.request.Request(
            f"{OPENAI_BASE_URL.rstrip('/')}/models",
            headers={"Authorization": f"Bearer {OPENAI_API_KEY}"},
        )
        with urllib.request.urlopen(req, timeout=10) as resp:
            models = {m["id"] for m in json.load(resp)["data"]}
        _models_cache = (time.monotonic(), models)
    except Exception:
        pass  # endpoint unreachable: keep the last list we had
    return _models_cache[1]


class ModelNotAvailable(Exception):
    pass


@app.exception_handler(ModelNotAvailable)
def model_not_available(request: Request, exc: ModelNotAvailable) -> JSONResponse:
    return JSONResponse(status_code=400, content={"error": "model not available"})


def pick_model(requested: str | None) -> str:
    """The chat model for this request: the requested one, else the MODEL default.
    Never falls back silently: a model the endpoint does not serve is a 400."""
    if not requested or requested == MODEL:
        return MODEL
    if requested not in available_models():
        raise ModelNotAvailable()
    return requested


class ChatRequest(BaseModel):
    message: str
    session_id: str
    model: str | None = None     # optional: chat model for this request


@app.post("/chat")
def chat(req: ChatRequest) -> dict:
    model = pick_model(req.model)  # use this model for the chat completions
    # TODO: implement your assistant.

    return {"answer": "TODO: not implemented", "sources": []}


@app.get("/health")
def health() -> dict:
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
