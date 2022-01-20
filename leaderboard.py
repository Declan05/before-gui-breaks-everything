def leaderboard(winner):
    existing_acc_check = False
    # Adds to leaderboard
    file = open("leaderboard.csv", "r")
    first_pass = 0
    for line in file:
        line = line.strip()
        line = line.split(",")
        line[1] = int(line[1])
        if line[0] == winner:
            line[1] += 1
            existing_acc_check = True
        line = ','.join(map(str, line)) 
        if first_pass == 0:
            leaderboard = open("leaderboard.csv", "w")
            leaderboard.write("")
            leaderboard.close()
            first_pass += 1
        leaderboard = open("leaderboard.csv", "a")
        leaderboard.write(f"{line}\n")
        leaderboard.close()
    leaderboard = open("leaderboard.csv", "a")
    if existing_acc_check == False:
        leaderboard.write(f"{winner},1\n")
    leaderboard.close()
    file.close()
        
    # Get the leaderboard
    file = open("leaderboard.csv", "r")

    leaderboard = []

    for line in file:
        line = line.strip()
        line = line.split(",")
        line[1] = int(line[1])
        leaderboard.append(line)

    sort = sorted(leaderboard, key=lambda row: int(row[1]), reverse=True)

    # PRINT LEADERBOARD
    print("\033[45;30;3mLeaderboard\033[0m:")
    try:
        for x in range(5):
            print(f"Rank {x+1} with {sort[x][1]} wins is {sort[x][0]}")
    # Stops if there isn't enough players to fill leaderboard instead of erroring
    except IndexError:
        pass

    file.close()