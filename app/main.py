"""Track 1 assistant — minimal skeleton. Implement your assistant here.

See README.md for the full contract (endpoints, docker run command, tools).
"""

import os

from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
from pydantic import BaseModel

app = FastAPI(title="Track 1 assistant")

CORPUS_DIR = os.environ.get("CORPUS_DIR", "/corpus")

# Inference endpoint (OpenAI-compatible) — see inference.env.example.
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("MODEL")  # default chat model, used when a request has no `model`

# Chat models a request may ask for in its optional `model` field. Both required
# models must stay in this set; add others if you support them.
SUPPORTED_MODELS = {
    "CSCS-Inference/google/gemma-4-31B-it",
    "RCP-AIaaS/swiss-ai/Apertus-large",
}
if MODEL:
    SUPPORTED_MODELS.add(MODEL)


class ModelNotAvailable(Exception):
    pass


@app.exception_handler(ModelNotAvailable)
def model_not_available(request: Request, exc: ModelNotAvailable) -> JSONResponse:
    return JSONResponse(status_code=400, content={"error": "model not available"})


def pick_model(requested: str | None) -> str:
    """The chat model for this request: the requested one, else the MODEL default.
    Never falls back silently: an unsupported model is a 400."""
    model = requested or MODEL
    if model not in SUPPORTED_MODELS:
        raise ModelNotAvailable()
    return model


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
