# Casos de uso:
## Não houve pontuação igual ao fim do campeonato:
- O time de maior pontuação terá posicionamento maior

## Houve pontuação igual do fim do campeonato:
- Calcula-se o "cesta average" (anexo 1) para dos dois times
- O de maior valor terá posicionamento maior
- Se persistir o empate, o de menor incrição no campeonato terá posicionamento maior

# Anexo 1 - Cálculo da "cesta average"
1. Soma-se todos as cestas marcadas do time
1. Soma-se todas as cestas recebidas
1. Se houve alguma cesta recebida o valor é a divisão entre as duas somas
1. Se não houve cesta recebida o valor é o número de cestas marcadas

# Estrutura do programa:
1. Ler a primeira linha da entrada e salvar em n
1. Calcular o número de jogos `y = (n * (n-1))/2`
1. Ler as `y` linhas seguintes da entrada e colocar o resultado do jogo no mapa de resultados
1. Calcular o número de pontos de cada time
1. Ordenar por número de pontos, implementando os edge-cases
1. Imprimir o resultado