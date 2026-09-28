# scene 1

label raventattooscene:
    hide screen raven_mall
    hide screen backbuttonMALL
    hide screen uppergui
    scene fs mall
    with Dissolve(1.0)
    pause

    show fbraven current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ ravenSprite = 1
    raven "Haaa...shit."
    show fbraven talkflip:
        xalign 0.7 ypos 120
    with move
    raven "I gotta go I gotta go, I booked the damn appointment."
    $ ravenSprite = 0
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.7)
    $ ravenSprite = 1
    show fbraven current:
        xalign 0.6 ypos 120
    with move
    raven "No no no there's no way, I can't!"
    $ ravenSprite = 0
    player "{i}Oh hey that's...{/i}"
    $ playerSprite = 1
    player "Raven?"
    $ playerSprite = 0
    $ ravenSprite = 1
    raven "Huh? Oh uh hi [povname]."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Everything alright? You look..."
    $ playerSprite = 15
    player "Upset?"
    $ playerSprite = 0
    $ ravenSprite = 1
    raven "I'm fine, totally fine thanks!"
    $ ravenSprite = 0
    $ playerSprite = 1
    player "You sure?"
    $ playerSprite = 0
    raven "....."
    $ ravenSprite = 1
    raven "Fuck okay. I guess there's no harm in telling you."
    $ ravenSprite = 2
    raven "I'm uh here..."
    $ ravenSprite = 1
    raven "To get a tattoo."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Oh that's cool."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "Mmmm yeah cool, so cool."
    $ ravenSprite = 0
    player "...."
    $ playerSprite = 8
    raven "...."
    $ playerSprite = 16
    player "I'm guessing there's more to this?"
    $ playerSprite = 0
    $ ravenSprite = 1
    raven "Sooo..."
    raven "I'm a goth chick right?"
    $ ravenSprite = 0
    $ playerSprite = 1
    player "You said it not me."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "Well girls who dress in all black and tattoos kinda go hand in hand."
    raven "But...I don't have one."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Oh wow really?"
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "See? Who hasn't heard of a goth chick without any tattoos!"
    raven "Anyways last month Melissa kinda brought it up."
    raven "And in a panic I said that I did have one, but it was on my ass."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Ah okay clever."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "Not really, that only made her want to see it more, I kept making excuses but I'm not sure I can do that anymore."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Well this seems like a classic case of peer pressure Raven."
    player "I figured you to have a strong enough personality to not give a shit what Melissa and Stephanie say."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "Well for one, you don't know me well enough don't work off of assumptions alright?"
    $ ravenSprite = 0
    $ playerSprite = 10
    player "Eh, true sorry. Meant no harm."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "It's fine don't worry."
    raven "But two, you don't understand. I love tattoos!"
    raven "I think they're sick, and I WANT one."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Oh....well."
    player "Then what's the problem?"
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "....I'm terrified of needles."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Ahhhh..."
    $ ravenSprite = 2
    $ playerSprite = 0
    raven "I c-can't stand them!"
    show fbraven current at surpriseshake:
        xalign 0.6 ypos 120
    raven "Just the thought of such a tiny metal pin going into my body ugh!"
    raven "I-It freaks me out!"
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Okay makes sense now. That sucks."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "I already made the appointment but I might cancel."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Would be a shame to come this far but if y-"
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "Wait!"
    $ ravenSprite = 0
    $ playerSprite = 11
    player "??"
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "You still owe us favors right? For the file thing?"
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Uh...yeah I guess I still have to do a favor for you."
    player "But I don't think me getting the tattoo would really work."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "Haha no not that but..."
    $ ravenSprite = 2
    raven "Maybe you could just...s-stay with me?"
    raven "While it happens? I can't ask one of the girls for support an-"
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Okay."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "Oh, really?"
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Yeah sure, let's go I got you."
    $ ravenSprite = 1
    $ playerSprite = 0
    raven "T-Thanks [povname]!"
    raven "C'mon the appointment is soon so let's go now!"
    $ ravenSprite = 0
    hide fbraven current
    hide fbplayer current
    scene fs blackblank
    with Dissolve(1.0)
    "Raven takes you to the tattoo parlor and she's immediately told to get ready"
    "You were a bit surprised when Raven started to take off her skirt and panties before getting on the table"
    "You remembered she said it was going on her ass.."
    scene fs raventattoo1a
    with Dissolve(0.7)
    "Bzzzz"
    scene fs raventattoo1araven
    raven "I-I don't know if I can do this [povname] I'm kinda freakin out."
    scene fs raventattoo1aplayer
    player "You're gonna be fine Raven. All you have to do is not move."
    scene fs raventattoo1bplayer
    player "Let's talk about something else. What kinda tattoo is it?"
    scene fs raventattoo1braven
    raven "I-It's a skull..."
    scene fs raventattoo1bplayer
    player "Why a skull?"
    scene fs raventattoo1braven
    raven "You mean aside from the obvious matching asthetics?"
    "Tattoo lady" "Heh."
    scene fs raventattoo2a
    with Dissolve(0.7)
    raven "I-It's so there's something to look at for the guy when he's doing me doggystyle."
    scene fs raventattoo2aplayer
    player "That is both hot and hilarious."
    scene fs raventattoo2a
    raven "Mmmmmmnnnnn!!"
    scene fs raventattoo2aplayer
    player "Hey relax, hold my hand you're gonna be okay."
    scene fs raventattoo2b
    raven "Ahhhh! Shit!"
    player "Squeeze my hand Raven! I'm right here."
    scene fs raventattoo3
    raven "Oh God, fuck me..."
    "Tattoo Lady" "Almost done hun."
    scene fs raventattoo4
    with Dissolve(0.7)
    player "You're doing great."
    raven "It doesn't feel like it."
    player "Anything I can do?"
    raven "No....Just keep doing that."
    "Tattoo Lady" "{i}Aww, cute couple.{/i}"
    scene fs raventattoo5
    "Tattoo Lady" "Annnnd finished!"
    raven "Wha? Really?"
    "Tattoo Lady" "Not as bad as you thought right?"
    raven "Uh...I guess not."
    "Tatoo Lady" "Go get changed and my assistant will bandage you up."
    raven "O-Okay!"
    scene fs raventattoo7a
    with Dissolve(1.0)
    player "Thanks for dealing with her."
    scene fs raventattoo7b
    "Tattoo Lady" "Hehe no prob, it's part of the job."
    scene fs raventattoo7a
    player "You have some pretty awesome Tattoos yourself."
    scene fs raventattoo7b
    "Tattoo Lady" "Thanks! I did about half of them on my own."
    scene fs raventattoo7a
    player "That's really impressive!"
    scene fs raventattoo7b
    "Tattoo Lady" "I'm Heather by the way."
    "Heather" "You want a tat too?"
    scene fs raventattoo7a
    player "Maybe one day."
    scene fs raventattoo7b
    "Heather" "Come back if you ever change your mind cutie."
    scene fs raventattoo7a
    player "Thanks Heather."
    scene fs blackblank
    with Dissolve(1.0)
    "You find Raven and leave the store"
    "Soon after she goes home since she said she should rest her ass"
    "You chuckle at the thought and head out yourself"
    $ ravenscene1 = 1
    $ ravenquestlog = "Well that's one favor down. Didn't think it'd involve me seeing Raven's bare ass but I ain't complaining."
    jump overworldmap

# scene 2

label ravenbjscene:
    scene fs playerbedneutral
    with Dissolve(0.7)
    player "{i}Ah today was pretty good I'd say.{/i}"
    player "{i}I wonder how long an ass tattoo takes to heal...{/i}"
    play sound "audio/knock-on-door.wav"
    "*Knock knock knock*"
    scene fs playerbedthink2
    player "Huh?"
    scene fs livingroomnight
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.4 ypos 120
    $ playerSprite = 1
    player "Who could that be?"
    $ playerSprite = 11
    raven "Hey uh, [povname]? Is this the right place?"
    $ playerSprite = 1
    player "Raven? Come in."
    $ playerSprite = 0
    $ ravenSprite = 2
    show fbraven current:
        xalign 0.6 ypos 120
    raven "Hey! Uh. Long time no see?"
    $ ravenSprite = 0
    $ playerSprite = 15
    player "Why are you here? Is everything alright?"
    $ playerSprite = 14
    $ ravenSprite = 2
    raven "Yeah totally! Thanks for the concern. My ass feels a lot better haha."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Haha great."
    $ playerSprite = 0
    raven "....."
    player "....."
    $ ravenSprite = 1
    $ playerSprite = 11
    raven "I came to suck your dick."
    player "...Hold on let me get the lights."
    scene fs raventattoo8b
    with Dissolve(1.0)
    player "You came to what now?"
    scene fs raventattoo8a
    raven "I was lying down and thinking about it and the dynamic didn't sit right with me."
    scene fs raventattoo8b
    player "The....dynamic?"
    scene fs raventattoo8a
    raven "Uh huh. I'm not supposed to be some damsel in distress."
    raven "I'm in the group that's supposed to be slutty hot chicks."
    scene fs raventattoo8b
    player "Bold label."
    scene fs raventattoo8a
    raven "Plus Stephanie's still trying to get us to seduce you."
    raven "Anyways. I figured it'd be a good way to pay you back for today so it works out."
    scene fs raventattoo8b
    player "I see. And you thought I'd go along with this?"
    scene fs raventattoo9
    raven "Uh huh."
    scene fs raventattoo8b
    player "I dunno Raven I kinda-"
    scene fs raventattoo10
    with vpunch
    raven "Mmmmmn!"
    player "!!!"
    scene fs raventattoo11b
    raven "What were you saying?"
    scene fs raventattoo11a
    player "Nothing. Do I have lipstick all over my mouth?"
    scene fs raventattoo11b
    raven "You sure do. I think I'll make your cock match."
    show ravenbjscene movie1
    with Dissolve(1.0)
    pause
    player "That feels good Raven..."
    raven "Hehe yeah?"
    raven "I wasn't expecting you to be so big."
    raven "Really turns me on..."
    show ravenbjscene movie2
    raven "MMM..."
    player "Oh shit."
    player "You know I have a girlfriend right? I shouldn't be doing this."
    raven "Mmph."
    pause
    scene fs raventattoo14
    with vpunch
    player "Oh fuck me!!"
    raven "Ughk!"
    player "You're so fucking deep!"
    player "{i}This is super hot I can't lie.{/i}"
    show ravenbjscene movie3
    pause
    show ravenbjscene movie4
    raven "*Suck suck suck*"
    raven "Mmmm!!"
    player "{i}Shit she's sucking just the tip super hard.{/i}"
    player "This view is too hot Raven I'm gonna fucking cum."
    raven "Hum foa meh!"
    show ravenbjscene movie5
    with vpunch
    pause
    player "AHHH!"
    scene fs raventattoo18
    pause
    raven "Uhn..."
    player "Hah...hah..."
    scene fs blackblank
    with Dissolve(1.0)
    raven "I'm pretty good right?"
    player "That was insane."
    raven "Hold still for a second."
    player "Huh?"
    show ravenselfie postravenblowjob
    with flash
    pause
    player "Ah. You gonna keep that to yourself?"
    melissa "HELL no I'm sending this to the girls right now!"
    player "Welp...can't stop you."
    $ renpy.notify("Got Raven's Picture!")
    $ phone_pictures.append("bullies selfies raven no tat")
    hide ravenselfie postravenblowjob
    with Dissolve(0.7)
    raven "Maybe we can go further next time."
    player "Wait, next time? Raven I can't-"
    raven "Byyeee!"
    player "Annnnd she's gone."
    player "...."
    player "I gotta get this lipstick off."
    $ ravenscene1 = 2
    $ ravenquestlog = "No more solo content for Raven in this version (Ch2.5B)"
    jump gotosleep