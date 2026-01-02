# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#character names
define a = Character("Amie")
define c = Character("Callista")


#character images
image callista = im.Scale("callista.png",1000,1000)
image amie = im.Scale("amie.png",1000,1000)

#background images
image bg library = im.Scale("library.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)


default score=0

# The game starts here.

label start:
    show bg empty
    narrator "The world values prestige"
    narrator "This world asks for those who can work endlessly"
    narrator "Anything in between is a waste, a distraction"
    c "At least that's what my mom has always told me"
    show bg library
    show callista at right
    show amie at left
    a "Are you still studying?"
    c "..."
    a "The library is almost closed you know"
    c"..."
    a "We were going out to get some drinks-"
    c "I'll pass"
    a "alright then"
    show amie moveoutright#im pretty sure this code is wrong
    c "{i}ugh... I'm getting dizzy{/i}"
    c "I can...sit up... longer-"
    hide callista
    show bg empty

    

    return
