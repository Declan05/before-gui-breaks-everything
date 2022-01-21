from guizero import App, PushButton, TextBox, Text, Box, Picture
from characters import Assault, Defence, Health
from random import choice
from time import sleep
from replit import audio
from login import login, sign_up
from leaderboard import leaderboard

selected_characters = []

# TO DO: CODE SIGN IN ERROR MESSAGES IN CASE THERE IS NO MATCH WITH USERNAMES OR PASSWORDS
# TO DO: STOP THE COIN FROM SPINNING AFTER IT LANDS ON A SIDE

# sound = audio.play_file('Main Title Theme.mp3')
# sound.volume = 0.5
# sound.set_loop(5)

######## CLEAR FUNCTION ########
main_box = None
            
def clear_box():
    global main_box
    if main_box is not None:
        main_box.destroy()
    main_box = Box(app,width=700,height=500)
    main_box.bg = "white"

    return main_box
          
###### SIGN IN / SIGN UP #######
valid_sign_in = 0

usernames = []

def sign_in(username, password):
    # error_message = Text(main_box,text="")
    global valid_sign_in
    retrieved_username = username.value
    retrieved_password = password.value
    login_check, player = login(retrieved_username, retrieved_password)
    usernames.append(player)
    if login_check == -10:
        valid_sign_in += 1
        home_page()
    elif login_check == -4:
        # error_message.destroy()
        text = Text(main_box, text = "ERROR")
        text.text_color = "red"

def sign_up_button(username, new_password, confirm_password):
     error_message = Text(main_box, text="")
     username = username.value
     new_password = new_password.value
     confirm_password = confirm_password.value
     sign_up_error = sign_up(username, new_password, confirm_password)
     if sign_up_error == -1:
        error_message.clear()
        error_message = Text(main_box, "Username already taken.")
        error_message.text_color = "red"
     elif sign_up_error == -2:
        error_message.clear()
        error_message = Text(main_box, text = "Passwords do not match.")
        error_message.text_color = "red"
 
def sign_up_menu():
    clear_box()
    welcome_text = Text(main_box, text="Welcome\nto\nSimpsons Brawler!", size=30)
    text_label = Text(main_box, text="Register a new username ")
    username = TextBox(main_box, width=20)
    text_label = Text(main_box, text="Enter a password ")
    new_password = TextBox(main_box, width=20, hide_text=True)
    confirm_password = TextBox(main_box, width=20, hide_text = True)
    buttons = Box(main_box, layout="grid")
    menu_buttons = Box(buttons, layout="grid", grid=[1,0])
    PushButton(menu_buttons, command=home_page, width=5, height=1, text="Go Back", grid=[0,2])
    PushButton(menu_buttons, command=lambda:sign_up_button(username, new_password, confirm_password), width=5, height=1, text="Sign up", grid=[0,1])

  
# DEFINING WINDOW CHARACTERISTICS
app = App(title = "Simpsons Brawler",  bg="white")

def home_page():
    main_box = clear_box()
    if valid_sign_in < 2:
        welcome_text = Text(main_box, text="Welcome\nto\nSimpsons Brawler!", size=20)
        text_label = Text(main_box, text="Enter your username ")
        user_name123 = TextBox(main_box, width=20)
        text_label = Text(main_box, text="Enter your password ")
        password1 = TextBox(main_box, width=20, hide_text=True)
        buttons = Box(main_box, layout="grid")
        menu_buttons = Box(buttons, layout="grid", grid=[1,0])
        PushButton(menu_buttons, command=lambda:sign_in(user_name123, password1), width=5, height=1, text="Sign in", grid=[0,1])
        PushButton(menu_buttons, command=sign_up_menu, width=5, height=1, text="Sign up", grid=[0,3])
    else:
        show_rules()

home_page()
# main_box = Box(app, width=700, height=500, layout = "grid")
# def pass_home():
#     if valid_sign_in < 2:
#         home_page()
#     else:
#         show_rules()

def show_rules():
    rule_title = Text(main_box,text = "Here are the rules!", size = 20,)
    rules_text = Text(main_box, text = """Welcome to Simpsons Brawler! \nThe rules are simple. Two players select their fighters \nand duke it out until one is defeated!\nOn each turn players can decide from 3 attacks\n They range in the damage that can be dealt.\n The more aggressive the attack, the wider the range of damage is done to the opponent. Best of 3 wins the game and your name shall live on in the immortal realm of a cvs file.""")
    # GOTTEN RID OF HEIGHT AND WIDTH IN rules_text
    next_page = PushButton(main_box, text="Next",command=coin_flip)  

######## COIN TOSS #########
def coin_outcome(user_choice):

    clear_box()

    global first_player, second_player
    
    coin = choice(["heads", "tails"]) 
    coin_outcome = f"The coin goes up and...\nIt's {coin}!\n"

    coin = Picture(main_box, image=f"Pictures/{coin}.jpg", width = 300, height= 300)

    if user_choice == coin:
        coin_outcome = coin_outcome + f"{usernames[0]} goes first"
        first_player = usernames[0]
        second_player = usernames[1]
    else:
        coin_outcome = coin_outcome + f"{usernames[1]} goes first"
        first_player = usernames[1]
        second_player = usernames[0]
        
    text = Text(main_box, text=coin_outcome, align="left")
    
    next_button = PushButton(main_box, text="Next", command=view_homer)
    
    
def coin_flip():
    clear_box()
    screen_text = Text(main_box, text=f"{usernames[0]}, pick either heads or tails!")
    heads_button = PushButton(main_box, command=lambda:coin_outcome("heads"), text="Heads")
    tails_button = PushButton(main_box, command=lambda:coin_outcome("tails"), text="Tails", width=5)
    coin_flip_gif = Picture(main_box, image="Pictures/coin-flip-50.gif")


######### CHARACTER VIEWING  ########
remove_character = []

def view_homer():
    clear_box()
    identifier = "Homer"
    info_box = Box(main_box, layout = "grid")
    homer_pic = Picture(info_box, image="Pictures/Homer_Simpson_2006.png", grid=[2,0])
    homer_stats = Text(info_box, text="----------\nClass: Health\n------------\nHealth: 280\n------------\nDamage: 50\n----------\n", grid = [0,0])
    PushButton(info_box, command = lambda:character_selection[1](), width = 4, height = 1, text = ">", grid=[4,2])
    PushButton(info_box, command = lambda:character_selection[-1](), width = 4, height = 1, text = "<", grid=[0,2])
    if "Homer" in remove_character:
        selection = PushButton(info_box, command=lambda:selected_character(identifier), width = 11, height = 1, text="Select character", grid=[2,2], enabled=False)
    else:
        selection = PushButton(info_box, command=lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2])
    
def view_lisa():
    clear_box()
    identifier = "Lisa"
    info_box = Box(main_box, layout = "grid")
    lisa_pic = Picture(info_box,image = "Pictures/Lisa_Simpson.png", grid = [2,0])
    lisa_stats = Text(info_box, text="----------\nClass: Defence\n------------\nHealth: 300\n------------\nDamage: 60\n----------\n", grid = [0,0])
    PushButton(info_box, command = lambda:character_selection[2](), width = 4, height = 1, text = ">", grid=[4,2])
    PushButton(info_box, command = lambda:character_selection[0](), width = 4, height = 1, text = "<", grid=[0,2])
    if "Lisa" in remove_character:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2], enabled = False)
    else:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2])

def view_bart():
    clear_box()
    identifier = "Bart"
    info_box = Box(main_box, layout = "grid")
    bart_pic = Picture(info_box,image = "Pictures/Bart_Simpson_Scaled.png",width = 300, height = 400, grid = [2,0])
    bart_stats = Text(info_box, text="----------\nClass: Assault\n------------\nHealth: 230\n------------\nDamage: 80\n----------\n", grid = [0,0])
    PushButton(info_box, command = lambda:character_selection[0](), width = 4, height = 1, text = ">", grid=[4,2])
    PushButton(info_box, command = lambda:character_selection[1](), width = 4, height = 1, text = "<", grid=[0,2])
    if "Bart" in remove_character:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2], enabled = False)
    else:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2])

###### CHARACTER SELECTION #########
character_selection = [view_homer, view_lisa, view_bart]

def selected_character(identifier):
    remove_character.append(identifier)
    if identifier == "Homer":
        view_homer()
        selected_characters.append(Health(name="Homer", full_damage=50, health=280, speech="DOH!"))
    elif identifier == "Lisa":
        view_lisa()
        selected_characters.append(Defence(name="Lisa", full_damage=60, health=300, speech="Woe is me...", block_damage=10))
    elif identifier == "Bart":
        view_bart()
        selected_characters.append(Assault(name="Bart", full_damage=80, health=230, speech="Eat my shorts!",damage_multi=8))
        
    if len(remove_character) > 1:
        display_fighting()


###### FIGHTING ##########

def proceed_to_next(attacker, defender):
  if defender.get_health() < 1:
    end_fighting(attacker, defender)
  else :
    display_fighting()


player_num = 1
round_num = 1
def display_fighting():
    clear_box()
    global player_num
    global round_num
    attack_box =Box(main_box, border=False, width="fill" ,height=250)
    defender = selected_characters[player_num]
    
    standing = Picture(attack_box, image=f"{remove_character[player_num]}/standing_reversed.png", align = "right")
    defender_num = player_num
    if player_num == 1:
        player_num -= 1
    elif player_num == 0:
        player_num += 1
    attacker = selected_characters[player_num]
    attack_buttons= Box(main_box, layout = "grid", align = "bottom", width = "fill", height = 250, border = True)
    Text(attack_buttons, text = f"Round {round_num}", grid = [9,0])
    
    PushButton(attack_buttons, command = lambda:fight_loop(1, player_num, defender_num), text=attacker.get_con_attack(), grid = [45,300])
    PushButton(attack_buttons, command = lambda:fight_loop(2, player_num, defender_num), text=attacker.get_bal_attack(), grid = [50,300])
    PushButton(attack_buttons, command = lambda:fight_loop(3, player_num, defender_num), text=attacker.get_aggro_attack(), grid = [55,300])
    standing = Picture(attack_box, image = f"{remove_character[player_num]}/standing.png", align = "left")


def fight_loop(attack_type, attacker_num, defender_num):
    global fixed_health_player_1
    global fixed_health_player_2

    attacker = selected_characters[attacker_num]
    defender = selected_characters[defender_num]
    fixed_health_player_1 = attacker.get_health()
    fixed_health_player_2 = defender.get_health()
    fight(attacker, defender, attack_type)


player_1_score = 0
player_2_score = 0
fixed_health_player_1 = 50
fixed_health_player_2 = 50
asdasd = True


def end_fighting(winner, loser):
    clear_box()
    Text( main_box, text = f"WINNER is {winner.get_name()}")
    PushButton(main_box, command=coin_flip, text="Play Again", width = 8, height = 1)
    PushButton(main_box, text = "Home Page",command=home_page, width = 8, height = 1)

  

def fight(attacker, defender, attack_type):
    global fixed_health_player_1, fixed_health_player_2, player_num, player_1_score, player_2_score, round_num, asdasd
    if asdasd == True:
        fixed_health_player_1 = attacker.get_health()
        fixed_health_player_2 = defender.get_health() 
        asdasd = False

    clear_box()
    Box(main_box)
    attack_box =Box(main_box, border = False , width = "fill", height = 250)
    if attack_type == 1:
        smash = Picture(attack_box, image = f"{attacker.get_name()}/attack_1.png", 
        align = "left")
        damaged = Picture(attack_box, image = f"{defender.get_name()}/hurt_reversed.png", align = "right")
        Text(main_box, text = f"{attacker.get_name()} used {attacker.get_con_attack()} ",size = 10)
        PushButton(main_box, command=proceed_to_next, args=[attacker, defender], text="Next")
    elif attack_type == 2:
        smash = Picture(attack_box, image = f"{attacker.get_name()}/attack_2.png", align = "left")
        Text(main_box, text = f"{attacker.get_name()} used {attacker.get_bal_attack()} ",size = 10)
        damaged = Picture(attack_box, image = f"{defender.get_name()}/hurt_reversed.png", align = "right")
        PushButton(main_box, command=proceed_to_next, args=[attacker, defender], text="Next")
    elif attack_type == 3:
        smash = Picture(attack_box, image = f"{attacker.get_name()}/attack_3.png", align = "left")
        Text(main_box, text = f"{attacker.get_name()} used {attacker.get_aggro_attack()} ",size = 10)
        damaged = Picture(attack_box, image = f"{defender.get_name()}/hurt_reversed.png", align = "right")
        PushButton(main_box, command=proceed_to_next, args=[attacker, defender], text="Next")
    attacker.attack(defender, attack_type)

    # if defender.get_health() < 1:
    #     dead = Picture(attack_box, image = f"{defender.get_name()}/dead_reversed.png", align = "right")
    #     round_num +=1
    #     if player_num == 0:
    #         player_1_score +=1
            
    #     else:
    #         player_2_score +=1
            
    #     if player_1_score + player_2_score > 4:
    #         pass

    #     # the reason this isn't working is because the characters on screen aren't using the classes: selected_characters[0] and selected_characters[1]. The classes we're using are attacker and defender
    #     selected_characters[0].set_health = fixed_health_player_1
    #     selected_characters[1].set_health = fixed_health_player_2




app.display()


# Moved the volume into the same line as play_file()
# and that seemed to fix it - Sam H :)
# sound = audio.play_file("Main Title Theme.mp3", volume=0.5)
# # PEPE/PEP-8

round_num = 1

# PROVIDE 3 CHARACTERS - DONE
lisa = Defence(name="Lisa", full_damage=60, health=300, speech="Woe is me...", block_damage=10)

bart = Assault(name="Bart", full_damage=80, health=230, speech="Eat my shorts!",damage_multi=8)

homer = Health(name="Homer", full_damage=50, health=280, speech="DOH!")


# ATTACKING SEQUENCE

# player_1_wins = 0
# player_2_wins = 0

# fixed_health_player_1 = player_1.get_health()
# fixed_health_player_2 = player_2.get_health()

# BEST OF THREE - SHOULD NOT CONTINUE ONTO THIRD ROUND IF A PLAYER HAS ALREADY WON THE LAST TWO
# while round_num < 2:

#     # WE MUST REPLENISH HEALTH IN BETWEEN EACH ROUND
    # player_1.set_health(fixed_health_player_1)
    # player_2.set_health(fixed_health_player_2)

#     #print(f"ROUND {round_num}")

#     while player_1.get_health() > 0 and player_2.get_health() > 0:
            
#         fight(player_1, player_2)

#         if player_1.get_health() < 1:
#             player_2_wins += 1
#         elif player_2.get_health() < 1:
#             player_1_wins += 1
#         else:
#             fight(player_2, player_1)
#     round_num += 1

# if player_1_wins > player_2_wins:
#     #print(f"{first_player} WINS")
#     winner = first_player
# else:
#     #print(f"{second_player} WINS ")
#     winner = second_player
# #now we need to establish whether player one is username 1 or username 2
# leaderboard(winner)

# #print("""
# -------------------------------------------------
# -------------------------------------------------
# """)