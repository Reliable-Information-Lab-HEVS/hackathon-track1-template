"""Track 1 assistant — minimal skeleton. Implement your assistant here.

See README.md for the full contract (endpoints, docker run command, tools).
"""

import os

from fastapi import FastAPI
from pydantic import BaseModel

app = FastAPI(title="Track 1 assistant")

CORPUS_DIR = os.environ.get("CORPUS_DIR", "/corpus")

# Inference endpoint (OpenAI-compatible LiteLLM proxy) — see inference.env.example.
OPENAI_BASE_URL = os.environ.get("OPENAI_BASE_URL")
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
MODEL = os.environ.get("MODEL")


class ChatRequest(BaseModel):
    message: str
    session_id: str


@app.post("/chat")
def chat(req: ChatRequest) -> dict:
    # TODO: implement your assistant.

    return {"answer": "TODO: not implemented", "sources": []}


@app.get("/health")
def health() -> dict:
    return {"ok": True}


if __name__ == "__main__":
    import uvicorn

    uvicorn.run(app, host="0.0.0.0", port=8080)
