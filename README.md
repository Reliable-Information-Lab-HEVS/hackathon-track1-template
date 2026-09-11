# Track 1 application template

Starter skeleton for the Track 1 documentation assistant. Read the task, corpus,
rules, and the full submission/tool contract on the website:
<https://hackathon-armasuisse.github.io/tracks/track-1/>.

This template uses FastAPI and Uvicorn as a simple starting point, for more information see this [description](https://www.geeksforgeeks.org/python/fastapi-uvicorn/). We note that usage of this template is **optional**. You can start from scratch or use your own framework, as long as you meet the requirements.

## What's here

- `app/main.py`: the `/chat` endpoint skeleton; implement your assistant here.
- `inference.env.example`: the inference endpoint variables we pass at deploy.
- `Dockerfile`: builds and runs the app on port 8080.
- `compose.yaml`: runs the app behind a TLS-terminating reverse proxy.
- `Caddyfile`: the reverse proxy configuration, replace `N` with your team number.

The corpus, the tool seed data (`tools_seed_data.json`), and the example
questions are distributed separately as an encrypted zip, see the website.

## Deploying on your team VM

Your VM already has a TLS certificate and a public hostname,
`llmhack-team-N.hackathon.intlab.ch`. `compose.yaml` in this repository runs two
containers: **Caddy**, which terminates TLS on that hostname, and **your app**,
which Caddy reaches at `app:8080` on the internal network. Before starting to build, do the following two steps:

1. Copy `inference.env.example` to `inference.env` and fill in the values for your team.
2. In the `Caddyfile`, replace `N` with your team number.


