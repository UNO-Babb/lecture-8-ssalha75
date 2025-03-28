def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile:
    print (line)

  myFile.close()


if __name__ == '__main__':
  main()
