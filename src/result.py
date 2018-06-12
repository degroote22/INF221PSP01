###########################################################
#  Author: Lucas de Avila Martins                         #
#  Created at: 2018-07-10                                 #
#  License: MIT                                           #
###########################################################

def reduceScore(acc, item):
    if(item['my'] > item['theirs']):
        return acc + 2
    return acc + 1

def getScore(team):
    results = team['data']

    return reduce(reduceScore, results, 0)

def getAverage(team):
    results = team['data']

    scored = reduce(lambda x, y: x+y['my'], results, 0)
    received = reduce(lambda x, y: x+y['theirs'], results, 0)

    if(received != 0):
        return float(scored) / float(received)
    return float(scored)

def result(filename):
    file = open(filename, "r")

    numberOfTeams = int(file.readline())

    numberOfGames = (numberOfTeams * (numberOfTeams -1))/2

    teamsData = {}

    # Incializa um array pra cada time guardar os resultados do seu jogo.
    # Usando index+1 porque os times virao numerados em base 1.
    for index in range(numberOfTeams):
        teamsData[index+1] = []

    for _ in range(numberOfGames):
        [teamA, scoreA, teamB, scoreB] = map(int, file.readline().split(" "))
        gameA = {'my': scoreA, 'theirs': scoreB}
        gameB = {'my': scoreB, 'theirs': scoreA}
        teamsData[teamA].append(gameA)
        teamsData[teamB].append(gameB)

    teamsDataList = map(
        lambda index: {'data': teamsData[index], 'index': index},
        list(teamsData)
        )

    teamsDataListWithScoreAndAverage = map(
        lambda team: {
            'average': getAverage(team),
            'score': getScore(team),
            'index': team['index']
            },
        teamsDataList
    )

    teamsSortedByAvg = sorted(
        teamsDataListWithScoreAndAverage,
        key= lambda team: team['average']
    )

    teamSortedByScore = sorted(
        teamsSortedByAvg,
        key= lambda team: team['score']
    )

    indexesOrdered = map(lambda team: team['index'], teamSortedByScore)
    return " ".join(list(reversed(map(str, indexesOrdered))))
