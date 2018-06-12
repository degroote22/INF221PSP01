# Proposta de Padronização de Codificação em Python

## Propósito:
- Guiar o desenvolvimento de programas em Python.

## Cabeçalho do programa:
- Todos os programas começam com um cabeçalho descritivo.

### Formato do cabeçalho:
```python
###########################################################
#  Author: Seu Nome                                       #
#  Created at: Data de criação (no formato 2018-11-01)    #
#  License: Licença comercial (por exemplo MIT)           #
###########################################################
```

## Imports:
- Todos os imports devem estar agrupados no começo do arquivo.

## Identificadores:
- Devem seguir o camelCase e tentar ser explícito ao invés de curto.
### Exemplos:
```python
numberOfPlayers = 1 # Bom uso
x = 1 # Mau uso
```

## Comentários:
- Procuram explicar a motivação por trás do programa e não o que o código faz.
- Se o código precisa de comentários para ser entendido (como no caso de uso de partes obscuras da linguagem) ele deve ser removido e substituído por uma implementação mais simples.

### Um bom exemplo de comentário:
```python
# Guarda-se o número de jogadores para usar no final da função
numberOfPlayers = totalPlayers
```

### Um mau exemplo de comentário:
```python
# Guarda o valor de totalPlayers em numberOfPlayers
numberOfPlayers = totalPlayers
```

## Espaços em branco:
- Devem ser usados ao máximo possível para facilitar e legibilidade.
- Todo bloco deve estar cercado de linhas em branco.