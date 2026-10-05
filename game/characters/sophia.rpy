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
    hide screen mia_atschool
    hide screen mia_sophia_atschool
    hide screen sophia_atschool
    player "Sophia kinda seems in a bad mood, plus her class is probably starting soon."
    player "I'll stop by her house in the afternoon, talk to her then."
    jump classroom1

# part 2

label sophiaphase1interaction1part2:
    if timeofday != "Day":
        player "I should visit Sophia this afternoon."
        jump overworldmap

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
    if timeofday != "Day":
        player "I should visit Sophia this afternoon."
        jump overworldmap

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

# chapter 2
# start

label gohomesophia:
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.3 ypos 120
    charlotte "Yes me too. The heat was unBAREable today."
    charlotte "Maybe I'll take a bath.."
    $ charlotteSprite = 0
    $ emilySprite = 1
    emily "Looks like we're splitting up here then?"
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
    with Dissolve(0.5)
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 1
    mia "Bye everyone!"
    $ miaSprite = 0
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.1 ypos 120
    with move
    player "See you later Mia."
    $ playerSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    $ emilySprite = 1
    emily "Bye [povname], bye Olivia and Sophia!"
    $ emilySprite = 0
    $ oliviaSprite = 1
    olivia "Bye Emily."
    $ oliviaSprite = 0
    hide fbemily current
    with Dissolve(0.5)
    $ playerSprite = 1
    player "You want to go back with us Olivia?"
    $ playerSprite = 0
    $ oliviaSprite = 1
    olivia "Sure I don't really any anything to do ton-"
    $ oliviaSprite = 9
    show fbolivia current at surpriseshake:
        xalign 0.8 ypos 120
    olivia "Ohmygod!"
    olivia "The new KeroKero Fight game I ordered comes in today!!"
    olivia "I totally forgot."
    olivia "I gotta go bye!"
    hide fbolivia current
    with Dissolve(0.5)
    $ playerSprite = 10
    sophia "Uhhh...bye Olivia?"
    $ playerSprite = 0
    show fbsophia current:
        xalign 0.5 ypos 120
    $ sophiaSprite = 1
    sophia "Oh geez there she goes again.."
    $ sophiaSprite = 0
    show fbplayer current:
        xalign 0.2 ypos 120
    with move
    $ playerSprite = 1
    player "Haha damn she can run! Probably should've participated in one of the events."
    $ sophiaSprite = 1
    $ playerSprite = 0
    sophia "Hahaha yeah, we'd just have to put a new graphics card at the finish line."
    $ sophiaSprite = 0
    $ playerSprite = 11
    player "Wow that is...actually a pretty good joke."
    $ sophiaSprite = 4
    $ playerSprite = 0
    sophia "What, you don't think I got jokes??"
    $ sophiaSprite = 3
    $ playerSprite = 6
    player "Easy there sheriff I surrender."
    sophia "...."
    player "...."
    $ playerSprite = 13
    $ sophiaSprite = 1
    "Both Of You" "Hahaha!"
    $ playerSprite = 1
    $ sophiaSprite = 0
    player "C'mon Soph. Lemme drive you home."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Thanks [povname], I'd appreciate that."
    $ sophiaSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    "So you drive yourself and Sophia back home"
    "You talk about the events you watched that day, how things were going with Mia"
    "And you even mentioned how happy you were that you and Sophia were getting along again, she seemed to really respond to that"
    "You didn't say it out loud but you enjoyed being close to her again"
    "Anyways eventually you dropped her at home, then took off all your clothes and passed out in your bed"
    "You must've been a lot more tired than you thought"
    "You had strange erotic dreams throughout the night, sweaty bodies and breasts went in and out of your conciousness..."
    "Eventually morning came..."
    "*Slurp* *Slurp*"
    player "Huh?"
    scene fs sophiachapterend0
    with Dissolve(1.0)
    player "What's going on? Why do I feel something..."
    scene fs sophiachapterend0b
    with Dissolve(1.0)
    player "W-What? Mia?"
    scene fs sophiachapterend1blur
    with Dissolve(0.7)
    $ hiden_textbox = True
    player "When did you get here?..."
    mia "...."
    scene fs sophiachapterend2
    with Dissolve(0.7)
    player "Ohhhh that...mmmm that feels good.."
    scene fs sophiachapterend3
    player "Yeah baby...lick the head just like that."
    scene fs sophiachapterend2
    player "Oh fuck..."
    scene fs sophiachapterend3
    player "Wait.."
    scene fs sophiachapterend2
    player "Mia wouldn't..."
    scene fs sophiachapterend3
    window hide
    pause
    scene fs sophiachapterend4
    with Dissolve(1.0)

    player "Sophia??!"
    player "What are you-"
    scene fs sophiachapterend6
    play sound "audio/sophiagameaudio/sophiablowjob1.wav"
    sophia "Uhn.."
    player "{i}She's sucking my dick!!{/i}"
    menu:
        "{color=#3eab33}Romantic{/color}":
            jump sophiachapter1rom
        "{color=#dd3939}Naughty{/color}":
            jump sophiachapter1naughty


label sophiachapter1rom:
    play sound "audio/sophiagameaudio/sophiablowjob1.wav" loop
    sophia "Uhnf.."
    scene fs sophiachapterend7
    player "Oh my god that feels so good.."
    sophia "MMMMM!"
    scene fs sophiachapterend6
    player "Holy shit yes! Your throat is so tight."
    scene fs sophiachapterend7
    sophia "Uh huh?"
    player "Don't fucking stop."
    scene fs sophiachapterend6
    voice "audio/sophiagameaudio/sophiauhn.wav"
    stop sound
    sophia "Uhhhn!!"
    player "Fuck baby I'm gonna cum!"
    scene fs sophiachapterend7
    "{i}{color=#a93b4c}He called me baby!{/color}{/i}"
    scene fs sophiachapterend6
    "{i}{color=#a93b4c}I can feel it twitching in my mouth.{/color}{/i}"
    scene fs sophiachapterend8
    with vpunch
    #$ hiden_textbox = False
    player "UUUGH! FUCK YES!"
    sophia "!!!!"
    scene fs sophiachapterend9
    with Dissolve(0.7)
    play sound "audio/sophiagameaudio/sophiapanting1.wav"
    player "Oh my god.."
    sophia "Hah...hah.."
    player "Sophia, what the hell was that?"
    scene fs sophiachapterend11
    sophia "Did you like cumming on my cute little face?"
    scene fs sophiachapterend10
    player "Hah, best childhood friend ever."
    scene fs sophiachapterend11
    sophia "Haha, pervert."
    player "I'm the pervert? You just broke into my house and blew me."
    scene fs sophiachapterend10
    sophia "Yeah I was...a little nervous about that. Wasn't sure how you'd react."
    player "Risky move."
    sophia "...."
    player "Well now you know...now WE know how I feel about it. About you."
    scene fs sophiachapterend11
    sophia "Really??!"
    player "Sophia if I knew you would and could blow me like that before I met Mia I wouldn't be dating her right now."
    scene fs sophiachapterend12
    sophia "I....I don't know what to say!"
    player "Me neither. This was nice but we need to have a serious talk soon."
    sophia "Yes I...I understand! No problem haha."
    sophia "Sorry I'm just so happy!"
    sophia "I-I'll get out of your hair...uh bed. Have a good day!"
    scene fs blackblank
    with Dissolve(1.0)
    "As promised Sophia left your place in a hurry, she didn't even wipe your cum off her face"
    "You felt pretty good, I mean after a morning bowjob who wouldn't? But you felt good about the future as well"
    player "I feel like everything is gonna work out."

    $ endchapter1_trigger = "1 sophia romantic"

    jump startofchapter2

label sophiachapter1naughty:

    scene fs sophiachapterend7
    voice "audio/sophiagameaudio/sophiauhn2.wav"
    sophia "Uhhnmf!"
    scene fs sophiachapterend6
    sophia "Mmmm."
    scene fs sophiachapterend7
    voice "audio/sophiagameaudio/sophiauhn.wav"
    sophia "UUUHN!"
    scene fs sophiachapterend6
    play sound "audio/sophiagameaudio/sophiablowjob2.wav" loop
    player "Look at you go."
    player "Always knew you were a dirty little slut."
    scene fs sophiachapterend7
    sophia "Uhn...Uhn!"
    scene fs sophiachapterend6
    player "You can't stop yourself can you? You're fucking pathetic."
    scene fs sophiachapterend7
    sophia "*Slurp* *Slurp*"
    scene fs sophiachapterend6
    player "You're not going deep enough."
    scene fs sophiachapterend7
    sophia "Uhhnn?"
    scene fs sophiachapterend6
    player "If you want to make me cum.."
    scene fs sophiachapterend13
    player "You're going to have to.."
    scene fs sophiachapterend14
    voice "audio/sophiagameaudio/sophiauhn.wav"
    with vpunch
    player "Go DEEPER!"
    sophia "EMMMMM! EMMM!"
    player "What's wrong? Mia can take this length easily."
    sophia "Uhnngg..."
    player "I wonder what she'd say, or the rest of your friends?"
    player "How could you do this to them huh? You must just not care about them at all."
    voice "audio/sophiagameaudio/sophiauhn.wav"
    sophia "EEUUUGH!"
    with vpunch
    voice "audio/sophiagameaudio/sophiauhn3.wav"
    sophia "EEUUUGH!"
    player "Getting harder to breath huh? Must be pretty difficult with my fat cock down your throat."
    with vpunch
    voice "audio/sophiagameaudio/sophiapwease.wav"
    sophia "EHN! PWEEASE!"
    player "The only way I'm letting you off my cock is if you make me cum."
    scene fs sophiachapterend13
    player "So don't..."
    scene fs sophiachapterend14
    with vpunch
    player "Stop sucking!!!"
    sophia "Ahhnnugh!"
    player "You ready bitch? Here it comes!"
    scene fs sophiachapterend15
    with vpunch
    sophia "MMMMM!"
    with flash
    player "Yeah that's it! That's it you stupid whore. Straight down your little throat."
    play audio "audio/sophiagameaudio/sophiagulping.wav"
    sophia "*Gulp* *Gulp*"
    window hide
    pause
    #$ hiden_textbox = False
    scene fs sophiachapterend16
    with vpunch
    play audio "audio/sophiagameaudio/sophiagasping.wav"
    sophia "Hah..*cough*...hah.."
    scene fs sophiachapterend17
    sophia "W-What the hell??! I almost died!"
    scene fs sophiachapterend19
    player "Shut the fuck up, I was holding your hair the entire time and I didn't feel one pull of resistance."
    scene fs sophiachapterend18
    sophia "I..."
    scene fs sophiachapterend19
    player "You know exactly what you did. You came into my house with intentions to sexually assault me and when things got rough you got upset."
    scene fs sophiachapterend17
    sophia "Assault you??! You just came down my throat!!"
    scene fs sophiachapterend19
    player "You think that would hold up in court?? I was ASLEEP Sophia!"
    scene fs sophiachapterend18
    sophia "No that's not..."
    player "...."
    scene fs sophiachapterend19
    player "I'm not going to sue you Sophia relax. I wouldn't do that."
    player "But what you did was really messed up."
    scene fs sophiachapterend17
    sophia "But you said such mean things!"
    scene fs sophiachapterend19
    player "And I meant every word. Because every word was true."
    player "You just made me cheat on Mia. My girlfriend and one of your BEST friends."
    player "Did you even think about that?"
    scene fs sophiachapterend18
    sophia "No..."
    scene fs sophiachapterend19
    player "You didn't think about anything other than how horny you were. That's what we call a slut."
    scene fs sophiachapterend18
    sophia "I'm not a s-"
    scene fs sophiachapterend19
    player "You are Sophia. Now stop denying it and get out of my house. I have a lot to think about."
    player "And we have a lot to talk about later. Understand?"
    sophia "...."
    player "I said do you UNDERSTAND?"
    scene fs sophiachapterend18
    sophia "Yes...I-I'll go.."
    scene fs blackblank
    with Dissolve(1.0)
    player "....Okay."
    player "That was awesome. I can't let Sophia know how much that turned me on."
    player "Of course she's still a pathetic little slut (which is interesting to find out after all these years)."
    player "But what guy doesn't like fucking a slut?"
    player "I'm gonna go back to sleep. Figure things out later."
    window hide
    pause

    $ endchapter1_trigger = "1 sophia naughty"

    jump startofchapter2

# interaction 1
# part 1

label sophiaphase2interaction1part1:
    hide screen uppergui
    hide screen tosunnyside
    scene fs sophiahouseoutside
    with Dissolve(0.5)

    $ sophiaquestlog = "It was crazy seeing Cass again. Sophia wanted to meet up at Café Seni in Sunnyside."
    $ cassandraquesticon = "gui/questboxCassandra.png"
    $ cassandraquestlog = "Weird seeing Cassandra again, she's still so hot."

    if endchapter1_trigger == "1 sophia romantic":
        player "{i}I need to talk to Sophia after what happened the other day.{/i}"
        player "{i}What she did was a surprise and...well probably wrong.{/i}"
        player "{i}But I'd be lying to myself if I said it wasn't hot.{/i}"
        player "{i}I did bust in her mouth. And she weighs like practically nothing I could've pushed her off anytime.{/i}"
        player "{i}Hah...damn. I'll just talk to her and see where things go. Nothing will come from just thinking about it.{/i}"

        show fbplayer current:
            xalign 0.3 ypos 120
        with Dissolve(0.5)
        pause

        show fbsophia defaultflip:
            xalign 0.45 ypos 120
        with Dissolve(0.5)
        pause

        show fbsophia current at surpriseshake
        $ cassSprite = 0
        player "Oh hey Sophia!"
        sophia "Wha-Oh! Hi [povname]!"
        player "I thought you were home I was about to knock on your door."
        sophia "No I was out and just got here haha."
        player "Ah cool..."
        sophia "Yeah. So...did you want to talk?"
        sophia "{size=-10}Or fool around again or something...{/size}"
        player "Yeah we really should talk. Can we go inside?"
        sophia "Haha yeah of course!"
        sophia "You know...I can't stop thinking about last night."
        player "{i}Shit.{/i}"
        sophia "I mean it's not exactly how I thought it would happen."
        show fbcassandra current behind fbsophia:
            xalign 0.7 ypos 120
        sophia "I almost didn't do it but after spending that time with you and talking and..."
        show fbcassandra current:
            xalign 0.65 ypos 120
        with move
        player "Ummm..."
        sophia "Haha well, you get what I'm trying to say."
        show fbcassandra current:
            xalign 0.6 ypos 120
        with move
        player "Soph? who is-"
        show fbcassandra current:
            xalign 0.55 ypos 120
        with move
        sophia "I know I know, we gotta figure out the Mia situation bu-"
        hide fbsophia current
        hide fbcassandra current
        show fbcassandra sophiahug1:
            xalign 0.50 ypos 120
        with vpunch
        cassandra "AHHHHH!"
        sophia "GAH!!!"
        sophia "Wha-"
        sophia "WHO ARE..."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Cass??!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Sophie!!!"
        player "Wait. Cass? Cassandra?"
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "No WAY is that [povname]??!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "G-Get off me sis!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Well would you LOOK at you! It's been ages!"
        player "Yeah you...you look great!"
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "Haha oh I know."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "UGH. Why are you here??"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Nice to see you too little sister."
        cassandra "I'm visiting!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Clearly."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Oh c'mon, I come all the way back here from across the country and this is my welcome?"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "...I-It's good to see you Cass.."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Haha I'm just messing with you sis no worries!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Have mom and dad s-"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Yeah I met with them a while ago, they said you were out so I was waiting to surprise you."
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "But it looks like I got a surprise too! Little [povname] is hot now holy shit."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "OH my God."
        player "Haha thanks Cass."
        sophia "Uh sis we were actually talking about something important s-"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "So you two dating yet?"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Cass!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Man Soph's been wanting to jump on your dick foreeeeeever. Glad to see it's finally happened."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "OH MY GOD CASSANDRA SHUT UP!!"
        player "Haha uh well, I'm actually dating a girl named Mia. Interesting to know that though."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Oops, sorry that must be awkward haha."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "UGH!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Wait Mia? Sophia's friend? Pink hair with a big smile and even bigger tits?"
        $ playerSprite = 1
        player "That's the one."
        $ playerSprite = 0
        cassandra "Oof, tough competition you got there lil sis."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Please god kill me."
        sophia "Cassandra. I am....GLAD....that you are back."
        hide fbcassandra sophiahug2
        show fbsophia defaultfliptalk:
            xalign 0.5 ypos 120
        show fbcassandra current:
            xalign 0.7 ypos 120
        with Dissolve(0.0)
        sophia "But would you PLEASE wait inside so I can talk to [povname] and we can catch up later?"
        show fbsophia defaultflip:
            xalign 0.5 ypos 120
        cassandra "Hmmm....fine for now. I'll see you soon [povname]! We gotta catch up too."
        $ playerSprite = 1
        player "Sounds uh...sounds good to me!"
        hide fbcassandra current
        with Dissolve(0.7)
        $ sophiaSprite = 1
        show fbsophia current:
            xalign 0.5 ypos 120
        sophia "Sigh....let's go to your place."
        $ sophiaSprite = 0
        player "Sure."

        scene fs livingroom
        with Dissolve(1.0)

        show fbsophia current:
            xalign 0.6 ypos 120
        show fbplayer current:
            xalign 0.4 ypos 120
        with Dissolve(0.7)

        player "Wow."
        sophia "I can't believe this..."
        player "Hey it's not that bad, sure she teases you a bit but she's always fun to be with."
        sophia "You don't understand [povname]. She's only gotten worse since we were kids."
        sophia "She's an unquenchable whore!!"
        player "Haha c'mon.."
        sophia "*Sigh*"
        sophia "Just promise me you'll stay away from her if you can help it."
        player "I can't say I won't greet her once since she's seen me. I mean she'll probably find me first.."
        player "But I'll try and keep my distance."
        sophia "Hah. Okay then."

        sophia "With that out of the way..."
        player "We have a serious talk to have Sophia."
        sophia "Yeah...we finally...got physical..."
        sophia "Did you just want to go all in from the get go or take it slow?"
        sophia "Oh that'd be so hot..."
        player "No you don't understand Sophia. We can't do anything like that again."
        sophia "W-What?"
        player "We both fucked up. What we did was a mistake."
        sophia "No....no! You s-said you liked it!"
        sophia "You came in my mouth! I made you feel good!! Better than Mia!!!"
        player "{i}Shit she's really overreacting here.{/i}"
        player "I know, and in the moment it did feel good. I didn't stop you."
        sophia "So then-"
        player "That's why I'm not angry at you, I was complacent. But it was still wrong."
        sophia "*sniff* I...I don't believe you. You're lying to yourself!"
        player "Soph. I was asleep."
        player "When you woke me up I was so drowzy I even thought you were Mia, I swear to God."
        sophia "....."
        player "Look. I'm flattered that you feel this way about me, and I'll always love you you know that."
        sophia "You will?"
        player "Of course don't be ridiculous."
        sophia "Okay..."
        player "But I'm dating Mia, we can't change that. Maybe if things were different..."
        sophia "??"
        player "But they aren't."
        sophia "Hmmm..."
        player "{i}She still doesn't look convinced. This might be harsh but I'll have to say something to really make her stop pursuing me{/i}"
        player "Mia is a great person Sophia you know that right?"
        sophia "Yeah."
        player "Well she's also really really hot. And she satisfies me like no one else can."
        player "I'm on cloud nine when we fuck, I can't get that from anyone else and I know for certain she feels the same."
        sophia "....."
        player "So do you understand? WE can't happen. Not like this."
        sophia "Yes. I think I understand."
        player "Great! You know we'll always be friends."
        sophia "So let's say....hypothetically."
        player "Do not say you're gonna kill Mia you little psycho."
        sophia "What?? No she's still my friend!!"
        sophia "I'm just saying if hypothetically we were in a situation where someone else was satisfiying you just as good you'd be with them?"
        player "Sophia."
        sophia "And you never knew Mia!"
        player "....."
        player "I suppose. In that hypothetical, if it'll give you closure..."
        player "Sure. Yeah I would."
        sophia "Okay!"
        player "We good?"
        sophia "We're good! Water under the bridge."
        player "Fantastic. I feel a lot better now."
        sophia "Yeah me too. I'm gonna go now, catch up with my sister."
        player "Sure no problem, I'll see you later."
        sophia "Bye!"

        hide fbplayer current
        scene fs sophiahouseoutside
        with Dissolve(0.5)
        pause
        show fbsophia current:
            xalign 0.5 ypos 120
        with Dissolve(0.7)
        sophia "{i}You really think I'm going to stop [povname]??{/i}"
        sophia "{i}Neither my sister, nor Mia, nor anyone else is going to stop me from having you all to myself!{/i}"
        sophia "{i}I've held onto these feelings for 15 years!{/i}"
        sophia "{i}I'll find a way for you to fall for me AND keep being friends with everyone!{/i}"
        sophia "Then I'll ride your fat cock till your balls are DRY!!!"
        "Neighbour" "W-What?!"
        sophia "Oh nothing Mrs Henderson! Sorry."
        "Neighbour" "Okay..."
        sophia "Ahem."
        $ sophiaphase2interaction1 = 1
        $ sophiaphase1interaction2 = 3

        jump overworldmap




    elif endchapter1_trigger == "1 sophia naughty":

        $ playerSprite = 0
        show fbplayer current:
            xalign 0.3 ypos 120
        with Dissolve(0.5)
        pause

        show fbsophia defaultflip:
            xalign 0.45 ypos 120
        with Dissolve(0.5)
        pause


        $ cassSprite = 0

        player "{i}I need to talk to Sophia after what happened the other day.{/i}"

        $ playerSprite = 1
        player "Hey Sophia."
        $ playerSprite = 0
        $ sophiaSprite = 7
        show fbsophia current at surpriseshake
        sophia "Wha-Oh! Hi [povname]..."
        $ sophiaSprite = 0
        $ playerSprite = 1
        player "I thought you were home I was about to knock on your door."
        $ playerSprite = 0
        $ sophiaSprite = 8
        sophia "Oh...yeah no I-I was out. Just got home."
        $ playerSprite = 16
        player "Ah cool..."
        $ playerSprite = 8
        sophia "Yeah..."
        $ playerSprite = 16
        player "So....we need to talk, should we go inside?"
        $ playerSprite = 0
        $ sophiaSprite = 7
        sophia "Yeah I guess I...yeah. Yup."
        $ sophiaSprite = 9
        sophia "{i}Oh gosh, what is he gonna say? He was so mean to me...{/i}"
        show fbcassandra current behind fbsophia:
            xalign 0.7 ypos 120
        pause
        $ playerSprite = 11
        player "Ummm..."

        show fbcassandra current:
            xalign 0.65 ypos 120
        with move
        $ playerSprite = 17
        player "First I..."
        $ playerSprite = 11
        show fbcassandra current:
            xalign 0.6 ypos 120
        with move
        $ playerSprite = 17
        player "Uhh...."
        $ playerSprite = 11
        $ sophiaSprite = 7
        sophia "What?"
        $ sophiaSprite = 0
        show fbcassandra current:
            xalign 0.55 ypos 120
        with Dissolve(0.7)
        $ playerSprite = 17
        player "Who...is-"
        $ playerSprite = 11
        hide fbsophia current
        hide fbcassandra current
        show fbcassandra sophiahug1:
            xalign 0.50 ypos 120
        with vpunch
        cassandra "HEHEHE!"
        sophia "GAH!!!"
        sophia "Wha-"
        sophia "WHO ARE..."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Cass??!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Sophie!!!"
        $ playerSprite = 17
        player "Wait. Cass? Cassandra?"
        $ playerSprite = 11
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "No WAY is that [povname]??!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "G-Get off me sis!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Well would you LOOK at you! It's been ages!"
        $ playerSprite = 16
        player "Yeah you...you look great!"
        $ playerSprite = 0
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "Haha oh I know."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "UGH. Why are you here??"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Nice to see you too little sister."
        cassandra "I'm visiting!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Clearly."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Oh c'mon, I come all the way back here from across the country and this is my welcome?"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "...I-It's good to see you Cass.."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Haha I'm just messing with you sis no worries!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Have mom and dad s-"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Yeah I met with them a while ago, they said you were out so I was waiting to surprise you."
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "But it looks like I got a surprise too! Little [povname] is hot now holy shit."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "OH my God."
        $ playerSprite = 1
        player "Haha thanks Cass."
        $ playerSprite = 0
        sophia "Uh sis we were actually talking about something important s-"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "So you two dating yet?"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Cass!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Man Soph's been wanting to jump on your dick foreeeeeever. Glad to see it's finally happened."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "OH MY GOD CASSANDRA SHUT UP!!"
        $ playerSprite = 1
        player "Haha uh well, I'm actually dating a girl named Mia. Interesting to know that though."
        $ playerSprite = 0
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Oops, sorry that must be awkward haha."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "UGH!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Wait Mia? Sophia's friend? Pink hair with a big smile and even bigger tits?"
        $ playerSprite = 1
        player "That's the one."
        $ playerSprite = 0
        cassandra "Oof, tough competition you got there lil sis."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Please god kill me."
        sophia "Cassandra. I am....GLAD....that you are back."
        hide fbcassandra sophiahug2
        show fbsophia defaultfliptalk:
            xalign 0.5 ypos 120
        show fbcassandra current:
            xalign 0.7 ypos 120
        with Dissolve(0.0)
        sophia "But would you PLEASE wait inside so I can talk to [povname] and we can catch up later?"
        show fbsophia defaultflip:
            xalign 0.5 ypos 120
        $ cassSprite = 1
        cassandra "Hmmm....fine for now. I'll see you soon [povname]! We gotta catch up too."
        $ cassSprite = 0
        $ playerSprite = 1
        player "Sounds uh...sounds good to me!"
        hide fbcassandra current
        with Dissolve(0.7)
        $ sophiaSprite = 2
        show fbsophia current:
            xalign 0.5 ypos 120
        sophia "Sigh....let's go to your place."
        $ sophiaSprite = 10
        player "Sure."

        scene fs livingroom
        with Dissolve(1.0)

        show fbsophia current:
            xalign 0.6 ypos 120
        show fbplayer current:
            xalign 0.4 ypos 120
        with Dissolve(0.7)

        $ playerSprite = 1
        player "Wow."
        $ playerSprite = 0
        $ sophiaSprite = 2
        sophia "I can't believe this..."
        $ playerSprite = 1
        $ sophiaSprite = 10
        player "Hey it's not that bad, sure she teases you a bit but she's always fun to be with."
        $ playerSprite = 0
        $ sophiaSprite = 2
        sophia "You don't understand [povname]. She's only gotten worse since we were kids."
        $ sophiaSprite = 4
        sophia "She's an unquenchable whore!!"
        $ playerSprite = 1
        $ sophiaSprite = 10
        player "Haha c'mon.."
        $ playerSprite = 0
        $ sophiaSprite = 2
        sophia "*Sigh*"
        sophia "Just promise me you'll stay away from her if you can help it."
        $ playerSprite = 1
        $ sophiaSprite = 10
        player "I can't say I won't greet her once since she's seen me. I mean she'll probably find me first.."
        player "But I'll try and keep my distance."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Hah. Okay then."
        sophia "With that out of the way..."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "We have a serious talk to have Sophia."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Oh yeah..."
        $ sophiaSprite = 0
        player "{i}I should probably be nice to start so she doesn't overreact.{/i}"
        player "{i}I don't want her to tell the Mia or the other girls{/i}"
        $ playerSprite = 1
        player "First of off Sophia. I wanted to say sorry."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "R-Really?"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "I was really...harsh. With some of the things I said, and in hindsight I regret saying them."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Okay!"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "I was groggy and horny and in a state of confusion at the time so I didn't mean half the things I said."
        $ playerSprite = 0
        sophia "{i}He admits I made him horny!!{/i}"
        $ sophiaSprite = 1
        sophia "T-That's alright I forgive you!"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "But now, we move on. We don't mention this to anyone and we just stay friends from now on."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "What?"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "What do you mean what?"
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "I just...I thought maybe we could figure something out?"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "Figure something out? Even after the way I treated you?"
        $ playerSprite = 0
        sophia "{i}I probably shouldn't tell him I got really turned on when he was rough with me.{/i}"
        $ sophiaSprite = 1
        sophia "{i}Not yet at least.{/i}"
        $ sophiaSprite = 1
        sophia "Yeah it's fine...w-water under the bridge."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "*Sigh* No that doesn't even matter. Sophia."
        player "I'm dating Mia, we can't change that. Maybe if things were different..."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "??"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "But they aren't."
        $ playerSprite = 0
        sophia "Hmmm..."
        player "{i}She still doesn't look convinced. This might be harsh but I'll have to say something to really make her stop pursuing me{/i}"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "Mia is a great person Sophia you know that right?"
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Yeah."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "Well she's also really really hot. And she satisfies me like no one else can."
        player "I'm on cloud nine when we fuck, I can't get that from anyone else and I know for certain she feels the same."
        $ playerSprite = 0
        sophia "....."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "So do you understand? WE can't happen. Not like this."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Yes. I think I understand."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "Great! You know we'll always be friends."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "So let's say....hypothetically."
        $ playerSprite = 5
        $ sophiaSprite = 0
        player "Do not say you're gonna kill Mia you little psycho."
        $ playerSprite = 4
        $ sophiaSprite = 7
        sophia "What?? No she's still my friend!!"
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "I'm just saying if hypothetically we were in a situation where someone else was satisfiying you just as good you'd be with them?"
        $ playerSprite = 15
        $ sophiaSprite = 0
        player "Sophia."
        $ playerSprite = 14
        $ sophiaSprite = 1
        sophia "And you never knew Mia!"
        $ sophiaSprite = 0
        player "....."
        $ playerSprite = 15
        $ sophiaSprite = 0
        player "I suppose. In that hypothetical, if it'll give you closure..."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "Sure. Yeah I would."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Okay!"
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "We good?"
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "We're good! Water under the bridge like I said."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "Fantastic. I feel a lot better now."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Yeah me too. I'm gonna go now, catch up with my sister."
        $ playerSprite = 1
        $ sophiaSprite = 0
        player "Sure no problem, I'll see you later."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Bye!"
        $ sophiaSprite = 0

        hide fbplayer current
        scene fs sophiahouseoutside
        with Dissolve(0.5)
        pause
        show fbsophia current:
            xalign 0.5 ypos 120
        with Dissolve(0.7)
        sophia "{i}You really think I'm going to stop [povname]??{/i}"
        sophia "{i}Neither my sister, nor Mia, nor anyone else is going to stop me from having you all to myself!{/i}"
        sophia "{i}I've held onto these feelings for 15 years!{/i}"
        sophia "{i}I'll find a way for you to fall for me AND keep being friends with everyone!{/i}"
        $ sophiaSprite = 4
        sophia "Then I'll ride your fat cock till your balls are DRY!!!"
        "Neighbour" "W-What?!"
        show fbsophia defaultfliptalk:
            xalign 0.5 ypos 120
        sophia "Oh nothing Mrs Henderson! Sorry."
        "Neighbour" "Okay..."
        $ sophiaSprite = 0
        show fbsophia current:
            xalign 0.5 ypos 120
        sophia "Ahem."
        $ sophiaphase2interaction1 = 1
        $ sophiaphase1interaction2 = 3

        jump overworldmap

    else:
        player "I should knock on Sophia's house, see what's she's up to."

        show fbplayer current:
            xalign 0.3 ypos 120
        with Dissolve(0.5)
        pause

        show fbsophia defaultflip:
            xalign 0.45 ypos 120
        with Dissolve(0.5)
        pause

        $ cassSprite = 0
        $ sophiaSprite = 0
        $ playerSprite = 1

        show fbsophia current at surpriseshake



        player "Oh hey Sophia."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Wha-Oh! Hi [povname]!"
        $ sophiaSprite = 0
        $ playerSprite = 1
        player "I thought you were home I was about to knock on your door."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Nope! Just got home."
        $ sophiaSprite = 0
        $ playerSprite = 1
        player "Ah cool."
        $ playerSprite = 0
        $ sophiaSprite = 1
        sophia "Haha."
        sophia "You wanna come inside?"
        $ sophiaSprite = 0
        player "{i}Heh.{/i}"
        $ playerSprite = 1
        player "Yeah sure I-"
        $ playerSprite = 11

        show fbcassandra current behind fbsophia:
            xalign 0.7 ypos 120
        pause
        player "...."
        sophia "?"
        player "Ummm..."

        show fbcassandra current:
            xalign 0.65 ypos 120
        with move
        $ playerSprite = 17
        player "First I..."
        show fbcassandra current:
            xalign 0.6 ypos 120
        with move
        player "Uhh...."
        $ playerSprite = 11
        $ sophiaSprite = 1
        sophia "What?"
        $ sophiaSprite = 0
        show fbcassandra current:
            xalign 0.55 ypos 120
        with move
        $ playerSprite = 17
        player "Who...is-"
        $ playerSprite = 11
        hide fbsophia current
        hide fbcassandra current
        show fbcassandra sophiahug1:
            xalign 0.50 ypos 120
        with vpunch
        cassandra "AHHHHH!"
        sophia "GAH!!!"
        sophia "Wha-"
        sophia "WHO ARE..."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Cass??!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Sophie!!!"
        $ playerSprite = 17
        player "Wait. Cass? Cassandra?"
        $ playerSprite = 11
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "No WAY is that [povname]??!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "G-Get off me sis!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Well would you LOOK at you! It's been ages!"
        $ playerSprite = 1
        player "Yeah you...you look great!"
        $ playerSprite = 0
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "Haha oh I know."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "UGH. Why are you here??"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Nice to see you too little sister."
        cassandra "I'm visiting!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Clearly."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Oh c'mon, I come all the way back here from across the country and this is my welcome?"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "...I-It's good to see you Cass.."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Haha I'm just messing with you sis no worries!"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Have mom and dad s-"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Yeah I met with them a while ago, they said you were out so I was waiting to surprise you."
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        cassandra "But it looks like I got a surprise too! Little [povname] is hot now holy shit."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "OH my God."
        show fbcassandra sophiahug3:
            xalign 0.50 ypos 120
        $ playerSprite = 1
        player "Haha thanks Cass."
        $ playerSprite = 0
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Uh sis we were actually talking about something important s-"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "So you two dating yet?"
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Cass!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Man Soph's been wanting to jump on your dick foreeeeeever. Glad to see it's finally happened."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "OH MY GOD CASSANDRA SHUT UP!!"
        player "Haha uh well, I'm actually dating a girl named Mia. Interesting to know that though."
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Oops, sorry that must be awkward haha."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "UGH!!"
        show fbcassandra sophiahug2b:
            xalign 0.50 ypos 120
        cassandra "Wait Mia? Sophia's friend? Pink hair with a big smile and even bigger tits?"
        $ playerSprite = 1
        player "That's the one."
        $ playerSprite = 0
        cassandra "Oof, tough competition you got there lil sis."
        show fbcassandra sophiahug2:
            xalign 0.50 ypos 120
        sophia "Please god kill me."
        sophia "Cassandra. I am....GLAD....that you are back."
        hide fbcassandra sophiahug2
        show fbsophia defaultfliptalk:
            xalign 0.5 ypos 120
        show fbcassandra current:
            xalign 0.7 ypos 120
        with Dissolve(0.0)
        $ sophiaSprite = 1
        sophia "But would you PLEASE wait inside so I can talk to [povname] and we can catch up later?"
        show fbsophia defaultflip:
            xalign 0.5 ypos 120
        cassandra "Hmmm....fine for now. I'll see you soon [povname]! We gotta catch up too."
        $ playerSprite = 16
        player "Sounds uh...sounds good to me!"
        hide fbcassandra current
        with Dissolve(0.7)
        $ sophiaSprite = 2
        $ playerSprite = 0
        show fbsophia current:
            xalign 0.5 ypos 120
        sophia "Sigh....let's go to your place."
        $ sophiaSprite = 0
        $ playerSprite = 1
        player "No."
        $ sophiaSprite = 1
        $ playerSprite = 0
        sophia "No?"
        $ sophiaSprite = 0
        $ playerSprite = 1
        player "Yeah go deal with your sister first. I know how you are with her. We can hang out somewhere else afterwards."
        $ sophiaSprite = 1
        $ playerSprite = 0
        sophia "Oh okay um..."
        sophia "Let's meet up at Café Seni!"
        $ sophiaSprite = 0
        $ playerSprite = 1
        player "Seni? Oh the one where you guys go all the time."
        $ sophiaSprite = 1
        $ playerSprite = 0
        sophia "Yeah I've been hanging out there during the day now since it gets so hot and I have a small break from school."
        $ sophiaSprite = 0
        $ playerSprite = 1
        player "Alright sounds good Soph, see you there."
        $ sophiaSprite = 1
        $ playerSprite = 0
        sophia "Great! See you later!"
        hide fbplayer current
        with Dissolve(0.7)
        pause
        $ sophiaSprite = 2
        sophia "*Sigh*....Happy face Sophia."
        show fbsophia defaultfliptalk:
            xalign 0.5 ypos 120
        sophia "Cass! Tell me about your trip!"
        hide fbsophia defaultfliptalk
        with Dissolve(0.7)

        $ sophiaphase2interaction1 = 1
        $ sophiaphase1interaction2 = 3

        jump overworldmap

# part 2


label sophiaphase2interaction2part2:
    hide screen exit_cafe
    hide screen questboxpreview
    stop music fadeout 5
    $ playerSprite = 0
    $ sophiaSprite = 1
    show fbsophia current:
        xalign 0.55 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    sophia "Hey [povname]!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Hey Sophia."
    player "Should we sit down?"
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Yeah let's get a booth together!"
    $ sophiaSprite = 0
    scene fs sophiacafescene1a
    with Dissolve(0.7)
    player "This place is really nice I should come by more often."
    scene fs sophiacafescene1b
    sophia "Yeah! I'm here all the time when I'm out and not at school!"
    sophia "{i}Hehe it's like we're on another date!{/i}"
    scene fs sophiacafescene1a
    player "So Sophia, there's something I really need to talk to you about."
    sophia "{i}He's so dreamy...{/i}"
    player "It's really important you listen to me alright?"
    scene fs sophiacafescene1b
    sophia "Uh huh..."
    scene fs sophiacafescene1a
    player "So our relationship has been..."
    sophia "{i}I just find myself thinking about his huge cock all the time...{/i}"
    player "I want to keep it completely platonic..."
    sophia "{i}I wonder if he'd wanna do it in my butt...{/i}"
    player "I mean we'll always be friends..."
    sophia "{i}Yeah....yeah he would.{/i}"
    scene fs sophiacafescene2a
    "Waitress" "Howdy folks!"
    scene fs sophiacafescene2b
    player "Hey."
    sophia "Hi!"
    "Waitress" "And what can I get the cute couple today?"
    player "{i}I won't bother saying we're not together, too much hassle.{/i}"
    player "I just want something light, you have a drink menu?"
    "Waitress" "We sure do!"
    sophia "{i}[povname] didn't correct her!!{/i}"

    scene fs sophiacafescene4a
    with Dissolve(0.7)
    "Waitress" "Here you go!"
    scene fs sophiacafescene4b
    sophia "Oh we gotta get the couples' re-TREAT!"
    scene fs sophiacafescene4a
    player "I don't know Sophia, this is the kinda thing I was talking about..."
    sophia "{i}Ohhh it comes with a fancy straw.{/i}"
    scene fs sophiacafescene3a
    sophia "If we don't order it I'm telling the waitress you were looking at her boobs."
    scene fs sophiacafescene3b
    player "What? I wasn't looking at her boobs."
    scene fs sophiacafescene3a
    sophia "Yes. Yes you were."
    sophia "And even if you weren't imma still tell her!"
    player "....."
    scene fs sophiacafescene3b
    player "Well it is 50 percent couples discount. Guess I can pretend to get the deal."
    scene fs sophiacafescene3c
    sophia "Yay!"
    sophia "{i}Couples drink for the couple!{/i}"
    scene fs blackblank
    with Dissolve(0.7)
    "A little while later.."
    scene fs sophiacafescene5
    with Dissolve(0.5)
    "Waitress" "Here's your drink! Enjoy!"
    player "This looks absolutely ridiculous."
    sophia "{i}It's...{/i}"
    sophia "{i}Perfect.{/i}"
    scene fs sophiacafescene6
    with Dissolve(0.5)
    player "*Gulp Gulp*"
    sophia "MMMMM!"
    scene fs sophiacafescene7
    with Dissolve(0.7)
    player "That's actually really not bad!"
    sophia "Hehe I knew it was gonna be good!"
    sophia "{i}Ahhh I'm so happy right now!{/i}"
    scene fs blackblank
    with Dissolve(0.5)
    "You and Sophia continue to down the drink together"
    "All the while you try your best to gently inform her that she's getting too clingy, and that you can't cross the line between friends and something more"
    "She kept nodding her head in agreement but...she might not've really been paying attention at all"

    scene fs livingroom
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbsophia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Well that was pretty fun."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Hehe yeah!!"
    $ playerSprite = 1
    $ sophiaSprite = 0
    player "Now you were paying attention right? You're okay with everything I said."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Yup!"
    $ playerSprite = 1
    $ sophiaSprite = 0
    player "About us?"
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Hehe uh huh!"
    $ playerSprite = 1
    $ sophiaSprite = 0
    player "You're sure?"
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Relax I TOTALLY UNDERSTAND what you're saying hehe."
    $ playerSprite = 4
    $ sophiaSprite = 0
    player "...."
    $ playerSprite = 5
    player "I don't think you've listened to a word that I said."
    $ playerSprite = 4
    $ sophiaSprite = 1
    sophia "Of course I have."
    $ playerSprite = 5
    $ sophiaSprite = 0
    player "Tell me what I want then."
    $ playerSprite = 4
    $ sophiaSprite = 1
    sophia "Hehe, you WANT us to keep our dating on the down low."
    sophia "So that no one catches on!"
    $ playerSprite = 5
    $ sophiaSprite = 0
    player "Sophia."
    $ playerSprite = 4
    $ sophiaSprite = 1
    sophia "I don't mind sharing you really I don't, as long as you save most of yourself for m-"
    $ playerSprite = 5
    $ sophiaSprite = 0
    player "Sophia that's not what I said at all!"
    $ playerSprite = 4
    $ sophiaSprite = 1
    sophia "Huh?"
    $ playerSprite = 5
    $ sophiaSprite = 0
    player "I just want to be FRIENDS. I don't want to fuck you and I don't want to date you!!!"
    $ playerSprite = 4
    $ sophiaSprite = 2
    sophia "But...n-no."
    $ playerSprite = 5
    $ sophiaSprite = 0
    player "The fuck do you mean no?"
    $ playerSprite = 4
    $ sophiaSprite = 4
    sophia "T-The night I invited you to that party! I was going to ask you out!!"
    sophia "I've loved you for so long [povname]! SINCE WE WERE KIDS!!!"
    $ playerSprite = 11
    $ sophiaSprite = 3
    player "Woah Sophia hold on..."
    $ sophiaSprite = 4
    sophia "You weren't supposed to...to meet Mia like that."
    sophia "I finally got the courage to tell you how I felt and I couldn't find you!"
    sophia "You already left."
    $ playerSprite = 15
    $ sophiaSprite = 3
    player "Yeah...Mia and I left the party about halfway in."
    $ playerSprite = 14
    $ sophiaSprite = 4
    sophia "It's not FAIR! It's not fair!!!!"
    $ playerSprite = 15
    $ sophiaSprite = 3
    player "Soph calm down."
    $ playerSprite = 14
    $ sophiaSprite = 8
    sophia "Ever since I saw you with Mia the night you stood me up I can't get you out of my head!"
    $ playerSprite = 11
    $ sophiaSprite = 10
    player "Wait what do you mean?"
    $ sophiaSprite = 8
    sophia "I followed you home [povname]. I watched you fuck one of my best friends while I stood there in the rain."
    $ sophiaSprite = 9
    player "{i}That's actually pretty hot to me. But I can't let her know that.{/i}"
    $ playerSprite = 15
    player "Jesus Sophia."
    $ playerSprite = 14
    $ sophiaSprite = 8
    sophia "I know...I know I'm pathetic!"
    $ sophiaSprite = 4
    sophia "I just can't let GO! My pussy is just always on FIRE!!"
    sophia "I already liked you but now every cell of my body wants you and it's..."
    sophia "It's tearing me apart!"
    $ playerSprite = 7
    $ sophiaSprite = 10
    player "Hmmm."
    $ sophiaSprite = 4
    sophia "'Hmmmm'? Really that's your response? I'm baring my soul here."
    $ playerSprite = 1
    $ sophiaSprite = 10
    player "You're like super horny."
    $ playerSprite = 0
    $ sophiaSprite = 7
    sophia "Yes!"
    $ playerSprite = 1
    $ sophiaSprite = 9
    player "No I mean like, I think that's the route of the problem rather than the symptom."
    $ playerSprite = 0
    $ sophiaSprite = 7
    sophia "What do you mean?"
    $ playerSprite = 1
    $ sophiaSprite = 9
    player "I think if we take care of....you. You'll be able to relax and move on."
    player "Trust me, as a guy sometimes you just can't focus until you get your rocks off."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "Uh....okay."
    sophia "So what are you suggesting."
    $ playerSprite = 5
    $ sophiaSprite = 0
    player "I need you to PROMISE never to tell anyone what we do tonight."
    $ playerSprite = 4
    $ sophiaSprite = 1
    sophia "Oh...okay!"
    $ playerSprite = 5
    $ sophiaSprite = 0
    player "Promise you'll move on and forget all this relationship with me stuff okay?"
    $ playerSprite = 4
    $ sophiaSprite = 1
    sophia "Sure sure I promise! W-What are we gonna do?"
    $ playerSprite = 15
    $ sophiaSprite = 0
    player "*Sigh*...get on my bed. I gotta take my pants off."
    scene fs sophiathighfuck1
    with Dissolve(0.7)
    sophia "Oh...wow!"
    player "{i}I can't let her know how turned on I'm getting.{/i}"
    player "{i}Hopefully she's so horny she won't realize how hard I am.{/i}"
    sophia "You're so hard!"
    player "Uh....yeah."
    player "Put your thighs on me."
    scene fs sophiathighfuck2
    with Dissolve(0.7)
    player "Yeah...yeah just like that."
    player "{i}Fuck this POV is hot.{/i}"
    player "Now you're gonna squeeze your thighs together and...well and move."
    scene fs sophiathighfuck3
    with Dissolve(0.7)
    sophia "Oh I see."
    sophia "You want to thigh fuck me!"
    player "Fuck....y-yeah."
    sophia "Okay!"
    show sophiathighfuck4 movie
    sophia "Mmmm."
    player "{i}Shit her skin is really soft.{/i}"
    sophia "This feels so good [povname] I-I can feel your cock against my pussy!"
    player "Yeah keep going Soph!"
    show sophiathighfuck5 movie
    sophia "I'm getting so wet!"
    player "Fuck that's it!"
    play sound "audio/sophiagameaudio/sophiamoaning1.wav"
    sophia "EHHHN!!!"
    player "I'm gonna cum!"
    sophia "ME TOO ME TOO!!!"
    pause
    show sophiathighfuck6 movie
    player "AHHH SHIT."
    voice "audio/sophiagameaudio/sophiaturnedonlaugh.wav"
    sophia "Hehehe."
    sophia "Mmmmm look at all of it..."
    scene fs sophiathighfuck6b
    with Dissolve(0.5)
    player "Phew..."
    sophia "I made you feel really good didn't I?"
    player "Yeah for sure. So..."
    player "You good now? You ready to move on?"
    sophia "Yeah I totally am!"
    player "Promise?"
    sophia "Promise!"
    player "Alright."
    scene fs blackblank
    with Dissolve(1.0)

    $ sophiascenedaycheck = 1
    $ sophiaphase2interaction1 = 2
    $ sophiaquestlog = "Sophia said she understands but I'm not so sure she got the message..."
    $ timeofday = "Night"
    jump gotosleep

# part 3

label sophiaphase2interaction2part3:
    hide screen backbuttonROOM
    hide screen uppergui
    scene fs playerbedsmile
    with Dissolve(1.0)
    "Some time during night.."
    player "Ahhh. I am very comfortable right now."
    "VVVVP VVVVVP"
    scene fs playerbedthink2
    player "Huh? Who's texting me?"

    scene fs playerroomNight
    with Dissolve(0.7)
    sophia "{cps=25}Heeey!{/cps}"
    player "{cps=25}Hey Sophia. What is it?{/cps}"
    sophia "{cps=25}I wanted to thank you for such a wonderful date the other day!{/cps}"
    sophia "{cps=25}So I've sent you something to help you sleep ;P{/cps}"
    $ renpy.notify("Got Sophia's Selfie!")

    $ phone_pictures.append("20-0c")

    show nfs sophiapussypic:
        xalign 0.5 yalign 0.4

    player "Holy shit what the fuck!"
    player "She sent me a pussy pic!"
    pause
    player "{cps=25}Sophia WTF???{/cps}"
    sophia "{cps=25}You like it? I was about to touch myself.{/cps}"
    sophia "{cps=25}Thinking about your BIG cock sliding inbetween my thighs...{/cps}"
    hide nfs sophiapussypic
    player "Lord knows I find that hot as hell but I can't let her think I'm into it."
    player "I need to stop this right now."
    player "{cps=25}Get the fuck over here right now!{/cps}"
    sophia "{cps=25}OMG I'll be right there!{/cps}"
    player "I'm gonna have to teach this bitch properly."
    player "Since the carrot didn't work, I'm gonna have to use the stick."
    scene fs livingroomnight
    with Dissolve(0.7)

    $ playerSprite = 4

    show fbsophia current:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ sophiaSprite = 1
    sophia "I'm here!"
    $ sophiaSprite = 0
    player "...."

    scene fs sophiacouchfinger1
    with Dissolve(0.7)
    sophia "H-Hey hehe..."
    scene fs sophiacouchfinger1b
    player "Sit down."
    scene fs sophiacouchfinger2
    sophia "Sure!"
    sophia "So what are we gonna do on the couch? Hehe."
    scene fs sophiacouchfinger2b
    player "You don't listen."
    scene fs sophiacouchfinger2
    sophia "You know I was pretty nervous when I sent that 'Selfie' haha."
    sophia "But I was so turned on, was the angle go-"
    scene fs sophiacouchfinger3
    player "Enough."
    sophia "Oh! I-Is it time? I dunno if I'm ready haha-"
    scene fs sophiacouchfinger3b
    voice "audio/sophiagameaudio/sophiaguh.wav"
    sophia "Ah!"
    scene fs sophiacouchfinger4b
    sophia "Uh...w-what are you doing?"
    scene fs sophiacouchfinger4
    player "You don't fucking LISTEN."
    scene fs sophiacouchfinger5
    sophia "[povname] I don't understand what you're saying. Is this some kind of role play?"
    scene fs sophiacouchfinger6b
    player "You're such a fucking SLUT."
    scene fs sophiacouchfinger6
    sophia "Why are you being mean to m-"
    scene fs sophiacouchfinger7
    with vpunch
    play sound "audio/oneslap.wav"
    voice "audio/sophiagameaudio/sophiaAhh.wav"
    sophia "AHH!"
    scene fs sophiacouchfinger6b
    player "You need to be taught a fucking LESSON!"
    scene fs sophiacouchfinger7
    with vpunch
    play sound "audio/oneslap.wav"
    voice "audio/sophiagameaudio/sophiauhn3.wav"    
    sophia "OWWW!!"
    scene fs sophiacouchfinger6
    sophia "[povname] that really hurts! I don't understan-"
    scene fs sophiacouchfinger7
    with vpunch
    play sound "audio/oneslap.wav"
    voice "audio/sophiagameaudio/sophiamoan2.wav"    
    sophia "AHHN!"
    scene fs sophiacouchfinger8
    with Dissolve(0.5)
    sophia "Hah....hah...oh..."
    scene fs sophiacouchfinger9
    with vpunch
    play sound "audio/oneslap.wav"
    voice "audio/sophiagameaudio/sophiamoan1.wav"  
    player "You're NOT my girlfriend!"
    player "SAY IT!"
    with vpunch
    play sound "audio/oneslap.wav"
    sophia "I-I'm not your girlfriend!"
    player "You're a dirty little whore."
    sophia "Um..."
    player "SAY IT!"
    with vpunch
    play sound "audio/oneslap.wav"
    voice "audio/sophiagameaudio/sophiamoan2.wav" 
    sophia "I'm a dirty little whore!!"
    init python:
        renpy.music.register_channel("secondsound", loop=True)

    image fingersophiacouch1:
        "21-10.png"
        0.7
        "21-10B.png"
        0.7
        repeat
    show fingersophiacouch1
    play secondsound "audio/pussyfingering.wav"
    sophia "Oh..w-what are you-"
    play sound "audio/sophiagameaudio/sophiafingerbanged.wav" loop
    sophia "OH MY GOD!"
    player "You like this you fucking bitch huh?"
    player "Like my fingers sliding up your slutty cunt?"
    sophia "I....I!!"
    sophia "I'm gonna!!!"
    scene fs sophiacouchfinger11
    with vpunch
    stop sound
    stop secondsound
    play sound "audio/sophiagameaudio/sophiaorgasm.wav"
    sophia "AHHHN!!!"
    with flash
    sophia "OHHHHMYGOOOOOD!"
    player "That's what I thought you worthless little whore!"
    scene fs sophiacouchfinger12
    with Dissolve(0.5)
    sophia "Ah...ah..guh..."
    player "Pathetic."


    #$ contact_list.append("Sophia")

    $ sophiaphase2interaction1 = 3
    $ sophiaquestlog = "I think Sophia got the message. Unrelated, I really liked that drink from Café Seni..."
    $ timeofday = "Night"
    jump passtime

# interaction 3
# part 1

label sophiaphase2interaction3part1:
    hide screen uppergui
    hide screen questboxpreview
    hide screen exit_cafe
    stop music fadeout 5
    scene fs blackblank
    with Dissolve(1.0)
    "A little while later..."
    scene fs waitressbang3
    with Dissolve(0.7)
    pause
    sophia "Hmmm."
    scene fs waitressbang4
    sophia "Should I get those new seasonal biscuits?"
    sophia "I think they have more calories though.."
    scene fs waitressbang5
    sophia "Where is the waitress? I've been waiting here for a while now..."
    scene fs waitressbang6
    "*Thump thump thump*"
    sophia "Huh?"
    sophia "I think I hear something from the bathroom? Is she in there?"
    scene fs waitressbang7
    "Waitress" "Oh yes!"
    "Waitress" "Yes!!"
    scene fs waitressbang8
    "Waitress" "God you're so big!"
    scene fs waitressbang9 with hpunch
    "Waitress" "AHN!"
    "Waitress" "Fuck me!"
    player "Yeah you like taking this fat cock don't you bitch?"
    scene fs waitressbang10
    "Waitress" "EHNNNN!!"
    player "That's right! Fucking cum while I'm inside you!"
    scene fs waitressbang11
    with Dissolve(0.5)
    "Waitress" "Mmmm."
    player "There's a good girl..."
    scene fs waitressbang12 with vpunch
    "Waitress" "UGGHK!"
    player "Ah shit! Fucking take it all that's right."
    scene fs waitressbang13
    with Dissolve(0.7)
    pause
    scene fs waitressbang14
    pause
    scene fs waitressbang15
    pause
    pause
    scene fs waitressbang16
    sophia "{i}WHAT THE HELL??!!!{/i}"

    $ sophiaphase2interaction3 = 1
    $ sophiaquestlog = "That waitress was a good fuck, I need some sleep"
    jump passtime

# part 2

label sophiaphase2interaction3part2:
    hide screen uppergui
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonROOM
    scene fs playerbedsmile
    with Dissolve(0.7)
    player "{i}Ahhh this'll be a good sleep.{/i}"
    scene fs blackblank
    with Dissolve(0.7)
    player "{i}That waitress was a good fuck. Not bad for an impromptu session{/i}"
    "*tink* *Creak*"
    player "{i}My front door just unlocked and opened.{/i}"
    player "{i}But who would...{/i}"
    player "{i}Sophia!{/i}"
    scene fs sophiasneakysex1
    with Dissolve(0.7)
    sophia "Thinks he can just cheat on Mia with some random girl and not me?"
    sophia "I'm totally going to hold him down an-"
    scene fs sophiasneakysex2
    play sound "audio/light-switch.wav"
    pause
    sophia "....."
    sophia "How did you turn on the light while sitting down?"
    scene fs sophiasneakysex2b
    player "I'm not happy to see you Sophia."
    scene fs sophiasneakysex2c
    sophia "Uh..l-listen I um."
    scene fs sophiasneakysex2b
    player "Not happy at all."
    scene fs sophiasneakysex2c
    sophia "T-This isn't what it looks like!"
    scene fs sophiasneakysex3
    with Dissolve(0.5)
    player "It seems like."
    "*Taking off clothes sound*"
    player "You just won't get it."
    scene fs sophiasneakysex4 with hpunch
    voice "audio/sophiagameaudio/sophiaguh.wav"
    player "WILL YOU?!"
    sophia "Uhn?"
    player "You-"
    scene fs sophiasneakysex5 with hpunch
    player "STUPID"
    voice "audio/sophiagameaudio/sophiasexyoh.wav"
    sophia "AHN!"
    scene fs sophiasneakysex6
    pause
    scene fs sophiasneakysex5 with hpunch
    player "LITTLE."
    voice "audio/sophiagameaudio/sophiaguh.wav"
    sophia "GUH!"
    scene fs sophiasneakysex6
    pause
    scene fs sophiasneakysex5 with hpunch
    player "WHORE."
    voice "audio/sophiagameaudio/sophiamoanlaugh.wav"
    sophia "[povname]! Hhehehe.."

    show sophiawindowsex1
    play sound "audio/sophiagameaudio/sophiasexsounds1.wav" loop
    play secondsound "audio/sophiagameaudio/sophiasex1.wav"
    pause
    sophia "Hah..hah..hah."
    player "Finally getting what you wanted huh?"
    sophia "Hah.."
    player "Hope this dick was worth betraying your friends!"
    sophia "I..hah?"
    player "You must really hate them huh? Must really hate Mia!"
    sophia "N-No!"
    stop sound
    stop secondsound
    show sophiawindowsex2    
    play sound "audio/sophiagameaudio/sophiasexsounds2.wav" loop
    play secondsound "audio/sophiagameaudio/sophiasex2.wav"
    player "I can see you smiling you liar!"
    sophia "Ahn!"
    sophia "I..hah...it-it's not!"
    stop sound
    stop secondsound
    scene fs sophiawindowsexcum
    with vpunch
    voice "audio/sophiagameaudio/sophiacuming.wav"
    sophia "AHHHH!"
    pause
    scene fs sophiasneakysex9
    with vpunch
    player "Ugh!"
    sophia "{i}Finally! F-Finally...f..final....{/i}"
    pause
    
    scene fs blackblank
    with Dissolve(1.0)
    pause
    player "{i}Well that didn't solve anything!{/i}"
    $ sophiaphase2interaction3 = 2
    if currentchapter >= 3:
        $ sophiaquestlog = "I have to not fuck Sophia out of anger again...is she at school?"
    else:
        $ sophiaquestlog = "I messed up. Rage fucking Sophia wasn't the plan...oh well."
    jump passtime

# end chapter 2
# end chapter 2 content

label sophiabeachchapter2end:
    hide screen mia_beach1
    hide screen mia_beach2
    hide screen mia_beach3
    hide screen sophia_beach
    hide screen charlotte_beach
    hide screen ava_beach
    hide screen emily_beach
    hide screen olivia_beach
    hide screen backbuttonBEACH

    scene fs sophiawaterthensex1
    "Ocean" "*Water noises*"
    sophia "Ahhh..."
    scene fs sophiawaterthensex2
    with Dissolve(0.7)
    player "Soph! Enjoying yourself?"
    scene fs sophiawaterthensex3
    sophia "Hey [povname]!"
    sophia "Yeah!"
    scene fs sophiawaterthensex2
    player "What'cha thinking about?"
    scene fs sophiawaterthensex3
    sophia "Oh you know, just how we're gonna break the news to Mia."
    sophia "How many kids we should have..stuff like that."
    scene fs sophiawaterthensex4
    player "...."
    #$ sophiaphase2interaction3 = 2
    if sophiaphase2interaction3 >= 2:
        "Would you like to end the day with Sophia?"
        menu:
            "Romance":
                jump sophiachapter2romance
            "Naughty":
                jump sophiachapter2naughty
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach

    label sophiachapter2romance:
        player "I...you..."
        sophia "Hmmm?"
        player "{i}I can't speak I'm so overcome with rage{/i}"
        sophia "Something the matter sweetie?"
        player "I'm going to do something Sophia. And I know you're probably gonna like it."
        sophia "Okay..."
        player "But I want you to know this is a punishment, I'm very angry."
        sophia "But I don't know wh-"
        scene fs sophiawaterthensex5
        sophia "Oh."
        sophia "He's gone."
        ava "Sophiiiiaaa!"
        scene fs sophiawaterthensex6
        with Dissolve(0.5)
        sophia "Hey guys!"
        scene fs sophiawaterthensex7
        ava "Where's [povname] I thought I saw him go into the water towards you?"
        sophia "I dunno. He kinda just left."
        scene fs sophiawaterthensex8
        with Dissolve(0.5)
        player "Hohoho Sophia."
        player "I'm gonna hate this so much."
        scene fs sophiawaterthensex9
        player "I mean you're. YOU'RE gonna hate this."
        scene fs sophiawaterthensex10
        player "Try and talk to your friends when I'm pussy deep in your...pussy."
        scene fs sophiawaterthensex13
        with Dissolve(0.5)
        sophia "{i}Wait is that him down there?{/i}"
        sophia "{i}What is he doing? He pulled down my bikini!{/i}"
        scene fs sophiawaterthensex10
        player "Hehehe."
        scene fs sophiawaterthensex11
        player "Bitch."
        scene fs sophiawaterthensex14
        with Dissolve(0.5)
        ava "You alright girl?"
        emily "Yeah you look a little off."
        scene fs sophiawaterthensex15
        sophia "Hah! Y-Yeah everythings fine!"
        scene fs sophiawaterthensex11
        with Dissolve(0.5)
        player"Mmmmm"
        player "{i}Even underwater I can tell how wet she is. What a slut.{/i}"
        scene fs sophiawaterthensex12
        with Dissolve(0.5)
        player "{i}Let's add a little more stimulation.{/i}"
        scene fs sophiawaterthensex15
        sophia "{i}Oh God he's gonna m-make me!{/i}"
        sophia "{i}I can't cum in front of the girls! I gotta think of a plan quick!{/i}"
        ava "You're SURE you're alright?"
        emily "Maybe we should have a closer look at you?"
        sophia "Nonono I'm fine!"
        sophia "Look hey! Let's play a game, best orgasm face wins I'll go first!"
        emily "What?"
        scene fs sophiawaterthensex16
        sophia "Ahhhn!!!"
        sophia "I f-feel another one cumming! Y-You guys try!"
        ava "No I'm good you little weirdo. We should go see how everyone else is doing."
        emily "Um yeah Sophia, we'll see you later. Tell us if you find [povname]."
        scene fs sophiawaterthensex17
        with Dissolve(0.5)
        sophia "Ahh! FFFFFuck!"
        scene fs sophiawaterthensex12
        with Dissolve(0.5)
        player "Damn she's really cumming hard!"
        player "I should go back up now though. Before I drown."
        scene fs sophiawaterthensex2
        with Dissolve(0.7)
        player "There...hah..."
        player "Learn your lesson?"
        sophia "We....should come to the beach more often?"
        player "....."
        stop music
        stop sound
        play music "audio/showersounds.wav"
        show sophiachapter2sex movie1
        sophia "Ahn ahn ahn!"
        player "WE."
        player "ARE."
        player "NOT."
        player "A COUPLE!"
        show sophiachapter2sex movie2
        sophia "Oh my god [povname] I'm cumming I'm cumming!"
        player "How many times do I have to fuck you to understand!?"
        sophia "A-A lot! SO MANY TIMES!"
        player "THEN THAT'S WHAT I'll DO!"
        show sophiachapter2sex movie3
        sophia "AHHHH!"
        player "Looks like your little pussy couldn't hold all my cum."
        sophia "Uggghhh."
        player "{i}She's totally out of it. Oh well. {/i}"
        player "{i}God her pussy actually feels amazing...{/i}"
        pause
        scene fs blackblank
        with Dissolve(1.0)

        $ endchapter2_trigger = "2 sophia romantic"
        $ sophiaquestlog = "I have to not fuck Sophia out of anger again...is she at school?"
        jump startofchapter3

    label sophiachapter2naughty:
        player "I...you..."
        sophia "Hmmm?"
        player "{i}I can't speak I'm so overcome with rage{/i}"
        sophia "Something the matter sweetie?"
        player "I'm going to do something Sophia. And I know you're probably gonna like it."
        sophia "Okay..."
        player "But I want you to know this is a punishment, I'm very angry."
        sophia "But I don't know wh-"
        scene fs sophiawaterthensex5
        sophia "Oh."
        sophia "He's gone."
        ava "Sophiiiiaaa!"
        scene fs sophiawaterthensex6
        with Dissolve(0.5)
        sophia "Hey guys!"
        scene fs sophiawaterthensex7
        ava "Where's [povname] I thought I saw him go into the water towards you?"
        sophia "I dunno. He kinda just left."
        scene fs sophiawaterthensex8
        with Dissolve(0.5)
        player "Hohoho Sophia."
        player "I'm gonna hate this so much."
        scene fs sophiawaterthensex9
        player "I mean you're. YOU'RE gonna hate this."
        scene fs sophiawaterthensex10
        player "Try and talk to your friends when I'm pussy deep in your...pussy."
        scene fs sophiawaterthensex13
        with Dissolve(0.5)
        sophia "{i}Wait is that him down there?{/i}"
        sophia "{i}What is he doing? He pulled down my bikini!{/i}"
        scene fs sophiawaterthensex10
        player "Hehehe."
        scene fs sophiawaterthensex11
        player "Bitch."
        scene fs sophiawaterthensex14
        with Dissolve(0.5)
        ava "You alright girl?"
        emily "Yeah you look a little off."
        scene fs sophiawaterthensex15
        sophia "Hah! Y-Yeah everythings fine!"
        scene fs sophiawaterthensex11
        with Dissolve(0.5)
        player"Mmmmm"
        player "{i}Even underwater I can tell how wet she is. What a slut.{/i}"
        scene fs sophiawaterthensex12
        with Dissolve(0.5)
        player "{i}Let's add a little more stimulation.{/i}"
        scene fs sophiawaterthensex15
        sophia "{i}Oh God he's gonna m-make me!{/i}"
        sophia "{i}I can't cum in front of the girls! I gotta think of a plan quick!{/i}"
        ava "You're SURE you're alright?"
        emily "Maybe we should have a closer look at you?"
        sophia "Nonono I'm fine!"
        sophia "Look hey! Let's play a game, best orgasm face wins I'll go first!"
        emily "What?"
        scene fs sophiawaterthensex16
        sophia "Ahhhn!!!"
        sophia "I f-feel another one cumming! Y-You guys try!"
        ava "No I'm good you little weirdo. We should go see how everyone else is doing."
        emily "Um yeah Sophia, we'll see you later. Tell us if you find [povname]."
        scene fs sophiawaterthensex17
        with Dissolve(0.5)
        sophia "Ahh! FFFFFuck!"
        scene fs sophiawaterthensex12
        with Dissolve(0.5)
        player "Damn she's really cumming hard!"
        player "I should go back up now though. Before I drown."
        scene fs sophiawaterthensex2
        with Dissolve(0.7)
        player "There...hah..."
        player "Learn your lesson?"
        sophia "We....should come to the beach more often?"
        player "....."
        stop music
        stop sound
        play music "audio/showersounds.wav"
        show sophiachapter2sex movie1
        sophia "Ahn ahn ahn!"
        player "TAKE IT YOU STUPID SLUT!"
        player "We're here on a trip with my GIRLFRIEND."
        player "And you're fantasizing about us again??"
        sophia "AHHHH!"
        player "I can feel you getting tighter! Jesus Christ!"
        show sophiachapter2sex movie2
        sophia "[povname]![povname]![povname]!"
        player "How much of a whore are you huh? You just don't care!"
        sophia "C-Cummming!!!"
        show sophiachapter2sex movie3
        sophia "AHHHN!!"
        player "That's right cum on my fat dick!"
        player "That's all that matters to you right??"
        sophia "Uggghhh."
        player "{i}She's totally out of it. Nothing will get through to her now. {/i}"
        player "{i}I can't tell her how good her pussy actually feels..{/i}"
        pause
        scene fs blackblank
        with Dissolve(1.0)
        $ endchapter2_trigger = "2 sophia naughty"
        $ sophiaquestlog = "I have to not fuck Sophia out of anger again...is she at school?"

        jump startofchapter3

# start chapter 3

# Chapter 3 and related character scenes.

label sophiaphase3interaction1part1:
    hide screen sophia_atschool
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbsophia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ sophiaSprite = 1
    $ playerSprite = 14
    sophia "Hiiiii [povname]."
    $ sophiaSprite = 0
    $ playerSprite = 15
    player "*sigh*"
    player "Hey Soph."
    $ playerSprite = 14
    $ sophiaSprite = 1
    sophia "What'chu up to loverbooooy?"
    $ sophiaSprite = 0
    $ playerSprite = 15
    player "I don't know."
    player "Hoping to run into Mia."
    $ playerSprite = 14
    $ sophiaSprite = 2
    sophia "Ah."
    $ sophiaSprite = 10
    $ playerSprite = 15
    player "She's not here so I'll check the hallway."
    $ playerSprite = 14
    hide fbplayer current
    $ sophiaSprite = 1
    sophia "Wait!"
    hide fbsophia current
    scene fs schoolhallway
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbsophia current:
        xalign 0.2 xzoom -1.0 ypos 120
    with Dissolve(0.5)
    sophia "I'll help! I think she went to the bathroom."
    $ sophiaSprite = 0
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ avaSprite = 1
    ava "Heyo."
    $ avaSprite = 0
    $ playerSprite = 1
    $ sophiaSprite = 10
    player "Ava!"
    player "How you doing what's up?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Just came back from a run around the track."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Ah, just keeping your legs warm?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Haha yeah!"
    $ avaSprite = 0
    sophia "...."
    $ avaSprite = 1
    ava "So what are you two doing?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "I'm looking for Mia, just wanted to give her a little surprise."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Aww. Cute."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Haha."
    $ playerSprite = 0
    sophia "...."
    $ avaSprite = 1
    ava "You know her birthday's coming up in a month, you know what you're gonna get her?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "You know I actually have the perfect idea?"
    $ playerSprite = 0
    scene fs sophiahallwayzoom1
    with Dissolve(1.0)
    player "Azhum ba loopa. Cama sa?"
    ava "Shoooma blah cuba cuba."
    scene fs sophiahallwayzoom2
    with Dissolve(1.0)
    player "Hahaha shuuuno koomba."
    ava "Ahhh. Zimtuba dupo."
    player "Dupo."
    ava "Zobia?"
    ava "ZOBIA?!"
    ava "SOPHIA!"
    $ sophiaSprite = 7
    $ avaSprite = 15
    $ playerSprite = 11

    scene fs schoolhallway

    show fbplayer current:
        xalign 0.4 xzoom -1.0 ypos 120
    show fbsophia current:
        xalign 0.2 xzoom -1.0 ypos 120
    show fbava current:
        xalign 0.7 ypos 120
    sophia "HUH?!"
    sophia "What?"
    $ sophiaSprite = 10
    $ avaSprite = 16
    ava "Dude you okay?"
    $ avaSprite = 15
    $ sophiaSprite = 2
    sophia "Um yeah I'm..."
    $ sophiaSprite = 10
    $ miaSprite = 1
    show fbmia current:
        xalign 0.6 ypos 120
    mia "Hello friends!"
    $ avaSprite = 0
    $ miaSprite = 0
    $ sophiaSprite = 10
    show fbplayer current:
        xalign 0.4 xzoom 1.0 ypos 120
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Mia!"
    $ avaSprite = 0
    $ sophiaSprite = 2
    sophia "Fine..."
    $ sophiaSprite = 10
    $ miaSprite = 1
    mia "[povname]!"
    $ miaSprite = 0
    $ playerSprite = 10
    player "Surprise! No gift though sorry."
    $ playerSprite = 0
    hide fbplayer current
    show fbmia mcmiamakeout:
        xalign 0.4 ypos 120
    mia "Mmmmm!"
    show fbmia current:
        xalign 0.5 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ miaSprite = 4
    mia "YOU'RE my gift!"
    $ miaSprite = 0
    $ avaSprite = 1
    ava "Awww. Again."
    $ avaSprite = 0
    $ sophiaSprite = 2
    show fbsophia current:
        xalign 0.1
    with move
    sophia "I'm...gonna go guys I got something..."
    show fbplayer current:
        xalign 0.35 xzoom -1.0 ypos 120
    sophia "Something to do."
    $ sophiaSprite = 10
    $ avaSprite = 16
    ava "You sure you're good?"
    $ avaSprite = 15
    $ sophiaSprite = 2
    sophia "Yeah I'll see you later."
    $ sophiaSprite = 10
    $ miaSprite = 1
    mia "Oh before you go Sophia."
    $ miaSprite = 0
    show fbmia current:
        xalign 0.22
    with move
    sophia "Hmm?"
    $ miaSprite = 4
    mia "I just wanna say your recipe for the butterscotch cookies was AMAZING!"
    $ miaSprite = 0
    $ sophiaSprite = 2
    sophia "Really?"
    $ sophiaSprite = 10
    $ miaSprite = 1
    mia "Even my MOM admitted it was better than hers hehe."
    mia "Don't tell her I said that though."
    $ sophiaSprite = 0
    mia "I just wanted to say thanks!"
    $ miaSprite = 0
    pause
    $ sophiaSprite = 10
    sophia "..."
    $ sophiaSprite = 2
    sophia "Okay. Thank you."
    sophia "I'm...really sorry Mia."
    $ sophiaSprite = 10
    mia "Hmm?"
    $ sophiaSprite = 2
    sophia "Bye."
    hide fbsophia current
    with Dissolve(0.5)
    $ avaSprite = 1
    ava "Bye!"
    $ avaSprite = 1
    $ playerSprite = 1
    player "See yah."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Bye Sophia!"
    $ miaSprite = 0
    $ sophiaSprite = 0
    $ sophiaphase2interaction3 = 3
    $ sophiaphase3interaction1 = 1
    $ sophiaquestlog = "Was nice to just talk to everyone together. Sophia seemed a little down near the end though."
    jump passtime

label sophiaphase3interaction1part2:
    scene fs playerbedneutral
    with Dissolve(0.7)
    pause
    scene fs playerbedthink1
    player "{i}Hmmm.{/i}"
    player "{i}Should I try out pickleball?{/i}"
    scene fs playerbedthink2
    pause
    player "{i}Naw.{/i}"
    scene fs playerbedneutral
    player "*sniff sniff*"
    player "{i}Man I need to take a shower or a bath or something{/i}"
    "Briiiing Briiiiing"
    scene fs playerbedphone
    player "Who's video calling?"
    scene fs sophiabathtime1
    pause
    scene fs sophiabathtime2
    "*Bring*"
    sophia "Hello!"
    player "Sophia hey!"
    scene fs sophiabathtime3
    sophia "How are you?"
    scene fs sophiabathtime3b
    player "I'm doing good, was about to head to sleep but decided to take a bath first."
    scene fs sophiabathtime4
    sophia "A bath?"
    sophia "I thought guys don't take baths."
    scene fs sophiabathtime3b
    player "It's rare but yeah we like a good soak every so often."
    scene fs sophiabathtime3
    sophia "Hehe okay."
    scene fs sophiabathtime3b
    player "You doing alright? Kinda left in a hurry earlier."
    scene fs sophiabathtime3
    sophia "Yeah I'm fine now, just needed a little offscreen contemplation."
    scene fs sophiabathtime3b
    player "Okay well that's good."
    player "Not to cut us short but it's getting late and I'm gonna have that bath now."
    scene fs sophiabathtime4
    sophia "Hmmm."
    scene fs sophiabathtime2
    sophia "Yeah okay, enjoy!"
    scene fs sophiabathtime3b
    player "See yah."
    scene fs sophiabathtime1
    "*Click*"
    scene fs blackblank
    with Dissolve(0.5)
    "A little while and a few less clothes later.."
    scene fs sophiabathtime5
    with Dissolve(1.0)
    player "Mmmm."
    player "{i}I gotta take these more often.{/i}"
    pause
    "...."
    scene fs sophiabathtime6
    pause
    sophia "...."
    scene fs sophiabathtime6b
    player "Ugh. I can tell you're there Sophia."
    scene fs sophiabathtime7
    with Dissolve(0.7)
    sophia "Um hi..."
    scene fs sophiabathtime7b
    player "Why are you here Soph?"
    scene fs sophiabathtime7c
    sophia "I'm not here to like.."
    sophia "It's not like last time."
    scene fs sophiabathtime7b
    player "I have a hard time believing that when I can see your bare pussy right in front of me."
    scene fs sophiabathtime7c
    sophia "I'm not I swear. I've been thinking about things.."
    sophia "I feel bad. I realized I've been stressing you out for my own...desires."
    scene fs sophiabathtime7
    player "...."
    scene fs sophiabathtime7b
    player "So why are you naked, and here?"
    scene fs sophiabathtime7c
    sophia "I wanted to bond, like we used to when we were little."
    scene fs sophiabathtime7b
    player "By taking a Bath with me? A very naked bath?"
    scene fs sophiabathtime7c
    sophia "I figured any other attempt, you'd brush me off."
    sophia "But you can't walk away in here and...and I really don't want to lose you."
    scene fs sophiabathtime7
    player "...."
    scene fs sophiabathtime7b
    player "Haaa....get in here."
    scene fs sophiabathtime8
    with Dissolve(1.0)
    pause
    scene fs sophiabathtime8sophia
    sophia "Thank you."
    sophia "I appreciate you giving me a chance."
    scene fs sophiabathtime8mc
    player "Yeah well, you seemed sincere for once."
    player "And if anyone found out I'll just say you held me down or something."
    scene fs sophiabathtime8
    player "{i}I can lie to her, but I can't lie to myself that everything we've been doing hasn't really turned me on{/i}"
    scene fs sophiabathtime8sophia
    sophia "I am, but I don't think anyone would believe you haha."
    sophia "I don't think three of me could hold you down."
    scene fs sophiabathtime8
    player "{i}Admitting how I feel after how I've treated her would really just complicate things..{/i}"
    scene fs sophiabathtime8mc
    player "Three of you? Now there's a thought."
    scene fs sophiabathtime8sophia
    sophia "Heh I don't know if that's a compliment or-"
    sophia "...I feel some-"
    scene fs sophiabathtime9
    with Dissolve(0.5)
    pause
    scene fs sophiabathtime10
    with Dissolve(0.5)
    pause
    scene fs sophiabathtime10b
    sophia "I-I swear that wasn't me, I didn't mean to-"
    player "It's fine."
    scene fs sophiabathtime10c
    player "T-This time it's all uh, me sorry hehe.."
    player "Beautiful girl. Naked. On top of me. Bound to happen, it's natural."
    sophia "O-Okay!"
    player "We should just try to relax again."
    sophia "Sure!"
    scene fs sophiabathtime10d
    with Dissolve(0.5)
    pause
    sophia "{i}Don't do it Sophia. Don't do it. Don't do it.{/i}"
    pause
    sophia "{i}Don't you do it!!"
    pause
    scene fs sophiabathtime11
    with Dissolve(1.0)
    pause
    player "...."
    scene fs sophiabathtime11b
    with Dissolve(0.7)
    player "Mphm."
    scene fs sophiabathtime11
    with Dissolve(0.7)
    pause
    scene fs sophiabathtime12
    with Dissolve(0.7)
    player "Hah.."
    sophia "Ahn."
    scene fs sophiabathtime11
    with Dissolve(0.7)
    pause
    scene fs sophiabathtime13
    with vpunch
    pause
    sophia "Ahn ahn ahn!"
    player "Agh!"
    pause
    scene fs sophiabathtime14
    with vpunch
    player "Fuck!"
    sophia "Oh GOD!"
    scene fs sophiabathtime15
    with Dissolve(0.5)
    pause
    scene fs sophiabathtime15b
    sophia "Hah...haha."
    sophia "I came and then..y-you came."
    sophia "It's all over me.."
    scene fs sophiabathtime15c
    sophia "Wait no, this is bad this is-"
    sophia "[povname] doesn't want this."
    player "No Sophia it's okay this time. My fault."
    sophia "Oh.."
    pause
    scene fs blackblank
    with Dissolve(1.0)
    player "Soph?"
    sophia "Yeah?"
    player "Do you want to go on a date with me? A proper date."
    player "I think we need to sort our feelings out."
    sophia "I would...love that."
    $ sophiaphase3interaction1 = 2
    $ sophiaquestlog = "No more Sophia content for this version (ch2.5)"
    jump passtime
