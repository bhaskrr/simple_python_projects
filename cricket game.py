import random

over = int(input("Enter overs: "))
batter_choices = [0, 1, 2, 3, 4, 6, "out", "wide", "no ball"]

total_runs = 0
overs = 0
wickets = 0
extras = 0


for i in range(over):  # counts overs
    j = 0
    while j < 6 and wickets < 10:  # counts balls
        player_choice = random.choice(batter_choices)
        if player_choice == "out":
            wickets += 1
            j += 1
            print(player_choice)
            continue

        elif player_choice == "wide" or player_choice == "no ball":
            total_runs += 1
            extras += 1
            print(player_choice)
            continue

        total_runs += player_choice  # counts total runs
        print(player_choice)
        j += 1

    if wickets < 10:
        overs += 1

    # prints stats
    print(f"Total runs: {total_runs}")
    print(f"Overs: {overs}")
    print(f"Wickets: {wickets}")
    print(f"Extras: {extras}")

    if wickets == 10:
        break
