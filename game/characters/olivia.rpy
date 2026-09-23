# chapter 1
# interaction 1
# part 1

label oliviaphase1interaction1part1:
    scene fs classroomZOOM
    hide screen olivia_atschool
    hide screen uppergui
    with Dissolve(1.0)

    $ oliviaSprite = 0
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)


    player "{i}That girl with the blue hair. Isn't that one of Mia's friends I met?{/i}"
    player "{i}I think her name is Olivia.{/i}"

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Hey, you're Olivia right?"
    $ playerSprite = 0
    olivia "...."
    $ playerSprite = 12
    player "Uh...*ahem*. Hey!"
    $ playerSprite = 0
    $ oliviaSprite = 1
    voice "audio/oliviagameaudio/oliviahey.wav"
    olivia "Hmm? Oh. Hello."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "I don't know if you remember me but I'm Mia's boyfriend, we met at the café."
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "I remember. [povname]. Hi."
    $ oliviaSprite = 0
    $ playerSprite = 8
    player "Yeah hi, do you have time to chat? You do seem busy with your Game-Man."
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "I'm good at multitasking."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "Heh, okay then. Are you waiting for class to start?"
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "Yes. Advanced Calculus. It's easy. Boring."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "I had trouble with that class when I took it, Mia did tell me you're pretty smart."
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "That's nice of her."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "So what do you lik-"
    $ playerSprite = 0
    "Professor" "Alright settle down and find your seats, we're starting from last week's assignments."
    $ oliviaSprite = 1
    olivia "Looks like I have to start class."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "Yeah sorry, guess I'll talk to you later."
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "....Arcade."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "Huh?"
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "Arcade during the day, meet me."
    olivia "If you like games."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "Oh uh yeah okay see you there."
    $ playerSprite = 7
    hide fbolivia current
    with Dissolve(0.5)
    player "{i}She seemes nice if not quiet, didn't really get to talk much. I should meet her at the arcade later like she said."
    $ oliviaphase1interaction1 = 1
    $ oliviaquesticon = "gui/questboxOlivia.png"

    if renpy.android:
        $ oliviaquestlog = "{size=-25}Olivia seems cool, I should meet her at the arcade.{/size}"
    else:
        $ oliviaquestlog = "Olivia seems cool, I should meet her at the arcade."
    hide fbolivia
    hide fbplayer
    hide fs classroomZOOM
    jump returnwhereyouare

# part 1 post convo

label oliviameetmeatarcade:
    scene fs classroomZOOM
    hide screen olivia_atschool
    with Dissolve(1.0)

    $ playerSprite = 1
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)


    player "Sorry, where can I meet you again?"
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "At the arcade, in the afternoon."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "Ah alright thanks!"
    hide fbolivia
    hide fbplayer
    hide fs classroomZOOM
    jump returnwhereyouare

# part 2

label oliviaphase1interaction1part2:
    hide screen uppergui
    scene fs arcade
    with Dissolve(1.0)
    stop music fadeout 10

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Woah this arcade is pretty sweet."

    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ oliviaSprite = 1
    voice "audio/oliviagameaudio/oliviahey.wav"
    olivia "Hey."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "Hey Olivia, I was just saying this arcade is awesome, has both some classics and new stuff."
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "I love it."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "Yeah....so I guess you're a real gamer girl huh?"
    $ playerSprite = 0
    $ oliviaSprite = 2
    voice "audio/oliviagameaudio/oliviacringe.wav"
    olivia ".....uuueegh."
    $ playerSprite = 6
    player "Sorry sorry I know, I cringed just saying that my bad."
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "As long as you understand...."
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "I don't have much time today but I can play one thing before I go, is that why you wanted to meet here?"
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "Uh huh. Do you like games?"
    $ oliviaSprite = 0
    $ playerSprite = 1
    player "I haven't had the chance to play anything new recently, life gets in the way you know?"
    player "Mia did tell me you have the high score on practically everything in here though, that's awesome."
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "I'm pretty good."
    $ oliviaSprite = 0

    hide fsplayer
    hide fbolivia
    scene fs blackblank
    with Dissolve(0.6)
    scene fs arcadeblur
    with Dissolve(0.6)
    show oliviascene arcadegaming1
    with Dissolve(0.7)
    "The two of you decide to play one of those arcade zombie shooter games. "
    "This one put the players head to head to see who could score the most points."
    player "{i}Hehe my plan is working, I'm playing slow and steady. Not getting all the zombies but racking up my points multiplier.{/i}"
    player "{i}I used to play this game all the time when I was a kid and had all the high scores from my old home town.{/i}"
    player "{i}Now! The last part has the most points per zombie!{/i}"
    show oliviascene arcadegaming2
    player "{i}Haha I'm racking up the kill count baby!{/i}"
    show oliviascene arcadegaming3
    voice "audio/oliviagameaudio/oliviahuh.wav"
    olivia "What?"
    $ oliviaSprite = 3
    "Arcade Machine" "Winner! Player 2!"
    $ playerSprite = 1
    hide oliviascene arcadegaming3
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    player "Hah I still got it!"
    $ playerSprite = 0
    $ oliviaSprite = 4
    olivia "You....you!"
    $ oliviaSprite = 3
    $ playerSprite = 1
    player "Oh, do you have something to say miss ex-reigning champion?"
    $ playerSprite = 0
    $ oliviaSprite = 4
    olivia "I went easy on you because I thought you were a newbie!"
    $ oliviaSprite = 3
    $ playerSprite = 1
    player "Hey you assumed that on your own, I never said I was new."
    $ playerSprite = 0
    $ oliviaSprite = 4
    voice "audio/oliviagameaudio/oliviaangryhmph.wav"
    olivia "Grrr..."
    voice "audio/oliviagameaudio/oliviaonemoretime.wav"
    olivia "One more time!"
    $ oliviaSprite = 3
    $ playerSprite = 1
    player "Nope, I'm taking my win and running away!"
    $ playerSprite = 0
    $ oliviaSprite = 4
    olivia "Ugh. Coward!"
    $ oliviaSprite = 3
    $ playerSprite = 1
    player "You get pretty passionate when it comes to games huh?"
    $ playerSprite = 0
    $ oliviaSprite = 13
    play sound "audio/oliviagameaudio/oliviasorry.wav"
    olivia "Oh...I...sor-"
    $ oliviaSprite = 8
    $ playerSprite = 10
    player "No it's totally cool haha, you'll get your second challenge if you promise to play more with me again sometime."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "I....Okay."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "I actually do have to go now though I wasn't trying to be a dick."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "It's okay."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "See you."
    $ playerSprite = 0
    $ oliviaSprite = 13
    olivia "Bye."
    $ oliviaSprite = 0
    hide fbolivia current
    with Dissolve(0.5)
    player "{i}Well that was a lot of fun. It was great seeing her reaction after I beat her.{/i}"
    player "{i}Something tells me it won't happen again though.{/i}"
    $ playerSprite = 7
    player "{i}Olivia can actually get pretty emotional when it comes to games....She can be pretty cute too.{/i}"
    player "{i}And god damn those legs! Her thighs are top quality....probably shouldn't be thinking like that.{/i}"
    player "{i}I'll come to the arcade again to play with her.{/i}"
    $ oliviaphase1interaction1 = 2
    $ oliviaquestlog = "I should hang out at the arcade again with Olivia."
    hide fbolivia
    hide fbplayer
    hide fs arcade
    jump passtime

# part 3

label oliviaphase1interaction1part3:
    hide screen olivia_atschool
    hide screen uppergui
    scene fs arcade
    with Dissolve(1.0)
    stop music fadeout 10

    $ playerSprite = 0
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    "You entered the arcade again and Olivia spots you right away."
    $ oliviaSprite = 4
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)


    olivia "Okay. Come. Rematch."
    $ oliviaSprite = 3
    $ playerSprite = 1
    player "Woah okay hi to you too."
    $ playerSprite = 0
    hide fbolivia
    hide fbplayer
    show oliviascene arcadegaming1
    with Dissolve(0.5)
    "Olivia shoves the gun in your hand and starts the game up"
    "You play it the same as before and do pretty well getting points"
    "But Olivia wasn't taking her time like you, she's going all in guns ablazing right out the gate, and she was hitting every shot"
    "By the time the game was over she had almost doubled your score and made a new record beating your now 2nd place standing"

    hide oliviascene arcadegaming1

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    $ oliviaSprite = 5

    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    play sound "audio/oliviagameaudio/olivialaugh.wav"
    olivia "Yes! Hahaha yeah!"
    $ playerSprite = 1
    player "Wow, you have a really pretty laugh."
    $ playerSprite = 0
    olivia "...."
    $ oliviaSprite = 13
    olivia "Ah!!"
    olivia "Sorry I got too into it. I-I didn't mean to laugh at you or anything I-"
    $ oliviaSprite = 8
    $ playerSprite = 10
    player "Hey no relax it's fine! You were fucking awesome, look at that new high score!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Thanks..."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Damn it's too bad Mia is so terrible with hand eye coordination. I'd love to play some games with her."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "....Well you could play with me."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Sure! Thanks again for the game, I'm going to head back home but I'll see you later okay?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Okay bye."
    $ oliviaSprite = 8
    hide fbplayer current
    with Dissolve(0.5)
    $ oliviaSprite = 10
    window hide
    pause
    olivia "{i}Usually I'm fine playing alone why...why did I did I get all flustered and ask him to play with me?{/i}"
    image fbolivia headdownflip = im.Flip("Sprites/olivia sprite hands back headdown.png", horizontal=True)
    show fbolivia headdownflip:
        xalign 0.7 ypos 120
    with move
    olivia "{i}I haven't got that excited in a long time I-I was just caught off guard!{/i}"
    show fbolivia current:
        xalign 0.4 ypos 120
    with move
    olivia "{i}It felt nice to have a challenge again...{/i}"
    show fbolivia headdownflip:
        xalign 0.6 ypos 120
    with move
    olivia "{i}Mia's lucky....{/i}"
    show fbolivia current:
        xalign 0.5 ypos 120
    with move
    pause
    $ oliviaSprite = 9
    olivia "Wait did he say I'm pretty?"
    scene fs blackblank
    with Dissolve(0.7)
    player "That was a lot of fun, I wouldn't mind hanging out with Olivia as a regular thing. I should ask if she'd like that."
    $ oliviaSprite = 8
    $ oliviaphase1interaction1 = 3
    $ oliviaquestlog = "Looks like I didn't win this time, I should chat her up at school again."
    hide fs arcade
    hide fbolivia
    hide fbplayer
    jump passtime

# interaction 2
# part 1

label oliviaphase1interaction2part1:
    hide screen olivia_atschool
    hide screen uppergui
    scene fs classroomZOOM
    with Dissolve(0.7)

    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)


    $ oliviaSprite = 0
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    player "Hey, good morning!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    play sound "audio/oliviagameaudio/oliviahey.wav"
    olivia "Hey [povname]."
    $ oliviaSprite = 8
    $ playerSprite = 13
    player "I don't believe it! I got you to look up from your game haha."
    $ oliviaSprite = 13
    $ playerSprite = 0
    olivia "I...I just don't want to be rude."
    $ oliviaSprite = 8
    $ playerSprite = 10
    player "No worries I was just teasing anyways."
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "Oh..."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "So I had a question for you."
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "Yeah?"
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "I love Mia, she's amazing, she's your friend, she's my boo, we all know that right?"
    $ oliviaSprite = 14
    $ playerSprite = 0
    play sound "audio/oliviagameaudio/oliviasnicker.wav"
    olivia "*snicker* Yeah I guess."
    $ oliviaSprite = 8
    $ playerSprite = 15
    player "Haha, well please don't tell her but she's awwwful at games."
    player "I know I mentioned it before but she can't be my like...gaming partner or whatever."
    player "And my buddy Jimmy's in another state and I've only been here a couple months I-"
    $ playerSprite = 14
    olivia "....."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Sorry, the point is I need someone to game with, you're Mia's friend and obviously really good, would you mind?"
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "Um...if it's games I guess it's fine...I did already say I'd play with you."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Thank you you're the best! This was kinda embarassing to ask."
    $ oliviaSprite = 13
    $ playerSprite = 0
    olivia "You're welcome. It's okay."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Do you have class now?"
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "No I think we still have some time."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Oh well okay then. I guess I should ask you what's your favorite type of game to play?"
    player "Or wait no what's your favorite game in general? If you had to pick one!"
    $ playerSprite = 0
    $ oliviaSprite = 10
    olivia "......"
    $ oliviaSprite = 9
    olivia "Well...When I was little, my dad and I would play Mortal Street Caliber 2 all the time."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Oh wow that's super old school! I loved that game but I could only ever play it at my friend's place or an emulator."
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "My dad was busy with work a lot so on his days off we'd just play all day and eat snacks. I love that game."
    $ oliviaSprite = 10
    olivia "He isn't with us anymore, I live with a roomate now. But I do like the memories I have of him and that game."
    $ oliviaSprite = 9
    olivia "I'd love to play it again but I never really brought myself to look for it. Plus I'm sure it's super expensive."
    $ oliviaSprite = 8
    $ playerSprite = 15
    player "Jesus Olivia I didn't know I'm so sorry, that's a great story."
    $ oliviaSprite = 13
    $ playerSprite = 14
    olivia "O-Oh sorry! I didn't mean to ruin the mood or....or whatever."
    $ oliviaSprite = 8
    $ playerSprite = 10
    player "No please, it's totally fine thanks for telling me."
    $ playerSprite = 0
    "The door opens and the professor walks in"
    $ playerSprite = 1
    player "Oh, looks like I gotta go, I'll see you soon okay?"
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "Sure."
    $ oliviaSprite = 8
    hide fbolivia current
    with Dissolve(0.7)
    scene fs schoolhallwayzoomblur
    with Dissolve(0.7)
    $ playerSprite = 7
    player "{i}I have to find that game. Olivia's story was too touching.{/i}"
    player "{i}And honestly I wouldn't mind just getting closer with her.{/i}"
    $ oliviaquestlog = "I should keep a look out for that game Olivia mentioned!"
    if videogamecount == 0:
        player "{i}Wait a minute, didn't I buy the game from the mall already?{/i}"
        player "{i}How the heck did I forget about that!? I'll give it to her at the arcade.{/i}"
        $ oliviaquestlog = "I should give Olivia the game, I hope she'll like it."
    $ oliviaphase1interaction1 = 4
    $ oliviaphase1interaction2 = 1
    jump returnwhereyouare

# part 1 post convo

label oliviaisinclass:
    player "{i}Olivia's class is about to start, I should probably get out of here.{/i}"
    player "{i}Maybe I should look for that game she was talking about? It'd be a awesome surprise.{/i}"

    if videogamecount == 0:
        player "{i}Wait a minute, didn't I buy the game from the mall already?{/i}"
        player "{i}How the heck did I forget about that!? I'll give it to her at the arcade.{/i}"
    jump returnwhereyouare

# part 2

label oliviaphase1interaction2part2:
    scene fs arcade
    hide screen uppergui
    with Dissolve(1.0)
    "You walk into the arcade and see that it's pretty empty"
    $ oliviaSprite = 0
    $ playerSprite = 1
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    "But you see Olivia, and you're excited to give her the good news"
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.7)
    $ oliviaSprite = 8
    player "Hey!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Oh, hi."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "I got you something good!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Got me something?"
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Uh huh, I think you're really gonna like it...."
    $ oliviaSprite = 10
    show fbplayer showvideogame:
        xalign 0.39 ypos 120
    player "Bam!"
    player "Mortal Street Calibur 2: Special Edition!"
    $ playerSprite = 0
    $ oliviaSprite = 13
    olivia "Wha..."
    $ playerSprite = 1
    hide fbplayer showvideogame
    show fbplayer current:
        xalign 0.35 ypos 120
    player "It comes with an extra character that they added after the initial rel-"
    $ playerSprite = 11
    hide fbolivia current
    $ oliviaSprite = 11
    play sound "audio/oliviagameaudio/oliviacrysniff.wav"
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    player "{i}Uh...why is she crying?{/i}"
    $ oliviaSprite = 12
    show fbolivia current:
        xalign 0.6 ypos 120
    with vpunch
    play sound "audio/oliviagameaudio/oliviawhatswrongwithyou.wav"
    olivia "Why did you do this? What's wrong with you??!"
    $ oliviaSprite = 11
    $ playerSprite = 15
    player "I-It's for you. A gift."
    player "You told me it was your favorite game so I thought-"
    $ playerSprite = 14
    $ oliviaSprite = 12
    olivia "This isn't right you...you shouldn't be this nice to me. What do you want??!"
    $ oliviaSprite = 11
    player "{i}I should be careful when I answer her. Do I want to persue some kind of relationship or stay as friends?{/i}"
    menu:
        "{color=#3eab33}You're my gaming partner.{/color}":
            jump gamingpartnerolivia
        "{color=#dd3939}It's just a gift for a friend.{/color}":
            jump justagiftolivia

# still part 2

label gamingpartnerolivia:
    $ playerSprite = 15
    player "Olivia, I don't want anything. I honestly just wanted to make you happy and severely underestimated what this game meant to you, I'm sorry."
    $ playerSprite = 14
    $ oliviaSprite = 10
    olivia "*Sniff*...."
    $ playerSprite = 1
    player "I wanted to do something nice for my new gaming partner. Will you take it?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    play sound "audio/oliviagameaudio/oliviasorry.wav"
    olivia "Okay...thank you...sorry."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "It's fine I'm just happy you're not upset with me."
    player "I'll see you later, give you some space."
    $ playerSprite = 0
    hide fbplayer current
    with Dissolve(1.5)
    $ oliviaSprite = 9
    show fbolivia current:
        xalign 0.55 ypos 120
    with move
    olivia "{size=-10}Wait..{/size}"
    $ oliviaSprite = 10
    hide fbplayer current
    with Dissolve(0.7)
    olivia "{i}He didn't hear me...{/i}"
    olivia "{i}I feel bad. Why is my chest hurting so much?{/i}"
    olivia "...."
    hide fbolivia current
    scene fs livingroom
    with Dissolve(0.7)
    $ playerSprite = 14
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "I really messed up huh? Course she's gonna be apprehensive!"
    player "It hasn't been long since we met and I gave her this super personal gift. Even if it's just a game to me."
    player "But she reacted so strongly."
    $ playerSprite = 0
    player "Let's text Mia, see if she can clear anything up for me."
    $ playerSprite = 2
    player "{cps=25}Hey Mia, you there?{/i}"
    mia "{cps=25}Hello! Yes!{/cps}"
    player "{cps=25}I need some advice, I think I upset Olivia.{/cps}"
    mia "{cps=25}Oh no what happened? :({/cps}"
    player "{i}I'll change some of the details just a bit..{/i}"
    player "{cps=25}I came across an old video game for super cheap so I bought it.{/cps}"
    player "{cps=25}But I don't have a console for it so I gave it to Olivia, but she got really upset when she saw which one it was.{/cps}"
    player "{cps=25}Accused me of trying to manipulate or hurt her in some way.{/cps}"
    mia "{cps=25}Ah okay I see what happened.{/cps}"
    mia "{cps=25}This is really personal so don't tell anyone this please."
    player "{cps=25}Of course.{/cps}"
    mia "{cps=25}Well when Olivia was young, she was often bullied because she was a little weird and more interested in games and computers than girly stuff.{/cps}"
    mia "{cps=25}So she was often by herself, but there were a couple occasions where mean girls would pretend to be nice to her and gave her things she liked.{/cps}"
    mia "{cps=25}But it was just a ploy to embarrass her later on in one way or another, it really made her sad.{/cps}"
    mia "{cps=25}She socialized online, but didn't have any real friends until much later when she met Emily.{/cps}"
    player "{cps=25}Ah I see.{/cps}"
    mia "{cps=25}At first Olivia tried to ignore her and brush her off, but Emily could see that she was suffering and warmed her way into her heart :){/cps}"
    mia "{cps=25}Next thing you know she started hanging out with Emily and Ava, then Charlotte and I joined together and not long after Sophia!{/cps}"
    player "{cps=25}Emily got through to her I guess huh?{/cps}"
    mia "{cps=25}Yup! She can be pretty persistent. And now we're all together!{/cps}"
    mia "{cps=25}Olivia is often on another wavelength than most people XD. She just analyzes and thinks about things differently!"
    player "{cps=25}So when I gave Olivia the game it probably brought her back to those bad times.{/cps}"
    mia "{cps=25}I would have to say so yes. Poor girl, not that it's your fault though! You couldn't have known.{/cps}"
    mia "{cps=25}Would you like me to talk to her and explain?{/cps}"
    player "{cps=25}No babe it's okay, I'll do it myself, clear all this up.{/cps}"
    mia "{cps=25}Okay :D{/cps}"
    player "{cps=25}Thanks a lot babe.{/cps}"
    mia "{cps=25}Of course! Have a great day!{/cps}"
    player "{i}Alright. Now I know why she reacted like that. I should go back and meet her in the arcade.{/i}"
    player "{i}The school has too many people around and I wanna keep this personal.{i}"
    $ oliviaphase1interaction2 = 3
    $ oliviaquestlog = "I should apologize to Olivia..."
    $ item_list.remove("Video Game")
    jump playerlivingroom

# still part 2 but BAD

label justagiftolivia:
    $ playerSprite = 10
    player "Olivia, relax. It's just a thoughtful gift for a friend."
    player "It was probably too thoughtful since I haven't known you long but I saw the opportunity and I took it."
    $ playerSprite = 0
    $ oliviaSprite = 8
    olivia "....."
    $ oliviaSprite = 9
    olivia "Really?"
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Yeah."
    $ oliviaSprite = 10
    olivia "...."
    $ oliviaSprite = 9
    olivia "...Okay I believe you."
    olivia "Thank you [povname]. Mia is a really lucky girl."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Hehe I know."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "I'll see you later?"
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Sure thing, bye."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Bye."
    $ oliviaSprite = 0
    hide fbolivia current
    with Dissolve(0.7)
    pause
    $ playerSprite = 7
    player "I hope I said the right thing. I don't think our relationship will get any stronger now but it's fine since..."
    player "Well since I'm with Mia anyways. So it's fine."
    "You have chosen to end your potential relationship with Olivia."
    "She will now regard you only as a friend and her path is now closed."
    $ oliviaphase1interaction2 = -99
    $ item_list.remove("Video Game")
    jump passtime

label oliviaphase1interaction2part3:

    # PLAYER TALKS TO HER AGAIN IN ARCADE AND APOLOGIZES, BUT OLIVIA FEELS BAD AND THEN OFFERS UP HER BOOBS
    scene fs arcade
    hide screen uppergui
    with Dissolve(1.0)
    $ oliviaSprite = 0
    show fbolivia current:
        xalign 0.6 ypos 120

    player "There she is, I should talk to her before she starts playing something."
    player "Looks like the arcade is pretty empty now too."
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.7)

    player "Hey!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Huh? Oh hi!"
    $ playerSprite = 0
    $ oliviaSprite = 8
    player "{i}Okay, good reaction.{/i}"
    $ playerSprite = 10
    player "So before you say anything I wanted to apologize again."
    $ playerSprite = 1
    player "I hope you don't mind but I spoke to Mia and well..."
    player "I'll just say I have a little more perspective now and I really hope we can be cool."
    $ playerSprite = 8
    player "I-I want to get along I guess is what I'm trying to say and I feel bad and I guess a little awkward."
    $ playerSprite = 0
    $ oliviaSprite = 10
    olivia "I'm the one who feels awkward now."
    $ playerSprite = 8
    $ oliviaSprite = 8
    player "Eh I guess that was a bit of a speech sorry."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "It's okay, I'm actually..."
    $ oliviaSprite = 10
    player "?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "I actually also wanted to apologize. I definitely overreacted and you even went out of your way to learn more about me."
    olivia "Let me make it up to you."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Sure, you wanna play some games?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "No."
    $ playerSprite = 11
    $ oliviaSprite = 8
    player "No?"
    $ oliviaSprite = 9
    olivia "I mean yes."
    $ oliviaSprite = 8
    player "Uh.."
    $ oliviaSprite = 9
    olivia "I mean like...I do want to play games."
    $ oliviaSprite = 10
    pause
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "But that's not enough, I want to give you something in return for the MSC2."
    $ oliviaSprite = 10
    olivia "{i}...and everything else.{/i}"
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "It's really not a big de-"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Yes it is."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "No it's not, I don't mi-"
    $ oliviaSprite = 9
    olivia "Yes it is."
    $ oliviaSprite = 8
    $ playerSprite = 4
    player "...."
    $ playerSprite = 1
    player "O-Okay geez if you insist."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "I just have to think of something, give me a minute."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Sure...you know you don't have to give me anything right this second though.."
    $ playerSprite = 0
    image fbolivia handsbackflip = im.Flip("Sprites/olivia sprite hands back.png", horizontal=True, vertical=False)
    show fbolivia handsbackflip:
        xalign 0.8 ypos 120
    with move
    olivia "Hmmm.."
    $ oliviaSprite = 10
    show fbolivia current:
        xalign 0.6 ypos 120
    with move
    $ playerSprite = 8
    player "{i}She's not listening.{/i}"
    olivia "......"
    show fbolivia handsbackflip:
        xalign 0.8 ypos 120
    with move
    olivia "{i}Charlotte says [povname]'s a pervert but I don't really mind.{/i}"
    show fbolivia current:
        xalign 0.6 ypos 120
    with move
    olivia "{i}I play a bunch of porn games so it's not like I can't call myself a perv either.{/i}"
    $ oliviaSprite = 10
    olivia "But if he is one, he'd probably like something naughty right?"
    $ playerSprite = 1
    player "Sorry what was that now?"
    $ playerSprite = 0
    $ oliviaSprite = 8
    olivia "{i}Guys like boobs right? Heh what am I saying of course they do.{/i}"
    $ oliviaSprite = 9
    olivia "Okay."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Okay?"
    $ playerSprite = 0
    olivia "....."
    $ oliviaSprite = 6
    $ playerSprite = 11
    player "...."
    $ oliviaSprite = 7
    play sound "audio/oliviagameaudio/oliviaboobs.wav"
    olivia "Boobs."
    $ oliviaSprite = 6
    $ playerSprite = 1
    player "What are you doing?"
    $ playerSprite = 0
    $ oliviaSprite = 7
    olivia "Boys like this kind of thing right?"
    $ oliviaSprite = 6
    $ playerSprite = 11
    player "{i}Well I mean yeah but...I certainly wasn't expecting an offer like this.{/i}"
    $ playerSprite = 1
    player "I thought you were gonna like buy me lunch or something!"
    $ playerSprite = 0
    $ oliviaSprite = 7
    olivia "I'm broke and don't work, so that's not an option."
    $ oliviaSprite = 6
    $ playerSprite = 1
    player "Okay..."
    $ playerSprite = 0
    $ oliviaSprite = 7
    olivia "There's no one else here right now....and I won't tell Mia so..go ahead."
    $ oliviaSprite = 6
    player "...."
    $ playerSprite = 1
    player "You're sure? This isn't a trap right, Mia isn't going to jump out and catch me in the act?"
    $ playerSprite = 0
    $ oliviaSprite = 7
    olivia "Ugh hurry up before I change my mind!"
    show fbplayer current behind fbolivia:
        xalign 0.6 ypos 120
    with move

    show fbplayer defaultflip:
        xalign 0.6 ypos 120
    olivia "Huh?"
    hide fbolivia current
    hide fbplayer defaultflip
    show oliviascene MCgroping2:
        xalign 0.65 ypos 120
    with Dissolve(0.4)
    olivia "Why are you behind me?"
    show oliviascene MCgroping1:
        xalign 0.65 ypos 120
    player "If I'm going to do this, I'm gonna do it right."

    image gropingOlivia1:
        "Sprites/olivia mc grop2.png"
        0.7
        "Sprites/olivia grop3.png"
        0.7
        repeat

    image gropingOlivia1talk:
        "Sprites/olivia mc grop2 talk.png"
        0.7
        "Sprites/olivia grop3 talk.png"
        0.7
        repeat

    hide oliviascene MCgroping2
    play sound "audio/oliviagameaudio/oliviaslowpant.wav"
    show gropingOlivia1:
        xalign 0.65 ypos 120

    window hide
    pause
    hide gropingOlivia1
    show gropingOlivia1talk:
        xalign 0.65 ypos 120
    olivia "Ohh..."
    hide gropingOlivia1talk
    show gropingOlivia1:
        xalign 0.65 ypos 120
    player "{i}God damn her tits are huge!{/i}"
    player "{i}I think they're the same size as Mia's.{/i}"
    hide gropingOlivia1
    show gropingOlivia1talk:
        xalign 0.65 ypos 120
    olivia "Hah...hah..."
    hide gropingOlivia1talk
    show gropingOlivia1:
        xalign 0.65 ypos 120
    player "Wait a minute."
    hide gropingOlivia1
    show gropingOlivia1talk:
        xalign 0.65 ypos 120
    olivia "W-What?"
    hide gropingOlivia1talk
    show gropingOlivia1:
        xalign 0.65 ypos 120
    player "Olivia you're not wearing a bra."
    hide gropingOlivia1
    show gropingOlivia1talk:
        xalign 0.65 ypos 120
    olivia "That's right."
    hide gropingOlivia1talk
    show gropingOlivia1:
        xalign 0.65 ypos 120
    player "I'm definitnely not complaining, but how come?"
    hide gropingOlivia1
    show gropingOlivia1talk:
        xalign 0.65 ypos 120
    olivia "It's just..hah...sometimes I don't wear a bra."
    hide gropingOlivia1talk
    show oliviascene MCgropingPinch:
        xalign 0.65 ypos 120
    with vpunch
    olivia "Ahh!"
    player "{i}Heh I'm pinching her nipples as hard as I can and she's just letting me.{/i}"
    window hide
    pause

    image gropingOlivia2:
        "Sprites/olivia mc grop2.png"
        0.7
        "Sprites/olivia grop3.png"
        0.7
        "Sprites/olivia mc grop2.png"
        0.7
        "Sprites/olivia pinch.png"
        0.7
        repeat


    image gropingOlivia2talk:
        "Sprites/olivia mc grop2 talk.png"
        0.7
        "Sprites/olivia grop3 talk.png"
        0.7
        "Sprites/olivia mc grop2 talk.png"
        0.7
        "Sprites/olivia pinch.png"
        0.7
        repeat

    hide oliviascene MCgropingPinch
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "So you gonna tell me WHY you don't wear it sometimes?"
    hide gropingOlivia2
    show gropingOlivia2talk:
        xalign 0.65 ypos 120
    olivia "Um..."
    olivia "Honestly..."
    olivia "It just turns me on."
    player "{i}That is an answer I'm definitely into.{/i}"
    olivia "It just feels good against my skin and I like it when I catch guys staring at my chest..."
    olivia "It...gives me confidence."
    olivia "A-And my mom still has perky breasts today so I'm not worried about them sagging."
    hide gropingOlivia2talk
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "Wow. You're a naughty girl Olivia."
    hide gropingOlivia2
    show gropingOlivia2talk:
        xalign 0.65 ypos 120
    olivia "I can't...hah...argue with that."
    hide gropingOlivia2talk
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "I wasn't expecting it but it really turns me on."
    olivia "...."
    player "You know how much I want to lift up your shirt right now and fuck these giant tits?"
    hide gropingOlivia2
    show gropingOlivia2talk:
        xalign 0.65 ypos 120
    play sound "audio/oliviagameaudio/oliviaslowpant.wav"
    olivia "Ahn..."
    hide gropingOlivia2talk
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "Something I make Mia do is squeeze her tits around my cock as I just thrust into them like a mad man."
    player "And then I just cover her face and boobs in my cum."
    hide gropingOlivia2
    show gropingOlivia2talk:
        xalign 0.65 ypos 120
    olivia "Y...You.."
    olivia "You dont have to talk dirty like that you know."
    hide gropingOlivia2talk
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "So we should sit here in silence as I fondle your tits?"
    player "Wouldnt that be even more awkward?"
    hide gropingOlivia2
    show gropingOlivia2talk:
        xalign 0.65 ypos 120
    olivia "True..."
    hide gropingOlivia2talk
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "Plus I know you're turned on by it, you pretty much admitted it yourself."
    hide gropingOlivia2
    show gropingOlivia2talk:
        xalign 0.65 ypos 120
    olivia "....I guess you're right."
    hide gropingOlivia2talk
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "But I should probably stop now huh?"
    hide gropingOlivia2
    show gropingOlivia2talk:
        xalign 0.65 ypos 120
    olivia "Hah...hah..."
    olivia "{i}Please don't...{/i}"
    window hide
    pause

    hide gropingOlivia2talk

    $ oliviaSprite = 8
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)

    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.7)
    player "You have an amazing body Olivia."
    $ playerSprite = 8
    player "I'll uh...I'll see you later alright? I'll text you."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Okay. I'd like that."
    $ oliviaSprite = 8
    player "{i}She'd like that?{/i}"
    $ playerSprite = 1
    player "What's your number?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "It's 734-2426."
    $ oliviaSprite = 8
    $ renpy.notify("Got Olivia's Number!")
    $ contact_list.append("Olivia")
    player "{i}Ah yes makes sense.{/i}"
    $ playerSprite = 1
    player "Alright great, how about I call you sometime and we ca-"
    show fbplayer current at surpriseshake:
        xalign 0.35 ypos 120
    player "Oh! Do you have a SMES system?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Of course I do."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Bring it over to my place and we can play Mortal Street Caliber!"
    $ playerSprite = 0
    $ oliviaSprite = 14
    play sound "audio/oliviagameaudio/oliviasnicker.wav"
    olivia "Heh. Prepare to lose. Many Times."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "I loved the look on your face when I beat you at the zombie game."
    $ playerSprite = 13
    player "I look forward to seeing it again."
    $ playerSprite = 0
    $ oliviaSprite = 4
    play sound "audio/oliviagameaudio/oliviayouregoingdown.wav"
    olivia "Oh you're going down!"
    $ oliviaSprite = 3
    $ playerSprite = 1
    player "Hahaha I'll see you soon!"
    $ playerSprite = 0
    $ oliviaSprite = 14
    play sound "audio/oliviagameaudio/oliviasnicker.wav"
    olivia "Hehe okay bye."

    hide fbplayer current
    with Dissolve(0.7)
    $ oliviaSprite = 8
    olivia "...."
    image fbolivia normalflip = im.Flip("Sprites/olivia sprite hands back.png", horizontal=True, vertical=False)
    show fbolivia normalflip:
        xalign 0.6 ypos 120
    olivia "...."
    olivia "I'm still really turned on."
    show fbolivia current:
        xalign 0.5 ypos 120
    with move
    pause
    $ oliviaSprite = 10
    olivia "And my breasts are sore...especially my nipples."
    show fbolivia normalflip:
        xalign 0.6 ypos 120
    with move
    olivia "Maybe I should ask Mia what she does when [povname]-"
    show fbolivia current at surpriseshake:
        xalign 0.6 ypos 120
    olivia "Wait. That would be a bad idea right? At the time all I was thinking about was paying back [povname] for the game."
    show fbolivia current:
        xalign 0.4 ypos 120
    with move
    olivia "But if I were dating him....I don't think I would want him to touch any other girls like that."
    show fbolivia normalflip:
        xalign 0.6 ypos 120
    with move
    olivia "God I'm getting even more wet now....Maybe I really am a bad girl."
    olivia "Am I a bad friend too?"
    show fbolivia current:
        xalign 0.5 ypos 120
    with move
    olivia "Ugh these thoughts are confusing I should go home and destress with some kekken 7."
    show fbolivia normalflip:
        xalign 0.5 ypos 120
    pause
    olivia "...."
    olivia "And then maybe masturbate before bed."
    $ oliviaquestlog = "I'm looking forward to playing Mortal Street Calibur with Olivia!"
    $ oliviaphase1interaction2 = 4
    $ oliviaphase1interaction3 = 1
    jump passtime

# part 4

label oliviaphase1interaction2part4:
    hide screen uppergui
    hide screen contacts
    hide screen phonecontacts
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonROOM
    hide screen questboxpreview
    scene fs livingroomnight
    with Dissolve(0.7)
    if failedoliviatest == 1:
        player "{i}Okay don't fall for it this time [povname]! Tits are only temporary but glory is forever!"
        player "{cps=25}Hey! You free? Come over again tonight!{/cps}"
        olivia "{cps=25}Am I bringing MFC2 again?{/cps}"
        player "{cps=25}You better.{/cps}"
        olivia "{cps=25}Heh. This time won't be any different! omw.{/cps}"
        player "We'll just see about that."
    else:
        player "{cps=25}Hey! You should come over tonight! Bring MFC2.{/cps}"
        olivia "{cps=25}Okay I'll head there soon.{/cps}"
        player "Hmm I'm kinda getting nervous."
        player "Relax [povname] relax, we're just playing some games. Gonna have a good time."

    play sound "audio/knock-on-door.wav"
    "*knock knock*"
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.6 ypos 120
    player "Hey, welcome. Come on in."
    $ playerSprite = 0
    $ oliviaSprite = 9
    show fbolivia current:
        xalign 0.8 ypos 120
    olivia "Thanks."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Sit down on the couch that's where I have everything set up."
    scene fs blackblank
    with Dissolve(1.0)
    player "Oh wait sorry let me get the lights."
    olivia "Nice home."
    player "Thanks, want anything to drink?"
    olivia "I'm alright."
    scene oliviascene couchgaming1player
    with Dissolve(0.8)
    player "Okay then, let's dive right into this. It's been a while but I have no plans on losing to you no more than 10 times!"
    scene oliviascene couchgaming1olivia
    play sound "audio/oliviagameaudio/oliviasnicker.wav"
    olivia "That's a shame because I plan on winning 100 times."
    scene oliviascene couchgaming1player
    player "Haha bring it!"
    scene oliviascene couchgaming1
    with Dissolve(0.7)
    "The two of you start up the game and have a great time"
    "Olivia trashed you in the beginning but eventually you got into your zone and won some matches too"
    "After a little more time the friendly atmosphere died down and your competitive spirits began to show"
    scene oliviascene couchgaming1player
    player "Damn....whats the score?"
    scene oliviascene couchgaming1olivia
    olivia "Nine all, we're tied."
    scene oliviascene couchgaming1player
    player "This is gonna be one hell of a tie breaker then."
    scene oliviascene couchgaming1
    olivia "...."
    scene oliviascene couchgaming1player
    player "Maybe I should actually start trying now hmmm?"
    scene oliviascene couchgaming1olivia
    olivia "What."
    scene oliviascene couchgaming1player
    player "I've played the gracious host long enough, time to put you in your place!"
    scene oliviascene couchgaming1olivia
    play sound "audio/oliviagameaudio/oliviapfft.wav"
    olivia "Pfft, a noob like you? You're practically a button masher!"
    scene oliviascene couchgaming1player
    player "Won't be a problem since I'll be playing against a GIRL."
    scene oliviascene couchgaming4
    with vpunch
    olivia "YOU BITCH!"
    player "{i}Hahaha she's so different when she's gaming.{/i}"
    olivia "OKAY. Let's make it interesting!"
    scene oliviascene couchgaming1player
    player "Interesting?"
    scene oliviascene couchgaming1olivia
    olivia "Loser does whatever the winner wants."
    scene oliviascene couchgaming1player
    player "Interesting stakes you've made....alright."
    scene oliviascene couchgaming1olivia
    olivia "ANYTHING."
    scene oliviascene couchgaming1player
    player "Yeah sure..."
    scene oliviascene couchgaming1
    player "{i}Why is she so into this?...I-Is she thinking about doing something naughty?"
    olivia "{i}He's gonna be buying me lunch for a freaking WEEK I swear to god.{/i}"
    "The two of you start the final match!"
    "It's neck and neck, combo-breaker after combo, constant chip damage"
    scene oliviascene couchgaming3
    with vpunch
    player "Oh shit! A distraction!"
    play sound "audio/oliviagameaudio/oliviawhat.wav"
    olivia "Huh? Wha-"
    scene oliviascene couchgaming4
    olivia "Hey!"
    scene oliviascene couchgaming4B
    player "Haha free hit for me!"
    scene oliviascene couchgaming5
    player "What the hell move your hand!"
    olivia "I'm just stretching!"
    player "ONE arm??"
    scene oliviascene couchgaming1olivia
    play sound "audio/oliviagameaudio/oliviasnicker.wav"
    olivia "Hehe and now you're poisoned!"
    scene oliviascene couchgaming1player
    player "Why the hell is there poison in a fighting game anyways!"
    scene oliviascene couchgaming5
    olivia "Hah!"
    player "Again?? Alright that's it."
    scene oliviascene couchgaming6B
    with vpunch
    olivia "...."
    scene oliviascene couchgaming7
    olivia "W-What the fuck that's sexual assault!"
    scene oliviascene couchgaming7B
    player "Shut up you literally asked me to do this the other day!"
    scene oliviascene couchgaming7
    olivia "That doesn't-"
    scene oliviascene couchgaming4B
    with Dissolve(0.6)
    player "You're in the red!"
    olivia "{i}Shit shit I'm gonna lose if I don't do something drastic."
    scene oliviascene couchgaming4
    olivia "Drastic...."
    olivia "{i}I just gotta stop him for a few seconds and the poison will finish him off!{/i}"
    scene oliviascene couchgaming8
    with vpunch
    player "Okay c'mon you can't-"
    player "Olivia wha-"
    scene oliviascene couchgaming9
    player "....."
    player "{i}Holy shit she's flashing me.{/i}"
    menu:
        "{color=#3eab33}Don't look at her tits, win the game{/color}":
            jump winthegame
        "{color=#dd3939}Look at her tits, lose game{/color}":
            jump lookattits

    label lookattits:
        player "{i}How can I look away from this??!{/i}"
        scene oliviascene couchgaming11
        with Dissolve(1.0)
        window hide
        pause
        player "Oh my God. Olivia..."
        olivia "You've already felt them, well now you've seen em too."
        player "You have the tits of a Goddess."
        "Game" "Warning! Health Low!"
        olivia "You really like them huh?"
        player "You're so fucking sexy."
        olivia "{i}C'mon just a little longer!{/i}"
        player "Man the things I would do to y-"
        "Game" "*Death scream* Game over!"
        scene oliviascene couchgaming12
        "Game" "Player 1 wins!"
        window hide
        pause
        olivia "Hehe. Looks like you lose."
        player "Shit yeah. But did I really?"
        olivia "Mmmmm I think so, the game said Player 1 wins and you're buying me lunch for a week."
        player "What??!"
        with vpunch

        if money == 0:
            olivia "Oh....you don't have any money."
            olivia "Lame."
        elif money >= 50:
            "Olivia took {color=#ff0030}50{/color} dollars from you for winning"
            $ money = money - 50
        else:
            "Olivia took {color=#ff0030}[money]{/color} dollars from you for winning"
            $ money = 0

        scene fs blackblank
        with Dissolve(1.0)
        "With that Olivia thanked you for the gaming and her winnings and went home"
        player "Damn my insatiable loins!"
        player "If only I had the will to look away! I wonder what I could've done after winning."
        player "I should invite her over again another night."
        $ failedoliviatest = 1
        $ oliviaquestlog = "I can't believe I lost to Olivia like that! I should invite her over again."
        $ timeofday = "Night"
        jump passtime


    label winthegame:
        player "....."
        scene oliviascene couchgaming10
        player "Not today thot!"
        play sound "audio/oliviagameaudio/oliviawhat.wav"
        olivia "Wha REALLY??!"
        "Game" "*Death Scream* Game over!"
        "Game" "Player 2 wins!"
        scene fs blackblank
        with Dissolve(0.8)
        player "Yeaaahhh! WOOOO!"
        play sound "audio/oliviagameaudio/oliviacongrats.wav"
        olivia "Sigh...Congrats."
        scene oliviascene couchgaming13
        with Dissolve(0.7)
        player "Sorry I got way too into that. Beating you is an honor you know, I'd love to play more."
        player "Sorry I called you a thot. You know I didn't mean that."
        scene oliviascene couchgaming14
        olivia "I-It's fine. I know..."
        scene oliviascene couchgaming15
        with Dissolve(0.7)
        player "{i}Man...she was really prepared to showed me her tits.{/i}" # to showed frfr ong
        player "{i}For a second I almost didn't look away.{/i}"
        scene oliviascene couchgaming15B
        olivia "So I guess...you'll be wanting your reward?"
        scene oliviascene couchgaming13
        player "Oh...."
        scene oliviascene couchgaming13B
        player "{i}Why...why is she saying it so sexually she doesnt usually talk like that.{/i}"
        player "{i}And she doesn't look upset about losing either....that's not like her at all.{/i}"
        scene oliviascene couchgaming15
        player "{i}Maybe I should just test her first.{/i}"
        scene oliviascene couchgaming16B
        player "Uh...lie down on your back and lift up your legs."
        scene oliviascene couchgaming15
        player "{i}That a pretty embarrassing pose there's no way she would do that for someone who isn't her boyfriend."
        scene oliviascene couchgaming17B
        play sound "audio/oliviagameaudio/olivialikethis.wav"
        olivia "Like this?"
        scene oliviascene couchgaming17
        player "So...when you said anything..you really meant-"
        scene oliviascene couchgaming17B
        olivia "I meant it."
        scene oliviascene couchgaming17
        player "And you won't get mad, no matter what I do?"
        scene oliviascene couchgaming17B
        olivia "No."
        scene oliviascene couchgaming18
        with Dissolve(0.7)
        player "You can't run away you know."
        olivia "Mmhm."
        player "{i}Is this happening? I'm so turned on right now...{/i}"
        scene oliviascene couchgaming19
        player "{i}Fuck I'm really taking out my cock. And it's rock hard.{/i}"
        scene oliviascene couchgaming20
        player "Your legs are so sexy..."
        scene oliviascene couchgaming21
        with Dissolve(0.8)

        image couchfuck movie = Movie(channel="couchfuck", play="images/animations/CG4-1 ANIMATED.webm")
        image couchfuck movie2 = Movie(channel="couchfuck", play="images/animations/CG4-2 ANIMATED.webm")
        image couchfuck movie3 = Movie(channel="couchfuck", play="images/animations/CG4-3 ANIMATED.webm")
        image couchfuck movie4 = Movie(channel="couchfuck", play="images/animations/CG4-4 ANIMATED CUM.webm")

        player "I've wanted to thigh fuck you the second we met."
        show couchfuck movie
        window hide
        pause
        player "{i}She's really...really letting me do this.{/i}"
        player "Hah...hah...oh fuck."
        play sound "audio/oliviagameaudio/oliviaslowpant.wav"
        olivia "....."
        show couchfuck movie2
        window hide
        pause
        player "Yeah that's it...Ugh!"
        player "{i}She's not saying anything! She's just panting and staring.{/i}"
        player "Fuck this feels good....I'm getting close."
        show couchfuck movie3
        window hide
        pause
        player "You're being so quiet what are you thinking?"
        olivia "....."
        olivia "I was thinking about how jealous I was of Mia for being able to take take such a big cock."
        show couchfuck movie4
        player "Oh shit!"
        with hpunch
        window hide
        pause
        scene fs livingroomnight
        show fbplayer current:
            xalign 0.35 ypos 120
        with Dissolve(0.7)
        image fbolivia cumstare1 = "Sprites/olivia kum1.png"
        image fbolivia cumstare2 = "Sprites/olivia kum2.png"
        image fbolivia cumtalk = "Sprites/olivia kum talk.png"
        image fbolivia cumblush = "Sprites/olivia kum talk blush.png"
        show fbolivia cumstare1:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        player "Fuck you can't...you can't be so quiet then talk so dirty like that all of a sudden."
        $ playerSprite = 0
        show fbolivia cumstare2:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        olivia "....."
        $ playerSprite = 15
        player "O-Olivia?"
        $ playerSprite = 14
        show fbolivia cumtalk:
            xalign 0.6 ypos 120
        olivia "Why not?"
        show fbolivia cumstare2:
            xalign 0.6 ypos 120
        $ playerSprite = 8
        player "I...good point."
        player "I got cum all over you I'm sorry-"
        $ playerSprite = 11
        show fbolivia cumtalk:
            xalign 0.6 ypos 120
        olivia "It's okay, I don't mind."
        show fbolivia cumstare2:
            xalign 0.6 ypos 120
        $ playerSprite = 1
        player "Really?"
        $ playerSprite = 0
        show fbolivia cumtalk:
            xalign 0.6 ypos 120
        olivia "Yes."
        $ playerSprite = 11
        play sound "audio/oliviagameaudio/oliviaGG.wav"
        olivia "GG, I'm going home now."
        show fbolivia cumstare2:
            xalign 0.6 ypos 120
        $ playerSprite = 1
        player "Uh...alright."
        hide fbolivia cumstare2
        with Dissolve(0.7)
        $ playerSprite = 11
        player "{i}....She didn't even wash up.{/i}"
        player "{i}I hope she's not mad at me...she didn't seem it?{/i}"
        hide fbplayer current
        scene fs overworldnight
        with Dissolve(1.0)
        show fbolivia cumstare1:
            xalign 0.5 ypos 120
        with Dissolve(0.7)
        olivia "...."
        show fbolivia cumtalk:
            xalign 0.5 ypos 120
        olivia "Hah...hah..."
        image fbolivia cumblushflip = im.Flip("Sprites/olivia kum talk blush.png", horizontal=True, vertical=False)

        show fbolivia cumblush:
            xalign 0.5 ypos 120
        olivia "Oh my god oh my god what the fuck was that?!!"
        olivia "He just...he just!"
        show fbolivia cumblushflip:
            xalign 0.75 ypos 120
        with move
        olivia "And I LET him! I...I liked it!"
        olivia "No no no god I'm so embarassed, that line about Mia I just...I just said exactly what I was thinking without...THINKING!"
        olivia "He was fucking my thighs so roughly, it was so hot."
        show fbolivia cumblush:
            xalign 0.4 ypos 120
        with move
        olivia "When I get really turned on like that I just freeze up until..it all explodes out of me."
        show fbolivia cumblushflip:
            xalign 0.6 ypos 120
        with move
        olivia "Even when I touch myself I-"
        olivia "Wait stop."
        olivia "B-Bigger problems!"
        olivia "Obviously I'm not telling Mia. Obviously."
        show fbolivia cumblush:
            xalign 0.5 ypos 120
        with move
        olivia "Was that the only time we're gonna....fool around?"
        show fbolivia cumblushflip:
            xalign 0.7 ypos 120
        with move
        olivia "It was so hot..."
        show fbolivia cumblush:
            xalign 0.5 ypos 120
        with move
        olivia "God I can't think straight I need to masturbate again when I get home to clear my head."
        show fbolivia cumstare1:
            xalign 0.5 ypos 120
        olivia "My dildos aren't even as big as him."
        olivia "...."
        show fbolivia cumblush at surpriseshake:
            xalign 0.5 ypos 120
        olivia "Gah! I'm still covered in cum!"
        olivia "Good thing it's night time..."
        hide fbolivia cumblush
        scene fs blackblank
        with Dissolve(1.0)
        $ oliviaphase1interaction3 = 2
        if currentchapter >= 2:
            $ oliviaquestlog = "That was so hot! I should really talk to her about where to go from here though."
        else:
            $ oliviaquestlog = "That was pretty hot, but I should focus on other things for now."
        jump passtime