# Copyright (C) 2020 Carleton University. No part of
# this file may be reproduced, in any form or by any
# other means, without permission in writing from
# the university.

# The script of the game goes in this file.
# Imports go here


# Declare characters used by this game. The color argument colorizes the
# name of the character.

define You = Character("[username]")
define Him = Character("Him")

# Variable space

$ nameFlag = True
$ points = int(1)
$ lol = int(0)

jump start # must be included at the beginning. we can skip anything inbetween


########################## The game starts here. ##########################

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene glass
    
    # Variables are denoted using a dollar sign ($) prefix before the variable name
    
    $ username = renpy.input("Hey there. What's your name?")
    $ username = username.strip()
    
    if not username:
        $ username = "You"

    # Calling variables are denoted by square brackets ([])
    
    "Hi there, [username]!"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    # These display lines of dialogue.

    You "Welcome"

    You "Placeholder name"
    
    "Here is a menu"
    
    menu:
        "Option 1":
            You "I have chosen option 1"
            $ lol = int(1)
        "Option 2":
            You "I have chosen option 2"
            $ lol = int(2)
        "Option 3":
            You "I have chosen option 3"
            $ lol = int(3)
            

    "Your total score is [lol]."
    
    

    "Game end"
    
    # This ends the game.

    return