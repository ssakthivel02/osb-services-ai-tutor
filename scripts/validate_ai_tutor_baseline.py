#!/usr/bin/env python3
from __future__ import annotations

import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
POLICY = json.loads((ROOT / 'config/tutor-policy.json').read_text(encoding='utf-8'))
SOURCES = json.loads((ROOT / 'config/source-policy.json').read_text(encoding='utf-8'))


def require(condition: bool, message: str) -> None:
    if not condition:
        raise AssertionError(message)


def main() -> int:
    require(POLICY['apiPrefix'].startswith('/api/v1/'), 'API must be versioned')
    require(POLICY['requireAuthentication'] is True, 'Authentication required')
    require(POLICY['enforceTenantIsolation'] is True, 'Tenant isolation required')
    require(POLICY['allowClientTenantOverride'] is False, 'Tenant override must be blocked')
    require({'en-GB', 'ta-IN'} <= set(POLICY['supportedLocales']), 'English and Tamil required')
    require(POLICY['maximumInputCharacters'] <= 4000, 'Input bound too high')
    require(POLICY['maximumConversationTurns'] <= 50, 'Conversation bound too high')
    require(POLICY['requireSourceGrounding'] is True, 'Grounding required')
    require(POLICY['requireCitationsForFactualClaims'] is True, 'Citations required')
    require(POLICY['promptInjectionDefenceRequired'] is True, 'Prompt-injection defence required')
    require(POLICY['systemInstructionOverrideAllowed'] is False, 'System override forbidden')
    require(POLICY['toolAllowListRequired'] is True, 'Tool allow-list required')
    require(POLICY['childSafetyModeRequired'] is True, 'Child safety required')
    require(POLICY['allowMedicalDiagnosis'] is False, 'Medical diagnosis forbidden')
    require(POLICY['allowCredentialCollection'] is False, 'Credential collection forbidden')
    require(POLICY['privacy']['logRawPrompts'] is False, 'Raw prompt logging forbidden')
    require(SOURCES['classifications']['restricted']['eligible'] is False, 'Restricted sources forbidden')
    require(SOURCES['requireTenantMatch'] is True, 'Source tenant match required')
    print('AI tutor baseline validation passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())