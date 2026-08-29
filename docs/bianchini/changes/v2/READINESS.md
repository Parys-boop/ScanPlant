```json
{
  "schema_version": 1,
  "status": "ready",
  "scope_digest": "73c31a207a63d9511b2fafa76ef8846cc7d0cb0416778d91a10dc867217d2998",
  "repository_revision": "172ef314579ccf9457c90806b7c173a37a5406f9",
  "design_required": false,
  "impact_map": {
    "applications": [
      "ScanPlantAPI",
      "ScanPlant-Final"
    ],
    "modules": [
      "external-fallback",
      "mobile-client"
    ],
    "contracts": [
      "fallback HTTP DTO",
      "mobile consent"
    ],
    "data": [],
    "platforms": [
      "ASP.NET Core .NET 8",
      "Expo/React Native"
    ]
  },
  "decisions": [
    {
      "id": "D-001",
      "statement": "P01 permanece blocked-terminal, não aprovado e não concluído; não haverá nova campanha Stryker.",
      "evidence": "artifacts/bianchini/v1/evidence/P01-R1-final-foreground-inconclusive.json",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md"
      ]
    },
    {
      "id": "D-002",
      "statement": "P02 depende de pré-condições técnicas verificáveis, não do status completed de P01.",
      "evidence": "artifacts/bianchini/v1/ledgers/P01.md",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ]
    }
  ],
  "assumptions": [
    {
      "id": "A-001",
      "impact": "high",
      "status": "confirmed",
      "statement": "Endpoint, DTO, consentimento, JWT e falhas neutras de P01 estão presentes e cobertos pelos gates funcionais registrados.",
      "evidence": "artifacts/bianchini/v1/ledgers/P01.md",
      "fallback": "bloquear P02 se qualquer pré-condição falhar",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ]
    }
  ],
  "pitfalls": [
    {
      "id": "P-001",
      "impact": "critical",
      "statement": "Desacoplar P02 não pode inferir aprovação de P01 nem enfraquecer segurança/privacidade.",
      "prevention": "pré-condições técnicas e gates móveis explícitos",
      "recovery": "bloquear P02 se uma pré-condição falhar",
      "verification": "planning audit e gates P02",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ]
    },
    {
      "id": "P-002",
      "impact": "high",
      "statement": "A observabilidade Stryker continua pendência separada sem waiver inventado.",
      "prevention": "follow-up documental sem bloquear P02 tecnicamente",
      "recovery": "novo pacote específico se capacidade futura existir",
      "verification": "ledger P01",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md"
      ]
    }
  ],
  "user_actions": [
    {
      "id": "U-001",
      "needed_by": "P02",
      "statement": "Aprovar o digest do pacote v2 e os planos P01/P02; nenhuma campanha Stryker será autorizada.",
      "fallback": "manter P01 bloqueado e não iniciar P02",
      "destinations": [
        "docs/bianchini/changes/v2/USER_ACTIONS.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "can_continue_without": false,
      "evidence_required": "approval of v2 package before P02 execution"
    }
  ],
  "spikes": [
    {
      "id": "S-001",
      "status": "passed",
      "statement": "Reavaliação confirmou que a dependência ampla de P02 é de qualidade, não técnica.",
      "evidence": "ledger P01 e contratos v1",
      "destinations": [
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ],
      "decision": "Desacoplar P02 por pré-condições técnicas e manter P01 bloqueado separadamente."
    }
  ],
  "design_surfaces": [],
  "spec_deltas": [
    {
      "id": "SD-001",
      "statement": "Pré-condições técnicas independentes de P02 e P01 bloqueado separado.",
      "source": "docs/bianchini/changes/v2/spec-deltas/replan-v2.md",
      "target": "docs/bianchini/current/specs/replan-v2.md",
      "destinations": [
        "docs/bianchini/changes/v2/spec-deltas/replan-v2.md",
        "docs/bianchini/changes/v2/specs/replan-v2.md",
        "docs/bianchini/changes/v2/plans/P01-observability-followup.md",
        "docs/bianchini/changes/v2/plans/P02-mobile-consented-client.md"
      ]
    }
  ]
}
```
