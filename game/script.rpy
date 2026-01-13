# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#character names
define a = Character("Amie")
define c = Character("Callista")
define d = Character("Doctor")
define l = Character("Lilith")




#character images
image callista = im.Scale("callista.png",1000,1000)
image amie = im.Scale("amie.png",1000,1000)
image lilith = im.Scale("fairy.png",1000,1000)



#background images
image bg library = im.Scale("library.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg hospital = im.Scale("hospital.png",1920,1080)
image bg bedroom = im.Scale("bedroom.png",1920,1080)
image bg schoolOut = im.Scale("schoolOut.png",1920,1080)
image bg sidewalk = im.Scale("sidewalk.png",1920,1080)

#phone images
image phone = im.Scale("phone.png",960,1080)


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
    c "..."#make this an option
    a "The library is almost closed you know"
    c"..."#make this an option
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
    hide callista with moveoutright
    hide bg hospital
    show bg bedroom
    show callista at right
    c"{i}Gosh I lost so much time just coming back from the hospital{/i}"
    c"{i}Who even brought me to the hospital? I'll have to thank them{/i}"
    narrator "Callista brushed off the though and tied up her hair, preparing to study late into the night"
    narrator "She glanced over to the corner her desk that had the medicine she had been perscribed."
    narrator "She uncapped it and took a dose of it before she began her studies"
    hide callista
    show bg empty
    narrator"Time: 6.30 am"
    show bg bedroom
    show callista at left
    narrator "Opening her eyes slowly, Callista saw a small little fairy in front of her eyes. The sight shocking enough for her to jolt back"
    c "AGHHH WHAT THE HECK"
    show lilith at right
    l "Hellooo"
    narrator "She had an overly sweet voice if you could it hear over Callista's attempts to shoo away the creature with a pillow"
    c "What are you!"
    l"If you stopped for a minute you would see that I am a fairy"
    narrator "That had Callista cease her attacks and reach out in front of her, squeezing the little creature"
    c "I must be hallucinating"
    l"Hey! Hey! That hurts"
    narrator"Callista let go of the fairy"
    l"Darn, that really hurt. You know I'm here to help you"
    c"Help me? Help me with what?"
    narrator"The fairy rolled her eyes as if the answer was obvious"
    l"Helping you HAVE a life"
    c"That is absolute-"
    l"ssshhhhhhhhhhhhh"
    l"I know {w}I'm too kind"
    narrator"Callista looked at the fairy incredulously"
    l"From today on, I have arranged after-school plans for you. Hangouts, clubs,encounters and any other things of the like"
    c "What if I just refuse?"
    l"The there will be consequences"
    narrator"Callista checks  the time and shakes her head"
    c"It's too early, I'm probably hallucinating"
    narrator"The fairy pulls her out of bed"
    l"Oh no you don't. You have a whole day ahead of you to stay energized for"
    narrator "Callista left the house with a fairy yapping annoyingly at her ear of which she tried to ignore"
    jump day_1

label day_1:
    show bg sidewalk
    show callista at right
    narrator"As she walks down the street she gets a text from Amie"
    #text showing about the club fair
    show phone
    c"Club fair?"
    hide phone
    c"I thought clubs were finalized for the year"
    show lilith at left
    l"Yes, but you only joined book club"
    narrator"Callista swats off Lilith"
    c"What does my scheduale matter to you, bug"
    l"Ugh! I am not a bug. And your scheduale matters to me because I am trying to help you get out more"
    c"I'm already in book club"
    narrator"Liltih rolls her eyes"
    c"We only have to meet once a month and I get a free book out of it too"
    hide lilith
    show bg front
    #noises
    narrator"Lilith was trying to pass by, not planning to join a new clubs, but her new companion has other plans"
    show lilith with moveinleft
    l"Ok so here are the BEST clubs for you to join with how would"
    

    
