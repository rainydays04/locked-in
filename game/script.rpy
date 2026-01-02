# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#character names
define a = Character("Amie")
define c = Character("Callista")
define d = Character("Doctor")


#character images
image callista = im.Scale("callista.png",1000,1000)
image amie = im.Scale("amie.png",1000,1000)

#background images
image bg library = im.Scale("library.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg hospital = im.Scale("hospital.png",1920,1080)


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
    hide amie with moveoutleft
    c "{i}ugh... I'm getting dizzy{/i}"
    c "I can...sit up... longer-"
    hide callista
    #have like a fading animation?
    show bg empty
    show bg hospital
    show callista 
    c"{i}Where am I?{/i}"
    d "Oh good, you're awake"
    d "How are you feeling?"
    c"Fatigued"
    c"What happened?"
    d"You were found passed out by one of the librarians at the library"
    narrator "Panic settled in on Callista's face"
    c "How long was I out for?"
    d"Around two hours"
    narrator "Frantic, Callista began to quickly gather her things. Grabbing her school bag and slipping on her shoes"
    c "Thank you for your time, doc. Is there any medicine you perscribe?"
    narrator "The doctor gently blocked Callista's path"
    d "I think you should take some rest"
    narrator "Callista looked at the doctor and shook her head"
    c "I took about enough breaks, thank you though-"
    narrator "The doctor searched her eyes and gave a reluctant sigh, pinching the bridge of his eyes"
    d "I know several teachers have come up to you about this, so I won't try"
    narrator "The doctor hands her some liquid medicine"
    d "Use this to help with your heart"
    narrator "Callista nodded and took the medicine from the doctor before leaving the door"
    hide bg hospital
    show bg 
    


    

    return
