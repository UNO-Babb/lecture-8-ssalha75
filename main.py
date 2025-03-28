def main():
  pitching = open("MLB_Pitching.csv", 'r')
  team_data = []

  #get the import info out of pitching and store into team_data

  pitching.close()

  hitting = open("MLB_Hitting.csv", 'r')

  #process all the data in hitting and add to the correct portion of the team_data

  hitting.close()


  outFile = open("mlb_output.csv", 'w')

  #process each line of the team_data and save to the output file.
  output = ""
  outFile.write(output)

  outFile.close()

if __name__ == '__main__':
  main()
