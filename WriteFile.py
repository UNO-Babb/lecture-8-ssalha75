import random

def main():

  outFile = open("dice_rolls.txt", 'w')

  die1 = random.randint(1,6)
  die2 = random.randint(1,6)
  total = die1 + die2

  output = str(die1) + " " + str(die2) + " " + str(total)
  outFile.write(output)

  outFile.close()

if __name__ == '__main__':
  main()
