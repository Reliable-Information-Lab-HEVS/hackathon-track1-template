# Track 1 — application template

Starter skeleton for the Track 1 documentation assistant. Read the task, corpus,
rules, and the full submission/tool contract on the website:
<https://hackathon-armasuisse.github.io/tracks/track-1/>.

We note that usage of this template is **optional**. You can start from scratch or use your own framework, as long as you meet the requirements.

## What's here

- `app/main.py` — the `/chat` endpoint skeleton; implement your assistant here.
- `inference.env.example` — the inference endpoint variables we pass at deploy.
- `Dockerfile` — builds and runs the app on port 8080.

The corpus, the tool seed data (`tools_seed_data.json`), and the example
questions are distributed separately as an encrypted zip — see the website.

## Run

```bash
docker build -t track1 .
docker run -p 8080:8080 track1
```
