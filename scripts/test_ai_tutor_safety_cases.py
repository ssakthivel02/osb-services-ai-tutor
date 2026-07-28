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
    require(POLICY['allowClientTenantOverride'] is False, 'Cross-tenant override risk')
    require(POLICY['systemInstructionOverrideAllowed'] is False, 'Prompt injection risk')
    require(POLICY['allowSecretDisclosure'] is False, 'Secret disclosure risk')
    require(POLICY['allowCredentialCollection'] is False, 'Credential harvesting risk')
    require(POLICY['allowMedicalDiagnosis'] is False, 'Unsafe medical advice risk')
    require(POLICY['allowPersonalFinancialAdvice'] is False, 'Unsafe financial advice risk')
    require(POLICY['allowPoliticalPersuasion'] is False, 'Political manipulation risk')
    require(POLICY['childSafetyModeRequired'] is True, 'Child safety bypass risk')
    require(POLICY['guardianControlsRequired'] is True, 'Guardian-control bypass risk')
    require(POLICY['maximumInputCharacters'] <= 4000, 'Prompt amplification risk')
    require(POLICY['maximumOutputCharacters'] <= 8000, 'Output amplification risk')
    require(POLICY['maximumConversationTurns'] <= 50, 'Unbounded session risk')
    require(POLICY['privacy']['logRawPrompts'] is False, 'Prompt leakage risk')
    require(POLICY['privacy']['logRawResponses'] is False, 'Response leakage risk')
    require(SOURCES['classifications']['needs_review']['eligible'] is False, 'Unverified-source risk')
    require(SOURCES['classifications']['restricted']['eligible'] is False, 'Restricted-source risk')
    print('AI tutor negative safety cases passed.')
    return 0


if __name__ == '__main__':
    raise SystemExit(main())