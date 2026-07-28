# ADR 0001: Grounded, Safe and Tenant-Scoped Tutoring

## Status

Accepted for baseline implementation.

## Context

The tutor serves multilingual educational and devotional content to adults and children. Generative responses create risks involving hallucination, prompt injection, source poisoning, tenant leakage, unsafe advice, privacy and tool abuse.

## Decision

Use an authenticated, tenant-scoped retrieval-augmented tutoring pipeline. System instructions are immutable at request time. Retrieved text and tool output are untrusted data, not executable instructions. Factual claims require citations to eligible retrieved sources. Restricted and needs-review sources are excluded by default.

All tools require explicit allow-listing, least privilege and argument validation. Child profiles require age-aware safety mode and guardian controls. Raw prompts and responses are not logged. Model, prompt, policy, source index and tool configuration are independently versioned and reversible.

## Consequences

Ungrounded answers must be qualified or refused. Quality optimisation cannot override tenant, child-safety, privacy or source-trust controls. Production remains blocked until integration, red-team, bilingual evaluation, load and recovery evidence exists.