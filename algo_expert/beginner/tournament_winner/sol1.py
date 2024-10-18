"""correct results after 22 minutes"""
def tournamentWinner(competitions, results):
    all_teams = {}
    for names in competitions:
        for name in names:
            all_teams[name] = 0

    for i, teams in enumerate(competitions):
        if results[i]:
            all_teams[teams[0]] += 1
        else:
            all_teams[teams[1]] += 1
    max_val = 0
    for k, v in all_teams.items():
        if v > max_val:
            winner = k
            max_val = v
    return winner

if __name__ == "__main__":

    competitions = [
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"],
        ["SQL", "C#"],
        ["HTML", "SQL"],
        ["SQL", "Python"],
        ["SQL", "Java"],
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"],
        ["SQL", "C#"],
        ["HTML", "SQL"],
        ["SQL", "Python"],
        ["SQL", "Java"],
        ["HTML", "Java"],
        ["Java", "Python"],
        ["Python", "HTML"],
        ["C#", "Python"],
        ["Java", "C#"],
        ["C#", "HTML"],
        ["SQL", "C#"],
        ["HTML", "SQL"],
        ["SQL", "Python"],
        ["SQL", "Java"]
    ]
    results = [0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0, 0, 1, 1, 1, 0, 1, 0, 1, 1, 0]

    w = tournamentWinner(competitions, results)
    print(w)

