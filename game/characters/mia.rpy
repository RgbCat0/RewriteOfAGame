# Correctly chronological. Probaly...
#chapter 1
# interaction 1
# part 1

label miaphase1interaction1part1:
    hide screen mia_atschool
    hide screen mia_sophia_atschool
    scene fs classroomZOOM
    with Dissolve(0.5)

    show fbsophia current:
        xalign 0.9 ypos 120

    show fbmia defaultflip:
        xalign 0.7 ypos 120
    pause
    "After walking around for a bit you find the right class and see your girlfriend chatting it up with Sophia"
    show fbplayer current:
        xalign 0.3 ypos 120
    show fbmia current:
        xalign 0.7 ypos 120
    $ miaSprite = 1
    mia "[povname]! You came!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Course I did, I told you I’d come."
    $ playerSprite = 0
    #kiss here
    $ sophiaSprite = 2
    with Dissolve(0.5)
    sophia "...."
    $ playerSprite = 1
    player "Hey Soph, are you two in the same class?"
    $ playerSprite = 0
    sophia "Yeah we took biology together."
    $ miaSprite = 1
    mia "Class starts in a little bit but the professor is always late anyways so you can always visit me here in the mornings."
    $ miaSprite = 0
    $ sophiaSprite = 1
    sophia "Um...m-me too."
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Yeah of course, always happy to see your cute face Mia!"
    player "Oh you too Soph."
    $ sophiaSprite = 2
    $ playerSprite = 0
    $ miaSprite = 4
    #voice "audio/miagameaudio/mialaugh.wav"
    mia "Oh youuuu teehee."
    $ miaSprite = 0
    $ sophiaSprite = 4
    #voice "audio/sophiagameaudio/sophiahmph.wav"
    sophia "Gee thanks. I’m going to go sit down and leave you two to make out or whatever."
    $ sophiaSprite = 3
    show fbsophia:
        xalign 1.5
    with move
    $ playerSprite = 11
    player "....."
    $ playerSprite = 1
    player "She doing alright?"
    $ playerSprite = 0
    $ miaSprite = 8
    mia "I don’t know what’s gotten up her butt lately."
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.42 ypos 120
    with move
    player "Hehe you said butt."
    $ playerSprite = 0
    $ miaSprite = 5
    show fbmia current:
        xalign 0.58 ypos 120
    with move
    voice "audio/miagameaudio/miahehe.wav"
    mia "Hehehe."
    $ miaSprite = 0
    $ playerSprite = 12
    player "*Ahem* Uh..."
    $ playerSprite = 1
    player "So listen Mia, I wanted to let you know I had a really good time the other night."
    player "You’re so beautiful and there’s no one else I’d rather be with right now."
    player "You uh....you make me really happy."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Oh [povname] that’s so sweet of you to say..."
    mia "But there probably aren’t any guys that would DISLIKE..that kind of thing that we did."
    $ miaSprite = 0
    $ playerSprite = 5
    player "Wha...here I am pouring my heart out-"
    $ playerSprite = 4
    $ miaSprite = 5
    #voice "audio/miagameaudio/mialaugh2.wav"
    mia "Hehehe I’m kidding! I um...I had a really good time too."
    $ miaSprite = 1
    mia "Thank you. For...you know, saying that."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Bah I can’t get mad at such a cute face!"
    $ playerSprite = 0
    $ miaSprite = 4
    mia "Hehehe."
    $ miaSprite = 0
    "Professor" "Alright settle down everyone, I’m just getting my laptop then we’re starting."
    $ playerSprite = 1
    player "I should go, I’ll talk to you later okay?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Come to my house later, you can meet my {color=#dd3939}Mom{/color} and {color=#dd3939}Sister{/color} if they’re home."
    $ miaSprite = 0
    $ playerSprite = 11
    player "Oh uh, alright. See yah."
    hide fbmia current
    with Dissolve(0.5)
    $ playerSprite = 7
    player "{i}I haven’t met her family yet so this should be interesting...no mention of a dad huh?{/i}"
    $ miaphase1interaction1 = 1
    $ playerSprite = 0

    $ miaquestlog = "Mia wants me to visit her family in the afternoon at her house."
    $ sophiaquestlog = "Sophia seems upset, I should talk to her in her class."
    $ sophiaquesticon = "gui/questboxSophia.png"

    hide fbplayer
    hide fbsophia
    hide fbmia
    hide fs
    jump classroom1

# UNREACHABLE
# UNREACHABLE
# UNREACHABLE MIAPIVOT
label miaphase1interaction1part1postconvo:
    hide screen mia_atschool
    hide screen sophia_atschool
    scene fs classroomZOOM
    with Dissolve(0.5)
    $ miaSprite = 1
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    mia "Come to my house later, class is about to start!"
    $ miaSprite = 0
    hide fbmia
    hide fbplayer
    jump classroom1

# part 2

label miaphase1interaction1part2:
    hide screen uppergui
    scene fs blackblank
    with Dissolve(1.0)
    $ playerSprite = 1
    $ juliaSprite = 3
    play sound "audio/knock-on-door.wav"
    player "*Knock* *Knock*"
    player "Uh, hello? Is anyone here?"

    mia "Oh you’re here! Moooom he’s here!"
    mia "Come in."
    scene fs gfhouse
    with Dissolve(0.3)
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Wow this is a really nice place Mia."
    $ playerSprite = 0

    $ miaSprite = 1
    mia "Thank you!"
    $ miaSprite = 0
    show fbjulia current behind fbmia:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    julia "I'm glad you like it young man."
    $ juliaSprite = 0
    $ playerSprite = 11
    player  "{i}Holy shit what a knock-out! Mia’s mom is smoking, now I know where her tits come from.{/i}"
    $ miaSprite = 1
    mia "Mom this is [povname]. [povname], Mom."
    $ playerSprite = 0
    $ miaSprite = 0
    $ juliaSprite = 3
    julia "Please, call me Julia."
    $ juliaSprite = 0
    $ playerSprite = 10
    player "Pleasure to meet you ma’am, oh er..Julia."
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Haha that’s fine too."
    $ playerSprite = 0
    $ juliaSprite = 2
    julia "I’m glad to see my daughter is dating someone so handsome."
    $ miaSprite = 6
    $ playerSprite = 8
    voice "audio/miagameaudio/miamuum.wav"
    mia "Muuuum!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Thank you ma’am, but I think you'd agree your daughter is the most beautiful girl I’ve ever met, and she obviously got her looks from you."
    $ playerSprite = 0
    $ juliaSprite = 0
    $ juliaSprite = 3
    julia "Oh my what a charmer! A double compliment haha. Mia dear, take care of our guest while I finish up dinner in the kitchen."
    $ juliaSprite = 0
    hide fbjulia current
    with Dissolve(0.5)
    $ miaSprite = 1
    mia "Come sit in the living ro-."
    $ katieSprite = 1
    show fbkatie current behind fbmia:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ miaSprite = 0
    $ playerSprite = 11
    $ katieSprite = 1
    katie "So this is him huh?"
    $ katieSprite = 0
    $ miaSprite = 1
    mia "Oh sis, yes this is [povname]."
    $ miaSprite = 0
    $ playerSprite = 0
    player "{i}Huh, she’s pretty cute.{/i}"
    $ miaSprite = 1
    mia "This is Katie my little sister."
    $ miaSprite = 0
    $ katieSprite = 1
    katie "So you’re banging my big sis?"
    $ katieSprite = 0
    $ playerSprite = 11
    player "Sorry?"
    $ katieSprite = 1
    katie "She stayed over at YOUR house the other night right? So you fucking or what?"
    $ katieSprite = 0
    $ playerSprite = 4
    menu:
        "Yup we fucking.":
            jump yupwefuckin
        "We are dating now yes.":
            jump wearedatingnowyes

    label yupwefuckin:
        $ miaSprite = 8
        mia "Katie you shouldn’t talk like that t-"
        $ playerSprite = 1
        player "Yup we’re fucking."
        $ playerSprite = 0
        mia "[povname] please don’t lower yourself to her level... "
        $ miaSprite = 0
        $ katieSprite = 1
        show fbkatie defaultfliptalk
        katie "What’s wrong sis? I’m just trying to make sure no thin-dicked loser takes advantage of you!"
        $ katieSprite = 0
        $ playerSprite = 4
        player "{i}Okay well I’m not letting that one go.{/i}"
        $ playerSprite = 5
        show fbkatie current behind fbmia:
            xalign 0.6 ypos 120
        player "Thin-dicked? Uh....Mia?"
        $ playerSprite = 0
        show fbkatie defaultfliptalk
        katie "Huh?"
        show fbkatie uniformflip

        $ miaSprite = 1
        mia "Um sis...he’s actually..."

        show fbmia current:
            xalign 0.682 ypos 120

        $ miaSprite = 7

        window hide
        voice "audio/miagameaudio/miahmm.wav"
        pause
        mia"Pretty large?"

        show fbkatie current behind fbmia:
            xalign 0.45 ypos 120
        with move
        $ playerSprite = 11
        $ katieSprite = 1
        katie "Oh really?.."
        $ katieSprite = 0
        show fbmia current:
            xalign 0.7 ypos 120
        $ miaSprite = 0
        player "{i}Okay not the reaction I was expecting...{/i}"
        $ katieSprite = 1
        katie "Can you prove it?"
        $ katieSprite = 0
        $ miaSprite = 6
        mia "Katie! That is not something that...I should..let you see?"
        $ miaSprite = 0

        show fbkatie defaultfliptalk behind fbmia:
            xalign 0.45 ypos 120
        katie "It's fine sis I'm just joking around.."
        $ katieSprite = 1
        show fbkatie current behind fbmia:
            xalign 0.45 ypos 120
        katie "If you're treating her right out and...inside the bedroom I guess I can let you off the hook."
        $ katieSprite = 0
        $ miaSprite = 6
        mia "UGH!"
        $ miaSprite = 2
        $ katieSprite = 1
        katie "Joking! Joking! I'm gonna go back upstairs, call me when dinner's ready"
        $ katieSprite = 0
        $ playerSprite = 7
        player "{i}Hmmm, I feel like if I don't ask for her number I might miss an opportunity.{/i}"
        menu:
            "Ask for Katie's phone number":
                jump askforkatienumber
            "Don't ask for number":
                jump continuemeetingfam

        label askforkatienumber:
            $ miaSprite = 0
            $ playerSprite = 1
            player "Hey before you go you uh, want to give me your number?"
            $ playerSprite = 0
            mia "?"
            $ playerSprite = 10
            player "In case of emergency of course and I need to get in touch with Mia."
            $ playerSprite = 0
            $ miaSprite = 1
            mia "Oh."
            $ miaSprite = 0
            #add katie to phone number list
            $ katieSprite = 1
            katie "Suuuuuure...It’s  552-1315."
            $ katieSprite = 0
            $ playerSprite = 1
            player "Heh. Great thanks."
            $ playerSprite = 0
            hide fbkatie default
            with Dissolve(0.5)
            $ katiequestlog = "I should text Katie!...Or should I?"
            $ katiequesticon = "gui/questboxKatie.png"
            jump continuemeetingfam

    label wearedatingnowyes:
        $ miaSprite = 1
        mia "Katie y-you don’t have to talk like that t-"
        $ miaSprite = 0
        $ playerSprite = 5
        player "We are dating now yes, so whatever actions come with that kind of relationship can be implied if you want, but that’d still be...private."
        $ playerSprite = 0
        $ katieSprite = 1
        katie "Uh huh."
        $ katieSprite = 0
        $ playerSprite = 1
        player "Where do you go to school?"
        $ playerSprite = 0
        $ katieSprite = 1
        katie "At the college down the road near karby’s."
        $ katieSprite = 0
        $ playerSprite = 1
        player "Ah the one where everybody is the legal age of consent?"
        $ playerSprite = 0
        $ katieSprite = 1
        katie "Yeah that’s the one. We’re on break now so I’m pretty free these days."
        $ katieSprite = 0
        $ playerSprite = 1
        player "I see...."
        $ playerSprite = 0
        "VVVVVPPP VVVVVPPPP"
        #show fbkatie phonelook
        $ katieSprite = 1
        katie "Oh! Josy is calling me I gotta go to my room, call me when dinner’s ready."
        $ katieSprite = 0
        hide fbkatie default
        with Dissolve(0.5)
        player "She seems nice, if not overprotective."
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Yes Katie loves me a lot and I love her too! But she can get a bit...aggressive."
        $ miaSprite = 0
        $ playerSprite = 1
        player "You’re still cuter though."
        $ playerSprite = 0
        $ miaSprite = 1
        mia "[povname]!"
        $ miaSprite = 0
        $ playerSprite = 1
        player "Hehe."
        $ playerSprite = 7
        player "{i}Hmmm, I feel like if I don't ask for her number I might miss an opportunity.{/i}"
        menu:
            "Ask for Katie's phone number":
                jump askforkatienumber2
            "Don't ask for number":
                jump continuemeetingfam

        label askforkatienumber2:
            $ playerSprite = 1
            player "Oh you should give me her number in case I can’t reach you."
            $ playerSprite = 0
            #add katie to phone number list
            $ miaSprite = 1
            mia "Oh um I guess that’s okay. It’s 552-1315."
            $ miaSprite = 0
            $ playerSprite = 1
            player "Heh. Great thanks."
            $ playerSprite = 0
            jump continuemeetingfam

        label continuemeetingfam:
            scene fs blackblank
            with Dissolve(1.0)
            $ renpy.notify("Got Katie's Number!")
            $ contact_list.append("Katie")
            "You continued to talk for a while before dinner was ready. It was a great meal and everyone enjoyed it"
            "Katie sat to your left and Mia to your right, while Julia was across from you. Julia’s cooking was amazing and you hoped that Mia will one day be just as good as her mom."
            "After dinner was done and you chatted while having dessert. You then said your goodbyes and thanked them for the meal before leaving"
            player "Hmmm I didn't really get any alone time with Mia, maybe I should text her once I'm home in my room."
            hide fbplayer
            hide fbmia
            hide fbjulia
            hide fbkatie
            hide fs
            $ miaquestlog = "Text Mia from your room at night."
            $ miaphase1interaction1 = 2
            jump gotosleep

#part 2.5 i guess
label textmiafornudes:
    hide screen contacts
    hide screen backbuttonROOM
    scene fs playerroomNight
    player "{cps=25}Hey baby, you awake?{/cps}"
    mia "{cps=25}Hi yes I’m just lying in bed, what’s up?{/cps}"
    player "{cps=25}Horny.{/cps}"
    mia "{cps=25}Oh...{/cps}"
    player "{cps=25}What are you wearing?{/cps}"
    mia "{cps=25}My night gown.{/cps}"
    player "{cps=25}Ooooo{/cps}"
    mia "{cps=25};P{/cps}"
    player "{cps=25}Can I see?{/cps}"
    mia "{cps=25}Okay.{/cps}"
    mia "{cps=25}Sent.{/cps}"
    player "{cps=25}You’re amazing, beautiful and amazing.{/cps}"
    mia "{cps=25}Oh I don't know maybe that's true haha!{/cps}"
    player "{cps=25}Night baby.{/cps}"
    mia "{cps=25}Good night!{/cps}"
    player "{i}I should definitely ask her to come over next time.{/i}"
    player "{i}But right now my phone's picture section is calling me.{/i}"
    $ renpy.notify("Got Mia's Selfie!")
    $ phone_pictures.append("mia selfienight")
    $ miaphase1interaction1 = 3
    $ miaroutecurrentday = dayNumber
    $ miaquestlog = "I should check out Mia's selfie, then text her again at night."
    hide fs playerroomNight
    jump playerRoom

#part 3
#this is basically miaphase1interaction1part3 (not my comment)
label textmiatocomeover:
    hide screen contacts
    hide screen backbuttonROOM
    player "{cps=25}Hey Mia, what’s up?{/cps}"
    mia "{cps=25}Hey [povname]. Not much! Need anything?{/cps}"
    player "{cps=25}Yeah I need YOU. Can you come over tonight?{/cps}"
    mia "{cps=25}Um yeah I think I can, I’ll be there soon.{/cps}"
    scene fs blackblank
    "After waiting for a bit..."
    scene fs livingroomnight
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    "*Knock* *Knock*"
    $ playerSprite = 1
    player "Come in it's open!"
    $ playerSprite = 0
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Hey babe, was it cold outside?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Yeah a bit."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Come cuddle with me on the couch."
    $ playerSprite = 0
    scene fs jerkoffonmia1
    with Dissolve(0.5)
    window hide
    pause
    "The two of you turn on the TV but focus on cuddling, the sound was so low you could barely hear it"
    mia "You're so warm."
    player "Comes with being a great cuddle buddy."
    mia "Hehe."
    player "{i}Man Mia smells amazing...{/i}"
    player "{i}I'm such a lucky guy. She's kinda perfect....{/i}"
    "You feel yourself starting to get an erection"
    scene fs jerkoffonmia2
    with Dissolve(1.0)
    pause
    mia "{i}Huh? What's that I feel against my...OH..."
    mia "I know what you're thinking about."
    player "{i}God I'm getting so turned on I need to kiss her.{/i}"
    player "Mia..."
    scene fs jerkoffonmia3
    with Dissolve(1.0)
    voice "audio/miagameaudio/miamakeout1.wav"
    mia "Mmmmm."
    player "{i}Man her lips taste amazing, I'm surprised every time we make out.{/i}"
    mia "{i}H-His tongue is...{/i}"
    scene fs jerkoffonmia4
    with Dissolve(1.0)
    mia "Ahn...."
    window hide
    pause
    player "{i}Fuck I'm so turned on now I can't hold back, I hope she doesn't freak out at this.{/i}"
    scene fs jerkoffonmia5
    with Dissolve(1.0)
    stop sound fadeout 5
    player "Sorry Mia I gotta jerk off."
    mia "Oh...You need to cum?"
    player "Yeah you're just so hot I can't stop myself, is that okay?"
    "You stand up and upzip your pants, taking out your cock"
    scene fs jerkoffonmia5b
    with Dissolve(0.7)
    mia "{i}C'mon Mia! Help him out you gotta be a good girlfriend!{/i}"
    mia "{i}You already had s-sex with him, it's not a big deal!{/i}"
    mia "O-Okay here."
    scene fs jerkoffonmia6
    with Dissolve(1.0)
    window hide
    pause
    scene fs jerkoffonmia7b
    with Dissolve(1.0)
    mia "Go ahead..."
    player "Sweet Jesus your tits are amazing."
    "Mia's tits were extremely stimulating, didn't take long before you were ready to climax"
    player "AHHHH YESSSS FUCK!"
    scene fs jerkoffonmia8b
    with flash
    pause
    scene fs jerkoffonmia9bb
    player "All over your tits!"
    scene fs jerkoffonmia9cb
    with flash
    pause
    scene fs jerkoffonmia9cbb
    window hide
    pause
    scene fs jerkoffonmia10
    with Dissolve(1.0)
    mia "{i}Oh wow this is so much! I didn't notice last time because he was inside me...{/i}"
    player "Oh fuck that was good, your tits get me everytime."
    scene fs jerkoffonmia6
    with Dissolve(1.0)
    mia "Feel better?"
    player "Loads better thank you baby."
    mia "Okay glad I could help. I should get cleaned up then head home though, I have another test tomorrow."
    menu:
        "Don’t clean up":
            jump dontcleanupmia
        "Sure thing":
            jump surethingmia

    label dontcleanupmia:
        player "Wait, I don’t want you to clean up."
        scene fs jerkoffonmia6b
        mia "What?"
        player "Leave my cum on you, let it dry and go to sleep with it."
        player "Don’t clean it off until your next shower."
        mia "I...that’s a little weird [povname]."
        player "It’s really hot is what it is!"
        player "The idea of you walking around with my cum all over your tits really turns me on."
        mia "Well okay then, if you like that..."
        scene fs blackblank
        with Dissolve(0.5)
        player "You do this for me and I’ll do something for you next time."
        mia "Ooooo hot chocolate! You know I love your hot chocolates."
        player "Alright then that’s a deal!"
        player "Be safe going home."
        mia "I will!"
        "You kiss goodbye and Mia leaves your home"
        $ miaphase1interaction1 = 4
        $ miaquestlog = "I should stop by Mia's place again during the afternoon."
        hide fs balckblank
        jump gotosleep

    label surethingmia:
        player "Sure thing. "
        scene fs blackblank
        with Dissolve(0.5)
        player "Be careful on your way home."
        mia "I will don’t worry."
        player "I owe you your favorite hot chocolate! Thanks again."
        "*Kiss*"
        mia "You’re welcome, bye."
        $ miaphase1interaction1 = 4
        $ miaquestlog = "I should stop by Mia's place again during the afternoon."
        hide fs blackblank
        jump gotosleep

# Interaction 2 
# part 1
# With mia's mom, can be skipped though. This reveales favorite treat for part 2

label miaphase1interaction2part1:
    hide screen julia_kitchen
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    $ juliaSprite = 0
    show fbjulia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Hello Julia!"
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Oh why hello there [povname], come to visit Mia?"
    $ juliaSprite = 0
    $ playerSprite = 1
    player "Yes ma’am, what are you cooking?"
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "I’m baking some Pecan Tarts, they’re the girls’ favourite!"
    $ juliaSprite = 0
    $ playerSprite = 1
    player "They look amazing! Can you teach Mia how to make these?"
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Oh sweety....I’m sorry. I’ve tried to teach Mia how to cook."
    julia "She...she has some trouble with it...."
    $ juliaSprite = 0
    $ playerSprite = 5
    player "Oh...damn. Yeah I can see that..."
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Well if you want to switch sisters, Katie inherited my cooking skills for sure haha."
    $ juliaSprite = 0
    $ playerSprite = 1
    player "Or I can go straight to the source!"
    $ playerSprite = 0
    julia "*blush*"
    $ juliaSprite = 3
    julia "Oh my was that a naughty joke Mr. [povname]?"
    $ juliaSprite = 0
    $ playerSprite = 6
    player "What? No! "
    player ".....Maybe?"
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Hehe I’ll keep that to myself. You should go see my daughter now."
    $ juliaSprite = 0
    $ playerSprite = 1
    player "S-Sure Julia, have a nice day."
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "You too handsome."
    $ juliaSprite = 0
    $ miaphase1interaction2 = 1
    $ juliaquestlog = "Mia's mom is super hot, I should talk to her more often."
    $ juliaquesticon = "gui/questboxJulia.png"
    hide fbplayer
    hide fbmia
    jump gfhouse

label miaphase1interaction2part1postconvo:

    hide screen julia_kitchen
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    show fbjulia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "What was it you were making again?"
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Pecan Tarts sweetie. The girls love them."
    $ juliaSprite = 0
    $ playerSprite = 1
    player "Got it, thanks Julia."
    $ playerSprite = 0
    hide fbplayer
    hide fbmia
    jump gfhouse

# part 2

#this is basically miaphase1interaction2part2
label charlottesmiaquiz:
    hide screen uppergui
    scene fs gfroomblur
    with Dissolve(0.5)
    hide screen charlottemia_room

    #this is so mia will stop saying to come over after her route is done
    $ miaphase1interaction1 = 5


    show fbcharlotte defaultflip:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    show fbmia current:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    show fbcharlotte defaultfliptalk
    charlotte "You really let him do that to you?! Just all over your b-boobs like that?"
    show fbcharlotte defaultflip
    $ miaSprite = 1
    mia "I didn’t really mind, and it made him really happy."
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk
    charlotte "Course it did, boys are all perverts who like that kind of thing."
    show fbcharlotte defaultflip
    $ miaSprite = 1
    mia "There’s nothing wrong with pleasing your boyfriend Charlotte, making someone else happy can make you happy too."
    mia "And it’s nice to know someone enjoys my....body the way he does."
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk
    charlotte "Yeah well your body's rockin so it ain't hard."
    show fbcharlotte defaultflip
    $ miaSprite = 1
    mia "Hehe you should find someone to do things like that with too. I’m sure it’d change your mind."
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk
    charlotte "Ugh It’s hard to argue with when you go full lecture mode."
    show fbcharlotte defaultflip
    $ miaSprite = 4
    voice "audio/miagameaudio/mialaugh2.wav"
    mia "Hehe it doesn’t happen often does it."
    $ miaSprite = 0
    image fbcharlotte lookawayflip = im.Flip("Sprites/charlotte sprite hugging arms.png", horizontal = True)
    show fbcharlotte lookawayflip:
        xalign 0.6 ypos 120
    charlotte "And I am NOT interested in b-boys right now. I’m focusing on school."
    show fbcharlotte defaultflip
    $ miaSprite = 1
    mia "Okay, but all I’m saying is [povname] is a good boyfriend."
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk
    charlotte "Well I still don’t trust him! He’s clearly only interested in your body and doesn’t care about you at all!"
    charlotte "A-And he’s a big fat stupid pervert!"
    show fbcharlotte defaultflip
    $ miaSprite = 8
    mia "*Sigh*"
    $ miaSprite = 0
    show fbplayer current:
        xalign 0.3 ypos 120
    $ playerSprite = 1
    player "Hey now I’m not fat."
    $ playerSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte current at surpriseshake
    show fbcharlotte current
    charlotte "Gah!"
    $ miaSprite = 0
    charlotte "Don’t sneak up on us you...you sneaky sneak thief."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Haha what?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Charlotte and I were just having some...girl talk!"
    $ miaSprite = 0
    $ charlotteSprite = 3
    show fbcharlotte current:
        xalign 0.59 ypos 120
    $ playerSprite = 4
    charlotte "I’m going to lay it all out for you Mister! I don’t trust you!"
    $ charlotteSprite = 2
    $ playerSprite = 5
    player "You barely know me..."
    $ playerSprite = 4
    $ charlotteSprite = 1
    charlotte "More like you barely know Mia! Making her do lewd things and filling her mind with...d-dirty filth!"
    #You look at Mia and she shrugs
    charlotte "I know what’ll expose you....a quiz!"
    $ charlotteSprite = 0
    mia "Hmm?"
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk
    charlotte "Being Mia’s long time best-est friend, I know everything about her!"
    $ charlotteSprite = 1
    show fbcharlotte current
    charlotte "I’ll ask you four questions! If you get them wrong we’ll all know you’re a fraud and don’t really care about her!"
    $ charlotteSprite = 0
    $ miaSprite = 1
    mia "Charlotte this is..."
    $ miaSprite = 0
    $ playerSprite = 10
    player "It’s alright Mia, I don’t mind a challenge, plus I’d like to see the look on Carly’s face here when I win."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "It’s CHARLOTTE!"
    $ charlotteSprite = 0
    $ playerSprite = 5
    player "I bet you’re not even French bitch."
    $ playerSprite = 4
    $ charlotteSprite = 1
    charlotte "Question 1!"
    charlotte "We’ll start off easy, what is Mia’s favourite color?"
    $ charlotteSprite = 0
    menu:
        "Blue":
            jump wronganswer
        "Green":
            jump wronganswer
        "Red":
            jump wronganswer
        "Pink":
            jump continuequiz1

    label continuequiz1:
        $ playerSprite = 1
        player "Pink."
        $ playerSprite = 0
        $ charlotteSprite = 1
        charlotte "Hmph. Anyone could’ve guessed that, moving on!"
        charlotte "What is Mia’s favourite treat?"
        $ charlotteSprite = 0
        menu:
            "Cookies":
                jump wronganswer
            "Pecan Pies":
                jump continuequiz2
            "Ice Cream":
                jump wronganswer
            "Donuts":
                jump wronganswer

        label continuequiz2:
            $ playerSprite = 1
            player "Pecan Pies."
            $ playerSprite = 0
            $ charlotteSprite = 1
            charlotte "Err..correct."
            $ charlotteSprite = 0
            $ miaSprite = 9
            mia "Yaaay."
            $ miaSprite = 0
            $ charlotteSprite = 1
            charlotte "Onto the next one!"
            charlotte "What kind of instrument can Mia play?"
            $ charlotteSprite = 0
            menu:
                "Piano":
                    jump wronganswer
                "Cello":
                    jump wronganswer
                "Violin":
                    jump wronganswer
                "Drums":
                    jump continuequiz3

            label continuequiz3:
                $ playerSprite = 1
                player "She played for me once when I visited."
                player "She’s fucking wicked at the drums."
                $ playerSprite = 0
                $ miaSprite = 1
                mia "Haha oh well you know I try..."
                $ miaSprite = 0
                $ playerSprite = 1
                player "No offense babe but I was expecting you to be terrible at keeping count yet you para-diddled the shit outta that set!"
                $ playerSprite = 0
                $ miaSprite = 4
                mia "Hehe."
                $ miaSprite = 0
                $ charlotteSprite = 1
                charlotte "Alright alright! Grrrr, final question!"
                charlotte "What is Mia’s favourite drink!?"
                $ charlotteSprite = 0
                menu:
                    "Tea":
                        jump wronganswer
                    "Mountain Mew":
                        jump wronganswer
                    "Hot chocolate":
                        jump continuequiz4
                    "Caramel Macchiato":
                        jump wronganswer

                label wronganswer:
                    $ charlotteSprite = 1
                    charlotte "ERRRRR! Sorry wrong answer bud!"
                    $ charlotteSprite = 0
                    $ playerSprite = 1
                    player "Wait really?"
                    $ playerSprite = 0
                    $ miaSprite = 1
                    mia "Sorry [povname]. It's alright though I don't mind!"
                    $ miaSprite = 0
                    $ charlotteSprite = 1
                    charlotte "No! He's gotta go!"
                    $ charlotteSprite = 0
                    "While Charlotte and Mia argued, you thought it might be best you excuse yourself and maybe try the quiz again tomorrow"
                    hide fs gfroomblur
                    hide fbcharlotte
                    hide fbmia
                    hide fbplayer
                    jump passtime

                label continuequiz4:
                    $ playerSprite = 1
                    player "Hot Chocolate."
                    $ playerSprite = 0
                    $ charlotteSprite = 3
                    charlotte "Hah! I knew you were a fraud! Mia and I have always loved Caramel Macchiato’s since we were little!"
                    charlotte "Okay goodbye now. You two can break up, twas a short but sweet relationship."
                    $ charlotteSprite = 2
                    $ miaSprite = 1
                    mia "Oh um Charlotte...."
                    $ miaSprite = 0
                    $ charlotteSprite = 0
                    charlotte "Hmm?"

                    $ miaSprite = 1
                    mia "Caramel Macchiato’s aren’t...aren’t my favourite drink..."
                    mia "It’s hot chocolate."
                    $ miaSprite = 0
                    show fbcharlotte defaultfliptalk
                    charlotte "Wha?...Since when?! We always had them together!"
                    show fbcharlotte defaultflip
                    $ miaSprite = 1
                    mia "Since about a month ago? When we started dating really. [povname] makes the most amazing tasty hot chocolates."
                    $ miaSprite = 0
                    $ charlotteSprite = 1
                    show fbcharlotte defaultfliptalk
                    charlotte "I....I...UGH!"
                    $ charlotteSprite = 4
                    show fbcharlotte current
                    charlotte "Give her back dickhead you stole her from me!"
                    show fbcharlotte current:
                        xalign 1.5
                    with move
                    with Dissolve(0.7)
                    # Charlotte runs out of the house crying"
                    $ miaSprite = 8
                    mia "..."
                    mia "Oh dear I should probably go after her."
                    $ playerSprite = 1
                    player "I’ll text you tonight?"
                    $ playerSprite = 0
                    $ miaSprite = 1
                    mia "Yes okay. I’ll see you later!"
                    $ miaSprite = 0
                    $ playerSprite = 1
                    player "Later."
                    $ playerSprite = 0
                    player "{i}I should text her from my room when I'm home.{/i}"
                    #kiss
                    # lol doesnt happen bitchass dev
                    $ miaphase1interaction2 = 2
                    $ charlotteSprite = 0
                    $ miaquestlog = "Mia had to run after Charlotte. I should wait until night and text her again."
                    hide fs gfroomblur
                    hide fbcharlotte
                    hide fbmia
                    hide fbplayer
                    jump passtime

# part 3
label miaphase1interaction2part3:
    hide screen questboxpreview
    hide screen contacts
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonROOM
    scene fs livingroomnight
    player "Hey Mia, wanna come over and watch a movie or something?"
    mia "Okay, I’m on my way!"
    scene fs blackblank
    with Dissolve(0.5)
    "A little while later"
    scene fs miacouchblowjob1
    with Dissolve(0.5)
    "You start watching some action movie with Mia"
    "She lies down and rests her head on your thigh, you found it really cute"
    scene fs miacouchblowjob2
    player "So how's Charlotte doing?"
    mia "She'll be alright, for the longest time it was just us girls."
    mia "But now that you're around and we're dating she's kinda overwhelmed. She doesn't know much about boys."
    player "Well I knew Soph forever, didn't Charlotte know that?"
    mia "Yeah but Sophia kinda kept you seperate from us for a while so it didn't bother her too much."
    mia "I wish she didn't, that way we would've met sooner!"
    player "Haha yeah same now that I'm thinking about it."
    scene fs miacouchblowjob1
    with Dissolve(0.5)
    pause
    scene fs miacouchblowjob2
    mia "Wow the action in this movie is pretty good."
    player "Yeah and Crimson Johansson is super hot, acting's a little iffy though."
    scene fs miacouchblowjob3
    mia "....hmph."
    scene fs miacouchblowjob4
    player "What?"
    scene fs miacouchblowjob4b
    mia "You think she's prettier than me?"
    scene fs miacouchblowjob4c
    player "What? No of course not th-"
    scene fs miacouchblowjob7c
    with Dissolve(0.5)
    player "...."
    player "Thaaaat is a nipple...and there's some boobs."
    mia "I didn't know there was a sex scene in this movie..."
    player "...."
    scene fs miacouchblowjob6
    with Dissolve(0.5)
    window hide
    pause
    scene fs miacouchblowjob7
    with Dissolve(0.5)
    window hide
    pause
    scene fs miacouchblowjob7b
    with Dissolve(0.5)
    window hide
    mia "Are you getting a boner!?"
    player "It's not my fault she's naked! And giving a blowjob!"
    mia "You want a blowjob from Crimson Johanson!??"
    player "Well I...n-no! She's probably terrible at-"
    scene fs miacouchblowjob8
    with Dissolve(0.5)
    mia "I know what'll stop you from thinking about her!"
    player "Wha-"
    scene fs miacouchblowjob9
    with Dissolve(0.5)
    window hide
    pause
    scene fs miacouchblowjob9b
    with Dissolve(0.5)
    player "OH..."
    voice "audio/miagameaudio/miahmph.wav"
    mia "I'll show you who's better at blowjobs!"
    player "Yeah...yeah you should show her..."
    scene fs miacouchblowjob10
    with Dissolve(0.5)
    player "{i}Movie night is looking up!{/i}"
    scene fs miacouchblowjob11
    with Dissolve(0.5)
    mia "*grumble* *grumble*"
    player "Haha I don't know why you're jealous all of a sudden."
    mia "I'm not jealous! I'm just not gonna let some hussy steal you away!"
    scene fs miacouchblowjob12
    with Dissolve(0.5)
    player "Well don't let me stop you..."
    image miadickkisses:
        "miacouchblowjob13.png"
        0.6
        "miacouchblowjob14.png"
        0.6
        repeat

    show miadickkisses
    with Dissolve(1.0)
    mia "*chuu* *chuu*"
    player "Ahhhh shit Mia..."
    scene fs miacouchblowjob15
    with Dissolve(0.5)
    voice "audio/miagameaudio/miabj1.wav"
    mia "*Uhgn..*"
    mia "....."
    image miadicksucking:
        "miacouchblowjob15b.png"
        0.4
        "miacouchblowjob16.png"
        0.4
        "miacouchblowjob16b.png"
        0.4
        "miacouchblowjob16.png"
        0.4
        repeat

    show miadicksucking
    with Dissolve(0.5)
    player "AHHH YES THAT'S IT!"
    scene fs miacouchblowjob17
    with Dissolve(0.5)
    player "Jesus Mia that's so good!"
    player "{i}This girl has a natural dick sucking mouth, it's like her second blowjob ever.{/i}"

    mia "Mmmmmm."
    player "Fuck baby keep doing that with your tongue you're gonna make me cum!"
    mia "Reah Nhao?"
    player "YEAH FUCK HERE IT COMES!"
    scene fs miacouchblowjob18
    with vpunch
    window hide
    pause
    player "UHN!"
    with vpunch
    mia "MMMMHN!!"
    mia "*Gulp* *Gulp*"
    player "{i}She's swallowing my entire load Jesus Christ I love this girl.{/i}"

    #Mia sits up with cum on her face
    scene fs miacouchblowjob19
    with Dissolve(0.7)
    voice "audio/miagameaudio/miapanting.wav"
    mia "Hah.....good?"
    player "So good..."
    mia "Better than Crimson what's her face?"
    player "I've never even met Cr...yes, much much better babe."
    mia "Hehehe I win this time."
    player "Congratulations."
    mia "Hehehe."
    # mia happily kisses you on the cheek while her face is still covered in cum
    $ miaphase1interaction2 = 4
    $ miaquestlog = "I should find Mia and ask her why she never answered my call."
    scene fs blackblank
    with Dissolve(1.2)
    hide fs blackblank
    hide miadicksucking
    jump gotosleep

#part 3.5
label miaphase1interaction2part3wakeup:
    $ miaphase1interaction2 = 5
    player "I should give Mia a call, make sure she got home last night."
    mia "........."
    player "She’s not answering."
    player "Huh...that’s a bit weird. Maybe I should go to her school and find her."
    $ miaphase1interaction3 = 1
    jump playerRoom

# phase 1
# interaction 3
# part 1

label miaphase1interaction3part1:
    hide screen mia_atschool
    hide screen sophia_atschool
    scene fs classroomZOOM
    with Dissolve(0.5)

    $ miaSprite = 3

    show fbmia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ sophiaSprite = 2

    show fbsophia current:
        xalign 0.9 ypos 120
    with Dissolve(0.5)
    
    voice "audio/miagameaudio/miaooosad.wav"
    mia "Oooo.."
    show fbmia current:
        xalign 0.25 ypos 120
    with move
    mia "where is it?!"

    image fbmia worriedflip = im.Flip("Sprites/miafrown.png", horizontal=True, vertical=False)
    show fbmia worriedflip:
        xalign 0.6 ypos 120
    with move
    sophia "It’s not over here Mia. Sorry."

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 5

    show fbmia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    player "Mia! Hey you didn’t answer your phone this morning I uh, I got worried."
    $ playerSprite = 4
    $ sophiaSprite = 1
    sophia "Che, obsessive much?"
    $ sophiaSprite = 0
    $ playerSprite = 5
    player "Fuck off Sophia I’m not being a creep I was legitimately worried."
    $ playerSprite = 4
    $ sophiaSprite = 2
    sophia "I-I.. uh..I didn’t mean..."
    $ miaSprite = 2
    image fbmia frownflip = im.Flip("Sprites/miafrowntalk.png", horizontal=True)
    show fbmia frownflip
    mia "[povname]. Apologize to her, and Sophia stop being so mean lately. Frankly it’s...it’s ticking me off too!"
    sophia "{i}W-why did he yell at me like that? I was only messing around...{/i}"
    $ miaSprite = 2
    show fbmia current
    $ playerSprite = 15
    player "*sigh* Sorry for snapping Soph. I lost my cool."
    $ playerSprite = 14
    $ sophiaSprite = 2
    sophia "It’s...okay. I’m sorry too."
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "So what’s going on?"
    $ playerSprite = 0
    $ sophiaSprite = 2
    sophia "*sigh* Mia lost her phone."
    $ playerSprite = 1
    player "Ah that makes sense."
    $ playerSprite = 0
    $ miaSprite = 3
    mia "My mom JUST bought it for me. Oh I’m really really in big trouble...."
    $ miaSprite = 2
    $ playerSprite = 7
    player "{i}I’ve never seen Mia like this before, usually she’s pretty lax about things so her phone must be pretty important to her.{/i}"
    $ miaSprite = 3
    mia "Ohhhh it’s not heeeere."
    $ miaSprite = 2
    $ playerSprite = 1
    player "Wait didn’t we talk on the phone before you came over and...."
    $ playerSprite = 0
    sophia "And?"
    $ playerSprite = 8
    player "And then you had to uh...we w-watched that movie?"
    $ playerSprite = 0
    sophia "Huh?"
    $ miaSprite = 3
    mia "The one where Crimson Johansson has se-?"
    $ miaSprite = 1
    show fbmia current at surpriseshake:
        xalign 0.6 ypos 120
    mia "OH!"
    $ miaSprite = 0
    mia "*Blushes*"
    $ miaSprite = 1
    mia "Y-Yeah."
    $ miaSprite = 0
    sophia "{i}Why is Mia blushing?{/i}"
    sophia "{i}OH. Oh my god...{/i}"
    $ playerSprite = 6
    player "The point is it wouldn’t be here at school, cause I called you at home afterwards."
    $ playerSprite = 0
    $ miaSprite = 3
    mia "Oh that makes sense."
    $ miaSprite = 2
    $ sophiaSprite = 1
    sophia "Where did you go between now and then?"
    $ sophiaSprite = 0
    $ miaSprite = 2
    mia "Hmmm."
    $ miaSprite = 3
    mia "I went to the park for a walk, the mall for some shopping, stopped by the arcade to see Olivia. And the library to give Charlotte her book back."
    $ miaSprite = 2
    $ playerSprite = 4
    player "{i}How the hell did she go to all those places in...you know what nevermind.{/i}"
    $ sophiaSprite = 2
    sophia "Sorry Mia but it looks like class is going to start soon."
    $ playerSprite = 1
    player "I’ll take a look around those places while you two take your classes. I’ll let you know if I find anything."
    $ playerSprite = 0
    $ miaSprite = 3
    show fbmia current:
        xalign 0.5 ypos 120
    with move
    mia "Oh [povname] thank you....don’t get your hopes up though, a-and don’t worry if you can’t find it alright?"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Oh well now I have to find it, can’t go having my girl look so sad like that!"
    #wipes tear from face
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Hehe s-stop it."
    $ miaSprite = 0
    sophia "{i}Oh darn it. He really is a good boyfriend.{/i}"
    $ miaphase1interaction3 = 2
    $ miaquestlog = "I gotta find Mia's phone! I should check out the 4 places she mentioned for it.."
    hide fbplayer
    hide fbsophia
    hide fbmia
    jump classroom1

# part 1.5

label miaphase1interaction3part1postconvo:
    hide screen mia_atschool
    hide screen sophia_atschool
    scene fs classroomZOOM
    with Dissolve(0.5)
    $ playerSprite = 1
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)

    player "Hey I know your class is starting soon sorry, but where did you visit again?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "It was...the park for a walk, the mall for some shopping, stopped by the arcade to see Olivia. And the library to give charlotte her book back."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Great thanks."
    $ playerSprite = 0
    hide fbplayer
    hide fbmia
    jump classroom1

# part 2

# park
label lookingforphonepark:
    hide screen uppergui
    $ playerSprite = 11
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    player "Damn the park is pretty big, I better get started looking."
    hide fbplayer
    with Dissolve(0.5)
    "You spend a couple hours in the park looking for Mia's phone but to no avail. It's not here."
    if timeofday != "Night":
        jump passtime
    else:
        jump overworldmap


# mall
label lookingforphonemall:
    scene fs mall
    hide screen uppergui
    with Dissolve(0.5)
    $ playerSprite = 11
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    player "Damn the mall is kinda big, I better start looking for Mia's phone."
    hide fbplayer
    with Dissolve(0.5)
    "You spend a couple hours in the mall looking for Mia's phone but to no avail. It's not here."
    hide fs mall
    hide fbplayer
    if timeofday != "Night":
        jump passtime
    else:
        jump overworldmap

# arcade
label lookingforphonearcade:
    scene fs arcade
    hide screen uppergui
    with Dissolve(0.5)
    $ playerSprite = 16
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    player "Well the Arcade doesn't seem too big, I'll start looking for Mia's phone"
    hide fbplayer
    with Dissolve(0.5)
    $ playerSprite = 0
    "You spend a couple hours in the arcade looking for Mia's phone but to no avail."
    "You even run into Olivia who says she hasn't seen it. The phone must not be here."
    hide fs arcade
    hide fbplayer
    if timeofday != "Night":
        jump passtime
    else:
        jump overworldmap


# libary
#basically miaphase1interaction3part2
label looking4miaphone:
    hide screen emily_atlibrary
    scene fs charlottelibraryjilling1
    with Dissolve(0.7)
    hide screen charlotte_library
    pause
    scene fs charlottelibrarycharlotte
    charlotte "Ah...it's you, what do YOU want at the library?"
    scene fs charlottelibraryplayer
    player "Uh...kay I'm looking for Mia's phone."
    scene fs charlottelibrarycharlotte
    charlotte "Her phone?"
    scene fs charlottelibraryplayer
    player "Yeah she lost it last night and this was one of the places she passed by."
    player "Said she gave you a book."
    scene fs charlottelibrarycharlotte
    charlotte "That's right she did...check near the end of the table that's where she handed it to me."
    scene fs charlottelibraryplayer
    player "Thanks a lot Charlotte, you're awesome!"
    scene fs charlottelibrary7
    charlotte "Yeah s-sure."
    $ miaphase1interaction3 = 3
    $ miaquestlog = "Charlotte said Mia's phone might be at the end of the table in the library."
    hide fs charlottelibrary7
    jump library

# libary still...
label looking4miaphonepostconvo:
    hide screen charlotte_library
    hide screen mia_phone
    scene fs charlottelibraryjilling1
    with Dissolve(0.7)

    pause
    scene fs charlottelibraryplayer
    player "Where did you say she handed you the book?"
    scene fs charlottelibrarycharlotte
    charlotte "At the end of the table over there."
    scene fs charlottelibraryplayer
    player "Great thanks."
    hide fs charlottelibraryjilling1
    jump library

# part 3
label miaphase1interaction3part3:
    hide screen charlotte_library
    hide screen mia_phone
    show fbplayer defaultphone:
        xalign 0.5 ypos 120
    player "No way I think this is it! It's gotta be."
    player "I should make sure I've done everything I can before I return her phone. I have a feeling we'll be busy for the rest of the day hehe."
    $ foundphonevariable = 1
    $ miaphase1interaction3 = 4
    $ miaquestlog = "I found Mia's phone! I should give it to her at her house."
    hide fbplayer
    jump overworldmap

# part 3 extra charlotte unreachable
label foundmiaphoneconvo:
    scene fs libraryBLUR
    hide screen charlotte_library
    show fbcharlotte current:
        xalign 0.5 ypos 120
    show fbplayer current:
        xalign 0.1 ypos 120
    $ playerSprite = 13
    player "Charlotte I found her phone!"
    $ playerSprite = 0
    $ charlotteSprite = 11
    charlotte "Oh that's great! Leave it to Mia to somehow lose it here."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Haha I know right? Good thing she's got friends like you."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "Oh I...you're the one who found it I didn't...you should just go already."
    $ playerSprite = 1
    player "Alright I'll see you later I guess."
    $ charlotteSprite = 0
    $ playerSprite = 0
    $ foundphonevariable = 2
    hide fs libraryBLUR
    hide fbplayer
    hide fbcharlotte
    jump library

# part 4
#basically miaphase1interaction3part4
label miaifoundyourphone:
    hide screen uppergui
    scene fs gfhouse
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    "*Rings Doorbell*"
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ miaSprite = 1
    mia "Hello?"
    mia "[povname]!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Guess what I found?"
    $ playerSprite = 0
    $ miaSprite = 5
    voice "audio/miagameaudio/mialaugh.wav"
    mia "WHAT! NO WAY!"
    player "{i}Wow she is really happy.{/i}"
    julia "Mia dear who is it?"
    $ miaSprite = 1
    mia "It's [povname]! He found my ph-"
    $ miaSprite = 10
    mia "OOOH! Um."
    $ miaSprite = 0
    julia "Huh?"
    $ miaSprite = 1
    mia "[povname] is here to pick me up!"
    mia "I’m uh...staying over for the night again, is that okay?"
    $ miaSprite = 0
    player "{i}Oh?{/i}"
    julia "Oh! Well...you’re a grown woman now you can make those kinds of deci-"
    $ miaSprite = 6
    voice "audio/miagameaudio/miamuum.wav"
    mia "MUUUM!"
    $ miaSprite = 0
    julia "Okay Okay, be safe!"
    julia "{i}She’s staying overnight at his house again? That boy must have something real special.{/i}"
    hide fs gfhouse
    hide fbmia
    hide fbplayer
    jump miastaysoveratmyplaceafterphone

# part 4 continue 1
label miastaysoveratmyplaceafterphone:
    hide screen uppergui
    scene fs playerroomNight
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "One second I gotta text some chick real quick."
    $ playerSprite = 0
    $ playerSprite = 2
    player "{cps=25}Hey wanna come over?{/cps}"
    show fbmia phonelook:
        xalign 0.7 ypos 120
    mia "{cps=25}Lol! Yeah sure. Oh I’m here ;){/cps}"
    $ miaSprite = 1
    show fbmia current:
        xalign 0.65 ypos 120
    with move
    mia "Thank you so much for finding my phone, I was feeling terrible about it."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Hey no worries, I’m just happy I was able to find it for you."
    $ playerSprite = 0
    $ miaSprite = 1
    show fbmia current:
        xalign 0.42 ypos 150
    with move
    mia "Come here!"
    hide fbmia current
    hide fbplayer current
    $ miaSprite = 0
    show fbmia mcmiamakeout:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    voice "audio/miagameaudio/miamwahkiss.wav"
    mia "Mmmmm!"
    player "Mmph!"
    $ playerSprite = 1
    show fbmia current:
        xalign 0.42 ypos 150
    show fbplayer current:
        xalign 0.3 ypos 120
    player "You want to move this into the bed?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Whatever you want."
    $ miaSprite = 0

    scene fs blackblank
    with Dissolve(1.0)
    window hide
    jump continuemiasex

# part 4 continue 2
label continuemiasex:
    scene fs miaphase1sex2
    with Dissolve(0.8)
    window hide
    voice "audio/miagameaudio/miadoggystyle1.wav"
    pause
    $ hiden_textbox = True
    mia "Ahhhh!"
    player "That's it, keep taking it like a good girl."
    mia "Y-Yes!"
    player "{i}God her pussy is so fucking good. She's squeezes my cock harder the further I get.{/i}"
    player "You like that?"
    mia "Yes you feel so good."
    player "Who's pussy is this!?"
    mia "It's yours! Only yours!"
    mia "W-Whenever you want it!"
    player "That's right, you big titted slut."
    scene fs blackblank
    with Dissolve(0.8)
    "As you contined to have sex Mia was an absolute pro"
    "Each deep thrust, each sexy insult, she always agreed with you and moaned when she couldn't."
    stop music fadeout 5
    stop sound fadeout 5
    scene fs miaphase1sex1B
    with Dissolve(0.5)
    voice "audio/miagameaudio/miapanting.wav"
    mia "Hah....hah..."
    scene fs miaphase1sex1
    player "Hah...you alright babe? That wasn't too much?"
    scene fs miaphase1sex1B
    mia "N-No I'm okay, I liked it."
    scene fs miaphase1sex1
    player "Well shit haha, ready to keep going?"
    scene fs miaphase1sex1
    mia "Yes, I want you to-"
    scene fs miaphase1sex3
    "*VVVVVIP* *VVVVVVIP*"
    window hide
    pause
    player "That your phone?"
    scene fs miaphase1sex4B
    mia "Yeah one sec..."
    window hide
    pause
    mia "Oh it’s the girl's group chat! Can I respond?"
    scene fs miaphase1sex4
    player "Hmmm...yeah go ahead. It’s kinda hot to know you’re talking to them casually when I’m inside you."
    scene fs miaphase1sex4B
    mia "{cps=25}Guess who got her phone back!!?{/cps}"
    ava "{cps=25}Omg no way! Where was it?{/cps}"
    emily "{cps=25}That’s great Mia, I know you were worried about it.{/cps}"
    mia "{cps=25}[povname] found it at the library today.{/cps}"
    sophia "{cps=25}Wow so he really found it!{/cps}"
    charlotte "{cps=25}Take a selfie girl!{/cps}"
    scene fs miaphase1sex5B
    mia "{cps=25}Haha Okay!{/cps}"
    show phoneselfie miavictory:
        xalign 0.9 yalign 0.4
    with flash
    window hide
    pause
    #Mia takes a selfie with you ploughing her in the background
    sophia "{cps=25}Omg is that...{/cps}"
    ava "{cps=25}HAHAHAHA{/cps}"
    ava "{cps=25}Didn’t think you were so bold Mia!{/cps}"
    scene fs miaphase1sex6B
    with hpunch
    show phoneselfie miavictory:
        xalign 0.9 yalign 0.4
    voice "audio/miagameaudio/miaah.wav"
    mia "Waaaah!"
    mia "{cps=25}Oh my god I’m so sorry!{/cps}"
    olivia "{cps=25}Wow.{/cps}"
    charlotte "{cps=25}Wait are you having sex RIGHT NOW??!{/cps}"
    scene fs miaphase1sex6
    player "What happened?"
    scene fs miaphase1sex6B
    mia "I accidently took a selfie with you in it behind me and and w-we’re-"
    scene fs miaphase1sex6
    player "Wait you just sent the girls a picture of me fucking you?!"
    scene fs miaphase1sex6B
    mia "YES! I don’t know how to delete it!"
    scene fs miaphase1sex6
    player "So they’re looking at me with my cock inside you right now?!"
    scene fs miaphase1sex6B
    mia "YES!"
    #player pounds mia really hard and fast
    scene fs miaphase1sex7 at fuckleft
    voice "audio/miagameaudio/miadoggystlye2.wav"
    mia "AHNNNN W-What are you d-AH doing!?"
    player "I’m so turned on right now baby j-just let me-"
    player "AH FUCK YES HERE IT COMES!"
    mia "OH GODDDD I’m cumming!"
    scene fs miaphase1sex7
    with vpunch
    #player grabs and pulls mia back as they cum together
    mia "W-w-wait the phone i-is slipping!"
    scene fs miaphase1sex8
    with flash
    # camera flashes
    show phoneselfie miacum:
        xalign 0.9 yalign 0.4
    with  flash
    window hide
    pause
    sophia "{cps=25}Another one?!{/cps}"
    ava "{cps=25}Holy shit are you two cumming together?{/cps}"
    emily "{cps=25}This is really inappropriate I think Mia...{/cps}"
    ava "{cps=25}It’s fucking hot Em is what it is!{/cps}"
    olivia "{cps=25}Yeah it is pretty hot.{/cps}"
    charlotte "{cps=25}Mia you HAVE to tell me about this later okay?{/cps}"
    ava "{cps=25}Hoho me too!{/cps}"
    sophia "...."
    mia "{cps=25}I gotta go girls I’m so sorry about this.{/cps}"
    hide phone
    player "Hah...hah. That was really something huh?"
    scene fs blackblank
    with Dissolve(0.8)
    mia "It was so embarrassing!"
    player "Not for me!"
    mia "They’re not your friends! They’re your girlfriend’s friends!"
    #they both look at the camera
    player "Heh."
    player "Well maybe one day they can be! I just met them."
    mia "Ooooh you know that’s not what I meant... "
    player "I know, I’m sorry. I’m sure it’ll be fine Mia, it was an accident and I’m sure your friends are mature enough to realize that."
    mia "Well...maybe some of them hehe."
    player "Hah, anyways don’t worry about it they know we’re dating and that we do this right?"
    mia "Yeah Okay...just...give me a second to catch my breath..I'm *Yaaaaawn*.."
    mia "Weally...sleepy...no..w...."
    scene fs miaphase1sex9
    with Dissolve(1.0)
    $ renpy.notify("Got Some Pictures!")
    $ phone_pictures.append("mia selfie 2")
    $ phone_pictures.append("mia selfie 3")
    player "Annnnd she's out."
    player "Hmmmm..."
    #$ hiden_textbox = False

    menu:
        "Take a dick pick with Mia's phone":
            jump takeadickpic
        "Snuggle":
            jump snugglewithmia

    label snugglewithmia:
        player "You wanna snuggle then?"
        mia "Yesh please."
        window hide
        pause
        scene fs miasexsnuggle1
        with Dissolve(1.2)
        window hide
        pause
        $ hiden_textbox = True

        mia "{i}I have to admit the sex was great though.{/i}"
        scene fs miasexsnuggle1mia
        mia "[povname]?"
        scene fs miasexsnuggle1mc
        player "Yeah?"
        scene fs miasexsnuggle1mia
        mia "I love you."
        scene fs miasexsnuggle1mc
        player "I love you too Mia."
        scene fs miasexsnuggle1
        player "...."
        scene fs miasexsnuggle1mc
        player "Your pussy was fire by the wa-"
        scene fs miasexsnuggle1mia
        mia "Don’t ruin it."
        scene fs miasexsnuggle1mc
        player "Yup okay sorry."
        $ miaphase1interaction3 = 5
        #$ hiden_textbox = False
        if currentchapter == 1:
            $ miaquestlog = "I should wait until after the track meet."
        else:
            $ miaquestlog = "I wonder if I should bring anyone else along with me to Mia's shopping trip..."
        hide fs miaphase1sex9
        jump gotosleep

    label takeadickpic:
        $ renpy.notify("Got A Dick Pic!")
        $ phone_pictures.append("mc new dick Bv2")
        player "{i}Since the girls never really had an angle of the goods I should give them something nice.{/i}"
        with flash
        show phoneselfie mcdickpic:
            xalign 0.9 yalign 0.4
        window hide
        pause
        player "{cps=25}Hope you girls enjoyed the show! Have a good night.{/cps}"
        scene fs parknight
        with Dissolve(1.0)
        show fbava phoneblush:
            xalign 0.5 ypos 150
        with Dissolve(0.5)
        ava "Holy shit [povname]..."
        scene fs schoolhallway2night
        with Dissolve(1.0)
        show fbemily phoneblush:
            xalign 0.5 ypos 150
        with Dissolve(0.5)
        emily "Oh my God...Does Mia know he did this?"
        scene fs sophiahouseoutsidenight
        with Dissolve(1.0)
        show fbsophia phoneblush:
            xalign 0.5 ypos 150
        with Dissolve(0.5)
        sophia "Of COURSE it's massive UGGGH!"
        scene fs charlotteroom
        with Dissolve(1.0)
        show fbcharlotte phoneblush:
            xalign 0.5 ypos 150
        with Dissolve(0.5)
        charlotte "Mia had that entire thing inside her!!?"
        scene fs arcade
        with Dissolve(1.0)
        show fbolivia phonelook:
            xalign 0.5 ypos 150
        with Dissolve(0.5)
        olivia "....."
        scene fs miaphase1sex9
        with Dissolve(0.8)
        player "Hehe they've all seen it but nobody's re-"
        scene fs miaphase1sex10
        olivia "{cps=25}Nice.{/cps}"
        player "...."
        scene fs miaphase1sex9
        player "Almost nobody's responding. Bet I know what they're thinking though."
        window hide
        pause

        #Transition to snuggle scene

        scene fs miasexsnuggle1
        with Dissolve(1.2)
        window hide
        pause
        $ hiden_textbox = True

        mia "{i}Mmmmm he's so comforting.{/i}"
        scene fs miasexsnuggle1mia
        mia "[povname]?"
        scene fs miasexsnuggle1mc
        player "Yeah?"
        scene fs miasexsnuggle1mia
        mia "I love you."
        scene fs miasexsnuggle1mc
        player "I love you too Mia."
        scene fs miasexsnuggle1
        player "...."
        scene fs miasexsnuggle1mc
        player "Your pussy was fire by the wa-"
        scene fs miasexsnuggle1mia
        mia "Don’t ruin it."
        scene fs miasexsnuggle1mc
        player "Yup okay sorry."
        $ miaphase1interaction3 = 5
        if currentchapter == 1:
            $ miaquestlog = "I should wait until after the track meet."
        else:
            $ miaquestlog = "I wonder if I should bring anyone else along with me to Mia's shopping trip..."
        #$ hiden_textbox = False
        hide fs miaphase1sex9







        # This scene then transitions to katie scene where she stumbles upon the dick pic
        scene fs gfhouse
        with Dissolve(1.0)
        show fbkatie phonelook:
            xalign 0.5 ypos 150
        with Dissolve(0.5)
        katie "Hmm? Oh it's sis's group chat again, bet they forgot I was added to that."
        show fbkatie phoneblush
        with Dissolve(0.5)
        katie "WOAH. Hellooooo there handsome. Haha oh man sis your clumsiness is second to none."
        show fbkatie phonelook
        katie "I'm going to have to ask her to share this peace of pie...or maybe just take a bite myself..."
        hide window
        pause
        scene blackblank
        with Dissolve(1.0)
        $ miaphase1interaction3 = 5
        hide fs blackblank
        hide fbkatie phonelook
        hide fbolivia
        hide fbcharlotte
        hide fbsophia
        hide fbava
        hide fbemily
        jump gotosleep

# end chapter 1

# chapter 2
# start

label gohomemia:
        show fbava runfliptalk:
            xalign 0.2 ypos 120
        show fbcharlotte current:
            xalign 0.3 ypos 120
        ava "Thanks again for coming out and cheering you guys."
        ava "Seriously it means a lot to me."
        show fbava runflip:
            xalign 0.2 ypos 120
        $ emilySprite = 1
        emily "You're more than welcome Ava!"
        $ emilySprite = 0
        $ miaSprite = 1
        mia "It was no problem!"
        $ miaSprite = 0
        show fbava runfliptalk:
            xalign 0.2 ypos 120
        ava "And man Mia I didn't know you could cheer like that! Loudest I think I've ever heard you."
        show fbava runflip:
            xalign 0.2 ypos 120
        $ miaSprite = 10
        mia "O-Oh well you know...just trying to support you."
        $ miaSprite = 12
        $ playerSprite = 13
        player "Hahaha!"
        $ playerSprite = 0
        mia "..."
        $ avaSprite = 2
        show fbava current:
            xalign 0.15 ypos 120
        "Everyone" "?"
        $ playerSprite = 12
        $ sophiaSprite = 0
        player "Sorry *ahem*."
        $ playerSprite = 0
        player "{i}I've never seen Mia this mad before, she's so cute!{/i}"
        $ charlotteSprite = 11
        show fbcharlotte current:
            xalign 0.3 ypos 120
        show fbava runflip:
            xalign 0.2 ypos 120
        charlotte "Anyways I think I'm going to head out girls! Congratulations again Ava."
        $ charlotteSprite = 0
        hide fbcharlotte current
        with Dissolve(0.7)
        show fbava runfliptalk:
            xalign 0.2 ypos 120
        ava "Bye Charlotte!"
        ava "Think I'm going to follow suite, I need a shower BAD! See yah!"
        show fbava runflip:
            xalign 0.2 ypos 120
        $ emilySprite = 1
        emily "Bye!"
        $ emilySprite = 0
        $ oliviaSprite = 1
        olivia "Bye."
        $ oliviaSprite = 0
        hide fbava
        with Dissolve(0.7)
        $ sophiaSprite = 2
        show fbsophia current at surpriseshake:
            xalign 0.5 ypos 120
        sophia "Oh shoot! Wait Charlotte can your driver take me home??!"
        hide fbsophia current
        with Dissolve(0.7)

        $ oliviaSprite = 9
        show fbolivia current at surpriseshake:
            xalign 0.8 ypos 120
        olivia "Gah! I forgot I pre-ordered that new Kerokero game! It arrives today!!"
        olivia "Sorry I gotta go."
        hide fbolivia current
        with Dissolve(0.5)
        $ playerSprite = 1
        player "Geez one right after another, okay bye."
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Oh there she goes."
        emily "Well looks like everyone's headed home then, are you two headed back together?"
        $ emilySprite = 0
        $ playerSprite = 1
        player "We-"
        $ playerSprite = 1
        show fbmia talkflip:
            xalign 0.7 ypos 120
        with move
        mia "Yes."
        show fbmia talkflip:
            xalign 0.7 ypos 120
        $ emilySprite = 2
        mia "We are."
        show fbmia defaultflip:
            xalign 0.7 ypos 120
        $ emilySprite = 1
        emily "Mind if I j-"
        show fbmia talkflip:
            xalign 0.75 ypos 120
        with move
        $ emilySprite = 2
        mia "I'll see you back at school Emily."
        show fbmia defaultflip:
            xalign 0.75 ypos 120
        $ emilySprite = 2
        emily "Um..."
        show fbmia talkflip:
            xalign 0.8 ypos 120
        with move
        mia "Be safe!"
        show fbmia defaultflip:
            xalign 0.8 ypos 120
        $ emilySprite = 1
        emily "O-Okay I'll uh go then. See yah..."
        $ emilySprite = 0
        $ playerSprite = 8
        show fbplayer current:
            xalign 0.1 ypos 120
        with move
        player "Bye...."
        hide fbemily current
        with Dissolve(0.7)
        $ playerSprite = 0
        $ miaSprite = 12
        show fbmia current:
            xalign 0.8 ypos 120
        window hide
        pause
        $ playerSprite = 14
        show fbmia current:
            xalign 0.65 ypos 120
        with move
        mia "...."
        show fbmia current:
            xalign 0.55 ypos 120
        with move
        $ playerSprite = 15
        player "What?"
        $ playerSprite = 14
        show fbmia current:
            xalign 0.4 ypos 120
        with move
        mia "Grrr!"
        $ playerSprite = 15
        player "Why are you looking at me like that what's wrong?"
        $ playerSprite = 14
        $ miaSprite = 13
        mia "What's WRONG is that you made me HORNY!"
        $ miaSprite = 12
        $ playerSprite = 1
        player "Haha oh well th-"
        $ playerSprite = 0
        $ miaSprite = 13
        mia "And I had an orgasm in front of a bunch of people!"
        $ miaSprite = 12
        $ playerSprite = 8
        player "Sorry babe I just got really worked up from you sitting on me and everytime you moved y-"
        $ miaSprite = 11
        $ playerSprite = 14
        show fbmia current:
            xalign 0.32 ypos 120
        mia "No! No more talking. We are going to your house."
        mia "Right now!"
        $ miaSprite = 12
        show fbmia current:
            xalign 0.4 ypos 120
        $ playerSprite = 15
        player "Okay..."
        $ playerSprite = 14
        $ miaSprite = 11
        show fbmia current:
            xalign 0.32 ypos 120
        mia "And you're going to fuck me until I'm satisfied."
        $ miaSprite = 12
        show fbmia current:
            xalign 0.4 ypos 120
        $ playerSprite = 13
        player "Okay!"
        $ playerSprite = 11
        $ miaSprite = 13
        mia "Don't be so happy mister, it's going to be a long night!"
        $ miaSprite = 12
        player "{i}Ho. Lee.{/i}"
        $ playerSprite = 13
        player"{i}Shit.{/i}"
        scene fs blackblank
        with Dissolve(1.0)
        window hide
        pause
        scene fs endchaptermia4
        with hpunch
        mia "AHH!"
        scene fs endchaptermia3
        with hpunch
        mia "OHH!"
        scene fs endchaptermia4
        with hpunch
        mia "AHN!"
        scene fs endchaptermia3
        with hpunch
        mia "H-Harder!"
        $ hiden_textbox = True
        scene fs endchaptermia6
        mia "Hah!"
        scene fs endchaptermia5
        with hpunch
        mia "AHHHNN!"
        scene fs endchaptermia6
        player "You like it don't you?? You like this big fucking dick!"
        scene fs endchaptermia5
        with hpunch
        mia "AHHHNN!"
        mia "YESSS!"
        scene fs endchaptermia1
        with Dissolve(0.7)
        mia "[povname]..."
        player "You're beautiful Mia."
        scene fs endchaptermia2
        with vpunch
        mia "OHHH!!"
        mia "I'm cumming!!"
        #$ hiden_textbox = False
        scene fs blackblank
        window hide
        pause

        show miaendchapterfuck1 movie
        player "Yeah...yeah just like that."
        show miaendchapterfuck2 movie
        player "Feels good baby?"
        mia "Y-Yeah..."
        show miaendchapterfuck4 movie
        mia "AHN..S-So big..."
        show miaendchapterfuck5 movie
        player "God I can't get enough of this fucking pussy!"
        mia "G-Go deeper! CUM INSIDE OF ME!"
        show miaendchapterfuck6 movie
        mia "AHN!!! YES YES!!!"
        player "I'm gonna cum Mia!!"
        window hide
        pause
        show miaendchapterfuck3 movie
        mia "[povname]!!!"
        player "AHHH YES!"
        hide miaendchapterfuck3 movie
        scene fs miasexlastframe
        with Dissolve(1.0)
        player "Fucking filling up your womb!"
        mia "Ohhh..."
        window hide
        pause
        scene fs endchaptermia8
        with Dissolve(1.0)
        mia "Hah...hah..."
        player "Fuck me..."
        mia "Wow!"
        scene fs endchaptermia7
        with Dissolve(0.5)
        player "You alright baby?"
        mia "Yes! That was...just incredible [povname]."
        player "Hehe, so you're 'satisfied'?"
        mia "VERY satisfied hehe."
        player "That..phew..is good."
        mia "Can I stay with you tonight?"
        scene fs blackblank
        with Dissolve(0.7)
        player "I wouldn't have it any other way."


        "Kyle Mercury" "Congratulations you've finished Chapter One!"
        $ endchapter1_trigger = "1 mia neutral"
        jump startofchapter2

# interaction 1
# part 1

label miaphase2interaction1part1:
    hide screen mia_room
    hide screen backbuttonGFHALLWAY
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbmia current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ miaSprite = 1
    mia "[povname] hey!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Hey Mia."
    $ miaSprite = 1
    $ playerSprite = 0
    mia "Are you ready to go to the mall?"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Yeah I'm good to go!"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Is anyone else gonna join us?"
    "You can only bring one girl along with you"
    $ CharsLeftToUnlock = ""
    if not (charlottephase1interaction2 >= 4 and charlottephase2interaction1 >= 3):
        $ CharsLeftToUnlock += ", Charlotte"
    if not (oliviaphase1interaction3 >= 2 and oliviaphase2interaction1 >= 2):
        $ CharsLeftToUnlock += ", Olivia"
    if not (avaphase1interaction1 >= 6 and avaphase2interaction1 >= 1):
        $ CharsLeftToUnlock += ", Ava"
    if not (sophiaphase1interaction2 >= 2 and sophiaphase2interaction1 >= 2):
        $ CharsLeftToUnlock += ", Sophia"
    if not (emilyphase1interaction2 >= 5 and emilyphase2interaction1 >= 5):
        $ CharsLeftToUnlock += ", Emily"
    if CharsLeftToUnlock != "":
        "Rgbcat" "Note: You haven't unlocked all the characters for this interaction yet."
        "Rgbcat" "You're currently missing[CharsLeftToUnlock]."
    $ miaSprite = 0
    menu:
        "Charlotte" if charlottephase1interaction2 >= 4 and charlottephase2interaction1 >= 3:
            jump malltripwithcharlotte
        "Olivia" if oliviaphase1interaction3 >= 2 and oliviaphase2interaction1 >= 2:
            jump malltripwitholivia
        "Ava" if avaphase1interaction1 >= 6 and avaphase2interaction1 >= 1:
            jump malltripwithava
        "Sophia" if sophiaphase1interaction2 >= 2 and sophiaphase2interaction1 >= 2:
            jump malltripwithsophia
        "Emily" if emilyphase1interaction2 >= 5 and emilyphase2interaction1 >= 5:
            jump malltripwithemily
        "Nobody Else":
            jump malltripwithmia

label malltripwithcharlotte:
    $ miaSprite = 1
    mia "Okay let's go!"
    $ playerSprite = 1
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    player "Woah wait up!"
    hide fbplayer current
    scene fs mall
    with Dissolve(0.7)
    "It doesn't take long for the two of you to get to the mall"
    "Mia talked about going clubbing, the upcoming talent show and a potential sleepover at Charlotte's house and other things they've all planned to do in the upcoming weeks"

    scene fs blackblank
    with Dissolve(0.7)
    "She took you through the mall to a section you've never been to before, mainly because it was mostly women's wear"
    "Eventually she found the store she was looking for and went in"
    "You knew Mia was going to take a long time so you walked around and browsed for a bit"

    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "{i}Alright I should probably be good to go back now.{/i}"
    player "{i}I wonder if Charlotte made it to the mall?{/i}"
    hide fbplayer current
    scene fs charlottechangeroomfeet
    with Dissolve(0.5)
    player "This should be the right place right?"
    player "I didn't see anyone around the store so they must be-"
    charlotte "Hmph!"
    player "Ah."
    player "I'd recognize that scoff anywhere!"
    scene fs charlottechangeroom1
    with Dissolve(0.7)
    charlotte "Look at yourself Charlotte!"
    charlotte "You're the very picture of womanly beauty!"
    charlotte "You don't need big boobs or parential love to live your best life!"
    scene fs charlottechangeroom2
    player "What we doing?"
    charlotte "Confidence training."
    player "Confidence training?"
    charlotte "I read about it in a self hel-"
    scene fs charlottechangeroom3
    with vpunch
    charlotte "Gah!!"
    mia "Charlotte you okay?"
    scene fs charlottechangeroom3b
    charlotte "Y-Yes Mia just stubbed my toe sorry!"
    charlotte "S-Still got a lot to try on."
    mia "Okidoke!"
    charlotte "...."
    scene fs charlottechangeroom4
    player "Hehe, hey."
    scene fs charlottechangeroom4b
    charlotte "{size=-10}What are you doing here??{/size}"
    scene fs charlottechangeroom4
    player "Training confidence?"
    scene fs charlottechangeroom4b
    charlotte "I'm serious Mia's in the next room!"
    charlotte "{size=-10}A-And keep your voice down!{/size}"
    scene fs charlottechangeroom5
    player "Listen Charlotte, it might not mean much coming from me but you are very beautiful you know."
    player "This self-help stuff is fine but take it from a secondary observer. You got it going on."
    charlotte "{i}He did not just say 'you got it going on'.{/i}"
    charlotte "{i}Though the sentiment is nice..{/i}"
    player "Let me prove it to you."
    scene fs charlottechangeroom6
    charlotte "W-Woah hey what are you doing??"
    charlotte "{i}I forgot that I'm completely naked!{/i}"
    scene fs charlottechangeroom7
    charlotte "{size=-10}Mia might hear us!{/size}"
    player "Mmhm."
    charlotte "{i}F-Fuck this is kinda hot..{/i}"
    scene fs charlottechangeroom7b
    charlotte "Oh!!"
    mia "Charlotte?"
    charlotte "I-It's fine Mia."
    scene fs charlottechangeroom7c
    charlotte "That...ahn..damn toe again."
    mia "Geez you're more clumsy today than me! You gotta be more aware of what's going on around you Charlotte!"
    scene fs charlottechangeroom7d
    charlotte "Yeah....fuck!"
    charlotte "{i}He's so good with his tongue ugh!{/i}"
    scene fs charlottechangeroom8
    pause
    player "Mmmm.."
    charlotte "{size=-10}D-Don't look at me like that...{/size}"
    scene fs charlottechangeroom8b
    player "Mmmhmm."
    charlotte "{size=-10}Ohmygod that's worse!{/size}"
    charlotte "Fuck fuck fuck I'm going to-"
    scene fs charlottechangeroom8c
    with vpunch
    charlotte "AHHN!!"
    charlotte "{i}I'm cumming while Mia's just on the other side of this wall!{/i}"
    scene fs charlottechangeroom7d
    with Dissolve(0.5)
    charlotte "{i}Her boyfriend's tongue is...is!!{/i}"
    charlotte "{i}God this is so hot I'm gonna cum again!{/i}"
    scene fs blackblank
    with Dissolve(0.7)
    "A little while later..."
    scene fs mall
    with Dissolve(0.7)
    $ charlotteSprite = 5
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbcharlotte current:
        xalign 0.5 ypos 120
    show fbmia current:
        xalign 0.65 ypos 120
    with Dissolve(0.7)
    $ miaSprite = 1
    mia "Well that was fun!"
    $ miaSprite = 0
    $ charlotteSprite = 13
    charlotte "Y-Yeah.."
    $ charlotteSprite = 5
    $ playerSprite = 1
    player "I had a good time!"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Haha waiting outside for us was a good time?"
    $ miaSprite = 0
    player "...."
    $ playerSprite = 1
    player "Yup."
    $ playerSprite = 0
    charlotte "..."
    $ playerSprite = 16
    player "Shall we go?"
    $ playerSprite = 0
    $ miaSprite = 5
    mia "Yeah! I'm satisfied with my visit, how about you Charlotte?"
    $ miaSprite = 0
    $ charlotteSprite = 8
    charlotte "Yeah um..."
    $ charlotteSprite = 13
    charlotte "V-Very satisfied."
    $ charlotteSprite = 5
    $ playerSprite = 13
    player "Hehe."
    $ playerSprite = 0

    jump passtime

label malltripwitholivia:
    $ playerSprite = 1
    player "Olivia said she could make it."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Okay let's go! We'll meet her there then!"
    $ playerSprite = 1
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    player "Woah wait up!"
    hide fbplayer current
    scene fs mall
    with Dissolve(0.7)
    "It doesn't take long for the two of you to get to the mall"
    "Mia talked about going clubbing, the upcoming talent show and a potential sleepover at Charlotte's house and other things they've all planned to do in the upcoming weeks"

    scene fs blackblank
    with Dissolve(0.7)
    "She took you through the mall to a section you've never been to before, mainly because it was mostly women's wear"
    "Eventually she found the store she was looking for and went in"
    "You knew Mia was going to take a long time so you walked around and browsed for a bit"

    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "{i}Alright I should probably be good to go back now.{/i}"
    player "{i}I wonder if Olivia made it to the mall?{/i}"
    hide fbplayer current
    scene fs oliviachangeroomfeet
    with Dissolve(0.5)
    player "Hmm both of these changerooms seem occupied, and I don't see the girls in the store anywhere."
    mia "La dee da..."
    player "Ah, Mia's in the one on the right..."
    scene fs oliviachangeroom1
    with Dissolve(0.7)
    olivia "Hmm..."
    scene fs oliviachangeroom2
    pause
    scene fs oliviachangeroom3
    pause
    scene fs oliviachangeroom2
    pause
    scene fs oliviachangeroom3
    pause
    scene fs oliviachangeroom2b
    olivia "Have they gotten bigger?"
    scene fs oliviachangeroom4
    with Dissolve(0.7)
    player "I can check if you want."
    scene fs oliviachangeroom5
    with Dissolve(0.7)
    olivia "[povname]?"
    player "Hey."
    olivia "Why are you in here? I'm naked."
    player "I'm quite aware."
    scene fs oliviachangeroom6
    player "There's no way I can miss this opportunity."
    olivia "M-Mia is right next door."
    scene fs oliviachangeroom6b
    player "Then we should be extra quiet."
    scene fs oliviachangeroom6
    olivia "..."
    scene fs oliviachangeroom6b
    pause
    scene fs oliviachangeroom7
    "*ziiiip*"
    olivia "{i}What is he doing?{/i}"
    scene fs oliviachangeroom8
    player "There's no way I can leave these amazing thighs unfucked."
    scene fs oliviachangeroom12
    with Dissolve(0.7)
    olivia "{i}Oh man I thought he was gonna put it inside me..{/i}"
    scene fs oliviachangeroom13
    with Dissolve(0.7)
    olivia "{i}T-This is still...pretty good..{/i}"
    scene fs oliviachangeroom14
    with Dissolve(0.7)
    olivia "{i}Don't make a sound Olivia, no matter how good this feels!{/i}"
    scene fs oliviachangeroom9
    olivia "Ah..."
    scene fs oliviachangeroom10
    with hpunch
    olivia "UHHN!!"
    olivia "{i}So much for that.{/i}"
    scene fs oliviachangeroom9
    mia "Olivia?"
    scene fs oliviachangeroom10
    with hpunch
    olivia "AH!"
    olivia "Y-Yeah?"
    scene fs oliviachangeroom9
    mia "Are you okay?"
    scene fs oliviachangeroom10
    with hpunch
    olivia "YES!"
    olivia "Yes I'm fine, just thought of something embarrassing that happened years ago!"
    scene fs oliviachangeroom9
    mia "Oh I hate when that happens!"
    mia "Alrighty then."
    scene fs oliviachangeroom10
    with hpunch
    olivia "Haaaa!"
    image thighfuckoliviachange1:
        "changeroom olivia9.png"
        0.7
        "changeroom olivia10.png"
        0.7
        repeat
    show thighfuckoliviachange1
    olivia "{i}Uggggh why does he do these things to me???{/i}"

    image thighfuckoliviachange2:
        "changeroom olivia9.png"
        0.2
        "changeroom olivia10.png"
        0.2
        repeat
    show thighfuckoliviachange2
    olivia "Ahh fuck!"
    mia "Wow it must've been pretty bad huh?"
    player "{size=-10}Olivia I'm gonna cum!{/size}"
    olivia "M-Me too!"
    scene fs oliviachangeroom12
    with Dissolve(0.7)
    player "Oh shit!"
    scene fs oliviachangeroom15
    with hpunch
    player "MMMM!"
    scene fs oliviachangeroom11
    with hpunch
    olivia "UHN!!"
    scene fs oliviachangeroom16
    with Dissolve(1.0)
    olivia "Hah...hah..."
    player "Hah.."
    player "{i}Hoo boy...{/i}"

    scene fs mall
    with Dissolve(1.0)

    show fbplayer current:
        xalign 0.4 ypos 120
    show fbolivia current:
        xalign 0.5 ypos 120
    show fbmia current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)

    image fbolivia blushflip = im.Flip("Sprites/olivia embarrassed B.png", horizontal = True)

    $ oliviaSprite = 8
    $ miaSprite = 1
    mia "Did you get everything you needed Olivia?"
    $ miaSprite = 0
    $ oliviaSprite = 10
    olivia "Um, yeah."
    $ miaSprite = 4
    mia "Great! Thanks for waiting for us [povname]."
    $ miaSprite = 0
    $ playerSprite = 1
    player "No problem, it was my pleasure."
    $ playerSprite = 0
    $ miaSprite = 5
    mia "You're gonna love Olivia's Bikini, really shows off her great body!"
    $ miaSprite = 0
    show fbolivia blushflip:
        xalign 0.5 ypos 120
    olivia "M-Mia. C'mon..."
    $ miaSprite = 4
    show fbolivia current:
        xalign 0.5 ypos 120
    mia "Haha I'm just teasing! C'mon let's go!"
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.7)
    player "..."
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.42 ypos 120
    with move
    player "I never did get to see it."
    $ playerSprite = 13
    $ oliviaSprite = 14
    olivia "Hehe. Shut up."

    jump passtime


label malltripwithava:
    $ playerSprite = 1
    player "Ava's gonna meet us there."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Awesome! Let's go!"
    $ playerSprite = 1
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    player "Woah wait up!"
    hide fbplayer current
    scene fs mall
    with Dissolve(0.7)
    "It doesn't take long for the two of you to get to the mall"
    "Mia talked about going clubbing, the upcoming talent show and a potential sleepover at Charlotte's house and other things they've all planned to do in the upcoming weeks"

    scene fs blackblank
    with Dissolve(0.7)
    "She took you through the mall to a section you've never been to before, mainly because it was mostly women's wear"
    "Eventually she found the store she was looking for and went in"
    "You knew Mia was going to take a long time so you walked around and browsed for a bit"

    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "{i}Alright I should probably be good to go back now.{/i}"
    player "{i}I wonder if Ava is here yet.{/i}"
    hide fbplayer current
    scene fs avachangeroomfeet
    with Dissolve(0.5)
    player "Ah, they're probably in these changerooms."
    player "I'm gonna assume the one with the...darker feet is Ava."
    player "I should have a little fun with her."
    scene fs avachangeroom1
    with Dissolve(0.7)
    ava "Hmmm.."
    scene fs avachangeroom1b
    ava "Yeah there's no way I can pull off something girly like this."
    scene fs avachangeroom2
    ava "{i}Pink is not my color.{/i}"
    scene fs avachangeroom2b
    player "I think you'd look great."
    scene fs avachangeroom3
    ava "Huh??"
    scene fs avachangeroom4
    with hpunch
    ava "What? Dude!"
    ava "What are you doing here??"
    scene fs avachangeroom4c
    mia "You say something Ava?"
    scene fs avachangeroom4d
    ava "N-No Mia it's fine, just t-talking to myself!"
    scene fs avachangeroom4c
    mia "Oh alrighty! I do that all the time!"
    scene fs avachangeroom4b
    player "You really should be a little more confident in yourself Ava."
    player "You have incredible feminine appeal."
    scene fs avachangeroom4
    ava "O-Ok thank you but Mia is right in the next room!"
    ava "We can't be-"
    scene fs avachangeroom5
    with Dissolve(0.5)
    ava "Ohh!!"
    image fingeravachangeroom1:
        "changeroom Ava7b.png"
        0.7
        "changeroom Ava7c.png"
        0.7
        repeat
    show fingeravachangeroom1
    with Dissolve(0.5)
    player "Can't be what?"
    ava "Ah..."
    player "Can't be fingering your pussy while your friend, MY girlfriend, is changing right next to us?"
    ava "{size=-10}Oh God...{/size}"
    player "A pussy which is incredibly wet by the way. Betraying Mia must really turn you on huh?"
    ava "{size=-10}N-No! No it d-{/size}"
    mia "What was that Ava?"
    scene fs avachangeroom7
    with vpunch
    ava "MMMMM!!!"
    mia "You still talking to yourself? Y'okay?"
    player "{size=-10}Wow, cumming while she's talking to you?{/size}"
    player "{size=-10}Maybe you're just a slut?{/size}"
    ava "Aamph f-fine Mia!"
    ava "{i}Fuck fuck fuck!{/i}"
    mia "Okay, if you say so!"
    ava "{i}What is [povname] fucking doing to me?{/i}"
    player "{size=-10}I'll step out now. Don't wanna get caught now do we?{/size}"
    scene fs blackblank
    with Dissolve(1.0)
    "You sneakily exit the changeroom and meet the two girls later outside the store"
    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    $ avaSprite = 12
    $ miaSprite = 0
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbmia current:
        xalign 0.5 ypos 120
    show fbava current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ miaSprite = 1
    mia "Well that was a lot of fun! Wasn't it Ava?"
    $ miaSprite = 0
    $ avaSprite = 14
    ava "Um...y-yeah."
    $ avaSprite = 12
    $ playerSprite = 1
    player "Glad you enjoyed yourself Ava."
    $ playerSprite = 0
    $ avaSprite = 14
    ava "...."
    $ miaSprite = 5
    $ avaSprite = 12
    mia "I think you'll really like my bikini [povname], it's super cute!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Well with a body like yours...MIA, I really don't mind WHAT you're wearing."
    player "Girly or not, in the end I'm gonna tear it off of you...."
    $ playerSprite = 0
    $ avaSprite = 11
    ava "!!!"
    $ miaSprite = 5
    $ avaSprite = 12
    mia "Hehe [povname] shhh! Ava is right heeere!"
    $ miaSprite = 0
    $ avaSprite = 11
    ava "I...um..."
    $ avaSprite = 12
    show fbmia talkflip:
        xalign 0.5 ypos 120
    mia "He's just messing with you Ava!"
    $ avaSprite = 14
    $ miaSprite = 5
    show fbmia current:
        xalign 0.5 ypos 120
    mia "Geez [povname] you're so embarrassing sometimes!"
    $ miaSprite = 0
    $ playerSprite = 13
    player "Haha sorry."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Alrighty let's go! I wanna try my bathing suit on again at home and see if it looks the same!"
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    ava "...."
    $ avaSprite = 12
    $ playerSprite = 1
    player "I'm looking forward to the beach. Heh."
    $ playerSprite = 0
    hide fbplayer current
    with Dissolve(0.5)
    ava "...."
    $ avaSprite = 13
    ava "{i}Me too.{/i}"

    jump passtime

label malltripwithsophia:
    $ playerSprite = 1
    player "Sophia told me she's coming."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Great! We'll meet her there!"
    $ playerSprite = 1
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    player "Woah wait up!"
    hide fbplayer current
    scene fs mall
    with Dissolve(0.7)
    "It doesn't take long for the two of you to get to the mall"
    "Mia talked about going clubbing, the upcoming talent show and a potential sleepover at Charlotte's house and other things they've all planned to do in the upcoming weeks"

    scene fs blackblank
    with Dissolve(0.7)
    "She took you through the mall to a section you've never been to before, mainly because it was mostly women's wear"
    "Eventually she found the store she was looking for and went in"
    "You knew Mia was going to take a long time so you walked around and browsed for a bit"

    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "{i}Okay that should be enough wandering around.{/i}"
    "Vvvvppp!"
    player "Hmm?"
    mia "{cps=25}Sophia is here, I'm in the left stall!{/cps}"
    player "{i}Ah okay good timing, I should head back.{/i}"
    hide fbplayer current
    scene fs sophiachangeroomfeet
    with Dissolve(0.5)
    player "{i}Okay, Mia said she was in the left changeroom.{/i}"
    player "{i}I should go in and have a little fun with her hehe.{/i}"

    scene fs sophiachangeroom1
    sophia "Hmm hm hm."
    player "Hey Sexy-"
    scene fs sophiachangeroom2
    with vpunch
    player "Huh??"
    scene fs sophiachangeroom3
    sophia "...."
    player "...."
    scene fs sophiachangeroom3b
    sophia "Hehehe."
    scene fs sophiachangeroom3c
    player "Oh no no no."
    player "{size=-10}It's not what you think!{/size}"
    player "{size=-10}I thought Mia was in here.{/size}"
    scene fs sophiachangeroom4
    sophia "You're saying.."
    player "{i}Ah shit her tits are out.{/i}"
    sophia "That even though you've denied me so many times and said you're not interested."
    sophia "You just waltz right in here without even checking?"
    scene fs sophiachangeroom5
    with Dissolve(0.7)
    sophia "I ain't buying it."
    player "{size=-10}Sophia could you keep your voice down??{/size}"
    image sophiachangeroomhj1:
        "changeroom sophia6.png"
        0.7
        "changeroom sophia6b.png"
        0.7
        repeat
    show sophiachangeroomhj1
    sophia "If you want to see your childhood friend naked, all you have to do is ask."
    player "{size=-10}Please don't say shit like that.{/size}"
    player "{size=-10}Ah fuck...{/size}"
    sophia "So girthy..."
    scene fs sophiachangeroom7
    with Dissolve(0.7)
    sophia "God I just have to taste it!"
    scene fs sophiachangeroom8
    mia "Soph? You say something?"
    player "!!!"
    sophia "Nothing Mia! I'm just excited to shove some fat cock down my throat."
    mia "Hahaha what? Geez you're so silly sometimes!"
    scene fs sophiachangeroom9
    sophia "Ahn huh."
    scene fs sophiachangeroom10
    sophia "Mmmm."
    mia "You normally don't make dirty jokes like that."
    scene fs sophiachangeroom11
    sophia "*Gulk*"
    player "{i}Ah fuck she must've been practicing..{/i}"
    mia "[povname] actually likes talking dirty like that while we're having sex!"
    scene fs sophiachangeroom11b
    player "Hah...hah."
    player "{i}She's sucking harder!{/i}"
    mia "He can get really rough! But I guess that's not really joking though."
    scene fs sophiachangeroom12
    with hpunch
    sophia "UGGHK!"
    player "{i}Fuck fuck fuck fuck!{/i}"
    scene fs sophiachangeroom13
    player "{size=-10}Sophia I'm gonna cum!!{/size}"
    scene fs sophiachangeroom14
    mia "I really do like it though, I mean who wouldn't?"
    mia "Hehe I hope after he sees me in this bikini at the beach he'll give me a good time!"
    mia "He cums a lot you know!"
    scene fs sophiachangeroom15
    with hpunch
    player "UUUUGHHH!!"
    scene fs sophiachangeroom16
    mia "I mean like more than your average guy I think. Like loads!"
    sophia "Ahhhh....yeah? I wouldn't know hehe."
    scene fs blackblank
    with Dissolve(1.0)
    "You quickly zip yourself up and head out of the store quietly"
    "After the girls bought their stuff and left you met up with them"
    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    show fbmia current:
        xalign 0.6 ypos 120
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    $ miaSprite = 1
    mia "Sorry I was such a chatterbox in the store Sophia."
    mia "I felt like it was just me talking the whole time, you couldn't get a word in!"
    $ miaSprite = 0
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    sophia "Hehe it's okay Mia! I didn't mind you talking while I was preoccupying myself."
    sophia "{size=-10}It was really hot.{/size}"
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    mia "Hmm?"

    $ playerSprite = 1
    show fbplayer current:
        xalign 0.4 ypos 120

    $ sophiaSprite = 0
    show fbsophia current:
        xalign 0.5 ypos 120

    player "Hey!"
    $ playerSprite = 16
    player "What a...what you girls talking about?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "[povname]! You finally showed up!"
    mia "I was expecting to see you in the store! Geez."
    $ miaSprite = 0
    $ playerSprite = 16
    player "I did! Uh, I mean.."
    player "Your instructions were wrong?"
    $ playerSprite = 15
    $ miaSprite = 2
    player "You said the left changeroom bu-"
    $ playerSprite = 11
    player "{i}Wait shit I can't let her know I went into Sophia's changeroom!{/i}"
    $ playerSprite = 14
    $ miaSprite = 3
    mia "Huh? No I was right! I said I was in the stall to left!"
    mia "MY left!"
    $ miaSprite = 2
    $ playerSprite = 15
    player "Wait...YOUR left?"
    $ playerSprite = 14
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    sophia "Hehehehe."
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 1
    mia "What's so funny?"
    $ miaSprite = 0
    $ playerSprite = 16
    show fbsophia current:
        xalign 0.5 ypos 120
    player "Mia why would you say it from that perspective??"
    $ playerSprite = 8
    $ miaSprite = 1
    mia "I'M the one talking! Why wouldn't I say it from MY perspective huh??"
    $ miaSprite = 4
    $ playerSprite = 11
    mia "Geez you two!"
    $ miaSprite = 0
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    sophia "Haha what did I do?"
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 1
    mia "I don't know I just have the feeling that you've been bad too!"
    $ miaSprite = 0
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    sophia "Uh....nope!"
    $ sophiaSprite = 1
    show fbsophia current:
        xalign 0.5 ypos 120
    sophia "Isn't that right [povname]?"
    $ sophiaSprite = 0
    $ playerSprite = 16
    player "L-Let's just get out of here huh?"
    scene fs blackblank
    with Dissolve(1.0)
    $ miaSprite = 1
    mia "Fine fine, I hope you appreciate the bikini I got for the beach [povname]."
    $ miaSprite = 0
    $ playerSprite = 16
    player "I'm sure I will!"
    $ playerSprite = 8
    player "....."
    $ playerSprite = 11
    pause
    jump passtime


label malltripwithemily:
    $ playerSprite = 1
    player "Emily said she could come!"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Yay! This is gonna be a lot of fun!"
    player "Ehhh.."
    mia "Let's go!"
    $ playerSprite = 1
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    player "Woah wait up!"
    hide fbplayer current
    scene fs mall
    with Dissolve(0.7)
    "It doesn't take long for the two of you to get to the mall"
    "Mia talked about going clubbing, the upcoming talent show and a potential sleepover at Charlotte's house and other things they've all planned to do in the upcoming weeks"

    scene fs blackblank
    with Dissolve(0.7)
    "She took you through the mall to a section you've never been to before, mainly because it was mostly women's wear"
    "Eventually she found the store she was looking for and went in"
    "You knew Mia was going to take a long time so you walked around and browsed for a bit"

    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "{i}Allllright that should be enough time for them. I wonder if Emily met Mia in the store?{/i}"

    hide fbplayer current

    scene fs emilychangeroomfeet
    with Dissolve(0.7)
    player "{i}Ah. I see two sets of beautiful feet.{/i}"
    player "{i}....{/i}"
    player "{i}Not that I'm a foot guy.{/i}"
    player "{i}I'm not.{/i}"
    player "{i}Shut up.{/i}"
    emily "*Sigh*..."
    player "{i}Ah! I recognize that breathy sigh.{/i}"
    scene fs emilychangeroom1
    with Dissolve(0.7)
    emily "{i}Have I gained weight again?{/i}"
    emily "{i}Hmmm, do guys like [povname] even like big butts?{/i}"
    emily "{i}Ugh why am I even thinking about him?{/i}"
    mia "Dum de dumm!"
    emily "{i}Probably cause Mia's here is all.{i}"
    scene fs emilychangeroom2
    with Dissolve(0.7)
    player "Hey."
    scene fs emilychangeroom2b
    emily "{i}I know he and I decided to...figure things out a bit but I'm still no-{/i}"
    ""
    scene fs emilychangeroom3
    with vpunch
    emily "AWHA?!"
    scene fs emilychangeroom4
    mia "Emily??"
    mia "Are you okay?!"
    emily "Y-Yeah Mia! Sorry I'm fine!"
    scene fs emilychangeroom3
    with Dissolve(0.5)
    emily "{size=-10}What are you doing here??{/size}"
    scene fs emilychangeroom5b
    with Dissolve(0.7)
    emily "Eh??"
    scene fs emilychangeroom5
    player "Well I knew you were changing in here."
    player "So how could I resist?"
    scene fs emilychangeroom5b
    emily "{size=-10}K-Keep your voice down!{/size}"
    scene fs emilychangeroom6
    player "I think you're the one who's gonna need to keep her voice down."
    emily "W-What do you mean?"
    image emilyfingerchangeroom1:
        "changeroom emily7a.png"
        0.7
        "changeroom emily7b.png"
        0.7
        repeat
    show emilyfingerchangeroom1
    with Dissolve(0.7)
    emily "Oh..."
    emily "O-Okay..."
    player "Hehe I can feel how wet you are baby."
    emily "{size=-10}B-Baby?{/size}"
    player "Turns you on that Mia is right next to us huh?"
    emily "{size=-10}No!...ehn..."
    player "Such a dirty little slut."

    image emilyfingerchangeroom2:
        "changeroom emily8.png"
        0.7
        "changeroom emily8b.png"
        0.7
        repeat
    hide emilyfingerchangeroom1
    show emilyfingerchangeroom2

    emily "AHHNNN!"
    mia "Emily?"
    player "{size=-10}Not even gonna deny it now?"
    mia "You sure you're okay?"
    emily "YES!"
    player "{size=-10} Fucking CUM for me my little slut!{/size}"
    mia "O-Okay if you say so..."
    emily "YES...YES!!"
    scene fs emilychangeroom9b
    with Dissolve(0.7)
    emily "MMMMPPHH!!"
    player "{i}OH?{/i}"
    player "{i}Really wasn't expecting her to kiss me!"
    player "{i}I can feel her cumming on my hand.{/i}"
    scene fs emilychangeroom10
    with Dissolve(1.0)
    emily "Hah...hah.."
    mia "You really sound...not yourself Emily?"
    emily "Sorry Mia it's fine I just.."
    emily "I'm sorry..I'm so so sorry..."
    mia "It's okay!"
    emily "{size=-10}Oh God no it's not...{/size}"
    scene fs blackblank
    with Dissolve(1.0)
    "You soon after left the changeroom and waited outside the store to meet up with the girls"
    scene fs mall
    with Dissolve(0.7)
    $ playerSprite = 0
    $ miaSprite = 1
    show fbmia current:
        xalign 0.7 ypos 120
    show fbemily upsetflip:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    mia "I think that was a success don't you?"
    $ miaSprite = 0
    emily "Mhmm yeah.."
    $ miaSprite = 1
    mia "I really think [povname] is gonna like my new bikini."
    $ miaSprite = 1
    show fbemily upsetfliptalk:
        xalign 0.5 ypos 120
    emily "T-That's great Mia."
    show fbemily upsetflip:
        xalign 0.5 ypos 120
    $ miaSprite = 1
    mia "Why do you look so down? Yours looks great too!"
    mia "You should show [povname], he'll tell you it's cute!"
    $ miaSprite = 0
    show fbemily blushfliptalk:
        xalign 0.5 ypos 120
    emily "What??"
    $ emilySprite = 2
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.4 ypos 120
    player "True, I never got to see it."
    $ playerSprite = 0
    show fbemily current:
        xalign 0.5 ypos 120
    emily "Huh??"
    $ emilySprite = 4
    $ playerSprite = 1
    player "I'm sure it's super cute like Mia said."
    $ playerSprite = 0
    $ miaSprite = 5
    mia "[povname]!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Get everything you needed?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Uh huh! I cannot WAIT for the beach hehe!"
    $ miaSprite = 0
    $ playerSprite = 13
    player "I can't either!"
    emily "...."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Alright well for now though I am POOPED. I gotta go home and take a shower."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Sounds good to me!"
    $ playerSprite = 0
    $ miaSprite = 4
    mia "Hehe you're not coming with!"
    $ miaSprite = 0
    $ playerSprite = 13
    player "Whaaat? Awww."
    $ playerSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    $ miaSprite = 1
    mia "Hehehe!"
    $ miaSprite = 1
    emily "..."
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.42 ypos 120
    with move
    player "When we get to the beach."
    $ playerSprite = 0
    emily "?"
    $ playerSprite = 1
    player "I'm gonna rip your bikini off and pound your tight little cunt until you can't fucking walk."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "W-Wha...I....I!"
    $ emilySprite = 4
    mia "[povname]? Emily?"
    $ playerSprite = 13
    player "Coming babe!"
    hide fbplayer current
    with Dissolve(0.5)
    emily "...."
    $ emilySprite = 2
    emily "God what have I become..."
    jump passtime

label malltripwithmia:
    $ playerSprite = 1
    player "Nope it's just going to be you and me babe!"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Oh okay!"
    mia "To be honest I was kinda hoping that was going to happen haha!"
    $ playerSprite = 1
    $ miaSprite = 0
    player "Oh boy, you want me all to yourself huh?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Yeah, I also want to surprise the girls with how good I look in my new swimsuit!"
    $ playerSprite = 5
    $ miaSprite = 0
    player "Wait...shouldn't...I be the one who..."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Okay let's go!"
    $ playerSprite = 1
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    player "Woah wait up!"
    hide fbplayer current
    scene fs blackblank
    with Dissolve(0.7)
    "It doesn't take long for the two of you to get to the mall"
    "Mia talked about going clubbing, the upcoming talent show and a potential sleepover at Charlotte's house and other things they've all planned to do in the upcoming weeks"
    "You listenend intently, legitimately enjoying what she was talking about"
    scene fs mall
    with Dissolve(0.7)
    "She took you through the mall to a section you've never been to before, mainly because it was mostly women's wear clothes"
    "Once she found the store she was looking for she made you wait while she browsed the swimsuit section"
    "So you waited."
    "And waited...."
    "Then finally you heard her call for you"
    scene fs miamallalone1
    with Dissolve(0.5)
    mia "[povname]!!!"
    player "I'm here I'm here!"
    player "PLEASE tell me you're done!"
    mia "I've narrowed it down to three."
    player "Oh God."
    mia "I need your help deciding though can you tell me which one you like the most?"
    player "Oh. Well yeah okay I can do that."
    mia "Okay I'm ready with the first one!"
    player "I'm ready too let's see it!"
    scene fs miamallalone2
    with Dissolve(0.5)
    mia "Okay first is this white one!"
    player "Ohhh wow okay that looks great."
    scene fs miamallalone2b
    mia "I know you're gonna say that for all of them haha."
    mia "But I still want to choose which one will surprise the girls the most!"
    scene fs miamallalone2
    mia "I've never worn one with these ribbon tassle things but it should be fine right?"
    player "Uh yeah. It'll be fine haha."
    scene fs miamallalone1
    mia "Okay next one!"
    mia "Ready?"
    player "Yes ma'am!"
    scene fs miamallalone4
    mia "Bam!"
    player "Woah! Look at you."
    scene fs miamallalone4b
    with Dissolve(0.5)
    mia "I love this one's design but I don't know if the purple works.."
    mia "What do you think? How's the back?"
    player "I...oh wow. Babe..."
    scene fs miamallalone4
    with Dissolve(0.5)
    mia "Hehe you're awful at this!"
    player "Sorry really, you're just so sexy in swimwear!"
    mia "Alright let's try the last one."
    scene fs miamallalone1
    with Dissolve(0.3)
    mia "You ready for me?"
    player "I literally cannot wait."
    scene fs miamallalone3b
    with Dissolve(0.5)
    mia "What do yah think'o this??"
    player "Ooooh, I like the green! And your ass!"
    mia "It doesn't clash with my hair?"
    player "Nope, I'm pretty sure it works."
    scene fs miamallalone3
    player "God does it work!"
    mia "Hehehe alright thank you!"
    #this is where you will make the choice between the three
    mia "So which do you like the most?"
    scene fs miamallalone1
    with Dissolve(0.3)

    show fbmiaswimsuit1:
        xalign 0.1 yalign 0.9
    show fbmiaswimsuit2:
        xalign 0.5 yalign 0.9
    show fbmiaswimsuit3:
        xalign 0.9 yalign 0.9

    pause

    menu:
        "The white one":
            jump thewhiteone
        "The purple one":
            jump thepurpleone
        "The green one":
            jump thegreenone

    label thewhiteone:
        player "I love the white one."
        $ swimsuitchoice = "white"
        jump miachangeroomscene
    label thepurpleone:
        player "I really like the purple one."
        $ swimsuitchoice = "purple"
        jump miachangeroomscene
    label thegreenone:
        player "Definitely the green one, super sexy."
        $ swimsuitchoice = "green"
        jump miachangeroomscene

label miachangeroomscene:
    hide fbmiaswimsuit1
    hide fbmiaswimsuit2
    hide fbmiaswimsuit3
    mia "Okay great! Wait there and I'll change back then go buy it!"
    player "Sounds good."
    mia "La dee da..."
    player "{i}Damn. All this waiting is killing me.{/i}"
    player "{i}And after seeing Mia in all those bikinis...{/i}"
    mia "And off my top goes! Hello there ladies."
    player "....."
    player "I'm going in."
    scene fs miamallalone5
    with Dissolve(0.7)
    mia "Dum de dum..."
    scene fs miamallalone6
    with Dissolve(0.4)
    player "Hey..."
    mia "Huh?"
    scene fs miamallalone7
    with Dissolve(0.4)
    mia "Hello handsome."
    mia "You...are not supposed to be here."
    player "Then I guess we should be quick before anyone catches us."
    mia "Hmmm."
    mia "What ever could you mean?"
    player "I want you to get on your knees."
    mia "Uh huh."
    player "And blow me till I bust all over these magnificent tits of yours."
    mia "And what do I get?"
    player "I just told you."
    mia "Hehe well when you put it like that..."
    player "Come here."
    scene fs miamallalone8a
    with Dissolve(0.4)
    player "Mmphm."
    scene fs miamallalone8b
    with Dissolve(0.5)
    mia "MMH!"
    mia "Mmmmhmmm..."
    scene fs miamallalone9
    with Dissolve(0.7)
    mia "Hehe let's take a looksee..."
    scene fs miamallalone9b
    player "Your eagerness is very appealing."
    scene fs miamallalone9c
    mia "Mmmm let's just say you got me in the mood hehe."
    mia "Now gimme dat di-"
    scene fs miamallalone9d
    with vpunch
    "*Bonk*"
    player "Haha"
    scene fs miamallalone10
    mia "Hmph. I'm not even gonna acknowledge that."
    player "That's...oh yeah..."
    scene fs miamallalone11
    player "That's fine with me."
    scene fs miamallalone12
    player "Haaaa..."
    scene fs miamallalone13
    player "That's it baby. I love it when you go deep."
    with vpunch
    mia "Uhhhgk!"
    player "Fuck! You're sucking my soul straight out my dick."
    scene fs miamallalone14
    mia "Hah..you wanna cum all over me?"
    scene fs miamallalone14b
    player "Yeah baby, but you got what it takes?"
    scene fs miamallalone14
    mia "To make you cum?"
    scene fs miamallalone14b
    player "You know I'm a very particular man. You gotta meet certain criteria if you want it."
    scene fs miamallalone14
    mia "Haha that's right."
    mia "[povname] only fucks girls with the biggest tits."
    scene fs miamallalone14b
    player "Hah..yeah that's right.."
    scene fs miamallalone14
    mia "You only cum for the girls with the prettiest faces."
    player "O-Only the prettiest!"
    mia "The most fuckable asses!"
    scene fs miamallalone14b
    player "OH fuck!"
    scene fs miamallalone14
    mia "The nicest personalities!"
    scene fs miamallalone15
    with hpunch
    player "Ahhh SHIT!"
    with flash
    scene fs miamallalone16
    player "That's it baby!"
    mia "Give it to me!"
    scene fs miamallalone17
    with Dissolve(0.5)
    player "Hah...hah.."
    mia "Ahhh..."
    player "Oh my god that was so good."
    player "You fucking drained me. Thanks for that."
    scene fs miamallalone18b
    mia "...."
    scene fs miamallalone19
    mia "Pfffft hahahaha!"
    player "What's so funny?"
    scene fs miamallalone18b
    mia "Hehe."
    scene fs miamallalone18
    mia "You came at 'nicest personality'. Haha."
    scene fs miamallalone18b
    player "Haha I guess I did."
    scene fs miamallalone18
    mia "Glad to know you don't just like me for my body!"
    scene fs miamallalone18b
    player "To secure myself against any future arguments I'm just gonna say right now I love you inside AND out."
    scene fs miamallalone18
    mia "Hehe. THAT is a smart choice."
    mia "Now let's go I wanna b-"
    "Employee" "Uh ma'am?"
    scene fs miamallalone20
    with vpunch
    mia "Huh?"
    "Employee" "Everything alright in there ma'am? I heard uh...something?"
    mia "Yes everything's fine I'll be right out!"
    scene fs miamallalone21
    pause

    scene fs miamallalone22
    mia "Dum de dum."
    "Employee" "Were you able to find everything m-"
    scene fs miamallalone23b
    "Employee" "...."
    scene fs miamallalone23
    mia "Yup! I got everything I needed!"
    "Employee" "...."
    scene fs miamallalone24
    with Dissolve(0.5)
    pause
    "Employee" "Dude...."
    scene fs miamallalone25
    player "Hmm?"
    "Employee" "Did...did you just...?"
    scene fs miamallalone26
    player "Heh. Yeah."
    scene fs miamallalone27
    "Employee" "....Nice man!"
    player "Thanks."
    "Employee" "She's fucking fine, keep doing whatever you're doing."
    player "That's the plan."
    $ miaphase2interaction1 = 2
    $ miaphase2interaction2 = 1
    $ miaquestlog = "Shopping with Mia was more fun then I was expecting, I should meet up with her again at her school."
    jump passtime

# holy part 1 lmao
#interaction 2
# part 1

label miaphase2interaction2part1:
    scene fs classroom
    
    show fbmia current:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.7)
    $ miaSprite = 1
    mia "[povname]! I was just thinking about calling you!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "What a coincidence! I was just thinking about kissing YOU."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Hehehe stop! My Mom wants you to come over for dinner again tonight, is that alright?"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Yeah sure! See you tonight."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Thanks!! I gotta go class is starting soon."
    $ miaSprite = 0
    $ miaquestlog = "Mia wants me to come over for dinner again tonight...should be fun?"
    $ miaphase2interaction2 = 2
    jump overworldmap

# part 2

label miaphase2interaction2part2:
    hide screen uppergui
    stop music fadeout 5
    stop sound fadeout 5
    mia "Moooom! He's here!"
    katie "C'mon in brother!"
    player "Haha thanks"
    scene fs miadinner1b
    with Dissolve(1.0)
    pause
    player "Wow! Julia you've outdone yourself this looks amazing."
    julia "I'm so glad you think so!"
    scene fs miadinner2c
    with Dissolve(0.5)
    julia "Alright everyone, dig in!"
    scene fs miadinner1
    with Dissolve(0.5)
    pause
    mia "Wow Mom!"
    mia "This shit straight Bussin!"
    julia "..."
    scene fs miadinner2c
    julia "Mia if you ever say something like that again I will throw you out of the house okay sweetie?"
    scene fs miadinner2b
    player "Hahaha!"
    scene fs miadinner1
    mia "Haha I'm just kidding! I heard some teenagers talking like that yesterday."
    scene fs miadinner2
    katie "Haha oh that reminds me!."

    if juliachecker >= 4:
        jump juliatablehjchoice
    else:
        jump continuedinner1

label juliatablehjchoice:
    "Katie and Mia continued to talk about their day and random stuff"
    "You just focused on the delicious meal in front of you"
    "After some time had passed though you noticed Julia asked you a question"
    scene fs miadinner3
    with Dissolve(0.7)
    player "Huh? Oh uh...sorry what?"
    scene fs miadinner4
    with Dissolve(0.5)
    julia "You should really pay more attention to the ladies around you dear."
    player "{i}Uh...Her hand is totally on my cock{/i}"
    player "{i}And now I'm rock hard with Mia and Katie right there. Great.{/i}"
    menu:
        "Let Julia continue":
            jump juliatablehj
        "Move her hand":
            jump continuedinner1
    
label juliatablehj:
    scene fs miadinner4b
    with Dissolve(0.5)
    player "Yeah uh sorry Julia."
    player "The meal is just....so delicious."
    scene fs miadinner4
    julia "I'm SO glad you think so [povname]."
    julia "I really wanted you to enjoy my....skills."
    scene fs miadinner4b
    player "Sure hehe..."
    mia "Mom could've been a professional if she wanted, she's always been a good cook!"
    player "Y-You don't say!"
    scene fs juliatablehj1
    player "!!!"
    player "Uhhh."
    mia "You okay [povname]?"
    show dinnerjuliajerkoff1
    julia "Yes dear is something the matter?"
    scene fs juliatablehj2b
    player "Ah...uh nope."
    player "Everything's g-good!"
    show dinnerjuliajerkoff1
    julia "Mmmm that's good dear. You should really...FINISH soon."
    show dinnerjuliajerkoff2
    pause
    player "Mmhmm."
    julia "I hope you saved room for desert. I've made some THICK, PLUMP,"
    player "CREAM pies."
    scene fs juliatablehj3
    with vpunch
    player "Uuugh fuck."
    mia "I don't know if I'd call them 'plump' Mom."
    scene fs juliatablehj4
    with Dissolve(0.7)
    julia "Potato potAto dear."
    mia "Is that what that means?"
    player "...."
    jump continuedinner2

label continuedinner1:
    player "{i}I probably shouldn't let her do anything crazy, not here at least.{/i}"
    scene fs miadinner4b
    with Dissolve(0.5)
    player "Thanks again for the invitation Julia."
    scene fs miadinner5
    with Dissolve(0.5)
    player "I really appreciate my GIRLFRIEND'S MOM treating me."
    scene fs miadinner6
    with Dissolve(0.5)
    player "To a WHOLESOME, delicious family dinner."
    scene fs miadinner6b
    with Dissolve(0.5)
    julia "Oh u-uh yes of course."
    player "I promise I'll pay more attention, the food was just so distracting."
    scene fs miadinner7
    with Dissolve(0.5)
    julia "Ahem. Uh yes, very good then..."
    player "{i}Seems I embarrassed her, but it's good she knows some boundaries.{/i}"
    jump continuedinner2

label continuedinner2:
    scene fs miadinner1
    with Dissolve(0.5)
    player "Let's....let's just work on finishing this delicious steak."
    scene fs miadinner12
    katie "...."
    katie "{i}Hmmmm.{/i}"
    katie "{i}Mom's steak is always good but...{/i}"
    scene fs miadinner13
    katie "{i}I think I'm in the mood for some THICK sausage hehe{/i}"
    scene fs miadinner14
    pause
    "*CLINK*"
    katie "Oops! Sorry dropped m'fork."
    julia "No problem dear."
    scene fs miadinner15
    with Dissolve(0.5)
    katie "Darn, where did it go?"
    scene fs miadinner16
    with vpunch
    player "Huh?"
    katie "Hehe."
    mia "Something wrong?"
    player "No everything's good."
    player "{size=25}Katie what are you doing?{/size}"
    $ katiephase2interaction1 = 4
    if katiephase2interaction1 >= 4:
        menu:
            "Don't stop her":
                jump katiedinnerblowjob
            "Stop her":
                jump continuedinner3
    else:
        jump continuedinner3

label katiedinnerblowjob:
    scene fs miadinner20
    katie "Hmm hm hmm..."
    player "Katie we really shouldn't be-"
    scene fs miadinner21
    katie "{size=25}There we go....{/size}"
    show katiedinnerhj1
    pause
    player "{i}Oh fuck. Okay...{/i}"
    katie "{size=25}What are you doing [povname]?{/size}"
    player "Huh?"
    katie "{size=25}My Mom and big sister are right there...{/size}"
    player "{size=25}But you're the one who-{/size}"
    katie "{size=25}How could you cum all over my pretty little face?{/size}"
    show katiedinnerhj2
    player "{i}FUCK! This feels so good!{/i}"
    pause
    katie "{size=25}What if we got caught?{/size}"
    scene fs miadinner23
    with Dissolve(0.5)
    katie "Ehhnnn.."
    player "{i}I can't take much more!{/i}"
    katie "{size=25}What if they saw me just covered in your-{/size}"
    scene fs miadinner24
    with hpunch
    player "UUUGH!"
    scene fs miadinner25
    with Dissolve(0.7)
    katie "Mmmmm."
    katie "Delicious."
    scene fs miadinner26b
    with Dissolve(1.0)
    katie "Man [povname] should come over more often!"
    mia "Haha I agree!"
    julia "I don't see why not!"
    player "....."
    
    scene fs blackblank
    with Dissolve(0.7)
    player "This family is crazy."
    player "And hot."
    player "Pretty hot. Very attractive..."
    player "What have I gotten myself into?"

    $ miaquestlog = "Dinner was...great. Looking forward to some one on one time with Mia."
    $ juliaquestlog = "No more content for Julia right now (ch2.5)"
    if katiephase2interaction1 >= 4:
        $ katiequestlog = "I can't stop thinking about Katie. I should contact Mia and ask for us to all hang out"
    $ miaphase2interaction2 = 3
    jump passtime

label continuedinner3:
    katie "Hehehe."
    scene fs miadinner17
    with Dissolve(0.5)
    katie "I'm here to..."
    scene fs miadinner18
    with Dissolve(0.5)
    katie "Suck..."
    scene fs miadinner19
    with Dissolve(0.5)
    katie "Your..."
    scene fs miadinner19b
    with Dissolve(0.5)
    katie "Cock?"
    scene fs miadinner19c
    with Dissolve(0.5)
    player "Sigh..."
    scene fs blackblank
    with Dissolve(0.7)
    player "This family is crazy."
    player "And hot."
    player "Pretty hot. Very attractive..."
    player "What have I gotten myself into?"

    $ miaquestlog = "Dinner was...great. Looking forward to some one on one time with Mia."
    $ juliaquestlog = "No more content for Julia right now (ch2.5B)"
    if katiephase2interaction1 >= 4:
        $ katiequestlog = "I can't stop thinking about Katie. I should contact Mia and ask for us to all hang out"
    $ miaphase2interaction2 = 3
    jump passtime

# part 3 (named part 4 as part 3 just doesnt exist anymore i guess)

label miaphase2interaction2part4:
    stop music fadeout 5
    stop sound fadeout 5

    hide screen uppergui
    hide screen questboxpreview
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonROOM

    scene fs livingroomnight
    with Dissolve(0.7)
    pause
    "Knock knock knock"
    player "Hmm?"

    show fbplayer current:
        xalign 0.4 ypos 120
    show fbmia current:
        xalign 0.6 ypos 120
    
    $ playerSprite = 1 
    player "Mia!"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Hey! I'm here!"
    $ miaSprite = 0
    $ playerSprite = 1 
    player "I'm happy about that, but why?"
    $ playerSprite = 0
    $ miaSprite = 1
    voice "audio/miagameaudio/mialaugh2.wav"
    mia "Sex!"
    $ miaSprite = 0
    $ playerSprite = 1 
    player "Huh?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "I'm here for sex! We didn't have any when you came over for dinner so...yeah!"
    mia "Thanks again for that by the way, I know my family can get a little crazy."
    $ miaSprite = 0
    $ playerSprite = 1 
    player "Oh you have no-"
    $ playerSprite = 0
    player "Ahem."
    $ playerSprite = 1
    player "Alright yeah I...let me get the lights!"
    show fbplayer current:
        xalign 1.4 ypos 120
    with move
    player "Actually no follow me!"
    show fbmia talkflip:
        xalign 0.6 ypos 120
    play sound "audio/miagameaudio/miahehe.wav"
    show fbmia talkflip:
        xalign 1.2 ypos 120
    with move
    mia "Hehe."
    $ playerSprite = 0


    show miasex movie1
    with Dissolve(1.0)
    play sound "audio/miagameaudio/miamakeout.wav"
    mia "Mmm.."
    mia "MMPH!"
    pause
    scene fs miasextime1
    with Dissolve(0.7)
    stop sound fadeout 5
    pause
    mia "Haha why are you staring in awe, you see them all the time!"
    scene fs miasextime1b
    pause
    scene fs miasextime2
    play sound "audio/miagameaudio/miaah.wav" volume 0.4
    mia "AHHH!"
    play sound "audio/miagameaudio/mialaugh.wav" volume 0.5
    mia "Hahaha okay okay!"
    scene fs miasextime3
    with Dissolve(0.5)
    mia "My gosh sometimes you're so silly."
    scene fs miasextime4
    with Dissolve(0.5)
    pause
    mia "Are you crying?"
    player "They're just so beautiful..."
    mia "My Boobs??"
    player "Mhmm."
    show miasex movie2
    with Dissolve(0.7)
    play sound "audio/miagameaudio/miamoan1.wav" loop
    mia "Ohh...Mmm."
    mia "C-Careful...hah.."
    pause
    scene fs miasextime5
    with Dissolve(0.5)
    stop sound fadeout 3
    mia "Phew..hah.."
    scene fs miasextime6
    with Dissolve(0.5)
    mia "Oh you're.."
    player "Yup."
    scene fs miasextime7
    with Dissolve(0.5)
    play sound "audio/miagameaudio/miamoanlaugh.wav"
    mia "Ahh!"
    mia "[povname] haha!"
    mia "R-Right there!"
    mia "Okay okay stop!"
    mia "Take me to the bed right now!"
    scene fs blackblank
    with Dissolve(0.5)
    player "Yes ma'am."
    show miasex movie3
    play sound "audio/miagameaudio/miamoan2.wav" loop
    mia "MMMHN!"
    player "That feel good baby?"
    show miasex movie4
    stop sound
    play sound "audio/miagameaudio/miasexmoan.wav" loop
    mia "I'm r-really trying not to scream!"
    player "Forget about my neighbors haha I want to hear you baby!"
    mia "O-Oh God [povname]!"
    mia "[povname]!"
    mia "I'm cumming!"
    pause
    show miasex movie5
    play sound "audio/miagameaudio/miaorgasm1.wav" loop
    mia "AHHHHN!"
    mia "I love you!"
    mia "I love you I love you I love you!"
    player "Fuck baby I can't stop!"
    mia "Get me pregnant!"
    stop sound
    scene fs miasextime8
    with Dissolve(0.7)
    mia "Hah...hah...I want.."
    mia "I want little [povname] babies.."
    player "Hahaha!"
    player "I love you too Mia."
    scene fs blackblank
    with Dissolve(0.7)
    pause
    $ miaquestlog = "I really can't get enough of Mia's body. All we did was fuck though!"
    $ miaphase2interaction2 = 4
    jump gotosleep

# end of chapter 2
# end of chapter 2 content

label miabeachchapter2end:
    hide screen mia_beach1
    hide screen mia_beach2
    hide screen mia_beach3
    hide screen sophia_beach
    hide screen charlotte_beach
    hide screen ava_beach
    hide screen emily_beach
    hide screen olivia_beach
    hide screen backbuttonBEACH

    scene fs miabeachcute1
    with Dissolve(0.7)
    player "Ahhh."
    pause
    mia "[povname]!"
    if swimsuitchoice == "white":
        scene fs miabeachcute2a
    elif swimsuitchoice == "purple":
        scene fs miabeachcute2b
    else:
        scene fs miabeachcute2c
    with Dissolve(0.7)
    voice "audio/miagameaudio/miaugh.wav"
    mia "Uggggh."
    player "Hey baby."
    mia "Ava made me play SO much volleyball..."
    player "Haha sorry, you can rest here for a bit."
    mia "Thanks.."

    mia "I don't even wanna rest though, we're at the beeeeach."
    player "Haha okay. Let me think about it."
    #$ miaphase2interaction2 = 6
    #if miaphase2interaction2 >= 6:
    #change the above back when chapter 2 is fully done------------------------------
    if miaphase2interaction2 == 4:
        "Would you like to end the day with Mia?"
        menu:
            "Yes":
                jump miachapter2endsex
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach

    label miachapter2endsex:
        player "You wanna eat something?"
        mia "No..."
        player "Play something other than volleyball?"
        mia "No..."
        player "It's hard to think with your big t-"
        player "Oh I know what to do."

        if swimsuitchoice == "white":
            scene fs miabeachcute3a
        elif swimsuitchoice == "purple":
            scene fs miabeachcute3b
        else:
            scene fs miabeachcute3c
        mia "Yeah??"
        player "Hehe oh yeah."
        player "You wanna sneak off for a little secret sex?"

        if swimsuitchoice == "white":
            scene fs miabeachcute4a
        elif swimsuitchoice == "purple":
            scene fs miabeachcute4b
        else:
            scene fs miabeachcute4c
        voice "audio/miagameaudio/miahehe.wav"
        mia "Oh...hehe."
        mia "I never thought about that.."
        mia "Let's do it!"
        scene fs blackblank
        with Dissolve(0.7)
        stop music fadeout 3
        "A few minutes later..."
        play music "audio/showersounds.wav" fadein 5
        scene fs miabeachsex1
        with Dissolve(0.5)
        mia "Mmmm."
        scene fs miabeachsex2
        with Dissolve(0.5)
        player "Hey there beautiful."
        mia "[povname]! Hehe glad you made it."
        scene fs miabeachsex3
        with Dissolve(0.5)
        mia "Mmmm!"
        player "Mmph."
        scene fs miabeachsex4
        with Dissolve(0.5)
        player "I ever tell you how much I love your tits?"
        show rs charlotteshowersright
        with Dissolve(0.7)
        charlotte "Haaa..."
        mia "You may have mentioned it haha."
        show fs miabeachsex5
        show ls emilyshowersleft
        with Dissolve(0.7)
        emily "Hmm hm hmmm."
        mia "Oh? Where are those hands going?"
        show fs miabeachsex6
        voice "audio/miagameaudio/miaah2.wav"
        mia "Ah! Oh my gosh!"
        show rs charlotteshowerslook
        charlotte "Huh? Mia?"
        player "My hands are occupied so you're gonna have to put it in."
        show fs miabeachsex7
        mia "So hard..."
        show ls emilyshowerslook
        emily "Oh? Someone else here?"
        charlotte "Emily? Is that you?"
        emily "Yeah I thought I heard Mia."
        show fs miabeachsex8
        mia "O-Oh! Yes sorry I was-"
        show fs miabeachsex9
        with vpunch
        voice "audio/miagameaudio/miaah.wav"
        mia "AHH!"
        player "{i}God I love this girl's pussy!{/i}"
        charlotte "Mia! Are you okay?"
        show miabeachsex movie1
        play sound "audio/miagameaudio/miamoaning.wav" loop
        mia "Ahn Ahn Ahn!"
        mia "I-I'm Finnnne!!"
        emily "It sounds like she's struggling Charlotte!"
        charlotte "Mia do you need help!??"
        mia "YESYESYESYES!!!"
        emily "Charlotte go get Ava!"
        scene fs blackblank
        with Dissolve(0.5)
        mia "N-No wait!"
        show fs miabeachsex10
        ava "Mia!? We're coming in to help!"
        play sound "audio/miagameaudio/miamoanno.wav"
        mia "N-No PLEEEASE!"
        show fs miabeachsex11
        with vpunch
        ava "Who's fucking with our-"
        scene fs miabeachsex14
        with Dissolve(0.7)
        ava "....friend."
        scene fs miabeachsex12
        mia "Nooo don't look!"
        player "Uh babe...I'm gonna-"
        scene fs miabeachsex13
        with vpunch
        play sound "audio/miagameaudio/miaorgasm2.wav"
        mia "C-Cumming!"
        player "Fuck!"
        scene fs miabeachsex14
        with Dissolve(0.5)
        "...."
        scene fs carscene8
        with Dissolve(1.2)
        stop music fadeout 3
        "It was an awkward drive back for mostly everyone"
        "You didn't really mind though. You fucked a pretty girl and came inside her while all her friends watched."
        "On paper that's pretty good!"
        pause
        pause
        pause
        scene fs carscene9
        with vpunch
        sophia "Gah!"
        $ endchapter2_trigger = "2 mia neutral"
        $ miaquestlog = "I've been patient. It's time Mia..."
        jump startofchapter3

# start chapter 3

# Chapter 3 and related character scenes.

label miaphase3interaction1part1:
    hide screen uppergui
    scene fs playerroomMorn
    with Dissolve(0.5)
    $ playerSprite = 4
    show fbplayer current:
        xalign 0.5 ypos 120
    player "...."
    player "It's time Mia."
    $ miaphase2interaction2 = 5
    $ miaphase3interaction1 = 1
    $ miaquestlog = "Finish the fight(Find Mia in her room)"
    jump playerlivingroom

label miaphase3interaction1part2:
    scene fs blackblank
    with Dissolve(0.7)
    katie "And then heeere's when we went bowling."
    sophia "Oh my God look at Josy haha!"
    emily "That's super cute."
    mia "Hehe."
    emily "Mia! Show us those 1st date pics you said you had!"
    katie "Oh yeah I've wanted to see those forever."
    mia "Haha okay, I haven't seen them myself since we took them."
    scene fs miaanal1
    with Dissolve(0.7)
    mia "Alrighty soooo.."
    scene fs miaanal2
    show selfieshare 1stdateselfie1:
        xalign 0.75 ypos 50
    mia "Here's us at the start."
    mia "He asked me out to a flower festival."
    scene fs miaanal3b
    show selfieshare 1stdateselfie1:
        xalign 0.75 ypos 50
    sophia "Aww!"
    katie "Very cute."
    emily "That's a great picture."
    scene fs miaanal1
    show selfieshare 1stdateselfie1:
        xalign 0.75 ypos 50
    mia "And then we walked around."
    scene fs miaanal2
    show selfieshare 1stdateselfie2:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal3b
    show selfieshare 1stdateselfie2:
        xalign 0.75 ypos 50
    emily "Oh my gosh."
    sophia "Ugh. You look so adorable."
    katie "Ugh this is way too sweet for me."
    scene fs miaanal1
    show selfieshare 1stdateselfie2:
        xalign 0.75 ypos 50
    mia "I don't remember what we did after."
    scene fs miaanal2
    show selfieshare 1stdateselfie3:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal3
    show selfieshare 1stdateselfie3:
        xalign 0.75 ypos 50
    pause
    katie "I have an idea or two."
    mia "T-That's yogurt!"
    katie "On the first date sis? Wow."
    emily "...."
    mia "It's YOGURT!"
    mia "Moving on!"
    scene fs miaanal4
    show selfieshare 1stdateselfie4:
        xalign 0.75 ypos 50
    pause
    "Everyone" "Awww!"
    mia "Oh yeah! We met Mr. Frog."
    sophia "I love Mr. Frog."
    katie "I'd die for Mr. Frog."
    mia "And then.."
    scene fs miaanal2
    show selfieshare 1stdateselfie5:
        xalign 0.75 ypos 50

    pause
    scene fs miaanal3b
    show selfieshare 1stdateselfie5:
        xalign 0.75 ypos 50
    sophia "Wooooow!"
    emily "This is a beautiful shot Mia."
    josy "This shit belongs in a movie, holy."
    mia "Aww thanks girls."
    scene fs miaanal2
    show selfieshare 1stdateselfie6:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal3
    show selfieshare 1stdateselfie6:
        xalign 0.75 ypos 50
    "!!!!"
    scene fs miaanal4b
    show selfieshare 1stdateselfie6:
        xalign 0.75 ypos 50

    katie "MIA!"
    emily "O-Oh my."
    sophia "Holy!"
    mia "N-No no no!"
    scene fs miaanal3c
    show selfieshare 1stdateselfie7:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal4b
    show selfieshare 1stdateselfie7:
        xalign 0.75 ypos 50
    katie "MIA ON A FIRST DATE???!!!"
    mia "...."
    scene fs miaanal6
    pause
    scene fs miaanal7
    with Dissolve(0.7)
    pause
    mia "It wasn't yogurt."
    "...."
    player "*knock knock*"
    player "Oh, hey everyone!"
    scene fs miaanal5
    with vpunch
    "Everyone" "[povname]!"
    scene fs gfroom
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.3 ypos 120
    show fbsophia current:
        xalign 0.4 ypos 120
    show fbkatie current:
        xalign 0.5 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.7)
    pause
    $ playerSprite = 1
    player "Hey now, no need for you all to get up cause'a me."
    emily "No it's okay, we were just about to leave anyways."
    sophia "We were?"
    katie "Yah, were we?"
    emily "Yes of COURSE we were. Plus [povname] clearly came to visit Mia right?"
    player "Uh yeah."
    emily "So let's not bother them and let them get to it!"
    sophia "Ohhhh.."
    katie "Alright I was gonna meet up with Josy after this anyways, see yah everyone."
    hide fbkatie current
    emily "C'mon Sophia. Bye Mia!"
    mia "Bye!"
    hide fbemily current
    sophia "Ugh."
    hide fbsophia current
    player "Everyone left in a rush huh?"
    mia "*Ahem* Y-Yes. Seems they were busy."
    mia "You wanted to see me?"
    player "Ah yes. Very important."
    mia "Important?"
    player "Mia."
    player "Whisper whisper Anal whisper whisper."
    mia "W-What??!"
    player "Whisper whisper right now whisper."
    mia "R-Right now?"
    player "Please. We've already talked about it."
    mia "Why were you SAYING whisper?"
    player "Mia I love you with all my cock. I yearn for your body!"
    player "Let me make you feel good, in a new way."
    mia "Ohhh well...I mean...maybe we can try?"
    scene fs miaanal8
    with vpunch
    mia "Wha-How did you take off your clothes so fast?!"
    scene fs miaanal9
    player "Practice."
    scene fs miaanal8
    mia "And we don't even have lube! I'm not doing it without lu-"
    scene fs miaanal10
    "*Squirt*"
    scene fs miaanal8
    mia "Where di-Where did you get that?!"
    scene fs miaanal9
    player "We can go as slow as you need."
    scene fs miaanal8
    mia "...."
    scene fs miaanal11
    with Dissolve(0.5)
    mia "I swear the things you do to me..."
    scene fs miaanal14
    with Dissolve(0.7)
    player "There you go, now lift yourself up slowly."
    scene fs miaanal13
    with Dissolve(0.5)
    mia "Ehhh.."
    player "You're doing great babe keep going."
    scene fs miaanal12
    with Dissolve(0.5)
    player "Perfect, now slowly put it in, I'll hold you."
    mia "[povname] I-I don't think I'm ready for this I didn't think you'd actua-"
    scene fs miaanal15
    with vpunch
    mia "OHHHHH MAH GAWD."
    player "Fuck Fuck baby holy shit."
    mia "I slipped!"
    player "Yeah no kidding!"
    player "You're so tight baby oh my god."
    scene fs miaanal16
    with Dissolve(0.5)
    mia "Ohhhh!"
    scene fs miaanal17
    with Dissolve(0.5)
    player "Here baby let me help you."
    scene fs miaanal17b
    pause
    scene fs miaanal18
    mia "Oh that's...that's a little better."
    player "Let's lie down slowly."
    scene fs miaanal19
    with Dissolve(0.5)
    player "Mia your ass feels incredile."
    player "I'm so fucking hard."
    mia "I-I can tell!"
    show miatakingituptheass1
    pause
    mia "Oh..."
    mia "OH."
    player "Yeah baby that's it."
    mia "Ahn..."
    player "You're feeling good aren't you?"
    mia "NnNNyEaHHhhHHh..."
    player "C'mon baby."
    show miatakingituptheass2
    player "C'MON BABY!"
    mia "AHHH!"
    mia "[povname]!"
    mia "[povname] I'm gonna CUM!"
    scene fs miaanal21
    pause
    scene fs miaanal21b
    with vpunch
    mia "AHHHH!!!"
    player "FUCK!"
    scene fs blackblank
    with Dissolve(0.3)
    "A few moments earlier..."
    scene fs miaanal22
    with Dissolve(0.5)
    pause
    mia "AHHH!"
    scene fs miaanal23
    ava "Heeey girl I'm he-"
    mia "[povname] I'm gonna CUM!"
    scene fs miaanal24
    with vpunch
    mia "AHHHH!!!"
    player "FUCK!"
    pause
    ava "{i}Goddamn Mia, all that in your ass?{/i}"
    mia "Hah...hah."
    ava "{i}I should...come back later...{/i}"
    mia "Oh [povname]...Ahn.."
    player "You feel so good baby."
    mia "Feel...so full.."
    ava "{i}It'd be the polite thing to do.{/i}"
    scene fs miaanal22
    pause
    mia "Mmmm..."
    scene fs miaanal25
    play sound "audio/camerasnap.mp3"
    $ renpy.notify("Got Mia's 1st date pics!")
    $ phone_pictures.append("mia selfie1a")
    $ phone_pictures.append("mia selfie2")
    $ phone_pictures.append("mia selfie 3 flower")
    $ phone_pictures.append("mia selfies4")
    $ phone_pictures.append("mia selfies5")
    $ phone_pictures.append("mia selfies6")
    $ phone_pictures.append("mia selfies7")
    pause
    $ miaphase3interaction1 = 2
    $ miaquestlog = "No more solo content for Mia this version(Ch2.5)"
    jump passtime

# chapter 3 end i guess?

label sleepwithmia:
    scene fs charlotteroom
    with Dissolve(1.0)
    show fbcharlotte pajama:
        xalign 0.4 ypos 120
    show fbava pajama:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    pause
    show fbmia pajama:
        xalign 0.6 ypos 120
    show fbsophia pajama:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    pause
    show fbolivia pajama:
        xalign 0.9 ypos 120
    show fbemily pajama:
        xalign 1.0 ypos 120
    show fbplayer pajama:
        xalign 0.1 ypos 120
    with Dissolve(0.5)
    pause
    show fbemily pajamatalk:
        xalign 1.0 ypos 120
    emily "Okay! *Yawn* Where's everyone sleeping?"
    show fbemily pajama:
        xalign 1.0 ypos 120
    show fbplayer pajamatalk:
        xalign 0.1 ypos 120
    player "Well I think Charlotte should get the bed, how many can fit on it?"
    show fbplayer pajama:
        xalign 0.1 ypos 120
    show fbcharlotte pajamatalk:
        xalign 0.4 ypos 120
    charlotte "Thank you [povname]. It can fit four."
    show fbcharlotte pajama:
        xalign 0.4 ypos 120
    show fbmia pajamatalk:
        xalign 0.6 ypos 120
    mia "I don't care as long as I can sleep next to [povname]."
    show fbmia pajama:
        xalign 0.6 ypos 120
    show fbplayer pajamatalk:
        xalign 0.1 ypos 120
    player "Babe I don't think any of our sleeping bags can fit both of us."
    show fbplayer pajama:
        xalign 0.1 ypos 120
    show fbava pajamatalk:
        xalign 0.3 ypos 120
    ava "Fine, you two also get the bed. Who's last?"
    show fbava pajama:
        xalign 0.3 ypos 120
    show fbolivia pajamatalk:
        xalign 0.9 ypos 120
    olivia "Emily should."
    show fbolivia pajama:
        xalign 0.9 ypos 120
    show fbemily pajamatalk:
        xalign 1.0 ypos 120
    emily "Me? No it's okay Sophia how abou-"
    show fbemily pajama:
        xalign 1.0 ypos 120
    show fbsophia pajamatalk:
        xalign 0.7 ypos 120
    sophia "It's fine Emily, I'm so tired it really doesn't matter to me right now."
    show fbsophia pajama:
        xalign 0.7 ypos 120
    show fbemily pajamatalk:
        xalign 1.0 ypos 120
    emily "Okay then! Thanks guys."
    show fbemily pajama:
        xalign 1.0 ypos 120

    scene fs sleepoverbedpovmia
    with Dissolve(1.0)
    pause
    "Most of the girls fell asleep even with the strong moonlight bursting through the windows"
    "But surrounded by all these beautiful girls kept your mind wandering, and your sleep restless.."
    scene fs groupbedsex3
    with Dissolve(0.7)
    pause
    scene fs groupbedsex3b
    with Dissolve(0.5)
    pause
    emily "*Snore*"
    scene fs groupbedmiasex1
    pause
    scene fs groupbedmiasex1b
    pause
    scene fs groupbedmiasex1c
    pause
    scene fs groupbedmiasex2
    mia "Hmm?"
    scene fs groupbedmiasex2b
    mia "..."
    player "..."
    scene fs groupbedmiasex2c
    mia "Hehehe."
    scene fs groupbedmiasex3
    pause
    scene fs groupbedmiasex4
    mia "!!!"
    scene fs groupbedmiasex4b
    player "Try not to make any noise."
    scene fs groupbedmiasex5
    pause
    scene fs groupbedmiasex6
    mia "Ah!"
    mia "I don't know...if I can do that."
    scene fs groupbedmiasex7
    mia "Mmm!"
    player "Auhn.."
    scene fs groupbedmiasex8
    with Dissolve(0.7)
    pause
    scene fs groupbedmiasex9
    with Dissolve(0.7)
    pause
    scene fs groupbedmiasex10
    player "Don't cover your mouth."
    mia "But what if they hear me? What if they wake up?"
    player "Good."
    scene fs groupbedmiasex11
    pause
    scene fs groupbedmiasex11b
    mia "Ehnnn!"
    scene fs groupbedmiasex122
    with Dissolve(0.5)
    mia "Hah..."
    scene fs groupbedmiasex12b
    with vpunch
    mia "Ahn!"
    scene fs groupbedmiasex122
    with Dissolve(0.3)
    mia "Oh.."
    scene fs groupbedmiasex12b
    with vpunch
    mia "AHN!"
    scene fs groupbedmiasex13
    mia "Hah..hah.."
    player "You like that baby?"
    scene fs groupbedmiasex13b
    mia "Yes!"
    player "You like it when I fuck you next to your friends?"
    scene fs groupbedmiasex13b2
    mia "I love it hehehe!"
    scene fs groupbedmiasex122
    with Dissolve(0.5)
    player "Take this fat fucking cock!"
    scene fs groupbedmiasex12b
    with vpunch
    mia "[povname]!"
    scene fs groupbedmiasex14
    with Dissolve(0.7)
    mia "[povname] I'm gonna cum!"
    player "Cum with me baby, let me fill you up!"
    mia "Please! Please!"
    pause
    scene fs groupbedmiasex122
    with Dissolve(0.5)
    player "What do you want?!"
    mia "I want you to cum inside me while everyone listens!"
    scene fs groupbedmiasex12b
    with vpunch
    player "AHHHGH!"
    mia "YES!!!"
    pause
    scene fs groupbedmiasex12c
    with Dissolve(0.7)
    pause
    scene fs blackblank
    with Dissolve (1.0)
    "The night passed by quickly for you and Mia, not so much for everyone else"
    "In the morning everyone was cordial but you noticed a lack of sleep in the girls eyes"
    "You said your goodbyes and headed back home"
    jump passtime

    scene fs groupbedsex1
    pause
    scene fs groupbedsex1b
    pause
    scene fs groupbedsex2
    pause
    scene fs groupbedsex2b
    pause
    scene fs groupbedsex3
    pause
    scene fs groupbedsex3b
    pause
    scene fs groupbedsex4
    pause
    scene fs groupbedsex4b
    pause
    scene fs groupbedsex5
    pause
    scene fs groupbedsex5b
    pause
    scene fs groupbedsex6
    pause
    scene fs groupbedsex6b
    pause

    scene fs groupbedmiasex1
    pause
    scene fs groupbedmiasex1b
    pause
    scene fs groupbedmiasex1c
    pause
    scene fs groupbedmiasex2
    pause
    scene fs groupbedmiasex2b
    pause
    scene fs groupbedmiasex2c
    pause
    scene fs groupbedmiasex3
    pause
    scene fs groupbedmiasex4
    pause
    scene fs groupbedmiasex4b
    pause
    scene fs groupbedmiasex5
    pause
    scene fs groupbedmiasex6
    pause
    scene fs groupbedmiasex7
    pause
    scene fs groupbedmiasex8
    pause
    scene fs groupbedmiasex9
    pause
    scene fs groupbedmiasex10
    pause
    scene fs groupbedmiasex11
    pause
    scene fs groupbedmiasex11b
    pause
    scene fs groupbedmiasex12
    pause
    scene fs groupbedmiasex122
    pause
    scene fs groupbedmiasex12b
    pause
    scene fs groupbedmiasex12c
    pause
    scene fs groupbedmiasex13
    pause
    scene fs groupbedmiasex13b
    pause
    scene fs groupbedmiasex13b2
    pause
    scene fs groupbedmiasex14
    pause

    jump passtime
