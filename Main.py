# Create an Intramural score tracker
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


# Each team entry is a list that includes
#   - Name
#   - Games Played
#   - Wins
#   - Losses
#   - Ties
#   - Goals For
#   - Goals Against

# You will ask how many teams are playing.
# Loop that many times, create a team and set all scores to 0, then append it to your list of teams
# Start an infinite loop for main menu
#   1) Add score
#   2) See Team stats
#   3) See Overall Standings
#   4) Quit

#   1) Enter team 1, team 2, goals for team 1, goals for team 2
#       - Find the teams, update the games played, add the goals for and against, and decide if it's a win, lose or tie

#   2) Print a list of team names.
#       Once the user selects, Print out their stats

#   3) Print out the teams in order from most team points to least
#   - Team points = wins*2 + ties*1
#   - If they have the same points, look for most goals for
#   - If they have the same goals for, take the least goals against.
#   - If those are the same, then just output the teams.

#   4) Say goodbye and break out of the loop