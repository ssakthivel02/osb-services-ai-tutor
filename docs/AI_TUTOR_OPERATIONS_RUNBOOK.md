# AI Tutor Operations Runbook

## Health checks

Verify API health, identity provider, retrieval service, source index freshness, model endpoint, safety classifier, citation resolver, tool gateway, cache and telemetry pipeline.

## Key metrics

Track request rate, success rate, p50/p95/p99 latency, input/output size, token usage, grounding rate, citation-validity rate, refusal rate, safety-block rate, empty-retrieval rate, fallback rate, tenant-filter failures and tool-call failures.

## Alerts

- Severity 1: cross-tenant disclosure, child-safety bypass, secret leakage, unauthorised tool use or sustained outage.
- Severity 2: citation failure spike, grounding degradation, model dependency outage, retrieval staleness or high latency.
- Severity 3: locale-specific quality drift, fallback increase or non-critical dependency degradation.

## Incident response

1. Capture request ID, deployment version, policy version and model version without raw prompts.
2. Disable affected model, tool or retrieval strategy using feature flags.
3. Fall back to verified, tenant-scoped, age-safe content.
4. Revoke compromised credentials and invalidate unsafe caches.
5. Preserve sanitised evidence and notify service, security, privacy and safeguarding owners.
6. Add regression tests before re-enablement.

## Recovery

Restore the last approved policy, prompt, model, source index and tool configuration. Revalidate tenant isolation, child safety, citation integrity and latency before reopening traffic.