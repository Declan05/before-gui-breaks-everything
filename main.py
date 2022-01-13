from characters import Character, Assault, Defence, Health
from random import randint, choice
from time import sleep
from replit import audio
from login import login
# sound = audio.play_file('Main Title Theme.mp3')
# sound.volume = 0.5
# sound.set_loop(5)

# Moved the volume into the same line as play_file()
# and that seemed to fix it - Sam H :)
sound = audio.play_file("Main Title Theme.mp3", volume=0.5)

print("""
+++++++++++++++++++++++++++++++++++++++++++++++++
+++++++++++++++++++++++++++++++++++++++++++++++++
""")
# # PEPE/PEP-8
# from termcolor import cprint

p1_name = login()
p2_name = login()


# # EXPLAIN THE RULES
"""Welcome to Simpsons Brawler! The rules are simple. Two players select their fighters and duke it out until one is defeated! The best of 3 wins the game and your name shall live on in the immortal realm of a text file."""

# PROVIDE 3 CHARACTERS - DONE
lisa = Defence(name="Lisa", full_damage=60, health=300, speech="Woe is me...", block_damage=10)

maggie = Assault(name="Maggie", full_damage=80, health=230, speech="*Pacifier noises*",damage_multi=8)

homer = Health(name="Homer", full_damage=50, health=280, speech="DOH!")

# # COIN TOSS
coin_toss = input(f"{p1_name}, Heads or Tails? ").lower() 
if "h" in coin_toss:
    print(f"{p2_name}, you're picking tails!")
    selected_coin_face = "heads"
else:
    print(f"{p2_name}, you're picking heads!") 
    selected_coin_face = "tails"
    
sleep(1)
print("The coin goes up and...")  
coin = choice(["heads", "tails"]) 
print(f"It's {coin}!"
)

if selected_coin_face == coin:
    print(f"{p1_name} goes first")
    first_player = p1_name
    second_player = p2_name
else:
    print(f"{p2_name} goes first")
    first_player = p2_name
    second_player = p1_name

# CHARACTER SELECTION

print("""
1. Homer
2. Lisa
3. Maggie
""")


def fighter_choice(player_name):

    confirmation = "no"
    while confirmation == "no":
        choice_1 = input(f"{player_name} pick your character! ").lower()

        if "1" in choice_1 or "homer" in choice_1:
            homer.describe()
            confirmation = input(
                "Would you like to select this character?\nYes\nNo\n> ").lower()
            if "yes" in confirmation:
                character = Health(name="Homer", full_damage=50, health=300, speech="DOH!")

        elif "2" in choice_1 or "lisa" in choice_1:
            lisa.describe()
            confirmation = input(
                "Would you like to select this character?\nYes\nNo\n> ").lower(  )
            if "yes" in confirmation:
                character = Defence(name="Lisa", full_damage=60, health=300, speech="Woe is me...", block_damage=10)

        elif "3" in choice_1 or "maggie" in choice_1:
            maggie.describe()
            confirmation = input(
                "Would you like to select this character?\nYes\nNo\n> ")
            if "yes" in confirmation:
                character = Assault(name="Maggie", full_damage=80, health=230, speech="*Pacifier noises*",damage_multi=8)
        else:
            print("\033[31mSelect a character number in the list\033[0m")
    return character

##################################################################


player_1 = fighter_choice(first_player)
player_2 = fighter_choice(second_player)

while player_1 == player_2:
    print("Sorry you can't pick the same character!")
    player_2 = fighter_choice(p2_name)

# ATTACKING SEQUENCE

player_1_wins = 0
player_2_wins = 0

fixed_health_player_1 = player_1.get_health()
fixed_health_player_2 = player_2.get_health()

# BEST OF THREE - SHOULD NOT CONTINUE ONTO THIRD ROUND IF A PLAYER HAS ALREADY WON THE LAST TWO
while player_1_wins + player_2_wins < 3:

    # WE MUST REPLENISH HEALTH IN BETWEEN EACH ROUND
    player_1.set_health(fixed_health_player_1)
    player_2.set_health(fixed_health_player_2)

    print(f"ROUND {player_1_wins + player_2_wins + 1}")

    while player_1.get_health() > 0 and player_2.get_health() > 0:
        def fight(attacker, defender):
            print(f"{attacker.get_name()}")
            attacker.attack(defender)
            
        fight(player_1, player_2)

        if player_1.get_health() < 1:
            player_2_wins += 1
        elif player_2.get_health() < 1:
            player_1_wins += 1
        else:
            fight(player_2, player_1)

if player_1_wins > player_2_wins:
    print("PLAYER 1 WINS")
else:
    print("PLAYER 2 WINS ")
print("now we need to establish whether player one is username 1 or username 2")

  
# # ADD 1 POINT TO EXISTING LEADERBOARD NAMES
file = open("leaderboard.csv", "r")
for line in file:
    print(line)
    line = line.strip()
    print(line)
    line = line.split(",")
    print(line)
    line[1] = int(line[1])
    print(line)
    
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
for x in range(5):
  print(f"Rank {x+1} with score {sort[x][1]}: {sort[x][0]}")