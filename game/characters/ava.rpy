# Ava scenes.

# Chapter 1


label avaphase1interaction1part1:
    scene fs schoolhallwayzoomblur

    $ playerSprite = 1

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)


    $ avaSprite = 0
    show fbava current:
        xalign 0.5 ypos 120


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

    ava "Oh haha no problem, for a second there I thought..."
    $ avaSprite = 1
    ava "Well nevermind. You should visit me in the afternoon, come check out the gym see if you like it."
    $ avaSprite = 4
    ava "I mean you don't look like you need to get in shape....b-but there's never anything wrong with gaining a few muscles and staying healthy!"
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
        $ avaquestlog = "{size=-25}Meet Ava at the gym beside the school during Day.{/size}"
    else:
        $ avaquestlog = "Meet Ava at the gym beside the school during Day."
    $ avaquesticon = "gui/questboxAva.png"
    $ avaphase1interaction1 = 1
    hide fs schoolhallwayzoomblur
    hide fbava
    hide fbplayer
    jump returnwhereyouare


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
    ava "Yeah these are my gym clothes. They show a bit of skin, but I don't get too hot and they're super easy to move in. I can even do one of those human pretzel things!"
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
    $ avaquestlog = "Bring $100 to the ticket machine outside the gym to buy a gym pass during Morning or Day."
    $ avaphase1interaction1 = 2
    hide fs gymarea
    hide fbava
    hide fbplayer
    jump returnwhereyouare


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


label avaphase1interaction1part3:
    scene fs outsidegym
    hide screen backbuttonGYMOUTSIDE
    if avaphase1interaction1 != 2:
        if avaphase1interaction1 >= 3:
            player "I don't want to interact with that again. *Shudders*"
        else:
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
    $ avaquestlog = "You have a gym pass. Meet Ava inside the gym during Day."
    hide screen gym_machine
    jump outsidegym


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


label giveuponava:
    player "{i}Okay I might be crossing a few too many lines here maybe I should stop.{/i}"
    menu:
        "Stop objectifying Ava":
            jump giveuponava2
        "Definitely DON'T stop objectifying Ava, look at that ass!":
            jump showmethatassava


label giveuponava2:
    player "Yeah I got it thanks."
    ava "Oh great! So should w-"
    player "Sorry Ava I don't think this is actually for me, sorry for wasting your time."
    ava "Wait what?"
    hide fs avasquats1
    hide fbplayer
    hide fbava
    jump passtime


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
    ava "Oh my god I can't deal with this right now I have the track meet to focus on. How could he flirt like that so blatantly he's dating Mia!"
    ava "And I just kept going too. Am I a bad friend? Did I like knowing he was looking at my ass like that?"
    ava "I mean it's always nice knowing boys find you attractive bu-stop stop it STOP Ava! Focus!"
    ava "Track. Meet."
    ava "I'm going to do some leg presses."
    $ avaphase1interaction1 = 4
    $ avaquestlog = "Talk to Ava at school during Morning about another workout."
    hide fs blackblank
    hide fbplayer
    hide fbava
    jump passtime


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
    $ avaquestlog = "Meet Ava at the park at Night."
    hide fs schoolhallwayzoomblur
    hide fbplayer
    hide fbava
    jump returnwhereyouare


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
    player "{i}Doth mine eyes deceive me? Her nipples are hard...{/i}"
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
    $ avaquestlog = "Meet Ava at the park again at Night."
    hide fs avasquats1
    hide avadoingsquats
    hide fbplayer
    hide fbava
    jump gotosleep


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
    $ avaquestlog = "Talk to Ava at school during Morning or at the gym during Day."
    $ avaphase1interaction2 = 3
    $ avaphase1interaction1 = 6
    jump gotosleep


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
        $ avaquestlog = "Continue exploring until Ava's track meet on day 10."

        jump returnwhereyouare


    player "Your big race is soon. I'll try to make it."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh um yeah! Thanks."
    ava "Honestly I've been distracted lately but I still have enough time to get focused for it."
    ava "The girls are expecting a lot from me. I hear Emily's even doing some big project."
    $ avaSprite = 0
    $ playerSprite = 1
    player "I'm sure they won't be disappointed."
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
    ava "Damn Ava. What have you gotten yourself into?"
    hide fbava current
    $ avaSprite = 0
    $ avaphase1interaction2 = 4
    $ avaquestlog = "Continue exploring until Ava's track meet on day 10."

    jump returnwhereyouare


# Chapter 2

label esch1_ava:

    "A little while later..."
    scene fs lockerroomblur
    with Dissolve(1.0)

    $ avaSprite = 9

    show fbava current:
        xalign 0.75 ypos 120
    with Dissolve(0.5)

    image fbjosy defaultflip = im.Flip("Sprites/josy1080default.png", horizontal=True, vertical=False)
    image fbjosy talkflip = im.Flip("Sprites/josy1080talk.png", horizontal=True, vertical=False)
    image fbava nakedfliptalk = im.Flip("Sprites/ava topless talk.png", horizontal=True)
    image fbava nakedflip = im.Flip("Sprites/ava topless 2.png", horizontal=True)

    show fbjosy talkflip:
        xalign 0.55 ypos 120
    with Dissolve(0.5)

    josy "-Oh my god, and then when he jumped!"
    josy "His foot caught the hurdle and he freakkin face-planted right into the ground hahaha."
    show fbjosy defaultflip:
        xalign 0.55
    $ avaSprite = 10
    ava "Haha holy shit, is he alright?"
    $ avaSprite = 9
    show fbjosy talkflip:
        xalign 0.55 ypos 120
    josy "His face was a MESS but the on site doctors said he'll be fine in a couple weeks."
    show fbjosy defaultflip:
        xalign 0.55 ypos 120
    $ avaSprite = 10
    ava "Well alright then I feel better about laughing then."
    $ avaSprite = 9

    show fbava pullshirt:
        xalign 0.775 ypos 120
    with Dissolve(0.5)
    window hide
    pause
    show fbava nakedtalk:
        xalign 0.75 ypos 120
    with Dissolve(0.5)
    ava "Man I can't wait to take a shower."
    show fbava naked:
        xalign 0.75 ypos 120
    show fbjosy talkflip:
        xalign 0.55 ypos 120
    josy "You smell fine if that means anything."
    show fbjosy defaultflip:
        xalign 0.55 ypos 120
    show fbava nakedtalk:
        xalign 0.75 ypos 120
    ava "It just helps me destress."
    show fbava naked:
        xalign 0.75 ypos 120
    show fbjosy talkflip:
        xalign 0.55 ypos 120
    josy "Sure, makes no difference to me."
    josy "I gotta go though, meeting Katie for shopping later."
    josy "Congrats again on your win!"
    show fbjosy defaultflip:
        xalign 0.55 ypos 120

    show fbava nakedtalk:
        xalign 0.75 ypos 120
    ava "No problem go ahead! And thanks! Congrats on your long jump win too!"
    show fbava naked:
        xalign 0.75 ypos 120

    show fbjosy talkflip:
        xalign 0.55 ypos 120
    josy "Sigh, now if only I had a man waiting at home to congratulate me by pounding my pussy raw..."
    show fbjosy defaultflip:
        xalign 0.55 ypos 120

    show fbava nakedtalk:
        xalign 0.75 ypos 120
    voice "audio/avagameaudio/avajosyhaha.wav"
    ava "Josy! Hahaha."
    show fbava naked:
        xalign 0.75 ypos 120
    show fbjosy talkflip:
        xalign 0.55 ypos 120
    josy "What? I've been so focused on this event I haven't gotten any action in fooooorever."
    josy "You're in the same boat too!"
    show fbjosy defaultflip:
        xalign 0.55 ypos 120
    show fbava nakedshyarms:
        xalign 0.75 ypos 120

    ava "oh uh..haha...yeah.."
    show fbava naked:
        xalign 0.75 ypos 120
    show fbjosy talkflip:
        xalign 0.55 ypos 120
    josy "Anyways I gotta go! Love you bye! Congrats again!"
    show fbjosy defaultflip:
        xalign 0.55 ypos 120

    show fbava nakedtalk:
        xalign 0.75 ypos 120
    ava "You too Josy."
    hide fbjosy current
    with Dissolve(0.7)
    show fbava naked:
        xalign 0.75 ypos 120
    pause
    show fbava nakedflip:
        xalign 0.9 ypos 120
    with move
    show fbava nakedfliptalk:
        xalign 0.9 ypos 120
    ava "Hah....man."
    show fbava nakedflip:
        xalign 0.9 ypos 120
    player "...."
    window hide
    pause
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.5 ypos 120
    player "Hey."
    $ playerSprite = 0
    show fbava nakedshytalk at surpriseshake:
        xalign 0.8 ypos 120
    voice "audio/avagameaudio/avaahh.wav"
    ava "Ahhh!"
    ava "Huh? Wait [povname]! Jesus you scared the shit out of me! W-why are you here??"
    show fbava nakedshy:
        xalign 0.8 ypos 120
    $ playerSprite = 1
    player "Sorry, it's pretty much impossible to sneakily enter a girl's locker room without seeming like a creep."
    show fbava nakedshytalk:
        xalign 0.8 ypos 120
    $ playerSprite = 0
    ava "Mind answering the question??!"
    show fbava nakedshy:
        xalign 0.8 ypos 120
    $ playerSprite = 1
    player "What do you mean? I'm here for your reward?"
    show fbava nakedshytalk:
        xalign 0.8 ypos 120
    $ playerSprite = 0
    ava "W-What?"
    show fbava nakedshy:
        xalign 0.8 ypos 120

    $ playerSprite = 1
    player "Is that pose really necessary?"
    $ playerSprite = 0
    ava "..."
    $ playerSprite = 1
    player "I've already seen them."
    $ playerSprite = 0
    ava "{i}He has a point I guess....{/i}"
    show fbava nakedshyarms:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    pause
    show fbava nakedarmsdown:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Fuck you're hot."
    $ playerSprite = 0
    show fbava nakedshyarms:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    ava "{i}I don't know what to do, I should be angry and creeped out right?{/i}"
    ava "{i}I was just fooling around before, I didn't think..it'd come to this so quickly...{/i}"
    show fbplayer pullshirttalk:
        xalign 0.5 ypos 120
    with Dissolve(0.5)
    player "So, like I said. I'm here to give you your reward."
    show fbplayer pullshirt:
        xalign 0.5 ypos 120
    show fbava nakedarmsdowntalk:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    ava "Why are you taking off y-your shirt?"
    show fbava nakedarmsdownnotalk:
        xalign 0.8 ypos 120
    show fbplayer pullshirttalk:
        xalign 0.5 ypos 120
    player "You know why Ava."
    show fbplayer pullshirt:
        xalign 0.5 ypos 120
    show fbava nakedshyarms:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    ava "Oh...o-okay.."
    "How would you like to proceed?"

    menu:
        "{color=#3eab33}Romantic{/color}":
            jump avachapter1rom
        "{color=#dd3939}Naughty{/color}":
            jump avachapter1naughty


label avachapter1rom:
    show fbplayer shirtless:
        xalign 0.5 ypos 120
    with Dissolve(0.5)
    show fbava nakedturnedon:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    ava "{i}Oh god he's so fucking hot!{/i}"
    show fbplayer shirtlesstalk:
        xalign 0.6 ypos 120
    with move

    player "You know I could probably spend hours just enjoying your tits."
    player "But that's not gonna make you cum will it?"
    show fbplayer shirtless:
        xalign 0.6 ypos 120
    show fbava nakedshyarms:
        xalign 0.9 ypos 120
    with move
    voice "audio/avagameaudio/avalittlemoan.wav"
    ava "c-cum?"
    show fbplayer shirtless:
        xalign 0.8 ypos 120
    with move
    show fbava nakedturnedon:
        xalign 0.9 ypos 120
    ava "Oh god..."
    show fbplayer shirtlesstalk:
        xalign 0.8 ypos 120
    player "Yeah."
    hide fbplayer shirtlesstalk
    hide fbava nakedturnedon
    scene fs avaec11ava
    with Dissolve(1.2)
    ava "Fuck [povname] we really shouldn't..."
    scene fs avaec11player
    player "I'm gonna make you feel real good Ava."
    scene fs avaec12
    with Dissolve(0.5)
    ava "{i}Is this really happening??!{/i}"

    player "I ever mention how sexy I think your tan lines are?"
    ava "Dude I just ran a race I'm all sweaty..."
    scene fs avaec13B
    with Dissolve(0.7)
    $ hiden_textbox = True
    player "Don't care."
    image mcfingeringavalocker:
        "ava end A CG4.png"
        0.7
        "ava end a cg4B.png"
        0.7
        repeat
    show mcfingeringavalocker
    voice "audio/avagameaudio/avadude.wav"
    ava "D-Dude!"
    play sound "audio/avagameaudio/avafingered.wav" loop

    image mcfingeringavalocker2:
        "ava end A CG2 finger1.png"
        0.7
        "ava end A CG2 finger2.png"
        0.7
        repeat
    show mcfingeringavalocker2
    window hide
    pause
    ava "Oh fuck you're really fingering me."
    player "Mhmm."
    image mcfingeringavalocker3:
        "ava end A cg5 finger1.png"
        0.7
        "ava end A cg5 finger2.png"
        0.7
        repeat
    show mcfingeringavalocker3
    ava "Uhn...and you're pretty good at it."
    player "Mhmm."
    ava "fffffuck."
    player "By the way I haven't seen you with your hair down before, it looks nice."
    ava "T-Thanks but now's really not the tim-"
    image mcfingeringavalocker4:
        "ava end A fingermoan1.png"
        0.3
        "ava end A fingermoan2.png"
        0.3
        repeat
    show mcfingeringavalocker4
    stop sound
    voice "audio/avagameaudio/avaohmygod.wav"
    ava "Oh my god [povname] you're gonna make me fucking cum!"
    player "Yeah you're gonna cum for me?"
    voice "audio/avagameaudio/avamoan.wav"
    ava "Ahn!"
    scene fs avaec14c
    with vpunch
    ava "SHIT! What the hell!"
    scene fs avaec16
    with vpunch
    ava "AHH! T-That's my clit."
    scene fs avaec17
    with Dissolve(0.7)
    play sound "audio/avagameaudio/avamoaninglocker.wav"
    ava "Fuck fuck fuck that feels so good!"
    ava "{i}Does he eat out Mia like this? Jesus christ!{/i}"
    scene fs avaec18
    with Dissolve(0.7)
    ava "{i}Ahn...and he's still fingering my G-spot too...{/i}"

    image avasboobgrope:
        "ava end angle B cg9.png"
        1.0
        "ava end angle B cg10.png"
        1.0
        repeat
    show avasboobgrope
    with Dissolve(1.0)
    ava "Oh..hah...hah..."
    ava "{i}Now he's...grabbing my boobs..{/i}"
    ava "You really have a thing for tits huh?"
    player "Euah."
    ava "Hehe hard to talk with my wet pussy in your mouth?"
    voice "audio/avagameaudio/avamoanokayokay.wav"
    scene fs avaec111
    with vpunch
    ava "AHHHN haha okay okay sorry!"
    ava "God [povname] I'm so close!"
    ava "I'm gonna c-"
    scene fs avaec112
    with vpunch
    josy "Sup I forgot my sho-"
    scene fs avaec112b
    josy "ooeeesss...."
    ava "...."
    scene fs avaec112
    josy "OH. MY. GOD."
    scene fs avaec112c
    ava "Dude! S-Someone's here why are you still going!??"
    josy "I didn't know you were such a slut Ava haha."
    josy "Is this why you wanted to stay behind for your 'shower'?"
    scene fs avaec112
    voice "audio/avagameaudio/avano.wav"
    ava "No! Josy please just-"
    scene fs avaec113
    with vpunch
    play sound "audio/avagameaudio/avabigorgasm.wav"
    ava "AHHNNN!!!"
    scene fs avaec114
    with vpunch
    ava "I'M CUMMING!!!!"
    josy "That guy's pretty hot..."
    josy "{i}Looks like he knows what he's doing too haha.{/i}"
    ava "OOHHH FUCK!"
    josy "I'll grab my shoes later...you two enjoy yourselves."
    ava "[povname]!!"
    scene fs avaec115
    with Dissolve(1.0)
    ava "Hah...hah..."
    scene fs avaec115b
    with Dissolve(0.7)
    ava "Dude I just came all over your face you can stop now."
    scene fs avaec116
    with Dissolve(0.5)
    player "Heh that was pretty good wasn't it?"
    scene fs avaec117
    ava "I mean yeah that was amazing, pretty much the biggest orgasm of my life."
    player "Are you into being watched? Cause you got like REALLY wet whe-"
    scene fs avaec116
    voice "audio/avagameaudio/avaahh.wav"
    ava "Wait no stop! We have a problem!"
    scene fs avaec117b
    player "What you mean?"
    ava "Josy's like the BIGGEST gossiper I know dude."
    ava "She's gonna tell everyone that she saw you going down on me garanteed."
    ava "UGH."
    player "Well does she know who I am?"
    ava "No I...I don't think so."
    scene fs avaec116
    player "Then we're fine. Don't worry about it."
    ava "Shit I hope so..."
    "Loud Voices" "Alright team let's hit the showers great work today!"
    player "Looks like I better go."
    scene fs avaec117
    with Dissolve(0.7)
    ava "Yeah um...thanks."
    player "Did you just thank me for eating you out?"
    scene fs avaec116
    ava "I...."
    player "Haha, bye Ava."
    voice "audio/avagameaudio/avabye.wav"
    ava "Bye..."
    scene fs blackblank
    with Dissolve(1.0)
    ava "{i}He's right...I don't think I have any regrets.{/i}"
    ava "{i}I know I should be mad at him, probably should've rejected him the second he walked into the room.{/i}"
    ava "{i}But I didn't...and he really did give me the best orgasm I've ever had.{/i}"
    ava "{i}Whatever we have, whatever this is...{/i}"
    ava "{i}I don't think I want it to stop.{/i}"

    scene fs trackmeet
    with Dissolve(1.0)

    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    show fbolivia current:
        xalign 0.8 ypos 120
    show fbmia current:
        xalign 0.65 ypos 120
    show fbemily current:
        xalign 0.9 ypos 120
    with Dissolve(0.5)


    $ emilySprite = 1
    emily "Man what a race!"
    $ emilySprite = 0
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    sophia "Not just Ava's too, our school did so well!"
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 1
    mia "I'm so proud!"
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk:
        xalign 0.4 ypos 120
    charlotte "Ava's taking a while to change."
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ emilySprite = 1
    emily "Yeah it has been a bit."
    $ emilySprite = 0
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    show fbcharlotte current:
        xalign 0.33 ypos 120
    show fbsophia current:
        xalign 0.5 ypos 120

    josy "Hey girls! It's been a while."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ emilySprite = 1
    emily "Josy! It has been long, congratulations on your win!"
    $ emilySprite = 0
    $ sophiaSprite = 1
    sophia "You did awesome!"
    $ sophiaSprite = 0
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "Thanks I appreciate it! If you guys are waiting on Ava she might be a while."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ emilySprite = 2
    emily "Oh? Howcome."
    $ emilySprite = 0
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "She's got some company in the locker room, CONGRATULATING her on the win hehe."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ charlotteSprite = 6
    charlotte "A-Are you talking about a boy? What do you mean 'congratulating'?"
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "Oh Charlotte, still so innocent. He's eating out her pussy like a roast beef sandwich."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    "Everyone" "...."
    charlotte "I....what?"
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "You know, cunnilingus?"
    show fbjosy cuniflip:
        xalign 0.2 ypos 120
    josy "Euulelelelele!"
    $ charlotteSprite = 8
    charlotte "I-I know what you mean!"
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ emilySprite = 2
    emily "A-Ava's really doing um...naughty stuff inside the locker room right now?"
    $ miaSprite = 4
    mia "Good for her!"
    $ miaSprite = 0
    $ sophiaSprite = 4
    sophia "But she's making us wait!"
    $ sophiaSprite = 3
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "In her defense I'd make you wait too, the guy was a grade A hotty haha."
    josy "Anyways I gotta go get ready to meet up with Katie soon, Mia is she still good to go tonight?"
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ miaSprite = 1
    mia "Yup she said she'll meet you at the usual place."
    $ miaSprite = 0
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "Great! Bye girls, nice seeing you again."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    "Everyone" "Bye Josy."
    hide fbjosy defaultflip
    with Dissolve(0.7)
    $ emilySprite = 2
    emily "L-Let's just....um."
    emily "Meet up with her later?"
    $ emilySprite = 0
    $ miaSprite = 1
    mia "Sure!"
    $ miaSprite = 0
    $ charlotteSprite = 6
    charlotte "O-Okay."
    $ charlotteSprite = 0
    $ sophiaSprite = 2
    sophia "L-Let's go then.."
    $ oliviaSprite = 1
    olivia "I literally do not care."
    $ oliviaSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    $ avaquestlog = "Visit Ava at the gym during Morning in chapter 2."
    $ endchapter1_trigger = "1 ava romantic"
    $ avaphase1interaction3 = 10


    jump startofchapter2


label avachapter1naughty:
    window hide
    pause
    show fbplayer pullshirt:
        xalign 0.25 ypos 120
    with move
    show fbava nakedarmsdownnotalk:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    ava "W-what are you.."
    show fbplayer pullshirtdick:
        xalign 0.25 ypos 120
    with Dissolve(0.5)
    player "..."
    show fbava nakedarmsdownnotalk:
        xalign 0.7 ypos 120
    with move
    ava "{i}Fuck me I forgot how big it is...{/i}"
    show fbplayer shirtlessdick:
        xalign 0.25 ypos 120
    with Dissolve(0.5)
    show fbava nakedarmsdownnotalk:
        xalign 0.6 ypos 120
    with move
    ava "{i}And he's hard already?{/i}"
    ava "{i}It turns me on so much knowing how he likes my body.{/i}"

    show fbplayer shirtlessdicktalk:
        xalign 0.25 ypos 120
    player "Well?"
    show fbava nakedarmsdownnotalk:
        xalign 0.5 ypos 120
    with move
    show fbplayer shirtlessdick:
        xalign 0.25 ypos 120
    ava "?"
    show fbplayer shirtlessdicktalk:
        xalign 0.25 ypos 120
    player "What are you waiting for?"
    player "Come get your reward."
    show fbplayer shirtlessdick:
        xalign 0.25 ypos 120
    show fbava nakedarmsdown:
        xalign 0.45 ypos 120
    with move
    voice "audio/avagameaudio/avalittlemoan.wav"
    ava "Hah..I um.."
    show fbava nakedarmsdowntalk:
        xalign 0.4 ypos 120
    with move
    ava "Okay."
    scene fs blackblank
    with Dissolve(1.0)
    ava "Oh! One second, let me put my hair up."
    player "?"
    ava "So...I can suck your cock easier."
    player "Atta girl."

    scene fs avaec1b1
    with Dissolve(0.7)
    window hide
    ava "{i}I can't believe I'm about to do this.{/i}"
    ava "{i}But I can't stop myself.{/i}"
    scene fs avaec1b2
    with Dissolve(0.7)
    player "Show me how good you are Ava."
    scene fs avaec1b1
    with Dissolve(0.7)
    ava "...."
    scene fs avaec1b3
    with Dissolve(0.7)
    voice "audio/avagameaudio/avammm.wav"
    ava "Mmmmm."
    ava "{i}Sorry Mia!{/i}"
    player "There you go..."
    scene fs avaec1b4
    with Dissolve(0.7)
    play sound "audio/avagameaudio/avablowjob1.wav"
    ava "Uungh!"
    player "Fuck that's it you fucking slut."
    player "Suck my cock."
    scene fs avaec1b5
    with Dissolve(0.7)
    window hide
    pause
    player "Fuck yes! Show me you're worth cheating on Mia for!"
    ava "{i}No that's not what I want!{/i}"
    ava "{i}B-But I can't stop myself, this dick tastes so good!{/i}"
    player "Keep up that pace you backstabbing slut."
    scene fs avaec1b6
    josy "Hey sorry I forgot my shoes!"
    scene fs avaec1b7b
    with Dissolve(0.7)
    josy "....."
    josy "OH MY GOD. Ava??!!"
    scene fs avaec1b7
    with Dissolve(0.7)
    ava "Mnnnhh!!"
    player "The fuck do you think you're doing? Keep going."
    scene fs avaec1b8b
    with Dissolve(0.7)
    window hide
    pause
    play sound "audio/avagameaudio/avablowjob1.wav"
    josy "Holy shit..."
    scene fs avaec1b8
    with Dissolve(0.7)
    josy "Didn't know you were such a slut Ava haha."
    scene fs avaec1b11
    with Dissolve(0.7)
    window hide
    pause
    player "You like it when your friend is watching you Ava?"
    josy "Don't mind me!"
    player "Haha she's sucking extra hard now, you want my cum that badly?"
    scene fs avaec1b8
    with Dissolve(0.7)
    josy "God that cock is huge!"
    player "Thanks."
    scene fs avaec1b9
    with Dissolve(0.7)
    window hide
    pause
    ava "UUGGHNN!!"
    josy "Haha look at her choking on it!"
    player "Oh fuck that's it!!"
    scene fs avaec1b12
    with Dissolve(0.7)
    player "Take my cum down your fucking throat!"
    window hide
    pause
    scene fs avaec1b13
    with Dissolve(0.7)
    play sound "audio/avagameaudio/avabjgulp.wav"
    ava "*gulp*....*gulp*"
    player "Oh fuck."
    player "Swallow as much as you can. Convince me you're better than Mia is!"
    josy "{i}Mia?{/i}"
    window hide
    pause
    josy "Hehe well I think I better get going, I'll get my shoes later."
    player "Bye baby."
    josy "Have fun!"
    scene fs avaec1b10
    with Dissolve(0.7)
    play sound "audio/avagameaudio/avarunpant.wav"
    ava "Hah...hah...hah."
    player "You have fun?"
    ava "That...hah..she's.."
    player "Hmm?"
    ava "Josy...biggest gossiper I know..hah.."
    stop sound
    ava "Not good."
    player "You still have some in your mouth, swallow it."
    scene fs avaec1b10b
    with Dissolve(0.7)
    ava "*Gulp*"
    player "Good."
    player "Don't worry about your little friend. She doesn't know who I am, we'll be fine."
    scene fs avaec1b10
    with Dissolve(0.7)
    ava "Okay...hah..."
    scene fs avaec1b10b
    with Dissolve(0.7)
    player "You look good covered in my cum Ava."
    scene fs avaec1b10
    with Dissolve(0.7)
    ava "T-Thanks."
    scene fs avaec1b10b
    with Dissolve(0.7)
    player "I'll see you later."
    scene fs avaec1b10
    with Dissolve(0.7)
    voice "audio/avagameaudio/avabye.wav"
    ava "Bye."

    scene fs trackmeet
    with Dissolve(1.0)

    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    show fbolivia current:
        xalign 0.8 ypos 120
    show fbmia current:
        xalign 0.65 ypos 120
    show fbemily current:
        xalign 0.9 ypos 120
    with Dissolve(0.5)


    $ emilySprite = 1
    emily "Man what a race!"
    $ emilySprite = 0
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    sophia "Not just Ava's too, our whole school did so well!"
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 1
    mia "I'm so proud!"
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk:
        xalign 0.4 ypos 120
    charlotte "Ava's taking a while to change."
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ emilySprite = 1
    emily "Yeah it has been a bit."
    $ emilySprite = 0
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    show fbcharlotte current:
        xalign 0.33 ypos 120
    show fbsophia current:
        xalign 0.5 ypos 120


    josy "Hey girls! It's been a while."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ emilySprite = 1
    emily "Josy! It has been long, congratulations on your win!"
    $ emilySprite = 0
    $ sophiaSprite = 1
    sophia "You did awesome!"
    $ sophiaSprite = 0
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "Thanks I appreciate it! If you guys are waiting on Ava she might be a while."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ emilySprite = 2
    emily "Oh? Howcome."
    $ emilySprite = 0
    show fbjosy smileflip:
        xalign 0.2 ypos 120
    josy "She's taking her reward a bit early if you know what I mean hehe."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ charlotteSprite = 6
    charlotte "W-What are you saying?"
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "Oh Charlotte, still so innocent. She's choking on some dude's cock."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120

    $ miaSprite = 10
    $ emilySprite = 2
    $ sophiaSprite = 2

    charlotte "...."
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "Sucking on some trouser snake?"
    show fbjosy defaultflip:
        xalign 0.2 ypos 120

    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    "Everyone" "...."
    charlotte "I....what?"
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "C'mon guys, a blowjob? Hello?"
    image fbjosy bjflip = im.Flip("Sprites/josy1080bj.png", horizontal = True)
    show fbjosy bjflip:
        xalign 0.2 ypos 120
    josy "Unngh unngh!"
    $ charlotteSprite = 8
    charlotte "I-I know what you mean!"
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ emilySprite = 2
    emily "A-Ava's really doing um...naughty stuff inside the locker room right now?"
    $ miaSprite = 4
    mia "Good for her!"
    $ miaSprite = 0
    $ sophiaSprite = 4
    sophia "But she's making us wait!"
    $ sophiaSprite = 3
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "In her defense I'd make you wait too, the guy was a grade A hotty haha."
    josy "Anyways I gotta go get ready to meet up with Katie soon, Mia is she still good to go tonight?"
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    $ miaSprite = 1
    mia "Yup she said she'll meet you at the usual place."
    $ miaSprite = 0
    show fbjosy talkflip:
        xalign 0.2 ypos 120
    josy "Great! Bye girls, nice seeing you again."
    show fbjosy defaultflip:
        xalign 0.2 ypos 120
    "Everyone" "Bye Josy."
    hide fbjosy defaultflip
    with Dissolve(0.7)

    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    with Dissolve(0.7)

    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    with Dissolve(0.7)

    $ emilySprite = 2
    emily "L-Let's just....um."
    emily "Meet up with her later?"
    $ emilySprite = 0
    $ miaSprite = 1
    mia "Sure!"
    $ miaSprite = 0
    show fbcharlotte surpriseflip:
        xalign 0.4 ypos 120
    charlotte "O-Okay."
    $ charlotteSprite = 0
    $ sophiaSprite = 2
    sophia "L-Let's go then.."
    $ oliviaSprite = 1
    olivia "I literally do not care."
    $ oliviaSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    $ avaquestlog = "Visit Ava at the gym during Morning in chapter 2."
    $ endchapter1_trigger = "1 ava naughty"
    $ avaphase1interaction3 = 10


    jump startofchapter2


label avaphase2interaction1part1:
    hide screen ava_atgym
    hide screen backbuttonGYM

    $ playerSprite = 1
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    player "Hey you!"
    $ playerSprite = 0

    $ avaSprite = 1
    show fbava current:
        xalign 0.5 ypos 120
    with Dissolve(0.5)

    ava "[povname], hey!"
    ava "I'm so glad to see you here!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Well I came to see YOU so feelings mutual."
    $ playerSprite = 0
    $ avaSprite = 4
    ava "Aww dude!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Hey don't go blushing on me now haha"
    $ avaSprite = 1
    ava "Ahh i-it might happen haha."
    ava "I'm just gonna be straight up with you."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Oh?"
    $ playerSprite = 0
    $ avaSprite = 4
    ava "I'm still kinda...being effected by our last interaction so to speak haha."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Oh uh, well yeah I get that."
    player "If I'm being honest too, half the reason I came here was to talk to you about it."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh yeah? I'm not good with like...feelings and stuff I prefer to have them all out in the open."
    ava "Everybody shows their cards you know?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "100 percent Ava. I'm all for that."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "W-Well that's great then."
    ava "How should we s-"
    $ avaSprite = 0
    josy "Hey girl!!"
    $ josySprite = 0
    show fbjosy current:
        xalign 0.7 ypos 120
    show fbava blushfliptalk at surpriseshake:
        xalign 0.6 ypos 120
    $ avaSprite = 1
    ava "Gah! Shit Josy!"
    show fbava defaultflip:
        xalign 0.6 ypos 120
    $ josySprite = 1
    josy "Hehe sorry!"
    $ josySprite = 0
    show fbava defaultfliptalk:
        xalign 0.6 ypos 120
    ava "It's...hah. it's fine."
    show fbava defaultflip:
        xalign 0.6 ypos 120
    $ josySprite = 1
    josy "Hello there!"
    $ josySprite = 0
    $ playerSprite = 1
    player "Hey Josy, nice to...meet you formally."
    $ playerSprite = 0

    $ josySprite = 1
    josy "Come to the gym?"
    $ josySprite = 0
    $ playerSprite = 1
    player "Yessir."
    $ playerSprite = 0
    $ josySprite = 1
    josy "To work out? Or to see Ava?"
    $ josySprite = 0
    $ playerSprite = 16
    player "T-To work out. Talking with Ava is a nice bonus."
    $ playerSprite = 0
    $ avaSprite = 1
    show fbava blushfliptalk at surpriseshake:
        xalign 0.6 ypos 120
    ava "Y-Yup! Just talking normal....talk."
    $ avaSprite = 14
    show fbava current:
        xzoom -1.0
    $ josySprite = 1
    josy "Uh huh..."
    josy "Who are you dating again [povname]?"
    $ josySprite = 0
    $ playerSprite = 11
    player "...."
    $ playerSprite = 16
    player "Mia."
    $ playerSprite = 0
    $ josySprite = 1
    $ avaSprite = 15
    josy "Ahhhhh yes that's right that's right. So silly of me to forget."
    $ josySprite = 0
    $ playerSprite = 1
    player "It's...no problem."
    $ playerSprite = 0
    $ josySprite = 1
    josy "It's honestly my own fault."
    $ josySprite = 0
    $ playerSprite = 1
    player "What do you mean?"
    $ playerSprite = 0
    $ josySprite = 1
    josy "Guys tend to...forget they're dating someone when they're around me."
    $ josySprite = 0
    $ playerSprite = 11
    $ avaSprite = 11
    player "{i}Woah this girl is naughty!{/i}"
    show fbava current:
        xzoom -1.0
    ava "{i}This girl is dangerous!{/i}"
    $ avaSprite = 1
    ava "Okay alright Josy I think that's enough, [povname] and I need to.."
    $ avaSprite = 0
    $ josySprite = 1
    josy "You need to?"
    $ josySprite = 0
    $ avaSprite = 1
    ava "Uh, hit the yoga room! Yeah we're gonna go in there...do some yoga."
    show fbava current:
        xzoom 1.0
    ava "Aren't we [povname]?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Yeah yeah, sorry Josy. Nice talking to you."
    $ playerSprite = 0
    $ josySprite = 1
    josy "I'm available for more than talking when you're free."
    $ josySprite = 0
    $ playerSprite = 1
    player "Yeah sure-"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Nope! Nope he's super busy!"
    ava "All the time!"
    show fbava current:
        xalign 0.4 ypos 120
    with move
    ava "Okay c'mon let's go!"
    $ avaSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    "You grab your gym clothes out of your car and head to the yoga room with ava"
    scene fs avayoga1ava
    with Dissolve(0.7)
    player "....."
    scene fs avayoga1player
    player "Uh Ava?"
    scene fs avayoga1ava
    voice "audio/avagameaudio/avahmmm.wav"
    ava "Hmmm?"
    scene fs avayoga1player
    player "What are you doing?"
    scene fs avayoga1ava
    ava "Downward dog!"
    scene fs avayoga1player
    player "Not that I mind, but does it have to be right up against my crotch?"
    scene fs avayoga1ava
    ava "Oh! My bad haha."
    scene fs avayoga1a
    ava "{i}I gotta take his mind off of Josy. It wouldn't be the first time she's snagged a guy away from me!{/i}"
    scene fs avayoga2b
    with Dissolve(0.5)
    ava "There we go."
    scene fs avayoga2a
    ava "{i}The fact that I really like this one, and that he's already Mia's boyfriend makes things a lot more complicated.{/i}"
    scene fs avayoga2b
    ava "Can you push down on my ass to help me stretch?"
    scene fs avayoga3a
    with Dissolve(0.3)
    player "Sure."
    scene fs avayoga3b
    voice "audio/avagameaudio/avaoh.wav"
    ava "Oh...."
    scene fs avayoga3a
    ava "That's not..."
    scene fs avayoga3b
    ava "What..."
    scene fs avayoga3a
    ava "I meant..."
    scene fs avayoga3b
    player "Instructions unclear."
    scene fs avayoga4a
    with Dissolve(0.5)
    voice "audio/avagameaudio/avagiggle.wav"
    ava "Hehe."
    scene fs avayoga4b
    ava "You are being bad."
    player "Heh sorry I can't help it."
    scene fs avayoga5player
    with Dissolve(0.5)
    player "You know I came here to have a serious conversation with you."
    scene fs avayoga5ava
    ava "Oh really?"
    scene fs avayoga5player
    player "Yeah I swear!"
    player "But I just keep getting distracted."
    scene fs avayoga5ava
    ava "Then let's do an exercise that won't distract you."
    ava "Grab my butt!"
    scene fs avayoga6b
    with vpunch
    ava "There!"
    scene fs avayoga6a
    player "I'm pretty sure this'll be very distracting for me"
    scene fs avayoga6b
    ava "It'll be fine, now hold me tightly!"
    scene fs avayoga7
    with Dissolve(0.5)
    voice "audio/avagameaudio/avagrunt1.wav"
    ava "Huu!"
    scene fs avayoga6b
    with Dissolve(0.5)
    voice "audio/avagameaudio/avagrunt2.wav"
    ava "Haa!"
    ava "There see?"
    scene fs avayoga6a
    player "Hmmm. Okay."
    scene fs avayoga7
    with Dissolve(0.5)
    voice "audio/avagameaudio/avagrunt1.wav"
    ava "Hup!"
    scene fs avayoga6b
    with Dissolve(0.5)
    voice "audio/avagameaudio/avagrunt2.wav"
    ava "Haa!"
    scene fs avayoga7
    with Dissolve(0.5)
    voice "audio/avagameaudio/avagrunt1.wav"
    ava "Hup!"
    scene fs avayoga8
    with Dissolve(0.5)
    ava "See it's not..."
    scene fs avayoga6b
    with Dissolve(0.5)
    ava "D-Distracting..."
    scene fs avayoga7
    with Dissolve(0.5)
    ava "...."
    scene fs avayoga8
    with Dissolve(0.5)
    voice "audio/avagameaudio/avagrunt2.wav"
    player "Yeah..."
    scene fs avayoga6a
    with Dissolve(0.5)
    ava "...."
    player "...."
    scene fs avayoga9
    with Dissolve(0.5)
    pause
    scene fs avayoga10a
    play sound "audio/avagameaudio/avamakeout.wav" loop
    ava "MMMMH!"
    player "MMHFF!"
    scene fs avayoga10b
    ava "HHNG!"
    scene fs avayoga11
    with Dissolve(0.7)
    stop sound
    play sound "audio/avagameaudio/avahardpant.wav"
    ava "Hah...hah.."
    player "Fuck...hah.."
    scene fs avayoga10a
    with Dissolve(0.5)
    play sound "audio/avagameaudio/avamakeout.wav" loop
    ava "Ahn..."
    scene fs blackblank
    with Dissolve(1.0)
    player "I think we're gonna have that serious conversation later."
    ava "Um yeah...totally."
    stop sound
    $ josiedaycheck = dayNumber
    $ avaquestlog = "Return to your bedroom during Morning on a later day for Ava's message."
    $ avaphase2interaction1 = 1
    $ avadaycheck = dayNumber
    jump gym


label avaphase2interaction2part1:
        hide screen uppergui
        "Vvvvpp vvvvppp"
        player "Huh?"
        $ playerSprite = 2
        show fbplayer current:
            xalign 0.5 ypos 120
        with Dissolve(0.5)
        ava "{cps=25}Need help. Freaking out. Can't ask girls.{/cps}"
        player "{i}It's From Ava. Is she okay?{/i}"
        player "{cps=25}Woah slow down, you safe?{/cps}"
        ava "{cps=25}Yeah totally safe just...meet at cafe in afternoon please.{/cps}"
        $ playerSprite = 7
        player "Alright I guess I'll head over there."
        $ avaquestlog = "Meet Ava at Cafe Seni in Sunnyside during Day."
        $ avaphase2interaction1 = 2
        $ avaphase2interaction2 = 1
        jump playerRoom


label avaphase2interaction2part2:
    scene fs insidecafe
    with Dissolve(0.5)
    $ avaSprite = 21
    show fbava defaultflip:
        xalign 0.7 ypos 120
    ava "{i}It's fiiiiine it's gonna be fine.{/i}"
    show fbava current:
        xalign 0.5 ypos 120
    with move
    ava "{i}Shit shit shit fuck shit!{/i}"
    ava "{i}I'm gonna leave, I'm just gonna leave!{/i}"
    $ playerSprite = 15
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    player "Woah Ava! Hey I'm here what's wrong?"
    $ playerSprite = 14
    $ avaSprite = 11
    ava "Oh [povname]. Good. I think...oh man."
    $ playerSprite = 1
    $ avaSprite = 21
    player "Deep breaths. What's happening?"
    $ playerSprite = 0
    $ avaSprite = 11
    ava "Ok ok so I have an interview with this big time sport recruiter"
    ava "And and and I'm like really bad under pressure."
    $ playerSprite = 1
    $ avaSprite = 21
    player "But you perform under pressure all the time! You won your race."
    $ playerSprite = 0
    $ avaSprite = 11
    ava "That's different! I can deal with stress by moving my body but when it comes to talking..."
    ava "I'm freaking out okay?! I can't do this!"
    $ playerSprite = 1
    $ avaSprite = 21
    player "Alright relax, I'll help you out don't worry, when is the interview?"
    $ playerSprite = 0
    $ avaSprite = 11
    ava "Like right now!"
    $ avaSprite = 21
    "Recruiter Guy" "Ah hello, I'm supposed to have an interview here is there anyone waiting for me?"
    $ avaSprite = 11
    ava "I'm gonna die."
    $ avaSprite = 21
    $ playerSprite = 1
    player "I got this Ava. Big smile let's go."
    $ playerSprite = 0
    scene fs blackblank
    with Dissolve(0.7)
    player "Hello sir, are you here to interview Ava?"
    "Recruiter Guy" "Yes."
    player "Follow me she's right over here."
    "Recruiter Guy" "Ah thank you."

    scene fs avainterviewscene1
    with Dissolve(0.7)
    "Recruiter Guy" "Nice place. Hello Miss Ava."
    ava "...."
    scene fs avainterviewscene1b
    player "You'll have to forgive her sir, she burnt her throat on some herbal tea."
    player "Supposed to be healthy stuff, but they don't tell you how hot to make it haha."
    scene fs avainterviewscene1c
    ava "{size=20}Sorry...{/size}"
    scene fs avainterviewscene1
    "Recruiter Guy" "Ah yes, I am fond of a good tea myself. I hope you recover soon."
    scene fs avainterviewscene1b
    player "Anyways that's why I'm here, to answer any questions you have on her behalf."
    player "I'm her boyfriend by the way, [povname]."
    scene fs avainterviewscene1
    ava "{i}Boyfriend{/i}??"
    "Recruiter Guy" "A pleasure. And totally understandable."
    "Recruiter Guy" "Let's get straight to the interview then."
    $ avajobinterview = 0
    jump avaquestion1

label avaquestion1:
    "Recruiter Guy" "Miss Ava, where do you see yourself in 5 years?"
    menu:
        "Journalist":
            jump answerjournalist
        "Mathematician":
            jump answermathematician
        "Succesful Athelete":
            jump answerathlete

    label answerjournalist:
        scene fs avainterviewscene1b
        player "Ava always wanted to be a journalist. Reporting on natural disasters and murders is really cool."
        scene fs avainterviewscene1
        "Recruiter Guy" "Oh. Okay then, moving on."
        $ avajobinterview = avajobinterview + 1
        jump avaquestion2
    label answermathematician:
        scene fs avainterviewscene3
        player "5 years?"
        scene fs avainterviewscene1b
        player "Ava's been studying real hard to be a mathematician! Calculus and square roots and all that."
        "Recruiter Guy" "I see. Moving on then."
        $ avajobinterview = avajobinterview + 1
        jump avaquestion2
    label answerathlete:
        scene fs avainterviewscene3
        player "5 years?"
        scene fs avainterviewscene1b
        player "That's going to be an Olympic year isn't it?."
        scene fs avainterviewscene1
        "Recruiter Guy" "Oh! Yes I believe so."
        scene fs avainterviewscene1b
        player "Ava doesn't just see herself participating as a professional athelete, I do too. And so should you."
        scene fs avainterviewscene1
        "Recruiter Guy" "I like the confidence, moving on."
        jump avaquestion2


label avaquestion2:
    "Why do you want to be an athlete?"
    menu:
        "The Money":
            jump answermoney
        "Feels Good":
            jump answerfeelsgood
        "The Fame":
            jump answerfame

    label answermoney:
        scene fs avainterviewscene2
        player "Top Atheletes get paid the big bucks right? What other reason is there?"
        scene fs avainterviewscene1
        "Recruiter Guy" "That's...true. Next question."
        $ avajobinterview = avajobinterview + 1
        jump avaquestion3
    label answerfeelsgood:
        scene fs avainterviewscene1b
        player "Simple. It feels good."
        scene fs avainterviewscene1
        "Recruiter Guy" "Feels good?"
        scene fs avainterviewscene1b
        player "Pushing your body to see what it's capable of, and then beating that limit tomorrow."
        player "Having the confidence to know you're hot as hell and you WORKED for that body."
        scene fs avainterviewscene1
        ava "...."
        scene fs avainterviewscene2
        player "Being able to prove you're the best with nothing but your own hard work?"
        player "It feels DAMN good."
        scene fs avainterviewscene3b
        ava "[povname]..."
        scene fs avainterviewscene1b
        player "...Is what Ava has told me."
        scene fs avainterviewscene1
        "Recruiter Guy" "Ah I see now, interesting. Next Question."
        jump avaquestion3
    label answerfame:
        scene fs avainterviewscene1b
        player "To be famous! What's better than a roaring crowd cheering you on?"
        scene fs avainterviewscene1
        "Recruiter Guy" "That's it?"
        scene fs avainterviewscene1b
        player "That's it."
        scene fs avainterviewscene1
        "Recruiter Guy" "Very well, next question."
        $ avajobinterview = avajobinterview + 1
        jump avaquestion3

label avaquestion3:
    "How well do you work in a team environment?"
    menu:
        "Well":
            jump answerwell
        "Not Well":
            jump answernotwell


    label answerwell:
        scene fs avainterviewscene1b
        player "Ava may be currently running for herself but she is constantly in a team environment."
        player "Her good friend Josy is the long jump star of the school, yet they encourage each other."
        player "Even though they're in different sports."
        scene fs avainterviewscene3
        player "Hey babe, how do you feel about relays?"
        ava "{i}Babe?{/i}"
        scene fs avainterviewscene3b
        ava "{size=20}I don't mind{/size}"
        scene fs avainterviewscene1b
        player "There you have it, she's okay with doing any position in a relay, as long as it wins them the race!"
        scene fs avainterviewscene1
        "Recruiter Guy" "Okay, good outlook. Moving on."
        jump avaquestion4
    label answernotwell:
        scene fs avainterviewscene1b
        player "Oh man NOT well at all! This one time I begged, BEGGED her to have a threesome with her friend Josy."
        scene fs avainterviewscene1
        ava "!!!!!"
        scene fs avainterviewscene4
        player "And she was NOT having it, wouldn't even let her watch, if you know what I mean."
        ava "{i}WHAT ARE YOU DOING????{/i}"
        "Recruiter Guy" "Oh uh...I..Alright. Next."
        scene fs avainterviewscene1
        $ avajobinterview = avajobinterview + 1
        jump avaquestion4
label avaquestion4:
    "How do you stay motivated after an injury?"
    menu:
        "Eat A Lot":
            jump answereat
        "Passion For Sport":
            jump answerpassion
        "Watch TV":
            jump answertv

    label answereat:
        scene fs avainterviewscene1b
        player "You know nuggy bites?"
        scene fs avainterviewscene1
        "Recruiter Guy" "Excuse me?"
        scene fs avainterviewscene1b
        player "Nuggy Bites. Those deep fried taters with the cheese in the middle?"
        scene fs avainterviewscene1
        "Recruiter Guy" "Yes?"
        scene fs avainterviewscene2
        player "Oh man, SOOOO many of those."
        scene fs avainterviewscene1
        "Recruiter Guy" "....."
        "Recruiter Guy" "Okay."
        $ avajobinterview = avajobinterview + 1
        jump avaquestion5
    label answerpassion:
        scene fs avainterviewscene1b
        player "One night, before we started fucking I went into her purse to find some condoms."
        ava "{i}What the shit??{/i}"
        scene fs avainterviewscene1
        "Recruiter Guy" "I don't see-"
        scene fs avainterviewscene1b
        player "Please sir let me finish."
        player "I found a little notebook, I picked it up and saw fresh notes she wrote that day."
        scene fs avainterviewscene2
        player "Notes on breathing techniques, new possible ways of strength training."
        player "Notes on not just famous atheletes, but who SHE thinks are going to be great up and comers."
        scene fs avainterviewscene4
        player "And this was the day AFTER she won a race, the day she's supposed to REST."
        player "I wouldn't question Ava's passion for anything in the world. She gets injured?"
        player "Then she just does what she needs to heal, while getting ready for when she can run again."
        scene fs avainterviewscene4b
        ava "Hehe..."
        player "And that's the truth."
        "Recruiter Guy" "Oh! Very well said. One last question."
        scene fs avainterviewscene1
        with Dissolve(0.5)
        jump avaquestion5
    label answertv:
        scene fs avainterviewscene1b
        player "There's this show, about this crazy family that's made up of entirely step members."
        player "They're constantly fucking each other and getting stuck in washing machines."
        player "I wa-"
        scene fs avainterviewscene1
        pause
        scene fs avainterviewscene4
        player "SHE watches it all the time, it's hilarious. Makes her feel better about herself you know?"
        ava "{i}Kill me.{/i}"
        scene fs avainterviewscene1
        "Recruiter Guy" "I uh, I've never heard of it. Moving on."
        $ avajobinterview = avajobinterview + 1
        jump avaquestion5

label avaquestion5:
    "Why do you deserve to be a professional athlete?"
    menu:
        "She's Good":
            jump answergood
        "She's Kind":
            jump answerkind
        "She's Hot":
            jump answerhot

    label answergood:
        scene fs avainterviewscene1b
        player "Do you know what the world record is for the female 400 meter sir?"
        scene fs avainterviewscene1
        "Recruiter Guy" "Of course! 47.60 held by Karita Moch."
        scene fs avainterviewscene1b
        player "Our Ava here, BEAT Moch's 400 meter record by 1.9 seconds when she was her age."
        scene fs avainterviewscene2
        player "And she's getting faster, every 3 months on average she's gaining 0.5 seconds."
        player "Not just 400 meter, 200 and 100 too."
        player "She's come first in both categories in the last two junior nationals."
        scene fs avainterviewscene1
        "Recruiter Guy" "Very impressive Miss Ava."
        scene fs avainterviewscene1c
        ava "T-Thanks.."
        scene fs avainterviewscene4
        player "Ava is GOOD. And she's going to be better than good. She's an opportunity of a lifetime."
        player "I should know."
        ava "{i}[povname]...{/i}"
        "Recruiter Guy" "I think I understand. Thank you both for your time."
        player "No problem."
        scene fs blackblank
        with Dissolve(0.7)
        "Recruiter Guy" "Miss Ava I will get back to you with the results soon."
        ava "Y-Yes of course! Thank you!"
        $ avaquestlog = "Go to sleep at Night to hear Ava's interview results."
        jump passtime
    label answerkind:
        scene fs avainterviewscene1b
        player "Ava is kind and compassionate. Who among us most deserve good things aside from good people?"
        scene fs avainterviewscene1
        "Recruiter Guy" "Uh. That's...true."
        "Recruiter Guy" "I will...Get back to you Miss Ava, with the results."
        "Recruiter GUy" "Good day."
        scene fs blackblank
        with Dissolve(0.7)
        $ avajobinterview = avajobinterview + 1
        $ avaquestlog = "Go to sleep at Night to hear Ava's interview results."
        jump passtime
    label answerhot:
        scene fs avainterviewscene1b
        player "Ava is hot as fuck."
        scene fs avainterviewscene2
        player "You want sponsorships? Someone to be on the front of magazines?"
        scene fs avainterviewscene4
        player "You need what Ava's got! A rocking body with some nice tits and a face you can cum on!"
        ava "{i}Well, there goes my future career{/i}."
        "Recruiter Guy" "Mr [povname]!"
        player "You picking up what I'm putting down?"
        "Recruiter Guy" "I will...Get back to you Miss Ava, with the results."
        "Recruiter GUy" "Good day."
        scene fs blackblank
        with Dissolve(0.7)
        $ avajobinterview = avajobinterview + 1
        $ avaquestlog = "Go to sleep at Night to hear Ava's interview results."
        jump passtime


label didshemakeit:
    scene fs playerbedneutral
    with Dissolve(0.7)

    "Briiing Briiing"
    scene fs playerbedphone
    with Dissolve(0.50)
    player "Huh? Now who's that?"
    ava "{cps=25}Hey dude!{/cps}"
    player "{cps=25}Ava!{/cps}"
    ava "{cps=25}I got the results.{/cps}"
    player "{cps=25}Holy shit already?! What'd he say?{/cps}"

    if avajobinterview > 0:
        ava "{cps=25}I uh...didn't pass.{/cps}"
        player "{cps=25}Oh...{/cps}"
        ava "{cps=25}But he said we're more than welcome to try again! He said he sees potential.{/cps}"
        ava "{cps=25}Could you help me out at the cafe again?{/cps}"
        player "{cps=25}Yeah sure!{/cps}"
        $ avajobinterview = 999
        $ avaquestlog = "Meet Ava at Cafe Seni in Sunnyside during Day to retry the interview."
        jump gotosleep
    elif avajobinterview == 0:
        ava "{cps=25}I paaaaassssed!!{/cps}"
        ava "{cps=25}Thank you thank you thank you!{/cps}"
        player "{cps=25}YESSSS!{/cps}"
        ava "{cps=25}What are you doing right now!?{/cps}"
        player "{cps=25}Well I was gonna have an early sleep?{/cps}"
        ava "{cps=25}Fuck that! I'm coming over we're celebrating!{/cps}"
        player "{cps=25}Haha alright! See you soon!{/cps}"
        $ avajobinterview = 999
        jump avaphase2interaction2part3
    else:
        "You shouldn't be here"
        jump passtime

label avaphase2interaction2part3:
    scene fs livingroomnight
    with Dissolve(0.7)
    pause
    "After an hour or two..."
    scene fs avainterviewscene5
    voice "audio/avagameaudio/avadrinking.wav"
    ava "Gulp gulp gulp"
    scene fs avainterviewscene6
    with vpunch
    voice "audio/avagameaudio/avaahhhhh.wav"
    ava "Ahhhhhh."
    scene fs avainterviewscene7
    ava "Man I needed that haha."
    scene fs avainterviewscene7b
    player "Sure looked like it."
    scene fs avainterviewscene7
    ava "Dude, you are SO good at bullshitting. That's a dangerous skill."
    scene fs avainterviewscene7b
    player "Hey, most of those were estimated guesses."
    scene fs avainterviewscene7
    ava "Condoms in my purse?"
    scene fs avainterviewscene7b
    player "Annnnd a little bullshitting yes."
    scene fs avainterviewscene7
    ava "How did you know about my numbers, I don't even think they were right? And that I beat Moch's old records?"
    scene fs avainterviewscene7b
    player "I didn't! I made the stats up, but I had a pretty good feeling you beat her record since you're so good anyways."
    scene fs avainterviewscene7
    ava "Wow."
    scene fs avainterviewscene7b
    player "Estimated guesses."
    scene fs avainterviewscene8
    with Dissolve(0.7)
    pause
    scene fs avainterviewscene8b
    ava "And you meant what you said?"
    scene fs avainterviewscene8
    player "Hmm?"
    scene fs avainterviewscene8b
    ava "About believing in me and me being really hot and all that?"
    scene fs avainterviewscene8
    player "I don't remember saying the hot part even if you are, but yeah of course."
    ava "...."
    player "What you doing?"
    scene fs avainterviewscene8b
    ava "Thinking on how to proceed."
    scene fs avainterviewscene8
    player "Pro-"
    scene fs avainterviewscene9
    pause
    voice "audio/avagameaudio/avagiggle.wav"
    ava "Proceed."
    player "Oh hello."
    scene fs avainterviewscene9c
    player "This is nice."
    scene fs avainterviewscene9b
    ava "Mmhmm."
    ava "I don't want to talk anymore."
    scene fs avainterviewscene9c
    player "That's fine with me."
    scene fs avainterviewscene10b
    play sound "audio/avagameaudio/avamakeout.wav" loop
    pause
    show avainterviewbj movie1
    pause
    ava "Mmmm.."
    scene fs avainterviewscene10
    pause
    scene fs avainterviewscene12
    with Dissolve(0.5)
    stop sound
    pause
    player "What are you doing?"
    scene fs avainterviewscene12b
    ava "Ahem. Getting ready."
    scene fs avainterviewscene12
    player "For?"
    scene fs avainterviewscene13
    ava "Oh you'll see."
    scene fs avainterviewscene14
    player "Wait are you gonna-"
    ava "Mhmm."
    player "Upside down?"
    scene fs avainterviewscene15b
    ava "Yup."
    scene fs avainterviewscene18
    with Dissolve(0.5)
    ava "Now take that big cock of yours out and fuck my throat."
    scene fs avainterviewscene19
    with Dissolve(0.7)
    ava "Ohhhh fuck yes."
    scene fs avainterviewscene20
    ava "Mmm."
    player "Fuck your body is so sexy."
    scene fs avainterviewscene20b
    ava "*Slurp* Mmhmm?"
    player "Your tits are fucking perfect."
    show avainterviewbj movie4
    with Dissolve(1.0)
    play sound "audio/avagameaudio/avaUDblowjob1.wav"
    pause
    player "Fuuuuck yeah there we go."
    show avainterviewbj movie2
    pause
    player "God that's good."
    show avainterviewbj movie3
    play sound "audio/avagameaudio/avaUDblowjob2.wav"
    ava "Mmmmhn!"
    player "You like me squeezing them don't you?"
    pause
    show avainterviewbj movie5
    ava "Guhk Guhk!"
    pause
    show avainterviewbj movie6
    play sound "audio/avagameaudio/avaUDblowjobswallow.wav" loop
    player "FUCK c'mon c'mon!"
    player "UGH I'm fucking cumming!"
    ava "MMMMHH!!"
    stop sound
    pause
    scene fs avainterviewscene24
    with Dissolve(0.7)
    ava "*Gasp*"
    play sound "audio/avagameaudio/avafingered.wav"
    ava "Hah...hah.."
    player "That was great."
    ava "Tasty."
    scene fs blackblank
    with Dissolve(1.0)
    "Ava cleaned herself up before saying her goodbyes and heading home for the night"
    $ avaquestlog = "Meet Ava at the gym during Day."
    $ avaphase2interaction2 = 3
    $ avaphase2interaction3 = 1
    jump gotosleep


label avaphase2interaction3part1:
    stop music fadeout 5
    stop sound fadeout 5
    hide screen backbuttonGYM
    hide screen ava_atgym

    $ playerSprite = 0

    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "Ah there's Ava! Lemme g-"
    josy "Heeeey!!"
    $ playerSprite = 11
    show fbplayer current:
        xalign 0.4 ypos 120
    with move
    $ josySprite = 0
    show fbjosy current:
        xalign 0.6 ypos 120
    $ playerSprite = 1
    player "Oh shit, Josy you surprised me haha."
    $ playerSprite = 0
    $ josySprite = 2
    josy "Oh sorry! Nice to see you!"
    $ josySprite = 0
    $ playerSprite = 1
    player "Nice to see you too."
    $ playerSprite = 0
    $ josySprite = 1
    josy "You've been coming here a lot lately, getting into shape?"
    $ josySprite = 2
    josy "You're plenty good looking already but it's pretty hot that you wanna keep yo body rockin'!"
    $ playerSprite = 1
    player "Haha!"
    player "You don't look too bad yourself!"

    $ avaSprite = 0
    show fbava current:
        xalign 0.9 ypos 120
    with Dissolve(0.5)
    ava "{i}Oh, [povname] is here.{/i}"
    josy "*Laughs seductively*"
    $ avaSprite = 15
    ava "{i}And he's...talking to Josy.{/i}"
    scene fs avagymzoom1
    with Dissolve(0.7)
    player "*Talks hornily*"
    ava "I..."
    scene fs avagymzoom2
    with Dissolve(0.7)
    josy "*Makes blowjob gesture with hand*"
    player "*Makes doggystle gesture with hips*"
    scene fs avagymzoom3
    with Dissolve(0.7)
    $ avaSprite = 1
    ava "Don't like that."
    scene fs gymarea

    show fbplayer current:
        xalign 0.4 ypos 120
    show fbjosy current:
        xalign 0.6 ypos 120

    show fbava current:
        xalign 0.65 ypos 120

    ava "HEY GUYS!"
    player "Ava! Hey."
    $ josySprite = 1
    show fbjosy current:
        xalign 0.5
        xzoom -1.0
    josy "Hey girl, [povname] and I wer-"
    show fbava current:
        xalign 0.5 ypos 120
    with move
    ava "Yup cool cool cool!"
    ava "You're here to work out right [povname]? I need someone to spot me!"
    player "Well uh yeah, gotta get changed first bu-"
    ava "Great! See you Josy! Bye!"
    show fbjosy current:
        xalign 0.7 ypos 120
        xzoom 1.0
    with Dissolve(0.5)
    josy "Oh okay um, bye!"
    $ josySprite = 0
    hide fbplayer current
    hide fbava current
    with Dissolve(0.5)
    pause
    josy "....."
    josy "Hmmm."
    scene fs blackblank
    with Dissolve(0.7)
    player "Alright I'm ready, what are you doing first?"
    ava "Let's do the bench! I uh, want to work my upper body today."
    player "Skipping leg-"
    ava "Don't say it."
    scene fs avagymworkout2
    with Dissolve(1.0)
    ava "Yeah this is..."
    ava "Much better."
    scene fs avagymworkout1
    player "Sorry?"
    ava "Nothing nothing."
    scene fs avagymworkout3
    voice "audio/avagameaudio/avagrunt1.wav"
    ava "Hup!"
    scene fs avagymworkout2
    voice "audio/avagameaudio/avagrunt2.wav"
    ava "Ah."
    ava "{i}God as my witness I'm gonna ride that fucking thing like a fuckin' damn roller coaster {/i}"
    player "Ava?"
    scene fs avagymworkout3
    voice "audio/avagameaudio/avagrunt1.wav"
    ava "Yup sorry, just thinking."
    scene fs blackblank
    with Dissolve(0.7)
    ava "Alright let's move on!"
    scene fs avagymworkout4
    with Dissolve(0.5)
    player "Do I need to be behind you for this one?"
    scene fs avagymworkout5
    ava "No you..."
    ava "You stay right fucking there."
    player "Well sorry, damn."
    scene fs avagymworkout4
    voice "audio/avagameaudio/avagrunt2.wav"
    ava "No sorry sorry, I'm just distracted ignore me."
    player "You do seem lost in your own thoughts today."
    scene fs avagymworkout5
    ava "...Do I?"
    scene fs avagymworkout4
    voice "audio/avagameaudio/avagrunt2.wav"
    player "A bit."
    scene fs blackblank
    with Dissolve(0.7)
    ava "Okay next!"
    scene fs avagymworkout6
    player "Alright last set you got this."
    ava "..."
    player "Ava?"
    scene fs avagymworkout7

    ava "You got any brothers [povname]?"
    player "What?"
    scene fs avagymworkout8
    voice "audio/avagameaudio/avagrunt1.wav"
    ava "Hah."
    player "No I'm an only child."
    scene fs avagymworkout7
    voice "audio/avagameaudio/avagrunt2.wav"
    ava "Shit, so it's gotta be you huh?"
    player "Uh....yeah?"
    scene fs avagymworkout8
    voice "audio/avagameaudio/avagrunt1.wav"
    ava "Hmph!"
    scene fs avagymworkout7
    voice "audio/avagameaudio/avagrunt2.wav"
    ava "Hooo..."
    scene fs blackblank
    with Dissolve(0.7)
    player "You okay?"
    ava "Yup."
    ava "Just in case though.."
    ava "Let's stop by your place so I can...rest."
    player "Yeah no problem."

    scene fs avafirstsex1
    with Dissolve(1.0)
    player "Phew, that was pretty good."
    player "Your glutes are looking fine, if me spotting you keeps you in the gym I'm all for it!"
    ava "Mmm."
    scene fs avafirstsex2
    player "What's up, you okay?"
    player "You've been a bit off today."
    ava "*breaths in*"
    ava "*breathes out"
    scene fs avafirstsex3
    ava "[povname]."
    player "Ava."
    ava "You remember how I said I wasn't good with words?"
    player "Mhmm."
    pause
    scene fs avafirstsex4
    with hpunch
    pause
    ava "Mmmm!"
    player "{i}OH!{/i}"
    show avafirstsex movie1
    with Dissolve(0.7)
    play sound "audio/avagameaudio/avamakeout.wav" loop
    pause
    scene fs avafirstsex6
    stop sound fadeout 5
    ava "Hah...hah."
    scene fs avafirstsex6b
    player "I think I get why you were so off now."
    scene fs avafirstsex6
    ava "No more talk."
    ava "Sex please!"
    scene fs avafirstsex6b
    player "Alright, let's go to my room."
    scene fs blackblank
    with Dissolve(0.7)
    "A few less clothes later.."
    scene fs avafirstsex7
    with vpunch
    voice "audio/avagameaudio/avauhno.wav"
    ava "Nope. I'VE been wanting to ride your cock all day, I'M THE ONE ON TOP."
    player "Maybe later but I am NOT letting you ride me before I feel your perfect ass slapping against me."
    scene fs avafirstsex8
    player "Hey!"
    ava "Too fuckin slow buddy!"
    ava "I'm gonna-"
    scene fs avafirstsex9
    with vpunch
    voice "audio/avagameaudio/avasurprisemoan.wav"
    ava "AHHN!"
    player "You're so tight!"
    pause
    scene fs avafirstsex10
    with Dissolve(0.7)
    ava "Hah..hehe."
    ava "Finally."
    scene fs avafirstsex10b
    player "You think you've won?"
    scene fs avafirstsex10
    ava "Don't act you don't want me to gr-"
    scene fs avafirstsex11
    show fs avafirstsex11
    with vpunch
    voice "audio/avagameaudio/avasurpriseah.wav"
    ava "Ahh!"
    player "C'mere!"
    show avafirstsex movie4
    play sound "audio/avagameaudio/avasex1.wav" loop
    ava "Fuck!"
    pause
    show avafirstsex movie2
    play sound "audio/avagameaudio/avasex2.wav" loop
    player "Feels good don't it?!"
    ava "Dude you're so big!"
    player "You wanted this badly didn't you? I can feel how wet you are!"
    ava "Ahn!"
    pause
    show avafirstsex movie5
    player "I love your expression as I pound you raw!"
    player "It's so cute!"
    ava "S-Shut up!"
    player "MMMM your tits got a nice bounce to them too!"
    pause
    show avafirstsex movie3
    ava "FUCK FUCK FUCK!"
    player "Let's pick up the pace huh?"
    ava "God [povname] I'm gonna fucking cum!"
    pause
    show avafirstsex movie6
    play sound "audio/avagameaudio/avasexorgasm.wav" loop
    ava "AHHHNN!!"
    player "FUCK you're squeezing me so hard!"
    player "UGH!"
    pause
    scene fs avafirstsex12
    with Dissolve(0.5)
    stop sound
    pause
    player "Hah...shit Ava sorry, I wasn-"
    ava "Itsokay!"
    ava "Hah...it's.."
    ava "It's okay..hah.."
    scene fs blackblank
    with Dissolve(0.5)
    player "So...this was.."
    ava "Fan-fucking-tastic."

    if currentchapter == 3:
        $ avaquestlog = "Talk to Ava at school during Morning."
    else:
        $ avaquestlog = "Continue exploring until the beach trip on day 20, then talk to Ava at school during Morning in chapter 3."
    $ avaphase2interaction3 = 2
    $ timeofday = "Night"
    jump passtime


label avabeachchapter2end:

    hide screen mia_beach1
    hide screen mia_beach2
    hide screen mia_beach3
    hide screen sophia_beach
    hide screen charlotte_beach
    hide screen ava_beach
    hide screen emily_beach
    hide screen olivia_beach
    hide screen backbuttonBEACH
    scene fs beach
    $ playerSprite = 19
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbava current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    player "Ava!"
    $ avaSprite = 23
    $ playerSprite = 18
    ava "[povname]! Just the man I was looking for."
    $ avaSprite = 22
    $ playerSprite = 19
    player "Haha, looking for me?"
    $ playerSprite = 18
    $ avaSprite = 23
    ava "Uh huh, time for some good ol' fasion competition!"
    $ avaSprite = 22
    $ playerSprite = 19
    player "What, the volleyball game wasn't enough?"
    $ playerSprite = 18
    $ avaSprite = 23
    ava "Not even close!"
    $ avaSprite = 22
    $ playerSprite = 19
    player "Alright then, what are we doing?"
    $ playerSprite = 18
    $ avaSprite = 23
    ava "Everything!"
    $ avaSprite = 22
    $ playerSprite = 19
    player "Bring it on!"
    scene fs blackblank
    with Dissolve(0.7)
    "Ava and I then started to compete in every beach themed game you could think of"
    scene fs avabeachfun1
    with Dissolve(0.7)
    pause
    scene fs avabeachfun2
    ava "21!"
    "And some, not so beach themed"
    scene fs avabeachfun3
    player "Feeling tired yet?"
    scene fs avabeachfun2
    ava "You wish!"
    scene fs avabeachfun4
    sophia "C'mon guys keep going you can do it!"
    charlotte "Why am I here?"
    scene fs avabeachfun1
    pause
    scene fs avabeachfun2
    ava "22!"
    scene fs avabeachfun5
    with Dissolve(1.0)
    olivia "Grrrr!"
    ava "Haha c'mon Olivia, show me that gamer girl strength!"
    sophia "This...hah..doesn't even make sense!"
    sophia "Why am I the one on the bottom??!"
    scene fs blackblank
    with Dissolve(1.0)
    "It was a lot of fun!"

    if avaphase2interaction3 >= 2:
        "Would you like to end the day with Ava?"
        menu:
            "Romance":
                jump avachapter2romance
            "Naughty":
                jump avachapter2naughty
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach

    label avachapter2romance:
        scene fs beachpictureempty
        with Dissolve(1.0)
        show fbplayer current:
            xalign 0.4 ypos 120
        show fbava current:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        player "Well..hah..seems like we tied?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Yeah haha."
        ava "I think I tied more though."
        $ avaSprite = 22
        $ playerSprite = 19
        player "What does that even mean lol?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Did you just lol?"
        $ avaSprite = 22
        player "..."
        $ avaSprite = 23
        ava "Moving so much did work up a good sweat, and it's getting later in the day."
        $ avaSprite = 22
        $ playerSprite = 19
        player "Yeah for sure. You...feeling dirty?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "I could really use a shower."
        $ avaSprite = 22
        $ playerSprite = 19
        show fbplayer current:
            xalign 0.55 ypos 120
        with move
        player "A dirty...tomboy shower?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Hahaha dude what the hell?"
        $ avaSprite = 22
        $ playerSprite = 19
        player "Haha sorry."
        $ playerSprite = 18
        ava "...."
        $ avaSprite = 23
        show fbava current:
            xzoom -1.0
        ava "C'mon. I need your cock inside me right now."
        $ playerSprite = 20
        player "Oh shit...uh.."
        player "Yes ma'am."
        pause
        show avabeachsex movie2
        ava "Hah hah hah.."
        player "Fuck you're tight!"
        ava "And you're so FUCKING big!"
        scene fs avabeachsex4
        with Dissolve(0.5)
        ava "Doing it in the shower is so HOT!"
        show rs oliviashowerright
        with Dissolve(0.7)
        player "You really like this huh?"
        show ls sophiashowerleft
        with Dissolve(0.7)
        ava "Feels so fucking good!"
        show rs oliviashowerlook
        ava "GOD dude. I want to marry your dick!"
        olivia "Huh?"
        ava "You better not pull out!"
        show ls sophiashowerlook
        sophia "Hmm?"
        olivia "Ava?"
        show fs avabeachsex6 behind ls
        with vpunch
        ava "Ah!"
        ava "Uh yeah?"
        show avabeachsex movie2
        olivia "You okay?"
        ava "Y-Yeah! Ahn!"
        sophia "You sound kinda weird.."

        scene fs avabeachsex5
        show ls sophiashowerlook
        show rs oliviashowerlook
        with Dissolve(0.5)
        ava "Oh my god! N-No I'm F-"
        ava "FUCK!"
        sophia "Do you need help?"
        olivia "I think we should open the d-"
        show avabeachsex movie2
        ava "N-No!"
        ava "T-The truth is there's a guy in here!"
        olivia "Ohhhh..."
        sophia "What?"
        ava "There's a guy in here w-AHN! With me. We're having s-SEX!"
        ava "God I'm gonna fucking cum!"
        sophia "Ohmygod. Uh okay sorry."
        show avabeachsex movie3
        ava "FUCK YES YES AHN!!!"
        player "UGGGH!!"
        scene fs avabeachsex3
        with Dissolve(1.0)
        ava "God I feel it..I feel it spilling out..."
        sophia "Oooookay."
        olivia "Haha, okay enjoy then, we'll get out first"
        scene fs blackblank
        with Dissolve(1.0)
        $ avaquestlog = "Talk to Ava at school during Morning."
        $ endchapter2_trigger = "2 ava romantic"
        jump startofchapter3

    label avachapter2naughty:
        scene fs beachpictureempty
        with Dissolve(1.0)
        $ playerSprite = 19
        show fbplayer current:
            xalign 0.4 ypos 120
        show fbava current:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        player "Well..hah..seems like we tied?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Yeah haha."
        ava "I think I tied more though."
        $ avaSprite = 22
        $ playerSprite = 19
        player "What does that even mean lol?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Did you just lol?"
        $ avaSprite = 22
        player "..."
        $ avaSprite = 23
        ava "Moving so much did work up a good sweat, and it's getting later in the day."
        $ avaSprite = 22
        $ playerSprite = 19
        player "Let's go to the shower then."
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Huh?"
        $ avaSprite = 22
        $ playerSprite = 19
        player "Let's go hit the showers. Together."
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Oh."
        $ avaSprite = 22
        $ playerSprite = 19
        player "I'm not giving you a choice."
        $ playerSprite = 18
        ava "...."
        show fbplayer current:
            xalign 0.7 ypos 120
        with move
        $ playerSprite = 19
        player "{size=20}I'm gonna pound your tight fucking pussy while all your friends have no idea.{/size}"
        $ playerSprite = 18
        ava "Y-Yes please."
        pause
        scene fs blackblank
        with Dissolve(0.5)
        "A little later on..."
        scene fs avabeachsex1
        with Dissolve(1.0)
        player "Tell me what you it."
        ava "I-I want it!"
        scene fs avabeachsex2
        ava "O-Oooohhh..."
        show avabeachsex movie1
        player "Mmmh yeah nice and slow."
        player "That's how you like it right?"
        ava "Uhn...N-No.."
        player "Soft...safe...boring.."
        pause
        scene fs avabeachsex4
        with Dissolve(0.5)
        ava "M-More.."
        show rs oliviashowerright
        with Dissolve(0.5)
        olivia "*Hums*"
        player "What was that? I can't hear you."
        show ls sophiashowerleft
        with Dissolve(0.5)
        sophia "Dum de dum"
        ava "H...HARDER!"
        player "Beg me."
        ava "Please! Please pound my fucking pussy!"
        show rs oliviashowerlook
        olivia "What the hell?"
        show ls sophiashowerlook
        sophia "Huh??"
        show avabeachsex movie2
        ava "AHN!!!"
        olivia "Ava? Is that you?"
        ava "Oh G-God!"
        ava "Olivia??"
        sophia "Ava are you okay?"
        ava "So-AHN! Sophia?"
        ava "What are you guys doing here?"
        sophia "Uhhh taking a shower?"
        player "{size=20}Don't let them know Ava.{/size}"
        ava "F-Fuck!"
        player "{size=20}Don't let them know you're fucking your friend's boyfriend right next to them.{/size}"
        ava "P-Please..."
        scene fs avabeachsex5
        show rs oliviashowerlook
        show ls sophiashowerlook
        with Dissolve(0.5)
        ava "GGGHHH!!"
        olivia "Are you okay?"
        ava "{i}Fuck fuck fuck what do I do??{/i}"
        ava "Yes! Yes I'm F-Fine!"
        sophia "You're absolutely sure?"
        show avabeachsex movie2
        ava "Yes Yes YES YES!!"
        olivia "Alright, are you gonna come out soon?"
        ava "YES!"
        player "UUUGHH!"
        ava "I'm CUMMING!!"
        pause
        show avabeachsex movie3
        pause
        ava "UHHHN!!!"
        scene fs avabeachsex3
        with Dissolve(0.7)
        sophia "Uh okay...see you soon."

        $ endchapter2_trigger = "2 ava naughty"

        jump startofchapter3

        scene fs avabeachsex2
        player "What was that?"
        ava "I WANT IT!!"
        pause
        show avabeachsex movie2
        ava "Hah hah hah.."
        player "Fuck you're tight!"
        ava "And you're so FUCKING big!"
        scene fs avabeachsex4
        with Dissolve(0.5)
        ava "Doing it in the shower is so HOT!"
        show rs oliviashowerright
        with Dissolve(0.7)
        player "You really like this huh?"
        show ls sophiashowerleft
        with Dissolve(0.7)
        ava "Feels so fucking good!"
        show rs oliviashowerlook
        ava "GOD dude. I want to marry your dick!"
        olivia "Huh?"
        ava "You better not pull out!"
        show ls sophiashowerlook
        sophia "Hmm?"
        olivia "Ava?"
        show fs avabeachsex6 behind ls
        with vpunch
        ava "Ah!"
        ava "Uh yeah?"
        show avabeachsex movie2
        olivia "You okay?"
        ava "Y-Yeah! Ahn!"
        sophia "You sound kinda weird.."

        scene fs avabeachsex5
        show ls sophiashowerlook
        show rs oliviashowerlook
        with Dissolve(0.5)
        ava "Oh my god! N-No I'm F-"
        ava "FUCK!"
        sophia "Do you need help?"
        olivia "I think we should open the d-"
        show avabeachsex movie2
        ava "N-No!"
        ava "T-The truth is there's a guy in here!"
        olivia "Ohhhh..."
        sophia "What?"
        ava "There's a guy in here w-AHN! With me. We're having s-SEX!"
        ava "God I'm gonna fucking cum!"
        sophia "Ohmygod. Uh okay sorry."
        show avabeachsex movie3
        ava "FUCK YES YES AHN!!!"
        player "UGGGH!!"
        scene fs avabeachsex3
        with Dissolve(1.0)
        ava "God I feel it..I feel it spilling out..."
        sophia "Oooookay."
        scene fs blackblank
        with Dissolve(1.0)

        jump startofchapter3

# Chapter 3


label avaphase3interaction1part1:
    show fbava current:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ avaSprite = 1
    ava "[povname]! Hey man."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Sup."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "How you doing? Get a good sleep?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Haha sleep? Yeah it was fine."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Sleep is very important for your health! It's when your body recovers and you build bigger muscles!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Huh. I'll keep that in mind. Did YOU sleep well?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Like a LOG oh my God."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Haha great to hear. So what are you up to?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Well I'm usually at the track around this time but I'm skipping today, so mainly just waiting around for one of the girls."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Wait why are you skipping? That's not like you."
    $ playerSprite = 0
    $ avaSprite = 4
    ava "Oh uh..well I'm *Ahem*."
    ava "Sore."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Sore? From what?"
    $ playerSprite = 14
    ava "...."
    $ avaSprite = 11
    ava "From YOU. Thanks for letting me be subtle."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Ohhhh. Oh shit."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Yeah."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Sorry."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "But it's okay I've been resting since we...did it. And I should be good after today."
    $ avaSprite = 0
    $ playerSprite = 1
    player "What about tonight?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Tonight? Yeah I should be fine."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Another run at the park together then?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Uh yeah okay. I can do that."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Awesome see you then."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "See you later!"
    $ avaSprite = 0
    $ avaquestlog = "Meet Ava at the park at Night."

    $ avaphase3interaction1 = 1
    jump school

label avaphase3interaction1part2:
    hide screen uppergui
    $ avaSprite = 7
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.7)
    pause
    player "Hate to see you leave."
    $ avaSprite = 6
    show fbplayer shortsbonertalk:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    player "But love to see you walk away."
    show fbplayer shortsboner
    $ avaSprite = 3
    ava "Haha shut up you dork that's not even the situation for that."
    $ avaSprite = 2
    show fbplayer shortsbonertalk
    player "Close enough."
    player "Ready to run?"
    $ avaSprite = 3
    ava "Let's do it."
    scene fs avarun1
    with Dissolve(0.7)
    "You run along the familiar park path with Ava once again"
    "The cool breeze was refreshing as it hit your skin"
    "You could hear Ava's rhythmic breath as she pulled away from you"
    scene fs avarun4
    with Dissolve(0.5)
    "But this time you caught up"
    scene fs avarun5
    with Dissolve(0.5)
    "And stayed there, right beside her"
    scene fs avarun4
    with Dissolve(0.5)
    pause
    scene fs parknight
    with Dissolve(0.7)
    show fbplayer shortstired1:
        xalign 0.4 ypos 120
    $ avaSprite = 5
    show fbava current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)

    ava "Hah..dude!"
    ava "You did it!"
    player "I...hah."
    show fbplayer shortstired2
    player "Did it!"
    show fbplayer shortstired1
    ava "I'm so proud of you. Great job keeping up."
    show fbplayer shortstired2
    player "You...hah..didn't make it easy."
    ava "Nothing good in life ever is."
    show fbplayer shortstired1
    player "I dunno..hah..if true..can't think."
    ava "Haha let's go to your car, we can rest back at your place."
    player "Good idea."
    scene fs blackblank
    with Dissolve(0.7)
    "You drive you and Ava's sweaty bodies back to your place"
    scene fs avacouchprank2b
    player "Alright last chance if you want to shower first."
    scene fs avacouchprank2
    ava "I told you it's fine, I'll just shower at home."
    scene fs avacouchprank2b
    player "Kay. Looks like we won't be doing anything naughty then."
    player "No way I'm touching a nasty sweaty Tomboy."
    scene fs avacouchprank2
    ava "Oh I'm your Tomboy now?"
    scene fs avacouchprank2b
    player "Yup."
    play music "audio/showersounds.wav"
    "*Shower noises*"
    scene fs avacouchprank2
    ava "Heh."
    scene fs avacouchprank2b
    ava "..."
    scene fs avacouchprank3
    ava "Wait what does he mean he wouldn't touch me if I was sweaty?"
    ava "Is that a challenge??"
    ava "I bet a perv like him would get even more turned on!"
    ava "I'm gonna prove it!"
    scene fs avacouchprank3b
    ava "With just a little underboob and some 'innocent vulnerability'..."
    scene fs avacouchprank4
    ava "He won't be able to keep his hands off me!"
    scene fs blackblank
    with Dissolve(0.5)
    stop music fadeout 5
    "A little while later.."
    scene fs avacouchprank5
    with Dissolve(0.5)
    player "Hey I'm back, do you-oh?"
    player "Looks like she fell asleep."
    player "{i}Why is her top pulled up so much?{/i}"
    ava "*Obvious fake snoring*"
    player "{i}Ahhhhh she's not asleep. She must've got upset at my little joke.{/i}"
    player "{i}Let's have a little fun with her.{/i}"
    scene fs avacouchprank5b
    player "Damn Ava, sometimes I forget how fucking hot your body is."
    player "I don't normally do something like this but your tits have me rock hard."
    player "I have to jack off!"
    scene fs avacouchprank5
    ava "{i}Heh. I knew it!{/i}"
    scene fs avacouchprank5b
    player "Mmmm yeah, don't wake up baby stay just like that."
    player "I remember just how good your pussy felt. You're such a tight little slut."
    scene fs avacouchprank5
    ava "{i}I'm kinda getting a little wet from this..{/i}"
    scene fs avacouchprank5b
    player "Fuck I can feel it coming! I'm gonna cum all over your perfect tits!"
    scene fs avacouchprank5
    ava "{i}Yes!{/i}"
    scene fs avacouchprank5b
    player "Your pretty little face!"
    scene fs avacouchprank5
    ava "{i}Do it!{/i}"
    scene fs avacouchprank5b
    player "Your beautiful hair!"
    scene fs avacouchprank6
    with vpunch
    ava "NOT THE HAIR!!"
    scene fs avacouchprank7
    player "Hahahaha."
    ava "Huh??"
    player "Oh man, that reaction was perfect."
    ava "That's not funny!"
    scene fs avacouchprank8b
    with Dissolve(0.7)
    player "Aww c'mon babe."
    scene fs avacouchprank8
    ava "Hmph."
    scene fs avacouchprank8b
    player "Did my cute, tanned little tomboy get upset at my little prank?"
    scene fs avacouchprank8c
    ava "No."
    scene fs avacouchprank8b
    player "No?"
    scene fs avacouchprank8c
    ava "I'm not little."
    scene fs avacouchprank9
    player "*Kiss*"
    player "Of course not."
    player "I was teasing you but I really would fuck a post-workout Ava."
    scene fs avacouchprank9b
    ava "Y-You said I was stinky and sweaty!"
    scene fs avacouchprank10
    with Dissolve(0.5)
    player "Mmmm"
    player "Did I?"
    show avacouchfinger movie1
    player "Did I really?"
    ava "Ahn..."
    ava "No."
    player "You want me to make you cum?"
    ava "Yes."
    player "You really want me to?"
    ava "YES."
    player "Are you my cute little tomboy?!"
    scene fs avacouchprank11
    with vpunch
    ava "YESSS!!!"
    ava "Ahhhmygod."
    pause
    scene fs blackblank
    with Dissolve(0.7)
    ava "Hah...hah.."
    player "Ava?"
    ava "Mmm?"
    player "Do you want to go out on a date with me?"
    ava "Really dude?"
    player "Yeah."
    ava "I...yeah I-I'd like that *Ahem*."
    $ avaphase3interaction1 = 2
    $ avaquestlog = "No more content for Ava in this version."
    jump overworldmap
