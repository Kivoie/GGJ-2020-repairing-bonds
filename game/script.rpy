# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

define u = Character("[mchar]")


# The game starts here.

label start:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    scene bg room
    $ mchar = renpy.input("What's your name, doc?")     #TODO
    $ mchar = mchar.strip()
    
    if not mchar:
        $ mchar = "Doctor"      #TODO
    
    u "Hi there, [mchar]"

    # This shows a character sprite. A placeholder is used, but you can
    # replace it by adding a file named "eileen happy.png" to the images
    # directory.

    show eileen happy           #TODO

    # These display lines of dialogue.

    u "Welcome"

    u "Better minds"
    
    "Here is a menu"
    
    menu:
        "Option 1":
            u "You have chosen option 1"
        "Option 2":
            u "You have chosen option 2"
        "Option 3":
            u "You have chosen option 3"

    "Game end"
    
    # This ends the game.

    return