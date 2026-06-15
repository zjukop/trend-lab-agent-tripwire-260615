# AgentTripwire

Canary secrets for coding agents. This minimal starter plants harmless honeytokens and scans files/log text for access markers so you can demo a defensive tripwire locally.

## Quick start

```bash
python -m venv .venv && source .venv/bin/activate
pip install -e .
agent-tripwire plant
agent-tripwire scan .
```

## Commands

- `agent-tripwire plant` creates `.agent-tripwire/canaries.env` with fake secrets.
- `agent-tripwire scan PATH` reports files containing planted canary values.
- `agent-tripwire demo` plants and triggers a tiny demo incident.

All generated secrets are fake and safe for demos.
