import collections
from collections import Counter

def tally(rows):
    table = ["Team                           | MP |  W |  D |  L |  P"]
    rowList =  [y.strip() for x in rows for y in x.split(";")]
    # get rid of win, draw, loss
    del rowList[2::3]
    a = 0
    for key, value in Counter(rowList).items():
        a += 1
        table.append("Team                           ")
        table[a] = table[a].replace("Team", key)[:31] + "| MP |  W |  D |  L |  P"
        table[a] = table[a].replace("MP", " " + str(value))
    table.pop(0)
    # Separate in different lists the winners, losers, and teams with draw matches
    winners = [y.strip() for x in rows if x.endswith("win") for y in x.split(";")]
    loser = [y.strip() for x in rows if x.endswith("loss") for y in x.split(";")]
    draw = [y.strip() for x in rows if x.endswith("draw") for y in x.split(";")]
    countWin = winners[::3] + loser[1::3] + ["countWin"]
    loser = loser[::3] + winners[1::3] + ["loser"]
    table = counter(countWin, table)
    table = counter(loser, table)
    table = counter(draw, table)
    table = applyZeros(table)
    #First sort the table by points
    table.sort(key = lambda x: int(x[-1]))
    table = table[::-1]
    #Sort table by alphabetic order if pair teams have the same points
    [table.sort() for x, y in zip(table, table[1:]) if x[-1] == y[-1] and len(table)<3]
    table.insert(0, "Team                           | MP |  W |  D |  L |  P")
    return table

def counter(result, table):
    points = 0
    for key, value in Counter(result).items():
        for item in range (len(table)):
            if table[item].split('  ', 1)[0] == key:
                if "countWin" in result:
                    table[item] = table[item].replace(" W ", " " + str(value) + " ")
                    points = value * 3
                    table[item] = table[item].replace(" P", " " + str(points))
                elif "loser" in result:
                    table[item] = table[item].replace(" L ", " " + str(value) + " ")
                elif "draw" in result:
                    table[item] = table[item].replace(" D ", " " + str(value) + " ")
                    points = points + 1
                    if table[item].find("|  P") != -1:
                        table[item] = table[item].replace(" P", " " + str(points))
                    #Will add points to the ones who won so we are casting from str to num and the oposite
                    else:
                       table[item] = table[item].replace("".join(filter(str.isdigit, table[item][-1])), str(int(table[item][-1])+points))
                    points = 0
    return table

def applyZeros(table):
    for item in range (len(table)):
        for x,y in ({ " W ": " 0 ", " D ": " 0 ", " L ": " 0 ", " P": " 0"}).items():
            table[item] = table[item].replace(x, y)
    return table