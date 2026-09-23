# chapter 1
# interaction 1
# part 1

label sophiaphase1interaction1part1:
    hide screen sophia_atschool
    hide screen mia_atschool
    scene fs classroomZOOM
    with Dissolve(0.7)

    $ playerSprite = 1
    $ sophiaSprite = 3

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbsophia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    player "Hey Soph. What's up?"
    $ sophiaSprite = 4
    $ playerSprite = 0
    sophia "Nothing, just waiting for class to start. You should probably go soon."
    $ sophiaSprite = 3
    $ playerSprite = 1
    player "Are you mad at me?"
    $ playerSprite = 0
    $ sophiaSprite = 4
    sophia "No. I'm not mad. Please leave."
    $ sophiaSprite = 3
    $ playerSprite = 1
    player "You say you're not mad but I'm picking up some serious mad vibes from you..."
    $ playerSprite = 0
    $ sophiaSprite = 4
    play sound "audio/sophiagameaudio/sophiagoaway.wav"
    sophia "Grrrr go away [povname]!"
    $ sophiaSprite = 3
    $ playerSprite = 6
    player "Okay okay sorry, I'm going."
    hide fbsophia current
    with Dissolve(0.5)
    $ playerSprite = 7
    player "{i}She's not usually like this, it's been a while since she's been mad at me.{/i}"
    player "{i}But I didn't even do anything!{/i}"
    $ playerSprite = 0
    player "{i}Whatever, I'll visit her in the afternoon and maybe she'll have calmed down. Good thing she lives right beside me.{/i}"
    $ sophiaphase1interaction1 = 1

    if renpy.android:
        $ sophiaquestlog = "{size=-25}Sophia's mad at me for some reason. I should talk to her again at her place.{/size}"
    else:
        $ sophiaquestlog = "Sophia's mad at me for some reason. I should talk to her again at her place."
    hide fbplayer
    hide fbsophia
    hide fs classroomZOOM
    jump classroom1

# part 1 post convo

label sophianottalkingtome:
    hide screen sophia_atschool
    player "Sophia kinda seems in a bad mood, plus her class is probably starting soon."
    player "I'll stop by her house in the afternoon, talk to her then."
    jump classroom1

# part 2

label sophiaphase1interaction1part2:
    scene fs sophiahouseoutside
    with Dissolve(0.7)

    $ playerSprite = 0

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    player "{i}Okay she should be home by now. Let's ring the doorbell here...{/i}"
    "*Ding Dong*"

    sophia "Yesss helloo?"
    $ playerSprite = 1
    player "Hey neighbour."
    $ playerSprite = 0
    sophia "Oh.."
    sophia "Hi."
    $ playerSprite = 1
    player "Can I come in?"
    $ playerSprite = 0
    "Sophia comes outside and shuts the door."

    $ sophiaSprite = 4
    show fbsophia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)


    play sound "audio/sophiagameaudio/sophiahmph.wav"
    sophia "We can talk outside."
    $ sophiaSprite = 3
    $ playerSprite = 1
    player "Oh uh yeah sure."
    $ playerSprite = 0
    player "...."
    $ playerSprite = 1
    player "So..."
    $ playerSprite = 0
    $ sophiaSprite = 4
    sophia "Why didn't you tell me you were dating Mia?"
    $ sophiaSprite = 3
    $ playerSprite = 5
    player "What?"
    $ playerSprite = 4
    $ sophiaSprite = 4
    sophia "I haven't talked to you in forever, I'm all excited to see you again and then I find out you're dating one of my best friends!"
    $ sophiaSprite = 2
    $ playerSprite = 5
    player "Soph I told you, I thought Mia would've said something about it to you."
    $ playerSprite = 1
    player "And also why is that a bad thing? It doesn't make a difference if you knew we were dating a month ago instead of now."
    $ playerSprite = 4
    $ sophiaSprite = 4
    sophia "It makes a big difference!"
    $ sophiaSprite = 2
    sophia "I would've..."
    sophia "{i}I never would've invited you to that party and introduced you...{/i}"
    $ sophiaSprite = 3
    player "?"
    $ sophiaSprite = 4
    sophia "Nothing nevermind."
    $ sophiaSprite = 3
    $ playerSprite = 1
    player "Okay clearly you're upset, I should've said something to you about dating Mia."
    player "So, what can I do to make you forgive me?"
    $ playerSprite = 0
    sophia "....."
    $ playerSprite = 1
    player "Squishy hug? Huh?"
    $ playerSprite = 0
    $ sophiaSprite = 0
    with Dissolve(0.5)
    sophia "...."
    $ playerSprite = 1
    player "You want a squishy hug? C'mooon I know you want one."
    $ playerSprite = 0
    $ sophiaSprite = 2
    sophia "[povname] we did that when we were kids I don-"
    $ playerSprite = 2
    player "Hmmm maybe I'll call up Mia see if she's free-"
    $ sophiaSprite = 5
    hide fbplayer current
    $ playerSprite = 1
    hide fbsophia current
    show fbsophia hug:
        xalign 0.3 ypos 120
    with Dissolve(0.7)
    play sound "audio/sophiagameaudio/sophiashortlaugh.wav"
    sophia "Okay okay haha here!"
    #sophia and MC hug
    player "Mmmmm better?"
    sophia "Better."
    $ sophiaSprite = 0
    show fbsophia current:
        xalign 0.5
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 1
    player "Not mad?"
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Not mad..."
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "I'll visit you at your school again okay?"
    $ sophiaSprite = 1
    sophia "Okay."
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "We'll do something when I'm there, something fun. See yah!"
    $ playerSprite = 0
    hide fbplayer current
    with Dissolve(0.5)
    $ sophiaSprite = 2
    sophia "...."
    play sound "audio/sophiagameaudio/sophiaimnotmad.wav"
    sophia "I'm not mad."

    $ sophiaquestlog = "Seems like Sophia's back to normal. I should visit her in class again!"
    $ sophiaphase1interaction1 = 2
    hide fbsophia
    hide fbplayer
    hide fs sophiahouseoutside
    jump passtime

# part 3

label sophiaphase1interaction1part3:
    hide screen sophia_atschool
    hide screen uppergui
    scene fs classroomZOOM
    with Dissolve(0.7)

    $ playerSprite = 0

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    player "{i}Hmm I don't see the girls here ye-{/i}"

    $ sophiaSprite = 1

    show fbsophia current:
        xalign 0.6 ypos 120

    sophia "Hey!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    show fbplayer current at surpriseshake:
        xalign 0.35 ypos 120
    player "Ah! Shit Soph you scared me."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "I'm skipping! Come with me quick!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Wait what?"
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Let's go let's go before the professor sees me!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Okay geez."
    scene fs blackblank
    with Dissolve(1.0)
    "Sophia takes you by the hand and leads you out of the building and eventually off the campus grounds"
    player "Soooph, where we going?"
    $ sophiaSprite = 1
    sophia "You wanted to do something fun with me right?"
    player "Yeah..."
    $ sophiaSprite = 1
    play sound "audio/sophiagameaudio/sophiashortlaugh.wav"
    sophia "So relax and just go with the flow!"
    player "Alright you crazy lady."
    scene fs park
    with Dissolve(1.0)
    "After some time, she leads you to the park"
    "And eventually you're walking on the big pathway"
    $ sophiaSprite = 1
    sophia "Here let's sit on that bench!"
    player "Sure thing."
    scene fs sophiamcbench
    with Dissolve(0.7)
    window hide
    "The two of you then sit down on the bench, it's surprisingly comfortable"
    "You spread your arms and take in the sun's warm rays"
    "You always knew your childhood friend was cute, but today you felt she was....a little bit extra cute"
    window hide
    pause
    scene fs sophiamcbenchtalkmc
    player "View is nice gotta admit."
    scene fs sophiamcbench
    sophia "....."
    scene fs sophiamcbenchtalksophia
    sophia "Okay it's probably not the funnest thing to do but maybe we can just hang for a bit?"
    sophia "Like we used to?"
    scene fs sophiamcbenchtalkmc
    player "Haha sure, I actually don't care what we do if you're happy about it, so no worries."
    scene fs sophiamcbench
    sophia "...."
    scene fs sophiamcbenchtalkmc
    player "Trees are starting to change color, fall must be starting soon I guess."
    #bench scene
    player "So any particular reason you wanted to skip today?"
    scene fs sophiamcbenchtalksophia
    sophia "Yeah."
    scene fs sophiamcbench
    player "...."
    scene fs sophiamcbenchtalkmc
    player "You gonna tell me?"
    scene fs sophiamcbenchcuddle
    with Dissolve(0.5)
    sophia "Can I get closer?"
    player "{i}You kinda already did.{/i}"
    scene fs sophiamcbenchcuddletalksophia
    with Dissolve(0.5)
    sophia "I'm....cold, the breeze is a bit much for me in this skirt."
    scene fs sophiamcbenchcuddletalkmc
    player "Oh uh, sure thing."
    scene fs sophiamcbenchcuddlehold
    sophia "Mmmm..."
    player "{i}I don't understand, she was so mad at me recently and now she's being extra close.{/i}"
    player "{i}Women...{/i}"
    #play sound "audio/sophiagameaudio/sophiacutelaugh.wav"
    sophia "{i}[povname]'s so warm...I bet we look like a couple teehee.{/i}"
    #sophia rubs him arm gently
    scene fs sophiamcbenchcuddletalkmc
    player "Did you want to get back soon?"
    scene fs sophiamcbenchcuddletalksophia
    sophia "Just a little bit longer..."
    sophia "Your hands are so warm and big."
    scene fs sophiamcbenchcuddletalkmc
    player "Yeah I guess they kinda are."
    scene fs sophiamcbenchcuddletalksophia
    sophia "I know what they say about boys with big hands."
    scene fs sophiamcbenchcuddletalkmc
    player "Wait what?"
    scene fs sophiamcbenchcuddletalksophia
    #play sound "audio/sophiagameaudio/sophialonglaugh.wav"
    sophia "Big feet! Hahaha!"
    scene fs sophiamcbenchcuddletalkmc
    player "Ugh."
    scene fs sophiamcbenchcuddletalksophia
    sophia "Don't worry Mia already told me how impressive you are!"
    scene fs sophiamcbenchcuddletalkmc
    player "Dammit I talked with her about carelessly saying things to you guys."
    scene fs sophiamcbenchcuddletalksophia
    sophia "Gotta say I was surprised when she told me, I remember when we were little and you let me see it..."
    scene fs sophiamcbenchcuddletalkmc
    player "Jesus Soph don't bring that up we were kids."
    player"I've grown and you've grown, so let's not bring up embarassing shit I did when I was little."
    player "We'd be here all day."
    scene fs sophiamcbenchcuddletalksophia
    sophia "You think I've grown?"
    scene fs sophiamcbenchcuddletalkmc
    player "....Yeah?"
    scene fs sophiamcbenchcuddletalksophia
    sophia "What do you mean?"
    scene fs sophiamcbenchcuddletalkmc
    player "Hey don't think I don't know where you're going with this!"
    player "If I say you got much cuter will you go back to class and I can leave this conversation?"
    scene fs sophiamcbenchcuddletalksophia
    sophia "Hahaha okay let's go then."
    scene fs blackblank
    with Dissolve(1.0)
    sophia "{i}Much cuter! He think's I'm cute I knew it!{/i}"
    sophia "{i}More than Mia right? He definitely thinks I'm cuter than Mia...{/i}"
    $ sophiaphase1interaction1 = 3
    $ sophiaquestlog = "It was a nice little moment in the park. I should get some sleep though."
    hide fs blackblank
    hide fbplayer
    hide fbsophia
    jump passtime

# part 4 (starts after part 3 when going to sleep)

label sophiaphase1interaction1part4:
    hide screen uppergui
    hide screen backbuttonROOM
    scene fs blackblank
    with Dissolve(1.0)


    play sound "audio/sophiagameaudio/sophiacutelaugh.wav"
    sophia "Hehehe."
    sophia "Who still leaves their extra key beneath the welcome mat?"
    scene fs sophiamorningwood1
    with Dissolve(0.7)
    sophia "{i}Since we're getting along again I thought I'd wake you up like I used to when we were kids.{/i}"
    scene fs sophiamorningwood2
    sophia "{i}Hehe, I remember you'd never get up in time for school so your parents told me to help!{/i}"
    scene fs sophiamorningwood1
    sophia "You look so cute when you're asleep..."
    sophia "I could watch you sleep all day...I'd love to snuggle.."
    scene fs sophiamorningwood2
    sophia "Hehe Nope! It's time to wake up!"
    sophia "And everyone knows the best way to get someone up..."
    scene fs sophiamorningwood3
    sophia "Is to pull..."
    scene fs sophiamorningwood4
    play sound "audio/sophiagameaudio/sophiaguh.wav"
    sophia "The sheets off-GUH!"
    window hide
    pause
    sophia "....."
    sophia "Ah...ah..th...that's yo....a.."
    sophia "{i}Penis!{/i}"
    sophia "{i}That thing's massive!{/i}"
    sophia "{i}Since when does [povname] sleep naked??!!{/i}"
    sophia "{i}Mia really wasn't kidding! H-How did she put....how did she take something like that??!{/i}"
    sophia "{i}My god....I can't look away..{/i}"
    sophia "{i}I-Is this what they call morning wood?{/i}"
    window hide
    pause
    player "Hmmmm mmm..."
    sophia "{i}Shit h-he's waking up I need to get out of here!{/i}"
    scene fs blackblank
    with Dissolve(0.7)
    player "Huh? How did the blankets fall off?"
    player "Meh."

    $ sophiaquestlog = "I wonder what Sophia's up to now?"
    $ sophiaphase1interaction1 = 4
    hide fs blackblank
    jump gotosleep

# interaction 2
# part 1

label sophiaphase1interaction2part1:
    scene fs classroom
    with Dissolve(0.7)
    hide screen mia_atschool

    $ playerSprite = 1
    $ sophiaSprite = 0

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbsophia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    player "Hey Soph, I just wanted to stop by quickly to say hi to you and Mia before classes start."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Hey!! You came to see me? Not just Mia?"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Um...yeah?"
    $ playerSprite = 0
    $ sophiaSprite = 1
    show fbsophia current at surpriseshake
    #play sound "audio/sophiagameaudio/sophiashortlaugh.wav"
    sophia "Teehee yaayy."
    sophia "Oh oh!! I almost forgot! My mom started making beef stromboli last night and it should be ready by the end of the day!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Oh sweet."
    $ sophiaSprite = 1
    $ playerSprite = 0
    sophia "She's not home tonight so you should come over and help me eat it!"
    $ sophiaSprite = 0
    $ playerSprite = 7
    player "Well..."
    $ sophiaSprite = 1
    $ playerSprite = 0
    sophia "Pleeeease! I can't eat all that yummy food by my wittle self!"
    $ sophiaSprite = 0
    $ playerSprite = 7
    player "*sigh* Well I do love your mom's stramboli."
    $ playerSprite = 5
    player "Just no more baby voice you know I hate that."
    $ sophiaSprite = 1
    $ playerSprite = 4
    #play sound "audio/sophiagameaudio/sophiadiis.wav"
    sophia "Whaaat diiiis??"
    $ sophiaSprite = 0
    $ playerSprite = 5
    player "UGH."
    $ sophiaSprite = 1
    $ playerSprite = 0
    #play sound "audio/sophiagameaudio/sophiashortlaugh.wav"
    sophia "Hahaha come over tonight! It's gonna be super fun."
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Sure I'll meet you at your place this afternoon."
    $ sophiaSprite = 1
    $ playerSprite = 0
    sophia "Great!"
    hide fbplayer current
    with Dissolve(0.7)
    sophia "{i}YES! Haha [povname] is commiiiiing oooover!{/i}"
    sophia "{i}God I just can't get the image of his huge COCK out of my mind!{/i}"
    sophia "{i}Hehe Sophia you're so naughty!{/i}"
    $ sophiaphase1interaction2 = 1
    $ sophiaquestlog = "Sophia wants me to visit for lunch at her place."
    jump returnwhereyouare

# part 1 post convo

    label cantwaitforvisitsophia:
    scene fs classroom
    with Dissolve(0.7)
    hide screen sophia_atschool
    hide screen mia_atschool

    $ playerSprite = 0
    $ sophiaSprite = 1

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbsophia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ sophiaSprite = 1
    sophia "Can't wait for your visit!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "When did you want me to come over again?"
    $ sophiaSprite = 1
    $ playerSprite = 0
    sophia "Afternoon silly! At my place."
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Alright."
    $ sophiaSprite = 1
    $ playerSprite = 0
    sophia "Hehe."
    jump returnwhereyouare

# part 2

label sophiaphase1interaction2part2:
    hide screen uppergui
    scene fs overworldnight
    stop music 
    with Dissolve(0.7)
    play music "audio/rainstorm.wav" fadein 10
    show foreground rain
    with Dissolve(0.5)
    pause
    $ playerSprite = 5
    scene fs sophiahouseoutsidenight
    show foreground rain

    show fbplayer current behind foreground:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    
    player "Oh man it's really starting to come down."

    show fbsophia current behind foreground:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Hey Soph."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "[povname]! You made it!"
    sophia "Great timing the rain is really coming down."
    $ playerSprite = 1
    player "Yeah it started up on my way over."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Hehe...I'm so glad you're here. I wa-"
    "VRRRRR VRRRRR"
    $ playerSprite = 1
    player "Oh wait sorry my phone's vibrating one sec."
    $ playerSprite = 2
    $ sophiaSprite = 2
    player "Hello? Oh hey Babe!"
    $ sophiaSprite = 1
    sophia "Y-You should come inside so you don't get your phone wet."
    $ sophiaSprite = 2
    player "Right now? Really?!"
    player "Fuck yeah of course! I'm coming over right now!"
    sophia "What?"
    $ playerSprite = 1
    player "Hey Soph sorry but I gotta go."
    $ sophiaSprite = 4
    $ playerSprite = 0
    sophia "But we made plans!"
    $ sophiaSprite = 3
    $ playerSprite = 1
    player "I know but that was a booty call."
    $ playerSprite = 0
    $ sophiaSprite = 2
    sophia "A...a..."
    $ playerSprite = 1
    player "Yeah Mia's really feeling it tonight for some reason haha."
    player "Doesn't happen often so I'm gonna have to take a rain check alright?"
    $ playerSprite = 0
    sophia "......"
    $ playerSprite = 1
    player "Hah. RAIN check."
    player "Anyways see yah!"
    $ playerSprite = 0
    hide fbplayer current
    with Dissolve(0.5)
    sophia "{size=-10}A...booty call..{/size}"

    stop music fadeout 5
    scene fs livingroomnight
    with Dissolve(0.7)

    $ playerSprite = 1
    $ miaSprite = 0
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbmia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)


    player "Hey sorry I ran over as soon as I can."
    $ miaSprite = 1
    mia "Alright let's go to your room."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Wow you really are in the mood."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "I watched a rom-com with Katie. It was so romantic and sweet..."
    mia "And well I kind of just need to get fucked now."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Thank god for romance movies."
    $ hiden_textbox = True
    scene fs blackblank
    with Dissolve(0.8)
    "A few minutes of stripping and giggling later.."
    play music "audio/rainstorm.wav" fadein 10
    scene fs sophiasexwatch1
    with Dissolve(1.0)
    window hide
    pause
    scene fs sophiasexwatch1mc
    player"You're so hot."
    scene fs sophiasexwatch1mia
    mia "Hehe I can't believe you've gone so long without glaring at my breasts."
    scene fs sophiasexwatch1mc
    player"Oh don't worry I'll be giving them plenty of attention real soon."
    scene fs sophiasexwatch1mia
    mia "[povname]."
    mia "I want you to ravage me."
    scene fs sophiasexwatch1mc
    player"Thought you'd never ask."
    scene fs sophiasexwatch2
    with Dissolve(0.4)
    mia "Oh! Oh my hehe."
    scene fs sophiasexwatch3
    with Dissolve(0.4)
    mia "Mmmm yeah..."
    player"Mmmmm."
    mia "O-Oh yeah just like...just like THAT!!"
    show sophiawatchsex1
    mia "Ahn."
    mia "AHN!"
    scene fs miasexthunder
    pause 0.1
    scene fs miasexthunder2
    pause 0.1
    show sophiawatchsex1
    mia "Oh [povname] take me!"
    mia "Yes!"
    scene fs miasexthunder
    pause 0.1
    show sophiawatchsex1
    mia "Harder! Fuck me harder!"
    mia "AHHHH!"
    player"{i}I don't know if it's the thunder but she is so primal tonight, god this is so hot!{/i}"
    player"Fuck Mia you're so wet!"
    scene fs miasexthunder
    pause 0.1
    scene fs miasexthunder2
    pause 0.1
    show sophiawatchsex2
    play sound "audio/lightningstrike.wav"
    mia "Oh Oh god you're so BIG!"
    sophia "......"
    player"That's it take my cock balls deep!"
    mia "You like watching my big t-tits bounce don't you?"
    player"{i}Hehe she's trying to talk dirty.{/i}"
    player"Yeah that's right I fucking love them."
    player"Can you even call yourself a woman if you don't have tits like these?"
    mia "O-Oh God! C-Careful they're sensitiv-OH MY GOD!"
    mia "Ahn! You're making me cum already!!!"
    player"Cum all over my cock baby!"
    mia "G-GOD YYYYESS!!! I love it! I LOVE THIS COCK!"
    sophia "....."
    mia "AHNNN!!!"
    player"You ready baby?!!"
    mia "Yes yes fill me up! Fill up my womb!"
    scene fs sophiasexwatch4
    with vpunch
    play sound "audio/sophiagameaudio/miamoanwhilesophiawatch.wav"
    mia "AHHHNNN!"
    player"FUCK YES!"
    mia "There it is there it is there it is!"
    mia " It's so warm!"
    mia "Yesss god yessss I'm cumminnnngg...."
    player"{i}This is crazy and I'm loving it!{/i}"
    sophia "*sniff*"
    mia "Hah..hah..I...hah.."
    player"No need to say anything babe catch your breath."
    mia "...Again.."
    player"Huh?"
    mia "Again! From behind."
    player"Yes ma'am."
    scene fs blackblank
    with Dissolve(1.0)
    "A little while later..."
    scene fs overworldnight
    with Dissolve(0.7)
    show foreground rain
    with Dissolve(0.5)
    pause
    $ sophiaSprite = 6
    show fbsophia current behind foreground:
        xalign 0.5 ypos 120
    with Dissolve(0.5)

    sophia "What am I doing?"
    sophia "I'm pathetic....and soaked."
    sophia "I gotta go home and dry off."
    stop music fadeout 10
    scene fs blackblank
    with Dissolve(1.0)
    pause
    scene fs sophiamasterbate1
    with Dissolve(1.0)
    window hide
    pause
    sophia "{i}Sigh...{/i}"
    sophia "{i}Why aren't you in your Pajamas Sophia?{/i}"
    sophia "...."
    sophia "{i}You know why...you stupid dirty little...little slut.{/i}"
    sophia "{i}How could you watch them?? H-How could you just stand there like some stalker and watch [povname]...{/i}"
    scene fs sophiamasterbate2
    with Dissolve(0.5)
    sophia "{i}W-Watch [povname] pound Mia raw..{/i}"
    image sophiatouchherself1:
        "sophia in bed2.png"
        0.5
        "sophia in bed2b.png"
        0.5
        repeat
    show sophiatouchherself1
    window hide
    pause
    sophia "It looked like Mia felt so good."
    sophia "She has such a cute pussy."
    image sophiatouchherself2:
        "sophia in bed10.png"
        0.4
        "sophia in bed10b.png"
        0.4
        repeat
    show sophiatouchherself2
    with Dissolve(0.8)

    sophia "A-And [povname] was stretching it so much w-with his m-massive thick cock...hah.."
    sophia "He was fucking her so good!"
    image sophiatouchherself3:
        "sophia in bed10.png"
        0.25
        "sophia in bed10b.png"
        0.25
        repeat
    show sophiatouchherself3
    sophia "It should be me! He should be on top of ME!"
    sophia "Holding me d-down an-AHN!"
    sophia "A-And fucking my tight little pussy! Harder and Hard- oHHH!"
    sophia "AHN! God [povname]!"

    scene fs sophiamasterbate5
    play sound "audio/sophiagameaudio/sophiacum1.wav"
    with vpunch
    sophia "AHHH!!"
    sophia "CUM INSIDE ME [povname]!!"
    scene fs blackblank
    with Dissolve(2.0)
    image sophiatouchherself4:
        "sophia in bed12.png"
        0.6
        "sophia in bed12b.png"
        0.6
        repeat
    show sophiatouchherself4
    with Dissolve(1.5)

    play sound "audio/sophiagameaudio/sophiasniffcry.wav"
    sophia "*Sniff*"
    sophia "[povname]....[povname]..."
    sophia "It should be me."
    window hide
    pause
    $ sophiaphase1interaction2 = 2
    if currentchapter >= 2:
        $ sophiaquestlog = "I feel bad about skipping out on lunch, I should see her again."
    else:
        $ sophiaquestlog = "I should focus on other things for now.."


    #$ hiden_textbox = False
    jump passtime

# end chapter 1