# chapter 2
# interaction 1 i guess
# part 1?

label josykatiehangout1:
    hide screen uppergui
    hide screen questboxpreview
    scene fs livingroom
    with Dissolve(0.5)
    ""
    show fbplayer current:
        xalign 0.4 ypos 120

    player "{i}Ahh, home sweet home.{/i}"
    player "{i}Should I game a little, or chill and watch something?{/i}"
    player "{i}Hmmm or mayb-{/i}"
    "Vvvvp vvvvp"
    $ playerSprite = 2
    player "Hmm? Who's calling?"
    josy "{cps=25}Heeeeey you! It's Josy.{/cps}"
    player "{cps=25}Josy? Ava's friend?{/cps}"
    josy "{cps=25}Yup! She gave me your number.{/cps}"
    josy "{cps=25}Okay I took her number from her phone but same thing.{/cps}"
    player "{cps=25}Haha okay. What's up?{/cps}"
    josy "{cps=25}So Katie and I are working on a computer business course and we need somewhere to study.{/cps}"
    josy "{cps=25}It's exam season so school's full, we can't do the library cause Charlotte's there and she HATES Katie.{/cps}"
    josy "{cps=25}And then Josy was all like hey! [povname]'s a computer nerd or something right? He could probably help us!{/cps}"
    player "{cps=25}Hmm well I did also take the same course when I was in school.{/cps}"
    josy"{cps=25}Really? Awesome I knew you could help!{/cps}"
    player "{cps=25}But idk, I got a bunch of NERDY things I gotta do...{/cps}"
    josy "{cps=25}Ohhh c'mon! I was kidding! Nerds are hot!{/cps}"
    josy "{cps=25}Well, hot nerds like you are hot!{/cps}"
    player "{cps=25}Haha alright alright, where are you? Want me to pick you up somewhere?{/cps}"
    josy "{cps=25}Ummm actually...{/cps}"
    play sound "audio/knock-on-door.wav"
    "*Knock Knock*"
    $ playerSprite = 11
    player "Huh?"
    $ josySprite = 6
    show fbjosy current:
        xalign 0.6 ypos 120
    josy "We're.."
    $ katieSprite = 1
    show fbkatie current:
        xalign 0.7 ypos 120
    katie "Already here!"
    $ katieSprite = 0
    josy "Hahaha!"
    $ playerSprite = 1
    $ josySprite = 4
    player "Wait, you came here first?"
    $ playerSprite = 0
    $ josySprite = 5
    josy "Katie pretty much assured me that you'd let us in."
    $ playerSprite = 16
    player "I...don't really know what to say to that."
    $ playerSprite = 0
    $ katieSprite = 3
    katie "You have a really nice place, I can see why my sister likes coming over so much."
    $ katieSprite = 0
    $ playerSprite = 1
    player "Thanks! I tried my best to keep it nice. Should we go to my room and get started?"
    $ playerSprite = 0
    $ josySprite = 6
    josy "Let's goooo!"
    $ josySprite = 4
    scene fs josykatiestudy1
    with Dissolve(1.0)
    "We all gathered on my bed to study."
    scene fs josykatiestudy2
    with Dissolve(1.0)
    "I showed the some basic computer science and fundamentals"
    "Making sure to give short and clear explanations"
    scene fs josykatiestudy3
    "The girls seemed to really appreciate the help, and we took some breaks just to talk about random things"
    scene fs josykatiestudy4
    with vpunch
    josy "Hey! Boobs on arms are not allowed!"
    katie "Whaaa? I dunno what you're talking about!"
    scene fs josykatiestudy5
    with Dissolve(1.0)
    "It was honestly pretty good company"
    "I was surprised we laughed so much"
    scene fs josykatiestudy5B
    with Dissolve(0.7)
    "And I'm never gonna complain when I have two beautiful girls at my side"
    "I was expecting some mischeif from them"
    scene fs josykatiestudy6
    with Dissolve(0.5)
    "But I think I'll let it go..."
    $ josyquestlog = "Helping the girls was kind of nice, wonder if they'll need it again"
    $ josyquesticon = "gui/questboxJosy.png"
    $ josyscene1 = 1
    jump passtime

# scene 2

label josykatiehangout2:
    hide screen uppergui
    hide screen questboxpreview
    scene fs livingroom
    with Dissolve(0.5)
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    play sound "audio/knock-on-door.wav"
    "*Knock Knock Knock*"
    $ playerSprite = 11
    player "Huh? Who's that now."
    $ josySprite = 6
    show fbjosy current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    josy "Heeey!"
    $ josySprite = 5
    player "Ah."
    $ katieSprite = 1
    show fbkatie current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    katie "Hehe hi [povname]!"
    $ katieSprite = 0
    $ playerSprite = 1
    player "I should've known."
    $ playerSprite = 0
    $ josySprite = 6
    josy "Do you mind? We have another quiz coming up..."
    $ josySprite = 5
    $ katieSprite = 1
    katie "We would weeeally appreciate it!"
    $ katieSprite = 0
    $ playerSprite = 1
    player "Promise not to say anything like that again and you got a deal."
    $ playerSprite = 0
    $ katieSprite = 1
    katie "Hehe done!"
    $ katieSprite = 0
    scene fs josykatiestudy2
    with Dissolve(1.0)
    "You sat with the girls on your bed again and went through a bunch of formulas and sorting methods"
    "They paid pretty good attention the first half"
    scene fs josykatiestudy5B
    with Dissolve(0.5)
    "But things got pretty silly the latter half"
    katie "Haha okay okay fine you were right."
    katie "I'll be back gotta use the washroom."
    josy "Hehe take your time."
    scene fs josykatiestudybj3b
    with Dissolve(0.7)
    player "Alright so you get this one?"
    scene fs josykatiestudybj3c
    josy "Yup totally, you explained it perfectly"
    scene fs josykatiestudybj3b
    player "Great cause there's some tricker problems I can show you two..."
    scene fs blackblank
    with Dissolve(0.7)
    "A few minutes later..."
    scene fs josykatiestudybj5
    with Dissolve(1.0)
    josy "*Sluuuurrp*"
    scene fs josykatiestudybj6
    with Dissolve(0.5)
    katie "Hey so we gotta go in half an hour."
    katie "Coach wants to try a new-"
    player "Fuck!"
    scene fs josykatiestudybj7
    pause
    scene fs josykatiestudybj8
    with vpunch
    katie "JOSY WHAT THE HELL!"
    katie "That's my sister's boyfriend."
    josy "Mhmm.."
    josy "*Slurp*"
    scene fs josykatiestudybj9b
    with Dissolve(0.7)
    katie "Move over and share at least."
    player "Holy shit.."
    scene fs josykatiestudybj9c
    josy "What was that coach always says about teamwork?"
    scene fs josykatiestudybj10
    katie "Mmmmh!"
    josy "Ah."
    scene fs josykatiestudybj11
    player "Girls holy shit."
    player "I don't know how much.."
    scene fs josykatiestudybj12
    player "Fuck! I don't know how much I can take you double teaming me."
    scene fs josykatiestudybj13
    katie "Yeah? You gonna cum for us?"
    josy "All over our pretty little faces?"   
    scene fs josykatiestudybjzoom1
    player "Hah..yeah I'm pretty close haha!"
    scene fs josykatiestudybjzoom3
    katie "C'mon then!"
    josy "C'mon and cum!"
    scene fs josykatiestudybjzoom2
    player "God damn it this is so wrong!"
    
    image katiejosybj:
        "katie josy extras 3.png"
        0.4
        "katie josy extras 4.png"
        0.4
        repeat
    show katiejosybj
    pause
    player "Fuck, girls!"
    scene fs josykatiestudybjzoom5
    with vpunch
    player "AHHH THAT'S IT!"
    scene fs josykatiestudybj15
    with Dissolve(1.0)
    katie "Hehehe."
    josy "There we go!"
    player "You two are so fucking hot."
    katie "Just wait until next time!"
    player "What?"
    josy "Hahaha!"
    pause
    
    
    $ josyquestlog = "Josy and Katie...what a pair."
    $ josyscene1 = 2
    jump passtime