def main():
  myFile = open("qbdata.txt", 'r')

  for line in myFile:
    info = line.split(",")
    #print(info)
    if info[1] == '"NE"' and info[0] == '"omaha"':
      year = int(info[8][1:5])
      if year > 2010:
        print(info[5])

  myFile.close()


if __name__ == '__main__':
  main()
