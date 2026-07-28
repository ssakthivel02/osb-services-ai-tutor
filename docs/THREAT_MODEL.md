# AI Tutor Threat Model

## Protected assets

Tenant boundaries, learner identity, child safety, guardian controls, conversation history, source provenance, system instructions, tool permissions, credentials and service availability.

## Primary threats and controls

1. Cross-tenant disclosure — derive tenant scope from validated identity claims and reject client override.
2. Prompt injection — isolate system instructions, treat retrieved content as untrusted data and deny instruction override.
3. Tool abuse — use an explicit allow-list, least privilege, argument validation and auditable tool calls.
4. Hallucinated facts — require grounded answers and citations for factual claims.
5. Source poisoning — permit only eligible, tenant-matched, versioned sources.
6. Child-safety bypass — require age-aware safety mode and guardian controls.
7. Secret leakage — prohibit credential collection and secret disclosure; redact identifiers.
8. Unsafe advice — prohibit medical diagnosis, personal financial advice and political persuasion.
9. Data leakage — do not log raw prompts or responses; apply bounded retention.
10. Resource exhaustion — cap input, output, turns, requests and execution time.
11. Indirect prompt injection — strip active instructions from retrieved documents and tool output.
12. Citation spoofing — validate that every citation resolves to an eligible retrieved source.

## Release requirement

Production requires integration tests, red-team cases, bilingual quality evidence, child-safety tests, cross-tenant tests, tool-abuse tests, privacy review, load tests and rollback evidence.