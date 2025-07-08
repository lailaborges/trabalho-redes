# Trabalho de Redes - Guido e Laila
Os progs foram upados na master

# Trabalho de Redes - Matriz, Inversão e Determinante com Docker

Este projeto simula a troca de dados entre 3 programas (cliente, servidor e servidor de resultado) usando sockets TCP. Os programas estão isolados em containers Docker e se comunicam entre si.

## Estrutura

- `prog1` → Gera matrizes e envia ao servidor (`prog2`)
- `prog2` → Inverte a matriz, calcula o determinante e envia o resultado ao servidor final (`prog3`)
- `prog3` → Exibe o resultado e o tempo de execução

## Pré-requisitos

- Docker instalado ([guia oficial](https://docs.docker.com/get-docker/))
- Docker Compose instalado ([guia oficial](https://docs.docker.com/compose/install/))

## Como rodar o projeto

1. **Clone este repositório:**

   ```bash
   git clone https://github.com/lailaborges/trabalho-redes.git
   cd trabalho-redes
2. Execute o Docker Compose com a flag --build:

```bash
    docker compose up --build
```
Os logs dos 3 programas serão exibidos no terminal. O prog3 mostrará as matrizes invertidas, os determinantes e o tempo total de execução.

Observações
Os containers usam nomes fixos (prog1, prog2, prog3) para garantir que os programas se encontrem via hostname no Docker.

As matrizes são geradas aleatoriamente dentro do prog1.

Toda comunicação ocorre via sockets TCP com troca de mensagens serializadas (JSON ou pickle).


