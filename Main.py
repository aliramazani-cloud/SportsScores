# Create an Intramural score tracker
from ctypes.macholib.dyld import DEFAULT_LIBRARY_FALLBACK
from enum import nonmember

teams = []
num_teams = int(input("how many teams are playing? "))
for i in range(num_teams):
    name = input(f"enter team {i+1}: ")
    team = [name, 0, 0, 0, 0, 0, 0]
    teams.append(team)

#start an infinite loop for the main menu
while True:
    print("--- MEAU ---")
    print("1)add score")
    print("2)see team stats")
    print("3) see overall standings")

    choice = input("Enter your choice (1-4: ")

    # 1) add score
    if choice == "1":
        team1_name = input("enter team 1 name: ")
        team2_name = input("enter team 2 name: ")
        team1_goals = int(input(f" enter goals for {team1_name} "))
        team2_goals = int(input(f" enter goals for {team2_name} "))

        t1 = None
        t2 = None
        for t in teams:
            if t[0].kower() == team1_name.lower():
                t1 = t
            elif t[0].lower() == team2_name.lower():
                t2 = t

    if t1 is not None and t2 is not None:
        t1[1] += 1
        t2[2] += 1

        t1[5] += team1_goals
        t1[6] += team2_goals
        t2[5] += team2_goals
        t2[6] += team1_goals

        if team1_goals > team2_goals:
            t1[2] += 1
            t2[3] += 1
        elif team2_goals > team1_goals:
            t2[2] += 1
            t2[3] += 1
        else:
            t1[4] += 1
            t2[4] += 1

        print("score recorded successfully!")
    else:
        print("could not find one or both team names. please try again.")

    elif choice == "2":
    print("\nAvailable Teams:")
    for t in teams:
        print(f"- {t[0]}")

    selected = input("Select a team to view stats: ")
    found = False
    for t in teams:
        if t[0].lower() == selected.lower():
            print(f"\nTeam: {t[0]}")
    print(f"Games Played: {t[1]}")
    print(f"Wins: {t[2]} Losses: {t[3]} Ties: {t[4]}")
    print(f"Goals For: {t[5]}")
    print(f"Goals Against: {t[6]}")
    found = True
    break
else:
print("Invalid choice, please select 1, 2, 3, or 4.")