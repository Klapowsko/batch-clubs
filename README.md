# batch-clubs

## 1. Descrição breve

O batch-clubs é um programa em Python que lê um arquivo JSONL de clubes de futebol, onde cada linha contém os dados de um clube e sua lista de jogadores. A partir dessa entrada, o programa gera dois arquivos CSV: clubs.csv (um registro por clube) e players.csv (um registro por jogador).

O processamento aplica regras de negócio e normalização de dados durante a leitura, descartando registros inválidos sem interromper a execução completa. O resultado final é salvo em arquivos de saída separados para facilitar consumo e análise posterior.

## 2. Requisitos

Você pode executar o projeto de duas formas:

- Docker (para rodar via Makefile)
- Ou Python 3.12+ e pip (para rodar diretamente)

## 3. Configuração

Rode o comando abaixo:

	make install

Esse comando já cria o arquivo .env a partir do .env.example automaticamente, apenas se o .env ainda não existir (sem sobrescrever customizações existentes).

A variável INPUT_FILE no .env define o caminho padrão do arquivo JSONL de entrada.

Importante: esse caminho precisa apontar para um arquivo dentro da pasta do projeto, porque no fluxo com Docker o volume montado é apenas a pasta atual do repositório.

## 4. Como executar

### Via Docker/Makefile

Usando o INPUT_FILE do .env:

	make run

Override pontual do arquivo de entrada:

	make run INPUT_FILE=caminho/outro_arquivo.jsonl

A saída vai para o diretório output/.

### Direto com Python

	python -m batch_clubs caminho/para/arquivo.jsonl [diretorio_saida]

O caminho do arquivo de entrada é um parâmetro obrigatório de linha de comando.

Esta é a forma de execução exigida pelo desafio; Docker/Makefile é conveniência adicional para padronizar o ambiente.

## 5. Como rodar os testes

Todos os testes:

	make test

Um arquivo específico:

	make test-file TEST_FILE=tests/arquivo.py

Alternativa direta com pytest:

	pytest -q

ou:

	pytest -q tests/arquivo.py

## 6. Regras de negócio aplicadas

- Filtro por campeonato: somente Série A e Série B.
- Formatação de datas: yyyy-MM-dd; quando inválida, o campo fica vazio.
- Campo Cores: lista unida em uma única string com separador |.
- Campos ausentes ou nulos: convertidos para vazio quando aplicável.

## 7. Decisões de design

- Arquitetura hexagonal: separa regras de domínio de detalhes de I/O, facilitando testes, manutenção e evolução.
- Robustez: registros malformados são descartados sem interromper o processamento do restante do arquivo.
- Escalabilidade para arquivos grandes: leitura e escrita em streaming, sem carregar todo o conteúdo em memória.

## 8. Estrutura do projeto

- domain/: regras de negócio e modelos de domínio.
- ports/: contratos de entrada e saída (interfaces).
- adapters/: implementações concretas dos ports (JSONL e CSV).
- entrypoints/: orquestração da execução da aplicação.
- tests/: testes automatizados.
