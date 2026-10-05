# Stephanie scenes.

# Chapter 2


label stephaniescene1part1:
    hide screen uppergui
    stop music fadeout 5
    stop sound fadeout 5
    "BZZZZ"
    stephanie "Ah, you're here. Good timing."
    player "I just w-"
    stephanie "Just come up."
    scene fs stephaniehouse
    with Dissolve(1.0)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbstephanie current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Alright I'm here, let's get this over with."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Would you relax?"
    stephanie "All I want you to do, is call Emily."
    $ playerSprite = 1
    $ stephanieSprite = 0
    player "What?"
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "You have her number right? Call her and get her to come over."
    $ playerSprite = 1
    $ stephanieSprite = 0
    player "What are you planning?"
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Just a harmless little prank. I promise."
    $ stephanieSprite = 0
    player "..."
    $ playerSprite = 2
    player "Okay one second."
    player "..."
    player "Hey Em? I have a weird request for you."
    scene fs blackblank
    with Dissolve(0.7)
    "While you waited for Emily, Stephanie was surprisingly a good host"
    "She asked you about yourself and provided refreshments"

    scene fs stephaniehouse
    with Dissolve(0.7)

    $ playerSprite = 0
    $ stephanieSprite = 1

    show fbplayer current:
        xalign 0.4 ypos 120
    show fbstephanie current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    stephanie "And yeah, my dad said I could have the place to myself as long as I keep up the grades."
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "Ah alright cool."
    $ playerSprite = 0
    $ emilySprite = 5
    show fbemily current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    emily "Okay...hah...I'm here."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Did you run here?"
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Emily! Heeeeey welcome."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "Shut it Stephanie! I know you're up to no good."
    emily "[povname] is she keeping you here against your will?"
    $ emilySprite = 4
    $ playerSprite = 1
    player "Well...I mean...maybe?"
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Did your white knight not tell you? In order for me to hand over those files he's doing me a favor."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "What? Are you serious??!"
    $ emilySprite = 4
    $ playerSprite = 1
    player "It's alright Emily I agreed to it in the end."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "And I'm cashing in that favor, with your help."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "What the heck is wrong with you Stephanie?!"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Hey I haven't even said what I wanted yet calm down."
    $ stephanieSprite = 0
    emily "..."
    $ stephanieSprite = 1
    stephanie "All you have to do Emily....is stay here."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "Huh?"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Just stay right here, while [povname] and I go into my room."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "I don't understand."
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Nothing to understand. You stay here for 15 minutes, we come back out, and it's done."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "That's really it?"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "That's it."
    $ stephanieSprite = 0
    $ emilySprite = 1
    emily "....Okay then."
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "C'mon mr White Knight."
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "Right..."
    $ playerSprite = 0
    scene fs stephaniealonescene1b
    with Dissolve(0.7)
    player "Alright spill."
    player "What's this all about? What's the prank here?"
    scene fs stephaniealonescene1a
    stephanie "Whatever do you mean? I simply wanted to show you my room!"
    scene fs stephaniealonescene1b
    player "Stephanie."
    scene fs stephaniealonescene1c
    stephanie "Hehe, there is no master plan. This is it!"
    stephanie "For fifteen minutes. Emily will have to wait while her precious [povname] is in a room alone with another girl."
    stephanie "And not just any girl, but ME."
    scene fs stephaniealonescene1b
    player "You know I'm dating Mia right?"
    scene fs stephaniealonescene1c
    stephanie "I've seen the way she looks at you [povname]. Girls can tell when other ones are in love."
    stephanie "This is KILLING her and I know it, meanwhile we're not even doing anything haha!"
    scene fs stephaniealonescene1b
    player "Hmmm. Okay I get it. So you're banking on Emily's overactive imagination and paranoia?"
    scene fs stephaniealonescene1c
    stephanie "Exactly. Pretty clever if I do say so myself."
    stephanie "Oh, one more thing haha."
    scene fs stephaniealonescene1b
    stephanie "*Ahem*"
    scene fs stephaniealonescene1a
    with hpunch
    stephanie "Ahn!"
    scene fs stephaniealonescene1b
    player "Huh? Why'd you moan...ah."
    player "You really are evil."
    stephanie "Hahaha."
    player "..."
    scene fs stephaniealonescene2a
    with Dissolve(0.7)
    player "Hmmm."
    stephanie "Huh?"
    player "You really are a lot cuter than I thought you were at first."
    scene fs stephaniealonescene2b
    with Dissolve(0.5)
    stephanie "Oh uh...um.."
    emily "G-Guys?"
    emily "Its been 15 minutes!"
    player "...."

    scene fs stephaniehouse
    with Dissolve(0.7)

    $ stephanieSprite = 1
    $ emilySprite = 4
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbstephanie current:
        xalign 0.6 ypos 120
    show fbemily current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    stephanie "Okay Emily, you can have him back now."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "W-What did you guys do??"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Oh nothing much, just hang around."
    stephanie "I am looking forward to the next two visits though."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "What?!"
    $ emilySprite = 4
    player "?"
    $ emilySprite = 5
    emily "What do you mean next two?"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Oh we didn't tell you? This was a three event favor. Isn't that right [povname]?"
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "....right yeah."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Hehe."
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "So...this whole thing.."
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Two more times."
    stephanie "Now if you don't mind I'm going to get NAKED and have a hot shower to...CLEAN off."
    $ stephanieSprite = 0
    emily "...."
    $ emilySprite = 5
    emily "Why'd you say the 'get naked' part?"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "And I would appreciate it if you two left my house."
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "Alright we'll get outta your hair."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Great. Same time tomorrow?"
    stephanie "Byyyye Emily."
    $ stephanieSprite = 0
    scene fs blackblank
    with Dissolve(0.5)
    "You and Emily walk in silence back to the school"
    scene fs schoolhallway
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ emilySprite = 5
    emily "Okay what happened??"
    emily "What did you two do behind that door?!"
    $ emilySprite = 4
    $ playerSprite = 1
    player "Emily calm down."
    player "We literally just talked."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "But...but I heard her..."
    emily "{size=25}Moan.{/size}"
    $ emilySprite = 4
    $ playerSprite = 1
    player "I know, she did that on purpose because she knew it'd drive you crazy."
    $ emilySprite = 5
    $ playerSprite = 0
    emily "R-Really?"
    $ emilySprite = 4
    $ playerSprite = 1
    player "Yeah, it's all just a big prank to mess with you. You're your own worst enemy sometimes."
    $ emilySprite = 5
    $ playerSprite = 0
    emily "Oh..well...okay then."
    emily "If it's just...that's fine then."
    $ emilySprite = 4
    $ playerSprite = 1
    player "It's cute seeing you so jealous like this."
    $ emilySprite = 5
    $ playerSprite = 0
    emily "[povname]!"
    $ emilySprite = 4
    $ playerSprite = 1
    player "C'mon, just two more visits then we're done."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Alright..."
    $ emilySprite = 4
    $ stephaniequestlog = "Visit the apartment building in Sunnyside on a later day during Morning or Day and buzz Stephanie."
    $ stephaniescene1 = 1
    $ stephaniedaychecker = dayNumber
    jump gotosunnyside


label stephaniescene1part2:
    hide screen uppergui
    stop music fadeout 5
    stop sound fadeout 5
    "You call Emily over again to Stephanie's apartement"
    "Bzzzzz"
    stephanie "Hey guyyyyss."
    emily "Just let us through."
    stephanie "Hehe."
    scene fs stephaniehouse
    with Dissolve(0.7)
    pause
    $ emilySprite = 5
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.5 ypos 120
    show fbstephanie current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    emily "Okay just..don't take so long in there..."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Course Em."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Hehe. 'Course Em'."
    $ stephanieSprite = 0
    $ emilySprite = 5
    show fbemily current:
        xzoom -1.0
    emily "I hate you."
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Hahaha."
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "You can't let her get to you."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "C'mon handsome."
    $ stephanieSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    scene fs stephaniealonescene1c
    with Dissolve(0.5)
    stephanie "Haha God this is so much fun!"
    stephanie "Should I 'moan' louder this time?"
    scene fs stephaniealonescene2a
    stephanie "H-Huh?"
    player "What if it wasn't fake this time?"
    scene fs stephaniealonescene2b
    stephanie "{i}What is he?{/i}"
    player "It'd give a better result wouldn't it?"
    scene fs stephaniealonescene3
    with Dissolve(0.7)
    stephanie "Oh!"
    stephanie "Oh my God.."
    scene fs stephaniealonescene4
    stephanie "{i}I just wanted to mess with him and Emily..{/i}"
    stephanie "Mmmmm."
    stephanie "I wasn't expecting he'd actually..."
    scene fs stephaniealonescene5
    stephanie "!!"
    player "You have a pretty great body Stephanie. I can see why you're the Queen Bee of the school."
    scene fs stephaniealonescene6
    stephanie "Ahn..."
    stephanie "Oh fuck!"
    emily "Guys?"
    player "Haha you're so wet, you really love fucking with Emily huh?"
    stephanie "{i}Holy Shit Emily's boyfri-{/i}"
    stephanie "{i}Or Mia's boyfriend, I don't care, has his fingers up my pussy! while she's outside!!{/i}"
    stephanie "OhmygodImgonnacum!"
    emily "What?"
    scene fs stephaniealonescene7
    with vpunch
    stephanie "AHHH!!"
    stephanie "YES THAT'S IT!"
    scene fs blackblank
    with Dissolve(0.7)
    pause

    scene fs stephaniehouse
    with Dissolve(0.7)
    $ emilySprite = 5
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.5 ypos 120

    emily "Where's?"
    $ emilySprite = 4
    $ playerSprite = 1
    player "Stephanie is...indisposed. She said we can just leave."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "And you guys just..."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Just talked."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "And all that noise was..."
    $ emilySprite = 4
    $ playerSprite = 1
    player "All fake again don't worry."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "O-Okay..."
    $ stephaniequestlog = "Visit the apartment building in Sunnyside on another day during Morning or Day and buzz Stephanie."

    $ stephaniedaychecker = dayNumber
    $ stephaniescene1 = 2
    jump overworldmap


label stephaniescene1part3:
    hide screen uppergui
    stop music fadeout 5
    stop sound fadeout 5
    emily "Okay this is the last one right?"
    player "Oh yeah, this is the big one."
    emily "What?"
    player "Nothing, let's go in."

    scene fs stephaniehouse
    with Dissolve(0.7)
    pause
    $ emilySprite = 4
    $ stephanieSprite = 1
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.5 ypos 120
    show fbstephanie current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    stephanie "Hey!"
    $ stephanieSprite = 0
    $ emilySprite = 5
    emily "So we're done afte-"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Yup yup okay let's go [povname]."
    $ stephanieSprite = 0
    show fbplayer current:
        xalign -0.5 ypos 120
    show fbstephanie current:
        xalign -0.5 ypos 120
    with move
    emily "..."
    scene fs stephaniealonescene4
    with Dissolve(0.7)
    player "Someone's eager."
    stephanie "Don't..ah..don't act like you aren't."
    player "Turn around."
    scene fs stephaniealonescene11
    with Dissolve(0.7)
    stephanie "Hehehe!"
    stephanie "[povname]..."
    scene fs stephaniealonescene13
    with Dissolve(0.5)
    stephanie "Oh God [povname]!"
    stephanie "Mmmmnn!"
    scene fs stephaniealonescene14
    with Dissolve(0.7)
    emily "{i}I-It's alright, they're just pretending!{/i}"
    show stephaniefuck movie1
    stephanie "Ahn ahn ahn!"
    stephanie "God how are you so big?!"
    player "Fuck stephanie!"
    pause
    scene fs stephaniealonescene14
    stephanie "AHHH FUCK YES YES!"
    stephanie "Harder!"
    emily "{i}It's not real Emily!{/i}"
    scene fs stephaniealonescene15
    with Dissolve(0.5)
    stephanie "HARDER! POUND MY FUCKING PUSSY!"
    emily "{i}It's not real it's not real it's not real!{/i}"
    show stephaniefuck movie2
    stephanie "[povname]!!!"
    player "You want this cum you slut??"
    stephanie "Fill my fucking womb!"
    player "What's that?!"
    stephanie "PLEASE!! I NEED IT!"
    pause
    scene fs blackblank
    player "AHH FUCK."
    stephanie "YESYESYES!"
    stephanie "He came inside me Emily!"
    stephanie "Your white knight just got me pregnant!"
    pause
    "You leave Stephanie to rest in her room and assure Emily again that nothing happened"
    "Though she was acting very strange when you spoke to her"
    "...."
    stephanie "{cps=25}What's up sluts?{/cps}"
    raven "{cps=25}Uh oh she called us sluts.{/cps}"
    melissa "{cps=25}She only does that when something JUICY happens lol{/cps}"
    show stephanieselfie postcreampie at fit_vertical:
        xalign 0.5 ypos 0

    with Dissolve(0.7)
    $ renpy.notify("Got Stephanie's Picture!")
    $ phone_pictures.append("bullies selfies steph color")
    pause
    stephanie "{cps=25}Guess who just got creampied by Emily's crush?{/cps}"
    raven "{cps=25}Haha no way!{/cps}"
    melissa "{cps=25}OMGEE.{/cps}"
    melissa "{cps=25}And you call US sluts? LOL!{/cps}"
    stephanie "{cps=25}Best part is we fucked in my room while Emily was right outside.{/cps}"
    stephanie "{cps=25}It's what I asked for my favor. Can't believe he actually went for it.{/cps}"
    raven "{cps=25}That's so fucking hot.{/cps}"
    stephanie "{cps=25}Anyways I gotta get cleaned up talk to you bitches later.{/cps}"
    melissa "{cps=25}Later!{/cps}"
    raven "{cps=25}See yah.{/cps}"
    $ stephaniescene1 = 3
    $ stephaniescene2 = 1
    $ stephaniequestlog = "No more solo content for Stephanie in this version."

    jump passtime
