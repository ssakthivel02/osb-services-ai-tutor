# Architecture - osb-services-ai-tutor

## Overview
AI tutor, RAG, agent orchestration, prompt governance and AI safety. This repository is part of the OmSaravanaBhava Learning Ecosystem Enterprise Architecture v1.0.

## Context diagram
```mermaid
graph TD
    User[User / Service] --> Repo[osb-services-ai-tutor]
    Repo --> Standards[osb-engineering-standards]
    Repo --> Platform[osb-platform-foundation]
```

## Architecture principles
- Secure by default
- Observable by default
- API-first where applicable
- Documentation-as-code
- ADR-controlled change

## Dependencies
See `ROADMAP.md` for implementation sequence and dependency notes.
