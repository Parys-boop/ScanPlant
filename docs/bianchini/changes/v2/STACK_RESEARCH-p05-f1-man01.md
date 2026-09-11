# Stack Research — P05 / F1-MAN01

Research mode: repo_only
Motivo: definir contrato documental e ferramentas locais já disponíveis, sem integrar biblioteca/API nem escolher agora taxonomia inédita. Consulta taxonômica oficial é entrada da execução prevista em U-201, não pesquisa de stack pendente.

## Stack detectada

Backend net8.0, testes net8.0/net10.0; mobile Expo 51, React Native 0.74.5; web Vite 5/TypeScript 5. Essas aplicações não serão alteradas. Python 3.12.3 e rg 15.2.0 presentes; Git 2.43.0. Não há manifesto botânico canônico nem validador documental existente a reaproveitar.

## Inventário local

- Manifests: `ScanPlantAPI/ScanPlantAPI/ScanPlantAPI.csproj`, `ScanPlantAPI/ScanPlantAPI.Tests/ScanPlantAPI.Tests.csproj`, `ScanPlant-Final/package.json`, `scanplant-web/package.json`, `ScanPlant-Final/eas.json`, `.config/dotnet-tools.json`.
- Lockfiles: `ScanPlant-Final/package-lock.json` e `scanplant-web/package-lock.json`, formato 3; node_modules ausentes, cache npm presente e NuGet parcial. Nenhum desses caches é necessário a P05.
- CI: `.github/workflows/deploy.yml`, Node 18 e build/deploy web no push master; não cobre o manifesto e não será alterada ou acionada.
- Testes: scripts `test:mobile-consent`, `validate:pt05` e xUnit são de produto, fora desta entrega. O contrato novo especifica CLI Python e unittest documental a criar na mesma unidade futura; nenhum desses arquivos ou comandos novos foi executado agora.
- Padrões locais: JSON em `docs/living/PROJECT_STATE.md`, hashes SHA-256, planos coesos sob changes/v2 e ledger append-only. P04 é somente precedente de evidência, sem reavaliação do benchmark.

Leitura localizada suficiente: a mudança define um artefato sem consumidores ativos, não atravessa fluxos das três aplicações. Conforme a exceção de leitura localizada da cartografia, não criar mapa artificial nem ler produto, imagens ou logs de mutação.

## Decisões aplicadas

D-201: P05 é o próximo número após P04 no ciclo v2 ainda aberto; não arquivar, criar v3 ou renumerar históricos. F1-MAN01 é identificador funcional proposto para o item sem código do roadmap §6; a busca de identificadores não encontrou colisão.

D-202: JSON versionado, schema fechado documentado, Python stdlib com testes negativos e revisão humana. Um validador de formato não pode provar verdade taxonômica nem aprovação das espécies; U-201 e evidência por nome permanecem obrigatórias.

D-203 e A-202: apenas Python 3.12 stdlib e Git são requisitos locais. Ubuntu 24.04/WSL2, repositório em ext4. .NET 8, Java, ADB, Android SDK, jq e pwsh ausentes; Docker daemon e PostgreSQL indisponíveis. Node 24.19.0 difere de Node 22.20.0 EAS. Nada disso bloqueia P05; nenhuma instalação ou restauração é parte do plano.

Consulta futura, exclusivamente páginas textuais públicas de autoridades taxonômicas oficiais, começando pelo POWO/Kew já usado no projeto. Não repetir referências já documentadas se a evidência datada e específica for suficiente; quando reutilizadas, conservar a data histórica real. Complementar somente os nomes/aliases sem evidência. Não usar páginas de preço/provider nem imagens/datasets. Nenhuma consulta web foi realizada neste planejamento.

## Riscos e lacunas

A-201: roadmap afirma 12 espécies, mas apenas cinco estão nominalmente documentadas em F1-G01 e na spec P04. São Epipremnum aureum, Monstera deliciosa, Zamioculcas zamiifolia, Spathiphyllum wallisii e Dracaena trifasciata. Sansevieria trifasciata é sinônimo documentado da última, não classe adicional. Isso não autoriza inferir as outras sete nem promover Bellis perennis a espécie suportada. A fonte de escopo é uma fronteira humana única U-201; fonte taxonômica externa não resolve decisão de produto.

Suposição limitada: a entrada humana deverá identificar 12 táxons distintos do escopo existente. Se contiver gênero genérico, cultivar ambíguo, duplicata taxonômica ou substituição, devolver à mesma U-201, sem preencher ou reduzir o escopo. O contrato parametrizado permite planejar integralmente; a disponibilidade da entrada não é declarada resolvida.

## Política consultada

Comando executado: `python3 -B /home/aluno/.agents/skills/_shared/scripts/bm.py policy --profile standard --risk low --change parser --manual-pdf scope --round 0 --risk-seam offline-manifest-contract --seam-round 0`.

Resultado: grouped/plan_gate, cadência group_seam, máximo 3 fix rounds no seam, rodada efetiva 0, breaker false, mutation not_required, manual_required false, arquitetura manual/report-only não requerida. Classificação factual parser: haverá lógica no validador; não mascará-la como documentation. Risco operacional low nesta entrega reversível, local, sem consumo no produto, decisões de saúde, inferência ou efeitos externos. O risco de qualidade taxonômica é tratado por evidência e gate humano; qualquer integração futura exige avaliação própria. Perfil standard preservado pelos contratos históricos de maior risco; nenhum contador/breaker P01/P03 é reiniciado.
