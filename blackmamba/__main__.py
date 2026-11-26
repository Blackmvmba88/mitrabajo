import json
from .core import Orchestrator, Policy

def main():
    engine = Orchestrator(Policy(frozenset({"triage"})))
    print(json.dumps({"mode": "synthetic-offline", "result": engine.run("triage", {"failed_logins": 12})}, indent=2))

if __name__ == "__main__":
    main()
