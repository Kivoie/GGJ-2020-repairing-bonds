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

$ lol = int(0)

jump start # must be included at the beginning. we can skip anything inbetween


########################## The game starts here. ##########################

label lol:

    # Show a background. This uses a placeholder by default, but you can
    # add a file (named either "bg room.png" or "bg room.jpg") to the
    # images directory to show it.

    #scene glass
    
    # Variables are denoted using a dollar sign ($) prefix before the variable name
    
    # $ username = renpy.input("Hey there. What's your name?")
    # $ username = username.strip()
    
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


label start:
    
    $ username = "You"
    $ points = 0
    $ nameFlag = True
    
    "It’s been 4 years since I graduated from high school, or something like that."
    "My experiences within that time had been amazing. Meeting new people from different fields and talking about our likes and differences."
    "But those new friends you’ve made don’t seem all that close to you compared to the ones you’ve made as kids"
    "Sure we have common interests, but..."
    You "\"Yeah, let’s talk again sometime!\""
    "Those were the last words I said to him."
    "During high school, I had a best friend I always hung out with."
    "We would talk about anything and everything, from the global news to the latest trends in video games."
    "There weren’t many dull moments in high school. You could say that it was quite a time to be alive."
    "When we graduated from high school, I went to a college on the other side of the country while he stayed local."
    "We kept in contact for a while, but we were getting busy with school and our college friend groups."
    "Communication between us gradually slowed down. From once a week to once every few months."
    "Eventually we stopped talking altogether. His name became foreign to me."
    "Life carried on. I continued my studies and I hung out with my college friends every now and then."
    "Is this really the same as living in the past?"
    "Of course it isn’t. These are people who I’m not familiar with besides their hair color and their brief political interests."
    "Aware of their \"now\"; knowing little of their past."
    "They’re not the same as my other friends."
    "I’d lose all the friends I’ve made in the past few years if I told them how I really feel."
    "Should I? Of course not. I have enough problems as it is."
    "The last time he texted me was 5 months ago, when he asked me who I’d vote for in the up-coming election."
    "Clearly under the influence given his message contents."
    "Drugs or not, it’s great hearing from him."
    You "Shit. It’s 23:00 already and I’ve hardly gotten anything done..."
    "Maybe I should text him."
    You "No, that’d be stupid. He’s probably busy with his new job as a tour guide at that automotive factory."
    "It’s hard to believe a knucklehead like him can even get a job that requires so much interaction with people."
    "But social media doesn’t lie. Otherwise he’d just have fooled all those 86 people who Liked his milestone update."
    "I’m happy for him, I really am. But how am I supposed to express it?"
    "With words? Virtually?"
    "The distance between us has increased, physically and figuratively."
    "Messaging him just out of the blue would just seem awkward."
    You "Is this really something I should be worrying about...? My first midterms are just a week away and I’m thinking about dumb shit like this..."
    You "I should really get back to studying..."
    "...*buzz*...*buzz*..."
    You "A text?"
    "Unfortunate. Another Qwitter notification."
    You "Hmm...? ... ... Oh... ... This... can’t be true..."
    You "... Hospitalized...?"
    
    scene elevators
    with blinds

    "Shit happens."
    "The text I received a week ago was regarding him."
    "Would it seem rude to contact him? We’re practically strangers now."
    You "No, showing concern is the right thing to do."
    "Right?"
    "If I contact him just because he got into an accident... what if..."
    "What if he doesn’t want to talk to me anymore? Does he even remember my name? Face? My favorite BonsterCat song that I keep changing every half month?"
    "Should I?"

    menu:               # point 1
        "Text him":
            $ points = points + 1
            You "\"Hey, I heard about what happened. Are you all right? Will you be able to walk again? How long will you stay in the hospital? Is your car totaled? Was it your fault?\""
            "Sweat begins to drip down from my forehead as I tap the send button with my shaking thumb."
            "Now that I think about it..."
            You "Crap, that sounds pretty insensitive..."
            "Not even a minute later after I sent my barrage of nearly-incomprehensible verbal diarrhea, I receive a reply."
            "To my disbelief, it was him who texted me back. Me of all people..."

            "\"thx so much for asking.. i’m in th ehospital rn i’m fine now but my car is completely totaled, i only bought it like 3 weeks ago too haha..\""
            while nameFlag is True:
                $ username = renpy.input("\"oh btw who is this?? i got a new phone recently..\"")
                $ username = username.strip()
                if not username:
                    $ nameFlag = True
                else:
                    $ nameFlag = False
            Him "\"Oh [username] it’s been a while lol..\""
        "Don’t text him":
            You "No. Texting him right now would be pretty insensitive. He’s probably all right and kicking."
            "...*buzz*...*buzz*..."
            You "A text?"
            You "It’s... from him...?"
            Him "Hey steve i don’t htink i can come to work for the next fe w weeks because i got into a pretty bad car crash."
            "\"...Steve? Work? He must have gotten the wrong number...\""
            You "I should let him know."
            "\"Hey, I think you got the wrong number, it’s not Steve.\""
            "..."
            "...*buzz*...*buzz*..."
            while nameFlag True:
                $ username = renpy.input("\"oh wat. sorry who is this..?\"")
                $ username = username.strip()
                if not username:
                    $ nameFlag = True
                else:
                    $ nameFlag = False
            Him "\"oh [username] it’s been a while lol..\""
            Him "\"sorry about that haha i guess i selected the wrong numbr or somethn.. \""
            
    Him "\"so hows it going? we havent talkd much lately..\""
        
    menu:               # point 2
        "(Talk about car crash)":
            $ points = points + 1
            You "\"So, how bad was the crash?\""
            Him "\"the docs say i will get discharged in abot a month or somethn\""
            Him "\"honestly it doesn't sound as bad as it was\""
            "That's a relief."
            You "\"Thank god you're all right.\""
        "(Talk about life)":
            You "\"How are you liking it at your new tour guide job?\""
            Him "\"its not bad, i do have to talk with a lot of ppl tho lol\""
            Him "\"but i wont be able to work for a while tho cuz the crash\""

    Him "\"i got a gf last week btw\""
    Him "\"thank god she wasnt in the car during the crsh\""
    
    menu:               # point 3
        "(Congratulate him)":
            $ points = points + 1
            You "\"Wait really?? Congrats! What's she like??\""
            Him "\"she's kinda nice i guess, but we'll see haha\""
        "\"Nice\"":
            Him "\"yea ikr\""
            
    Him "\"oh btw did u get to watch that show i recommnd u last year??\""
    
    menu:               # point 4
        "Yeah I did. It was great!":
            Him "\"yea i didn't really like it.. but glad u did tho..\""
        "Yeah I did. It was kinda shit...":
            $ points = points + 1
            Him "\"lol ikr??? i thought so to. the end sucked so much loool\""
    
    Him "\"oh btw hows ur family doin? with u bein away and all\""
    
    menu:               # point 5
        "They're doing great!":
            $ points = points + 1
            You "\"They're doing great!\""
            You "\"They're happy that I'm getting good grades too.\""
            You "\"I'm happy that they're being really supportive of me and my career choice.\""
        "Not bad.":
            You "\"They're not bad. I haven't seen them in a while though...\""
            Him "\"thats good to heer..\""
    
    
    
    
    
    
    
    You "\"Hey listen, I'm coming back to town for my first work term. Wanna hang out?\""
    
    if points == 5:
        Him "\"Yea for sur lets hang out when u get here\""
        You "\"Yeah, I'm looking forward to that! I hope you get better soon!\""
        "{b}Congratulations, you've managed to fix your relationship with your friend. Now it's up to you to strengthen that!{/b}"
        scene black
        with Fade(5, 1, 0)
    else:
        Him "\"prob not, i'm kinda busy. but maybe anothr time tho\""
        You "\"All right, may some other time then...\""
        "{b}You didn't score enough points to fix your relationship with your friend. Better luck next time...{/b}"
        scene black
        with Fade(5, 1, 0)

    "{b}Thank you for playing! Developed by Danny Vuong and David Liu. #GlobalGameJam2020{/b}"


    return