{
  "verdict": "passed",
  "findings": [
    {
      "id": "NOTE-001",
      "severity": "note",
      "summary": "O pacote preserva integralmente os limites aprovados e separa o merge autorizado da implementação.",
      "evidence": "U-001 bloqueia P01 até merge autorizado; P01/P02 não incluem Nominatim, scanplant-web, PT-05, migration, dataset ou chamadas reais por padrão."
    },
    {
      "id": "NOTE-002",
      "severity": "note",
      "summary": "Os seams de maior risco têm contrato público, fakes e garantia seletiva definidos antes da execução.",
      "evidence": "P01 declara strict/per_task, handlers falsos, integração autenticada e mutação seletiva; P02 depende de P01 e limita-se ao cliente mobile."
    },
    {
      "id": "NOTE-003",
      "severity": "note",
      "summary": "A passagem 2 confirma somente a remoção de quatro espaços finais nos dois planos congelados.",
      "evidence": "A comparação com as cópias pré-correção mostra diferença exclusiva no whitespace ao fim das linhas 3 e 4 de P01 e P02; escopo, contratos, tarefas, comandos e decisões permanecem idênticos."
    }
  ]
}
