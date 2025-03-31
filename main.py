def main():
  team_data = []

  hitting = open("MLB_Hitting.csv", 'r')
  #process all the data in hitting and add to the correct portion of the team_data
  for team in hitting:
    teamInfo = team.split(",")
    print(teamInfo[0], teamInfo[3])
    team_data.append([teamInfo[0], teamInfo[3] ])

  hitting.close()

  pitching = open("MLB_Pitching.csv", 'r')
   #get the import info out of pitching and store into team_data
  teamNum = 0
  for team in pitching:
    teamInfo = team.split(",")
    name = teamInfo[0]
    runAllowed = teamInfo[3]
    wins = teamInfo[3]
    losses = teamInfo[5]
    era = teamInfo[7]
    team_data[teamNum] = team_data[teamNum] + [runAllowed, wins, losses, era]
    teamNum = teamNum + 1

  pitching.close()

  outFile = open("mlb_output.csv", 'w')

  #process each line of the team_data and save to the output file.
  output = ""
  for team in team_data:
    teamString = str(team)
    teamString = teamString.replace("[", "")
    teamString = teamString.replace("]", "")
    output = output + teamString + "\n"

  outFile.write(output)

  outFile.close()

if __name__ == '__main__':
  main()
