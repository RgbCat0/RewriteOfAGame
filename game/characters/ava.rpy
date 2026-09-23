#chapter 1
# interaction 1
# part 1

label avaphase1interaction1part1:
    scene fs schoolhallwayzoomblur

    $ playerSprite = 1

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    #show fbava current:
    #    xalign 0.7 ypos 120
    #with Dissolve(0.5)
    $ avaSprite = 0
    show fbava current:
        xalign 0.5 ypos 120
    #with Dissolve(0.5)


    player "Hey, Ava right?"
    $ playerSprite = 0
    $ avaSprite = 1
    voice "audio/avagameaudio/avahey.wav"
    ava  "Oh hey yeah! You're [povname], what's up?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Not much, just stopping by the school seeing if I can chat with Mia or anyone else before class starts. Yourself?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "I'm just going through my health notes also before class starts, quiz today."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Oh well good luck!"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Haha thanks! I've been stressin' bout it all weekend."
    $ avaSprite = 0
    $ playerSprite = 1
    player "I'm sure you'll be fine, Mia tells me your passion's getting you nothing but straight As and I believe her. Are you meeting with any of the girls afterwards?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "That's cool of you to say, no though I usually go to the gym after classes in the afternoons. With the track meet on the way I gotta make sure I'm in shape and ready for it. "
    $ avaSprite = 0
    $ playerSprite = 1
    player "I'd love to look at you."
    $ playerSprite = 0
    ava "Hmm?"
    $ playerSprite = 6
    player "I-I mean look as good as you sorry."
    $ playerSprite = 0
    $ avaSprite = 4
    #play sound "audio/avagameaudio/avaohuh.wav"
    ava "Oh haha no problem, for a second there I thought..."
    $ avaSprite = 1
    ava "Well nevermind. You should visit me in the afternoon, come check out the gym see if you like it."
    $ avaSprite = 4
    ava "I mean you dont look like you need to get in shape....b-but there's never anything wrong with gaining a few muscles and staying healthy!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Can't argue with that, maybe I will stop by!"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Great I'll see you there then!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Yeah have a good one, oh and good luck on the test!"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh, yeah. Right. Thanks again."
    if renpy.android:
        $ avaquestlog = "{size=-25}Ava seems cool. She invited me to go to the gym in the afternoon beside the school.{/size}"
    else:
        $ avaquestlog = "Ava seems cool. She invited me to go to the gym in the afternoon beside the school."
    $ avaquesticon = "gui/questboxAva.png"
    $ avaphase1interaction1 = 1
    hide fs schoolhallwayzoomblur
    hide fbava
    hide fbplayer
    jump returnwhereyouare

# part 1 post convo

label avaphase1interaction1part1postconvo:
    scene fs schoolhallwayzoomblur
    $ avaSprite = 0
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)


    player "Sorry where's the gym again?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "It's right beside the school you can't miss it."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Ah thanks."
    $ playerSprite = 0
    hide fs schoolhallwayzoomblur
    hide fbplayer
    hide fbava
    jump returnwhereyouare

# part 2

label avaphase1interaction1part2:
    scene fs gymarea

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    player "{i}Hmm I'm here now but where's Ava?{/i}"
    player "{i}For a school gym this place is pretty impressive, they have everything you need. Oh there she is, I think she sees me.{/i}"

    $ avaSprite = 3
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    play sound "audio/avagameaudio/avahey.wav"
    ava "Hey [povname]! So awesome of you to stop by!"
    $ avaSprite = 2
    $ playerSprite = 1
    player "Hey I told you I'd come so I made sure I did!"
    $ playerSprite = 0
    player "{i}God damn Ava's gym clothes are revealing! She looks so hot in them, specially with how in shape she is...{/i}"
    $ avaSprite = 3
    ava "I like I man who does what he says he'll do!"
    $ avaSprite = 2
    $ playerSprite = 1
    player "Really?"
    $ playerSprite = 0
    $ avaSprite = 20
    ava "I-I mean like as a friend! I like...dudes for friends who..set their minds...um...forget I said anything!"
    ava "W-What do you think of the gym?!"
    $ avaSprite = 2
    $ playerSprite = 1
    player "Honestly it's really impressive."
    $ playerSprite = 0
    $ avaSprite = 3
    ava "Right? I have everything I need here, from powerlifting to cardio to stretching in the yoga room."
    $ avaSprite = 2
    $ playerSprite = 1
    player "You.....stretch in those clothes?"
    $ playerSprite = 0
    $ avaSprite = 3
    ava "Yeah these are my gym clothes. Shows a bit of skin but I dont get too hot and super easy to move in. I can even do one of those human pretzel things!"
    $ avaSprite = 2
    $ playerSprite = 11
    player "{i}Yup I need join this gym ASAP.{/i}"
    $ playerSprite = 1
    player "Well I'm convinced! What do I need to join?"
    $ playerSprite = 0
    $ avaSprite = 3
    ava "Nice! All you need is some gym clothes and to pay for the gym card. One time fee."
    $ avaSprite = 2
    $ playerSprite = 1
    player "Cool I'll get on that, think you can show me the ropes when I visit?"
    $ playerSprite = 0
    $ avaSprite = 3
    ava "I'd love to! I'm always here during the week days in the afternoon after class."
    $ avaSprite = 2
    $ playerSprite = 1
    player "Great can't wait."
    $ playerSprite = 0
    $ avaSprite = 3
    ava "Oh um, Mia is okay with all this right?"
    $ avaSprite = 2
    $ playerSprite = 1
    player "Huh? Yeah I don't see why she wouldn't be. Why?"
    $ playerSprite = 0
    $ avaSprite = 3
    ava "N-No reason I'm just...just making sure! See yah!"
    $ avaSprite = 2
    $ playerSprite = 7
    player "Huh..."
    $ playerSprite = 0
    $ avaquestlog = "If I want to work out at Ava's gym with her I'll need a gym pass!"
    $ avaphase1interaction1 = 2
    hide fs gymarea
    hide fbava
    hide fbplayer
    jump returnwhereyouare

# part 2 post convo

label avayoushouldbuygympass:
    hide screen ava_atgym
    hide screen backbuttonGYM
    if whereami == "gym":
        scene fs gymarea
    else:
        scene fs schoolhallway
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    if whereami == "gym":
        $ avaSprite = 3
    else:
        $ avaSprite = 1

    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    ava "Hey! Don't forget you need to buy a pass from the machine in the front of the gym before we can start."
    hide fs
    hide fbava
    hide fbplayer
    jump returnwhereyouare

# part 3

label avaphase1interaction1part3:
    scene fs outsidegym
    hide screen backbuttonGYMOUTSIDE
    if avaphase1interaction1 != 2:
        player "What a strange looking machine."
        jump outsidegym


    $ playerSprite = 7

    show fbplayer current:
        xalign -0.02 ypos 120
    with Dissolve(0.5)

    player "Hmm now how does this thing work?"
    $ playerSprite = 4
    show fs gympass2
    "Machine" "Insert currency."
    show fs gympass1
    $ playerSprite = 5
    player "What?"
    $ playerSprite = 4
    show fs gympass2
    "Machine" "Insert currency for gym pass!"
    show fs gympass1
    $ playerSprite = 5
    player "What the-"
    player "Why does it talk?"
    $ playerSprite = 4
    show fs gympass2
    "Machine" "One hundred credits!!"
    show fs gympass1
    if money >= 100:
        menu:
            "Pay for gym pass":
                jump payforgym
            "Don't pay":
                jump outsidegym
    else:
        $ playerSprite = 5
        player "Okay I'll pay."
        $ playerSprite = 4
        show fs gympass2
        "Machine" "You do not have sufficient amount of currency!"
        "Machine" "You scum!"
        hide fs gymarea
        hide fbplayer

        jump outsidegym

# part 3 still

label payforgym:
    $ playerSprite = 5
    player "Okay here's my money."
    $ playerSprite = 4
    image insertyourcurrency:
        "ATM money.png"
        0.7
        "atm money2.png"
        0.7
        repeat
    show insertyourcurrency behind fbplayer
    "Machine" "Mmmm. Yeah. That's good."
    $ playerSprite = 5
    player "What the fuck..."
    $ playerSprite = 4
    "Machine" "Oh...*Beep*..right there..*Beep Beep*...insert your currency!"
    hide insertyourcurrency
    show fs gympass5
    with vpunch
    "Machine" "RELEASING PRODUUUUCT!"
    player "...."
    $ playerSprite = 5
    player "Well I got my gym pass now...how did it know all my information already? Huh."
    $ playerSprite = 4
    "Machine" "...."
    $ money -= 100
    $ avaphase1interaction1 = 3
    $ avaquestlog = "That machine was really strange, but at least now I have my gym pass."
    hide screen gym_machine
    jump outsidegym

# part 3.5 after pass (only happens when not at gym i guess)

label igotthepassava:
    scene fs schoolhallwayzoomblur

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    $ avaSprite = 0
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Hey I got a gympass!"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Sweet! I'm about to head to class but I'll see you there in the afternoon!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Alright sounds good."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "See yah!"
    $ avaSprite = 0
    hide fs schoolhallwayzoomblur
    hide fbplayer
    hide fbava
    jump returnwhereyouare

# part 4

label avaphase1interaction1part4:
    hide screen ava_atgym
    hide screen gym_machine
    hide screen backbuttonGYM
    scene fs gymarea

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    $ avaSprite = 2

    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Hey! I made it."
    $ playerSprite = 0
    $ avaSprite = 3
    ava "Looking good! I just finished my warm up and was about to do some squats. You want to start there?"
    $ avaSprite = 2
    $ playerSprite = 1
    player "Yeah sure sounds good."
    $ playerSprite = 0
    hide fbplayer
    hide fbava
    scene fs blackblank
    with Dissolve(0.5)
    $ avasprite = 3
    ava "Squats are great because it almost works out your entire body, it's a good measure of strength and strength building."
    $ avaSprite = 2
    scene fs avasquats1
    with Dissolve(0.5)
    $ avasprite = 3
    ava "Okay you just sit right there and I'll show you my form using just the bar."
    $ avaSprite = 2
    $ playerSprite = 1
    player "{i}Annnd that's why I'm here.{/i}"
    $ playerSprite = 0
    scene fs avasquats2
    with Dissolve(0.5)
    play sound "audio/avagameaudio/avagrunt1.wav"
    $ avasprite = 3
    ava "Okay so you're gonna want to keep your legs shoulder width apart, and when you bend down keep your heels on the ground, it's not easy at first."
    $ avaSprite = 2
    scene fs avasquats3b
    with Dissolve(0.5)
    $ playerSprite = 1
    scene fs avasquatbutt
    with Dissolve(0.7)
    player "{i}Holy shit look at that ass!{/i}"
    $ playerSprite = 0
    scene fs avasquats2b
    play sound "audio/avagameaudio/avagrunt2.wav"
    player "{i}I guess I never saw her from behind cause there's no way I'd miss that bubble butt.{/i}"
    show avadoingsquats
    $ avaSprite = 3
    ava "You're gonna want to do 3 sets of 5 to start out."
    $ avasprite = 2
    $ playerSprite = 1
    player "Three sets...gotcha..."
    $ playerSprite = 0
    scene fs avasquats1c
    with Dissolve(0.5)
    ava "So you wanna try it out yourself now?"
    scene fs avasquats1b
    player "Uh actually, could you show me the form again real quck?"
    $ playerSprite = 0
    show avadoingsquats
    $ avasprite = 3
    ava "Oh uh sure. Watch carefully."
    $ avaSprite = 0
    player "{i}Oh I will.{/i}"
    window hide
    pause
    player "{i}Shit her ass is amazing I'm actually starting to get hard.{/i}"
    $ avaSprite = 1
    ava "Hah..."
    scene fs avasquats1
    with Dissolve(0.5)
    ava "Alright how was that?"
    $ avaSprite = 0
    scene fs avasquats1
    with Dissolve(0.5)
    menu:
        "Show me again.":
            jump showmethatassava
        "Yeah I got it thanks":
            jump giveuponava

# great label (part 4)

label giveuponava:
    player "{i}Okay I might be crossing a few too many lines here maybe I should stop.{/i}"
    menu:
        "Stop objectifying Ava":
            jump giveuponava2
        "Definitely DON'T stop objectifying Ava, look at that ass!":
            jump showmethatassava

# great label 2 (part 4)

label giveuponava2:
    player "Yeah I got it thanks."
    ava "Oh great! So should w-"
    player "Sorry Ava I don't think this is actually for me, sorry for wasting your time."
    ava "Wait what?"
    hide fs avasquats1
    hide fbplayer
    hide fbava
    jump passtime

# part 4 continue

label showmethatassava:
    scene fs avasquats1b
    player "Sorry I uh missed it, show me again?"
    scene fs avasquats5
    with Dissolve(0.7)
    ava "You missed it?"
    player "Yup."
    scene fs avasquats2c
    with Dissolve(0.7)
    ava "{i}What does he mean he missed it he's right behind me, plus I can see through the mirror he's looking right at...wait..{/i}"
    scene fs avasquats3c
    ava "{i}Is he looking at my ass or something?{/i}"
    scene fs avasquats4c
    with Dissolve(0.5)
    ava "{i}He totally is!{/i}"
    scene fs avasquats5c
    with Dissolve(0.5)
    ava "{i}He's glaring so hard...s-should I stop? He's Mia's boyfriend!{/i}"
    scene fs avasquats5d
    with Dissolve(0.7)
    pause
    scene fs avasquats5e
    with Dissolve(0.7)
    ava "A-Are you paying attention to how I keep my balance?"
    player "Oh I'm paying attention."
    ava "...."
    scene fs avasquats5d
    with Dissolve(0.7)
    pause
    scene fs avasquats5c
    with Dissolve(0.7)


    scene fs avasquatbutt
    with Dissolve(0.7)
    ava "Hah...hah..how was that?"
    player "Again."
    ava "O-Okay..."
    show avadoingsquats2
    ava"{i}Why am I listening to him?! This is wrong right? I shouldn't like this right?!{/i}"
    play sound "audio/avagameaudio/avalittlemoan.wav"
    ava "Uhn!"
    ava "{i}Fuck did I just moan a little??! What is wrong with me??{/i}"
    player "{i}Hah she just moaned. I don't know if that was on purpose but I am having a great time watching her get so flustered. I should stop soon though else my dick will rip a hole in my pants.{/i}"
    player "Okay I think that's enough."
    scene fs avasquats4c
    with Dissolve(0.5)
    ava "O-Okay."
    player "Think I'll leave now, I learned a lot thanks."
    ava "You're leaving?!"
    scene fs avasquatbutt
    with Dissolve(0.7)
    player "Yeah I uh..got what I came for."
    ava "{i}Jesus Christ the balls this guy has.{/i}"
    player "I'll come back soon. See you."
    ava "Sure, see you."
    scene fs blackblank
    with Dissolve(1.0)
    ava "Oh my god I can't deal with this right now I have the track meet to focus on. How could he flirt like that so blatantly he's dating Mia!" # this should be italic
    ava "And I just kept going too. Am I a bad friend? Did I like knowing he was looking at my ass like that?"
    ava "I mean it's always nice knowing boys find you attractive bu-stop stop it STOP Ava! Focus!"
    ava "Track. Meet."
    ava "I'm going to do some leg presses."
    $ avaphase1interaction1 = 4
    $ avaquestlog = "That was hot. I should talk to Ava again about another work out together."
    hide fs blackblank
    hide fbplayer
    hide fbava
    jump passtime

# part 5

label avaatschoolinteraction1:
    scene fs schoolhallwayzoomblur

    $ avaSprite = 4

    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    ava "{i}I still can't get my mind off of what happened at the gym with [povname]. I mean I'm no prude but...{/i}"
    ava "{i}Oh shit there he is.{/i}"

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Hey Ava, I'm down for another session."
    $ playerSprite = 0
    $ avaSprite = 1
    voice "audio/avagameaudio/avaohuh.wav"
    ava "Oh uh, really?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Yeah I'm...getting pretty excited thinking about it."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Yeah me too..."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Good. I thought you'd be."
    $ playerSprite = 0
    ava "...."
    $ playerSprite = 1
    player "Anyways see you there later!"
    show fbplayer defaultflip:
        xalign 0.25 ypos 120

    ava "{i}No no no c'mon Ava don't let him control you like that!{/i}"
    $ avaSprite = 4
    show fbava current:
        xalign 0.6 ypos 120
    with move

    ava "W-Wait!"
    $ avaSprite = 0
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.3 ypos 120
    player "Hmm?"
    $ avaSprite = 1
    ava "Actually I can't I have to practice running....a-at night! Can't put too much muscle on you know? Weighs you down."
    $ avaSprite = 0
    $ playerSprite = 1
    player "And the night part?"
    $ playerSprite = 0
    $ avaSprite = 4
    ava "I....like running at night?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Ah okay, no problem."
    $ playerSprite = 0
    ava "{i}Oh thank god.{/i}"
    $ playerSprite = 1
    player "I'll meet you tonight at the park then?"
    $ playerSprite = 0
    $ avaSprite = 4
    ava "A wha?"
    $ playerSprite = 1
    player "The park? Seems like a good place to run since the gym will be closed."
    ava "Oh yeah..."
    $ avaSprite = 12
    ava "{i}Shit.{/i}"
    player "Alright see you then!"
    hide fbplayer current
    with Dissolve(0.7)
    ava "{i}It's gonna be fine right? What am I even scared of happening, the guy isn't a rapist...{/i}"
    $ avaSprite = 13
    ava "{i}Would he make a move on me though?{/i}"
    $ avaSprite = 14
    ava "{i}Am I be more scared that I might....reciprocate?{/i}"
    $ avaSprite = 0
    ava "Heh, look at me using words like reciprocate."
    ava "...."
    $ avaSprite = 12
    ava "Fuck, we're just going for a run. Stop thinking so much girl!"
    $ avaphase1interaction1 = 5
    $ avaphase1interaction2 = 1
    $ avaquestlog = "I agreed to meet up with Ava at the park at night."
    hide fs schoolhallwayzoomblur
    hide fbplayer
    hide fbava
    jump returnwhereyouare

# part 5 post convo

label letsmeetatthepark:
    scene fs schoolhallwayzoomblur

    $ playerSprite = 1
    $ avaSprite = 0
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    player "We're meeting at the park yeah?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Yup. At night, don't forget."
    $ avaSprite = 0
    jump returnwhereyouare

# interaction 2
# part 1

label avaphase1interaction2part1:
    hide screen uppergui
    stop music fadeout 5
    stop sound fadeout 5
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    player "{i}It's a bit dark but at least it's pretty warm, now where is Ava?{/i}"
    player "{i}Ah there she is near the bench.{/i}"
    $ avaSprite = 0
    show fbava current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Sup."
    $ playerSprite = 0
    $ avaSprite = 1
    play sound "audio/avagameaudio/avaalright.wav"
    ava "Alright! Finally ready to get serious?"
    $ playerSprite = 1
    $ avaSprite = 0
    player "What do you mean? I was serious before too."
    $ playerSprite = 0
    $ avaSprite = 4
    ava "Um. Yeah of course."
    ava "Let's just run. You know proper breathing techniques right?"
    $ playerSprite = 11
    $ avaSprite = 0
    player "Proper what now?"
    $ playerSprite = 0
    scene fs avarun0
    with Dissolve(1.0)
    "You starting jogging with Ava as she explains the correct way to breath and expend energy while you're running"
    play sound "audio/avagameaudio/avarunpant.wav" loop
    scene fs avarun1
    with Dissolve(1.0)
    "Even with her sports top on you could see her tits bouncing after each stride, which was pretty good motivation to keep up"
    scene fs avarun2
    with Dissolve(1.0)
    "Eventually you had to slow down, you told yourself it was so you could see her ass but you were just out of shape"
    scene fs avarun3
    with Dissolve(1.0)
    "After a bit more time you were just lagging behind, but you never stopped and that was something."
    stop sound
    scene fs parknight
    with Dissolve(0.7)
    $ avaSprite = 5
    show fbava current:
        xalign 0.6 ypos 120

    show fbplayer shortstired1:
        xalign 0.35 ypos 120
    voice "audio/avagameaudio/avagoodjob.wav"
    ava "Hah...hah...we did it good job."
    ava "{i}I definitely ran harder than I normally would, felt like he was just chasing me during that last bit{/i}"
    $ avaSprite = 3
    player "Yeah no....no problem hah...."
    ava "Since this is your first run honestly I wasn't expecting you to keep up but I'm impressed."
    $ avaSprite = 2
    show fbplayer shortstired2:
        xalign 0.35 ypos 120
    player "Hey I gotta k..hah...keep you on your toes, can't let you slip up your practice."
    $ avaSprite = 3
    ava "Haha thanks, whenever I convinced one of the girls to run with me I always had to stop at least once."
    $ avaSprite = 2
    player "{i}Nice I can see her clevage. This run was totally worth it.{/i}"
    $ avaSprite = 5
    ava "Man I'm sweating something fierce!"
    ava "Brrr I didn't notice it cause the run kept me warm but it's actually getting kinda cold out now..."
    show fbplayer shortsboner:
        xalign 0.4 ypos 120
    with move
    player "{i}Doth mine eyes deceive me? Her nipples are hard...{/i}" # spelling mistake lmao
    ava "{i}Why is he getting so close to me? I'm-{/i}"
    $ avaSprite = 17
    ava "{i}Oh my god my nips are freaking hard as a rock! No wonder he looks so freaking horny.{/i}"
    $ avaSprite = 5
    ava "Um....ah..."
    player "Hmm?"
    $ avaSprite = 17
    ava "{i}He's looking at me...looking at my tits...his cock is probably hard right now..{/i}"
    show fbplayer shortsbonertalk:
        xalign 0.4 ypos 120
    player "You alright?"
    show fbplayer shortsboner:
        xalign 0.4 ypos 120
    ava "{i}His gaze is piercing right through me...he'd only do this if he thought I was hot right? W-Which means he wants to fuck me right?{/i}"
    ava "{i}E-Even though he's dating Mia he wants to fuck ME! Wants to to pound my pu-{/i}"
    show fbplayer shortsbonertalk at surpriseshake:
        xalign 0.4 ypos 120
    player "AVA."
    show fbplayer shortsboner:
        xalign 0.4 ypos 120
    $ avaSprite = 5
    show fbava current at surpriseshake:
        xalign 0.6 ypos 120
    ava "Huh?!"
    ava "Oh sorry one..hah..sec..."
    $ avaSprite = 6
    voice "audio/avagameaudio/avastretch.wav"
    show fbplayer shortsbonertalk:
        xalign 0.4 ypos 120
    player "What are you doing?"
    show fbplayer shortsboner:
        xalign 0.4 ypos 120
    ava "Just s-some post run stretches. You should do em too."
    show fbplayer shortsboner:
        xalign 0.35 ypos 120
    with move
    player "Yeah okay...good idea."
    player "{i}Is it just me or is she streching so I can see her tits better against her clothes?{/i}"
    $ avaSprite = 7
    ava "Ahhhnn..."
    player "{i}Well that pretty much answered my question.{/i}"
    $ avaSprite = 6
    ava "UHN....OOOhhh yeah that's good right theeeere..."
    player "{i}She's not even trying to hide it!{/i}"
    $ avaSprite = 8
    show fbava current at surpriseshake:
        xalign 0.6 ypos 120

    ava "Oh my god you...you have a boner!"
    show fbplayer shortsbonerlookdown:
        xalign 0.35 ypos 120
    player "What?"
    player "Oh."
    show fbplayer shortsboner:
        xalign 0.35 ypos 120
    player "Well if you're not going to be subtle why should I?"
    ava "What..What do you mean? I don't kno-"
    show fbplayer shortsbonerpoint:
        xalign 0.35 ypos 120
    player "You're one step away from flashing me and all I've done is LOOK at you."
    show fbplayer shortsboner:
        xalign 0.35 ypos 120
    $ avaSprite = 5
    ava "Fuck....you're right..I'm terrible. Jesus that thing is massive."
    player "Thank you. But Ava you need to relax, you're not terrible. We didn't even do anything really."
    ava "...True."
    player "We're both really tired and horny so let's just go home for tonight hmm?"
    ava "Yeah that's a good idea."
    player "Thanks for running with me, it was a real pleasure."
    ava "Oh yeah I bet it was huh."
    player "I'm not taking it back, see yah!"
    hide fbplayer shortsboner
    with Dissolve(0.7)
    ava "Man that guy, we actually get along pretty well."
    ava "Why does he have to be Mia's boyfriend god dammit!"

    $ avaphase1interaction2 = 2
    $ avaquestlog = "That was pretty tiring but fun, I should go for another run with her!"
    hide fs avasquats1
    hide avadoingsquats
    hide fbplayer
    hide fbava
    jump gotosleep

# part 3 (part 2 is unsed part3 (A) is also unused? nice bro)

label avaphase1interaction2part3B:
    hide screen uppergui
    stop music fadeout 5
    stop sound fadeout 5
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    $ avaSprite = 2
    show fbava current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Well! Here we are again huh?"
    $ playerSprite = 0
    $ avaSprite = 3
    ava "Yeah let's...get to it."
    play sound "audio/avagameaudio/avarunpant.wav" loop
    scene fs avarun1
    with Dissolve(0.7)
    "You and Ava go on another run, you felt better this time"
    scene fs avarun2
    with Dissolve(0.7)
    "You still couldn't fully keep up with her"
    scene fs avarun1
    with Dissolve(0.7)
    "But you were able to hang on much better than last time"
    "And you took in every second of her glorious ass as you could"
    stop sound
    scene fs parknight
    with Dissolve(0.7)
    show fbplayer shortstired2:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    $ avaSprite = 5
    show fbava current:
        xalign 0.6 ypos 120

    player "Hah...hah..alright!"
    ava "We did it again!"
    player "Ah...Yeah."
    ava "And this time yo-"
    show fbplayer shortsboner:
        xalign 0.35 ypos 120
    ava "....."
    $ avaSprite = 8
    ava "Dude again??"

    show fbplayer shortsbonerlookdown:
        xalign 0.35 ypos 120

    player "UGH! Man c'mon!"
    player "This is all YOUR fault."
    ava "How is it MY fault you're creeping on me??"
    player "One, don't act like you don't like it."
    player "And two, you could've just ran beside me the whole time!"
    ava "I don't understand why YOU'RE the one getting angry."
    player "I had to go HOME like this last time."
    $ avaSprite = 3
    ava "Haha what?"
    $ avaSprite = 2
    player "I walked home, with a giant hard dick poking out of my shorts the ENTIRE time."
    player "You know how many weird looks I got? Pretty sure someone called the cops at some point too."
    $ avaSprite = 3
    ava "You were hard the entire time?"
    $ avaSprite = 2
    player "Yes Ava. You really turn me on if that wasn't obvious by now!"
    ava "...."
    player "Well I'm not doing it again, I'm not going home like this."
    $ avaSprite = 3
    ava "Well what are you gonna do?"
    $ avaSprite = 2
    player "I guess I just...gotta take care of it."
    $ avaSprite = 3
    ava "You're gonna jack off?"
    ava "In the park!?"
    $ avaSprite = 2
    player "Please don't say it like that. But yeah I can't see any other way."
    $ avaSprite = 3
    ava "Pffft."
    $ avaSprite = 2
    player "You're gonna stand over there and keep a look out. You owe me that much."
    $ avaSprite = 3
    ava "Sigh...Fine."
    $ avaSprite = 2
    player "And...OH! I know what to do."
    $ avaSprite = 3
    ava "What?"
    $ avaSprite = 2
    player "I'm gonna call Mia, make this go a whole lot faster."
    ava "Huh..."
    image avaparkmasterbate1:
        "ava park scene cg1.png"
        0.7
        "ava park scene CG2.png"
        0.7
        repeat
    show avaparkmasterbate1
    with Dissolve(0.8)
    player "Hey Mia, I need a quick favor."
    player "Yeah I need you to talk dirty to me for a little bit. I kinda have to cum as soon as possible."
    player "Yeah you will? Where are you?"
    player "Oh and you're wearing that pink one I like?"
    player "Mmmm yeah..."
    player "Take out your tits for me."
    player "Oh I love it when you do that..."
    image avaparkmasterbate2:
        "ava park scene CG3.png"
        0.7
        "ava park scene CG5 new.png"
        0.7
        repeat
    show avaparkmasterbate2
    player "You miss my big cock? You want to choke on it again?"
    ava "{i}Damn this is getting pretty intense.{/i}"
    player "I loved the way you screamed last time, when I bent you over you remember?"
    image avaparkmasterbate3:
        "ava park scene CG4.png"
        0.5
        "ava park scene CG6 new.png"
        0.5
        repeat
    show avaparkmasterbate3
    ava "...."
    player "Yeah you took it real good, every drop I had hehe."
    ava "{i}Fuck I can't just listen to this anymore.{/i}"
    scene fs avabench5
    player "I wish you-ah...."
    player "Yeah I wish you were here..."
    player "You know I love your tits baby..."
    scene fs avabench6
    play sound "audio/avagameaudio/avasoftly.wav"
    ava "Mmmmm..."
    player "I uh...Oh..shit okay..."
    scene fs avabench7
    ava "Ahn..."
    player "Fuck..yeah this is really turning me on..."
    player "I want fuck you so bad, just straight up ravage your tight pussy."
    scene fs avabench8
    player "Huh?"
    window hide
    pause
    scene fs avabench9
    window hide
    pause
    player "Holy shit."
    player "Your tits are amazing."
    player "Shit that did it I'm gonna fucking cu-"
    scene fs avabench10
    with vpunch
    player "AHH!"
    scene fs avabench11
    with flash
    player "Fuck this is so hot!"
    scene fs avabench12
    with Dissolve(0.7)
    player "Yeah that was it...incredible babe."
    player "Exactly what I needed."
    scene fs avabench13
    voice "audio/avagameaudio/avagiggle.wav"
    ava "Hehe."
    player "Yeah I'll talk to you later."
    scene fs avabench14player
    player "Jesus Christ."
    scene fs avabench14ava
    ava "Hahaha, good?"
    scene fs avabench14player
    player "Amazing. But what the fuck haha."
    scene fs avabench14ava
    ava "How could I just stand by and watch when you were doing that right next to me."
    ava "Had to join in."
    scene fs avabench14player
    player "You have great tits by the way."
    scene fs avabench14ava
    ava "Haha I figured you felt that way after seeing them."
    ava "And since you're dating Mia and still saying that to me, it's quite the compliment."
    scene fs avabench14player
    player "Hehe, well I mean it."
    scene fs blackblank
    with Dissolve(1.0)
    "You chat with Ava for a little bit longer before going home"
    $ avaquestlog = "I was not expecting the night to end like that. I should talk to Ava again about it."
    $ avaphase1interaction2 = 3
    $ avaphase1interaction1 = 6
    jump gotosleep

# part 3C (part 4 i guess or 3?? man idk)

label avaphase1interaction2part3C:
    if whereami == "school":
        scene fs schoolhallway
        scene fs schoolhallwayzoomblur
    elif whereami == "gym":
        hide screen ava_atgym
        hide screen backbuttonGYM
        scene fs gymarea

    $ playerSprite = 10
    $ avaSprite = 0

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    #show fbava current:
    #    xalign 0.7 ypos 120
    #with Dissolve(0.5)

    show fbava current:
        xalign 0.5 ypos 120
    with Dissolve(0.5)

    player "Hey."
    $ playerSprite = 0
    $ avaSprite = 11
    voice "audio/avagameaudio/avaohuh.wav"
    ava "Oh! Um hey."
    $ avaSprite = 14
    ava "....."
    $ avaSprite = 12
    $ playerSprite = 16
    player "So...the other night was fun."
    $ playerSprite = 8
    $ avaSprite = 1
    ava "Haha yeah um, it was."
    $ avaSprite = 0
    $ playerSprite = 8
    ava "...."
    $ avaSprite = 12
    $ playerSprite = 0
    player "...."
    $ playerSprite = 1
    player "Kinda weird to be awkward about it now right?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Yeah haha, I uh...in the moment it was fine. But in hindsight it's like...you know?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Yeah."
    $ playerSprite = 0
    $ avaSprite = 11
    ava "Do you regret....what I..what we did?"
    $ avaSprite = 1
    ava "Haha God listen to me, you'd think we banged already or something....b-but you know what I mean."
    $ avaSprite = 0
    $ playerSprite = 1
    player "'Already' huh?"
    $ avaSprite = 14
    $ playerSprite = 0
    ava "...."
    $ playerSprite = 1
    $ avaSprite = 12
    player "Nope, not at all."
    $ playerSprite = 0
    $ avaSprite = 11
    ava "R-Really?"
    $ avaSprite = 12
    ava "{i}Was it just me feeling this way?{/i}"
    $ playerSprite = 14
    player "Well you know, there's a little bit of guilt there but..."
    $ playerSprite = 13
    player "Mainly excitement and...well arousal I guess."
    $ playerSprite = 0
    ava "{i}Oh!?{/i}"
    $ avaSprite = 11
    ava "Arousal?"
    $ avaSprite = 12
    $ playerSprite = 1
    player "I'm going to be honest Ava I didn't bust because I was on the phone with Mia, you're the one that made me cum."
    $ playerSprite = 0
    $ avaSprite = 12
    ava "{i}OH shit okay okay um fuck!{/i}"
    $ avaSprite = 11
    ava "{i}Did he really just say that? Stay calm! I don't want him knowing how happy I am.{/i}"
    $ playerSprite = 1
    player "Ava?"
    $ avaSprite = 12
    ava "{i}God why am I this way?{/i}"
    $ avaSprite = 1
    ava "W-Well."
    $ avaSprite = 14
    ava "If we're both gonna be honest."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Yeah?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "When I went home afterwards, I spent like 2 hours masturbating."
    $ avaSprite = 0
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    with move
    player "You did?"
    $ playerSprite = 0
    $ avaSprite = 13
    show fbava current:
        xalign 0.45 ypos 120
    with move
    ava "Yeah."
    $ avaSprite = 12
    $ playerSprite = 1
    player "What did you think about?"
    $ playerSprite = 0
    $ avaSprite = 14
    ava "All the things you were saying to Mia, I fantasized about you doing them to me instead."
    $ avaSprite = 12
    $ playerSprite = 1
    player "Did you scream my name?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Mmmmmmmaaybe once or twice haha."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Fuck that's so hot."
    $ playerSprite = 0
    $ avaSprite = 13
    ava "...."
    player "...."
    $ playerSprite = 1
    player "So."
    $ playerSprite = 0
    $ avaSprite = 12
    ava "Yeah..."
    $ avaSprite = 0
    $ playerSprite = 1
    if currentchapter > 1:
        player "I'll see you at the gym then?"
        $ avaSprite = 1
        ava "Uh huh, see you there haha."
        hide fbplayer current
        with Dissolve(0.5)

        $ avaSprite = 12
        show fbava current:
            xalign 0.45 ypos 120
        with Dissolve(1.0)

        ava "...."
        $ avaSprite = 14
        ava "Damn Ava. What have you gotten yourself into?"
        hide fbava current
        $ avaSprite = 0
        $ avaphase1interaction2 = 4
        $ avaquestlog = "I feel like I'm making a real connection with Ava, I should see her at the gym again."

        jump returnwhereyouare


    player "Your big race is soon. I'll try to make it."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh um yeah! Thanks."
    ava "Honestly I've been distracted lately but I still have enough time to get focused for it."
    ava "The girls are expecting a lot from me. I hear Emily's even doing some big project."
    $ avaSprite = 0
    $ playerSprite = 1
    player "I'm sure they won't be dissapointed."
    player "What do you get if you win?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Ehhh actually not that much, there's not even a trophy. They mail you a medal a week later."
    $ avaSprite = 0
    $ playerSprite = 5
    player "What are you serious??"
    $ playerSprite = 4
    $ avaSprite = 1
    ava "Yeah haha."
    $ avaSprite = 0
    $ playerSprite = 5
    player "Well then why is it such a big event?!"
    $ playerSprite = 4
    $ avaSprite = 1
    ava "It's not official but this is where all the big scouts for potential pro athletes show up for the first time."
    ava "So that's kinda why it's turned into a big deal."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Ahhh, but still. Not good enough."
    player "How's this, if you win I'll give you my own reward."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh! What do I get??"
    $ avaSprite = 0
    $ playerSprite = 13
    player "It'll be good."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh man now I'm hyped, I gotta win now!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "I'm glad."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Okay well..."
    ava "Thanks [povname]. I don't really know what for yet but thanks."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Haha no problem Ava. I'll see your sweet ass at the track meet!"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Heh alright, see you there!"

    hide fbplayer current
    with Dissolve(0.5)

    hide fbava current
    $ avaSprite = 12
    show fbava current:
        xalign 0.45 ypos 120
    with Dissolve(1.0)

    ava "...."
    $ avaSprite = 14
    ava "Damn Ava. What have you gotten yourself into?" # should be italic
    hide fbava current
    $ avaSprite = 0
    $ avaphase1interaction2 = 4
    $ avaquestlog = "I have a couple ideas for Ava's...reward. Can't wait for the track meet!"

    jump returnwhereyouare

# end chapter 1

