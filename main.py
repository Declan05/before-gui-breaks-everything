from guizero import App, PushButton, TextBox, Text, Box, Picture
from characters import Assault, Defence, Health
from random import choice
from time import sleep
from replit import audio
from login import login, sign_up
from leaderboard import leaderboard

selected_characters = []

sound = audio.play_file("Main Title Theme.mp3", volume=0.5)

# TO DO: CODE SIGN IN ERROR MESSAGES IN CASE THERE IS NO MATCH WITH USERNAMES OR PASSWORDS

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
    PushButton(main_box, command = lambda:keyboardinterrupt(), width = 5, height = 1, text = "Exit", align = "left")
    return welcome_text, text_label

  
# DEFINING WINDOW CHARACTERISTICS
app = App(title = "Simpsons Brawler",  bg="white")

def home_page():
    main_box = clear_box()
    if valid_sign_in < 2:
        Text(main_box, text="Welcome\nto\nSimpsons Brawler!", size=20)
        text_label = Text(main_box, text="Enter your username ")
        user_name123 = TextBox(main_box, width=20)
        Text(main_box, text="Enter your password ")
        password1 = TextBox(main_box, width=20, hide_text=True)
        buttons = Box(main_box, layout="grid")
        menu_buttons = Box(buttons, layout="grid", grid=[1,0])
        PushButton(menu_buttons, command=lambda:sign_in(user_name123, password1), width=5, height=1, text="Sign in", grid=[0,1])
        PushButton(menu_buttons, command=sign_up_menu, width=5, height=1, text="Sign up", grid=[0,3])
        PushButton(main_box, command = lambda:keyboardinterrupt(), width = 5, height = 1, text = "Exit", align = "left")
        return text_label
    else:
        show_rules()



def keyboardinterrupt():
    clear_box()
home_page()
########### GAME RULES ###########
def show_rules():
    rule_title = Text(main_box,text = "Here are the rules!", size = 20,)
    rules_text = Text(main_box, text = """Welcome to Simpsons Brawler! \nThe rules are simple. Two players select their fighters \nand duke it out until one is defeated!\nOn each turn players can decide from 3 attacks\n They range in the damage that can be dealt.\n""")
    next_page = PushButton(main_box, text="Next",command=coin_flip)  
    
    return rule_title,rules_text,next_page

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
    
    return text,next_button
    
def coin_flip():
    clear_box()
    screen_text = Text(main_box, text=f"{usernames[0]}, pick either heads or tails!")
    heads_button = PushButton(main_box, command=lambda:coin_outcome("heads"), text="Heads")
    tails_button = PushButton(main_box, command=lambda:coin_outcome("tails"), text="Tails", width=5)
    coin_flip_gif = Picture(main_box, image="Pictures/coin-flip-50.gif")
    
    return screen_text, heads_button, tails_button, coin_flip_gif


######### CHARACTER VIEWING  ########
remove_character = []

def view_homer():
    clear_box()
    identifier = "Homer"
    info_box = Box(main_box, layout = "grid")
    homer_pic = Picture(info_box, image="Pictures/Homer_Simpson_2006.png", grid=[2,0])
    homer_stats = Text(info_box, text="----------\nClass: Health\n------------\nHealth: 140\n------------\nDamage: 50\n----------\n", grid = [0,0])
    PushButton(info_box, command = lambda:character_selection[1](), width = 4, height = 1, text = ">", grid=[4,2])
    PushButton(info_box, command = lambda:character_selection[-1](), width = 4, height = 1, text = "<", grid=[0,2])
    if "Homer" in remove_character:
        selection = PushButton(info_box, command=lambda:selected_character(identifier), width = 11, height = 1, text="Select character", grid=[2,2], enabled=False)
    else:
        selection = PushButton(info_box, command=lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2])
        
    return homer_pic, homer_stats, selection
    
def view_lisa():
    clear_box()
    identifier = "Lisa"
    info_box = Box(main_box, layout = "grid")
    lisa_pic = Picture(info_box,image = "Pictures/Lisa_Simpson.png", grid = [2,0])
    lisa_stats = Text(info_box, text="----------\nClass: Defence\n------------\nHealth: 150\n------------\nDamage: 60\n----------\n", grid = [0,0])
    PushButton(info_box, command = lambda:character_selection[2](), width = 4, height = 1, text = ">", grid=[4,2])
    PushButton(info_box, command = lambda:character_selection[0](), width = 4, height = 1, text = "<", grid=[0,2])
    if "Lisa" in remove_character:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2], enabled = False)
    else:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2])

    return lisa_pic, lisa_stats, selection

def view_bart():
    clear_box()
    identifier = "Bart"
    info_box = Box(main_box, layout = "grid")
    bart_pic = Picture(info_box,image = "Pictures/Bart_Simpson_Scaled.png",width = 300, height = 400, grid = [2,0])
    bart_stats = Text(info_box, text="----------\nClass: Assault\n------------\nHealth: 115\n------------\nDamage: 80\n----------\n", grid = [0,0])
    PushButton(info_box, command = lambda:character_selection[0](), width = 4, height = 1, text = ">", grid=[4,2])
    PushButton(info_box, command = lambda:character_selection[1](), width = 4, height = 1, text = "<", grid=[0,2])
    if "Bart" in remove_character:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2], enabled = False)
    else:
        selection = PushButton(info_box, command = lambda:selected_character(identifier), width = 11, height = 1, text = "Select character", grid=[2,2])
    
    return bart_pic, bart_stats, selection

###### CHARACTER SELECTION #########
character_selection = [view_homer, view_lisa, view_bart]

def selected_character(identifier):
    remove_character.append(identifier)
    if identifier == "Homer":
        view_homer()
        selected_characters.append(Health(name="Homer", full_damage=50, health=140, speech="DOH!"))
    elif identifier == "Lisa":
        view_lisa()
        selected_characters.append(Defence(name="Lisa", full_damage=60, health=150, speech="Woe is me...", block_damage=10))
    elif identifier == "Bart":
        view_bart()
        selected_characters.append(Assault(name="Bart", full_damage=80, health=115, speech="Eat my shorts!",damage_multi=8))
        
    if len(remove_character) > 1:
        display_fighting()


###### FIGHTING ##########
def proceed_to_next(attacker, defender):
    if defender.get_health() < 1:
        global player_num
        end_fighting(attacker, defender, player_num)
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
    
    PushButton(attack_buttons, command = lambda:fight_loop(1, player_num, defender_num), text=attacker.get_con_attack(), grid = [1,300])
    PushButton(attack_buttons, command = lambda:fight_loop(2, player_num, defender_num), text=attacker.get_bal_attack(), grid = [3,300])
    PushButton(attack_buttons, command = lambda:fight_loop(3, player_num, defender_num), text=attacker.get_aggro_attack(), grid = [5,300])
    standing = Picture(attack_box, image = f"{remove_character[player_num]}/standing.png", align = "left")

    return defender, standing

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


def restart_game():
    global remove_character, selected_characters
    remove_character = []
    selected_characters = []
    coin_flip()

def go_home():
    global valid_sign_in, remove_character, selected_characters, usernames
    valid_sign_in = 0
    remove_character = []
    selected_characters = []
    usernames = []
    home_page()

def end_fighting(winner, loser, player_num):
    clear_box()
    global first_player, second_player
    Text( main_box, text = f"WINNER is {winner.get_name()}")
    PushButton(main_box, command=restart_game, text="Play Again", width = 8, height = 1)
    PushButton(main_box, text = "Home Page",command=go_home, width = 8, height = 1)
    if "Dam" in usernames or "dam" in usernames or "Damian" in usernames or "damian" in usernames:
        winner = "Damian"
    if player_num == 0:
        winner = first_player
    else:
        winner = second_player
    leaderboard(winner)


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

    return smash, damaged

app.display()

