# OPERATION FIRST LIGHT / Prototype 001

## Run
Python 3.10+; no external dependencies.

```sh
python -m blackmamba
python -m unittest discover -s tests -v
```

## Implemented scope
A deterministic, offline, single-step dispatcher and deny-by-default capability check with synthetic failed-login triage. This is not model inference, a SOC, a sandbox or a production authorization boundary.

## Threat model
Untrusted payloads may be malformed. Unknown and unauthorized capabilities are rejected. The tool registry is fixed by trusted application code. A caller with arbitrary Python execution can bypass this in-process policy. No real telemetry, external network access or remediation is implemented.

## Verification
Tests are supplied; execution status must be confirmed independently. No benchmarks or AI accuracy claims yet.

## Next gate
Add a local model adapter, enforce process isolation and resource limits, and measure performance on declared hardware.
