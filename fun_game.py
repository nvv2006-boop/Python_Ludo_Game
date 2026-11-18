# By submitting this assignment, I agree to the following:
#   "Aggies do not lie, cheat, or steal, or tolerate those who do."
#   "I have not given or received any unauthorized aid on this assignment."
#
# Names:        Ryan Makelki
#               Navya Vegesna
#               Ranveer Hayr
#               Sampadha Uppu
# Section:      512
# Assignment:   Lab 13-2 (team)
# Date:         14 November 2024




############  We are making Ludo ##############################
import tkinter as tk
from PIL import Image, ImageTk
import random
from tkinter import messagebox

## Important starting variables for memory
bl = 'blue'
gr = 'green'
re = 'red'
ye = 'yellow'
wh = 'blank'
bs = 'blsqr'
gs = 'grsqr'
ys = 'ylsqr'
rs = 'resqr'
ws = 'whsqr'
mm = 'mm'
tl = 'tl'
tr = 'tr'
bl = 'bl'
br = 'br'
gt = 'gt'
yt = 'yt'
bt = 'bt'
rt = 'rt'
start_square = {'green':1, 'blue': 14, 'yellow':27, 'red':40}
safe_spaces = [9,22,35,48]
background = [[gs,gs,gs,gs,gs,gs,ws,ws,ws,ys,ys,ys,ys,ys,ys],
              [gs,ws,ws,ws,ws,gs,ws,ys,ys,ys,ws,ws,ws,ws,ys],
              [gs,ws,gs,gs,ws,gs,gt,ys,ws,ys,ws,ys,ys,ws,ys],
              [gs,ws,gs,gs,ws,gs,ws,ys,ws,ys,ws,ys,ys,ws,ys],
              [gs,ws,ws,ws,ws,gs,ws,ys,ws,ys,ws,ws,ws,ws,ys],
              [gs,gs,gs,gs,gs,gs,ws,ys,ws,ys,ys,ys,ys,ys,ys],
              [ws,gs,ws,ws,ws,ws,tl,ys,tr,ws,ws,ws,yt,ws,ws],
              [ws,gs,gs,gs,gs,gs,gs,mm,bs,bs,bs,bs,bs,bs,ws],
              [ws,ws,rt,ws,ws,ws,bl,rs,br,ws,ws,ws,ws,bs,ws],
              [rs,rs,rs,rs,rs,rs,ws,rs,ws,bs,bs,bs,bs,bs,bs],
              [rs,ws,ws,ws,ws,rs,ws,rs,ws,bs,ws,ws,ws,ws,bs],
              [rs,ws,rs,rs,ws,rs,ws,rs,ws,bs,ws,bs,bs,ws,bs],
              [rs,ws,rs,rs,ws,rs,ws,rs,bt,bs,ws,bs,bs,ws,bs],
              [rs,ws,ws,ws,ws,rs,rs,rs,ws,bs,ws,ws,ws,ws,bs],
              [rs,rs,rs,rs,rs,rs,ws,ws,ws,bs,bs,bs,bs,bs,bs]]


##Variables that can change
locations = {'green': [0,-1,-2,-3], 'blue': [0,-1,-2,-3], 'red': [0,-1,-2,-3], 'yellow': [0,-1,-2,-3]}
homes0 = {'green':True,'yellow':True,'blue':True,'red':True}
scores = {'green':0,'yellow':0,'blue':0,'red':0}
turn = [0]  
roll = [0]
six_in_row = [0]
captured = [False]
new_roll = [False]


game_window = tk.Tk()

####### Images ########
imgbs= Image.open(r"Ludo Images/blue_square.png")
blue_square = ImageTk.PhotoImage(imgbs)

imggs= Image.open(r"Ludo Images/green_square.png")
green_square = ImageTk.PhotoImage(imggs)

imgys= Image.open(r"Ludo Images/yellow_square.png")
yellow_square = ImageTk.PhotoImage(imgys)

imgrs= Image.open(r"Ludo Images/red_square.png")
red_square = ImageTk.PhotoImage(imgrs)

imgws= Image.open(r"Ludo Images/white_square.png")
white_square = ImageTk.PhotoImage(imgws)

imgwc = Image.open(r"Ludo Images/white_circle.png")
white_circle = ImageTk.PhotoImage(imgwc)

imgrc = Image.open(r"Ludo Images/red_circle.png")
red_circle = ImageTk.PhotoImage(imgrc)

imggc = Image.open(r"Ludo Images/green_circle.png")
green_circle = ImageTk.PhotoImage(imggc)

imgyc = Image.open(r"Ludo Images/yellow_circle.png")
yellow_circle = ImageTk.PhotoImage(imgyc)

imgbc = Image.open(r"Ludo Images/blue_circle.png")
blue_circle = ImageTk.PhotoImage(imgbc)

imgmm = Image.open(r"Ludo Images/middle split square.png")
middle_middle = ImageTk.PhotoImage(imgmm)

imgbl = Image.open(r"Ludo Images/middle_bottom_left.png")
bottom_left = ImageTk.PhotoImage(imgbl)

imgbr = Image.open(r"Ludo Images/middle_bottom_right.png")
bottom_right = ImageTk.PhotoImage(imgbr)

imgtl = Image.open(r"Ludo Images/middle_left_corner.png")
top_left = ImageTk.PhotoImage(imgtl)

imgtr = Image.open(r"Ludo Images/middle_yellow_blue.png")
top_right = ImageTk.PhotoImage(imgtr)

imggt = Image.open(r"Ludo Images/green_star.png")
green_star = ImageTk.PhotoImage(imggt)

imgyt = Image.open(r"Ludo Images/yellow_star.png")
yellow_star = ImageTk.PhotoImage(imgyt)

imgbt = Image.open(r"Ludo Images/blue_star.png")
blue_star = ImageTk.PhotoImage(imgbt)

imgrt = Image.open(r"Ludo Images/red_star.png")
red_star = ImageTk.PhotoImage(imgrt)

colors = {'blue':blue_circle,'green':green_circle, 'red':red_circle, 'yellow':yellow_circle}
home_squares = {'blue':blue_square,'green':green_square, 'red':red_square, 'yellow':yellow_square}
bg_images = {'blsqr': blue_square,'grsqr':green_square,'ylsqr': yellow_square,'resqr':red_square,'whsqr': white_square,'mm': middle_middle, 'tr':top_right,'tl':top_left,'br':bottom_right,'bl':bottom_left, 'gt':green_star,'yt':yellow_star,'rt':red_star,'bt':blue_star}



#################################   Important functions  ###################################

##starts the game
def start():
    """
Opens a window for choosing the number of players.

This function creates a new window where the user can pick between 2, 3, or 4 players. 
It also closes the previous windows (like the main menu or instructions) to keep 
everything clean. The window uses buttons for player selection, and each button calls 
the `players()` function with the selected number.

Pop-up Variables:
    play: Button widgets used to select the number of players.
    rules, instructions, load_game1: Other windows that get closed when this starts.
    player_window: The new window where player selection happens.
"""
    global play
    global rules
    global instructions
    global load_game1
    global player_window
    player_window = tk.Tk()
    play.destroy()
    rules.destroy()
    instructions.destroy()
    load_game1.destroy()
    label1 = tk.Label(player_window, text = 'Select Number of Players', height=10, width=40)
    label1.grid(row = 1, column = 1)
    play = tk.Button(player_window, text = '2 Players', command=lambda: players(2), height=5, width=40)
    play.grid(row = 2, column = 1)
    play = tk.Button(player_window, text = '3 Players', command=lambda: players(3), height=5, width=40)
    play.grid(row = 2, column = 2)
    play = tk.Button(player_window, text = '4 Players', command=lambda: players(4), height=5, width=40)
    play.grid(row = 2, column = 3)
    player_window.mainloop()

def generate():
    for i in range (15):
        for j in range(15):
            # print(background[i][j])
            label1 = tk.Label(game_window, image = bg_images[background[i][j]], height=50, width=50)
            label1.grid(row = i, column = j)   
    ##pieces
    generate_pieces()
    ##Die
    dice = tk.Button(game_window, text = 'Roll', command=lambda: dice_roll(), height=2, width=8)
    dice.grid(row = 1, column = 15)
    label1 = tk.Label(game_window, text = roll[0], height=2, width=10)
    label1.grid(row = 1, column = 16)
    ##Save game
    dice = tk.Button(game_window, text = 'Save Game', command=lambda: save_game(), height=2, width=8)
    dice.grid(row = 0, column = 15)
    ##Current turn
    label1 = tk.Label(game_window, text = 'Current Turn:', height=2, width=10)
    label1.grid(row = 2, column = 15)
    current_player = turn_order[turn[0]]
    ##Quit
    dice = tk.Button(game_window, text = 'Quit Game', command=lambda: game_window.destroy(), height=2, width=8)
    dice.grid(row = 3, column = 15) 
    loc = tk.Button(game_window, text = "Can't Move", command=lambda: cant_move(), height=2, width=8)
    loc.grid(row = 4, column = 15)
    label1 = tk.Label(game_window, image = home_squares[current_player], height=47, width=47)
    label1.grid(row = 2, column = 16)
    scoreboard()

def cant_move():
    next_turn()
    new_roll[0] = False

def debug():
    print('Locations:')
    for i in locations:
        print(f"            '{i}': {locations[i]}")
    print(f'Homes0:     {homes0}')
    print(f'Turn order: {turn_order}')
    print(f'Scores:     {scores}')
    print(f'Turn:       {turn[0]}')
    print(f'Roll:       {roll[0]}')
    print(f'Sixes:      {six_in_row[0]}')
    print(f'Captured:   {captured[0]}')
    print(f'New Roll:   {new_roll[0]}')

def load_game():
    global turn_order
    global play
    global rules
    global instructions
    global load_game
    play.destroy()
    rules.destroy()
    instructions.destroy()
    load_game1.destroy()
    #########Load stuff in from save file here #####################
    save_file = open('Ludo_save_file.txt','r')
    s = save_file.readlines()
    loc = s[0:4]
    num = 0
    for i in locations:
        loc1 = loc[num].split(',')[0:-1]
        locations[i] = loc1
        for p in range(len(locations[i])):
            locations[i][p] = int(locations[i][p])            
        num+=1
    t = s[4].split(',')
    turn_order = []
    for i in t[0:4]:
        turn_order.append(i)
    h = s[5].split(',')[0:4]
    num = 0
    for i in homes0:
        homes0[i] = bool(h[num])
        num+=1
    sc = s[6].split(',')[0:4]
    num = 0
    for i in scores:
        scores[i] = int(sc[num])
        num+=1
    turn[0] = int(s[7][0])
    roll[0] = int(s[8][0])
    six_in_row[0] = int(s[9][0])
    captured[0] = bool(s[10][:-1])
    new_roll[0] = bool(s[11][:-1])
    debug()
    
    ################################################################
    generate()

## Selects number of players
def players(x):
    global turn_order
    global player_window
    player_window.destroy()
    if x == 2:
        turn_order = ['green','red']
    elif x == 3:
        turn_order = ['green','yellow','red']
    elif x == 4:
        turn_order = ['green','yellow','blue','red']
    generate()
    
     
def dice_roll():
    """
    Simulates a six sided dice roll.

    Returns
    -------
    int:
        A random integer between 1 through 6, inclusive, replicating a dice roll.
    """
    roll[0] = random.randint(1,6)
    label1 = tk.Label(game_window, text = roll[0], height=2, width=10)
    label1.grid(row = 1, column = 16)
    new_roll[0] = True

def generate_pieces():
    """
   Puts all the players' game pieces on the board in the right spots.

   This function checks where each player's pieces are supposed to be and puts them there. If a piece 
   is still at the starting position (not yet on the board), it places them in the home area for that 
   player. If the piece is already on the board, it uses the square's coordinates to place it.

   Here's the breakdown:
   1. Loops through all the players and their four pieces.
   2. Figures out where the piece is:
      - If the piece hasn't started, it's placed in the home area (specific rows and columns 
        based on the player's color).
      - If the piece is on the board, we figure out the board location using `coordinates()`.
   3. Uses `make_button()` to place the piece on the board visually.

   Note:
   - Each player's home area is defined by their color: 
     - Green: Top-left corner.
     - Yellow: Top-right corner.
     - Red: Bottom-left corner.
     - Blue: Bottom-right corner.

   No Arguments:
   - This function uses global variables like `locations` to figure out where the pieces should go.

   """
    for player in locations:
        for number in range(4):
            img = colors[player]
            if locations[player][number]<0 or locations[player][number]==0 and homes0[player]:
                if player == 'green':
                    row = 2
                    column = 2
                elif player == 'yellow':
                    row = 2
                    column = 11
                elif player =='red':
                    row = 11
                    column = 2
                elif player =='blue':
                    row = 11
                    column =11
                row+= (number//2)
                column+= (number%2)
            elif locations[player][number]>60 and locations[player][number]%100>4:
                ()
            else:
                row,column = coordinates(locations[player][number])
            make_button(row,column,player,locations[player][number],roll[0],number,img)

def next_turn():
    turn[0] += 1
    global game_window
    if turn[0] == len(turn_order):
        turn[0] = turn[0]%(len(turn_order))
    current_player = turn_order[turn[0]]
    label1 = tk.Label(game_window, image = home_squares[current_player], height=47, width=47)
    label1.grid(row = 2, column = 16)
    six_in_row[0] = 0

def rules1():
    rules_window = tk.Tk()
    rules_label = tk.Label(rules_window, text="RULES OF LUDO: Ludo is a 2-4 player game where each player \n aims to move their four pieces from the Home Base to the Finish. \n A roll of 6 is required to move a piece onto the board, and players get an extra turn for rolling a 6. \n Pieces move based on die rolls, and landing on an opponent's piece \n sends it back to the Home Base. Safe zones protect pieces from being captured. \n To win, a player must move all four pieces to the Finish by rolling the exact number needed. \n The first to do so wins!")

    rules_label.grid(row=1, column=1)
    rules_label.mainloop()

def show_instructions():
    instructions = """
    Welcome to Ludo!
    
    Objective:
    Each player must move all four of their tokens from the starting arean/to the finishing area. The first player to do so wins the game.

    Basic Rules:
    1. Roll a six to move a token out of the starting area.
    2. Tokens move clockwise around the board.
    3. If your token lands on an opponent's token, the opponent's token /nis sent back to their starting area.
    4. Safe zones protect tokens from being captured.
    5. Capturing a piece or rolling a six grants an additional turn, but three consecutive sixes /nforfeits the turn.
    6. Tokens must reach the finish area with an exact dice roll.
    
    Have fun and good luck!
    """
    messagebox.showinfo("Ludo Instructions", instructions)

## checks if all 4 pieces are in the home
def check_home(color,piece_index):
    if piece_index ==0:
        return homes0[color]
    else:
        return piece_index<0

def check_start(player):
    x = True
    for i in locations[player]:
        if i == start_square[player]:
            x = False
        else:
            ()
    return x

def coordinates(x):
    if x <=5:
        return 6, x
    elif 6<=x<=11:
        return 11-x,6
    elif x == 12:
        return 0,7
    elif 13<=x<=18:
        return x-13,8
    elif 19<=x<=24:
        return 6,x-10
    elif x == 25:
        return 7,14
    elif 26<=x<=31:
        return 8,40-x
    elif 32<=x<=37:
        return x-23,8
    elif x ==38:
        return 14,7
    elif 39<=x<=44:
        return 53-x,6
    elif 45<=x<=50:
        return 8,50-x
    elif x ==51:
        return 7,0
    elif 100<=x<=199:
        return 7,x-99
    elif 200<=x<=299:
        return x-199,7
    elif 300<=x<=399:
        return 7,313-x
    elif 400<=x<=499:
        return 413-x,7

##returns the coordinate of starting location based on color
def start_coordinate(x):
    if x =='green':
        return 6,1
    elif x =='red':
        return 13,6
    elif x =='blue':
        return 8,13
    elif x =='yellow':
        return 1,8
    else:
        ()

##Fills the missing location at the home in
def fill_home(player, piece_index):
    img = home_squares[player]
    if player == 'green':
        row = 2
        column = 2
    elif player == 'yellow':
        row = 2
        column = 11
    elif player =='red':
        row = 11
        column = 2
    elif player =='blue':
        row = 11
        column =11
    row+= (piece_index//2)
    column+= (piece_index%2)
    label1 = tk.Label(game_window, image = img, height=50, width=50)
    label1.grid(row = row, column = column)

##move the player from home
def leave_home(player, piece_index, dice_roll, piece_number, img):
    
    if player == 'green':
        num = 1
    elif player == 'red':
        num = 40
    elif player == 'yellow':
        num = 14
    else:
        num = 27
    row,column = start_coordinate(player)
    locations[player][piece_number] = num
    make_button(row,column,player, piece_index, dice_roll, piece_number, img)
    if piece_number == 0:
        homes0[player] = False
    fill_home(player,piece_number)

def check_move(player,piece_index):
    x=True
    for i in locations[player]:
        if i == piece_index:
            x=False
        else:
            ()
    for color in locations:
        for j in locations[color]:
            for space in safe_spaces:
                if j == space:
                    x=False
    if piece_index == 1:
        for i in locations['green']:
            if i ==1:
                x=False
            else:
                ()
    elif piece_index == 14:
        for i in locations['yellow']:
            if i ==14:
                x=False
            else:
                ()
    elif piece_index == 27:
        for i in locations['blue']:
            if i ==27:
                x=False
            else:
                ()
    elif piece_index == 40:
        for i in locations['red']:
            if i ==40:
                x=False
            else:
                ()
    return x

def scoreboard():
    num = 0
    for i in scores:
        label1 = tk.Label(game_window, image = home_squares[i], height=47, width=47)
        label1.grid(row = 5+num, column = 15)
        label1 = tk.Label(game_window,text = scores[i], height=3, width=3)
        label1.grid(row = 5+num, column = 16)
        num+=1

def score(player):
    scores[player]+=1
    scoreboard()

def move(player, piece_index, dice_roll, piece_number, img):
    try:
        orow,ocol = coordinates(piece_index)
    except TypeError:
        piece_index = piece_index-52
        orow,ocol = coordinates(piece_index)
    new_index = piece_index+roll[0]
    new_index = near_base(player,new_index) 
    try:
        nrow,ncol = coordinates(new_index)
    except TypeError:
        print('wrap around')
        new_index-=52
        nrow,ncol = coordinates(new_index)
    can_move = check_move(player,new_index)
    moveable,endspace = in_base(player,new_index)
    if can_move and moveable:
        if endspace:
            label1 = tk.Label(game_window, image = bg_images[background[orow][ocol]], height=50, width=50)
            label1.grid(row = orow, column = ocol)
            score(player)
        else:
            locations[player][piece_number] = new_index    
            capture(player,new_index)
            make_button(nrow,ncol,player,new_index,dice_roll,piece_number,img)
            label1 = tk.Label(game_window, image = bg_images[background[orow][ocol]], height=50, width=50)
            label1.grid(row = orow, column = ocol)
    else:
        ()

def capture(player,piece_index):
    for players in locations:
        for i in range(4):
            if players == player:
                ()
            else:
                if piece_index == locations[players][i]:
                    return_home(players,i)
                    captured[0] = True
                    if i == 0:
                        homes0[players] = True
                    
def return_home(player,piece_number):
    if player == 'green':
        row = 2
        column = 2
    elif player == 'yellow':
        row = 2
        column = 11
    elif player =='red':
        row = 11
        column = 2
    elif player =='blue':
        row = 11
        column =11
    row+= (piece_number//2)
    column+= (piece_number%2)
    piece_index = -1*piece_number
    locations[player] = piece_index
    dice_roll = roll[0]
    img = colors[player]
    make_button(row,column,player, piece_index, dice_roll, piece_number, img)
    

##Generates a new button based on the location
def make_button(row1,column1,player, piece_index, dice_roll, piece_number, img):
    piece = tk.Button(game_window, image = img, command=lambda: move_circle(player,locations[player][piece_number], roll[0], piece_number, img), height=47, width=47)
    piece.grid(row = row1, column = column1)

def six():
    six_in_row[0]+=1
    if six_in_row[0] == 3:
        next_turn()
    else:
        ()



def near_base(player,piece_index):
    if player == 'green':
        if 52<=piece_index<=70:
            return 100+(piece_index-52)
        else:
            return piece_index
    elif player =='yellow':
        if piece_index-roll[0]<=12 and piece_index>12:
            return 200+(piece_index-13)
        else:
            return piece_index
    elif player == 'blue':
        if piece_index-roll[0]<=25 and piece_index>25:
            return 300+(piece_index-26)
        else:
            return piece_index
    elif player == 'red':
        if piece_index-roll[0]<=38 and piece_index>38:
            return 400+(piece_index-39)
        else:
            return piece_index
    else:
        return piece_index

def in_base(player,piece_index):
    if piece_index <100:
        return True,False
    else:
        if player == 'green':
            num = 105
        elif player == 'yellow':
            num = 205
        elif player == 'blue':
            num = 305
        elif player == 'red':
            num = 405
        if piece_index<num:
            return True,False
        if piece_index == num:
            return True,True
        else:
            return False,False
              
    
## performs the logic of moving a piece
def move_circle(player, piece_index, dice_roll, piece_number, img):
    if player != turn_order[turn[0]]:
        print('out of order')
    elif new_roll[0]:
        if check_home(player,piece_index):
            if dice_roll == 6 and check_start(player):
                leave_home(player, piece_index, dice_roll, piece_number, img)
                six()
            else:
                print('no move')
                next_turn()
        else:
            move(player, piece_index, dice_roll, piece_number, img)
            if roll[0] ==6:
                six()
            elif captured[0]:
                captured[0] = False
            else:
                next_turn()
        new_roll[0] = False

def save_game():
    save_file = open('Ludo_save_file.txt','w')
    for color in locations:
        for i in range(4):
            save_file.write(f'{locations[color][i]},')
        save_file.write('\n')
    for i in turn_order:
        save_file.write(f'{i},')
    save_file.write('\n')
    for color in homes0:
        if homes0[color]: 
            save_file.write(f'{homes0[color]},')
        else:
            save_file.write(',')
    save_file.write('\n')
    for color in scores:
        save_file.write(f'{scores[color]},')
    save_file.write('\n')
    save_file.write(f'{turn[0]}\n')
    save_file.write(f'{roll[0]}\n')
    save_file.write(f'{six_in_row[0]}\n')
    if captured[0]:
        save_file.write(f'{captured[0]}\n')
    else:
        save_file.write('\n')
    if new_roll[0]:
        save_file.write(f'{new_roll[0]}\n')
    else:
        save_file.write('\n')
    save_file.close()
    print('game saved')
    game_window.destroy()
    
################################## starts menu (backbone)  ###################################



play = tk.Button(game_window, text = 'Play', command = lambda: start(), height=5, width=40)
play.grid(row = 1, column = 1)
rules = tk.Button(game_window, text = 'Rules', command=lambda: rules1(), height=5, width=40)
rules.grid(row = 2, column = 1)
instructions = tk.Button(game_window, text = 'Instructions', command=lambda: show_instructions(), height=5, width=40)
instructions.grid(row = 3, column = 1)
load_game1 = tk.Button(game_window, text = 'Load Game', command=lambda: load_game(), height=5, width=40)
load_game1.grid(row = 4, column = 1)

game_window.mainloop()
################### Import Images #########################
 

