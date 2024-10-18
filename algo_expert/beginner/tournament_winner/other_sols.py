def tournamentWinner(competitions, results):
    teamPoint = {}
    currentWinner = "",0
    for competition, result in zip(competitions, results):
        winner = competition[not result]
        loser = competition[result]
        if winner not in teamPoint:
            teamPoint[winner] = 0
        teamPoint[winner] += 3

        if teamPoint[winner] > currentWinner[1]:
            currentWinner = winner, teamPoint[winner]
    
    return currentWinner[0]

def tournamentWinner(competitions, results):
    t = dict()
    for c, r in zip(competitions, results):
        t[c[1-r]] = t.get(c[1-r], 0) + 1
    return max(t, key=t.get)

def tournamentWinner(competitions, results):
    teams = dict()
    for i, comp in enumerate(competitions):
        if results[i]:
            teams[comp[0]] = teams.get(comp[0], 0) + 1
        else:
            teams[comp[1]] = teams.get(comp[1], 0) + 1
    return max(teams, key=teams.get)