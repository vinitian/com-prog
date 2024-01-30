# HW2 Football-League-Table (*** DO NOT DELETE this line or add line before this ***)
# Only add your code in the provided area.
# DO NOT delete or modified the given code in main()

def toString(table):
    # create a string that represents the table for printing
    # for example if the table is: [["Arsenal",0,0,0,0,0],["Chelsea",0,0,0,0,0],["Liverpool",0,0,0,0,0]]
    # this method will return a string that can be printed as a table

    #Team        |Pld|Pts|Dif|For|Agst|
    #Arsenal     |  0|  0|  0|  0|   0|
    #Chelsea     |  0|  0|  0|  0|   0|
    #Liverpool   |  0|  0|  0|  0|   0|

    # team name can have up to 12 characters
    # Pld, Pts, Dif, For can have up to 3 characters
    # Agst can have up to 4 characters

    # enter your code here
    s = "Team        |Pld|Pts|Dif|For|Agst|\n"
    for i in range(len(table)):
      s += table[i][0]+" "*(12-len(table[i][0])) + "|"
      for j in range(1,5):
        s += " "*(3-len(str(table[i][j]))) + str(table[i][j]) + "|"
      s += " "*(4-len(str(table[i][5]))) + str(table[i][5]) + "|\n"
    return s






def createTable(s):
    # create table from team names, for example: "Arsenal Liverpool Chelsea"
    # return the created table, for example: [["Arsenal",0,0,0,0,0],["Chelsea",0,0,0,0,0],["Liverpool",0,0,0,0,0]]
    # the created table must be sorted according to function "sortTable"

    # enter your code here
    s = s.split()
    x = []
    for i in range(len(s)):
      x.append([s[i],0,0,0,0,0])
    x = sortTable(x)
    return x




def sortTable(table):
    # sort table by the following fields in order:
    # Pts (descending)
    # Dif (descending)
    # For (descending)
    # Agst (ascending)
    # teamname (ascending)
    # Pld (ascending)

    # return the sorted table
    # enter your code here
    forSort = []
    for i in range(len(table)):
        forSort.append([-1*table[i][2], -1*table[i][3], -1*table[i][4], table[i][5], table[i][0], table[i][1]])

    newTable = []
    forSort = sorted(forSort)
    for i in range(len(forSort)):
        for j in range(len(table)):
            if forSort[i][4] == table[j][0]:
                newTable.append(table[j])
                break

    return newTable







def saveTable(table):
    # save the table to file "table.txt" (as a ready-to-print string)
    # also print the table out
    # enter your code here
    table = toString(table)
    textFile = open("table.txt", "w")
    textFile.write(table)
    textFile.close()
    print(table)






def match(table, team1, team2, score1, score2):
    # input is the table, team1 name, team2 name, goals that team1 scores, goals that team2 scores
    # if team1 and team2 are the same, just report and return table
    # if either team is not in the table, report accordingly and return table
    # otherwise, update the table and return the updated table that is already sorted

    # enter your code here
    names = []
    for i in range(len(table)):
        names.append(table[i][0])
    if team1 == team2:
      print("Error: a team plays the same team!")
      return table
    elif (team1 not in names) and (team2 not in names):
      print("Error: Both team do not exist in the table!")
      return table
    elif (team1 in names) and (team2 not in names):
      print("Error: Second team does not exist in the table!")
      return table
    elif (team1 not in names) and (team2 in names):
      print("Error: First team does not exist in the table!")
      return table

    else:
      if score1 > score2:
          win = team1
      elif score1 == score2:
          win = 'draw'
      else:
          win = team2

    for name in [team1, team2]:
      for i in range(len(table)):
          if name == table[i][0]:
              #Pts
              if win == name:
                  table[i][2] += 3
              elif win == 'draw':
                  table[i][2] += 1

              #Pld
              table[i][1] += 1

              #Dif
              if name == team1:
                  table[i][3] = score1-score2
              else:
                  table[i][3] = score2-score1

              #For & Agst
              if name == team1:
                  table[i][4] += score1
                  table[i][5] += score2
              elif name == team2:
                  table[i][4] += score2
                  table[i][5] += score1

    table = sortTable(table)
    return(table)






def changePoint(table, team, point):
    # change the Pts of the given team by "point" amount (can be positive and negative integer)
    # return the updated table after point change (the table must be sorted again)

    #enter your code here

    for i in range(len(table)):
      if team == table[i][0]:
        table[i][2] += point
        break

    table = sortTable(table)
    return(table)







def removeTeams(table, toRemove):
    # remove some team from the table ,
    # toRemove is a list of team names to remove, for example: ["Southampton", "Arsenal", "Liverpool"]
    # return the updated table (must already be sorted again)

    # enter your code here
    names = []
    for i in range(len(table)):
        names.append(table[i][0])

    for j in toRemove:
      for i in range(len(table)):
        if j == table[i][0]:
          table.pop(i)
          break

    table = sortTable(table)
    return(table)







def addTeams(table, toAdd):
    # add some team to the table,
    # toAdd is a list of team names to add, for example: ["Southampton", "Arsenal", "Liverpool"]
    # set all numbers associated with the newly added teams to 0
    # return the updated table (must already be sorted again)
    # Assume that the name of team will never duplicate with existing ones in the table!

    # enter your code here
    for i in toAdd:
      table.append([i,0,0,0,0,0])

    table = sortTable(table)
    return(table)





def resetTable(table):
    # reset all number information in the table to 0
    # return the updated table (already sorted again)
    # enter your code here
    for i in range(len(table)):
      table[i][1], table[i][2], table[i][3], table[i][4], table[i][5] = 0,0,0,0,0

    table = sortTable(table)
    return table





def loadFile(filename):
    # make a table from a given text file
    # the text file form is similar to the following example (actual file is also given)
    # Be careful, there are white spaces to make the table readable:

    # Team        |Pld|Pts|Dif|For|Agst|
    # Blackburn   |  2|  3|  1|  3|   2|
    # Southampton |  1|  3|  1|  2|   1|
    # Chelsea     |  2|  3| -1|  3|   4|
    # Arsenal     |  1|  1|  0|  4|   4|
    # Liverpool   |  1|  1|  0|  4|   4|
    # Everton     |  1|  0| -1|  1|   2|

    # return the table (must be sorted)

    # enter your code here
    f = open(filename, "r")
    s = f.readlines()
    s.pop(0)
    for i in range(len(s)):
        s[i] = s[i].strip("|\n")

    table = []

    for i in range(len(s)):
        table.append(s[i].split("|"))

    for i in range(len(s)):
        for j in range(6):
            table[i][j] = table[i][j].strip()
            if j != 0:
                table[i][j] = int(table[i][j])

    sortTable(table)
    return table
