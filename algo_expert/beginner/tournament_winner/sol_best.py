"""Don't iterate twice, get the winner inside single operation"""
def tournamentWinner(competitions, results):
    all_teams = {}
    max_val = 0
    winner = None

    for i, teams in enumerate(competitions):
        home_team, away_team = teams

        comp_winner = home_team if results[i] else away_team

        all_teams[comp_winner] = all_teams.get(comp_winner, 0) + 3

        # track max val in one go
        if all_teams[comp_winner] > max_val:
            winner = comp_winner
            max_val = all_teams[comp_winner]

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

