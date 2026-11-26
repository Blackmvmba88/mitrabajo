# Architecture

```mermaid
flowchart TD
  U[Enterprise client] --> G[Policy gateway]
  G --> A[Agent orchestrator]
  A --> P[Permission kernel]
  P --> R[Model router]
  R --> E[Local inference]
  R --> C[Approved cloud provider]
  P --> S[Read-only security tools]
  G --> T[Redacted audit telemetry]
  P --> T
```

Trust boundaries: client identity, agent sandbox, local runtime and external providers. Default deny; external transfer requires explicit policy. Treat model output and retrieved content as untrusted. Separate control and data planes. Use synthetic fixtures first.

ADR-001: Start with a modular monolith and explicit interfaces; distribute only after measurements justify complexity.
