"""Bounded, deterministic defensive prototype; no network or shell tools."""
from dataclasses import dataclass
from typing import Callable

@dataclass(frozen=True)
class Policy:
    allowed: frozenset[str] = frozenset()

    def authorize(self, capability: str) -> None:
        if capability not in self.allowed:
            raise PermissionError("Capability denied")

def triage(event: dict) -> dict:
    if not isinstance(event, dict):
        raise ValueError("Expected an event object")
    failures = event.get("failed_logins", 0)
    if type(failures) is not int or not 0 <= failures <= 1000000:
        raise ValueError("Invalid failed_logins")
    if failures >= 10:
        return {"priority": "high", "reason": "Synthetic failed-login threshold exceeded"}
    if failures >= 3:
        return {"priority": "medium", "reason": "Repeated failed logins"}
    return {"priority": "low", "reason": "Below synthetic thresholds"}

class Orchestrator:
    """Single-step dispatch to a fixed, trusted in-process registry."""
    def __init__(self, policy: Policy):
        self.policy = policy
        self._tools: dict[str, Callable] = {"triage": triage}

    def run(self, capability: str, payload: dict) -> dict:
        self.policy.authorize(capability)
        if capability not in self._tools:
            raise PermissionError("Unknown capability")
        return self._tools[capability](payload)
