# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.


#character names
define a = Character("Amie")
define c = Character("Callista")
define d = Character("Doctor")
define l = Character("Lilith")
define g = Character("Grace")
define h = Character("Hannah")
define an = Characyer("Andreas")


#audio
define audio.schoolBell="schoolBell.mp3"

#character images
image callista = im.Scale("callista.png",1000,1000)
image amie = im.Scale("amie.png",1000,1000)
image lilith = im.Scale("fairy.png",500,500)
image grace = im.Scale("grace.png",1000,1000)
image hannah = im.Scale("hannah.png",1000,1000)
image andreas = im.Scale("andreas.png",1000,1000)
image jason = im.Scale("jason.png",1000,1000)
image twogirls = im.Scale("twogirls.png",1000,1000)



#background images
image bg library = im.Scale("library.png",1920,1080)
image bg empty = im.Scale("empty.png",1920,1080)
image bg hospital = im.Scale("hospital.png",1920,1080)
image bg bedroom = im.Scale("bedroom.png",1920,1080)
image bg schoolOut = im.Scale("schoolOut.png",1920,1080)
image bg sidewalk = im.Scale("sidewalk.png",1920,1080)
image bg front = im.Scale("front.png",1920,1080)
image bg classroom = im.Scale("classroom.png",1920,1080)
image bg computerRoom = im.Scale("computer.png",1920,1080)
image bg newspaper = im.Scale("newspaper.png",1920,1080)
image bg hallway = im.Scale("hallway.png",1920,1080)
image bg gardening = im.Scale("gardening.png",1920,1080)
#phone images
image phone = im.Scale("phone.png",960,1080)


default score=0
default club="none"
default thing="none"


#alignment for lilith
transform topright:
    xalign 1.0 yalign 0.0
transform topleft:
    xalign 1.0 yalign 0.0
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
    show lilith at topright
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
    show lilith at topleft
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
    narrator"The fairy shows three flyers: Robotics, Newpaper, and Gardening"
    narrator"Callista looked incredulously"
    c"And I have to choose one of these?"
    l"You wanna find out happens if you don't abide?"
    menu:
        "Yes":
            c"Try me"
            narrator"Lilith covered Callista in sticky glitter"
            c"PEH! What in the world?"
            narrator"Several heads turned to stare at Callista"
            c"Please, remove it"
            l"Choose a club then"
        "No":
            c"I'd rather you just tell me"
            narrator"Lilith rolled her eyes almost as if she was disappointed"
            l"Well you would you enjoy having glitter stuck to you for 30 minutes to 3 hours"
            c"NO!"
            narrator"Several heads turned to stare at Callista to which she hid her face behind her hand"
            c"Fine, I'll choose a stupid club"
    menu:
        "Robotics":
            $ club=="robotics"
            c"I'll join the robotics club"
            l"Great! Let me show you where the club table is"
        "Gardening":
            $ club=="gardening"
            c"I guess I'll join the gardening club"
            l"Ooo getting some vitamin d, I see. I think the club table is around the back"
        "Newspaper":
            $ club=="newspaper"
            c"The newspaper club seems fun I guess"
            l"Makes sense, The club table is over there"
    narrator"Lilith led Callista around the tables, trying to lead her to the club table, but she bumped into Amie"
    show callista at right
    show amie at left
    hide lilith
    a"Callista! You're already up, I expected you to take a bit off today after-"
    c"I'm fine, besides, I have work to do"
    a"Are you heading to the library again?"
    c"No, I am actually joining a club"
    narrator "Amie looked at her in suprise, a smile creeping onto her face"
    a"Really? Not just like bookclub or something"
    narrator"Callista shook her head"
    a"That's... That's great Callista. Do you need me to help you find the table"
    narrator"Callista looked around, trying to find Lilith, but she was no where to be found, so she accepted her friends's offer"
    hide amie
    hide callista
    show bg empty with fade
    narrator"After signing up for her clubs, the two parted ways to go to their classrooms"
    show bg classroom with fade
    show callista at right
    narrator"Callista was in the accelerated class, seperated from her only friend"
    narrator"She hasn't made much of an effort to talk to others"
    show lilith at topleft
    narrator"Lilith peeked out of Callista's bag while her classmates were chattering about the clubs they signed up for"
    l"You should try talking to them"
    c"And who are you again to determine my social life?"
    l"Forgot my name already?"
    c"When you pulled that disappearing act on me earlier to something YOU dragged me into"
    l"Aww so you care about me?"
    menu:
        "Yeah well...":
            c"Well you seem to be attachde to me for some reason and I don't want to anger whatever sent you down"
        "No":
            c"Who are you again? I seem to suffering from amnesia"
    narrator"Lilith rolled her eyes and flew about the classroom, scanning and listening to what her classmates were talking about"
    hide lilith with moveoutleft
    c"H-hey, get back here"
    narrator"Callista's soft cries brought on the attention of her seatmate"
    c"{i}Is she looking at me?{/i}"
    show callista at right
    show grace at left with moveinleft
    g"Sorry, I just so rarely hear your voice, your head is always in your books and -"
    narrator"Just hearing her talk was enough to make her head spin"
    c"Yeah I just wanted to catch up on my classes"
    g"Catch up? Gosh everyone is so lost in their heads"
    g"Giving more and more of themselves and less time for themselves"
    narrator"She lets out a wistful sigh"
    c"Well, what would you do?"
    narrator"She paused to give it some thought"
    g"We're upperclassmen now, we have sooo many upperclassmen privileges"
    g"Like uhh... leaving school early! Everyone in this class uses it as an extra study period or clubs while everyone else goes out"
    g"Besides,"
    g"If anyone should be worrying, it isn't you"
    narrator"It has always annoyed Callista when people only saw her results, not her."
    narrator"Even if she didn't get a good results people still halo effected her, like a loop of misunderstanding"
    c"I got other stuff"
    g"R-right! Oh, sorry I didn't mean to assume that you didn't have like other stuff going on"
    g"Uhh, uh... So like, what are your hobbies?"
    c"I-"
    g"OMG wait no, I see you like always in the library. You've been reading much"
    menu:
        "Fantasy":
                c"I like to escape every once in a while with a good fantasy books"
                narrator"She looks up thoughtfully"
                c"The princesses, the fights, the duals. They all are for something and have some kinda meaning"
                g"...W-wow"
                g"That's like..super deep"
                c"Oh? I guess, but it's just what fantasy is for I guess"
        "Romance":
            c"Romance novels have always been of interest to me"
            g"Ooo la la"
            c"Hah..Yeah, swoony I know"
            c"I think I was about 12 when I stumbled upon them in my sister's bedroom"
            narrator"Callista's eyes gain a faraway look"
            c"She used to spend her weekends in her reading nook, giggling at her books"
            g"Aww, that's sooo sweet"
        "Sci-Fi":
            c"I have gotten piles and piles of Science-Fiction books"
            c"I was researchng quantum physics for one class and I stumbled upon a good novel which led me down a rabbit hole"
            g"Science-fiction you say? I'm going to a movie with that genre..uhh The Humanix?"
            c"I love that book! I have a copy all worn out and bookmarked"
            g"Maybe we could go together?"
            menu:
                "Sure why not":
                    c"Sounds fun"
                    narrator"The girl scribbles something down on a peice of paper and passes it to Callista"
                    g"Here's my number. Oh, my name is Grace by the way"
                    c"Callista"
                "Oh I don't think...":
                    c"Sorry, I dont think I can make-"
                    narrator"A sudden poof of glitter covers Callista"
                    c"Actually uh, yeah sounds great"
                    narrator"The glitter disappears and the girl scribbles something down on a peice of paper and passes it to Callista"
                    g"Here's my number. Oh, my name is Grace by the way"
                    c"Callista"
    hide grace
    hide callista
    play music schoolBell
    show bg empty with fade
    show bg classroom with fade
    show callista at right
    narrator"As Callista writes her notes, Lilith crawls out of her school bag"
    show lilith with move in left at topleft
    l"Seems like that went very well"
    narrator"Callista loks around to see if anyone else see the little annoying fairy on her desl"
    l"Tsk tsk"
    l"No one but you can see and hear me"
    c"Oh so you're just a figment of my imagination"
    l"If I say yes, would you get at minimum 8 hours of sleep to get rid of me?"
    menu:
        "You're a nightmare":
            c"Sleep would just induce nightmares of you"
            l"Oh so you would dream of me? How sweet and so soon"
        "That wouldn't work":
            c"I think I tried enough things to know that wouldn't work"
            l"So quick to give up"
    narrator"Lilith streches and yawns"
    l"You should go to the club meetings today"
    c"But they aren't until next week"
    l"Glitter?"
    narrator"Callista tightens her hold around her pencil, biting her lower lip"
    c"Fine"
    narrator"Lilith smiles with satisfaction and climbs into Callista's bag to continue her nap"
    hide callista
    hide lilith
    show bg empty with fade
    if club=="robotics":
        jump robotics_day1
    elif club=="newspaper":
        jump newspaper_day1
    else:
        jump gardening_day1
    return

label robotics_day1:
    show bg computerRoom
    show hannah at left
    narrator"The room was hidden somewhere on the second floor and there were only a handful members when she entered"
    narrator"The club leader, Hannah, was alone at a table surrounded by parts, screws, and laptops"
    narrator"On the other end of the table was a small group of students writing away in their notebooks"
    menu:
        "Looks a bit rough in here":
            h"Oh so your the new member, here let me just set up a computer for you"
            narrator"Hannah grabs a laptop and begins setting it up, ignoring Callista"
        "Hi I'm Callista":
            narrator"...No one responds"
            menu:
        "Anything I can do to help around here?":
            c"Could I help out with anything?"
            h"No no I got it"
            narrator"Hannah doesn't even look up and then she realized she needs to set up a laptop for Callista"
            h"Take a seat, I'll get this set up for you"
    narrator"Lilith murmurs from Callista's bag"
    l"Talk about controlling, maybe I should send one over for her"
    narrator"The statement made Callista curious as to what she meant, but she didn't speak out loud due to their company"
    menu:
        "Sit with Hannah":
            narrator"Callista took the seat near Hannah"
            menu:
            "Offer help":
                c"Seriously I'd love to help with anything really"
                h"It's fine, really fine, I'll get this set up for you soon"
                narrator"Callista is suprised at her outburst and a tad bit concerned too, but just sits back next to Hannah quietly"
                narrator"Hannah sets up a computer in front of Callista and begins teachering her the basics of the program"
                narrator"Meanwhile the other members join them at the table to start working"
                h"We are currently preparing for a showcase and then a copetition later on, so I'll help you keep up to pace with the rest of the team"
                show lilith with moveinleft at topleft 
                l"Doesn't look like they are working on whatever she said"
                narrator"Nothing else was said as they all continued working in silence, Hannah's soft voice filling the room"
            "Ask about the club"
                c"So what are you guys working on right now?"
                narrator"Hannah doesn't take her eyes off the screen as she types away at the computer"
                h"We are uh... preparing for a showcase and then like a competition against other school"
                c"Oh cool, what did you guys do last semester?"
                narrator"Hannah paused and looked up at her, clearing her throat"
                h"Well um... Nothing really, we just presented some battle bots"
                c"Oh, I see"
                narrator"Hannah turned the computer to Callista and began teaching her the program"
                narrator"The other members filed over to work on their computers, none of them seemed to be working towards Hannah's itinerary though"
            "Grab one of the computers":
                narrator"Callista grabbed one of the computers that was in front of her with a video game project"
                c"{i}Strange, thought this was a robotics club{/i}"
                c"What is this?"
                narrator"Hannah glanced over at the screen and let out a sigh"
                h"Nothing, we should all be working on our projects for competitions and showcases right now"
                narrator"She takes the computer bag and opens up a different software, the other members filed over to work on their computers, none of them seemed to be working towards Hannah's itinerary though"
                narrator"Nothing else was said as they all continued working in silence, Hannah's soft voice filling the room"
        "Sit with the other team members":
            narrator"Callista sat with the other members, pulling up a chair"
            c"So, whatcha guys doing?"
            narrator"{i}Team member 1{/i}: Some video games"
            narrator"{i}Team member 2{/i}: Yeah, we're planning something for our next project, but its on one of the computers Hannah is setting up"
            c"What's the project?"
            narrator"They all put a halt what they were doing and begin explaining each of their different projects"
            c"Wow, these ideas seem so cool"
            c"How come I've never seen your projects in the school newspaper? Its always competitions and showcases"
            narrator"{i}Team member 1{/i}: Ugh, Hannah is insistent on these competitions and showcases"
            narrator"{i}Team member 3{/i}: We can't really go against her since she gives us access to the computers"
            narrator"They hold up their notebooks"
            narrator"As they look up and see that Hannah has finished setting up the table with their computers"
            narrator"They all walk towards the tables and whisper something about ignoring Hannah's instructions and working on their latest project"
            narrator"Hannah turned the computer to Callista and began teaching her the program"
            narrator"Nothing else was said as they all continued working in silence, Hannah's voice the only noise in the room"
    narrator"The rest of the club followed in the same manner until the clock hit 5 o'clock"
    hide hannah
    hide callista
    show bg empty with fade


label newspaper_day1:
    show bg hallway
    show callista at left
    show lilith at topright
    l"This is one of THE best clubs to get into, I'm telling you"
    l"It's on the same floor as the teacher's lounge, so all the students get snacks from there"
    l"And it has the biggest club room"
    c"Just because it's bigger does not make it a good club"
    show bg newspaper
    hide lilith with moveoutleft
    narrator"There were about 12 students in attendence, most of them working on their papers and laptops"
    narrator"At the front of the room was Andreas, talking to 2 seemingly new members"
    narrator"Callista walked up to join them, Andreas' face lightening up seeing her"
    show andreas with moveinright at right
    an"Hi!, you must be Callista. I saw your name on the list and was so glad to see you there"
    an"I'm Andreas, and I coordinate the Newspaper Club"
    c"Nice to meet you, I'm excited to get started"
    an"Well you don't have to wait to soon"
    narrator"He points to the board where it has 3 groups written on it"
    an"I can put each of you in one of these sections."
    an"Section editors are allowed to basically write about any news topic so long as they do thorough research on it"
    an"Reporters focus on writing about what's happening, school events and things of the like"
    an"And lastly photography, which is going out and taking photos for school events, or maybe even compile photos you just want to share"
    menu:
        "Section Editors":
            c"I could be section editor, I like doing research"
            narrator"Andreas smiles and wrote her name on the board next to the other section editors"
            #glitter her
        "Reporters":
            narrator"After considering it for a while, she decieded to step out of her comfort zone"
            c"I could be a reporter"
            an"Excellent, I'll give you my number since I especially like to write or helpn with that section"
            an"It also might be tough for newcomers"
            c"I appreiciate it"
        "Photographers":
            c"I could be a photographer, albeit, I don't have much experience"
            an"No worries, everything is a learning process"
            narrator"He says with a toothy grin"
            an"Here you even have your own camera provided by the school"
            narrator"Andreas hands over a camera bag to her"
            an"Keep it safe alright?"
            c"Noted"
    hide andreas with moveoutright
    c"{i}He is quite talkative. Must be good when leading the club{/i}"
    narrator"Callista spent the rest of the club period talking to the other club members and enjoying snacks"
    hide callista
    show bg empty with fade

    
    narrator"After clubs, Callista grabbed a the latest newspaper the club had published"
    show bg hallway
    show callista with moveinleft at left
    c"Wow this is really good"
    c"They have articles, sources, art, photography of sport and scenery around the town"
    show andreas with moveinleft at left
    an"I don't think that it's a good idea Miss. Hawkins"
    narrator"Callista hid behind a pillar to listen in, unable to hear the other voice"
    an"Yes I'm sure it would be useful, but I don't have the team to-"
    an"..."
    an "Yes,no of course. I understand. I think I'll be able to scrounge something up anyways"
    an"Sorry Miss.Hawkins, I'll look into adding that as a column in the newspaper next month"
    narrator"There were footsteps walking the other way and a soft groan from the adolescent from the other side of the pillar"
    an"It's fine, I can add it in if need be"
    hide andreas with moveoutright
    c"Damn, seems like he has a lot on his plate"
  

label gardening_day1:
    show bg gardening
    show callista at right
    narrator"The gardening club was behind the school, a few planting beds around"
    narrator"Jason was tending to some flowers, lost in his work, a few following suit"
    narrator"However, a majority of the members were occupied with doing nothing or playing around"
    menu:
        "Talk to the lazing students":
            narrator"As you approach the lazing students, you find that they have no interst in talking to you so you end up talking to Jason"
            show Jason with moveinleft at left 
            narrator"He looks up and brushed his hands on his legs"
            j"You must be Callista, I'm Jason, the club leader"
            narrator"He takes of his glove and shakes her hand"
            menu:
                "I've always foudn gardening calming":
                    c"I've always found gardening quite calming"
                    j"Yeah, calming"
                    narrator"Jason gains a bit of a faraway look before snapping back in the present"
                    j"Most people join this club to get away from school responsibilites"
                    j"Feel free to do whatever you want"
                    c"{i}Whatever I want? He means like...plant anything I want, right? {/i}"
                "Looks interesting":
                    c"I have always been interested in gardening, but I don't think I have much a green thumb"
                    j"Don't worry about it, you can really do what you like"
            narrator"Callista looks at hime confused at this idea from him"
            c"Are you sure you don't have any specific rules for where I'm suppose to plant stuff"
            narrator"Jason simply shrugs and shakes his head"
            narrator"He looks at the rest of the garden, Callista following his gaze"
            narrator"The garden looks dishevled, like beauty was put there and an evil spirit took it over"
            narrator"Two underclassmen girls are between the beds, picking dirt up and chucking it at each other"
            menu:
                "Tell them to stop":
                    hide callista with moveoutright
                    hide jason
                    show twogirls at right
                    show callista with moveinleft at left
                    c"Hey! Stop that"
                    narrator"The two girls halt their actions and stare at her"
                    narrator"{i}Girl 1{/i}: Why? Jason allows us to do it"
                    c"Jason might allow it, but I don't and mother nature surely doesnt either"
                    narrator"She started to slowly cleaned up the mess and tended to the garden with her limited knowledge"
                    c"You should be gentle with the garden, it could be beautiful you know"
                    narrator"The girls join in and follow silently mimic her movements and soon enough the area is cleaned up"
                    narrator"{i}Girl 2{/i}: That was kinda fun... We should try this next club time"
                    hide twogirls with moveoutleft
                    show jason with moveinleft at left
                    j"That was amazing, I haven't seen them actually interacting with the gardening like that"
                    j"You really didn't need to do that"
                    menu:
                        "Be gentle":
                            c"You seemed annoyed, I wanted to help out in anyway I can"
                            j"Thanks :)"
                        "Lwk yell at him":
                            c"No, I did have to. You have to"
                            narrator"She gets closer and points a finger at his him "
                            c"It is your responsibility"
                            j"Yeah, that's why I don't force the other members to do anyting"
                            narrator"Callista get upset at this"
                            c"You let them in your club, no? You are the leader, you shouldn't let them treat you like that and nonetheless the garden"
                            j"..."
                            c"Any instructions?"
                            j"..."
                            c"Fine"
                            hide callista with moveoutright
                            hide jason
                            show callista with moveinleft
                            narrator"She walked over to a bench under a tree and began reading, feeling Lilith's glitter be cast upon her"

                "Let them go":
                    narrator"She silently watches the girls playing arounf with the dirt"
                    narrator"Standing side by side, she could feel his unease, the clenching of his fists"
                    c"No gonna do anything"
                    j"mh.."
                    j"Just do whatever. No one cares as you can see"
                    hide jason with moveoutleft
                    c"I guess I'll just walk around then"
                    c"Oh...Hmm?"
                    narrator"She looks at a flower bed of purple chrysanthemums"
                    narrator"She gently strokes the flowers, barely perserved from other's destruction"
                    show lilith with moveinright at topleft
                    l"Here let me just"
                    #show flower in her hair
                    c"Thank you"
                    #tears
        "Talk to Jason":
            show Jason with moveinleft at left 
            narrator"He looks up and brushed his hands on his legs"
            j"You must be Callista, I'm Jason, the club leader"
            narrator"He takes of his glove and shakes her hand"
            menu:
                "I've always foudn gardening calming":
                    c"I've always found gardening quite calming"
                    j"Yeah, calming"
                    narrator"Jason gains a bit of a faraway look before snapping back in the present"
                    j"Most people join this club to get away from school responsibilites"
                    j"Feel free to do whatever you want"
                    c"{i}Whatever I want? He means like...plant anything I want, right? {/i}"
                "Looks interesting":
                    c"I have always been interested in gardening, but I don't think I have much a green thumb"
                    j"Don't worry about it, you can really do what you like"
            narrator"Callista looks at hime confused at this idea from him"
            c"Are you sure you don't have any specific rules for where I'm suppose to plant stuff"
            narrator"Jason simply shrugs and shakes his head"
            narrator"He looks at the rest of the garden, Callista following his gaze"
            narrator"The garden looks dishevled, like beauty was put there and an evil spirit took it over"
            narrator"Two underclassmen girls are between the beds, picking dirt up and chucking it at each other"
            menu:
                "Tell them to stop":
                    hide callista with moveoutright
                    hide jason
                    show twogirls at right
                    show callista with moveinleft at left
                    c"Hey! Stop that"
                    narrator"The two girls halt their actions and stare at her"
                    narrator"{i}Girl 1{/i}: Why? Jason allows us to do it"
                    c"Jason might allow it, but I don't and mother nature surely doesnt either"
                    narrator"She started to slowly cleaned up the mess and tended to the garden with her limited knowledge"
                    c"You should be gentle with the garden, it could be beautiful you know"
                    narrator"The girls join in and follow silently mimic her movements and soon enough the area is cleaned up"
                    narrator"{i}Girl 2{/i}: That was kinda fun... We should try this next club time"
                    hide twogirls with moveoutleft
                    show jason with moveinleft at left
                    j"That was amazing, I haven't seen them actually interacting with the gardening like that"
                    j"You really didn't need to do that"
                    menu:
                        "Be gentle":
                            c"You seemed annoyed, I wanted to help out in anyway I can"
                            j"Thanks :)"
                        "Lwk yell at him":
                            c"No, I did have to. You have to"
                            narrator"She gets closer and points a finger at his him "
                            c"It is your responsibility"
                            j"Yeah, that's why I don't force the other members to do anyting"
                            narrator"Callista get upset at this"
                            c"You let them in your club, no? You are the leader, you shouldn't let them treat you like that and nonetheless the garden"
                            j"..."
                            c"Any instructions?"
                            j"..."
                            c"Fine"
                            hide callista with moveoutright
                            hide jason
                            show callista with moveinleft
                            narrator"She walked over to a bench under a tree and began reading, feeling Lilith's glitter be cast upon her"

                "Let them go":
                    narrator"She silently watches the girls playing arounf with the dirt"
                    narrator"Standing side by side, she could feel his unease, the clenching of his fists"
                    c"No gonna do anything"
                    j"mh.."
                    j"Just do whatever. No one cares as you can see"
                    hide jason with moveoutleft
                    c"I guess I'll just walk around then"
                    c"Oh...Hmm?"
                    narrator"She looks at a flower bed of purple chrysanthemums"
                    narrator"She gently strokes the flowers, barely perserved from other's destruction"
                    show lilith with moveinright at topleft
                    l"Here let me just"
                    #show flower in her hair
                    c"Thank you"
                    #tears
    hide callista
    hide lilith
    show bg empty with fade
       



            
    
    





    
    


    
