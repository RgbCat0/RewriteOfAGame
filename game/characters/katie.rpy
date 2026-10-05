# Katie scenes.

label conversationkatie1:
    $ katieconversationday = dayNumber
    player "{cps=25}Hey.{/cps}"
    katie "{cps=25}Oh? Texting me already huh?{/cps}"
    katie "{cps=25}That didn't take too long.{/cps}"
    player "{cps=25}Sorry I messaged you by accident!{/cps}"
    katie "{cps=25}Lol if you say so.{/cps}"
    jump returnwhereyouare


label conversationkatie2:
    if katieconversationday == dayNumber:
        player "I already texted her I should wait until tomorrow at least..."
        jump returnwhereyouare
    else:
        $ katieconversation = 2
        player "{cps=25}What's up?{/cps}"
        katie "{cps=25}Once is an accident, twice not so much.{/cps}"
        player "{cps=25}It really was I swear!{/cps}"
        katie "{cps=25}Suuuuure.{/cps}"
        katie "{cps=25}Well since I have you here, how's my sis in bed?{/cps}"
        player "{cps=25}I'm not telling you that.{/cps}"
        katie "{cps=25}C'mon! I'm basically just a fun sized version of her I'm only curious.{/cps}"
        katie "{cps=25}We even have the same sized tits!{/cps}"
        player "...."
        player "{cps=25}Not sayin.{/cps}"
        katie "{cps=25}Alright fine you're no fun.{/cps}"
        katie "{cps=25}Different question then.{/cps}"
        katie "{cps=25}What do you like most about her?{/cps}"
        player "....."
        player "{cps=25}Her tits.{/cps}"
        katie "{cps=25}Interesting.{/cps}"
        katie "{cps=25}You do know I JUST said we're pretty much equal in that regard?{/cps}"
        player "{cps=25}Yeah.{/cps}"
        katie "{cps=25}I take it back. You ARE fun.{/cps}"
        $ katieconversationday = dayNumber
        jump returnwhereyouare


label conversationkatie3:
    if katieconversationday == dayNumber:
        player "I already texted her I should wait until tomorrow at least..."
        jump returnwhereyouare
    else:
        $ katieconversation = 3
        player "Fuck what am I doing...."
        player "{cps=25}Hey Katie.{/cps}"
        katie "{cps=25}Haha you just can't get enough huh?{/cps}"
        player "{cps=25}I just wanna talk.{/cps}"
        katie "{cps=25}Yeah, like your cock isn't in your hand right now.{/cps}"
        player "....."
        katie "{cps=25}I know what you want, here I'll even help you...{/cps}"
        katie "{cps=25}I love it when a guy grabs my waist from behind and just fucks me senseless in front of a mirror so he can see my big tits bouncing as he pounds me.{/cps}"
        player "Jesus Christ...I can't ever let Mia see my phone..."
        katie "{cps=25}That something you'd be into doing?{/cps}"
        player "{cps=25}.....Yes.{/cps}"
        katie "{cps=25}With my sister of course ;){/cps}"
        player "{cps=25}Of course.{/cps}"
        katie "{cps=25}Knew you'd agree.{/cps}"
        $ katieconversationday = dayNumber
        jump returnwhereyouare


label conversationkatie4:
    if katieconversationday == dayNumber:
        player "I already texted her I should wait until tomorrow at least..."
        jump returnwhereyouare
    else:
        hide screen questboxpreview
        $ katieconversation = 4
        player "{cps=25}Katie?{/cps}"
        katie "{cps=25}Wow here we are again, you should be rewarded for your tenacity don't you think?{/cps}"
        player "....."
        katie "{cps=25}You aren't getting anything unless you respond.{/cps}"
        katie "{cps=25}What do you want?{/cps}"
        player "{cps=25}I want to be rewarded.{/cps}"
        katie "{cps=25}Good boy.{/cps}"
        katie "{cps=25}I'm a little busy right now so this'll have to do.{/cps}"
        katie "{cps=25}Sent.{/cps}"
        katie "{cps=25}Don't tell big sis ;){/cps}"
        player "I should check my images to see what she sent."
        $ renpy.notify("Got Katie's Selfie!")
        $ phone_pictures.append("katiebathselfie")
        $ katieconversationday = -1
        if currentchapter > 1:
            $ katiequestlog = "Maybe I should stop by Katie's room?"
        else:
            $ katiequestlog = "Katie is a naughty girl for sure, I should keep my distance for now.."

        jump returnwhereyouare


label conversationkatie5:
    player "I might get in trouble if I text her anymore..."
    jump returnwhereyouare


# Chapter 2


label katiefootmassage:
    hide screen backbuttonGFHALLWAY
    hide screen uppergui
    "You take a deep breath before you walk into Katie's room"
    player "{i} You got this [povname]. Just be confident, it takes a strong personality to handle a strong personality!{/i}"
    scene fs katiefootmassage1
    with Dissolve(1.0)

    player "Hey Katie."

    scene fs katiefootmassage1b2
    katie "Oh hey [povname], I knew you'd come."
    scene fs katiefootmassage1
    player "{i}Man it is bright and girly in here.{/i}"
    player "{i}There's...the mirror she mentioned.{/i}"
    scene fs katiefootmassage1b
    katie "To be honest, I was half hoping you wouldn't show up."
    scene fs katiefootmassage1b2
    katie "Don't think I can tie you down with my feet feeling like this."
    scene fs katiefootmassage1
    player "Hah, lucky me. I came because I wanted to."
    scene fs katiefootmassage1b2
    katie "Hehe, I do have that effect on boys."
    scene fs katiefootmassage2mc
    with Dissolve(0.7)
    player "Very funny."
    scene fs katiefootmassage2katie
    katie "Uhhh what are you doing?"
    scene fs katiefootmassage2mc
    player "I'm gonna give you a massage, should help you feel better."
    scene fs katiefootmassage2katie
    katie "What? You one of those guys with a foot fetish?"
    scene fs katiefootmassage2mc
    player "No not really, I mean you do have pretty feet but.."
    scene fs katiefootmassage2katie
    katie "But?"
    scene fs katiefootmassage3mc
    with Dissolve(0.7)
    player "But everything about you is pretty."
    scene fs katiefootmassage3katieoh
    katie "Oh."
    scene fs katiefootmassage3katie
    katie "Well okay then massage away."
    image katiefoot katiefootrub1:
        "22-3katie.png"
        0.7
        "22-3katie2.png"
        0.7
        repeat

    image katiefoot katiefootrubmc1:
        "22-3mcface2a.png"
        0.7
        "22-3mcface2b.png"
        0.7
        repeat

    image katiefoot katiefootrub2:
        "22-3katieface2a.png"
        0.7
        "22-3katieface2b.png"
        0.7
        repeat

    image katiefoot katiefootrub3:
        "22-4.png"
        0.7
        "22-4b.png"
        0.7
        repeat


    image katiefoot katiefootrub4:
        "22-5.png"
        0.7
        "22-5b.png"
        0.7
        "22-5c.png"
        0.7
        "22-5d.png"
        0.7
        repeat

    image katiefoot katiefootrub5:
        "22-6.png"
        0.9
        "22-6B.png"
        0.9
        repeat

    image katiefoot katiefootrub6:
        "22-7.png"
        0.9
        "22-7B.png"
        0.9
        repeat


    show katiefoot katiefootrub1
    pause
    katie "Mmmm that does feel really good."
    show katiefoot katiefootrubmc1
    player "I'm glad."
    show katiefoot katiefootrub1
    player "{i}Shit I can totally see up her skirt!{/i}"
    player "{i}Stay calm...use your poker face and focus on the massage..{/i}"
    katie "So why are you really here?"
    show katiefoot katiefootrubmc1
    player "What do you mean?"
    show katiefoot katiefootrub1
    katie "No matter how nice-"
    show katiefoot katiefootrub2
    katie "Ooooohh yeah right there."
    show katiefoot katiefootrub1
    katie "How nice a guy is he doesn't offer his girlfriend's sister a foot massage when she's not there."
    katie "You get off on her being in the next room or something?"
    show katiefoot katiefootrubmc1
    player "No I-"
    scene fs katiefootmassage3face3
    with vpunch
    katie "Uhhhn!"
    katie "Fuck you really good at this!"
    player "{i}She's gotta be doing this on purpose to mess with me..{/i}"
    show katiefoot katiefootrubmc1
    with Dissolve(0.5)
    player "I'm glad you like it but can you not moan like that?"
    show katiefoot katiefootrub1
    katie "Can't help it, it just feels SO...GOOD."
    player "Stay strong stay strong! No emotions!"
    show katiefoot katiefootrubmc1
    player "I wanted to talk."
    show katiefoot katiefootrub1
    katie "Mmmm, to talk?"
    show katiefoot katiefootrubmc1
    player "About...the picture you sent, our texts."
    show katiefoot katiefootrub1
    katie "Oh that? Heh I should've known. Not a bad pic huh? It was hard getting that angle just right."
    show katiefoot katiefootrubmc1
    player "Why did you send it?"

    show katiefoot katiefootrub3

    katie "Mmmmm! A-Aside from how obvious it was that you wanted me to send you something naughty?"
    scene fs katiefootmassage3b
    player "Uh...no comment."
    player "Other leg please."
    show katiefoot katiefootrub4
    katie "Hah...hah.."
    katie "C'mon [povname], no need to take it so seriously. I'm just having some fun."
    scene fs katiefootmassage5mc
    player "Don't you care about your sister?!"
    show katiefoot katiefootrub4
    katie "Of course I do, but sisters sometimes borrow things from each other. It's not a big deal if we just fool around a bit."
    scene fs katiefootmassage5mc
    player "I don't know Katie-"
    show katiefoot katiefootrub4
    katie "What are you in love with me or something?"
    scene fs katiefootmassage5mc
    player "What? No!"
    show katiefoot katiefootrub4
    katie "Then as long as feelings aren't involved what's the problem?"
    scene fs katiefootmassage5mc
    player "What if Mia finds out something?"
    show katiefoot katiefootrub4
    katie "Isn't...mmmm..isn't that the the whole point? The thrill of getting caught?"
    katie "God your hands are amazing."
    player "Thanks..."
    katie "Hehe, and from what I hear it's not the only amazing part of you is it?"
    show katiefoot katiefootrub5
    with Dissolve(0.7)
    player "Woah uh..."
    player "Katie hold on."
    katie "C'mon, let me repay the favor."
    player "I really...don't think..."
    show katiefoot katiefootrub6
    with Dissolve(0.7)
    katie "Ahh there we go.."
    player "Shit!"
    katie "Did you jerk off to it? The picture I sent?"
    katie "I'll know if you're lying by the way."
    player "Fuck Katie c'mon..."
    katie "This boner looks real painful. But how would you explain cumming in your pants in my room to Mia?"
    player "Okay Okay I did. I loved the picture it was great!"
    katie "Haha you really are just so much fun!"
    player "I'm just fun for you then?"
    katie "Yup! And as much as I would like to have even more of it with you. You should probably leave before my sister gets suspicious."
    katie "She's slow on the uptake but she's not an idiot."
    player "Okay yeah. I'm gonna go."
    katie "Awww don't worry, we'll have some more fun soon!"
    player "Uh...bye."
    katie "Hehe bye!"
    scene fs blackblank
    with Dissolve(1.0)
    player "{i}Shit well that was a complete failure."
    player "{i}I wanted to take some control in whatever kind of relationship we have but I think I just gave her even more of an edge."
    player "{i}She said it's not a big deal as long as feelings aren't involved. Hmm...{/i}"
    $ katiequestlog = "Trying to handle Katie is a tough job. I'm looking forward to some sleep."

    $ katiephase2interaction1 = 2
    jump miahousehallway


label katiesecondselfie:
    hide screen backbuttonROOM
    "VVVVVVVP VVVVVVP"
    player "Huh? That's my phone."
    katie "{cps=25}Hey there.{/cps}"
    player "{cps=25}Katie? What's up.{/cps}"
    katie "{cps=25}I just wanted to send you a little thank you again for the massage.{/cps}"
    player "{cps=25}Oh it was no problem.{/cps}"
    katie "{cps=25}Since you were staring at my panties so much I figured you would like this.{/cps}"
    player "{cps=25}I wasn't...{/cps}"
    katie "{cps=25}LOL sure. This one's bigger so check your email!{/cps}"
    katie "{cps=25}Have a good night!{/cps}"
    $ renpy.notify("New Picture Received!")
    player "Shit she seriously has the upper hand here."
    player "I gotta check my computer later to see what picture she sent me."
    $ katiequestlog = "I can look at Katie's email on my computer."
    $ katiephase2interaction1 = 3
    $ katiebjday = dayNumber
    jump playerRoom


label talkaboutpizzaparty:
    hide screen questboxpreview
    hide screen uppergui
    hide screen tonormalmap
    hide screen backbuttonOUTSIDEOFFICE
    player "Okay I gotta call Mia and ask to hang out together with Katie."
    player "God what am I getting myself into?"
    player "No. All I want is to hang out, I'm just being nice inviting Katie too."
    "Riiing Riiing"
    mia "Hey [povname]!"
    player "Mia!"
    mia "This is crazy timing haha."
    player "What you mean?"
    mia "Katie was JUST telling me that we should all do something together!"
    player "Oh...she did huh?"
    mia "Yeah yeah! I'm busy during the day but...what about a overnight pizza party!"
    player "Pizza sounds good."
    mia "Yeah it'll be comfy and fun!"
    player "Kinda like you!"
    mia "OH geez haha, okay see you tonight."
    mia "Love you!"
    player "Love you too."
    "*Click*"
    player "...."
    $ katiequestlog = "Mia and Katie are staying over tonight! Surely Katie won't try anything with Mia there.."
    $ katiephase2interaction1 = 5
    jump returnwhereyouare


label pizzapartykatiefuck:
    hide screen questboxpreview
    hide screen backbuttonLIVINGROOM
    hide screen uppergui
    scene fs livingroomnight
    with Dissolve(0.5)
    player "Alrighty they should be h-"
    "*Ding Dong*"
    mia "Hiiiii!"
    player "C'mon in!"
    scene fs miapizzatime1
    with Dissolve(0.7)
    "The three of you hung out for a bit and watched some bad TV movies"
    "Like Mia said, it was comfy and fun"
    scene fs miapizzatime2
    with Dissolve(0.7)
    "Then the pizza arrived and you realized how hungry you were"
    "There was a bit of dancing and lot of laughter"
    scene fs miapizzatime3
    with Dissolve(0.7)
    "As the night died down you resumed watching movies"
    "Eventually it got late enough that you all went to sleep..."
    scene fs katiefirstfuck1
    play sound "audio/miagameaudio/miasex1.wav" loop
    mia "Ahn ahn ahn!!!!"
    "Not before giving Mia a rough pounding first of course"
    scene fs katiefirstfuck2
    with Dissolve(1.0)
    stop sound fadeout 3
    pause
    scene fs katiefirstfuck3
    pause
    scene fs katiefirstfuck4
    pause
    player "Huh?"
    scene fs katiefirstfuck5b
    with Dissolve(0.5)
    katie "Hey."
    scene fs katiefirstfuck5
    player "Katie. You're lucky I can't move because it'll wake Mia."
    player "What are you doing?"
    scene fs katiefirstfuck5b
    katie "We both know this is where things were headed [povname]."
    katie "No use lying about it."
    scene fs katiefirstfuck5
    player "Katie Mia is RIGHT there!"
    scene fs katiefirstfuck6
    with Dissolve(0.5)
    katie "Relax I'm not gonna put it in. Look how hard you are I can just..."
    pause
    show katiefirstsex movie1
    katie "Sliiiide like this..."
    player "That...fuck...that isn't the issue here!"
    katie "C'mon [povname], isn't the chance of getting caught so hot?"
    katie "Your girlfriend's sister is naked and-"
    scene fs katiefirstfuck8
    mia "Wha?"
    katie "!!!"
    player "!!!"
    mia "Whosa...whashisname..."
    player "..."
    scene fs katiefirstfuck8b
    mia "Zzzz.."
    scene fs katiefirstfuck9
    katie "Holy shit."
    player "Katie."
    katie "This is so fucking hot."
    player "Katie no you said you weren't gonna-"
    show katiefirstsex movie2
    katie "MMMM!"
    katie "Oh my God yes!"
    player "Fuck!"
    pause
    show katiefirstsex movie3
    katie "AHN!!"
    player "PLEASE be more quiet!"
    katie "I know you want this!"
    katie "I know you want my tight little pussy [povname]!"
    player "Fuck fuck Katie I'm gonna cum!"
    show katiefirstsex movie4
    katie "NNNNHHHGH!!!"
    katie "Yes! Cum inside me while my big sister is right beside us!!!!"
    katie "Your cock feels so fucking good."
    pause
    scene fs katiefirstfuck13
    with Dissolve(0.7)
    katie "Hah...."
    katie "Hehehe!"
    player "Katie this...fuck...way too risky."
    katie "And yet, you absolutely filled me."
    katie "I can't wait to see what else we can get up to hehe."
    scene fs blackblank
    with Dissolve(0.7)
    player "Ah fuck.."
    pause
    $ katiephase2interaction1 = 6
    $ katiequestlog = "Can't believe I fucked Mia's sister...well she fucked me really."
    jump gotosleep


label katieblowjob:
    hide screen backbuttonROOM
    hide screen uppergui
    scene fs blackblank
    with Dissolve(1.0)
    pause
    scene fs katieblowjob1
    with Dissolve(0.7)
    julia "Alright girls I'm headed out!"
    katie "Sure thing mom."
    mia "Drive safe. See you tomorrow."
    julia "Enjoy your movie, and Katie please don't spread your legs like that."
    katie "Uh huh."
    julia "So unladylike..."
    scene fs katieblowjob2
    with Dissolve(0.7)
    katie "...."
    scene fs katieblowjob2c
    "*Movie noises*"
    scene fs katieblowjob2
    mia "*munch munch*"
    scene fs katieblowjob2a
    katie "Man this movie blows."
    scene fs katieblowjob3
    mia "I know, but I heard there's a really good sex scene in the middle."
    scene fs katieblowjob2a
    katie "I don't know if a sex scene could fix this trainwreck."
    katie "No matter how good it is."
    scene fs katieblowjob2
    "Movie" "I want to be with you! There's nobody else that's good enough for me!"
    scene fs katieblowjob3
    mia "Well we're getting close to it so we'll find out soon."
    scene fs blackblank
    with Dissolve(0.7)
    "5 minutes later..."
    scene fs katieblowjob2
    with Dissolve(0.5)
    "Movie" "Take me! Take me now!"
    scene fs katieblowjob2a
    katie "Yup here it is, looks like we're in for a show..."
    scene fs katieblowjob2
    pause
    scene fs katieblowjob4
    with Dissolve(1.0)
    "Movie" "Ahn ahn yes!!!"
    katie "Woah."
    "Movie" "Fuck me! FUCK MY PUSSY!"
    katie "I stand corrected."
    mia "...."
    "Movie" "Harder! Hold my legs behind my head!"
    katie "You wanna go to bed after this scene?"
    mia "Mhmm.."
    scene fs blackblank
    with Dissolve(1.0)
    scene fs katieblowjob5
    katie "Zzzz..."
    mia "{size=-10}Ahn...{/size}"
    scene fs katieblowjob6
    with vpunch
    mia "AHN!"
    katie "Hmm?"
    mia "Oh! Right there right there!"
    scene fs katieblowjob7
    with Dissolve(0.5)
    katie "Looks like Mia's having some nice alone time."
    player "You like this dick baby?"
    katie "Damn! Looks like it's not alone time at all."
    scene fs katieblowjob9
    with Dissolve(0.5)
    mia "Put my legs above my head!"
    player "I'm so fucking hard Mia."
    mia "Seems like that movie really got her riled up haha."
    show katieblowjob1 movie1
    katie "Mmmm, talking dirty like that is getting me all horny..."
    mia "Ahn ahn!"
    "*Smack smack smack smack*"
    mia "AHHHN!! YES!!"
    scene fs katieblowjob10
    with Dissolve(0.5)
    katie "Fuck this sounds hot!"
    mia "I'm GONNA CUM!"
    player "Damn baby already?!"
    mia "YESYESYESYESYES!!"
    with vpunch
    mia "AHHHHHH!"
    player "Fuck yes Mia I love it when you cum on my cock!"
    player "...."
    scene fs katieblowjob11
    player "Mia?"
    katie "?"
    mia "*Snore*"
    player "Are you serious??"
    katie "Did she seriously fall asleep?"
    mia "Zzzzz..."
    katie "That must've been one hell of an orgasm."
    player "Babe c'mon, I'm still rock hard here!"
    player "....Shit."
    "*Door squeak*"
    scene fs katieblowjob12
    with Dissolve(0.5)
    katie "Oh? Looks like the boyfriend has a case of blue balls hehe."
    katie "Sounds like he went into the bathroom. Maybe I should help him out."
    scene fs miabathroom
    with Dissolve(1.0)
    show fbplayer underwearbonerfrowntalk:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    player "Shit, what should I do now?"
    player "She called me in the middle of the night to tell me to come over."
    player "But she was so apparently horny she passed right out after cumming."
    player "I don't know if I should be proud of myself or pissed."
    player "Should I just jack off in here?"
    show fbkatie undiestalk:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    katie "Wow, what a sentence to walk into."

    show fbkatie undies:
        xalign 0.6 ypos 120
    show fbplayer underwearbonershock:
        xalign 0.4 ypos 120
    with vpunch
    player "!!"
    show fbplayer underwearbonerweaksmiletalk:
        xalign 0.4 ypos 120
    player "K-Katie hey! What are you doing here? I thought you were sleeping."
    show fbplayer underwearbonerweaksmile:
        xalign 0.4 ypos 120
    show fbkatie undiestalk:
        xalign 0.6 ypos 120
    katie "Yeah kinda hard to sleep when you two were being so...loud."
    show fbplayer underwearbonerweaksmiletalk:
        xalign 0.4 ypos 120
    show fbkatie undies:
        xalign 0.6 ypos 120
    player "Ah haha..Sorry."
    show fbplayer underwearbonerweaksmile:
        xalign 0.4 ypos 120
    show fbkatie undiestalk:
        xalign 0.6 ypos 120
    katie "It's alright. It kinda turned me on to be honest."
    katie "My nips are rock hard and pussy's soakin wet."
    player "{i}Jesus help me.{/i}"
    katie "But I think, between the two of us you're the hornier one."
    show fbkatie undies:
        xalign 0.6 ypos 120
    show fbplayer underwearbonerweaksmiletalk:
        xalign 0.4 ypos 120
    player "Whaaat? Haha no no.."
    show fbplayer underwearbonerweaksmile:
        xalign 0.4 ypos 120
    show fbkatie undiespointtalk:
        xalign 0.5 ypos 120
    with move
    katie "Dude your boner is, literally raging."
    katie "Seems like my sister gave you a good ol' case of the blue balls huh?"
    show fbkatie undies:
        xalign 0.5 ypos 120
    show fbplayer underwearbonerweaksmiletalk:
        xalign 0.4 ypos 120
    player "Even if she did..."
    show fbplayer underwearbonerweaksmile:
        xalign 0.4 ypos 120
    show fbkatie undiestalk:
        xalign 0.45 ypos 120
    with move
    katie "I can help you out you know? Like, I REALLY want to help you out."
    show fbkatie undies:
        xalign 0.45 ypos 120
    show fbplayer underwearbonerweaksmiletalk:
        xalign 0.35 ypos 120
    with move
    player "Katie...I really appreciate it but.."
    show fbplayer underwearbonerweaksmile:
        xalign 0.35 ypos 120
    show fbkatie undiestalk:
        xalign 0.45 ypos 120
    katie "Hehe."
    katie "How about this? I'm gonna get down on my knees and suck your balls."
    show fbkatie undies:
        xalign 0.45 ypos 120
    show fbplayer underwearbonerblushtalk at surpriseshake:
        xalign 0.35 ypos 120
    player "What??"
    show fbkatie undiestalk:
        xalign 0.45 ypos 120
    katie "And if at any point you wanna walk away...go ahead hehe."
    show fbkatie undies:
        xalign 0.45 ypos 120
    player "Uh..."
    show fbkatie undies:
        xalign 0.45 ypos 120
    scene fs blackblank
    with Dissolve(1.0)
    katie "Hands on your hips. You're not allowed to move."
    player "Katie!"
    scene fs katieblowjob13
    katie "Daaamn, i-it's even more impressive up close!"
    player "{i}I did not consent to this! That makes it alright.{/i}"
    scene fs katieblowjob14
    with Dissolve(0.5)
    katie "Let's take this off."
    player "{i}Right?{/i}"
    scene fs katieblowjob15
    pause
    scene fs katieblowjob16
    katie "Sweet fuck this thing is thick!"
    player "Katie c-can you keep it down?"
    katie "Pictures do not do it justice, Mia is so fucking lucky."
    scene fs katieblowjob17
    with Dissolve(0.5)
    katie "God I just wanna.."
    scene fs katieblowjob17b
    pause
    scene fs katieblowjob17
    pause
    scene fs katieblowjob17b
    katie "Do EVERYTHING with it."
    scene fs katieblowjob18
    katie "Wait."
    katie "I wonder what Mia's pussy tastes like."
    player "W-What?"
    katie "There must still be..."
    scene fs katieblowjob19
    with Dissolve(0.7)
    katie "Mmmm.."
    player "Oh fuck."
    show katieblowjob1 movie2
    with Dissolve(0.5)
    pause
    player "Fuck Katie that feels good."
    katie "Uh huh?"
    scene fs katieblowjob21
    with Dissolve(0.7)
    katie "Man your balls are so hefty!"
    katie "You must be ready to cum huh?"
    player "Well I uh-"
    scene fs katieblowjob22
    with vpunch
    player "Oh shit okay!"
    show katieblowjob1 movie3
    pause
    player "Fuck me!"
    katie "Mmmmm!"
    player "I'm close already Katie!"
    show katieblowjob1 movie4
    pause
    player "AHH fuck yes!"
    scene fs katieblowjob24
    katie "*Gasp*"
    show katieblowjob1 movie5
    player "God you're so fucking hot!"
    player "Take it all over your face and tits you fucking slut!"
    katie "AHNN!"
    scene fs katieblowjob26
    with Dissolve(0.5)
    player "Hah...hah.."
    player "God dammit."
    scene fs katieblowjob27
    katie "Ah?"
    player "You're a fucking Succubis."
    scene fs blackblank
    with Dissolve(1.0)
    katie "Hahaha."
    katie "Maybe I am!"
    player "I'm going home, gotta reset my conscience."
    katie "I hope you know that was just an appetizer."
    player "You're killing me."
    if miaphase2interaction2 >= 4:
        $ katiequestlog = "I can't stop thinking about Katie. I should contact Mia and ask for us to all hang out"
    else:
        $ katiequestlog = "Katie's such a little slut. Will she try anything at the next dinner?"
    $ katiephase2interaction1 = 4
    jump passtime


# Chapter 3

label katiephase3interaction1part1:
    scene fs blackblank
    with Dissolve(0.7)
    "Briiing Briiing"
    player "Hmm? Oh hey Mia."
    mia "[povname]...I just waaatched a moooovie.."
    player "Oh yeah? Was it another romance?"
    mia "Maaaaybe."
    player "I'm on my way."
    pause
    "Not too very long after..."
    scene fs katiejealous1
    with Dissolve(0.5)
    mia "Ahn..hah.."
    pause
    scene fs katiejealous2
    mia "Ah!"
    mia "Oh [povname]! You always go so DEEP!"
    player "Hah.."
    scene fs katiejealous3
    mia "Hah..hah..hah.."
    scene fs katiejealous4
    mia "AH! I'm gonna cum!"
    pause
    scene fs katiejealous3
    player "Cum for me baby."
    scene fs katiejealous4
    mia "Oh GOSH [povname]!"
    mia "I love you!"
    mia "I LOVE YOU I LOVE YOU I LOVE YOU!"
    player "Fuck baby I love you too UGH I'm CUMMING!"
    mia "Cum inside me!"
    scene fs blackblank
    with Dissolve(0.7)
    mia "YESSS!"
    mia "I-I can...feel..it.."
    "After a few minutes..."
    scene fs katiejealous5
    with Dissolve(0.7)
    pause
    katie "....."
    katie "Wake up."
    mia "Hmm?"
    katie "Mia wake up."
    scene fs katiejealous5b
    mia "Oh...hi Katie."
    katie "You're lucky mom's staying at her office tonight."
    mia "Oh yeah...would've...been awkward."
    katie "Can you guys like tone it down a notch?"
    mia "Sorry...was I too loud?"
    katie "No, with the lovey-dovey shit."
    katie "So annoying hearing you scream 'I love you' as you get blasted with baby batter."
    mia "Hehe..yeah...okay."
    katie "Mia? I mean it I hate that."
    scene fs katiejealous5
    with Dissolve(0.5)
    mia "*Snore*..."
    katie "...."
    scene fs katiejealous6
    with Dissolve(0.7)
    katie "...."
    scene fs katiejealous7
    katie "...."
    scene fs katiejealous6
    katie "{i}Whatever.{/i}"
    scene fs katiejealous8
    "*Slam*"
    $ katiephase3interaction1 = 1
    $ katiequestlog = "Mia told me Katie heard us fucking...kinda hot."
    jump passtime

label katiephase3interaction1part2:
    hide screen uppergui
    hide screen questboxpreview
    scene fs livingroom
    with Dissolve(0.7)
    $ playerSprite = 0
    $ katieSprite = 7
    show fbplayer current:
        xalign 0.5 ypos 120
    pause
    "*knock knock*"
    player "Hmm?"
    show fbkatie current:
        xalign 0.7 ypos 120
    katie "Hey you."
    $ playerSprite = 1
    player "Katie?"
    player "Hey, what are you doing here?"
    $ playerSprite = 0
    $ katieSprite = 7
    katie "Oh you know, I was just in the area and thought I'd stop by."
    katie "Give my favorite sister's boyfriend a hug."
    $ katieSprite = 6
    katie "{i}And a soul-sucking blowjob{/i}"
    $ playerSprite = 1
    player "Yeah sure, help yourself."
    $ playerSprite = 0
    $ katieSprite = 7
    show fbkatie current:
        xalign 0.55 ypos 120
    with move
    katie "Yay!"
    $ katieSprite = 6
    scene fs katiephonebj1
    with Dissolve(0.7)
    katie "MMMM!"
    player "I like your dress."
    katie "Oh I know."
    pause
    scene fs katiephonebj2
    katie "Hehehe."
    katie "{i}Mia I'm about to make your boyfriend cum so hard his legs'll buckle{/i}"
    player "Alright what are you up to? I know that face."
    katie "{i}Just show a little cleavage and he's ready to fuck me senseless{/i}"
    scene fs katiephonebj2b
    katie "Nothiiing."
    scene fs katiephonebj2
    katie "{i}No 'I love yous' needed!{/i}"
    player "Katie."
    scene fs katiephonebj3
    katie "Oop! What's this?"
    player "My phone..wait are you calling Mia?"
    scene fs katiephonebj4
    player "Did you call her by accident?"
    scene fs katiephonebj5
    "*Click*"
    mia "Hello?"
    scene fs katiephonebj6
    pause
    player "Oh fuck."
    player "Uh hey Mia!"
    scene fs katiephonebj7
    katie "{i}Hehehe, he's mine now!{/i}"
    player "Hey yeah no, I'm doing good."
    scene fs katiephonebj8
    with Dissolve(0.5)
    player "Are you at school?"
    player "No? Ah okay that's actually great."
    scene fs katiephonebj9
    with Dissolve(0.5)
    player "I need your help again.."
    katie "{i}Again?{/i}"
    scene fs katiephonebj10
    katie "*Kiss*"
    scene fs katiephonebj9
    player "Yeah I've been just stuck working a lot past few days, need to relieve some stress."
    scene fs katiephonebj11
    player "Oh really? Hehe."
    scene fs katiephonebj12
    player "OOhhh, yes baby.."
    katie "{i}Smart of him to initiate some dirty phone talk{/i}"
    katie "{i}Wasn't part of the plan but whatever{/i}"
    scene fs katiephonebj12b
    player "Fuck that's so hot."
    show katiephoneblowjob movie1
    player "Yes baby use it."
    player "Haha not as big as me huh?"
    player "Hah..."
    player "God I want you so fucking bad right now!"
    katie "{i}He's not...{/i}"
    scene fs katiephonebj13
    katie "{i}He's not into me at all!{/i}"
    katie "{i}He's just using me to jack off with Mia{/i}"
    show katiephoneblowjob movie2
    player "Cum for me baby!"
    player "Make an absolute mess!"
    player "AGH YES FUCK!!"
    scene fs katiephonebj14
    with Dissolve(0.5)
    player "Hah..."
    player "Thanks so much baby that was so hot."
    pause
    $ playerSprite = 21
    scene fs livingroom
    show fbplayer current:
        xalign 0.5 ypos 120
    show fbkatie titsoutcum1:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    pause
    $ playerSprite = 22
    player "Haha yeah it was a lot."
    player "Actually no I had something to cum on so no cleanup needed."
    show fbplayer current:
        xalign 0.3 xzoom -1.0 ypos 120
    player "Haha yeah."
    player "By the way, I wanted to ask-"
    hide fbplayer current
    pause
    katie "..."
    show fbkatie titsoutcum2:
        xalign 0.6 ypos 120
    katie "What the fuck!?"
    $ katiequestlog = "No more content for Katie in this version(Ch2.5)"
    $ katiephase3interaction1 = 2
    jump passtime
