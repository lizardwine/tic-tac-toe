import os
table = [["*", "*", "*"], ["*", "*", "*"], ["*", "*", "*"]]
positions = {
    1: (0, 0),
    2: (0, 1),
    3: (0, 2),
    4: (1, 0),
    5: (1, 1),
    6: (1, 2),
    7: (2, 0),
    8: (2, 1),
    9: (2, 2)
}
def print_table(table):
    c = 1
    ch = 1
    for i in table:
        cv = 1
        for j in i:
            print("  " + (str(c) if j == "*" else j) + f"  " + ("|" if cv < 3 else ""), end="")
            c += 1
            cv += 1
        print(("\n" + "-"*17) if ch < 3 else "")
        ch += 1
def movement(pos, xo):
    global table
    y, x = positions[pos][0], positions[pos][1]
    table[y][x] = xo
def check(table):
    wins = [[[0, 0], [0, 1], [0, 2]], [[0, 0], [1, 0], [2, 0]],
            [[0, 0], [1, 1], [2, 2]], [[0, 2], [1, 1], [2, 0]],
            [[0, 1], [1, 1], [2, 1]], [[0, 2], [1, 2], [2, 2]],
            [[1, 0], [1, 1], [1, 2]], [[2, 0], [2, 1], [2, 2]]]
    for xo in ["X", "O"]:
        for i in wins:
            tt = []
            for j in i:
                y, x = j[0], j[1]
                if table[y][x] == xo:
                    tt.append(True)
                else:
                    tt.append(False)
            if tt == [True, True, True]:
                return f"{xo} Wins."
    return "Tie."
def play():
    poss = list(range(1, 10))
    x = False
    while True:
        os.system("clear")
        print_table(table)
        x = not x
        xo = "X" if x else "O"
        pos = ""
        try:
            pos = int(input(f"{xo}: "))
        except:
            ...
        while not pos in poss:
            if type(pos) == str:
                print("Expected a number.")
            elif pos > 9 or pos < 1: 
                print("Expected a number between 1 and 9.")
            elif not pos in poss:
                print(f"{pos} is already placed.")
            pos = input(f"{xo}: ")
            try:
                pos = int(pos)
            except:
                continue
        poss.pop(poss.index(pos))
        movement(pos, xo)
        wot = check(table)
        if wot.endswith("Wins.") or (wot == "Tie." and poss == []):
            os.system("clear")
            print_table(table)
            print(wot)
            break
play()