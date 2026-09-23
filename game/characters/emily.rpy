# chapter 1
# interaction 1
# part 1

label emilyphase1interaction1part1:
    hide screen uppergui
    hide screen emily_atschool
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)
    $ playerSprite = 3
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    player "{i}Ah. There's what's-her-face.{/i}"
    player "{i}Not only am I not attracted to 'main character' type girls like her, I don't even really want to talk to her.{/i}"
    player "{i}She'd probably get me wrapped up in some sort of journey or quest.{/i}"
    player "{i}Looks like she's working on the banner alone...{/i}"

    show fbplayer frownflip:
        xalign 0.25
    with move
    player "{i}Yeah I'll go somewhere else.{/i}"


    emily "Ah! Alright time for a quick break!"
    show fbplayer frownflip:
        xalign 0.15
    with move
    play sound "audio/emilygameaudio/emilyhey.wav"
    emily "OH! [povname]! Is that you?"
    player "{i}Oh god she sees me.{/i}"
    emily "Come over here!"
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    player "{i}Ugh, okay relax. She's Mia's friend. I can talk to her, even if just a pretense. Small conversation. It's fine.{/i}"

    $ emilySprite = 1
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ emilySprite = 1
    emily "Hehe nice to see you again."
    $ emilySprite = 0
    $ playerSprite = 1
    player " Haha yeah sure."
    $ playerSprite = 3
    player "{i}Look at her face, can you get any more generic looking?{/i}"
    $ playerSprite = 5
    player "You look like you belong on the cover of a adventure book for girls so they can self insert themselves as you."
    $ playerSprite = 11
    player "{i}Shit did I just say that out loud?{/i}"
    emily "...."
    $ emilySprite = 1
    play sound "audio/emilygameaudio/emilythanks.wav"
    emily "Wow that's so cool! Nice of you to say that."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Uh no problem..."
    $ playerSprite = 3
    $ emilySprite = 1
    emily "What are you doing here?"
    $ emilySprite = 0
    $ playerSprite = 5
    player "Looking for Mia."
    $ playerSprite = 4
    player "{i}Or literally anyone else other than you.{/i}"
    $ emilySprite = 1
    emily "Oh of course! You seem like such a nice boyfriend."
    $ emilySprite = 0
    $ playerSprite = 1
    player "I try to be."
    $ playerSprite = 4
    $ emilySprite = 1
    emily "Mia's really lu-"
    show fbemily headturn
    "Someone Passing By" "Hey Emily thanks again for helping me study I aced the quiz!"
    show fbemily headturnsmile
    emily "No problem Darren I knew you could do it!"
    $ emilySprite = 1
    show fbemily current
    with Dissolve(0.5)
    emily "Yeah so like I was saying Mia-"
    show fbemily headturn
    "Someone Else Passing By" "Sup Em! Thanks for replacing Samantha for cheerleading last week!"
    show fbemily headturnsmile
    emily "Glad I could help! I hope her leg feels better soon!"
    $ emilySprite = 0
    show fbemily current
    with Dissolve(0.5)
    player "....."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Haha sorry about that."
    emily "Mia seems to re-"
    $ playerSprite == 4
    show fbemily headturn
    "Another Freaking Person" "Emilllyyyyy wazzzzaaaaaap??!"
    show fbemily rockon
    emily "Wazzzzzuuuup!!!!"
    $ playerSprite = 3
    player "{i} Somebody please kill me.{/i}"
    $ emilySprite = 1
    show fbemily current
    with Dissolve(0.5)
    emily "Ahem, so yeah like I was saying."
    emily "Mia's really lucky to have you, so please treat her well she's the one who deserves it most of all of us."
    $ emilySprite = 0
    $ playerSprite = 1
    player "....Yeah for sure. I really care about her."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Me too, she's like a...precious rare gem but super cute!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "In the shape of a teddy bear with a heart made of kittens!"
    $ playerSprite = 0
    $ emilySprite = 1
    play sound "audio/emilygameaudio/emilylaugh.wav"
    emily "Hahaha yeah!"
    $ emilySprite = 0
    $playerSprite = 4
    player "{i}Shit, I didn't mean to get chummy with her.{/i}"
    emily "...."
    $ emilySprite = 1
    emily "Listen if you ever need a friend, I help to prepare the big track meet banner in the afternoon here at school if you wanna talk."
    $ emilySprite = 0
    player "{i}Really? The 'if you ever need a friend' line?"
    $ playerSprite = 1
    player "What makes you think I don't have friends to talk to?"
    $ playerSprite = 0
    $ emilySprite = 2
    emily "Oh no I-I didn't mean-"
    emily "I just meant If you happened by is all. You could help with the banner!"
    $ emilySprite = 0
    $ playerSprite = 5
    player "Yeah I'll think about it."
    $ playerSprite = 4
    $ emilySprite = 1
    emily "Well that's all I can ask for! Class is about to start so I guess I'll see you later!"
    $ emilySprite = 0
    $ playerSprite = 5
    player "Yup maybe."
    $ playerSprite = 4
    $ emilySprite = 1
    emily "Bye!"
    $ emilySprite = 0
    hide fbemily
    with Dissolve(0.5)
    window hide
    pause
    $ playerSprite = 7
    player "{i}Okay that wasn't as agonizing as I was expecting.{/i}"
    player "{i}I'm weak to Mia talk.{/i}"
    player "{i}Also does she know every single person in this school? Jesus.{/i}"
    player "{i}No way am I helping with that banner though....probably.{/i}"
    $ playerSprite = 0
    $ emilyphase1interaction1 = 1
    $ emilyquesticon = "gui/questboxEmily.png"
    if renpy.android:
        $ emilyquestlog = "{size=-25}If I want to help Emily with the banner I can meet her in the hallway. If I WANT to do that.{size=-25}"
    else:
        $ emilyquestlog = "If I want to help Emily with the banner I can meet her in the hallway. If I WANT to do that."
    hide fs schoolhallwayBLUR
    hide fbemily
    hide fbplayer
    jump passtime

# part 1 post convo (does fucking every part 1 have a post???)

label emilyisbusy:
    hide screen emily_atschool
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)
    $ playerSprite = 4
    $ emilySprite = 1
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    $ emilySprite = 1
    emily "Hey sorry, I need to concentrate! I should be able to talk during the afternoon, I'll still be here."
    $ emilySprite = 0
    player "{i}Pfft, don't assume I wanted to talk to you...{/i}"
    $ playerSprite = 5
    player "Uh yeah, okay."
    $ playerSprite = 0
    hide fs schoolhallwayBLUR
    hide fbemily
    hide fbplayer
    jump schoolhallway

# part 2

label emilyphase1interaction1part2:

    hide screen emily_atschool
    hide screen uppergui
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)
    $ playerSprite = 4
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    player "{i}Alright I'm just here to check on the banner, maybe have a small conversation. That's it.{/i}"

    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ emilySprite = 1
    $ emilySprite = 1
    play sound "audio/emilygameaudio/emilyhey.wav"
    emily "Ahh [povname]! You came you really came!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Yeah I *ahem* came."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh this is great. The power of friendship I tell yah!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Look I'm just curious about this banner, Mia's supporting Ava and I wanna support Mia so yeah."
    $ playerSprite = 0
    show fbemily bigsmile
    emily "Well hey, I'll take it!"
    $ emilySprite = 1
    show fbemily current
    emily "So this here is a partly poliester mixed material, that way the paint will last longer, five feet long and twelve across...."
    scene fs blackblank
    with Dissolve(0.7)
    $ emilySprite = 0
    "Emily continues to give you the details and plans about the banner."
    "Her explanation was quite meticulous, she obviously cares about the project"
    "For some time she goes through the type of paint they'll be using, where it's going to go so Ava will best see it near the finish line, and some other stuff"
    "Not once did you ever show interest in what she was saying, but her enthusiasm never wavered"
    scene fs schoolhallwayBLUR
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    player "{i}Man she's really reved up about this. I really don't care about all these particulars though.{/i}"
    $ emilySprite = 1
    emily "And yeah that's about it. There's not much to do now except wait for the paint to arrive and just start painting."
    $ emilySprite = 0
    $ playerSprite = 5
    player "Wait you don't have help coming?"
    $ playerSprite = 4
    $ emilySprite = 1
    emily "Nope just me."
    $ emilySprite = 0
    $ playerSprite = 5
    player "Aren't you part of some comittee or something, isn't there people who are supposed to work on this together with you?"
    $ playerSprite = 4
    $ emilySprite = 1
    emily "Well uh I really advicated to the board for this banner thing to happen and while they agreed to give it to me it used up what was the rest of the funds available."
    $ emilySprite = 0
    $ playerSprite = 1
    player "And other members wanted those funds for their own reasons?"
    $ playerSprite = 0
    $ emilySprite = 1
    play sound "audio/emilygameaudio/emilyum.wav"
    emily "Um, yes."
    $ emilySprite = 0
    $ playerSprite = 5
    player "So you don't have anyone else to help you?"
    $ playerSprite = 4
    $ emilySprite = 2
    emily "They...have other duties to attend to I-I'm sure."
    $ emilySprite = 1
    emily "I don't mind though! It'll all be worth it when Ava's face lights up seeing the banner as she crosses the finish line!"
    $ emilySprite = 0
    $ playerSprite = 4
    player "{i}Shit I'm starting to feel bad. I gotta get out of here!{/i}"
    $ playerSprite = 1
    player "Ah damn well your dedication is impressive I uh, I gotta go now though!"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh um okay."
    $ emilySprite = 0
    $ playerSprite = 1
    player "I probably won't have time but when is that paint coming in?"
    $ emilySprite = 1
    emily "It should be here by tomorrow same time!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Okay, like I said I probably won't show up though!"
    $ emilySprite = 1
    emily "No pressure! I don't mind doing everything myself."
    $ emilySprite = 0
    $ playerSprite = 4
    player "{i}UGGGH.{/i}"
    $ playerSprite = 0
    $ emilyphase1interaction1 = 2
    $ emilyquestlog = "What am I doing? Now I'd feel bad if I don't help her out."
    hide fs schoolhallwayBLUR
    hide fbemily
    hide fbplayer
    jump passtime

# part 2 post convo 1 (not used)

label whensthepaintagain:

    hide screen emily_atschool
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Real quick, when's the paint coming in again?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Tomorrow right here in the afternoon!"
    $ emilySprite = 0
    hide fs schoolhallwayBLUR
    hide fbemily
    hide fbplayer
    jump schoolhallway

# part 2 post convo 2 (also unreachable but is in the code (the game sets the sleep convo to the next state so it basically skips this))

label whensthepaintagain2:
    hide screen emily_atschool
    hide screen uppergui
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)

    $ emilySprite = 1
    show fbemily current:
        xalign 0.6 ypos 120

    show fbplayer current:
        xalign 0.35 ypos 120
    emily "Hey sorry class is about to start but I'll be painting the banner in the afternoon in the hallway!"
    hide fs schoolhallwayBLUR
    hide fbemily
    hide fbplayer
    jump schoolhallway

# part 2 sleep shit

label thinkaboutemilybeforesleep:
    hide screen backbuttonROOM
    scene fs blackblank
    with Dissolve(0.7)
    scene fs playerbedneutral
    with Dissolve(0.7)
    player "Hmmmm."
    player "Emily. What should I do about her?"
    scene fs playerbedthink1
    player "I could ignore her, like I was trying to before....but she might get upset if I don't show up to help with the banner."
    player "Can't have her telling Mia that."
    scene fs playerbedthink2
    player "I don't hate her, or at least I don't think I do...shit maybe I do, but..."
    player "Even if I don't like the dynamic of her being a generic 'main character' trope, I did tell Mia I'd try to get along with all her friends."
    scene fs playerbedthink1
    player "I think there might be some potential here...for something. She seems so malleable, if I play my cards right I might be able to..."
    scene fs playerbedneutral
    player "Hmmm no. For now I'll just see where things go."
    jump gotosleep

# part 3

label emilyphase1interaction1part3:

    hide screen emily_atschool
    hide screen uppergui
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Hey Emily."
    $ playerSprite = 3
    $ emilySprite = 1
    emily "[povname]! I thought you couldn't make it?"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Well you're..."
    $ playerSprite = 5
    player "*Sigh*, you're Mia's friend and this is important to you and....I just made the time alright?"
    $ playerSprite = 4
    $ emilySprite = 1
    emily "Well I'm glad to have you!"
    $ emilySprite = 0
    hide fbemily current
    with Dissolve(0.5)
    player "{i}I hope I don't regret this.{/i}"
    $ playerSprite = 0
    player "{i}C'mon [povname], big smile!{/i}"
    scene fs emilypainting1
    with Dissolve(1.0)
    "You work away with Emily at the banner throughout the afternoon"
    window hide
    pause
    player "{i}Huh...this is actually not too bad. Kinda relaxing.{/i}"
    scene fs emilypainting2talkplayer
    player "Well it's been like 4 hours so far. I'd say we're about halfway done."
    scene fs emilypainting2talkemily
    emily "Yeah I think we should stop soon after this part is finished."
    emily "Thanks you really made this fly by, it would probably take three more days to finish if you weren't here." # spelling mistake once again
    scene fs emilypaintplayerfrown
    player "{i}Don't worry I'm sure with your Mary-Sue powers you wouldve found a way to finish without anyone else.{i}"
    scene fs emilypainting1
    with Dissolve(0.3)
    "As you continue to paint the sun hits your eye through the window, causing you to turn towards Emily."
    scene fs emilypaintcloseup
    with Dissolve(1.0)
    window hide
    pause
    $ hiden_textbox = True
    player "{i}Woah...{/i}"
    player "{i}In this lighting...{/i}"
    player "You're actually really pretty."
    #$ hiden_textbox = False
    window hide
    pause
    scene fs emilypainting6b
    with vpunch
    play sound "audio/emilygameaudio/emilyhuh.wav"
    emily "W-W-Wha what?"
    scene fs emilypainting7
    player "Shit I uh, yeah sorry I just. Yeah."
    scene fs emilypainting5
    with Dissolve(0.7)
    emily "...."
    emily "T-Thank you."
    scene fs emilypainting2talkemily
    with Dissolve(0.7)
    play sound "audio/emilygameaudio/emilyshortlaugh.wav"
    emily "Although maybe you should reserve the compliments f-for Mia."
    emily "Or maybe it's no big deal and I'm being weird sorry!"
    scene fs emilypainting5
    with Dissolve(0.7)
    player "{i}God damn it why'd I have to just blurt that out?!{/i}"
    player "No it's whatever no worries."
    player "{i} I'm such an idiot, I'm not even supposed to like her remember??!{/i}"
    player "{i}Let's just focus on finishing up this last part of the banner. Then forget this ever happened.{/i}"
    player "{i}I'm gonna need more orange for this.{/i}"
    window hide
    pause
    scene fs emilypainting8
    with hpunch
    $ hiden_textbox = True

    play sound "audio/emilygameaudio/emilyoh.wav"
    emily "Oh!"
    window hide
    pause
    player "{i}Seriously? Is this a joke we just did the most cliché shit you can do.{/i}"
    emily "...."
    player "{i}Why isn't she moving her hand? Why aren't I moving MY hand?{/i}"
    scene fs emilypainting9
    with Dissolve(0.5)
    player "{i}Shit now we're holding hands...did I grab hers? Or did she grab mine?{/i}"
    emily "{i}What are you doing Emily?? T-This is Mia's boyfriend!{/i}"
    emily "{i}One guy says you're pretty and what? You fall for him instantly??{/i}"
    emily "{i}W-Why isn't he letting go?{/i}"
    player "{i}Her hands are really soft. Probably uses lotion.{/i}"
    player "{i}Do I smell lavender?{/i}"
    player "{i}What the fuck am I talking about!!{/i}"
    scene fs emilypainting10
    emily "{i}Now he's rubbing my hand...I can't concentrate on the banner like this!{/i}"
    scene fs emilypainting9
    player "{i}It's so god damn soft...{/i}"
    scene fs emilypainting10moan
    play sound "audio/emilygameaudio/emilysoftahn.wav"
    emily "{i}Ah...{/i}"
    scene fs emilypainting9
    player "{i}Bitch did you just moan??!{/i}"
    scene fs emilypainting10
    player "{i}....This is actually getting pretty sensual.{/i}"
    scene fs emilypainting9
    emily "{size=25}[povname]..{/size}"
    scene fs emilypainting10
    player "{i}This is...really nice.{/i}"
    player "{i}Do I like this girl?{/i}"
    scene fs emilypainting9
    player "{i}NOPE. Okay that's it, this has gone too far I need to sto-{/i}"
    scene fs emilypainting11
    with vpunch
    play sound "audio/emilygameaudio/emilysorry.wav"
    emily "{i}S-Sorry I can't..{/i}"
    emily "{i}I shouldnt've done that I...I...{/i}"
    play sound "audio/emilygameaudio/emilycry.wav"
    emily "{i}*sobs*{/i}"
    scene fs blackblank
    with Dissolve(1.0)
    #$ hiden_textbox = False
    "Her face beet red, Emily runs away teary eyed and confused."
    player "{i}....{/i}"
    player "{i}Man what the fuck.{/i}"
    $ playerSprite = 0
    $ emilyphase1interaction1 = 4
    $ emilyquestlog = "What is WRONG with me??"
    #$ timeofday = "Day"

    hide fs blackblank
    hide fbemily
    hide fbplayer
    jump passtime

# part 3 sleep shit once again

label thinkaboutemilybeforesleep2:
    hide screen backbuttonROOM
    hide screen uppergui
    scene fs playerbedneutral
    with Dissolve(0.7)
    player "I don't know what the hell I was thinking."
    scene fs playerbedthink1
    player "I'm an idiot. How you gonna call Emily pretty after thinking about how unattractive she is??"
    scene fs playerbedthink2
    player "....."
    player "Why am I so horny? Should I see if Mia's free or-"
    scene fs playerbedneutral
    player "....."
    scene fs playerbedsmile
    player "Wait a minute that's it! Hahaha."
    player "I don't like Emily, it was just my dick talking! Man my libido is in overdrive these days."
    scene fs playerbedthink1
    player "....."
    scene fs playerbedsmile
    player "Okay I can work with this."
    player "I just have to approach this from this new angle."
    player "I've never hate-fucked anyone before."
    scene fs blackblank
    with Dissolve(1.0)
    player "Whether or not I'd do it, still seems pretty hot to me."
    player "How am I going to take advantage of her now? Do I even want to?"
    player "First thing's first. Gotta talk to her again, smooth things out. She was really flustered when she ran away."
    player "Heh okay now I'm getting excited."
    $ emilyphase1interaction2 = 1
    $ emilyquestlog = "I gotta get Emily to talk to me."
    jump gotosleep

# interaction 2
# part 1

label emilyphase1interaction2part1:
    hide screen uppergui
    hide screen emily_atschool
    hide screen uppergui
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)
    $ playerSprite = 0

    image fbemily defaultflip = im.Flip("Sprites/emilydefault.png", horizontal=True, vertical=False)
    show fbemily defaultflip:
        xalign 0.8 ypos 120
    with Dissolve(0.5)

    player "{i}Alright there she is, must still be working on the banner.{/i}"

    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.5)

    window hide
    pause

    show fbplayer current behind fbemily:
        xalign 0.65 ypos 120
    with move

    $ playerSprite = 1
    player "Hey Emily."

    $ playerSprite = 0
    $ emilySprite = 2
    show fbemily current at surpriseshake:
        xalign 0.8 ypos 120
    with Dissolve(0.5)


    play sound "audio/emilygameaudio/emilysurprised.wav"
    emily "Ahhh!"
    emily "I'm..I-I'm really busy sorry bye!"
    show fbemily defaultflip:
        xalign 1.5 ypos 120
    with move

    show fbplayer current:
        xalign 0.5 ypos 120
    with move

    $ playerSprite = 4
    player "{i}Seriously? She ran away again!?{/i}"
    player "{i}I don't know how I'm gonna sort things out if I can't even talk to her.{/i}"

    image fbava talkflip = im.Flip("Sprites/avatalk.png", horizontal=True, vertical=False)
    show fbava talkflip:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    ava "Woah I haven't seen Em run that fast in a while."

    $ avaSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.8 ypos 120
    with Dissolve(0.5)

    charlotte "I know! Her face was all red and she looked really flustered."
    $ charlotteSprite = 3
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    charlotte "You! Did you do something to Emily??"
    $ charlotteSprite = 0

    $ playerSprite = 5
    player "What?"
    player "No! I didn't even get a chance to talk to her."

    $ playerSprite = 0
    $ avaSprite = 16
    ava "Hmm in that case..."
    ava "I hope it's not..."
    $ avaSprite = 15
    $ charlotteSprite = 1
    charlotte "It can't be! We helped her kick it!"
    charlotte "And plus where would she even get any? I don't know any place that sells it."
    $ charlotteSprite = 0
    $ playerSprite = 7
    player "{i}I gotta find out what they're talking about.{/i}"
    $ playerSprite = 1
    player "Sorry what are you guys talking about? Did I do something wrong?"
    $ playerSprite = 0
    $ avaSprite = 16
    ava "No no it's not you."
    $ avaSprite = 15
    $ charlotteSprite = 1
    charlotte "Ava! Don't tell HIM."
    $ charlotteSprite = 0
    $ avaSprite = 1
    ava "Relax, what could be the harm? Like you said she already kicked the habit. Plus he's Mia's boyfriend."
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "Ugh."
    $ charlotteSprite = 0

    $ playerSprite = 1
    player "So nothing's my fault?"
    $ playerSprite = 0
    $ avaSprite = 16
    ava "No it's okay, you see about a year ago there was an...incident. Involving Em."
    $ avaSprite = 15
    $ playerSprite = 11
    player "An incident?"
    $ playerSprite = 0
    $ avaSprite = 16
    ava "Yeah."
    $ avaSprite = 15
    $ charlotteSprite = 1
    charlotte "You know how everybody has something they like."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Um yeah? I like video games."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "No idiot, like food wise. Treats or snacks."
    charlotte "I like drinking Caramel Macchiatos."
    charlotte "Ava likes eating Scallops."
    $ charlotteSprite = 0
    $ avaSprite = 1
    ava "Love em."
    ava "And they're so good for you!"
    $ avaSprite = 0
    $ charlotteSprite = 1
    if katieconversation > 0:
        charlotte "And-"
        $ charlotteSprite = 0
        $ playerSprite = 1
        player "Katie likes sucking dick."
        $ playerSprite = 0
        charlotte "....."
        $ avaSprite = 1
        ava "HAHAH!"
        ava "Oh man hahahaha so you met her huh?"
        $ avaSprite = 0
        $ charlotteSprite = 1
        charlotte "Okay that...that was pretty funny."
    charlotte "*Ahem* But anyways, Emily....likes strawberry candy."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Okay?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "She REALLY likes strawberry candy."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I still don't see-"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "It's not like a simple sweet tooth, she goes crazy for strawberry flavored candy SPECIFICALLY."
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "Especially if it's chewy."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Huh."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "And when I say crazy I mean crazy. She bought out the ENTIRE town over the course of a week."
    $ avaSprite = 0
    $ playerSprite = 11
    player "...."
    $ avaSprite = 1
    ava "And when there wasn't any left? She lost it."
    $ avaSprite = 16
    ava "I rather not go into detail."
    $ avaSprite = 15
    $ charlotteSprite = 1
    charlotte "She didn't hurt anyone, but it wasn't for lack of trying. The police even got involved."
    charlotte "And she didn't listen to us at all, it was like we weren't even her friends anymore."
    $ charlotteSprite = 0
    $ playerSprite = 11
    player "Woah...but that's like her whole thing."

    $ avaSprite = 16
    ava "Exactly, that's why it was so scary. So we all worked together to get her off the habit."
    ava "And that's what the town calls the great void."
    $ avaSprite = 15
    $ playerSprite = 1
    player "Haha what?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "You laugh but this town takes it really serious. We had no idea how many volunteer programs Emily was a part of."
    $ charlotteSprite = 0
    $ avaSprite = 1
    ava "Not only is she in half of the school clubs and an honorary member of the other half."
    ava "She's also in a TON of town stuff."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Well how much can one girl be-"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Soup Kitchens, park restoration programs, volunteer cleaning services, music performances, public plays..."
    $ charlotteSprite = 0
    $ avaSprite = 16
    ava "The list goes on man."
    $ avaSprite = 15
    $ playerSprite = 11
    player "Shit okay..."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "And she was usually always in a leader position."
    $ avaSprite = 16
    $ charlotteSprite = 0
    ava "So what do you think happens to all these groups when Emily not only goes crazy, but takes several weeks off to get better?"
    $ avaSprite = 15
    $ playerSprite = 1
    player "Ahhh it all makes sense now."
    $ playerSprite = 0
    $ avaSprite = 16
    ava "It was chaos, and when it wasn't chaos it was dissapointment and wasted city money and resources."
    $ avaSprite = 15
    $ charlotteSprite = 1
    charlotte "Well, as Emily says with the power of friendship she was able to pull through. She's better than ever and we're all closer than ever."
    $ charlotteSprite = 0
    $ avaSprite = 1
    ava "The town even put an embargo on strawberry candy imports. It'd be pretty difficult to find it in this town."
    $ avaSprite = 0
    $ playerSprite = 1
    player "No way!"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Just shows how important Emily is."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I knew she was a central character type but...like wow never in such a literal sense."
    player "Well girls I appreciate the story, I'll keep it in mind around Emily."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "I just hope she's not back on it again."
    $ charlotteSprite = 0
    $ avaSprite = 1
    ava "Well just have to ask her later, I'm sure everythings fine Charlotte. We should go."
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "Yes alright, let's go to class then."
    $ charlotteSprite = 0
    $ avaSprite = 1
    ava "Bye [povname], see you later."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Yeah bye you two."
    $ playerSprite = 7
    hide fbava current
    with Dissolve(0.7)
    hide fbcharlotte current
    with Dissolve(0.7)
    player "{i}Holy Shit.{/i}"
    player "{i}That was a crazy story.{/i}"
    player "{i}I'm not sure I can take advantage of it just yet though.{/i}"
    player "{i}I still need to just talk to her again.{/i}"
    player "{i}If she wants to finish this banner she'll have to come back at some point. I should return in the afternoon.{/i}"
    $ emilyphase1interaction2 = 2
    jump passtime

# part 1 post convo (man pls)

label emilyrunsaway:
    hide screen emily_atschool
    scene fs schoolhallway2extras
    "As you approach Emily she notices you and runs away blushing."
    "Maybe you should return in the afternoon and try again"
    jump schoolhallway

# part 2

label emilyphase1interaction2part2:

    hide screen emily_atschool
    hide screen uppergui
    scene fs schoolhallwayBLUR
    with Dissolve(0.5)

    $ playerSprite = 7
    $ emilySprite = 0

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)



    player "Okay. There she is. Wow she looks really upset."
    $ playerSprite = 0
    player "[povname] you heart breaker you hehe."

    hide fbplayer current
    $ emilySprite = 4
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)

    play sound "audio/emilygameaudio/emilyworried.wav"
    emily "{i}Look at you Em. You just had to push them! You always go too far with things!{/i}"
    $ emilySprite = 5
    play sound "audio/emilygameaudio/emilycry.wav"
    emily "*sniff* Now you're screwed!"
    $ emilySprite = 4
    player "{i}I'm just gonna go up  to her, tell her to forget the whole thing ever happened, and move on. Quick and simple.{/i}"
    emily "{i}I've always been able to pull through before...but I don't think gumption is gonna help me this time around..{/i}"

    $ playerSprite = 1

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    player "Hey Emily."
    $ emilySprite = 5
    $ playerSprite = 0
    emily "Hello."
    $ emilySprite = 4
    $ playerSprite = 6
    player "Listen don't run away again I can tell you're really upset by what happened so I'm just gonna apologize now so we can mo-"
    $ emilySprite = 2
    emily "Wait what? Oh [povname]!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Uh yeah hi like I was say-"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "What are you talking about??"
    $ emilySprite = 0
    $ playerSprite = 5
    player "I was helping you out...and you look really depressed now...so I'm apolog-"
    $ emilySprite = 4
    player "Wait have you been crying? Jesus Emily it's not like we fucked or anything we just held hands."
    $ playerSprite = 11
    $ emilySprite = 2
    emily "W-W-What?? What are you talking about!?"
    emily "I'm not...of course we didn't...d-do something like that!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "I know."
    player "THAT'S what I'm saying. We just held hands."
    $ playerSprite = 0
    $ emilySprite = 0
    player "{i}Oh I gotta hit her with the magic word!{/i}"

    $ playerSprite = 1
    player "FRIENDS can do that without it being weird right?"
    $ playerSprite = 0
    $ emilySprite = 2
    emily "Y-Yeah of course."
    $ emilySprite = 1
    emily "Sorry for running away in embarassment. That was a new experience for me."
    emily "*Ahem* But anyway that's not why I'm upset now!"
    $ emilySprite = 2
    emily "Jeez you can be pretty crude you know!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Hey it stopped you from crying didn't it?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh I....I guess it did haha."
    $ emilySprite = 0
    $ playerSprite = 7
    player "{i}Alright now's the time to strike!{/i}"
    player "{i}I'm still not saying I want to sleep with her but I mean... {/i}"
    player "{i}Grateful pussy IS good pussy.{/i}"
    $ emilySprite = 0
    $ playerSprite = 1
    player "So..."
    player "How can I help?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "It's my problem you don't have to worry abou-"
    $ emilySprite = 0
    $ playerSprite = 10
    player "Nope. Don't shut me down after I've gone through the trouble of asking. Just tell me what's wrong."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Hehe what are you Ava?....Alright."
    $ emilySprite = 5
    emily "I'm out of paint."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Out of paint? That's it?"
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Yes that's it! I messed up! I ran out of paint because I didn't buy enough so the banner can't be finished and I screwed up!"
    $ emilySprite = 4
    $ playerSprite = 1
    player "Gotta say it's refreshing seeing you act like this. But it's no big deal just buy more paint?"
    $ playerSprite = 0
    $ emilySprite = 5
    emily "I'm out of money! The budget the board gave me after I BEGGED them has ran out I can't get anymore and I have no money of my own."
    emily "People expect me to always figure things out no matter what, Ava's relying on me, all the girls are relying on me!"
    emily "But I don't know what to do this time I'm screwed!"
    $ emilySprite = 4
    if paintcount == 0:
        player "{i}Wait a minute...I have a can of paint on me right now!{/i}"
        player "{i}I could just give it to her now...{/i}"
        player "{i}But for some reason I'm compelled to give it to her in my own turf.{/i}"
        player "{i}I'll call from my place and tell her to come over.{/i}"
    $ playerSprite = 1
    player "It's the same color we were using before right?"
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Yeah why?"
    $ emilySprite = 4
    $ playerSprite = 1
    player "No reason."
    player "Give me your number."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Um okay."
    $ renpy.notify("Got Emily's Number!")
    $ contact_list.append("Emily")
    $ emilySprite = 0
    $ playerSprite = 1
    player "Since there's no paint here I'm gonna go."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Yeah I understand, bye."
    hide fbemily current
    with Dissolve(0.5)
    if paintcount == 1:
        $ playerSprite = 3
        player "{i}Shit this is why I didn't want to start talking to her ugh!{/i}"
        player "{i}I think there's paint available somewhere in the mall I should go check it out.{/i}"

        $ emilyphase1interaction2 = 3
    else:
        $ emilyphase1interaction2 = 4

    $ emilyquestlog = "After I get some paint I should call Emily from my place."
    jump passtime

# part 3

label emilyphase1interaction2part3:
    hide screen phonecontacts
    hide screen contacts
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonROOM
    hide screen uppergui
    hide screen questboxpreview

    scene fs livingroom
    emily "{cps=25}Hello?{/cps}"
    player "{cps=25}Hey Emily. It's [povname].{/cps}"
    emily "{cps=25}Hi [povname]. Can I help you with something? I don't really have much time to chat.{/cps}"
    player "{cps=25}Yeah I really need your help. Can you come over to my place?{/cps}"
    emily "{cps=25}I'm sorry I really don't...I don't think I can..{/cps}"
    emily "{cps=25}Can you ask Mia or one of the other girls to help? I'm not in a very good place right now.{/cps}"
    player "{cps=25}Please Emily, it's something only YOU can do. I need a FRIEND right now.{/cps}"
    emily "{cps=25}....Okay. But I can't stay for long.{/cps}"
    player "{i}Gotcha bitch!{/i}"
    player "{cps=25}For sure, thanks a lot.{/cps}"
    "After a little while of waiting"

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    "*Ding Dong*"
    $ playerSprite = 1
    player "Come on in."
    $ playerSprite = 0

    show fbemily current behind fbplayer:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ emilySprite = 5
    emily "Hello [povname]. You have a lovely home."
    $ emilySprite = 4
    $ playerSprite = 11
    player "{i}Jesus she's really depressed about this."
    $ playerSprite = 1
    player "Thanks!"
    $ playerSprite = 0
    $ emilySprite = 5
    emily "So what was it that you needed help with?"
    show fbplayer holdpaint:
        xalign 0.39 ypos 120
    emily "Like I mentioned before I might not be able to really provide any-"
    $ emilySprite = 4
    emily "......."
    $ emilySprite = 2
    $ playerSprite = 1
    player "I need help figuring out what to do with this big ol' can of paint!"
    $ playerSprite = 0
    $ emilySprite = 1
    show fbemily current at surpriseshake:
        xalign 0.6 ypos 120
    play sound "audio/emilygameaudio/emilyhuh.wav"
    emily "A-Are you for real right now!?"
    $ emilySprite = 0
    $ playerSprite = 1
    player "It's all yours!"
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.35 ypos 120
    show fbemily paintholdtalk:
        xalign 0.64 ypos 120
    emily "No [povname] I-I can't rely on you t-"

    show fbemily painthold:
        xalign 0.64 ypos 120
    $ playerSprite = 1
    player "I payed a lot of money for this Emily, now take it and finish the banner." # PAYED LMAOOO
    player "Besides, the look on your face is giving you away."
    $ playerSprite = 0
    show fbemily paintholdtalk:
        xalign 0.64 ypos 120
    emily "How much was it? I-I swear I'll pay you back as soon as I can!"

    show fbemily painthold:
        xalign 0.64 ypos 120
    $ playerSprite = 1
    player "I don't want your money Emily. I want your friendship."
    $ playerSprite = 0
    scene fs blackblank
    with Dissolve(0.7)
    emily "*sniff* H-Hold on let me set this down."
    scene fs emilygropefront1
    with Dissolve(1.0)
    emily "I can't...you don't understand how happy this makes me."
    player "I dunno, you have a pretty big smile right now."
    emily "Ahhhh! I can't thank you enough!"
    scene fs emilygropefront2
    with Dissolve(0.7)
    play sound "audio/emilygameaudio/emilycmere.wav"
    emily "C'mere you!"
    scene fs emilygropefront3
    with Dissolve(0.7)
    play sound "audio/emilygameaudio/emilyhugsound.wav"
    player "Woah! Okay no problem."
    scene fs emilygropeback1
    with Dissolve(0.7)
    "While the hug wasn't expected it certainly wasn't unwelcome"
    "Having been hugged by Mia many times, the feeling of her arms squeezed around you tightly put you in reflex mode"
    scene fs emilygropeback2
    with Dissolve(1.0)
    "And without even thinking about it you lifted her skirt and started to feel her butt"
    emily "O-Oh..."
    emily "Um...[povname]?"
    emily "We...you shouldn't.."
    scene fs emilygropeback1
    player "Woah!"
    with vpunch
    player "Shit Emily I'm so sorry I didn't even realize!"
    emily "Y-You didn't?"
    scene fs emilygropefront4
    with Dissolve(0.7)
    player "No it was all reflex....Mia's a big hugger."
    scene fs emilygropefront5
    emily "Hehe she is."
    scene fs emilygropefront4
    player "Yeah and when she gives me a long one I....I grab her butt."
    player "She really likes it."
    scene fs emilygropefront5b
    with Dissolve(0.5)
    emily "S-She does huh?"
    scene fs emilygropefront4b
    player "Yeah and by now we've like normalized it, not even anything special it's just part of the hug."
    scene fs emilygropefront5b
    emily "Well...if Mia likes it then I don't mind."
    scene fs emilygropefront4b
    player "You don't?"
    scene fs emilygropefront5b
    emily "Yeah like you said it's...it's just normal skinship b-between friends."
    player "{i}I mean I didn't say that but I like where this is going.{/i}"
    emily "It's not even a big d-deal right?"
    scene fs emilygropefront4b
    player "Yeah totally..."
    scene fs emilygropeback1
    with Dissolve(1.0)
    emily "So just...go ahead...as long as you just do what you do to Mia."
    scene fs emilygropeback2
    with Dissolve(0.7)
    player "Sure..."
    play sound "audio/emilygameaudio/emilyah.wav"
    emily "Ah..."
    scene fs emilygropeback3
    with Dissolve(0.7)
    player "{i}Her ass is so plump{/i}"
    emily "Hah..."
    scene fs emilygropeback4
    with Dissolve(0.7)
    player "{i}She's starting to pant..{/i}"
    scene fs emilygropeback2
    with Dissolve(0.7)
    play sound "audio/emilygameaudio/emilyah2.wav"
    emily "Uhn."
    player "{i}Damn I'm getting really turned on.{/i}"
    scene fs emilygropeback3
    with Dissolve(0.7)
    emily "S-So you really do this with her?"
    player "Yeah all the time."
    scene fs emilygropeback4
    with Dissolve(0.7)
    emily "You're not j-just taking advantage of me are you?"
    player "Of course not! You can even ask Mia, want me to call her?"
    scene fs emilygropeback2
    with Dissolve(0.7)
    emily "No it's okay..."
    emily "S-So this is all you would do?"
    player "Well..."
    player "By this time...I would usually.."
    scene fs emilygropeback5
    with vpunch
    play sound "audio/emilygameaudio/emilyah3.wav"
    emily "H-H-Hey! That's undern-n-neath my..."
    window hide
    pause
    "Yours fingers slowly pass over her asshole and lodge themselves inside of her"
    scene fs emilygropeback5 at slowfingerfuck
    play sound "audio/emilygameaudio/emilypant.wav"
    "You carefully penetrate her with gentle thrusts"
    window hide
    pause
    emily "Ohhh...[povname]...n-no..."
    player "Do you want me to stop?"
    emily "No it...it fe-feels really good it's just..."
    scene fs emilygropeback5 at slowfingerfuck2
    emily "It's just!"
    scene fs emilygropeback5 at slowfingerfuck3
    play sound "audio/emilygameaudio/emilycum1.wav"
    emily "OOOOHH!"
    emily "{i}Oh god I think I'm gonna cum!{/i}"
    player "{i}Holy shit she's soaking wet now.{/i}"
    scene fs emilygropeback6
    with vpunch
    play sound "audio/emilygameaudio/emilycum2.wav"
    emily "MMMMMM!!!!"
    player "{i}I think she just came all over my hand.{/i}"
    scene fs emilygropefront6
    with Dissolve(1.0)
    "You pull your fingers out of her and let her rest for a moment"
    emily "Oh...[povname]..."
    player "Yeah?"
    emily "....!!"
    scene fs livingroom
    show fbplayer current:
        xalign 0.35 ypos 120

    show fbemily current at surpriseshake:
        xalign 0.45 ypos 120

    $ emilySprite = 2
    emily "Oh my god!"
    show fbemily current:
        xalign 0.6 ypos 120
    with move
    emily "Um okay yeah t-that was...that was great."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Hey hey relax."
    player "You alright?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yeah no I'm fine! I-I just haven't been that um..."
    emily "Excited since I tried out that dildo Katie gave me for my birthday last y-"
    $ emilySprite = 2
    show fbemily current at surpriseshake:
        xalign 0.6 ypos 120
    emily "OH MY GOD YOU DIDN'T HEAR THAT!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Haha sure, I didn't hear anything."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh man I'm as jittery as Charlotte and clumsy as Mia right now."
    $ emilySprite = 4
    $ playerSprite = 1
    emily "{i}Oh my god MIA. What have I done?!{/i}"
    player "Hey no worries. Take the paint and go finish your amazing banner."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Gosh I...okay yes thank you again."
    $ emilySprite = 2
    emily "Come talk to me again at school when I'm...uh...normal again."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Sure thing."
    $ playerSprite = 0
    $ emilySprite = 1
    play sound "audio/emilygameaudio/emilynervousbye.wav"
    emily "Okay bye!"
    $ emilySprite = 0

    show fbemily current:
        xalign 1.5 ypos 120
    with move

    $ item_list.remove("Paint")

    player "{i}Wow."
    player "{i}She just let me full on finger her for 5 minutes.{/i}"
    player "{i}Normally that'd be hot already but the fact that it was goody two shoes, super prude, PG-13 Emily...{/i}"
    player "{i}I feel like I could cum right now if I wanted.{/i}"
    player "{i}She definitely wants me, but her connection to Mia and her main character 'convictions' are making her feel conflicted.{/i}"
    player "{i}Haha I mean what was with that reasoning for me to feel her up like that?{/i}"
    player "{i}The reason it's okay to do with Mia is because she's my girlfriend.{/i}"
    player "{i}But hey I'm not complaining. Seems as though I'll be able to get even closer to Emily if I just rationalize it enough to her.{/i}"
    player "{i}I wonder if I can use that story Ava and Charlotte told me to my advantage, the one about the candy.{/i}"
    player "{i}She also told me to meet her at school, so I should do that too.{/i}"
    $ emilyphase1interaction2 = 5
    $ emilyquestlog = "That was fucking hot! I knew Emily was a secret slut. I should talk to her again though at school."
    jump passtime

# part 4

label emilyphase1interaction2part4:
    hide screen emily_atschool
    scene fs schoolhallway2extras
    with Dissolve(0.5)

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)

    show fbemily current:
        xalign 0.6 ypos 120

    $ playerSprite = 1
    player "Hey."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh hey."
    $ emilySprite = 0
    if currentchapter == 1:
        $ playerSprite = 1
        player "Banner almost done?"
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Pretty much hehe..."
        $ emilySprite = 4
    player "..."
    emily "..."
    $ playerSprite = 16
    player "It's still kinda awkward isn't it?"
    $ playerSprite = 0
    $ emilySprite = 5
    emily "I know sorry! I'm trying not to let it phase me but it's hard haha."
    $ emilySprite = 1
    emily "I'm not used to...um. Being that physical with someone haha."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Okay this is no good you've just nervous-laughed twice in a row."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "Oh gosh I did didn't I."
    $ emilySprite = 0
    $ playerSprite = 1
    player "What can we do to clear the air? You want to do something later together that's....normal?"
    $ playerSprite = 0
    if currentchapter == 1:
        $ emilySprite = 1
        emily "Yeah I think that's a great idea!"
        emily "Let's see....oh! I do love a scary movie!"
        $ emilySprite = 0
        $ playerSprite = 1
        player "Really? The super intense suspenceful ones or we talking cheesy retro ones."
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Haha DEFINITELY the cheesy ones!"
        emily "Watching a really bad raunchy horror movie is like my FAVORITE thing to do right after eating strawberry ca-"
        $ emilySprite = 2
        player "{i}She was about to say Strawberry Candy.{/i}"
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Uh..*Ahem* anyways."
        emily "But none of the girls will watch them with me UGH!"
        $ emilySprite = 0
        $ playerSprite = 1
        player "Haha yeah I can see how Mia wouldn't want to, she scares super easy. But not even Ava?"
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Ava doesn't get scared like the others but she just rolls her eyes at the bad acting and make-up."
        $ emilySprite = 0
        $ playerSprite = 1
        player "But THAT'S what's so good about them!"
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Right?!"
        emily "Heh...look at you, you're really becoming part of the group. Even name dropped Ava."
        $ emilySprite = 0
        $ playerSprite = 1
        player "Yeah of course. I want to get really close with you girls."
        $ playerSprite = 0
        emily "...."
        $ emilySprite = 1
        emily "Okay...so you're down for a movie then?"
        $ emilySprite = 0
        $ playerSprite = 1
        player "Yup, I'll be sure to find a good one."
        $ playerSprite = 0
        $ emilySprite = 1
        emily "G-Great! Just let me know when!"
        $ emilySprite = 0
        $ playerSprite = 1
        hide fbemily current
        with Dissolve(0.7)
        player "I should head over to the mall to see if I can buy any movies there."
        player "Also...if I'm looking to really take advantage of the situation maybe it'll be worth looking for some candy too...the strawberry kind."
        $ playerSprite = 0
        $ emilyphase1interaction2 = 6
        $ emilyquestlog = "Is Emily becoming a friend? Or do I really just want to fuck her?"
        jump returnwhereyouare
    else:
        $ emilySprite = 1
        emily "Sure!"
        $ emilySprite = 0
        $ playerSprite = 1
        player "Alright I'll contact you soon and we should hang out!"
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Sounds good to me!"
        $ emilySprite = 0
        hide fbemily current
        with Dissolve(0.7)
        $ emilyphase1interaction2 = 6
        $ emilyquestlog = "Is Emily becoming a friend? Or do I really just want to fuck her?"
        jump returnwhereyouare

# end chapter 1

