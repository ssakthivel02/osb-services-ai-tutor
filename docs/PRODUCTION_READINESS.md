# AI Tutor Production Readiness

Production is **NO-GO** until every applicable control has evidence.

## Required evidence

- Running authenticated `/api/v1/tutor` service
- Validated identity and tenant claims
- Cross-tenant negative integration tests
- English and Tamil evaluation corpus
- Child-profile and guardian-control tests
- Prompt-injection and indirect-injection red-team tests
- Source eligibility and citation-resolution tests
- Versioned system prompts and model configuration
- Tool allow-list, least privilege and argument-validation tests
- Secret-leakage and credential-harvesting tests
- Medical, financial and political-safety tests
- Privacy and retention review
- Load, timeout, rate-limit and dependency-failure tests
- Dashboards, alert routing and incident ownership
- Rollback and recovery drill

## Release record

Record commit SHA, policy version, prompt version, model version, source-index version, evaluation evidence, risks, approvers and rollback target.