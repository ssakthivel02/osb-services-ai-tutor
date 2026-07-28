# AI Tutor Quality Evaluation

Evaluate English and Tamil separately across every supported age band and tenant.

## Core measures

- Grounded factual accuracy
- Citation precision and citation coverage
- Retrieval recall
- Instruction following
- Pedagogical usefulness
- Age appropriateness
- Harmful-content refusal quality
- Prompt-injection resistance
- Tool-call correctness
- Latency and fallback rate

## Hard release gates

A release fails for any cross-tenant disclosure, unsupported factual claim without required citation, restricted-source use, invalid citation, child-safety bypass, secret disclosure, unauthorised tool call or system-instruction override.

## Evidence

Store policy version, prompt version, model version, source-index version, evaluation dataset version, code commit, results, known limitations, approvers and release decision. Exclude raw personal conversations from evaluation artefacts.