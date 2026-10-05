# Olivia scenes.

# Chapter 1


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
    player "{i}She seems nice if not quiet, didn't really get to talk much. I should meet her at the arcade later like she said."
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
    player "Thank you you're the best! This was kinda embarrassing to ask."
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


label oliviaisinclass:
    player "{i}Olivia's class is about to start, I should probably get out of here.{/i}"
    player "{i}Maybe I should look for that game she was talking about? It'd be a awesome surprise.{/i}"

    if videogamecount == 0:
        player "{i}Wait a minute, didn't I buy the game from the mall already?{/i}"
        player "{i}How the heck did I forget about that!? I'll give it to her at the arcade.{/i}"
    jump returnwhereyouare


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
    player "{i}I should be careful when I answer her. Do I want to pursue some kind of relationship or stay as friends?{/i}"
    menu:
        "{color=#3eab33}You're my gaming partner.{/color}":
            jump gamingpartnerolivia
        "{color=#dd3939}It's just a gift for a friend.{/color}":
            jump justagiftolivia


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
    player "{cps=25}Hey Mia, you there?{/cps}"
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
    olivia "You don't have to talk dirty like that you know."
    hide gropingOlivia2talk
    show gropingOlivia2:
        xalign 0.65 ypos 120
    player "So we should sit here in silence as I fondle your tits?"
    player "Wouldn't that be even more awkward?"
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
    player "Damn....what's the score?"
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
        player "{i}Man...she was really prepared to showed me her tits.{/i}"
        player "{i}For a second I almost didn't look away.{/i}"
        scene oliviascene couchgaming15B
        olivia "So I guess...you'll be wanting your reward?"
        scene oliviascene couchgaming13
        player "Oh...."
        scene oliviascene couchgaming13B
        player "{i}Why...why is she saying it so sexually she doesn't usually talk like that.{/i}"
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
        olivia "No no no god I'm so embarrassed, that line about Mia I just...I just said exactly what I was thinking without...THINKING!"
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


# Chapter 2


label gohomeolivia:
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.3 ypos 120
    charlotte "Yes me too."
    $ charlotteSprite = 0
    $ sophiaSprite = 1
    sophia "I wanted to take a bath before bed so I should go too."
    $ sophiaSprite = 0
    $ emilySprite = 1
    emily "Looks like we're splitting up here?"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Mia you gonna go home?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Yes I think my mom wanted my help with some stuff tonight."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Alright girls stay safe on your way back!"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Bye!"
    $ charlotteSprite = 0
    hide fbcharlotte current
    with Dissolve(0.5)
    show fbava runfliptalk:
        xalign 0.25 ypos 120
    ava "See yah! Thanks again for coming out everyone!"
    hide fbava runfliptalk
    with Dissolve(0.5)
    $ sophiaSprite = 2
    sophia "Wait Charlotte! Can your driver take me home??!"
    hide fbsophia current
    with Dissolve(0.5)
    $ miaSprite = 1
    mia "Bye everyone!"
    $ miaSprite = 0
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.3)
    player "See you later Mia."
    $ playerSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    $ emilySprite = 1
    emily "Bye [povname], bye Olivia!"
    $ emilySprite = 0
    $ oliviaSprite = 1
    olivia "Bye Emily."
    $ oliviaSprite = 0
    hide fbemily current
    with Dissolve(0.5)
    player "...."
    $ playerSprite = 0
    $ oliviaSprite = 8
    show fbolivia current:
        xalign 0.65 ypos 120
    with move
    $ playerSprite = 1
    player "Just me an you left."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Finally."
    $ oliviaSprite = 8
    $ playerSprite = 11
    player "Huh?"
    $ playerSprite = 0
    $ oliviaSprite = 14
    olivia "Hehe just a joke."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Haha you got me, well what about you?"
    player "Any plans?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "No not really."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "You wanna come over?"
    player "Maybe we can do something toge-"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Okay."
    $ oliviaSprite = 8
    $ playerSprite = 11
    player "Okay?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Okay I'll come over."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Uh alright great, let's go."
    $ playerSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    player "Hey let me see that game you always play on your Game-Man, must be good if you're always on it."
    olivia "Sure. Just make sure you don't overwrite my save."
    scene oliviascene couchtits1
    with Dissolve(0.7)
    "After you arrive home the two of you chill on the couch and turn on the console"
    "Olivia watches you play with interest"
    pause
    scene oliviascene couchtits2
    with Dissolve(0.7)
    olivia "Okay now careful of the rocks here. They have a bullshit hitbox."
    scene oliviascene couchtits1
    with Dissolve(0.7)
    player "Kay."
    pause
    scene oliviascene couchtits2
    with Dissolve(0.7)
    olivia "Don't attack the bats they just spawn two more when you kill them."
    scene oliviascene couchtits1
    with Dissolve(0.7)
    player "Alright."
    pause
    scene oliviascene couchtits3
    with Dissolve(0.7)
    olivia "The boss is coming, you have to throw back the spikes he shoots at you while avoiding the bats."
    scene oliviascene couchtits1
    with Dissolve(0.7)
    pause
    scene oliviascene couchtits3
    with Dissolve(0.7)
    olivia "No I told you not to attack the bats!"
    scene oliviascene couchtits3angry
    with Dissolve(0.7)
    player "{i}Okay I didn't mind the comments but now she's criticizing me.{/i}"
    olivia "See you did it again! Why would you stand there it's obvious that's where his foot was gonna land!"
    player "Obviously I didn't attack the bats on purpose, they flew in the way when I was throwing the spike back."
    olivia "You have to throw it in the air! How didn't you see that?"
    scene oliviascene couchtits4player
    with Dissolve(0.3)
    player "Oi!"
    player "Backseat gamer! You mind not shouting in my ear about me not beating the boss the first time I play??"
    scene oliviascene couchtits4olivia
    with Dissolve(0.3)
    olivia "Well maybe I wouldn't need to help you if you were competent!"
    olivia "How can I trust you when we play team games if you can't beat this simple boss??"
    scene oliviascene couchtits4player
    with Dissolve(0.3)
    player "Oh I'm sorry, I forgot that they changed the definition of 'help' to 'being an annoying loud bitch'."
    scene oliviascene couchtits4olivia
    with Dissolve(0.3)
    olivia "Stop making excuses for sucking ass at games!"
    scene oliviascene couchtits4player
    with Dissolve(0.3)
    player "Well if YOU think you're so..."
    scene oliviascene couchtits4c
    with Dissolve(0.7)
    player "{i}I know it's kinda fucked but...angry Olivia kinda turns me on.{/i}"
    scene oliviascene couchtits4olivia
    with Dissolve(0.3)
    olivia "So what?"
    scene oliviascene couchtits4c
    with Dissolve(0.7)
    player "{i}I just got an idea.{/i}"
    scene oliviascene couchtits4player
    with Dissolve(0.3)
    player "...so good, why don't you get on my lap and show me how it's done?"
    scene oliviascene couchtits4olivia
    with Dissolve(0.3)
    olivia "With pleasure!"
    scene oliviascene couchtits5olivia
    with Dissolve(1.0)
    olivia "There see? You just have to jump when he slams his foot down."
    player "{i}She actually smells really nice.{/i}"
    olivia "His foot stuns the bats so it's easy to get a clear shot at him with the spike."
    player "Mhmm."
    player "{i}Such a small waist...and huge tits.{/i}"
    olivia "And there! See? It's so easy."
    scene oliviascene couchtits5player
    with Dissolve(0.7)
    player "Yeah."
    scene oliviascene couchtits5olivia
    with Dissolve(1.0)
    olivia "Now this is the second level."
    olivia "There's ice everywhere but it's easy to get used to the sliding."
    scene oliviascene couchtits6
    with Dissolve(1.0)
    olivia "Most of the snowmen are friendly but a couple of them are enemies and will attack when you're not looking."
    player "Mmmm."
    scene oliviascene couchtits7
    with Dissolve(0.7)
    olivia "And then...once you..."
    player "*chuu*"
    olivia "You..you're.."
    player "Uh huh?"
    scene oliviascene couchtits9
    with Dissolve(0.7)
    olivia "Y-You just wanted...to...be naughty didn't you?"
    scene oliviascene couchtits8
    player "Hmmm, maybe."

    image olivianipple play1:
        "CG12-9.png"
        0.7
        "CG12-7B.png"
        0.7
        repeat


    image olivianipple play2:
        "CG12-8.png"
        0.7
        "CG12-8B.png"
        0.7
        repeat

    show olivianipple play2
    with Dissolve(0.7)
    olivia "ehn.."
    olivia "But w-what about the game?"
    show olivianipple play1
    player "Don't care anymore."
    show olivianipple play2
    olivia "You tricked me!"
    show olivianipple play1
    player "No bra again today huh?"
    show olivianipple play2
    olivia "Just a c-coincidence!"
    olivia "W-Wait!"
    scene oliviascene toplesscouch1olivia
    with Dissolve(0.7)
    olivia "Wait."
    scene oliviascene toplesscouch1player
    player "Kay."
    scene oliviascene toplesscouch1
    pause
    player "...."
    scene oliviascene toplesscouch1olivia
    olivia "We..."
    olivia "Can't do that."
    scene oliviascene toplesscouch1player
    player "Can't do what?"
    scene oliviascene toplesscouch1olivia
    olivia "Can't fool around like that."
    olivia "You're dating Mia."
    scene oliviascene toplesscouch1
    player "...."
    scene oliviascene toplesscouch1olivia
    olivia "She's my friend..."
    scene oliviascene toplesscouch2olivia
    with Dissolve(0.7)
    olivia "And if we..do naughty things..."
    scene oliviascene toplesscouch2player
    player "Things like what?"
    scene oliviascene toplesscouch2olivia
    olivia "Like..."
    window hide
    pause
    scene oliviascene toplesscouch3
    with Dissolve(0.7)
    pause
    olivia "Mmmmm."
    scene oliviascene toplesscouch4
    with Dissolve(0.5)
    player "Mhhm."
    scene oliviascene toplesscouch2olivia
    with Dissolve(0.7)
    olivia "Hah...hah..."
    scene oliviascene toplesscouch2
    olivia "...."
    scene oliviascene toplesscouch3
    with Dissolve(0.7)
    olivia "Uhhnmm..."
    scene oliviascene toplesscouch4
    with Dissolve(0.7)
    olivia "{i}What am I doing?{/i}"
    scene oliviascene toplesscouch3
    with Dissolve(0.7)
    pause
    scene oliviascene toplesscouch5
    with Dissolve(0.7)
    pause
    scene oliviascene toplesscouch6
    with Dissolve(0.7)
    pause
    scene oliviascene toplesscouch7
    with Dissolve(0.7)
    pause
    scene oliviascene toplesscouch8
    with Dissolve(0.7)
    pause
    scene oliviascene toplesscouch9
    with Dissolve(0.7)
    player "{i}Holy shit.{/i}"
    olivia "{i}My tits are out again and I'm making out with Mia's boyfriend!{/i}"
    scene oliviascene toplesscouch10
    with Dissolve(0.7)
    olivia "{i}Why does he taste so good? I've never been this horny before!{/i}"
    scene oliviascene toplesscouch11
    with Dissolve(0.7)
    olivia "{i}Is...is that his cock?{/i}"
    olivia "{i}It's rubbing against my ass!{/i}"

    menu:
        "{color=#3eab33}Romantic{/color}":
            jump oliviachapter1rom
        "{color=#dd3939}Naughty{/color}":
            jump oliviachapter1naughty


label oliviachapter1rom:
    scene oliviascene suckoliviatits1c
    with Dissolve(0.7)
    olivia "{i}He's lifting me up now..staring at my boobs.{/i}"
    olivia "{i}What is he going to-{/i}"
    scene oliviascene suckoliviatits1
    with Dissolve(0.7)
    player "I know I've said it before but your tits are amazing."
    scene oliviascene suckoliviatits1b
    with Dissolve(0.7)
    olivia "T-Thanks."
    scene oliviascene suckoliviatits2
    with Dissolve(0.7)
    player "Mmmm!"
    scene oliviascene suckoliviatits3
    with Dissolve(0.7)
    olivia "{i}He really likes them that much?{/i}"
    player "Ahmazheng!"
    scene oliviascene suckoliviatits4c
    with Dissolve(0.7)
    player "{i}How can breasts taste so good?{/i}"
    image oliviatittysuck1:
        "CG14-3B.png"
        0.2
        "CG14-3.png"
        0.2
        "CG14-4C.png"
        0.2
        "CG14-3.png"
        0.1
        "CG14-3B.png"
        0.2

        repeat

    show oliviatittysuck1
    window hide
    pause
    olivia "{i}Oh my god oh my god! Why does this feels SO good!?{/i}"
    olivia "{i}I've never been this turned on!{/i}"
    image oliviatittysuck2:
        "CG14-3B.png"
        0.1
        "CG14-3.png"
        0.1
        "CG14-4C.png"
        0.1
        "CG14-3.png"
        0.05
        "CG14-3B.png"
        0.05

        repeat

    show oliviatittysuck2
    olivia "{i}He's going faster! I think..I think I'm gonna....{/i}"
    player "{i}This is so fucking hot, I can't hold back anymore I have to just...{/i}"
    scene oliviascene suckoliviatits5
    with vpunch
    olivia "AHHHNNN!!!"
    window hide
    olivia "Yeeeess!!!"
    scene oliviascene suckoliviatits6
    with Dissolve(0.7)
    olivia "Hah...hah...*gasp*"
    player "Hehe did you cum from me biting your boobs?"
    scene oliviascene suckoliviatits7
    olivia "W-What? No!"
    olivia "Do you think I'm an anime girl or something??"
    scene oliviascene suckoliviatits8
    with Dissolve(0.7)
    olivia "Geez! That would be...really ridiculous."
    player "Uh huh."
    player "I do love that part about you. Among other things."

    scene oliviascene suckoliviatits6
    with Dissolve(0.7)
    olivia "Huh?"
    player "I like how you keep your moans inside until you can't anymore."
    scene oliviascene suckoliviatits8
    with Dissolve(0.7)
    olivia "I don't know what you're talking about."
    player "And then it bursts out of you super loudly."
    scene oliviascene suckoliviatits6
    with Dissolve(0.7)
    olivia "{size=-10}It's not super loud...{/size}"
    player "Don't worry, I like loud."
    olivia "....."
    player "I wonder what kind of noises you make when you have sex."
    scene oliviascene suckoliviatits8
    with Dissolve(0.7)
    pause
    scene oliviascene toplesscouch8
    with Dissolve(0.7)
    window hide
    pause

    image toplessoliviamakingout:
        "CG13-9.png"
        0.7
        "CG13-9B.png"
        0.7
        repeat
    show toplessoliviamakingout
    window hide
    pause

    scene fs blackblank
    with Dissolve(1.0)

    $ endchapter1_trigger = "1 olivia romantic"
    "You make out with Olivia and her tits for the next while before she heads home"
    "You were slightly disappointed but still satisfied"
    player "{i}Hmmm. We're not just fooling around anymore...{/i}"
    player "{i}I'll have to figure out if I'm willing to take things further with her.{/i}"


    jump startofchapter2


label oliviachapter1naughty:

    image oliviaboobjob movie = Movie(channel="oliviaboobjob", play="images/animations/ations/ANIM15-1.webm")
    image oliviaboobjob movie2 = Movie(channel="oliviaboobjob", play="images/animations/ANIM15-2.webm")
    image oliviaboobjob movie3 = Movie(channel="oliviaboobjob", play="images/animations/ANIM15-3.webm")
    image oliviaboobjob movie4 = Movie(channel="oliviaboobjob", play="images/animations/ANIM15-4.webm")
    image oliviaboobjob movie5 = Movie(channel="oliviaboobjob", play="images/animations/ANIM15-5.webm")
    image oliviaboobjob movie6 = Movie(channel="oliviaboobjob", play="images/animations/ANIM15-6.webm")

    scene oliviascene suckoliviatits6
    with Dissolve(0.7)
    olivia "Hah...hah.."
    player "I want to cum all over your pretty face."
    olivia "....okay."
    scene fs blackblank
    with Dissolve(0.7)
    "After a moment of moving to the ground, Olivia takes out your rock hard cock"
    show oliviaboobjob movie
    window hide
    pause
    player "Fuck yes."
    olivia "{i}I can't believe I'm doing this but at this point there's no way I can stop.{/i}"
    player "Your tits feel amazing Olivia."
    show oliviaboobjob movie2
    window hide
    pause
    olivia "{i}His cock is so big!{/i}"
    player "Yeah, just like that."
    olivia "{i}I can barely picture Mia's pussy taking this thing.{i}"
    show oliviaboobjob movie3
    window hide
    pause
    player "That's it go faster now you {color=#b8233f}SLUT{/color}."
    olivia "{i}I wonder what it would feel like inside me.{/i}"
    player "You're a terrible friend."
    olivia "What?"
    player "I invited you over to game."
    player "Hah...and here you are."
    player "Rubbing your fat tits all over my dick."
    player "You KNOW I'm Mia's boyfriend."
    show oliviaboobjob movie4
    window hide
    pause
    olivia "...."
    player "And you're still not stopping."
    player "You're really trying to make me cum, just cause I asked you to?"
    player "Normally people would be pissed. Yet here you are, betraying Mia's trust."
    olivia "...."
    player "That's right just keep quiet."
    player"I do have to admit though..."
    player "Your tits feel a lot better than Mia's do."
    show oliviaboobjob movie5
    window hide
    pause
    player "Holy shit haha I guess you liked that huh?"
    olivia "Hah...hah.."
    player "I'm getting close, don't you fucking stop."
    window hide
    pause
    show oliviaboobjob movie6
    window hide
    pause
    player "Ahhh fuck yes!!"
    scene oliviascene suckoliviatits9
    with Dissolve(0.7)
    pause
    player "Hah...I'm starting to really like covering you in my cum."
    scene fs blackblank
    with Dissolve(1.0)
    player "How'd it feel? Betraying Mia like that?"
    olivia "..."
    olivia "...."
    olivia "It felt good."
    window hide
    pause

    $ endchapter1_trigger = "1 olivia naughty"

    jump startofchapter2


label oliviaphase2interaction1part1:
    hide screen uppergui
    scene fs arcade
    with Dissolve(1.0)
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.3 ypos 120
    show fbolivia current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 1
    player "Olivia! Hey."
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "Hey [povname]."
    olivia "It's...nice to see you."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Ditto."
    player "Um...I think..w-"
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "We should talk about our relationship?"
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Oh uh yeah. I kinda..I think-"
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "Think you're really starting to like me? Me too."
    olivia "Like..but for you."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Uh, yeah. Spending time with you this past week and a bit was like really really fun."
    player "But obviously...I'm dating Mia. So mayb-"
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "Maybe we should keep things hidden from the other girls until we can be sure of our feelings and future together."
    olivia "That way if things don't work out we can maintain the status quo so nobody has to know and nobody gets hurt?"
    $ playerSprite = 11
    $ oliviaSprite = 8
    player "...."
    player "How..."
    $ oliviaSprite = 9
    $ playerSprite = 0
    olivia "I've thought about you....about US. Like A LOT."
    olivia "Kinda went crazy inside my head."
    $ playerSprite = 1
    $ oliviaSprite = 9
    show fbolivia current:
        xalign 0.47 ypos 120
    with move
    olivia "E-Even now my heart's beating like crazy."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Well, if it helps everything you said was absolutely on point and for what it's worth..."
    $ oliviaSprite = 9
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.33 ypos 120
    with move
    $ playerSprite = 1
    player "You make my heart beat fast too Olivia."
    player "I wouldn't ever consider doing something like this if I wasn't absolutely sure I really liked you."
    $ playerSprite = 0
    $ oliviaSprite = 13
    olivia "Um..wow t-thanks."
    show fbplayer current:
        xalign 0.36 ypos 120
    with move
    $ playerSprite = 1
    player "I kinda..."
    $ playerSprite = 0
    show fbolivia current:
        xalign 0.44 ypos 120
    with move
    olivia "Wanna kiss you right now?"
    $ playerSprite = 1
    player "You read..."
    $ playerSprite = 0
    olivia "My..."
    $ playerSprite = 1
    player "M-"
    $ playerSprite = 11
    $ oliviaSprite = 8

    show fbplayer current at surpriseshake:
        xalign 0.36 ypos 120
    show fbolivia current at surpriseshake:
        xalign 0.44 ypos 120
    "???" "OH MY GOOOOD."
    "???" "SHUUUT UP!"
    olivia "???!"
    player "???!"
    $ pennySprite = 1
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    show fbpenny current:
        xalign 0.8 ypos 120
    "???" "Is this what you've been up to while I was gone Olivia?"
    "???" "No wonder your subscribers have plummeted and your high scores are shit."
    $ pennySprite = 0
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "Penny???"
    hide fbolivia angryfliptalk
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "Uh huh."
    $ pennySprite = 0
    olivia "*Sigh*"
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "I guess you're back from the tournament huh?"
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "That's right. Another win for Penny Arcade."
    penny "It was easy as shit though."
    penny "But let's talk about this guy you were about to start swaping spit with."
    $ pennySprite = 0
    $ playerSprite = 5
    player "I'd introduce myself but you seem kinda like a bitch."
    $ playerSprite = 4
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "She IS a bitch."
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "Wow, a real co-op situation we got going on here."
    penny "So you haven't told your new boyfriend who I am Olivia?"
    $ pennySprite = 0
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "This..is Penny. She is a...very-"
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "Extremely."
    $ pennySprite = 0
    olivia "...."
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "Extremely good gamer."
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "Gamer, streamer extrordinaire, content creator. I'm kinda hot right now."
    $ pennySprite = 0
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "We're also kind of known as rivals in the community."
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "I mean BARELY. You're second to me but is it really a rivalry when the distance is so big? Heh."
    $ pennySprite = 0
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "She's actually known for being quiet and cute on stream, too bad that's just a persona."
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "Hah! You're lucky you get to know the real me."
    $ pennySprite = 0
    show fbolivia angryfliptalk:
        xalign 0.44 ypos 120
    olivia "I almost throw up every time I see you thank someone for a dono acting like a cat-girl."
    show fbolivia angryflip:
        xalign 0.44 ypos 120
    $ pennySprite = 1
    penny "Hey the subscribers love it and it brings in the big bucks."
    penny "Anyways, I've been busy kicking you down to second place on all these machines, I'm about halfway done so I gotta get back to it."
    penny "You."
    $ pennySprite = 0
    $ playerSprite = 1
    player "It's [povname]."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "[povname], Olivia's boyfriend."
    $ playerSPrite = 11
    penny "Let me know when you wanna fuck someone who matters."
    $ pennySprite = 0
    hide fbpenny current
    with Dissolve(0.5)
    $ oliviaSprite = 3
    show fbolivia current:
        xalign 0.5 ypos 120
    $ playerSprite = 15
    player "Wow."
    player "What a lovely young woman."
    $ playerSprite = 14
    $ oliviaSprite = 4
    olivia "Che."
    olivia "I feel dirty just being in her presence."
    $ playerSprite = 15
    $ oliviaSprite = 3
    player "You wanna leave? Go somewhere else together?"
    $ playerSprite = 14
    $ oliviaSprite = 4
    olivia "No, I'm in a bad mood and I wanna take a shower."
    olivia "Come over to my place tonight and we'll hang out there. I'll suck you off."
    $ oliviaSprite = 3
    $ playerSprite = 15
    player "Sure I can pass b-"
    $ playerSprite = 11
    player "Wait what?"
    $ playerSprite = 14
    $ oliviaSprite = 4
    olivia "I'm angry. I wanna suck some cock."
    $ playerSprite = 1
    $ oliviaSprite = 3
    player "Hey whatever helps you get over it! I'm down for tonight, where do you live?"
    $ playerSprite = 0
    $ oliviaSprite = 4
    olivia "Big apartement in Sunnyside, suit 8008."
    $ playerSprite = 1
    $ oliviaSprite = 3
    player "See you there."
    $ playerSprite = 0
    $ oliviaphase2interaction1 = 1
    $ oliviaquestlog = "Did Olivia say she wanted to suck my dick?? I should go to her place tonight."
    $ pennyquesticon = "gui/questboxPenny.png"
    $ pennyquestlog = "Who does Penny think she is? Just cause she's short and cute and hot..."
    jump overworldmap


label oliviaphase2interaction1part2:
    "BZZZZ"
    olivia "Hello?"
    player "Hey! It's me."
    player "{i}I am super looking forward to Olivia's blowjob!{/i}"
    olivia "Hey [povname], come on up I'll buzz you in."
    player "{i}She just seems like she can suck good dick you know?{/i}"
    player "{i}Or is it...suck a dick good?{/i}"
    player "{i}Whatever I'm getting some head tonight that's all that matters.{/i}"

    stop music
    scene fs oliviahouse
    with Dissolve(0.7)
    $ oliviaSprite = 9
    show fbolivia current:
        xalign 0.55 ypos 120
    olivia "Hey [povname] you can come in."
    $ oliviaSprite = 8
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 1
    player "Woah Olivia!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Hehe you like my place?"
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "This is rad!!"
    player "I mean like...it's perfect! It fits you perfectly!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Well only half of it is mine."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Still, your place is really special."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "You think so?"
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "You're pretty special too you know..."
    $ playerSprite = 0
    $ oliviaSprite = 13
    olivia "You're gonna make me blush [povname].."
    $ oliviaSprite = 14
    $ playerSprite = 1
    player "You're cute when you blush."
    $ playerSprite = 0
    $ oliviaSprite = 13
    olivia "Do I get anything for being special?"
    $ oliviaSprite = 14
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.45 ypos 120
    with move
    player "I'm not sure, maybe your bedroom ca-"
    $ oliviaSprite = 8
    $ playerSprite = 0
    $ pennySprite = 1
    show fbpenny pennypjflipyawn:
        xalign 0.45 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 11
    show fbplayer current:
        xalign 0.3 ypos 120
    with move
    $ oliviaSprite = 10
    show fbolivia current:
        xalign 0.65 ypos 120
    with move
    penny "*YAWWWWWWN*"
    $ playerSprite = 11
    player "!!!!!"
    show fbpenny pennypjfliptalk:
        xalign 0.45 ypos 120
    penny "Sup."
    $ pennySprite = 2
    show fbpenny current:
        xalign 0.45 ypos 120
    $ playerSprite = 17
    player "You-"
    $ playerSprite = 11
    pause
    $ playerSprite = 17
    player "But-"
    pause
    show fbpenny pennypjfliptalk:
        xalign 0.45 ypos 120
    penny "Olivia we outta milk?"
    show fbpenny pennypjflip:
        xalign 0.45 ypos 120
    $ oliviaSprite = 4
    olivia "No it's in the back, almost done though."
    $ oliviaSprite = 3
    show fbpenny pennypjfliptalk:
        xalign 0.45 ypos 120
    penny "KK."
    show fbpenny pennypjflip:
        xalign 0.45 ypos 120
    hide fbpenny pennypjflip
    with Dissolve(0.5)
    $ oliviaSprite = 8
    show fbolivia current:
        xalign 0.6 ypos 120
    with move
    $ oliviaSprite = 9
    $ playerSprite = 11
    olivia "Sorry about that."
    $ oliviaSprite = 8
    $ playerSprite = 5
    player "P..Penny? Olivia!!"
    $ playerSprite = 4
    $ oliviaSprite = 9
    olivia "What? What is it?"
    $ oliviaSprite = 8

    show fbplayer current:
        xalign 0.4 ypos 120
    with move
    $ playerSprite = 5
    player "You didn't tell me you LIVE with Penny!!"
    $ playerSprite = 4
    $ oliviaSprite = 9
    olivia "I didn't?"
    $ oliviaSprite = 8
    $ playerSprite = 5
    player "NO!"
    $ playerSprite = 4
    $ oliviaSprite = 9
    olivia "Oh, yeah we're roomates."
    $ oliviaSprite = 8
    $ playerSprite = 5
    player "Isn't she your rival and biggest competitor and all that??!"
    $ playerSprite = 4
    $ oliviaSprite = 9
    olivia "Yeah it sucks."
    $ oliviaSprite = 8
    $ playerSprite = 5
    player "I...okay."
    player "But don't you...can't you like not get in the mood when she's around?"
    $ playerSprite = 11
    $ oliviaSprite = 9
    olivia "Hmmmm, yeah now that I've seen her I kinda ain't feeling it."
    $ oliviaSprite = 8
    player "...."
    $ playerSprite = 4
    pause
    $ playerSprite = 5
    player "We're going to my place."
    $ playerSprite = 4
    $ oliviaSprite = 9
    show fbplayer frownflip:
        xalign 0.45 ypos 120
    olivia "But you just got here?"
    show fbplayer frownflip:
        xalign 0.3 ypos 120
    with move
    player "You can show me around another time, we'll game at my place c'mon."
    $ oliviaSprite = 9
    show fbplayer frownflip:
        xalign -1.5 ypos 120
    with move
    olivia "W-Woah hang on!"
    $ oliviaSprite = 8
    hide fbolivia current
    scene fs blackblank
    with Dissolve(1.0)
    "A little while later at your place..."
    scene oliviascene oliviablowjob1
    with Dissolve(0.7)
    pause
    scene oliviascene oliviablowjob2
    player "Yeah c'mon!"
    player "Dodge!"
    scene oliviascene oliviablowjob1
    olivia "Mmmm.."
    scene oliviascene oliviablowjob2
    player "Dodge!"
    player "Reflect!"
    scene oliviascene oliviablowjob1
    olivia "Gughk!"
    scene oliviascene oliviablowjob2
    player "Get fucked!"
    player "Haha."
    scene oliviascene oliviablowjob3
    with Dissolve(0.7)
    player "Yeah that's it."
    scene oliviascene oliviablowjob3b
    player "That's fucking it!"
    scene oliviascene oliviablowjob3
    player "Keep sucking that fat cock while I dunk on this ass hole."
    scene oliviascene oliviablowjob4
    olivia "Guhg! Gluhk!"
    scene oliviascene oliviablowjob5
    with Dissolve(0.7)
    olivia "MMMMM."
    scene oliviascene oliviablowjob6
    olivia "MMMHFF!"
    scene oliviascene oliviablowjob5
    player "Oh baby that's it keep using your tongue like that!"
    scene oliviascene oliviablowjob6
    olivia "GGUUGGH!!"
    player "Fuck me I'm cumming Olivia!"
    scene oliviascene oliviablowjob7
    with vpunch
    player "AHHH That's so good baby!"
    with flash
    olivia "MMMHMM!"
    scene oliviascene oliviablowjob8
    with Dissolve(0.5)
    olivia "*Gulp* *Gulp*"
    player "You're so fucking pretty, you're so much hotter than Penny."
    scene oliviascene oliviablowjob9
    with Dissolve(0.5)
    olivia "Hmm hmm!"
    player "{i}Looks like she liked that.{/i}"
    player "Yeah swallow it, take every drop..."
    olivia "*Gulp* *Gulp*"
    player "Ahh..."
    scene fs blackblank
    with Dissolve(0.7)

    $ oliviaquestlog = "Olivia gives one hell of a blowjob. This is getting pretty serious."
    $ oliviaphase2interaction1 = 2
    $ pennyquestlog = "Seems like Penny also spends her time at the arcade during the day."
    jump overworldmap


label oliviaphase2interaction2part1:
    hide screen olivia_atschool
    scene fs classroomBlur
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 1
    player "Hey there you are!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Hey, I actually wanted to talk to you."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Oh, yeah sure what's up?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "There's a KeroKero duos tournament at the arcade in a couple days."
    olivia "Wanna be my partner?"
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Oh uh just like that?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Just like that."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Well sure, I know of it but I've never played myself."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "It's okay we'll practice online first, wouldn't bring you in as a total noob."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Yeah shit, should be a lot of fun!"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "So was there a reason you were looking for me?"
    $ playerSprite = 7
    $ oliviaSprite = 8
    player "Ummmm."
    $ playerSprite = 1
    player "Oh yeah shit, I wanted to apologize for bringing you to my place so quickly."
    player "When you wanted to show me yours."
    player "And you know...stuffing my cock down your throat as soon as we sat down."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Oh, I wasn't bothered by it. Honestly spending time away from Penny is a good time for me."
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Ah haha, alright."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "And as for the cock down my throat.."
    $ oliviaSprite = 13
    olivia "Maybe you got the order wrong on who stuffed it there hehe."
    $ oliviaSprite = 8
    player "..."
    $ playerSprite = 1
    player "You are....so cool."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "I know."
    olivia "Message me for practice alright?"
    $ playerSprite = 1
    $ oliviaSprite = 8
    player "Yeah, I'll see you online!"
    $ playerSprite = 0

    $ oliviaquestlog = "I gotta get on my computer tonight to game with Olivia"
    $ oliviaphase2interaction1 = 3
    $ oliviaphase2interaction2 = 1
    jump passtime


label oliviaphase2interaction2part2:
    scene fs blackblank
    with Dissolve(0.7)
    player "Okay...this wire goes here.."
    player "That cord goes there...headphones on.."
    player "Hey hello?"
    scene fs oliviagamingsext1
    player "Can you hear me?"
    olivia "Yup I can hear you, am I good?"
    player "You're good!"
    olivia "Okay, let's get started. Lots to cover."
    player "Let's do it!"
    scene fs blackblank
    with Dissolve(0.7)
    "Olivia went right into explaining things"
    "It was essentially a fighting game on a 2D plane but with 3 dimensional movement"
    scene fs oliviagamingsext1b
    with Dissolve(0.5)
    olivia "Okay! He's coming at you with a froggy kick you have to dodge!"
    scene fs oliviagamingsext1
    player "Got it."
    scene fs oliviagamingsext1b
    olivia "And what do you do after the dodge?"
    scene fs oliviagamingsext1
    player "Leaping uppercut!"
    scene fs oliviagamingsext1d
    olivia "Nice. This one is doing a punch combo watch out!"
    scene fs oliviagamingsext1c
    player "Okay punch punch....Knee! So I counter with tongue whip!"
    scene fs oliviagamingsext1d
    olivia "Awesome, now if it was punch punch kick what would you do?"
    scene fs oliviagamingsext1c
    player "Boing drop!"
    scene fs oliviagamingsext1d
    olivia "Exactly. Okay one more guy coming at you."
    olivia "He's charging his lasor."
    scene fs oliviagamingsext1c
    player "Why would a frog have a-"
    scene fs oliviagamingsext1d
    olivia "Concentrate. How do you respond."
    scene fs oliviagamingsext1
    player "It's a timing thing, I have to wait for his cheeks to expand then..."
    player "Poison Jab!!"
    scene fs oliviagamingsext2
    olivia "Yes! You did it!"
    olivia "You cleared all the test rounds I made for you. I think we're ready."
    player "Nice!"
    player "Thanks for all the help you were a great teacher."
    scene fs oliviagamingsext3
    olivia "Hmmm."
    olivia "The situation now demands a reward and motivation..."
    player "Haha what?"
    olivia "Hmmm.."
    player "Olivia this isn't a foreign dating simulator you don't have to-"
    scene fs oliviagamingsext4
    olivia "Be right back!"
    player "...."
    player "Cute profile."
    scene fs oliviagamingsext5a
    pause
    scene fs oliviagamingsext5b
    olivia "Hey."
    player "I...hey."
    scene fs oliviagamingsext5c
    player "Are you...all the way naked?"
    scene fs oliviagamingsext5d
    olivia "Yeah."
    player "..."
    player "Should I get naked?"
    scene fs oliviagamingsext6
    with Dissolve(0.5)
    pause
    olivia "{size=20}Yes.{/size}"
    scene fs oliviagamingsext7
    with Dissolve(0.7)
    pause
    player "Fuck Olivia your pussy is s-"
    olivia "Hurry up and take your dick out already!"

    show oliviasexting movie1
    pause
    player "Yes ma'am."
    show oliviasexting movie2
    olivia "Hah...hah.."
    player "I've never done this online before"
    olivia "Stop talking and stroke faster!"
    pause
    show oliviasexting movie3
    olivia "Ahhhnnn."
    olivia "Yes...you're so big."
    pause
    show oliviasexting movie4
    olivia "MMMMM!"
    player "Fuck this is so hot Olivia I'm really close!"
    olivia "M-Me too just..."
    olivia "JUST!"
    pause
    show oliviasexting movie5
    olivia "AHHHHH!!!"
    player "FUCK!"
    pause
    scene fs oliviagamingsext14b
    with Dissolve(0.7)
    olivia "Hah...there...reward received."
    scene fs oliviagamingsext14a
    player "What?..hah..oh yeah."
    scene fs oliviagamingsext14b
    olivia "I'll see you at the tournament in two days."
    scene fs oliviagamingsext14a
    player "See you there baby."
    scene fs oliviagamingsext14b
    olivia "Hehe..'baby'."
    scene fs blackblank
    with Dissolve(0.7)
    pause

    $ oliviaquestlog = "I gotta wait for the tournament in 2 days!"
    $ oliviatournyday = dayNumber
    $ oliviaphase2interaction2 = 2
    if pennyscene2 == 2:
        $ pennyscene2 = 3
        $ pennyscene3 = 1
    jump playerRoom


label oliviaphase2interaction3part1:
    hide screen uppergui
    stop music fadeout 5
    scene fs oliviatournament1
    with Dissolve(0.7)
    "Announcer" "Welcome ladies and gentlemen to the DUO'S CHAMPION KEROKERO TOURNAMENT!"
    "Announcer" "I'm assuming you all know the rules but just in case you don't this will be an 8 round tournament"
    "Announcer" "If you & your partner manage to make it to the top you will be playing against THE World champion duo in an online final!"
    "Announcer" "Good luck, have fun, and most importantly-"
    "Everyone shouting" "Time to go FROG WILD!"
    scene fs oliviatournament1b
    olivia "Let's DO THIS [povname]!"
    scene fs oliviatournament1c
    player "You got it!"
    scene fs blackblank
    with Dissolve(0.7)
    "Already hyped from the start the first couple rounds were slam dunks"
    scene fs oliviatournament1d
    with Dissolve(0.5)
    "You and Olivia easily dealt with your opponents"
    scene fs oliviatournament2
    with Dissolve(0.5)
    "Rounds after 4 were way more tough, you started losing 1 or 2 lives with every win"
    scene fs oliviatournament3
    with Dissolve(0.5)
    "Undetered the two of you comboed, combo-broke, and stun-locked(When needed) your way to the later rounds"
    scene fs oliviatournament4
    with Dissolve(0.5)
    "As more and more people were eliminated more and more people started to crowd around you"
    "Then it happened"
    "Announcer" "LADIES AND GENTLEMEN I don't believe it!"
    "Announcer" "Our very own local legend Olivia and her...boyfriend?"
    "Announcer" "Have beaten the 9th round!"
    "*Cheers*"
    "Announcer" "My Froggy fighters...only one fight remains, are you ready to connect online?"
    "Olivia and [povname]" "Yes!"
    "Announcer" "Here we GO!"
    "The fight starts off standard. Olivia takes one opponent while you take the other."
    "Your opponent leaps at you with a Froggy kick, what do you do?"
    menu:
        "Punch":
            jump losefrogfight
        "{color=#008000}Dodge{/color}":
            jump frogfightwin1
        "Counter":
            jump losefrogfight
label frogfightwin1:
    "After you dodge you find yourself right under him"
    menu:
        "Boing Drop":
            jump losefrogfight
        "{color=#008000}Leaping Uppercut{/color}":
            jump frogfightwin2
        "Tongue Whip":
            jump losefrogfight

label frogfightwin2:
    "After he takes the damage, you go on the offensive!"
    menu:
        "{color=#008000}Punch Punch then kick{/color}":
            jump frogfightwin3
        "{color=#008000}Triple Punch{/color}":
            jump frogfightwin3
        "{color=#008000}Kick Knee Punch{/color}":
            jump frogfightwin3
label frogfightwin3:
    "Announcer" "I don't believe it Olivia has died! Leaving her partner to face two opponents!"
    "Olivia's opponent killed her but he's low HP and attacks you with a punch punch knee combo"
    menu:
        "Boing Drop":
            jump losefrogfight
        "Leaping Uppercut":
            jump losefrogfight
        "{color=#008000}Tongue Whip{/color}":
            jump frogfightwin4
label frogfightwin4:
    "You countered Olivia's now defeated opponent and see that yours started charging a lasor attack!"
    menu:
        "Look at his eyes":
            jump losefrogfight
        "{color=#008000}Look at his cheeks{/color}":
            jump frogfightwin5
        "Look at his legs":
            jump losefrogfight
label frogfightwin5:
    "You got the timing right! What attack will you use to finish him off?"
    menu:
        "leaping uppercut!":
            jump losefrogfight
        "Boing drop!":
            jump losefrogfight
        "{color=#008000}Poison Jab!{/color}":
            jump frogfightwin

label frogfightwin:
    scene fs oliviatournament5
    "Announcer" "They did it they did it they did it!!!"
    "Announcer" "CONGRATULATIONS Olivia and [povname]!"
    pause
    player "Let's gooooo!"
    olivia "YESSSS!"
    scene fs oliviatournament6
    "*SLAP*"
    "Announcer" "What a spectacle!"
    scene fs blackblank
    with Dissolve(0.5)
    "Announcer" "Your plaque and trophy will be delivered to you in 8 business days"
    "Announcer" "Now tell me, how do you two plan on celebrating your remarkable win tonight?"
    olivia "Well.."

    show oliviatournysex movie2
    olivia "AHN Hah Hah!"
    player "YES!"
    player "God I love watching your big fucking tits bounce!"
    scene fs oliviatournament10a
    with Dissolve(0.5)
    olivia "[povname]! [povname]!"
    olivia "YES YES!"
    show oliviatournysex movie1
    with Dissolve(0.7)
    player "Let's slow down a bit huh? Savor it a bit."
    olivia "Y-You're supposed to start slow dummy, I wasn't prepared for..."
    player "For?"
    olivia "Such a rough pounding."
    player "Haha I was surprised when you moaned so loud from the get go."
    player "So you prefer it nice and slow?"
    olivia "I..hah...didn't say that."
    pause
    show oliviatournysex movie2
    player "Then I think you CAN HANDLE SOME MORE!"
    olivia "OH MY GOD!!"
    pause
    scene fs oliviatournament10a
    with Dissolve(0.5)
    olivia "AHN!!!"
    scene fs oliviatournament10b
    olivia "Harder!"
    penny "God damn."
    show oliviatournysex movie2
    olivia "I'm CUMMING!"
    player "Fuck me too! Should I pull ou-"
    olivia "DON'T YOU FUCKING STOP!!"
    show oliviatournysex movie3
    olivia "AHHHN!!"
    player "Fucking fill you up baby!"
    pause
    scene fs oliviatournament7
    with Dissolve(1.0)
    pause
    olivia "Hah...hah.."
    player "Sorry, there was no way I could pull out, hope you don't mind?"
    olivia "I love your cum."
    olivia "I love your cum in my pussy."
    player "God you're fucking beautiful..."
    scene fs blackblank
    with Dissolve(1.0)
    olivia "T-Thanks."
    "After some more rigorous fucking you fell asleep at Olivia's place then headed home in the morning"
    $ oliviaquestlog = "I wonder what I can get up to with Olivia at the beach trip?"
    if currentchapter >= 3:
        $ oliviaquestlog = "That was some incredible sex. I should chat up Olivia at the school."
    $ oliviaphase2interaction2 = 3
    $ oliviaphase2interaction3 = 1
    if pennyscene5 == 1:
        $ pennyquestlog = "Penny is a full blown internet whore...I kinda wanna talk to her about it.Maybe at the arcade?"
    jump passtime

label losefrogfight:
    scene fs blackblank
    with Dissolve(0.5)
    "Announcer" "Oh no! Looks like [povname] messed up and got mega-countered!"
    "Your loss cost you the game, which cost you the match"
    "At least there's always tomorrow night!"
    jump passtime


label oliviabeachchapter2end:
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
    $ playerSprite = 18
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbolivia current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 19
    player "Olivia hey!"
    $ playerSprite = 18
    $ oliviaSprite = 17
    olivia "[povname]. Hey."
    $ oliviaSprite = 15
    $ playerSprite = 19
    player "You doing alright? Having fun."
    $ playerSprite = 18
    $ oliviaSprite = 17
    olivia "Yeah sure, Ava's worn me out so I'm done with my physical activity for the day."
    $ oliviaSprite = 15
    $ playerSprite = 19
    player "Haha that's fair."
    $ playerSprite = 18

    if oliviaphase2interaction3 >= 1:
        "Would you like to end the day with Olivia?"
        menu:
            "Romance":
                jump oliviachapter2romance
            "Naughty":
                jump oliviachapter2naughty
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach

    label oliviachapter2romance:
        $ playerSprite = 19
        player "You wanna walk with me then?"
        player "Very low physical levels."
        $ playerSprite = 18
        $ oliviaSprite = 17
        olivia "Hehe. Yeah sure."
        $ oliviaSprite = 15
        scene fs beachpictureempty
        with Dissolve(0.7)
        pause

        show fbplayer current:
            xalign 0.4 ypos 120
        show fbolivia current:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        $ playerSprite = 19
        player "You look nice. The bikini looks nice."
        $ playerSprite = 18
        $ oliviaSprite = 17
        olivia "Um thanks.."
        olivia "I don't often wear bikinis."
        $ playerSprite = 19
        $ oliviaSprite = 17
        player "Cause it shows so much skin."
        olivia "It shows so much skin."
        $ oliviaSprite = 15
        player "...I like it though."
        $ oliviaSprite = 17
        $ playerSprite = 18
        olivia "Cause it shows so much skin."
        $ oliviaSprite = 15
        $ playerSprite = 19
        player "It shows so much skin."
        $ playerSprite = 18
        olivia "..."
        $ playerSprite = 19
        player "Hahaha!"
        $ playerSprite = 18
        $ oliviaSprite = 17
        olivia "Hahaha!"
        olivia "I really...this is nice [povname]."
        $ oliviaSprite = 15
        show fbplayer current:
            xalign 0.5 ypos 120
        with move
        $ playerSprite = 19
        player "Hey so.."
        player "I feel like we made the right decision being together to...figure things out."
        $ playerSprite = 18
        $ oliviaSprite = 17
        olivia "I know I..."
        olivia "Things are moving fast and...and I'm feeling things you know?"
        $ oliviaSprite = 15
        $ playerSprite = 19
        player "Romantic feelings or naughty feelings hehe?"
        $ playerSprite = 18
        $ oliviaSprite = 17
        olivia "Haha both I guess.."
        olivia "Earlier I had an easy time agreeing with this arrangement cause I thought if it doesn't work out.."
        olivia "We end it, it's done. I wouldn't have a problem moving on."
        olivia "But I didn't really think about what would happen if things went the opposite direction.."
        olivia "It's awkward and scary..."
        show fbolivia current:
            xalign 0.55 ypos 120
        with move
        olivia "Is this l-love? Is it even right?"
        olivia "You know?"
        $ playerSprite = 19
        player "Olivia..."
        player "I'm sorry I wasn't paying attention at all your bikini is so fucking distracting."
        $ playerSprite = 18
        $ oliviaSprite = 17
        show fbolivia current at surpriseshake:
            xalign 0.6 ypos 120
        olivia "OHMYGOD [povname]!"
        $ oliviaSprite = 15
        $ playerSprite = 19
        player "Hahaha I'm kidding I'm kidding."
        $ playerSprite = 18
        $ oliviaSprite = 17
        olivia "Geez!"
        $ oliviaSprite = 15
        $ playerSprite = 19
        player "Here, let's go by those rocks over there and I'll show you how I feel about you."
        $ playerSprite = 18
        $ oliviaSprite = 17
        olivia "...Hehe okay."
        $ oliviaSprite = 15
        scene fs blackblank
        with Dissolve(0.7)
        "A little while later.."

        scene fs beach
        with Dissolve(0.7)

        $ miaSprite = 14
        $ charlotteSprite = 14
        $ avaSprite = 22
        $ sophiaSprite = 12
        $ emilySprite = 6
        show fbmia current:
            xalign 0.25 xzoom -1.0 ypos 120
        show fbcharlotte current:
            xalign 0.1 xzoom -1.0 ypos 120
        show fbava current behind fbmia:
            xalign 0.4 xzoom -1.0 ypos 120
        show fbsophia current:
            xalign 0.62 ypos 120
        show fbemily current:
            xalign 0.52 ypos 120
        with Dissolve(0.7)
        $ avaSprite = 23
        ava "Phew! That was a lot of fun."
        $ avaSprite = 22
        $ emilySprite = 8
        emily "Haha yeah!"
        $ emilySprite = 6
        $ sophiaSprite = 11
        sophia "Oh my gosh can we PLEASE do something relaxing now?"
        $ sophiaSprite = 12
        $ charlotteSprite = 15
        charlotte "I agree, I can't do anymore physical activity."
        $ charlotteSprite = 14
        $ avaSprite = 23
        ava "Okay okay geez sorry everyone for trying to have some fun!"
        $ avaSprite = 22
        $ emilySprite = 8
        emily "Alright everybody let's calm down."
        $ emilySprite = 6
        $ miaSprite = 17
        mia "I'm hungry, maybe we can order something?"
        $ miaSprite = 14
        $ emilySprite = 8
        emily "Good Idea, where's Olivia?"
        $ emilySprite = 6
        $ sophiaSprite = 11
        sophia "Hmm, I havn't seen her or [povname] for a while..."
        $ sophiaSprite = 12
        $ emilySprite = 8
        show oliviabeachsex movie1
        olivia "Hah hah hah!"
        player "Fuck baby your pussy is so good!"
        show oliviabeachsex movie2
        olivia "Ahn!"
        olivia "C-Call me baby again!"
        pause
        show oliviabeachsex movie3
        player "You like it when I'm inside you baby?"
        olivia "Yes!!"
        player "Make me believe you!"
        olivia "I-I love it! I love your cock!"
        olivia "C-Cum...!"
        player "What?"
        olivia "CUM INSIDE ME [povname] PLEASE!!!"
        show oliviabeachsex movie4
        olivia "AHHHN!!!"
        player "UGGH!!"
        pause
        show oliviabeachsex movie5
        with Dissolve(0.7)
        olivia "Hah...hah.."
        player "You okay baby?"
        olivia "Yes...that was really good."
        pause
        scene fs blackblank
        with Dissolve(1.0)
        player "You okay to head back?"
        olivia "Yeah le-wait.."
        olivia "Where's my top?"

        scene fs beach
        with Dissolve(0.7)

        $ miaSprite = 14
        $ charlotteSprite = 14
        $ avaSprite = 22
        $ sophiaSprite = 12
        $ emilySprite = 6
        show fbmia current:
            xalign 0.25 xzoom -1.0 ypos 120
        show fbcharlotte current:
            xalign 0.1 xzoom -1.0 ypos 120
        show fbava current behind fbmia:
            xalign 0.4 xzoom -1.0 ypos 120
        show fbsophia current:
            xalign 0.62 ypos 120
        show fbemily current:
            xalign 0.52 ypos 120
        with Dissolve(0.7)
        pause
        $ emilySprite = 6
        $ oliviaSprite = 16
        show fbplayer current:
            xalign 0.95 xzoom -1.0 ypos 120
        show fbolivia current:
            xalign 0.85 ypos 120
        with Dissolve(0.5)
        $ playerSprite = 19
        player "Hey sorry guys!"
        $ playerSprite = 18
        show fbsophia current:
            xalign 0.68 xzoom -1.0 ypos 120
        show fbemily current:
            xalign 0.52 xzoom -1.0 ypos 120
        $ charlotteSprite = 15
        charlotte "Where were you?"
        $ charlotteSprite = 14
        $ emilySprite = 8
        emily "Oh my gosh Olivia!"
        $ emilySprite = 6
        $ sophiaSprite = 11
        sophia "Your boobs!"
        $ sophiaSprite = 12
        $ oliviaSprite = 19
        olivia "It's fine."
        $ oliviaSprite = 16
        $ playerSprite = 19
        player "Olivia lost her top. I was uh..helping her find it."
        $ playerSprite = 18
        $ miaSprite = 17
        mia "Ohhhh!"
        $ miaSprite = 14
        $ oliviaSprite = 19
        olivia "Yeah. [povname] really came in handy(me)."
        $ oliviaSprite = 16
        $ sophiaSprite = 11
        sophia "But you never found it?"
        $ sophiaSprite = 12
        $ oliviaSprite = 19
        olivia "....Nope."
        $ oliviaSprite = 16
        scene fs blackblank
        with Dissolve(1.0)
        mia "Aww well that's nice of you to help her out like that!"
        player "Yeah of course, Olivia you can count on me anytime."
        olivia "Hehe, of course thanks."

        $ endchapter2_trigger = "2 olivia romantic"

        jump startofchapter3

    label oliviachapter2naughty:
            $ playerSprite = 19
            player "Let's spend some time together then."
            $ playerSprite = 18
            $ oliviaSprite = 17
            olivia "Oh yeah uh sure, I'd like that."
            $ oliviaSprite = 15
            scene fs beachpictureempty
            with Dissolve(0.7)
            pause

            show fbplayer current:
                xalign 0.4 ypos 120
            show fbolivia current:
                xalign 0.6 ypos 120
            with Dissolve(0.7)
            $ playerSprite = 19
            player "You look nice. The bikini looks nice."
            $ playerSprite = 18
            $ oliviaSprite = 17
            olivia "Um thanks.."
            olivia "I don't often wear bikinis."
            $ oliviaSprite = 15
            $ playerSprite = 19
            player "Good, cause I wouldn't be able to take my hands off of you."
            $ playerSprite = 18
            $ oliviaSprite = 17
            olivia "Oh...um yeah I...nice."
            $ oliviaSprite = 15
            $ playerSprite = 19
            player "Haha cute response."
            $ playerSprite = 18
            $ oliviaSprite = 17
            olivia "T-Thanks."
            $ oliviaSprite = 15
            $ playerSprite = 19
            player "I'm gonna be honest, I haven't stopped thinking about the sex we had."
            $ playerSprite = 18
            olivia "..."
            $ playerSprite = 19
            show fbplayer current:
                xalign 0.5
            with move
            player "I know you're the same."
            $ playerSprite = 18
            olivia "..."
            $ playerSprite = 19
            player "Tell you what, there's some rocks at the end of the beach over there."
            player "Let's use them for some privacy."
            $ playerSprite = 18
            olivia "..."
            $ oliviaSprite = 17
            olivia "I-"

            show oliviabeachsex movie1
            olivia "Ahn Ahn Ahn!!"
            player "Fuck baby your pussy is so good!"
            olivia "MMMMMMM!"
            player "You like that huh? You like my big cock inside you?"
            pause
            show oliviabeachsex movie2
            olivia "Hah hah hah!"
            olivia "Y-Yes!"
            player "Your friends are probably wondering where we are!"
            olivia "I-I dunno!"
            pause
            show oliviabeachsex movie3
            player "Don't act innocent!"
            olivia "AHHH!!!"
            player "You're FUCKING one of their boyfriends aren't you!?"
            olivia "Oh G-God!"
            player "You're squeezing me so hard baby, that really turns you on huh?"
            player "You like the fact that we're cheating!"
            olivia "I-I wait [povname]!"
            player "You're gonna fucking cum aren't you!?"
            player "Tell me you're a slut and I'll fill your pussy to the brim!"
            olivia "I-I'm a slut!"
            olivia "I'm A HUGE SLUT AND I WANT YOU CUM INSIDE ME [povname]!!!"
            olivia "I-I like that Mia's boyfriend is fucking me!"
            olivia "It's so wrong but it feels so go-"
            show oliviabeachsex movie4
            olivia "AHHHN!!!"
            player "UGGH!!"
            pause
            show oliviabeachsex movie5
            with Dissolve(0.7)
            olivia "Hah...hah.."
            player "Good job."
            olivia "God I'm...I'm such a-."
            player "It's fine Olivia, I'm at fault too."
            pause
            scene fs blackblank
            with Dissolve(1.0)
            player "You okay to head back?"
            olivia "Yeah le-wait.."
            olivia "Where's my top?"

            scene fs beach
            with Dissolve(0.7)

            $ miaSprite = 14
            $ charlotteSprite = 14
            $ avaSprite = 22
            $ sophiaSprite = 12
            $ emilySprite = 6
            show fbmia current:
                xalign 0.25 xzoom -1.0 ypos 120
            show fbcharlotte current:
                xalign 0.1 xzoom -1.0 ypos 120
            show fbava current behind fbmia:
                xalign 0.4 xzoom -1.0 ypos 120
            show fbsophia current:
                xalign 0.62 ypos 120
            show fbemily current:
                xalign 0.52 ypos 120
            with Dissolve(0.7)
            $ avaSprite = 23
            ava "Phew! That was a lot of fun."
            $ avaSprite = 22
            $ emilySprite = 8
            emily "Haha yeah!"
            $ emilySprite = 6
            $ sophiaSprite = 11
            sophia "Oh my gosh can we PLEASE do something relaxing now?"
            $ sophiaSprite = 12
            $ charlotteSprite = 15
            charlotte "I agree, I can't do anymore physical activity."
            $ charlotteSprite = 14
            $ avaSprite = 23
            ava "Okay okay geez sorry everyone for trying to have some fun!"
            $ avaSprite = 22
            $ emilySprite = 8
            emily "Alright everybody let's calm down."
            $ emilySprite = 6
            $ miaSprite = 17
            mia "I'm hungry, maybe we can order something?"
            $ miaSprite = 14
            $ emilySprite = 8
            emily "Good Idea, where's Olivia?"
            $ emilySprite = 6
            $ sophiaSprite = 11
            sophia "Hmm, I havn't seen her or [povname] for a while..."
            $ sophiaSprite = 12
            $ emilySprite = 8
            emily "I think I saw [povname] go for a walk?"
            $ emilySprite = 6
            $ oliviaSprite = 16
            show fbplayer current:
                xalign 0.95 xzoom -1.0 ypos 120
            show fbolivia current:
                xalign 0.85 ypos 120
            with Dissolve(0.5)
            $ playerSprite = 19
            player "Hey sorry guys!"
            $ playerSprite = 18
            show fbsophia current:
                xalign 0.68 xzoom -1.0 ypos 120
            show fbemily current:
                xalign 0.52 xzoom -1.0 ypos 120
            $ charlotteSprite = 15
            charlotte "Where were you?"
            $ charlotteSprite = 14
            $ emilySprite = 8
            emily "Oh my gosh Olivia!"
            $ emilySprite = 6
            $ sophiaSprite = 11
            sophia "Your boobs!"
            $ sophiaSprite = 12
            $ oliviaSprite = 19
            olivia "It's fine."
            $ oliviaSprite = 16
            $ playerSprite = 19
            player "Olivia lost her top. I was uh..helping her find it."
            $ playerSprite = 18
            $ miaSprite = 17
            mia "Ohhhh!"
            $ miaSprite = 14
            $ oliviaSprite = 19
            olivia "Um Yeah."
            $ oliviaSprite = 16
            $ miaSprite = 17
            mia "Awww I'm sorry Olivia, I'm glad [povname] tried to help though!"
            $ miaSprite = 14
            $ oliviaSprite = 19
            olivia "Like I said it's....fine."
            $ oliviaSprite = 16
            scene fs blackblank
            with Dissolve(1.0)
            mia "Let's go shopping again soon, just you and me we'll get you another one!"
            olivia "Oh mia. N-No-"
            mia "I insist!"
            olivia "..."
            olivia "Okay."

            $ endchapter2_trigger = "2 olivia naughty"

            jump startofchapter3

# Chapter 3


label oliviaphase3interaction1part1:
    hide screen olivia_atschool
    $ oliviaSprite = 0
    $ playerSprite = 1
    show fbolivia current:
        xalign 0.5 ypos 120
    with Dissolve(0.5)
    pause
    show fbplayer current:
        xalign 0.35 ypos 120
    player "Hello World FeroFero Champion Olivia."
    $ oliviaSprite = 9
    olivia "Oh!"
    $ oliviaSprite = 14
    olivia "Hello World FeroFero Champion [povname]."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Hehe."
    player "How you doing baby?"
    $ playerSprite = 0
    olivia "{i}I can feel my ovaries thump when he calls me that{/i}"
    $ oliviaSprite = 9
    olivia "I'm doing great, midterms are finished now so I can game all I want for a bit."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Sweet!"
    player "Do you have time to hang out then?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Yeah. Actually come over later I'm just gonna grab something to eat first."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "Sounds great, I'll see you this evening then."
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "Cool."
    $ oliviaSprite = 8
    $ oliviaquestlog = "Gonna hang out with Olivia at her place tonight"
    $ oliviaphase2interaction3 = 2
    $ oliviaphase3interaction1 = 1
    jump classroom2

label oliviaphase3interaction1part2:
    stop music fadeout 5
    scene fs oliviahouse
    with Dissolve(0.7)
    pause
    scene fs oliviaboobjob1
    with Dissolve(0.5)
    pause
    "GameMan" "*Plink Plink*"
    "GameMan" "*Boom*"
    penny "Olivia?"
    scene fs oliviaboobjob2
    olivia "Hey Penny. Finally done streaming?"
    scene fs oliviaboobjob1
    penny "Yeah I'm headed out to the convienence store."
    penny "Anything we need?"
    scene fs oliviaboobjob2
    olivia "Not really no."
    scene fs oliviaboobjob1
    penny "Anything you want?"
    player "Mmmph."
    scene fs oliviaboobjob2
    olivia "No I'm...I'm good."
    scene fs oliviaboobjob1
    penny "Alright."
    pause
    "GameMan" "*Plink Plink*"
    scene fs oliviaboobjob3
    olivia "...."
    player "Mmmm."
    scene fs oliviaboobjob4
    with Dissolve(0.5)
    olivia "Ah...you know she definitely could've heard you."
    player "Mmhmm?"
    olivia "You don't care at all."
    scene fs oliviaboobjob5
    with Dissolve(0.5)
    olivia "Hah..."
    scene fs oliviaboobjob6
    olivia "AHN."
    player "*Suck*"
    scene fs oliviaboobjob7
    olivia "That f-feels really good."
    scene fs oliviaboobjob8
    with Dissolve(0.7)
    player "*Chuu*"
    olivia "Ehnn..."
    player "I need to fuck your fat tits."
    olivia "Hah...okay."
    scene fs oliviaboobjob9
    with Dissolve(0.7)
    "*Ziiiip*"
    pause
    scene fs oliviaboobjob10
    with Dissolve(0.7)
    player "God you're so beautiful Olivia."
    olivia "...."
    player "Squish those tits together!"
    scene fs oliviaboobjob11
    with Dissolve(0.5)
    pause
    show oliviaboobjob movie1
    pause
    player "Yeah..."
    player "What do you think of my fat fucking cock baby?"
    olivia "...."
    show oliviaboobjob movie2
    player "C'mere..."
    pause
    olivia "Hah...hah.."
    show oliviaboobjob movie3
    player "Oh yeah. That's fucking good!"
    olivia "Ahn..."
    player "Your tits feel so good I might cum baby, is that what you want?"
    olivia "Yes."
    player "tell me what do you want. Say it."
    olivia "I want you to use my tits to cum."
    olivia "P-Please."
    show oliviaboobjob movie4
    player "AGH!!"
    olivia "Ahhh..."
    pause
    scene fs oliviaboobjob12
    with Dissolve(0.7)
    player "Hah...hah..fuck baby."
    scene fs oliviaboobjob13
    penny "Wow that's a lot."
    olivia "Huh??"
    penny "Yeah I was just getting my shoes on when I said bye. You two started tittyfucking before even listening for the door to close."
    player "Uh...sorry?"
    penny "Oh it's fine, got one hell of a show."
    player "Glad you're not mad."
    olivia "!!!!"
    penny "Doesn't seem like you got the couch dirty so it's all good."
    penny "You look really hot with cum all over your face Olivia."
    olivia "...."
    scene fs blackblank
    with Dissolve(0.7)
    penny "Haha, maybe next time you and I can make use of the couch [povname]?"
    olivia "!!!"
    penny "Don't worry Olivia, you can watch."
    player "Oh boy..."
    pause

    $ oliviaphase3interaction1 = 2
    $ oliviaquestlog = "No more Olivia content in this version (ch2.5)"
    jump passtime
