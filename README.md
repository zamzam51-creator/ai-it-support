# AI IT Support

AI-assisted, human-controlled IT support automation.

## Goal
Build workflows and AI agents that automate IT ticket triage and routine tasks,
and escalate sensitive issues to people.

## Folders
- `api/` – FastAPI backend
- `agents/` – AI agents (read-only first, human approval for actions)
- `n8n/` – workflow automations
- `database/` – PostgreSQL schema
- `scripts/` – IT tools (health checks)
- `tests/` – automated tests
- `docs/` – notes and documentation

## Health check tool

`scripts/health_check.py` checks a computer and a website, then reports the results as JSON.

### What it checks

| Check | What it tests | Fails when |
|---|---|---|
| disk | Free space on the local drive | The disk is 90% full or more, or the drive can't be read  |
| dns | The domain resolves to an IP address (A record) |The name can't be turned into an IP address (it doesn't exist, or DNS isn't reachable)  |
| port | Port 443 (HTTPS) accepts a TCP connection |Port 443 refuses the connection or doesn't answer within 3 seconds  |
| website | An HTTPS request to the domain |The site answers with an error code (400 or higher, like 404), or can't be reached at all |

### Setup

```
pip install -r requirements.txt
```

### Run

```
python scripts/health_check.py example.com
```

If no domain is given, it checks `example.com`. Results are printed and saved to `report.json`.

### Sample output

```

  {
    "check": "dns",
    "ok": true,
    "detail": "142.250.202.110"
  },
  {
    "check": "port",
    "ok": true,
    "detail": "google.com:443 is open"
  },
  {
    "check": "website",
    "ok": true,
    "detail": "200 in 664 ms"
  }

4 of 4 checks passed

```

### Run the tests

```
python -m pytest
```

## Status
Prototype in development. Synthetic data only.