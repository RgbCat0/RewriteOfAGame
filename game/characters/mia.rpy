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
    player "Hey Mia, what’s up?"
    mia "Hey [povname]. Not much! Need anything?"
    player "Yeah I need YOU. Can you come over tonight?"
    mia "Um yeah I think I can, I’ll be there soon."
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
