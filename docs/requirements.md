# Resolve Basquete - Requerimentos de software

## Requisitos funcionais:
1. Determinar o vencedor de um capeonatdo de basquete dados as regras:
    > Um time ganha 3 pontos de vence o jogo ou ganha 1 ponto se perde o jogo. **Não há empate**
    
    > Se o score figar igual ao final do campeonato:
    >* Fica na frente o time com a melhor "cesta average". Para calcular a "cesta average":
    >* Razão entre o número de pontos marcados pelo time dividido pelo número de pontos recebidos. (Se não houver nenhum recebido usa-se o número de pontos marcados como "cesta average")

    >Persistindo o empate, é escolhido o time com menor número de inscrição no campeonato.

# Requisitos não funcionais:
1. Executar em menos de um segundo.