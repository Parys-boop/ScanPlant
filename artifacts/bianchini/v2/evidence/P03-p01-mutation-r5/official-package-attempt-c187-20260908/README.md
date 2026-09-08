# P03-R5 — aquisição oficial dotnet-stryker 4.16.0 bloqueada

Tipo: checkpoint de continuidade não canônico.

Revisão funcional:

c187eec242a8f37b8f5807558b03bb7dc1c8a171

Branch funcional:

bm/v2-p03

## Resultado

Uma única aquisição controlada foi autorizada para dotnet-stryker 4.16.0.

O pacote oficial:

dotnet-stryker.4.16.0.nupkg

foi obtido via HTTPS de api.nuget.org com HTTP 200 e TLS validado.

Tamanho observado:

46147078 bytes

O endpoint exato autorizado para:

dotnet-stryker.4.16.0.nupkg.sha512

retornou HTTP 404.

Consequentemente:

- nenhuma fonte alternativa foi utilizada;
- o SHA-512 oficial não pôde ser comparado;
- dotnet nuget verify não foi executado;
- o preflight integral não foi iniciado;
- restore offline não foi executado;
- build não foi executado;
- MutationHarness não foi executado;
- Stryker não foi executado;
- campaign_count permaneceu 0;
- nenhuma campanha mutacional foi executada;
- U-008 não foi consumida;
- o cache global NuGet não foi alterado;
- nenhuma rede de aplicação/provider real foi utilizada.

## Launcher

SHA-256 observado do launcher original:

b8d3df713ff4deef8bbaa756e0bb7d2ab0fe6440717c4da8393351a7ce6918d3

O launcher original continha caminhos absolutos locais e, por isso, não foi
versionado diretamente. Uma versão sanitizada é preservada neste checkpoint.

## Pacote

O .nupkg não foi versionado porque sua cadeia oficial de autenticação não foi
concluída.

Os arquivos:

- source-sha256.txt
- source-sha512.txt
- source-inventory.txt
- package-sha512-base64.txt

preservam sua identidade criptográfica e inventário observado.

## Próxima ação

É necessária nova autorização definindo uma fonte oficial válida para o
checksum ou outro mecanismo oficial de obtenção/verificação do hash.

Este checkpoint não aprova o pacote, o preflight, U-008 ou qualquer campanha.

Checkpoint UTC: 2026-09-08T14:12:55Z
