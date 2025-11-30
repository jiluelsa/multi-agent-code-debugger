import json, time
from pathlib import Path


LOGFILE = Path("agent_logs.jsonl")


def log(agent_name: str, event: str, payload: dict):
    entry = {"ts": time.time(), "agent": agent_name, "event": event, "payload": payload}
    with open(LOGFILE, "a", encoding="utf-8") as f:
        f.write(json.dumps(entry) + "\n")
