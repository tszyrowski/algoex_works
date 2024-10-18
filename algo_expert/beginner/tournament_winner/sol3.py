"""Don't iterate twice, get the winner inside single operation"""
def tournamentWinner(competitions, results):
    all_teams = {}
    max_val = 0
    winner = None
    for names in competitions:
        for name in names:
            all_teams[name] = 0

    for i, teams in enumerate(competitions):
        if results[i]:
            all_teams[teams[0]] += 1
            if all_teams[teams[0]] > max_val:
                winner = teams[0]
                max_val = all_teams[teams[0]]
        else:
            all_teams[teams[1]] += 1
            if all_teams[teams[1]] > max_val:
                winner = teams[1]
                max_val = all_teams[teams[1]]

    return winner

if __name__ == "__main__":
    competitions = [
        ["A", "B"],
        ["B", "C"],
        ["C", "A"]
    ]
    results = [0, 0, 1]
    w = tournamentWinner(competitions, results)
    print(w)

