# Parecer de Qualidade — P01-R1-T01

## Veredito

**APROVADO.** O diff entrega as asserções observáveis de fronteira exigidas nesta tarefa; a prova de campanha de mutação pertence à Tarefa 3 e não é um gate adicional para T01.

## Escopo revisado

O pacote contém um único arquivo de harness, com 120 adições e 3 remoções (`artifacts/bianchini/v1/reviews/P01-R1-T01.md:17-20`). Não há mudança de produção, persistência ou chamada de rede no diff. Isso está alinhado ao contrato de adicionar apenas testes puros (`.superpowers/bianchini/v1/p01/P01-R1-T01-brief.md:24-26`).

## Spec

- As adições cobrem o aceite no limite de bytes, dimensões máximas, leitura fragmentada limitada e rejeição do primeiro byte excedente: `ValidateAsync_WhenPayloadIsExactlyMaxImageBytes_AcceptsIt` (`P01-R1-T01.md:40-52`), `ValidateAsync_WhenDimensionsAreExactlyAtLimit_AcceptsIt` (`P01-R1-T01.md:54-66`), `ValidateAsync_WhenPayloadIsFragmentedExactlyAtLimit_PreservesBytesAndUsesBoundedReads` (`P01-R1-T01.md:68-82`) e `ValidateAsync_WhenActualPayloadHasFirstByteOverLimitDespiteDeclaredLength_RejectsIt` (`P01-R1-T01.md:84-95`). O stream falso fragmenta leituras, mede o maior buffer pedido e falha quando o teto configurado é excedido (`P01-R1-T01.md:197-229`).
- O contexto do diff mantém a asserção de ausência de consentimento sem chamada ao provider (`P01-R1-T01.md:97-106`) e de Groq desabilitado sem chamada de conhecimento (`P01-R1-T01.md:107-116`), coerente com os invariantes de segurança. A unidade não introduz efeito irreversível: os cenários usam fakes; portanto não há nova evidência ambígua de envio externo, estado durável ou retomada a avaliar.

## Qualidade

Os novos testes usam entradas observáveis e verificam tanto o resultado quanto os bytes/limite de leitura, sem alterar produção. Em particular, o payload acima do limite é apresentado com comprimento declarado no limite e deve produzir `PayloadTooLarge`/resultado inválido (`P01-R1-T01.md:84-95`), cobrindo a contabilidade derivada da leitura real; o stream fragmentado rejeita pedido de buffer acima do teto e registra a maior solicitação (`P01-R1-T01.md:197-229`). A execução de 14 testes aprovada é relatada (`.superpowers/bianchini/v1/p01/P01-R1-T01-report.md:11-14`).

## Findings

### Important

Nenhum.

### Critical

Nenhum.

### Minor

Nenhum.

### Note

Nenhuma.

## Contagem

- Critical: 0
- Important: 0
- Minor: 0
- Note: 0
