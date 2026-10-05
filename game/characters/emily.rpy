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
    emily "Thanks you really made this fly by, it would probably take three more days to finish if you weren't here." # grammer hard bruh?
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

# chapter 2
# start

label gohomeemily:
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.32 ypos 120
    charlotte "Yeah me too."
    $ charlotteSprite = 0
    show fbava runfliptalk:
        xalign 0.25 ypos 120
    ava "Alright then girls, thanks again for coming out. Emily I can't thank you enough for the banner."
    show fbava runflip:
        xalign 0.25 ypos 120
    $ emilySprite = 1
    emily "Ohhh i-it was nothing! And [povname] helped me alot with it too!"
    $ emilySprite = 0

    show fbava runfliptalk:
        xalign 0.25 ypos 120
    ava "Well thanks to you both then, I don't know if I would've won if I hadn't seen it."
    show fbava runflip:
        xalign 0.25 ypos 120
    emily "..."
    show fbava current:
        xalign 0.15 ypos 120
    $ playerSprite = 1
    player "No problem Ava."
    $ playerSprite = 0
    $ charlotteSprite = 1
    show fbava runflip:
        xalign 0.25 ypos 120
    charlotte "This is really nice but I'm leaving now, super sweaty."
    image fbcharlotte happytalkflip = im.Flip("Sprites/charlottehappytalk.png", horizontal = True)
    show fbcharlotte happytalkflip:
        xalign 0.4 ypos 120
    charlotte "Byyyyye!"
    $ charlotteSprite = 0
    hide fbcharlotte
    with Dissolve(0.7)
    show fbava runfliptalk:
        xalign 0.25 ypos 120
    ava "Yeah she's right, bye guys!"
    show fbava runflip:
        xalign 0.25 ypos 120
    hide fbava
    with Dissolve(0.7)
    show fbsophia current at surpriseshake:
        xalign 0.5 ypos 120
    sophia "Oh wait Charlotte! Can your driver take me home?!"
    hide fbsophia
    with Dissolve(0.7)
    $ miaSprite = 1
    show fbmia current:
        xalign 0.5 ypos 120
    with move
    mia "I think my mom wanted me to help her with some things tonight so I'm going to leave too."
    $ miaSprite = 0
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.3 ypos 120
    with move
    player "Alright no problem, I'll see you later?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Yeah!"
    show fbmia talkflip:
        xalign 0.5 ypos 120
    mia "Bye guys!"
    show fbmia defaultflip:
        xalign 0.5 ypos 120
    $ emilySprite = 1
    emily "Bye Mia"
    $ emilySprite = 0
    $ oliviaSprite = 1
    olivia "See yah."
    $ oliviaSprite = 0
    hide fbmia
    with Dissolve(0.7)
    emily "{i}Now's my chance!{/i}"
    $ emilySprite = 1
    emily "So Olivia...are you doing anything this evening?"
    $ emilySprite = 0
    $ oliviaSprite = 1
    olivia "Hmm nah."
    olivia "I can just hang out with you guys."
    $ oliviaSprite = 0
    $ emilySprite = 2
    emily "Oh but uhhh...didn't..."
    emily "Didn't you say you were looking forward to playing that new game tonight?"
    $ emilySprite = 0
    $ oliviaSprite = 9
    show fbolivia current at surpriseshake:
        xalign 0.8 ypos 120
    olivia "Shit!"
    olivia "You're right I gotta go bye!"
    hide fbolivia
    with Dissolve(0.7)
    with move
    $ playerSprite = 1
    player "Bye."
    $ playerSprite = 0
    show fbemily current:
        xalign 0.6 ypos 120
    with move
    $ emilySprite = 1
    emily "Hehe have fun!"
    $ emilySprite = 0
    show fbplayer current:
        xalign 0.4 ypos 120
    with move
    $ playerSprite = 11
    player "Woah that was quick."
    $ playerSprite = 4
    player "{i}Is it me or did Emily say that like she wanted Olivia to leave?{/i}"
    $ emilySprite = 1
    emily "Oh you know Olivia! Always keeping on top of those new video game releases!"
    $ emilySprite = 0
    player "...."
    $ emilySprite = 1
    emily "Well!"
    emily "Then there were two huh? Haha."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Hmm...yeah."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "L-Looks like Ava really liked the banner!"
    $ emilySprite = 0
    player "{i}Why is she nervous?{/i}"
    $ playerSprite = 1
    player "Yeah, we did a great job. I'm happy it worked out for both of you."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "[povname]...it wouldn't have happened without you and your help."
    emily "I know I already said thank you a bunch of times..."
    $ emilySprite = 0
    player "{i}Yes here we go...{/i}"
    $ emilySprite = 1
    emily "But it's really not enough."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Emily it's fine. That's what friends do right? Help eachother out?"
    $ playerSprite = 0
    $ emilySprite = 2
    emily "!!!"
    emily "{i}Oh...he's such a good guy!{/i}"
    emily "{i}After all that help he doesn't even want payment...and he clearly shares my feelings about friendship..{/i}"
    emily "{i}And he's so...handsome!{/i}"
    emily "D-Do you have that movie we talked about? A cheesy scary one?"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Yes ma'am. Wolfman 3, bought it the other day. Never seen it!"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh really?! Great!!"
    emily "That one is...perfect. For us to watch..."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Perfect huh?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "*Ahem* sorry I mean...maybe to celebrate, I can come over and w-watch it with you?"
    emily "I mean watch it together. Tonight? Haha..."
    $ emilySprite = 0
    player "{i}Look how flustered she's getting! I've played the part perfectly.{/i}"
    $ playerSprite = 1
    player "Yeah of course, let's head back now and we'll meet at my place in an hour?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yes! Great!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Haha looks like you're really excited."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "{i}Oh gosh Emily what are you doing you dolt!{/i}"
    emily "Sorry um y-yes okay an hour."
    $ emilySprite = 1
    emily "Bye!"
    $ emilySprite = 0
    hide fbemily
    with Dissolve(0.7)
    player "{i}Still not sure how things are going to pan out in the end but it's all coming together perfectly.{/i}"
    player "{i}I should get back home quick.{/i}"
    hide fbplayer
    with Dissolve(0.7)
    pause
    show fbemily current:
        xalign 0.4 ypos 120
    with Dissolve(0.4)
    $ emilySprite = 4
    emily "Hah..hah..okay Em you got this."
    emily "You're n-not gonna go all the way! Just relax. I-It's just setting up a little fantasy!"
    $ emilySprite = 2
    emily "Just to have something to think about while you're touching yourself!"
    emily "Women go bra-less all the time! E-Even if he notices it's not like anything's gonna happen.."
    emily "He's Mia's boyfriend remember! Nothing..."
    emily "Nothing's going to happen.."
    $ emilySprite = 4
    emily "{size=-10}Even if you want it to...{/size}"
    window hide
    pause
    hide fbemily current
    with Dissolve(0.7)
    scene fs livingroomnight
    with Dissolve(0.7)
    player "Alright back home...am I setting out the candy?"
    if candycount != 3:
        player "Yeah. The more options I have to manipulate the situation in my favor the better."
        player "I don't even have to use them if I don't want to. I'll decide in the moment."
    else:
        player "Oh nevermind, I never got any. Maybe I would've had more options at my feet but it's fine."
        "Kyle Mercury" "Just pretend the candy on the couch isn't there.."

    player "Hmmm, here's an idea. Let me turn the thermostat down just a bit."
    player "Being cold is a pretty good reason to get close...physically at least."
    "It wasn't too much longer before you heard the doorbell ring"
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 1
    player "Hey! come on in."
    $ playerSprite = 0
    $ emilySprite = 3
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    emily "Hi!! Hello! Haha um what's up?"
    $ emilySprite = 0
    $ playerSprite = 13
    player "Not much haha, I'm glad you're so excited."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "Ahh, I just-"
    $ emilySprite = 1
    emily "Sorry, I'm just excited for the movie."
    $ emilySprite = 4
    emily "{i}Jeez Louise Emily! Calm down!{/i}"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Not a problem, same here!"
    player "And speaking of, movie's already in the player and ready."
    if candycount !=3:
        player "And I put some snacks on the couch."
    player "Need anything before we start?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Nope I'm fine!"
    $ emilySprite = 0

    scene fs emilychapter1end1
    with Dissolve(1.0)
    "The two of you sit down as the movie plays"
    "It's exactly as you expected, the terrible acting and set pieces were great"
    "And it seemed to be a lot more raunchy then the previous movies, you almost forgot about why you were really there with Emily"
    "But then..."
    scene fs emilychapter1end2
    with Dissolve(1.0)
    emily "Brrr..."
    player "You okay?"
    emily "Yeah...it's just.."
    player "{i}Wait...her nipples are showing through her shirt!{/i}"
    player "{i}She's not wearing a bra hahaha!{/i}"
    scene fs emilychapter1end3
    with Dissolve(1.0)
    player "{i}I gotta keep a straight face!{/i}"
    player "Just what?"
    scene fs emilychapter1end4
    emily "Sorry."
    emily "It's a bit cold, do you have a blanket or can turn the heat up?"
    scene fs emilychapter1end3
    player "Ehh..only blanket I have is on my bed, and the heater is broken. Getting fixed next week."
    scene fs emilychapter1end4
    emily "Oh boy.."
    scene fs emilychapter1end3
    player "You wanna sit in front of me?"
    scene fs emilychapter1end4
    emily "In front of you?"
    scene fs emilychapter1end3
    player "Yeah? I'll hold onto you and we'll both be warm."
    scene fs emilychapter1end3c
    emily "Yup okay."
    player "{i}That was quick.{/i}"
    scene fs emilychapter1end5
    with Dissolve(1.0)
    "She sits in your lap and the movie continues"
    "Just before the third act, the two main characters found a quiet place alone"
    scene fs emilychapter1end6
    with Dissolve(1.0)
    "Movie" "Oh! Oh yes take me now Damian!"
    player "{i}Wow the movie was pretty raunchy the whole time but that still escalated real quick!{/i}"
    "Movie" "Let me see those tits!"
    scene fs emilychapter1end7
    with Dissolve(1.0)
    "Movie" "Uhn uhn Yes! Fuck me!"
    emily "...."
    "Movie" "Fuck me hard!"
    "Movie" "Take that cock baby!"
    player "{i}Emily said she saw this movie before, and that it would be perfect for us to watch.{/i}"
    player "{i}I don't think I'm going to get a bigger signal than this. Plus I'm starting to get hard anyways.{/i}"
    scene fs emilychapter1end8
    player "Wow. They're really going at it huh?"
    scene fs emilychapter1end6
    emily "Huh? O-Oh I don't know I didn't really notice.."
    "Movie" "AHHHH! YES YES UHN RIGHT THERE!!"
    scene fs emilychapter1end6b
    player "Really? Because it looks like at this point they ran out of the budget and decided to just make porn."
    scene fs emilychapter1end7
    "Movie" "Make me cum with your big fucking cock!"
    scene fs emilychapter1end6b
    player "So the acting is pretty terrible, and the directing is even worse."
    scene fs emilychapter1end6
    emily "But?"
    scene fs emilychapter1end6b
    player "But at least the cast is super hot, I mean look at those tits. And that dude is just pounding away at her."
    scene fs emilychapter1end6
    emily "Y-yeah."
    emily "{i}Oh man I'm getting so wet...{/i}"
    scene fs emilychapter1end10
    player "Haha can you imagine going to the movie theatres for this thing?"
    emily "Oh man, all those couples going to see a scary movie?"
    emily "They'd all end up making out and touching eachother haha!"
    scene fs emilychapter1end9
    player "What?"
    player "No!"
    player "They would surely withold temptations!"
    scene fs emilychapter1end10
    with Dissolve(0.7)
    player "For the sanctity of the theatre."
    player "And not..."
    emily "Start...making out?"
    emily "...."
    scene fs emilychapter1end11
    with Dissolve(0.7)
    window hide
    pause
    emily "Mmmm."
    player "Mphm.."
    scene fs emilychapter1end12
    with Dissolve(0.7)
    emily "Hah...hah..."
    player "Hah.."
    scene fs emilychapter1end11
    with Dissolve(0.7)
    emily "{i}Oh my gosh! His tongue is...{/i}"
    emily "{i}So good! And he's touching my boobs...{/i}"
    emily "{i}I feel like I can just let him take me....wait NO!!{/i}"
    scene fs emilychapter1end12
    with vpunch
    emily "W-Wait! Hah...hah.."
    player "You okay?"
    emily "Yes it's just...*ahem*."
    player "{i}Oh I know what's coming.{/i}"
    scene fs emilychapter1end13
    with Dissolve(0.7)
    emily "T-That was really nice. But clearly we've taken it too far."
    emily "{i}Good job Emily! I must be in control of my sexual urges!{/i}"
    player "Uh huh."
    scene fs emilychapter1end14
    with Dissolve(0.7)
    emily "I didn't come over so we can do naughty things."
    emily "You're uh...Mia's boyfriend and she's one of my best friends."
    player "Yeah?"
    emily "Y-Yes and even if we become good friends who are comfortable with eachother there are lines that we shouldn't cross."
    scene fs emilychapter1end15
    with Dissolve(0.7)
    player "Lines like trying to seduce me?"
    emily "Um....yes?"
    scene fs emilychapter1end16
    with Dissolve(0.7)
    player "Lines like making your best friend's lover watch porn with you."
    emily "H-Huh? It's not porn it's just a s-scary movie.."
    scene fs emilychapter1end17
    with Dissolve(1.0)
    player "Like rubbing your ass against my crotch and not wearing a bra to show me your nipples?"
    emily "I...I don't.."
    player "Like some slut?"
    emily "{i}Oh god he took my boobs out!{/i}"
    scene fs emilychapter1end18
    with Dissolve(1.0)
    emily "Ohh..."
    scene fs emilychapter1end18mc
    player "I do have to admit it worked Emily, you have really nice breasts."
    scene fs emilychapter1end18
    emily "{i}This is over the line, we DEFINITELY shouldn't be doing this.{/i}"
    emily "{i}I have to tell him to stop! Why aren't I stopping him??{/i}"
    if candycount != 3:
        menu:
            "{color=#3eab33}Romantic{/color}":
                jump emilyromance1
            "{color=#dd3939}Naughty{/color}":
                jump emilynaughty1
            "{color=#6a4c77}Degradation{/color}":
                jump emilydegredation1
    else:
        menu:
            "{color=#3eab33}Romantic{/color}":
                jump emilyromance1
            "{color=#dd3939}Naughty{/color}":
                jump emilynaughty1


    label emilyromance1:
        scene fs emilychapter1end18mc
        player "God you're so beautiful."
        scene fs emilychapter1end19
        emily "Really? You mean it?"
        scene fs emilychapter1end19mc
        player "I don't think I can keep my feelings for you hidden any longer Emily, if that wasn't obvious by now."
        scene fs emilychapter1end20
        emily "I don't know what to say, I'm s-so confused."
        scene fs emilychapter1end20mc
        player "I kept telling myself there's no way I could like someone like you."
        scene fs emilychapter1end19
        player "{i}There's no denying the power of a main character I suppose.{/i}"
        scene fs emilychapter1end18mc
        player "But I can't keep it inside anymore."
        scene fs emilychapter1end18
        emily "[povname]..."
        scene fs emilychapter1end19mc
        player "Lift your legs."
        scene fs emilychapter1end19
        emily "My legs?"
        scene fs emilychapter1end20mc
        player "I want to make you feel good Emily. Can you let me do that?"
        player "Just for tonight, we'll figure everything out later."
        scene fs emilychapter1end20
        emily "Okay I trust you.."
        scene fs emilychapter1end21
        with vpunch
        emily "Ahhhnnn!!"
        scene fs emilychapter1end18mc
        player "Hehe still trust me?"
        scene fs emilychapter1end18
        emily "Oh you big meanie!"
        scene fs emilychapter1end22
        with Dissolve(1.0)
        emily "Just..hah...go ahead."
        scene fs emilychapter1end23
        with Dissolve(1.0)
        player "Just close your eyes and relax.."
        emily "Oh...oh!!"
        scene fs emilychapter1end24
        emily "{i}He's inside! His finges are inside me agian!{/i}"
        image mcfingeringemilyendch1:
            "CG8-11.png"
            0.5
            "CG8-12.png"
            0.5
            repeat

        show mcfingeringemilyendch1
        player "That feel good?"
        emily "Y-Yeah..."
        player "You like that?"
        emily "{i}I can't believe Mia gets to feel like this all the time!{/i}"
        player "You're so fucking wet. Can you feel my cock getting hard against your ass?"
        emily "Uh huh."
        player "I want you to cum for me Emily, can you do that?"
        emily "Yes.."
        image mcfingeringemilyendch12:
            "CG8-11.png"
            0.15
            "CG8-12.png"
            0.15
            repeat

        show mcfingeringemilyendch12
        emily "Yes!!"
        player "Oh you're getting close! I can feel you."
        emily "Oh GOD!"
        player "Say my name Emily."
        emily "[povname]! [povname] I'm cumming!!!"
        scene fs emilychapter1end25
        with vpunch
        emily "AHNN!!!"
        with flash
        emily "YESYESYES!!!"
        with vpunch
        window hide
        pause
        scene fs emilychapter1end26
        with Dissolve(1.0)
        "Emily passed out after that, she wouldn't wake up so you decided to let her sleep on the couch"
        "You felt vindicated but still a little torn about what the two of you did"
        scene fs blackblank
        with Dissolve(1.0)
        "You're still dating Mia afterall, but you decided to talk it out with Emily later"
        "She was already gone when you woke up next morning"
        "So it looks like you're gonna have to go find her"

        $ endchapter1_trigger = "1 emily romantic"

        jump startofchapter2

    label emilynaughty1:

        scene fs emilychapter1end18
        player "These are some nice tits Emily."
        scene fs emilychapter1end18lookdown
        emily "R-Really?"
        scene fs emilychapter1end19lookdown
        player "Of course, you must be happy about this huh?"
        emily "I don't know what you mean."
        scene fs emilychapter1end19mc
        player "C'mon. You think I don't know what you're up to?"
        player "You're a dirty slut who gets off by fucking her friend's boyfriends."
        scene fs emilychapter1end20lookdown
        emily "W-What? No! I've never done that before in my life!"
        player "Well everybody's got a first time."
        emily "I WOULDN'T ever do that either!"
        show emilyboobs sqeezingemilyboobsmc
        player "Really? So you didn't want me to finger you when you came over the other day?"
        show emilyboobs sqeezingemilyboobs
        emily "I...I didn't...not really.."
        show emilyboobs sqeezingemilyboobsmc
        player "You didn't want me to notice you weren't wearing a bra?"
        player "Weird way to get a guy's attention by the way, I mean it worked don't get me wrong. But weird nonetheless."
        show emilyboobs sqeezingemilyboobs
        emily "Y-You've uhn...you've got it all wrong!"
        show emilyboobs sqeezingemilyboobsmc
        player "Your moaning really isn't helping your case."
        player "You feel my cock yet? I noticed you were rubbing your ass against me."
        show emilyboobs sqeezingemilyboobs
        emily "Yes...I noticed."
        show emilyboobs sqeezingemilyboobsmc
        player "You like making me hard?"
        show emilyboobs sqeezingemilyboobs
        emily "Um..."
        show emilyboobs sqeezingemilyboobsmc
        player "Answer the question."
        show emilyboobs sqeezingemilyboobs
        emily "Yes I admit...I admit I'm a little excited."
        emily "But that's all!"
        show emilyboobs sqeezingemilyboobsmc
        player "Great now we know, you like to make your friend's boyfriend's cocks hard."
        player "Tell me what that makes you."
        show emilyboobs sqeezingemilyboobs
        emily "No! I'm no-"
        show emilyboobs sqeezingemilyboobsmc
        player "Tell me, or I'll call Mia right now and tell her what you're up to."
        show emilyboobs sqeezingemilyboobs
        emily "S-She wouldn't believe you!"
        scene fs emilychapter1end21
        with vpunch
        emily "Ahhhnn! Okay!"
        emily "It...it m-makes me a slut!"
        show emilyboobs sqeezingemilyboobs
        with Dissolve(0.7)
        emily "{i}It's just words Em! It doesn't mean anything!{/i}"
        show emilyboobs sqeezingemilyboobsmc
        player "I love squeezing these nice titties of yours but that's not gonna make you cum is it?"
        show emilyboobs sqeezingemilyboobs
        emily "What?! Cum??"
        player "Lift your legs for me. Right now."
        scene fs emilychapter1end22
        with Dissolve(1.0)
        emily "{i}What am I doing what am I doing what am I doing??!{/i}"
        scene fs emilychapter1end25b
        with Dissolve(1.0)
        emily "Ahh..."
        player "There you go, good girl..."
        scene fs emilychapter1end24
        emily "{i}He's inside! His finges are inside me agian!{/i}"
        image mcfingeringemilyendch1:
            "CG8-11.png"
            0.5
            "CG8-12.png"
            0.5
            repeat

        show mcfingeringemilyendch1
        player "This is what you wanted isn't it?"
        player "Are you happy now hmm?"
        emily "Uhn...ooohh!"
        player "I fucking love hearing you moan, moan louder!"
        emily "Ahh! Uhhn..."
        hide mcfingeringemilyendch1
        show fs emilychapter1end24b
        with vpunch
        emily "MMMMM!!!"
        show mcfingeringemilyendch1
        player "Are you a good girl Emily?"
        emily "W-What?"
        player "Are you going to be a good girl for me??"
        emily "Yes! Yes I'm a good g-girl!"
        image mcfingeringemilyendch12:
            "CG8-11.png"
            0.15
            "CG8-12.png"
            0.15
            repeat

        show mcfingeringemilyendch12
        player "Cum for me like a good girl Emily!"
        emily "{i}Oh God OH GOD I'M CUMMING!!!{/i}"
        scene fs emilychapter1end25
        with vpunch
        player "YES."
        with flash
        emily "UHNNN!!! OHHH GOD!"
        player "There you go! There you go you fucking slut."
        show fs emilychapter1end25c
        with Dissolve(1.0)
        emily "Uhnnn...*sob*...M-Mia..."
        emily "Mia I'm so s-sorry..."
        player "You should be. Cumming from another woman's boyfriend, even though you preach so much about friendship."
        emily "Oh....oh god no..."
        player "You betrayed her Emily, you betrayed all your friends."
        emily "N-No...you..you did t-this..to me."
        player "Em. You could've walked away at any point. I would never force myself on you."
        emily "...."
        player "You know I'm not lying."
        emily "I...I just need to think..and sleep.."
        scene fs emilychapter1end26
        with Dissolve(1.0)
        player "You haven't even asked me to take my fingers out of your pussy."
        emily "....."
        player "She's passed out."
        player "Well I don't think that could've been any better, or gotten any hotter!"
        scene fs blackblank
        with Dissolve(1.0)
        player "Man was it satisfying to see her finally break down."
        player "Fuck me did I ever enjoy that. I'll let her sleep on the couch tonight."
        player "Can't wait to see what tomorrow brings."

        $ endchapter1_trigger = "1 emily naughty"

        jump startofchapter2


    label emilydegredation1:

        scene fs emilychapter1end18
        player "These are some nice tits Emily."
        scene fs emilychapter1end18lookdown
        emily "R-Really?"
        scene fs emilychapter1end19lookdown
        player "Of course, you must be happy about this huh?"
        emily "I don't know what you mean."
        scene fs emilychapter1end19mc
        player "C'mon. You think I don't know what you're up to?"
        player "You're a dirty slut who gets off by fucking her friend's boyfriends."
        scene fs emilychapter1end20lookdown
        emily "W-What? No! I've never done that before in my life!"
        player "Well everybody's got a first time."
        emily "I WOULDN'T ever do that either!"
        show emilyboobs sqeezingemilyboobsmc
        player "Really? So you didn't want me to finger you when you came over the other day?"
        show emilyboobs sqeezingemilyboobs
        emily "I...I didn't...not really.."
        show emilyboobs sqeezingemilyboobsmc
        player "You didn't want me to notice you weren't wearing a bra?"
        player "Weird way to get a guy's attention by the way, I mean it worked don't get me wrong. But weird nonetheless."
        show emilyboobs sqeezingemilyboobs
        emily "Y-You've uhn...you've got it all wrong!"
        show emilyboobs sqeezingemilyboobsmc
        player "Your moaning really isn't helping your case."
        player "You feel my cock yet? I noticed you were rubbing your ass against me."
        show emilyboobs sqeezingemilyboobs
        emily "Yes...I noticed."
        show emilyboobs sqeezingemilyboobsmc
        player "You like making me hard?"
        show emilyboobs sqeezingemilyboobs
        emily "Um..."
        show emilyboobs sqeezingemilyboobsmc
        player "Answer the question."
        show emilyboobs sqeezingemilyboobs
        emily "Yes I admit...I admit I'm a little excited."
        emily "But that's all!"
        show emilyboobs sqeezingemilyboobsmc
        player "Great now we know, you like to make your friend's boyfriend's cocks hard."
        player "Tell me what that makes you."
        show emilyboobs sqeezingemilyboobs
        emily "No! I'm no-"
        show emilyboobs sqeezingemilyboobsmc
        player "Tell me, or I'll call Mia right now and tell her what you're up to."
        show emilyboobs sqeezingemilyboobs
        emily "S-She wouldn't believe you!"
        scene fs emilychapter1end21
        with vpunch
        emily "Ahhhnn! Okay!"
        emily "It...it m-makes me a slut!"
        show emilyboobs sqeezingemilyboobs
        with Dissolve(0.7)
        emily "{i}It's just words Em! It doesn't mean anything!{/i}"
        show emilyboobs sqeezingemilyboobsmc
        player "I love squeezing these nice titties of yours but that's not gonna make you cum is it?"
        show emilyboobs sqeezingemilyboobs
        emily "What?! Cum??"
        player "Lift your legs for me. Right now."
        scene fs emilychapter1end22
        with Dissolve(1.0)
        emily "{i}What am I doing what am I doing what am I doing??!{/i}"
        scene fs emilychapter1end25b
        with Dissolve(1.0)
        emily "Ahh..."
        player "There you go, good girl..."
        scene fs emilychapter1end24
        emily "{i}He's inside! His finges are inside me agian!{/i}"
        image mcfingeringemilyendch1:
            "CG8-11.png"
            0.5
            "CG8-12.png"
            0.5
            repeat

        show mcfingeringemilyendch1
        player "This is what you wanted isn't it?"
        player "Are you happy now hmm?"
        emily "Uhn...ooohh!"
        player "I fucking love hearing you moan, moan louder!"
        emily "Ahh! Uhhn..."
        hide mcfingeringemilyendch1
        show fs emilychapter1end24b
        with vpunch
        emily "MMMMM!!!"
        show mcfingeringemilyendch1
        player "Are you a good girl Emily?"
        emily "W-What?"
        player "Are you going to be a good girl for me??"
        emily "Yes! Yes I'm a good g-girl!"
        image mcfingeringemilyendch12:
            "CG8-11.png"
            0.15
            "CG8-12.png"
            0.15
            repeat

        show mcfingeringemilyendch12
        player "Cum for me like a good girl Emily!"
        emily "{i}Oh God OH GOD I'M CUMMING!!!{/i}"
        scene fs emilychapter1end25
        with vpunch
        player "YES."
        with flash
        emily "UHNNN!!! OHHH GOD!"
        player "There you go! There you go you fucking slut."
        show fs emilychapter1end25c
        with Dissolve(1.0)
        emily "Uhnnn...*sob*...M-Mia..."
        emily "Mia I'm so s-sorry..."
        player "You should be. Cumming from another woman's boyfriend, even though you preach so much about friendship."
        emily "Oh....oh god no..."
        player "You betrayed her Emily, you betrayed all your friends."
        emily "N-No...you..you did t-this..to me."
        player "Em. You could've walked away at any point. I would never force myself on you."
        emily "...."
        player "You know I'm not lying."
        emily "I...I just need to think..and sleep.."
        scene fs emilychapter1end26
        pause
        scene fs emilychapter1end26
        with vpunch
        player "Oh no you don't!"
        scene fs emilychapter1end25
        with vpunch
        emily "AHNN! W-What?"
        scene fs emilychapter1end25b
        player "You think we're just going to end it there?!"
        scene fs blackblank
        with Dissolve(0.7)
        player "Get on your knees."
        emily "N-No I-"
        player "GET on your FUCKING knees right now."
        scene fs emilychapter1deredationend1b
        with Dissolve(0.7)
        emily "W-Why do you want me here?!"
        scene fs emilychapter1deredationend1
        player "You really think it's fair?"
        scene fs emilychapter1deredationend1b
        emily "What's fair?"
        scene fs emilychapter1deredationend1c
        emily "Wait why do you have your phone out??!"
        scene fs emilychapter1deredationend1
        player "I'll get to that in a bit don't worry."
        player "But fair that you get to cum, and I don't?!"
        scene fs emilychapter1deredationend1b
        emily "I..I don't..what are you talking about?"
        scene fs emilychapter1deredationend1
        player "You come over here, take advantage of me."
        scene fs emilychapter1deredationend1b
        emily "I didn't take advant-"
        scene fs emilychapter1deredationend1
        player "TAKE ADVANTAGE OF ME. So that we both cheat on Mia, but you're the only one who gets off?!"
        player "Do you even know what blue balls is?"
        scene fs emilychapter1deredationend1b
        emily "I...I do."
        scene fs emilychapter1deredationend1
        player "You can't seduce me, make me rock hard, cum all over my hand then leave like some whore."
        scene fs emilychapter1deredationend1c
        with vpunch
        emily "I'm not a whore!!"
        emily "{i}I really made his penis rock hard?{/i}"
        emily "Stop twisting the situation with your words!!"
        scene fs emilychapter1deredationend1
        player "Okay look. First have some of this."
        scene fs emilychapter1deredationend2
        emily "Huh?"
        player "It's just candy, I bought some for movie night."
        scene fs emilychapter1deredationend2b
        emily "Oh..n-no this is strawbe-"
        player "Just eat the fucking candy and calm down alright?"
        emily "...."
        scene fs emilychapter1deredationend3
        emily "*munch munch*"
        player "{i}Yes...yes that's it you fucking slut!{/i}"
        scene fs emilychapter1deredationend1
        player "Good."
        emily "...."
        scene fs emilychapter1deredationend5
        player "Now you're going to suck my cock."
        emily "W-W-Wha.."
        emily "{i}Oh my god it's HUGE!{/i}"
        emily "...."
        player "Impressed I see."

        scene fs emilychapter1deredationend6
        emily "No!"
        scene fs emilychapter1deredationend6c
        emily "I'm just surprised that there's a penis in my face."
        scene fs emilychapter1deredationend6b
        player "Didn't think you were a liar Em."
        scene fs emilychapter1deredationend5
        emily "Okay maybe...maybe it is big but that's not the point!"
        scene fs emilychapter1deredationend6b
        player "Are you done talking? I'm still waiting."
        scene fs emilychapter1deredationend6c
        emily "Okay but..but first can I..."
        scene fs emilychapter1deredationend6b
        player "Can you what?"
        scene fs emilychapter1deredationend6c
        emily "Can I have another piece of candy?"
        scene fs emilychapter1deredationend6b
        player "The hell? Read the mood. No, get more after."
        scene fs emilychapter1deredationend6c
        emily "P-Please? I uh...I would really-"
        scene fs emilychapter1deredationend6b
        player "I'm getting fucking soft now Jesus Christ. Talk dirty, get me hard and suck me off. THEN you'll get some more candy."
        scene fs emilychapter1deredationend6c
        emily "I-I can have more after then?"
        scene fs emilychapter1deredationend6b
        player "If you make me cum you can take the whole damn bowl now hurry the hell up!"
        scene fs emilychapter1deredationend5
        emily "Okay....okay I can..hah.."
        scene fs emilychapter1deredationend7
        emily "Mmm."
        player "Yeah there you go...using your tongue already? I like that."
        emily "{i}It tastes strange...but I don't dislike it..{/i}"
        emily "{i}He wanted me to talk dirty..{/i}"
        scene fs emilychapter1deredationend6c
        with Dissolve(0.7)
        emily "I...I like how big it is!"
        scene fs emilychapter1deredationend6b
        player "Haha yeah?"
        scene fs emilychapter1deredationend6c
        emily "I can't believe you..you.."
        scene fs emilychapter1deredationend6b
        player "Fuck."
        scene fs emilychapter1deredationend6c
        emily "Y-You fuck Mia with this massive thing."
        scene fs emilychapter1deredationend5
        emily "You would stretch me out so much."
        player "Yeah...okay that's getting me going. Keep sucking."
        scene fs emilychapter1deredationend7
        with Dissolve(0.7)
        emily "Mphm."
        player "Deeper!"
        scene fs emilychapter1deredationend8
        emily "MUUUGH!"
        player "Oh fuck that's good, keep going."
        scene fs emilychapter1deredationend7
        emily "Ugh."
        scene fs emilychapter1deredationend8
        emily "MMMM!"
        player "Go deeper you fucking slut."
        player "Mia deepthroats it and she's not even a whore like you are."
        emily "Ehm nuh ahoore!"
        player "I told you."
        scene fs emilychapter1deredationend9
        player "To fucking go.."
        scene fs emilychapter1deredationend10
        with vpunch
        player "DEEPER!"
        emily "EUG!!"
        window hide
        pause
        player "YES HOLY SHIT!"
        emily "EHHHMMM!"
        player "Your throat is so small, feels so fucking good."
        player "Keep sucking baby come on!"
        emily "{i}He called me baby! I-I'm actually liking this.{/i}"
        emily "{i}He's being so rough and mean, and I can barely breath but I..I'm so turned on!{/i}"
        scene fs emilychapter1deredationend9
        player "God damn I'm getting close Emily. I think you should be rewarded don't you?"
        emily "Huu?"
        scene fs emilychapter1deredationend10
        with vpunch
        player "{i}Fuck I can feel her throat constricting my cock!{/i}"
        player "Good girls get rewarded, are you a good girl?"
        scene fs emilychapter1deredationend9
        emily "Ah...Ahm eh guu gurl!"
        scene fs emilychapter1deredationend10
        player "Again."
        emily "AHM EH GUD GUURL!"
        window hide
        scene fs emilychapter1deredationend11
        with vpunch
        pause
        player "AHH YESS FUCK!"
        window hide
        with flash
        pause
        player "Right down your fucking throat! Swallow it!"
        emily "*Gulp* *Gulp* *Gulp*"
        emily "{i}There's so much! It's everywhere I'm going to pass out!{/i}"
        player "It's getting all over your cute little face and tits."
        emily "{i}Why?! Why d-does it taste so good??{/i}"
        with flash
        player "Haha I should stop before you pass out huh?"
        scene fs emilychapter1deredationend12
        with Dissolve(1.0)
        window hide
        pause
        emily "Gah! Hah...hah.."
        emily "*cough* *cough*"
        player "That was amazing. Better than Mia ever did."
        emily "!!!"
        player "{i}She won't say it but that just made her really happy, I can tell.{/i}"
        player "You look so sexy covered in my cum Emily."
        emily "R-Really?"
        player "Really. Seeing it drip off your tits is even keeping me hard."
        emily "...."
        player "Go ahead and take the candy with you after you wash up."
        emily "...."
        player "We'll meet up soon, obviously we have some things to talk about."
        emily "Okay."
        player "Bathrooms down the hall to the left."
        emily "Thank you."
        scene fs blackblank
        with Dissolve(1.0)
        "Emily didn't say a word to you as she grabbed the candy and left after washing up."
        "You could tell she was absolutely ashamed and yet still turned on, a combination you were very happy with"
        player "That worked out perfectly. And now I have a recording to use later, should come in handy."
        player "Haha now that I think about it I forgot to give her a reason why I was filming, meh."
        player "Gotta be honest though I wasn't lying about that blowjob blowing(heh) my mind."
        player "Her tiny throat really did feel amazing and when it was twitching, trying to breath..."
        player "Damn that sent me over the edge for sure. I really wouldn't mind continuing...whatever this is."
        player "Kinda feels like it makes me a villain but hey. Sometimes it's fun to be the 'Bad guy'."
        $ endchapter1_trigger = "1 emily degredation"

        jump startofchapter2

# interaction 1
# part 1
label emilyphase2interaction1part1:
    hide screen emily_atschool

    $ avaSprite = 0
    $ sophiaSprite = 0
    $ charlotteSprite = 0
    $ oliviaSprite = 0

    scene fs schoolhallway2
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ emilySprite = 1
    emily "Woah uh-hey!"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Hey!"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "I...um..."
    $ playerSprite = 1
    $ emilySprite = 0
    player "It's nice to...uh."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Ava's race! She did so well."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Yeah she really did, great job on the banner once again."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "C'mon [povname] you already know I couldn'tve done it without you."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Even so, congrats."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Thanks."
    $ playerSprite = 1
    $ emilySprite = 0
    player "It was nice meeting Josy, I didn't know she was friends with Katie."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yeah yeah she's....nice."
    $ playerSprite = 1
    $ emilySprite = 0
    player "I'll probably start seeing her a bunch soon."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "W-What?? Why?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Uh...isn't she friends with Katie?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Huh?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "You know. My girlfriend's sister?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "OH! Oh yeah, yeah yeah sorry."
    $ emilySprite = 0
    emily "..."
    $ playerSprite = 1
    player "Haha we're doing it again aren't we?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Heh yeah we are, aren't we?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Listen let's get out of this hallway, this room is empty right now right?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yeah I think it's free."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Alright let's go."
    $ playerSprite = 0
    scene fs classroom
    with Dissolve(0.5)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 1
    player "There. Now we can talk."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Y-Yeah."
    $ playerSprite = 1
    $ emilySprite = 0
    player "You can relax Emily, let's try and make this a no-pressure conversation."
    player "We can just say what we want to say and go from there."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Sorry you're right. I just don't really know...what to expect."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Haha did you think I wanted you alone to make out or something?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "I...I dunno! M-Maybe? I'm new to this!"
    $ playerSprite = 1
    $ emilySprite = 0
    player "New to what?"
    $ playerSprite = 0
    $ emilySprite = 2
    emily "I don't know!!"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Okay okay, you go first. Get everything off your chest."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Okay well, you know how after you got me that paint to help me with the banner I hugged you and.."
    emily "Well we kinda took things in a...naughty direction?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "How could I forget?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Haha...um well I was kinda overwhelmed at the time, lots of emotions were going through me you know?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "You saying it was a mistake then?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yes, it was."
    emily "But...I liked it."
    emily "And when I went home and had time to realise what uh...I let you do to me-"
    $ playerSprite = 1
    $ emilySprite = 0
    player "It really wasn't all that big a de-"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "It was [povname]! It IS. To ME....f-fingering your..."
    emily "Someone who isn't your girlfriend is NOT something you do. It's not right."
    $ playerSprite = 1
    $ emilySprite = 0
    player "...But?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "But I wasn't upset. I-In fact I think I enjoyed it."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Well I am pretty good if I do say so myself."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "N-No! I mean like I enjoyed the ACT of...doing something I shouldn't have."
    $ playerSprite = 11
    $ emilySprite = 0
    player "...."
    $ emilySprite = 2
    emily "And that scares me!"
    emily "God PLEASE don't tell anyone I said that I would just die..."
    $ emilySprite = 4
    player "{i}Okay this is a big development, she just admitted to being turned on by being with me.{/i}"
    $ playerSprite = 1
    player "Okay. Go on."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "T-That's pretty much as far as I got. I'm kind of wrestling with these feelings."
    emily "I don't want anyone to get hurt! Especially Mia!"
    $ playerSprite = 1
    $ emilySprite = 4
    player "Okay, you said what you wanted to say?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Um, yeah pretty much."
    $ playerSprite = 1
    $ emilySprite = 0
    player "{i}Alright, now all I have to do is phrase this right and I think I've got this!{/i}"
    player "Firstly, yes I agree. I also don't want Mia to get hurt."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Okay."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Secondly, I'm going to be fully honest here. I did not like you when we first met."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "I...um okay."
    $ playerSprite = 1
    $ emilySprite = 0
    player "From what Mia told me and talking to you, I really thought that our personalities did not match up."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh.."
    $ playerSprite = 1
    $ emilySprite = 0
    player "But, after getting to know you, and finding out how...authentic you are, I realised that I actually do like you."
    player "Like a lot. And even if I tried to deny it in the past I'm extremely attracted to you."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "I eh um o-okay! Thank you."
    $ emilySprite = 0
    player "{i}I won't mention the idea of fucking the shit out of her while still dating Mia gets me hard as diamonds.{/i}"
    $ playerSprite = 1
    player "So. Where do we go from here right?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Um yeah. I don't know."
    $ playerSprite = 1
    $ emilySprite = 0
    player "I have a proposition."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Sure."
    $ playerSprite = 1
    $ emilySprite = 0
    player "It would be a disservice to ourselves, and even Mia, if we were to stop whatever relationship we have now."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "I don't know..."
    $ playerSprite = 1
    $ emilySprite = 4
    player "Let me land."
    player "Let's say we're meant to be together, but I end up staying with Mia and you don't get with me."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Okay..."
    $ playerSprite = 1
    $ emilySprite = 4
    player "My thoughts are about you when I'm with her. I'm looking at her face and thinking of yours. We're having sex and I-"
    $ playerSprite = 0
    $ emilySprite = 2
    emily "O-Okay okay I get it!!"
    $ playerSprite = 1
    $ emilySprite = 4
    player "Haha, so you really think that's fair to Mia. Or really anyone else I would be with?"
    $ playerSprite = 0
    $ emilySprite = 2
    emily "No..."
    emily "You really like me that much?"
    $ emilySprite = 0
    player "{i}Oh baby you're making this too easy Emily!{/i}"
    $ playerSprite = 1
    player "I do Em."
    $ playerSprite = 0
    emily "{i}He called me Em!{/i}"
    $ playerSprite = 1
    $ emilySprite = 0
    player "So! The proposition. You and me continue to...figure things out. Spend time together."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Date?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "If you want to call it that."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Hehe."
    $ playerSprite = 1
    $ emilySprite = 0
    player "And we see where things go, if we realize we want to be together forever and fuck like rabbits."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "[povname]! N-Not so loud!!"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Haha, if we realize that then I'll break up with Mia, cleanly."
    player "Then not long after we can announce that we're a couple, we can even go to Mia first."
    player "It might be a bit awkward but at this point if we get together it's going to be awkward no matter what, but this way we avoid anyone getting hurt."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Okay that....makes sense."
    emily "But what about if w-"
    $ playerSprite = 1
    $ emilySprite = 0
    player "If we DON'T work out, well then it'll be our little secret. We tried something and learned that it wasn't meant to be."
    player "I stay with Mia, you can date whomever you like, nobody gets hurt and life moves on."
    $ playerSprite = 0
    emily "...."
    $ emilySprite = 1
    emily "That's...a good idea."
    emily "But what if we...like get caught? I can't lie to my friends!"
    emily "L-Like directly."
    $ playerSprite = 1
    $ emilySprite = 0
    player "That's the weakest part of the plan. We just have to be smart about it so nobody misunderstands."
    player "Just some careful planning about when we meet up is all."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Ehhh....okay."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Don't tell me you aren't looking forward to that."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "I do like organizing and planning.."
    $ playerSprite = 1
    $ emilySprite = 0
    player "And from what I hear you're one of the best at it."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Hehe thanks."
    $ playerSprite = 1
    $ emilySprite = 0
    player "I know it'll be hard but you'll have to stop yourself from kissing me while we're hanging out with everybody."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "Wha-"
    emily "Hey I'm not gonna do that!"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Hahaha."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh geez [povname]!"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Sorry. So we're good?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "I think we're good. I'm good."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Great. Glad that we talked about this."
    player "{i}And I'm glad I pretty much have permission to get into your pants eventually.{/i}"
    player "Shall we go?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yeah! Let's go."
    emily "Thanks [povname]. I'm happy you thought of this."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Me too Em."
    player "Let's get outta here."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yes let's. Just remember, we can't get caught!"

    scene fs schoolhallway2
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.2 ypos 120
    show fbemily current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    emily "We have to be extra careful when we're togeth-"
    show fbava current behind fbemily:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    $ avaSprite = 1
    ava "Hey guys!"
    $ avaSprite = 0
    show fbemily current at surpriseshake:
        xalign 0.4 ypos 120
    emily "Gah!"
    show fbemily current:
        xalign 0.48 ypos 120
    with move
    emily "Ava! Oh hehe hi!"
    $ avaSprite = 1
    $ emilySprite = 0
    ava "Sorry didn't mean to scare yah! Haha."
    ava "What were you two doing?"
    $ avaSprite = 0
    $ emilySprite = 2
    emily "Uhhh um we..."
    show fbsophia current:
        xalign 0.07 ypos 120
    with Dissolve(0.5)
    $ sophiaSprite = 1
    sophia "[povname]! Oh and Ava and Emily!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Hey Soph."
    $ playerSprite = 0
    $ sophiaSprite = 1
    sophia "What are you guys up to?"
    $ sophiaSprite = 0
    show fbplayer current:
        xalign 0.05 ypos 120
    show fbsophia current:
        xalign 0.2 ypos 120
    with move
    $ playerSprite = 1
    player "We're just hanging out. Thinking about maybe organizing a get together to celebrate Ava's win."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Whaaaat??"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Isn't that right Emily?"
    $ emilySprite = 1
    emily "Oh uh yeah yeah we uh-"
    $ emilySprite = 0
    $ sophiaSprite = 1
    sophia "That sounds like fun!"
    $ sophiaSprite = 0
    $ emilySprite = 0
    show fbcharlotte current:
        xalign 0.47 ypos 120
    show fbolivia current:
        xalign 0.62 ypos 120
    with Dissolve(0.5)
    show fbsophia current:
        xalign 0.15 ypos 120
    show fbava current:
        xalign 0.2 ypos 120
    show fbemily current:
        xalign 0.35 ypos 120
    with move
    $ charlotteSprite = 1
    charlotte "I'm just saying it would do wonders for your pores Olivia."
    $ charlotteSprite = 0
    $ oliviaSprite = 1
    olivia "I'm not doing it Charlotte."
    $ oliviaSprite = 0
    $ charlotteSprite = 1
    charlotte "Everyone else went with me!"
    charlotte "Oh! Hey girls. And [povname]."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Charlotte. Olivia."
    $ playerSprite = 0
    $ emilySprite = 2
    emily "H-Hi!"
    $ emilySprite = 0
    $ sophiaSprite = 1
    sophia "What were you guys talking about?"
    $ sophiaSprite = 0
    $ charlotteSprite = 1
    charlotte "I'm trying to convince Olivia to go to the full day spa with me. She's the only one of the group who hasn't gone."
    $ charlotteSprite = 0
    $ oliviaSprite = 1
    olivia "I don't need it and it's too expensive."
    $ oliviaSprite = 0
    $ charlotteSprite = 1
    charlotte "You ABSOLUTELY need it and I told you I would pay!"
    charlotte "Cooped up in your home all day with that awful roomate..."
    $ avaSprite = 1
    $ charlotteSprite = 0
    ava "I think you should go Olivia, I didn't think I'd like it either but it was awesome."
    $ avaSprite = 0
    $ sophiaSprite = 1
    sophia "Yeah it was really relaxing when she took me."
    $ sophiaSprite = 0
    $ avaSprite = 1
    ava "They gave me a brazilian!"
    $ avaSprite = 0
    $ emilySprite = 1
    emily "Ava..."
    $ emilySprite = 0


    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    $ miaSprite = 1
    mia "Did somebody say Brazilian?!"
    $ playerSprite = 1
    $ miaSprite = 0
    player "Mia!"

    hide fbplayer current
    show fbmia mcmiamakeout:
        xpos 300 ypos 120
    with Dissolve(0.5)
    mia "Mmmmm!"
    $ emilySprite = 4
    emily "...."
    $ avaSprite = 1
    ava "Geez guys get a room already haha!"
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "Or better yet just stop. Like forever."
    $ charlotteSprite = 0
    sophia "{i}This is kinda hot...{/i}"
    olivia "{i}Fucking bullshit OP broken boss level...{/i}"

    show fbmia current:
        xpos 290 ypos 120
    show fbplayer current behind fbmia:
        xpos -60 ypos 120
    with Dissolve(0.5)

    $ miaSprite = 1
    $ playerSprite = 0
    mia "So what's everyone doing here?"
    $ miaSprite = 0
    $ charlotteSprite = 1
    charlotte "Um..."
    $ charlotteSprite = 0
    $ sophiaSprite = 1
    sophia "What were we doing here?"
    $ sophiaSprite = 0
    $ oliviaSprite = 1
    olivia "We were all in line to kiss [povname] but you cut in front."
    $ oliviaSprite = 0
    $ avaSprite = 14
    $ sophiaSprite = 7
    $ charlotteSprite = 8
    $ emilySprite = 2
    $ playerSprite = 13
    "Everyone" "!!!!"
    $ miaSprite = 1
    show fbmia current:
        xzoom -1.0
    mia "Oh! Really?"
    mia "Sorry guys-"
    $ charlotteSPrite = 1
    $ miaSprite = 0
    charlotte "Nononono!"
    show fbsophia current at surpriseshake:
        xzoom -1.0
    sophia "Olivia!!"
    $ emilySprite = 1
    emily "Oh my gosh."
    $ oliviaSprite = 14
    $ emilySprite = 9
    olivia "Hahahaha!"
    $ avaSprite = 1
    show fbava current:
        xalign 0.3 xzoom -1.0
    ava "You sneaky bitch haha!"
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "Mia that is NOT what was happening don't believe her lies!"
    $ charlotteSprite = 0
    player "Hahaha."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Oh okay?"
    $ miaSprite = 0
    $ sophiaSprite = 1
    sophia "Sometimes Olivia geez...."
    olivia "Okay sorry sorry."
    $ emilySprite = 1
    show fbemily current:
        xalign 0.4 xzoom -1.0
    emily "I gotta admit that was a good one!"
    emily "Next time tho-"

    "???" "Well well well."

    $ stephanieSprite = 0
    $ ravenSprite = 0
    $ melissaSprite = 0

    show fbstephanie current:
        xalign 0.75 ypos 120
    show fbraven current behind fbstephanie:
        xalign 0.86 ypos 120
    show fbmelissa current:
        xalign 0.98 ypos 120
    with Dissolve(0.7)
    $ stephanieSprite = 1
    stephanie "Look who it is girls."
    stephanie "The whole gang is here."
    $ stephanieSprite = 0
    $ playerSprite = 11
    player "Huh?"

    $ oliviaSprite = 2
    $ sophiaSprite = 3
    $ avaSprite = 15
    $ emilySprite = 4

    show fbplayer current:
        xalign 0.5 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    show fbmia current:
        xalign 0.42 ypos 120
    show fbsophia current:
        xalign 0.06 ypos 120
    show fbolivia current behind fbsophia:
        xalign 0.12 xzoom -1.0 ypos 120
    show fbcharlotte current behind fbsophia:
        xalign 0.25 xzoom -1.0 ypos 120
    show fbava current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    pause

    $ stephanieSprite = 1
    stephanie "All the losers in one place!"
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "Hahaha!"
    $ melissaSprite = 0
    raven "..."
    $ emilySprite = 5
    emily "Stephanie."
    emily "Looks like you're back from your trip."
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Yeah just got back yesterday. It's too bad you'll never experience a big tropical Cruise this time of year."
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "We rubbed elbows with like, a BUNCH of rich business people."
    $ melissaSprite = 0
    $ stephanieSprite = 1
    stephanie "Charlotte, I think I saw your parents there? I was so confused because MY parents brought me with them."
    stephanie "And my friends too!"
    $ stephanieSprite = 0
    $ charlotteSprite = 5
    charlotte "Yeah I..."
    charlotte "I wanted to stay here."
    $ melissaSprite = 1
    melissa "Haha sure you did!"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Heh."
    $ ravenSprite = 0
    $ stephanieSprite = 1
    stephanie "Awww, well maybe next time."
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "Or not! Hehehe."
    $ melissaSprite = 0
    player "{i}What the fuck is going on?{/i}"
    show fbemily upsetfliptalk:
        xalign 0.6 ypos 120
    emily "Charlotte, don't bother with them."
    $ emilySprite = 5
    show fbemily current
    emily "What do you want Stephanie?"
    $ emilySprite = 4
    $ stephanieSprite = 1
    stephanie "Why I only wanted to stop by and say hi!"
    $ stephanieSprite = 0
    $ sophiaSprite = 4
    sophia "Oh please, you just wanted to gloat that you went on that trip after you LOST to Emily for student council president two weeks ago!"
    $ sophiaSprite = 3
    $ avaSprite = 1
    ava "It was a landslide VICTORY if I remember correctly."
    $ avaSprite = 0
    $ stephanieSprite = 1
    stephanie "Oh PLEASE I just ran for fun."
    stephanie "Like I care about losing some stupid council contest to some stupid council girl."
    stephanie "Besides, I got vice-president didn't I?"
    stephanie "I simply didn't want our school to be a dictatorship. Alas democracy fell with thunderous applause."
    $ stephanieSprite = 0
    $ charlotteSprite = 0
    charlotte "Ugh."
    olivia "Didn't your parents spend a shit ton of money to bribe students, and you cried your eyes out in front of everyone?"
    stephanie "...."
    $ stephanieSprite = 1
    stephanie "There is NO evidence that any coercion took place."
    stephanie "And I was just like...emotional, it was my time of the month it had nothing to do with winning or losing!"
    $ stephanieSprite = 0
    $ avaSprite = 1
    ava "Yeah we ALL believe you."
    $ avaSprite = 0
    $ stephanieSprite = 5
    stephanie "Listen here you litt-"
    $ stephanieSprite = 4
    stephanie "...."
    "Everyone" "...."
    $ stephanieSprite = 3
    stephanie "Who is that?"
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "Wait yeah, did that guy just get here?"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "He's been here the whole time Melissa."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Uh hey, I'm [povname]."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Emily. No WAY did you get a boyfriend while I was gone??"
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "NGL he kinda cute."
    $ melissaSprite = 0
    raven "...."
    $ emilySprite = 5
    emily "What? N-No!"
    emily "He's Mia's boyfriend!"
    $ emilySprite = 4
    stephanie "....."
    $ stephanieSprite = 1
    stephanie "Mia?"
    stephanie "Like MIA Mia?"
    $ stephanieSprite = 0
    $ miaSprite = 1
    mia "Hi!"
    $ miaSprite = 0
    $ melissaSprite = 1
    melissa "Big titty dum-dum over here?"
    $ melissaSprite = 0
    $ miaSprite = 13
    mia "Hey!"
    $ miaSprite = 12
    mia "...."
    $ miaSprite = 11
    show fbmia current:
        xalign 0.47
    mia "You have big tits too!"
    $ miaSprite = 12
    show fbmia current:
        xalign 0.42
    melissa "...."
    $ melissaSprite = 1
    melissa "Oh yeah."
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Jesus Christ."
    $ ravenSprite = 0
    $ stephanieSprite = 1
    stephanie "Well. I gotta congratulate you then, you're actually dating someone who's kinda hot."
    stephanie "Even if it's....obvious why."
    $ stephanieSprite = 0
    $ miaSprite = 0
    mia "Hmm?"
    $ stephanieSprite = 1
    stephanie "It's not for your personality honey, is what I'm saying."
    $ stephanieSprite = 0
    $ avaSprite = 16
    ava "Alright that's too far I am gonna beat the shit ou-"
    $ avaSprite = 0
    $ emilySprite = 5
    emily "Hold on hold on Ava. We don't need to fall for her dumb provacations. We are above that."
    $ emilySprite = 4
    show fbplayer current:
        xalign 0.65 ypos 120
    with move
    $ playerSprite = 5
    player "If I may add something."
    player "It's not exactly a secret that my girlfriend is hot. And I'm not exactly hiding the fact that I'm attracted to how hot she is."
    $ playerSprite = 4
    $ stephanieSprite = 4
    stephanie "O-Okay?"
    $ playerSprite = 5
    player "And I also happened to LIKE her personality. In fact, I fuck her every chance I GET because I like her personality so much."
    $ playerSprite = 4
    show fbstephanie current:
        xalign 0.78 ypos 120
    with move
    stephanie "O-Oh I uh-"
    $ playerSprite = 5
    player "And where's YOUR boyfriend?"
    $ playerSprite = 4
    stephanie "Huh? I d-don't want to be tied down right n-"
    $ playerSprite = 5
    player "Yeah I didn't think so. You and your friends here have the personality of a two-bit cartoon villain."
    player "And I'm guessing you don't have the maturity or ability to have a serious relationship with someone."
    player "I mean seriously? I swear to God I've seen this exact scene in a movie somewhere. You should watch out for busses."
    player "How could anyone over the age of 12 think you're intimidating like at ALL?"
    $ playerSprite = 4
    player "{i}Well actually I could think of one group who'd actually entertain their bullshit.{/i}"
    $ playerSprite = 5
    player "So why don't you and your two friends shut the fuck up, grow the fuck up, and get the fuck out of our faces?"
    $ playerSprite = 4
    "Emily Mia Ava Charlotte Olivia and Sophia" "...."
    "Raven Melissa and Stephanie" "...."
    $ melissaSprite = 1
    $ stephanieSprite = 0
    melissa "Is it weird that I'm seriously turned on right now?"
    $ melissaSprite = 0
    $ ravenSprite = 1
    show fbraven current:
        xzoom -1.0
    raven "Oh my God Melissa!"
    $ ravenSprite = 0
    $ melissaSprite = 1
    melissa "What?! That was hot!"
    $ melissaSprite = 0
    $ stephanieSprite = 1
    show fbraven current:
        xzoom 1.0
    stephanie "Wow. Looks like you got a real keeper Emily."
    $ ravenSprite = 1
    raven "Mia."
    $ ravenSprite = 0
    $ stephanieSprite = 1
    stephanie "Right Mia."
    stephanie "I like a man who...can take charge."
    $ stephanieSprite = 0
    $ playerSprite = 5
    player "Were you listening to like anything I said?"
    $ playerSprite = 4
    $ stephanieSprite = 1
    stephanie "Sure whatever. Alright girls let's leave these losers to whatever pathetic plans they were making."
    stephanie "I look forward to seeing you later Mr. White knight."
    $ stephanieSprite = 0
    show fbstephanie current:
        xalign 1.5 ypos 120
    with move
    $ playerSprite = 5
    player "Please do NOT call me that."
    $ playerSprite = 4
    $ melissaSprite = 1
    melissa "Byyyye [povname]! Maybe call me?"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "He doesn't have your number Mel."
    $ ravenSprite = 0
    $ melissaSprite = 1
    melissa "Oh right, I'll call you!"
    $ melissaSprite = 0
    show fbmelissa current:
        xalign 1.5 ypos 120
    with move
    $ ravenSprite = 1
    raven "*Sigh*"
    $ ravenSprite = 0
    raven "...."
    "Everyone" "...."
    $ ravenSprite = 1
    raven "See yah."
    $ ravenSprite = 0
    show fbraven current:
        xalign 1.5 xzoom -1.0 ypos 120
    with move

    pause

    show fbemily current:
        xalign 0.2 ypos 120
    show fbmia current:
        xalign 0.3 ypos 120
    show fbsophia current:
        xalign 0.4 ypos 120
    show fbolivia current:
        xalign 0.5 ypos 120
    show fbcharlotte current:
        xalign 0.6 ypos 120
    show fbava current:
        xalign 0.7 ypos 120
    show fbplayer current:
        xalign 0.1 ypos 120
    with Dissolve(0.7)

    $ playerSprite = 5
    player "What the HELL was that?"
    $ playerSprite = 4
    $ avaSprite = 16
    ava "Ugh. That was Stephanie and her cronies Melissa and Raven."
    $ avaSprite = 15
    $ charlotteSprite = 11
    charlotte "Call Raven Patricia, she HATES that hehe."
    $ charlotteSprite = 0
    $ playerSprite = 5
    player "What was their deal? Especially Stephanie."
    $ playerSprite = 4
    $ emilySprite = 5
    emily "*Sigh* Stephanie has been..."
    $ emilySprite = 4
    $ sophiaSprite = 4
    show fbsophia current:
        xalign 0.4 xzoom 1.0 ypos 120
    sophia "A rival!"
    $ sophiaSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.6 xzoom 1.0 ypos 120
    charlotte "An annoyance!"
    $ charlotteSprite = 0
    $ avaSprite = 11
    show fbava current:
        xalign 0.7 xzoom 1.0 ypos 120
    ava "An obstacle!"
    $ avaSprite = 0
    show fbolivia current:
        xalign 0.5 xzoom 1.0 ypos 120
    olivia "A bitch."
    $ emilySprite = 2
    $ oliviaSprite = 0
    $ miaSprite = 0
    show fbmia current:
        xalign 0.3 xzoom 1.0 ypos 120
    show fbemily current:
        xalign 0.2 xzoom 1.0 ypos 120
    emily "*Ahem*"
    $ emilySprite = 1
    emily "Difficult. For a long time now."
    $ emilySprite = 0
    $ avaSprite = 1
    ava "Every single event or like thing to happen in the past decade she's been there trying to beat Emily."
    $ avaSprite = 0
    $ emilySprite = 5
    emily "I don't even know what I did? But she's always so just nasty and underhanded."
    $ emilySprite = 4
    $ charlotteSprite = 1
    charlotte "She's just a mean and terrible person for like no reason!"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Sounds like someone I know."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "Eh..."
    $ charlotteSprite = 0
    $ sophiaSprite = 4
    sophia "The point is she's the worst and goes out of her way to beat us at something or ruin what we've worked on."
    $ sophiaSprite = 3
    $ miaSprite = 1
    mia "Huh. I always thought they were okay."
    $ miaSprite = 0
    "Everyone" "!!!!"
    $ avaSprite = 16
    ava "Mia, babe. How on EARTH could you possibly think they were cool after all the things they say about us?"
    $ avaSprite = 15
    $ miaSprite = 3
    show fbmia current:
        xzoom -1.0
    mia "I thought they were being ironic!"
    mia "You're saying they really meant all the stuff they've said all these years?"
    $ miaSprite = 2
    $ sophiaSprite = 4
    sophia "Yes Mia."
    $ sophiaSprite = 3
    $ miaSprite = 3
    mia "Ohhh.."
    mia "Yeah they're really mean."
    $ miaSprite = 2
    $ avaSprite = 1
    ava "Took a while but you got there hun haha."
    $ avaSprite = 0
    $ emilySprite = 1
    show fbmia current:
        xzoom 1.0
    emily "Well alright. Let's forget about them for now and move on, it's not good to let them effect us too much."
    $ emilySprite = 0
    $ oliviaSprite = 9
    olivia "I agree."
    $ oliviaSprite = 8
    $ charlotteSprite = 1
    charlotte "Well said. We'll just kick their butts in the talent show."
    $ charlotteSprite = 0
    $ playerSprite = 17
    player "Sorry what? Talent show?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yeah the school is having a big annual talent show in two weeks."
    $ emilySprite = 0
    $ sophiaSprite = 4
    sophia "Stephanie and her goons always do some underhanded method to mess with us every year."
    $ sophiaSprite = 3
    $ emilySprite = 1
    emily "BUT! We still make it through and win in the end. Together!"
    $ emilySprite = 0
    $ avaSprite = 1
    ava "Nobody can keep these girls from kicking ass!"
    $ avaSprite = 0
    $ miaSprite = 1
    mia "Yeah!!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Welp. Least you guys seem to have everything under control."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "This year we're gonna play a song."
    $ miaSprite = 0
    $ playerSprite = 1
    player "A song?"
    $ playerSprite = 0
    $ oliviaSprite = 9
    olivia "We're forming a band."
    $ oliviaSprite = 8
    $ playerSprite = 1
    player "That is awesome. Can't wait to see it."
    $ playerSprite = 0
    $ emilySprite = 3
    emily "It's still a bit away though."
    $ emilySprite = 0
    $ sophiaSprite = 1
    sophia "Yeah I'm still looking forward to the beach!"
    $ sophiaSprite = 0
    $ avaSprite = 1
    ava "True!"
    ava "Let's not let those bitches occupy our minds until AFTER we have our big relaxing day."
    $ avaSprite = 0
    $ playerSprite = 1
    player "That sounds like a good idea."
    $ playerSprite = 0
    $ emilySprite = 3
    emily "I agree!"
    $ emilySprite = 1
    emily "But for now, I think I should go guys I got a lot to prepare for."
    $ emilySprite = 0
    $ charlotteSprite = 11
    charlotte "Yeah no problem! I should go too."
    $ charlotteSprite = 0
    $ avaSprite = 1
    ava "Alright this is a good time to seperate for now then huh?"
    $ avaSprite = 0
    $ miaSprite = 1
    mia "Okay!"
    $ miaSprite = 0
    $ sophiaSprite = 1
    sophia "Bye girls bye [povname]!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Bye Soph, bye everyone haha."
    "Everyone" "Bye!"
    hide fbolivia current
    with Dissolve(0.5)
    hide fbsophia current
    with Dissolve(0.5)
    hide fbcharlotte current
    with Dissolve(0.5)
    hide fbava current
    with Dissolve(0.5)
    $ miaSprite = 1
    mia "Goodbye my super hot boyfriend!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Goodbye my absolutely beautiful girlfriend!"
    $ playerSprite = 0
    hide fbmia current
    hide fbplayer current
    $ emilySprite = 4
    show fbmia mcmiamakeout:
        xalign 0.0 ypos 120
    with Dissolve(0.5)
    mia "Mmmmmmwuah!"
    show fbmia current:
        xalign 0.1 ypos 120
    show fbplayer current behind fbmia:
        xalign 0.0 ypos 120
    with Dissolve(0.5)
    show fbemily current:
        xalign 0.2 ypos 120
    with move
    $ playerSprite = 1
    player "Hehe bye babe."
    $ playerSprite = 0
    $ miaSprite = 5
    mia "Hehe!"
    hide fbmia current
    with Dissolve(0.5)
    emily "...."
    $ playerSprite = 1
    player "I guess I'll see you later huh?"
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Yeah come..."
    emily "Come find me when you're free."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Will do. See you later Em."
    $ playerSprite = 0
    $ emilySPrite = 1
    hide fbplayer current
    with Dissolve(0.7)
    $ emilySprite = 5
    emily "See you later..."


    $ emilyphase1interaction2 = 7
    $ emilyphase2interaction1 = 1
    $ emilyquestlog = "Well that was dramatic. I should talk to Emily about those three bullies."
    $ melissaquesticon = "gui/questboxMelissa.png"
    $ stephaniequesticon = "gui/questboxStephanie.png"
    $ ravenquesticon = "gui/questboxRaven.png"
    $ melissaquestlog = "She seems to sure love bubblegum."
    $ stephaniequestlog = "Seems like she's the leader of the group. Such a Mean Girl."
    $ ravenquestlog = "One of Stephanie's Cronies. Goth."
    jump passtime

# part 2

label emilyphase2interaction1part2:
    hide screen emily_atschool
    scene fs schoolhallway2
    with Dissolve(0.5)

    $ playerSprite = 1
    show fbemily upsetflip:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.45 ypos 120
    with Dissolve(0.7)

    player "Hey."
    $ playerSprite = 0
    show fbemily upsetflip:
        xalign 0.8 ypos 120
    with move
    emily "Shit shit shit."
    $ emilySprite = 0
    $ playerSprite = 11
    player "{i}Woah it's not like her to swear.{/i}"
    $ playerSprite = 1
    player "Emily!"
    $ playerSprite = 0
    $ emilySprite = 1
    show fbemily current:
        xalign 0.75 ypos 120
    emily "Huh? Oh hi [povname] sorry. I was just headed to the library."
    $ emilySprite = 0
    $ playerSprite = 1
    show fbemily current:
        xalign 0.6 ypos 120
    with move
    $ playerSprite = 1
    player "Yeah you look like you were moving pretty fast."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yeah I'm kinda in a bind. There's some paperwork the School's board of directors need really soon."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Oh? And you're gonna...get it to them?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Not exactly, I have to do it all over again."
    emily "You SEE. A certain Vice-President's ONLY responsibility was to get this done and handed in yesterday."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Vice-President....OH you mean Stephanie?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yes."
    $ emilySprite = 0
    $ playerSprite = 1
    player "And so..."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "And so she didn't!"
    emily "Now I gotta run around getting purchase statements and rental receipts and all this other BULLSHIT-"
    $ emilySprite = 4
    $ playerSprite = 1
    player "Woah woah woah there, calm down Em."
    player "If it was her responsibility wouldn't the consequences fall on her?"
    $ playerSprite = 0
    $ emilySprite = 5
    emily "That'd be nice wouldn't it? But no her parents are influencial and she'd get a 'Slap on a the wrist' at worst."
    emily "But I don't even CARE about that, this paperwork is related to the talent show!"
    $ emilySprite = 4
    $ playerSprite = 1
    player "Ohhh."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "If it's not delivered soon there won't be one!"
    $ emilySprite = 4
    $ playerSprite = 5
    player "So that bitch didn't even do anything."
    $ playerSprite = 4
    $ emilySprite = 5
    emily "Ugh no. She did it."
    emily "She's smart...no she's conniving! She actually DID do all the work, she was sending me pics showing me she did them."
    $ emilySprite = 4
    $ playerSprite = 15
    player "Well then why..."
    $ playerSprite = 14
    $ emilySprite = 5
    emily "She doesn't WANT the talent show to happen! She thinks we're gonna beat her this year too and she doesn't want that."
    emily "But she made sure to actually DO the work so when the blame comes to her she can say she did it, and make up some story about how she sent it to me."
    emily "And I somehow lost it."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Wow that's quite the intricate scheme. And you're definitely not reaching?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Trust me I KNOW her, if she hasn't thought of that idea it's something worst."
    emily "There's no way she's gonna give it to me if I ask her for it. So might as well just redo everything."
    $ emilySprite = 0
    player "{i}Huh she seems pretty confident that Stephanie has this big plan but she didn't seem...motivated enough to me in order to hatch something like that.{/i}"
    $ playerSprite = 1
    player "Well if there's nothing I can do..."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "No not this time sorry."
    emily "Unless Stephanie hands you the papers herself I just have to go."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Hands me them herself huh?"
    $ playerSprite = 0
    $ emilySprite = 1
    show fbemily current:
        xalign 0.8 ypos 120
    with move
    emily "Yup I gotta get back to it sorry, I'll see you later!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Where does Stephanie live exactly?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Uhh the same building as Olivia, the one next to the café!"
    $ emilySprite = 0
    $ playerSprite = 7
    player "Hmmm..."
    $ emilySprite = 1
    show fbemily current:
        xalign 1.5 ypos 120
    with move
    hide fbemily current
    emily "Okay bye!"
    $ emilySprite = 0
    player "....."
    player "HMMMMM."
    $ playerSprite = 0

    $ emilyphase2interaction1 = 2
    $ emilyquestlog = "I gotta get my hands on those files! Emily will jump my dick garanteed!"
    jump overworldmap

# part 3

label emilyphase2interaction1part3:
    stop music fadeout 5
    stop sound fadeout 5
    player "Okay let's see let's see..."
    player "Ah there we go, Stephanie DeBardieu. Ouu fancy name."
    "BZZZZZ"
    melissa "Uhhh like hello?"
    player "Uh hi?"
    melissa "Who the hell is this?"
    player "It's uh, [povname]. Wait that voice...is this Melissa?"
    melissa "Oh my Gooood! You're that hunk that's dating Emily!"
    player "Well actu-"
    melissa "You remembered my name?"
    player "Um yeah, of course."
    melissa "*Sigh*, sometimes being super hot has it's perks I gotta admit."
    player "Right listen, is Stephanie there?"
    melissa "What you don't wanna phone sex me?"
    player "Phone se-"
    stephanie "OHMYGOD Melissa I swear to god if you're seducing the Pizza guy again!"
    melissa "Whaaaat? No! I-"
    stephanie "Give me that!"
    melissa "But I wanna Phone Sex!!"
    raven "It's not a phone you idiot."
    stephanie "UGH!"
    player "....."
    stephanie "Hi hello? Who is this? My friend just pranked called you we don't want anymore pizza!"
    player "No this is uh [povname], we met at the school? I'm Mia's boyfriend?"
    stephanie "OH! Mr. White Knight himself."
    player "Yeah I was wondering if you still had those pap-"
    stephanie "This is no way to talk, come on up."
    "BZZZZZ"
    player "Alright looks like I'm going in."
    player "Hope this wasn't a mistake."

    scene fs stephaniehouse
    with Dissolve(0.7)

    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Woah, the penthouse is really...nice?"
    $ playerSprite = 0

    $ stephanieSprite = 3
    show fbstephanie current:
        xalign 0.45 ypos 120
    with Dissolve(0.5)
    stephanie "I know right? There's no way I'm gonna live with my parents so I got them to hook me up with this place!"
    $ stephanieSprite = 1
    stephanie "It's not as big as I want but it'll do. Not like there's anyplace nicer in this town anyways."
    $ stephanieSprite = 2

    show fbmelissa current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ melissaSprite = 1
    melissa "Well I think it's super fancy! And I can eat all the snacks I want."
    $ melissaSprite = 0

    show fbraven current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    $ ravenSprite = 1
    raven "It's not dark enough."
    raven "Could use some more black."
    $ ravenSprite = 0
    show fbmelissa talkflip:
        xalign 0.55 ypos 120
    melissa "Wow what a surprise, YOU want to make it darker."
    melissa "Do you EVER not suck the life out of everything?"
    show fbmelissa defaultflip:
        xalign 0.55 ypos 120
    $ ravenSprite = 1
    raven "UHH Do you ever stop sucking dick?! You fucking slut!"
    $ ravenSprite = 0
    $ melissaSprite = 2
    show fbmelissa talkflip:
        xalign 0.55 ypos 120
    melissa "WELL TELL YOUR DAD TO STOP HITTING ME UP THEN YOU EMO GOTH PUNK LOSER!"
    show fbmelissa defaultflip:
        xalign 0.55 ypos 120
    $ ravenSprite = 1
    raven "ONLY ONE OF THOSE IS RIGHT YOU STUPID FAT TITTED F-"
    $ ravenSprite = 0
    $ stephanieSprite = 1
    $ melissaSprite = 0
    show fbmelissa current at surpriseshake:
        xalign 0.6 ypos 120
    show fbstephanie angryflip:
        xalign 0.4 ypos 120
    stephanie "Can you two idiots stop embarrassing me for one FUCKING second!!??"
    stephanie "At least have your little love affairs when I don't know...I don't have a guest???!!"
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "Oh I'm a guest?"
    $ playerSprite = 0
    $ ravenSprite = 2
    raven "Shit s-sorry Stephanie."
    $ ravenSprite = 0
    $ melissaSprite = 1
    melissa "Yeah my B. I get irritable when I'm hungry."
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Do you ever stop putting things in your mouth?"
    $ ravenSprite = 0
    $ stephanieSprite = 1
    stephanie "What did I just say!??"
    stephanie "Ugh."
    $ StephanieSprite = 3
    show fbstephanie current:
        xalign 0.45 ypos 120
    stephanie "Okay finally. And yes, you're a guest Mr. White Knight."
    $ stephanieSprite = 2
    $ playerSprite = 1
    player "[povname]."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "[povname]."
    stephanie "And why wouldn't you be? I let you in didn't I?"
    $ stephanieSprite = 2
    $ playerSprite = 1
    player "I dunno. Just assummed you'd be hostile since I'm dating someone from Emily's group?"
    $ playerSprite = 0
    $ stephanieSprite = 3
    stephanie "Well for one, we still don't know why you're here and I'm curious."
    $ stephanieSprite = 2
    $ melissaSprite = 1
    melissa "Hehe I bet he couldn't resist our feminine charms!"
    $ melissaSprite = 0
    $ stephanieSprite = 1
    stephanie "And secondly...mmm well maybe I'll keep that one a secret."
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "You wanna seduce me and use me somehow to get back at Emily."
    $ playerSprite = 0
    stephanie "...."
    $ stephanieSprite = 2
    stephanie "...."
    $ melissaSprite = 1
    melissa "Hehe bingo!"
    melissa "Between the three of us there's no way you can't be like...persuaded!"
    melissa "Hell even Raven has something for the boys who are into her kinda thing."
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Wow. Gee. Thanks."
    $ ravenSprite = 0
    $ melissaSprite = 1
    melissa "You are welcome."
    $ melissaSprite = 0
    $ stephanieSprite = 1
    stephanie "Well I'd be lying if I said the thought hasn't crossed my mind. And stayed there."
    stephanie "But we still don't know why you're here."
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "Oh yeah. Almost forgot."
    player "So you're the vice president right?"
    $ playerSprite = 0
    $ stephanieSprite = 3
    stephanie "Uh huh."
    $ stephanieSprite = 2
    $ melissaSprite = 1
    melissa "OOhhh political scandal??"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Quiet! I wanna see where he's going with this."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Emily said you have some papers for the school board? Something to do with the talent show in a few weeks?"
    $ playerSprite = 0
    $ stephanieSprite = 4
    stephanie "Oh yeah! What about them?"
    $ playerSprite = 1
    player "Well they were due yesterday and I'm here to see wh-"
    $ playerSprite = 0
    $ stephanieSprite = 4
    show fbstephanie current at surpriseshake:
        xalign 0.45 ypos 120
    stephanie "OH SHIT! OH MY GOD!"
    stephanie "I totally forgot, shit shit shit hang on!"
    $ stephanieSprite = 2
    show fbstephanie current:
        xalign 1.5 ypos 120
    with move

    $ melissaSprite = 1
    melissa "Oh booo, you just wanted some papers?"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Dissapointing."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "I dunno why you guys were expecting something raunchy."
    $ playerSprite = 0
    $ melissaSprite = 1
    melissa "Raunchy is fun!"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Sex makes the pain of life a bit more tolerable."
    $ ravenSprite = 0
    $ playerSprite = 11
    player "...."
    melissa "...."
    $ playerSprite = 1
    player "Well at least your appearance matches your personality."
    $ playerSprite = 0
    show fbstephanie foldertalk:
        xalign 0.45 ypos 120
    with move

    stephanie "Okay here got em, because of the trip it totally slipped my mind."
    stephanie "I haven't even unpacked the suitcase I was keeping it in."
    stephanie "So you're gonna take it to Emily for me then?"
    show fbstephanie folder:
        xalign 0.45 ypos 120
    $ stephanieSprite = 0
    $ playerSprite = 17
    player "Wait...so you're just gonna give it to me?"
    show fbstephanie foldertalk:
        xalign 0.45 ypos 120
    stephanie "Yeah?"
    show fbstephanie folder:
        xalign 0.45 ypos 120
    $ playerSprite = 1
    player "No...schemes or anything to stop the talent show?"
    $ playerSprite = 0
    show fbstephanie foldertalk:
        xalign 0.45 ypos 120
    stephanie "Stop the talent show? What are you talking about we want the talent show to happen!"
    show fbstephanie folder:
        xalign 0.45 ypos 120
    $ melissaSprite = 1
    melissa "Yeah we're gonna make a band like those losers and blow them out of the water!"
    $ melissaSprite = 0
    show fbstephanie foldertalk:
        xalign 0.45 ypos 120
    stephanie "It's gonna be so sweet to see the look on Emily's face when we win fair and square haha."
    show fbstephanie folder:
        xalign 0.45 ypos 120
    $ melissaSprite = 1
    melissa "She'll be all like 'B-But I thought you guys had to cheat!' 'T-T-There's no way you can beat us!'."
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Hahaha!"
    $ ravenSprite = 0
    show fbstephanie foldertalk:
        xalign 0.45 ypos 120
    stephanie "I got my parents to pay some crazy good teachers to help us learn some instruments."
    show fbstephanie foldertalk:
        xalign 0.45 ypos 120
    $ playerSprite = 1
    player "For real?"
    $ playerSprite = 0
    $ melissaSprite = 1
    melissa "You bet! Raven here already plays the guitar and she's wicked good haha we're halfway there!"
    $ melissaSprite = 0
    show fbstephanie foldertalk:
        xalign 0.45 ypos 120
    stephanie "Yeah she's actually talented."
    show fbstephanie folder:
        xalign 0.45 ypos 120
    $ ravenSprite = 2
    raven "G-Guys c'mon..."
    $ ravenSprite = 0
    show fbmelissa talkflip:
        xalign 0.55 ypos 120
    melissa "Aww no need to blush! It doesn't match your colors haha."
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "And we're back."
    show fbmelissa current:
        xalign 0.6 ypos 120
    $ ravenSprite = 0
    $ playerSprite = 1
    player "Well I haven't heard you play yet Raven but that's super cool either way."
    $ playerSprite = 0
    $ ravenSprite = 1
    raven "Um, thanks [povname]."
    $ ravenSprite = 0
    $ playerSprite = 1
    player "No problem. So I can have those papers now?"
    $ playerSprite = 0
    show fbstephanie foldertalk:
        xalign 0.42 ypos 120
    with move
    stephanie "Yeah sure just t-"
    stephanie "Wait."
    stephanie "Why isn't Emily here picking it up?"
    show fbstephanie folder:
        xalign 0.42 ypos 120
    $ playerSprite = 16
    player "Uhhh she's busy?"
    $ playerSprite = 8
    show fbstephanie foldertalk:
        xalign 0.42 ypos 120
    stephanie "I KNOW she's not busy because that little bitch always finishes whatever she's assigned as soon as she can."
    stephanie "And there's nothing left to do. This paperwork was the last thing."
    show fbstephanie folder:
        xalign 0.42 ypos 120
    $ melissaSprite = 1
    melissa "Ohhh interesting!"
    $ melissaSprite = 0
    $ playerSprite = 16
    player "Uhhh so...she didn't think you'd give it to her? So she's doing it all over herself."
    $ playerSprite = 8
    $ stephanieSprite = 3
    show fbstephanie current:
        xalign 0.45 ypos 120
    with move
    stephanie "If she didn't think I was gonna hand it over, then WHY are you here?"
    $ stephanieSprite = 0
    $ playerSprite = 16
    player "Uhh-"
    $ playerSprite = 8
    $ ravenSprite = 1
    raven "He was gonna BARGAIN for it!!"
    $ ravenSprite = 0
    $ melissaSprite = 1
    melissa "*GASP!*"
    melissa "Like Dormammu??"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "That's a pretty outdated reference now Mel."
    $ ravenSprite = 0
    $ ravenSprite = 0
    show fbmelissa talkflip:
        xalign 0.55 ypos 120
    melissa "Reference?"
    show fbmelissa current:
        xalign 0.6 ypos 120
    $ stephanieSprite = 3
    stephanie "And to think I almost just handed them right over to you."
    $ stephanieSprite = 2
    $ ravenSprite = 1
    raven "What were you willing to do huh?"
    $ ravenSprite = 0
    $ playerSprite = 16
    player "Okay girls now c'mon. You JUST said you also wanted this event to happen."
    $ playerSprite = 11
    $ ravenSprite = 1
    raven "Well if Emily's already re-doing it why should it matter?"
    $ ravenSprite = 0
    $ stephanieSprite = 1
    stephanie "Haha nice Raven, yeah not only will we not have to do anything, but Emily being super late on the delivery will make her look bad!"
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "Win-Win baby!"
    $ melissaSprite = 0
    $ playerSprite = 4
    player "{i}God dammit I was so close!{/i}"
    $ playerSprite = 16
    player "Okay fine. If you give me the papers I'll do you a favor."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Hmmm that's not good enough."
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "I say we tie him up and suck his balls!!"
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "Jesus christ Melissa!"
    $ ravenSprite = 0
    show fbmelissa talkflip:
        xalign 0.55 ypos 120
    melissa "What?!"
    show fbmelissa defaultflip:
        xalign 0.55 ypos 120
    raven "...."
    $ ravenSprite = 1
    raven "There's three of us, one of us should be riding him too!"
    $ ravenSprite = 0
    show fbmelissa talkflip:
        xalign 0.55 ypos 120
    melissa "Hahaha yeah!"
    $ melissaSprite = 1
    show fbmelissa current at surpriseshake:
        xalign 0.6 ypos 120
    melissa "YEAH!"
    $ melissaSprite = 0
    player "{i}These girls are actually fucking hilarious.{/i}"
    $ playerSprite = 7
    player "{i}But I can't let them know I might be willing to...humor their ideas.{/i}"
    $ playerSprite = 5
    player "Calm the fuck down you lecherous succubi!"
    $ playerSprite = 0
    $ stephanieSprite = 1
    show fbstephanie current:
        xzoom -1.0
    stephanie "Haha he's right girls you are being a bit much."
    $ stephanieSprite = 0
    $ melissaSprite = 1
    melissa "Hehe."
    $ melissaSprite = 0
    $ ravenSprite = 1
    raven "We're just messing around haha no worries."
    $ ravenSprite = 0
    $ melissaSprite = 1
    melissa "One of us might've been serious."
    $ melissaSprite = 0
    $ playerSprite = 1
    show fbstephanie current:
        xzoom 1.0
    player "Okay okay, I'll do you guys one favor, each."
    $ playerSprite = 0
    $ stephanieSprite = 1
    stephanie "Each huh?"
    $ stephanieSprite = 0
    $ playerSprite = 1
    player "You want me to find something? Do something? Help you with something? I'll do it."
    $ playerSprite = 0
    $ melissaSprite = 1
    melissa "{size=-10}Hehe 'Do' something.{/size}"
    $ melissaSprite = 0
    stephanie "....."
    $ stephanieSprite = 1
    stephanie "Alright that's fine with me, that good with you girls?"
    $ stephanieSprite = 0
    $ ravenSprite = 1
    raven "Yes."
    $ ravenSprite = 0
    $ melissaSprite = 1
    melissa "Yup!"
    $ melissaSprite = 0
    show fbstephanie foldertalk:
        xalign 0.4 ypos 120
    stephanie "Here's your precious paperwork Mr. [povname]. Expect us to contact you soon."
    $ stephanieSprite = 2
    show fbstephanie current:
        xalign 0.4 ypos 120
    player "Thanks...."
    $ playerSprite = 14
    player "{i}Shit.{/i}"
    $ stephanieSprite = 1
    stephanie "Bye bye!"
    $ stephanieSprite = 0

    scene fs blackblank
    with Dissolve(0.5)
    $ playerSprite = 1
    player "I should get these papers back to Emily."
    $ playerSprite = 0

    $ emilyphase2interaction1 = 3
    $ emilyquestlog = "Man what am I getting myself into? Emily should be in the library..."
    $ melissaquestlog = "I wonder what kind of favor I'm going to have to do for her."
    $ ravenquestlog = "I wonder what kind of favor I'm going to have to do for her."
    $ stephaniequestlog = "I wonder what kind of favor I'm going to have to do for her."
    jump passtime

# part 4

label emilyphase2interaction1part4:
    if whereami == "library":
        hide screen phone
        hide screen phonecontacts
        hide screen emily_atlibrary
        hide screen charlotte_library
        hide screen uppergui
        with Dissolve(0.5)

        show fbplayer current:
            xalign 0.4 ypos 120
        show fbemily current:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        $ playerSprite = 1
        player "Hey! I got em."
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Ahhhh! I can't believe you actually got it!"
        $ playerSprite = 1
        $ emilySprite = 0
        player "A feat easily completed for one such as me haha!"
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Oh geez you keep on saving my day huh?"
        $ playerSprite = 1
        $ emilySprite = 0
        player "It's no problem, really."
        $ playerSprite = 0
        player "{i}I'm just racking up those sympathy points!{/i}"
        $ emilySprite = 1
        emily "Alright listen, gimme the papers and I'll go run them to the board right away. Call me tonight alright?"
        $ playerSprite = 1
        $ emilySprite = 0
        player "Oh uh.. yeah sure."
        $ playerSprite = 0
        $ emilySprite = 1
        emily "Okay bye!!"
        $ playerSprite = 1
        $ emilySprite = 0
        scene fs blackblank
        with Dissolve(0.7)
        player "Sweet. I should call her from my room tonight like she said."
        $ emilyphase2interaction1 = 4
        $ emilyquestlog = "I'm looking forward to this, Emily wants me to call her over tonight."
        jump passtime
    elif whereami == "schoolhallway":
        hide screen emily_atschool

        show fbplayer current:
            xalign 0.4 ypos 120
        show fbemily current:
            xalign 0.6 ypos 120
        with Dissolve(0.7)

        player "Hey! I got em."
        emily "Ahhhh! I can't believe you actually got it!"
        player "A feat easily completed for one such as me haha!"
        emily "Oh geez you keep on saving my day huh?"
        player "It's no problem, really."
        player "{i}I'm just racking up those sympathy points!{/i}"
        emily "Alright listen, gimme the papers and I'll go run them to the board right away. Call me tonight alright?"
        player "Oh uh.. yeah sure."
        emily "Okay bye!!"
        scene fs blackblank
        with Dissolve(0.7)
        player "Sweet. I should call her from my room tonight like she said."
        $ emilyphase2interaction1 = 4
        $ emilyquestlog = "I'm looking forward to this, Emily wants me to call her over tonight."
        jump passtime
    else:
        hide screen contacts
        hide screen phonecontacts
        emily "Hello?"
        player "Hey I got the papers!"
        emily "No way! Please get them to me as soon as possible!!"

# part 5

label emilyphase2interaction1part5:
    hide screen backbuttonROOM
    hide screen backbuttonLIVINGROOM
    hide screen uppergui
    scene fs livingroomnight
    with Dissolve(0.7)

    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.5)
    player "Alright I should probably call Emily now."
    player "Let's see..."
    play sound "audio/knock-on-door.wav"
    "*knock knock knock*"
    $ playerSprite = 17
    player "Huh?"
    player "I wonder who's at the door."

    show fbemily current:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ emilySprite = 1
    emily "Hi [povname]!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Oh hey Em. I was literally about to call you!"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Oh haha."
    emily "I um...yeah I wanted to.."
    emily "I couldn't wait I just kinda started heading over sorry."
    $ emilySprite = 0
    $ playerSprite = 1
    player "No no don't apologize."
    player "I'm glad you're here."
    $ playerSprite = 0
    $ emilySprite = 7
    emily "*blush*"
    $ playerSprite = 1
    player "Wanna go to my room?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "O-Okay!"
    $ emilySprite = 0
    scene fs blackblank
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Let me get the lights."
    $ playerSprite = 0
    scene fs emilyclosetmiasex1b
    with Dissolve(1.0)
    player "...."
    scene fs emilyclosetmiasex2player
    player "So."
    scene fs emilyclosetmiasex3
    emily "Hehe so..."
    scene fs emilyclosetmiasex2player
    player "You get those papers delivered alright?"
    scene fs emilyclosetmiasex2emily
    emily "Yup! It's all taken care of."
    emily "So....how did you end up getting them in the first place?"
    scene fs emilyclosetmiasex2player
    player "Oh, you would be really proud of me."
    scene fs emilyclosetmiasex2emily
    emily "Oh yeah?"
    scene fs emilyclosetmiasex2player
    player "I found Stephanie's apartment and buzzed her."
    scene fs emilyclosetmiasex2emily
    emily "Really?"
    scene fs emilyclosetmiasex2player
    player "Yup, and I told her that she better let me in."
    player "Did you know she lives in the penthouse?"
    scene fs emilyclosetmiasex2emily
    emily "Yeah I knew, she never let's an opportunity go to tell me."
    scene fs emilyclosetmiasex2player
    player "Those other two..."
    scene fs emilyclosetmiasex1
    player "{i}Let's spice things up to get her going hehe.{/i}"
    scene fs emilyclosetmiasex2player
    player "BITCHES. Were there too."
    scene fs emilyclosetmiasex2emily
    emily "Ugh, Melissa and Raven. They're the worst!"
    scene fs emilyclosetmiasex2player
    player "They came onto me, tried to get me to cheat on Mia could you believe it?"
    scene fs emilyclosetmiasex4emily
    with Dissolve(0.5)
    emily "So typical! Those SLUTS!"
    scene fs emilyclosetmiasex4player
    player "So I told them they could fuck right off."
    scene fs emilyclosetmiasex4emily
    emily "Wow really?"
    scene fs emilyclosetmiasex4player
    player "And I told Stephanie."
    scene fs emilyclosetmiasex4emily
    emily "That bitch."
    scene fs emilyclosetmiasex4player
    player "I told her to give me the papers right now or there'll be consequences."
    scene fs emilyclosetmiasex6emily
    with Dissolve(0.5)
    emily "Mmmm yeah, and then what happened?"
    scene fs emilyclosetmiasex6player
    player "She froze up, couldn't say anything."
    player "Went into her room, and came out with the papers."
    scene fs emilyclosetmiasex6emily
    emily "Holy...geez...[povname]."
    scene fs emilyclosetmiasex9emily
    emily "That's...really hot."
    scene fs emilyclosetmiasex9player
    player "Yeah? That make you happy?"
    scene fs emilyclosetmiasex9emily
    emily "You know when you went up to them when we all met in the hallway?"
    emily "And you started talking smack to Stephanie?"
    scene fs emilyclosetmiasex9player
    player "Uh huh."
    scene fs emilyclosetmiasex9emily
    emily "I got really wet. Thought about it the whole day."
    scene fs emilyclosetmiasex9player
    player "That really turns me on Emily..."
    scene fs emilyclosetmiasex11
    emily "[povname], I really wanted to take things slow."
    emily "Make sure we're both emotionally ready since our situation is....unique."
    emily "But I just don't think...."
    scene fs emilyclosetmiasex8
    with Dissolve(1.0)
    emily "I can hold myself back anymore."
    scene fs emilyclosetmiasex12
    with Dissolve(0.7)
    emily "Mmmmm!"
    player "{i}Fuck yes finally.{/i}"
    scene fs emilyclosetmiasex13
    player "{i}Forgot how nice these tits are.{/i}"
    emily "{i}This is really happening! I'm really doing this!{/i}"
    scene fs emilyclosetmiasex12
    emily "{i}I didn't even mean to start feeling his...dick. It just happened!{/i}"
    scene fs emilyclosetmiasex14
    player "Hah..."
    emily "Hah...hah...hah..."
    emily "....."
    scene fs emilyclosetmiasex15
    with Dissolve(0.5)
    emily "MMMMM!"
    player "{i}No way she just took out my dick haha!{/i}"
    emily "{i}Oh my god I just took it out!{/i}"
    emily "{i}Am I...am I really going to have sex with [povname] tonight?!{/i}"
    emily "{i}It's so...THICK and BIG...{/i}"
    emily "{i}I don't know if I-{/i}"
    play sound "audio/knock-on-door.wav"
    "Knock Knock Knock!"
    scene fs emilyclosetmiasex16
    emily "Huh??"
    player "W-What? What the fuck?"
    mia "Hello? [povname] are you in your room?"
    player "What? Mia?!"
    mia "I'm coming in!"
    scene fs emilyclosetmiasex17
    player "Shit! Quick Emily get in the fucking closet!!"
    emily "Huh? wha-o-okay!"
    scene fs emilyclosetmiasex23
    with Dissolve(0.7)
    mia "Heeey! I let myself in sorry."
    scene fs emilyclosetmiasex19
    with Dissolve(0.5)
    emily "Why the heck is Mia here??"
    emily "Oh I hope she doesn't notice me, even she would figure out what we're up to!"
    scene fs emilyclosetmiasex23player
    player "Mia why didn't you let me know you were coming??"
    player "You can't just pop in like that!"
    scene fs emilyclosetmiasex23mia
    mia "Huh? Why not?"
    scene fs emilyclosetmiasex23player
    player "Uh..."
    player "I guess....never mind you...can?"
    scene fs emilyclosetmiasex23mia
    mia "Haha yay okay!"
    scene fs emilyclosetmiasex24mia
    mia "Wait a second."
    mia "Why is your dong out?"
    mia "And why are you so hard?"
    scene fs emilyclosetmiasex24player
    player "Uhh..."
    player "Because....you're here?"
    scene fs emilyclosetmiasex24
    mia "...."
    scene fs emilyclosetmiasex24mia
    mia "Well thanks!"
    mia "Do you...want me to take care of it?"
    scene fs emilyclosetmiasex24player
    player "Would you?"

    scene fs emilyclosetmiasex19
    with Dissolve(0.7)
    mia "Sure!"
    mia "Honestly I was feeling a little friskly lately."
    emily "{i}Wait...what is Mia?{/i}"
    mia "I can never get used to how big you are, no matter how many times I suck it!"
    scene fs emilyclosetmiasex18
    with Dissolve(0.5)
    emily "{i}No!{/i}"
    emily "{i}I d-don't want to watch this!{/i}"

    scene fs emilyclosetmiasex26
    with Dissolve(0.7)
    player "Yeah...yeah just like that."
    mia "Mmmmm..."
    scene fs emilyclosetmiasex27
    player "Ahhh fuck yeah!"
    mia "Unghh!"
    player "{i}Holy shit this is so hot, knowing Emily is right there watching Mia suck my cock...{/i}"
    emily "{i}Wow she doesn't even need any help to-{/i}"
    scene fs emilyclosetmiasex28
    mia "UHGUCK!"
    player "HOLY FUCK YES MIA!"
    player "The whole way down your throat baby that's it!"
    emily "{i}OH MY GOD! How can she just take his whole cock down her throat without him holding her down!{/i}"
    player "AHHH you better be paying attention!"
    player "This is how you suck a fucking cock!"
    mia "?"
    emily "{i}Is he talking to me?{/i}"
    scene fs emilyclosetmiasex27
    pause
    scene fs emilyclosetmiasex26
    pause
    mia "You want to cum on my face?"
    player "No. I have a better idea."
    player "Take off your clothes."
    mia "Oh! Okay."
    scene fs emilyclosetmiasex19
    with Dissolve(0.5)
    emily "{i}Wait what? Why doesn't he just finish this so she can leave!?{/i}"
    scene fs emilyclosetmiasex29
    with Dissolve(0.5)
    emily "{i}No!{/i}"
    scene fs emilyclosetmiasex30
    emily "{i}NO!{/i}"
    scene fs emilyclosetmiasex31
    player "Get over here!"
    mia "Oh my! Haha!"

    scene fs emilyclosetmiasex20
    mia "Hehe looks like I'm not the only one who's feeling frisky!"
    player "Yeah for some reason I'm just...really in the mood tonight hehe."
    emily "...."
    mia "Oh!"
    scene fs emilyclosetmiasex21
    with Dissolve(0.5)
    mia "Oh! [povname]!!"
    scene fs emilyclosetmiasex22
    with Dissolve(0.5)
    emily "...."
    player "Fuck Mia you're so wet already."
    mia "Don't keep me waiting!"
    show emilymiasex movie
    window hide
    mia "Ahhh! Ah!"
    player "Yeah that's it just like that..."
    mia "AHN!"
    player "Tell me how it feels baby! Tell me how good this dick is!"
    mia "It's Amazing I love it!"

    scene fs emilyclosetmiasex22
    with Dissolve(0.5)
    emily "{i}W-Why is [povname] doing this to me?{/i}"
    emily "{i}But even if I hate it I can't...I can't look away!{/i}"

    show emilymiasex movie2
    window hide
    pause
    mia "AH! AH! AH!"
    player "Look at those fat tits bounce!"
    mia "Y-You're pounding me so hard [povname]!"
    player "Feels good doesn't it??!"
    mia "YES! YES IT'S AMAZING!!"
    emily "{i}Wow I...I've never seen Mia like this.{/i}"
    emily "{i}She's normally so mild mannered.{/i}"
    mia "AHHH! I'M GONNA CUM!!"
    mia "YOU'RE MAKING ME CUM WITH YOUR GIANT COCK!!"
    scene fs emilyclosetmiasex22
    with Dissolve(0.5)
    mia "UHHHN!"
    player "That's it baby cum all over my cock. Show her what she's missing!"
    mia "I...huh?"

    scene fs emilyclosetmiasex38
    with Dissolve(0.7)
    mia "Hah...hah..."
    player "There we go, good girl."
    player "God seriously, would you look at these massive tits."
    player "You're going to have to really satisfy me if you want to compete with these things."
    player "Above and beyond, you understand?"
    emily "...."
    mia "What...hah...are you saying?"
    player "Nothing baby, you did good."
    mia "Did you cum?"
    player "Not yet, get on your knees in front of the closet."
    mia "Okay."
    scene fs emilyclosetmiasex35
    with Dissolve(0.7)
    player "Yeah lift up your boobs just like that."
    mia "Hehe."
    player "Now close your eyes."
    scene fs emilyclosetmiasex36
    with Dissolve(0.5)
    mia "Like this?"
    player "Uh....yeah..."
    scene fs emilyclosetmiasex37
    with Dissolve(0.7)
    mia "Ahhhhh."
    player "Heh."
    player "You ready baby?"
    mia "Give it to me!"
    show emilymiasex movie3
    player "UGGGH."
    player "So fucking hot."
    pause
    scene fs blackblank
    with Dissolve(1.0)
    "Emily sneakily went back into the closet before Mia cleaned herself up and left."
    "After exchanging a few words and agreeing to meet up again she also left your place."
    $ emilyphase2interaction1 = 5
    $ emilyquestlog = "We were interrupted before, so I should talk to Emily about getting together"
    jump passtime

# interaction 2
# part 1

label emilyphase2interaction2part1:
    hide screen emily_atschool
    scene fs schoolhallway2
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    $ playerSprite = 1
    player "Emily, hey."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Oh [povname]."
    emily "Hi."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Okay, you're upset. I get it."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Why would you do that?!"
    emily "It was really....strange. Watching you two."
    $ emilySprite = 4
    $ playerSprite = 1
    player "I'll admit I did find it hot, I'm not gonna lie to you."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "What the heck!"
    $ emilySprite = 4
    $ playerSprite = 10
    player "BUT. But."
    $ playerSprite = 1
    player "We were almost caught, I literally had my dick out."
    player "I needed a distraction to take Mia's mind off things."
    player "If she really thought about it she would've put two and two together Em."
    player "I needed to act quickly."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Sigh....fine."
    emily "I guess."
    $ emilySprite = 4
    $ playerSprite = 1
    player "Let me make it up to you!"
    player "A proper date, just you and me!"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "A date? Really?"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Yeah! Let's go....to the beach! We can scout out a good place for the group later!"
    player "And we should go late evening, more romantic that way."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "That does sound pretty good..."
    $ emilySprite = 0
    $ playerSprite = 1
    player "{i}Just one more push..{/i}"
    player "I promise we can get up to some naughty things."
    $ playerSprite = 0
    $ emilySprite = 5
    emily "Wha-I don't....don't care about that!"
    $ emilySprite = 4
    emily "..."
    $ emilySprite = 1
    emily "Fine let's go! Tonight!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Awesome! Okay I'll see you there."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "See you there! Sunnyside beach!"
    $ emilySprite = 0
    $ emilyquestlog = "Gotta be honest, I'm looking forward to this evening beach date"
    $ emilyphase2interaction2 = 1
    jump passtime

# part 2

label emilyphase2interaction2part2:
    play music "audio/justbeach.mp3" fadein 10
    scene fs beachnight
    with Dissolve(1.0)
    $ emilySprite = 6
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    pause
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.7)
    pause
    $ playerSprite = 1
    player "Hey. Wait long?"
    $ playerSprite = 0
    $ emilySprite = 8
    emily "No. Just around 4 minutes after I got changed."
    $ playerSprite = 1
    $ emilySprite = 6
    player "Haha why so specific?"
    $ playerSprite = 0
    $ emilySprite = 8
    emily "Heh I dunno..."
    $ emilySprite = 6
    $ playerSprite = 17
    player "You look..."
    $ playerSprite = 1
    player "Let me change then we can start walking, we should get more light if we go around those rocks."
    $ playerSprite = 0
    $ emilySprite = 8
    emily "Okay yeah.."
    $ emilySprite = 6
    scene fs emilybeach1
    with Dissolve(1.0)
    pause
    scene fs emilybeach2b
    with Dissolve(0.5)
    emily "You were right, we really do get a lot more light here."
    scene fs emilybeach2
    player "Yeah the sun sets in this direction so it's the last to give off light."
    player "Can see some really great colors."
    scene fs emilybeach2b
    emily "Thanks for thinking of this [povname], I think it was a great idea."
    scene fs emilybeach2
    player "Not mad anymore?"
    scene fs emilybeach2b
    emily "Hehe maybe, maybe not."
    scene fs emilybeach1
    with Dissolve(1.0)
    pause
    scene fs emilybeach3
    with Dissolve(0.7)
    pause
    scene fs blackblank
    with Dissolve(0.5)
    "A little while later..."
    scene fs emilybeach4
    with Dissolve(0.5)
    emily "So then Mia said 'Wait that's pizza!'"
    player "Hahaha!"
    emily "Charlotte's legs slip over her head like a cartoon character, pizza is flying everywhere!"
    player "No way!"
    emily "And at that exact moment Olivia walks in and says-"
    emily "'Didn't I ask for Pepperoni?'"
    scene fs emilybeach5
    player "Hahahaha!"
    emily "Hahaha!"
    player "Oh my God, she never told me that one."
    scene fs emilybeach6b
    with Dissolve(0.5)
    player "Thanks for joining me Emily, this is really nice."
    scene fs emilybeach6c
    emily "I-I'm glad I came [povname]."
    emily "Things have been a li-"
    scene fs emilybeach6b
    player "Let me stop you right there, this date is supposed to be all about you."
    player "Let's forget about consequences or anything else, just for tonight."
    scene fs emilybeach7
    with Dissolve(0.7)
    player "I want to make you feel good."
    scene fs emilybeach8
    with Dissolve(0.5)
    emily "Oh um..."
    emily "I-If you insist."
    scene fs emilybeach8b
    with Dissolve(0.5)
    emily "Ah.."
    emily "You really like boobs don't you?"
    scene fs emilybeach8c
    emily "Ehn!"
    player "Haha yeah."
    scene fs emilybeach9
    with Dissolve(0.5)
    pause
    scene fs emilybeach9b
    with Dissolve(0.5)
    player "Beautiful."
    pause
    scene fs emilybeach10
    with Dissolve(0.5)
    pause
    scene fs emilybeach10b
    player "Tell me what you want."
    scene fs emilybeach10c
    emily "I think.."
    emily "I want you to kiss me..."
    scene fs emilybeach11
    with Dissolve(0.5)
    pause
    emily "Mmm."
    scene fs emilybeach12
    with Dissolve(0.5)
    emily "MMMPH!"
    image emilybeachfinger:
        "emily beach12.png"
        0.7
        "emily beach12b.png"
        0.7
        repeat
    show emilybeachfinger
    pause
    emily "Ahn...[povname]..."
    pause
    scene fs emilybeach13
    with Dissolve(0.5)
    emily "Oh Gosh!!"
    player "*Sucks*"
    
    image emilybeachboobsuck:
        "emily beach13.png"
        0.7
        "emily beach13b.png"
        0.7
        repeat
    show emilybeachboobsuck
    pause
    emily "Ahh! Why does that feel so much better than I think it should?"
    player "Mhhuhhn(I dunno)."
    pause
    scene fs emilybeach14
    emily "God [povname] I think I'm cumming!!"
    pause
    with flash
    scene fs emilybeach15
    with Dissolve(0.7)
    emily "Hah...hah."
    player "Felt good?"
    emily "Incredible...hah.."
    scene fs emilybeach15b
    emily "Thank you...again."
    scene fs emilybeach15c
    player "Anytime."
    scene fs emilybeach15
    with Dissolve(0.5)
    pause
    scene fs blackblank
    with Dissolve(0.7)
    pause
    player "Like seriously anytime, I will suck your tits whenever you want me to."
    emily "Oh my gosh shut up haha!"

    $ emilyquestlog = "We've taken things as far as they can go before fucking. One more step?"
    stop music fadeout 2
    $ emilyphase2interaction2 = 2
    jump passtime

# part 3

label emilyphase2interaction2part3:
    hide screen questboxpreview
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonROOM

    show fbplayer current:
        xalign 0.5 ypos 120
    player "{i}Alright. I'm calling Emily.{/i}"
    player "{i}I have no idea what kind of relationship I want with her.{/i}"
    player "{i}My emotions are all over the place.{/i}"
    player "{i}All I know is that right now...{/i}"
    $ playerSprite = 2
    "[povname]'s Phone" "*Briiing Briing*"
    player "{i}I need to fuck her brains out.{/i}"
    emily "Hello?"
    player "Hey."
    scene fs blackblank
    with Dissolve(1.0)
    "One invite and a little time later..."
    scene fs livingroomnight
    with Dissolve(0.7)

    $ emilySprite = 0
    show fbplayer current:
        xalign 0.4 ypos 120 
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)

    $ playerSprite = 1
    player "Uh...Hey."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Hehe. Hey."
    $ playerSprite = 1
    $ emilySprite = 0
    player "Sooo."
    $ playerSprite = 0
    $ emilySprite = 1
    show fbemily current:
        xalign 0.5 ypos 120
    with move
    emily "So."
    $ playerSprite = 1
    $ emilySprite = 0
    player "I was thinking."
    player "Put on a movie, get something nice to eat."
    player "Maybe open up some wine? Snuggle on the couch you know that kind of thing."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "That does sound nice."
    $ playerSprite = 1
    $ emilySprite = 0
    player "But I ALSO think.."
    $ playerSprite = 0
    emily "Hmm?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "Those are all things...we can do..."
    player "After."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "After?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "After."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Hehe after what?"
    $ playerSprite = 1
    $ emilySprite = 0
    player "I think you know exactly after what."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Hmmmm. Okay..."
    
    scene fs emilychapter2sex1b
    with Dissolve(1.0)
    emily "Ahnn."
    pause    
    player "Unbutton your shirt."
    emily "Okay.."
    scene fs emilychapter2sex2
    with Dissolve(0.5)
    emily "Oh..."
    pause  
    scene fs emilychapter2sex2b
    emily "Haha that tickles, but it feels really nice too..."
    pause      
    scene fs emilychapter2sex3
    with Dissolve(0.7)
    emily "Oh god [povname]."
    emily "[povname]!"
    emily "You always...make me feel so good."
    pause
    scene fs blackblank
    with Dissolve(1.0)
    pause
    show emilychapter2sex movie1
    emily "Hah hah hah!"
    pause
    scene fs emilychapter2sex6
    with Dissolve(0.5)
    player "How does it feel?"      
    scene fs emilychapter2sex6b
    with vpunch
    emily "Ahn!"
    scene fs emilychapter2sex6
    player "How does getting pounded by my cock feel hmm?"
    scene fs emilychapter2sex7
    with vpunch
    emily "Good! SO GOOD!"
    emily "I feel...primal!"
    emily "This is how it's supposed to be!"
    scene fs emilychapter2sex7c
    emily "This is how a woman has sex! I'm having sex!"
    emily "On my hands and knees like an ANIMAL!"
    player "{i}Damn she's really getting into it!{/i}"
    show emilychapter2sex movie2
    pause
    emily "My B-Boobs! They've never bounced like this before!"
    emily "I-I wasn't AHN!!"
    emily "I wasn't expecting that!"
    pause
    emily "Oh my gosh [povname] I'm really close!"
    player "Me too! Every fiber of my being is telling me to fill you up with cum."
    scene fs emilychapter2sex7b
    with vpunch
    emily "DO IT!"
    emily "Please!"
    player "But what about Mia?"
    emily "DO IT!!!!"     

    scene fs emilychapter2sex5
    with vpunch
    emily "AHHHN!!!"
    player "Fuck!"
    emily "Yes Yes! Just like I dreamed about!"
    pause      
    scene fs emilychapter2sex4
    with Dissolve(0.7)
    emily "Hah...hah."
    player "You..hah..good?"
    emily "Just...don't move.."
    pause      
    scene fs blackblank
    with Dissolve(1.0)
    emily "Stay like that for a bit..."

    $ emilyquestlog = "Wow. So fucking hot. I need to fuck her again at the beach trip"
    $ emilyphase2interaction2 = 3
    jump passtime

# end chapter 2
# end chapter 2 content

label emilybeachchapter2end:
    hide screen mia_beach1
    hide screen mia_beach2
    hide screen mia_beach3
    hide screen sophia_beach
    hide screen charlotte_beach
    hide screen ava_beach
    hide screen emily_beach
    hide screen olivia_beach
    hide screen backbuttonBEACH

    scene fs emilychapter2end1
    emily "Hmmm hmhm hmmm."
    scene fs emilychapter2end2
    player "Emily hey!"
    emily "[povname]!"
    player "Working on a sand castle?"
    emily "Yeah! Like it?"
    player "Didn't some little girl make this though?"
    emily "...."
    emily "I was thinking of adding a moat!"
    player "Well that would certainly help protext the castle from intruders!"
    emily "Haha yeah!"
    emily "The gallant knights must protect the princess's castle from enemies!"
    player "Neither sword nor dragon's breath will cross this bridge!"
    emily "Hehehe!"
    jump emilychoice

label emilychoice:
   # $ emilyphase2interaction2 = 3
    if emilyphase2interaction2 >= 3:
        "Would you like to end the day with Emily?"
        menu:
            "Romance":
                jump emilychapter2romance
            "Naughty":
                jump emilychapter2naughty
            "Degredation":
                jump emilychapter2degredation
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach

    label emilychapter2romance:
        player "But you know..."
        emily "Hmm?"
        player "There is one danger that moat cannot protect from!"
        emily "Haha what is i-"
        scene fs emilychapter2end3
        player "THE GIANT METEOR RAINING DOWN FROM THE SKYYYY!!!!"
        scene fs emilychapter2end4
        emily "N-Nonono!"
        emily "Wait!"
        scene fs emilychapter2end5
        emily "T-There's no meteor in this story haha..."
        emily "..."
        emily "..."
        scene fs emilychapter2end6
        player "AND THEN THE GIANT METEOR RAINS DOWN FROM THE SKYYYY!!!"
        emily "Ahhh! No stoooop!"
        scene fs emilychapter2end7
        player "Woah wait Emily careful!"
        emily "B-Balance!"
        scene fs emilychapter2end8
        with vpunch
        player "Ah."
        emily "Ouch."
        player "..."
        emily "..."
        scene fs emilychapter2end9
        emily "Hahaha!"
        player "Hehe oh man!"
        player "Sorry Em I was just fooling around."
        emily "It's okay! It was my own fault and the moat would've taken too long anyways."
        emily "Plus I like your fooling around haha!"
        scene fs emilychapter2end10
        player "Speaking of.."
        player "How about you and I...get away from the others for a little bit."
        scene fs emilychapter2end11
        emily "Oh...you mean.."
        emily "Right now? Here?"
        scene fs emilychapter2end10
        player "Your cuteness does something to me."
        player "Plus your bikini's got me all riled up"
        scene fs emilychapter2end11
        emily "Oh um..."
        scene fs emilychapter2end10
        player "If you want...I can keep it in when I cum."
        scene fs blackblank
        with Dissolve(0.7)
        emily "...."
        emily "Okay."
        show emilychapter2endsex movie1
        emily "Hah...hah.."
        player "Gotta say the showers is the perfect spot."
        emily "Ahn...ooohhhh."
        emily "{i}His hands! He's so good with them!{/i}"
        emily "{i}But it's his....cock that is incredible!{/i}"
        player "Hmmm, you seem a little quiet, maybe I should go a little harder"
        pause
        show emilychapter2endsex movie2
        emily "AHN! Oh G-God!"
        player "Does it feel good?"
        emily "It feeels...You feel incredible!"
        player "You're really tight Em, I'm really close."
        emily "O-Oh man oh man! Me too!!!"
        player "I believed I promised not to pull out!"
        pause
        show emilychapter2endsex movie4
        emily "UUUUHHHN!!!"
        player "FUCK!"
        pause
        show emilychapter2endsex movie3
        with Dissolve(0.7)
        emily "{i}He's doing it again, he's cumming inside me!{/i}"
        emily "{i}His love is filling me to the brim!!{/i}"
        pause
        scene fs blackblank
        with Dissolve(1.0)
        $ emilyquestlog = "I fucked her again at the beach. Seems she really wants my cock."
        $ endchapter2_trigger = "2 emily romantic"

        jump startofchapter3

    label emilychapter2naughty:
        player "But you know..."
        emily "Hmm?"
        player "There is one danger that moat cannot protect from!"
        emily "Haha what is i-"
        scene fs emilychapter2end3
        player "THE GIANT METEOR RAINING DOWN FROM THE SKYYYY!!!!"
        scene fs emilychapter2end4
        emily "N-Nonono!"
        emily "Wait!"
        scene fs emilychapter2end5
        emily "T-There's no meteor in this story haha..."
        emily "..."
        emily "..."
        scene fs emilychapter2end6
        player "AND THEN THE GIANT METEOR RAINS DOWN FROM THE SKYYYY!!!"
        emily "Ahhh! No stoooop!"
        scene fs emilychapter2end7
        player "Woah wait Emily careful!"
        emily "B-Balance!"
        scene fs emilychapter2end8
        with vpunch
        player "Ah."
        emily "Ouch."
        player "..."
        emily "..."
        scene fs emilychapter2end9
        emily "Hahaha!"
        player "Hehe oh man!"
        player "Sorry Em I was just fooling around."
        emily "It's okay! It was my own fault and the moat would've taken too long anyways."
        emily "Plus I like your fooling around haha!"
        scene fs emilychapter2end10
        player "Speaking of.."
        player "That bikini you're wearing."
        player "The black suits you, it's really nice."
        scene fs emilychapter2end11
        emily "Oh, um thank you."
        scene fs emilychapter2end10
        player "I want it off."
        scene fs emilychapter2end11
        emily "What?"
        scene fs emilychapter2end10
        player "I want it off you. Right now."
        scene fs blackblank
        with Dissolve(0.7)
        emily "Oh [povname] I don't know if-"
        player "Come with me. We're going to the showers and I'm going to stuff your pussy with my cock."
        emily "O-Okay."
        show emilychapter2endsex movie1
        emily "Hah...hah.."
        player "Ah fuck this is just what I need."
        emily "Ahn ahn!"
        player "You hanging in there Em?"
        emily "{i}He's inside me again!{/i}"
        emily "{i}He's cheating on Mia with me again!{/i}"
        player "Seems like my little slut has her mind elsewhere."
        player "Let me pick up the pace."
        pause
        show emilychapter2endsex movie2
        emily "AHN! Oh G-God!"
        player "Yeah there you go."
        emily "{i}His hand's around my neck! It's turning me on so much! {/i}"
        player "Wonder where the others are right now. Maybe looking for you hmmm?"
        emily "UUHN!"
        player "Haha I just felt you get tighter! Fuck I'm getting really close now Em."
        emily "Ahn ahn [povname]!"
        player "Fucking take it!"
        pause
        show emilychapter2endsex movie3
        emily "UUUUHHHN!!!"
        player "FUCK!"
        emily "{i}No!! Yes!! This feels so good I-{/i}"
        emily "{i}I can't think! I know this is wrong but I can't help but give in!{/i}"
        pause
        show emilychapter2endsex movie3
        player "I'm fucking cumming!!"
        show emilychapter2endsex movie4
        emily "OH MY GOD!"
        emily "{i}He's cumming inside me! I can feel it!{/i}"
        emily "{i}I-Is he trying breeding me?{/i}"
        pause
        scene fs blackblank
        with Dissolve(1.0)
        emily "{i}I...I love it.{/i}"
        $ endchapter2_trigger = "2 emily naughty"
        $ emilyquestlog = "I fucked her again at the beach. Seems she really wants my cock."
        jump startofchapter3

    label emilychapter2degredation:
        player "But you know..."
        emily "Hmm?"
        player "There is one danger that moat cannot protect from!"
        emily "Haha what is i-"
        scene fs emilychapter2end3
        player "THE GIANT METEOR RAINING DOWN FROM THE SKYYYY!!!!"
        scene fs emilychapter2end4
        emily "N-Nonono!"
        emily "Wait!"
        scene fs emilychapter2end5
        emily "T-There's no meteor in this story haha..."
        emily "..."
        emily "..."
        scene fs emilychapter2end6
        player "AND THEN THE GIANT METEOR RAINS DOWN FROM THE SKYYYY!!!"
        emily "Ahhh! No stoooop!"
        scene fs emilychapter2end7
        player "Woah wait Emily careful!"
        emily "B-Balance!"
        scene fs emilychapter2end8
        with vpunch
        player "Ah."
        emily "Ouch."
        player "..."
        emily "..."
        scene fs emilychapter2end9
        emily "Hahaha!"
        player "Hehe oh man!"
        player "Sorry Em I was just fooling around."
        emily "It's okay! It was my own fault and the moat would've taken too long anyways."
        emily "Plus I like your fooling around haha!"
        scene fs emilychapter2end10
        player "Speaking of.."
        player "That bikini you're wearing."
        player "The black suits you, it's really nice."
        scene fs emilychapter2end11
        emily "Oh, um thank you."
        scene fs emilychapter2end10
        player "I want it off."
        scene fs emilychapter2end11
        emily "What?"
        scene fs emilychapter2end10
        player "I want it off you. Right now."
        scene fs blackblank
        with Dissolve(0.7)
        emily "Oh [povname] I don't know if-"
        player "Come with me. We're going to the showers and I'm going to stuff your pussy with my cock."
        emily "O-Okay."
        scene fs emilychapter2degrade3
        with Dissolve(1.0)
        emily "..."
        emily "[povname]...I-"
        scene fs emilychapter2degrade2
        player "Shut up."
        scene fs emilychapter2degrade3
        emily "W-What?"
        scene fs emilychapter2degrade4
        with hpunch
        emily "Ahn!"
        scene fs emilychapter2degrade2
        with Dissolve(0.3)
        player "I said Shut up."
        scene fs emilychapter2degrade3
        emily "Why would you-"
        scene fs emilychapter2degrade4
        with hpunch
        emily "Oww! Stop!"
        scene fs emilychapter2degrade2
        with Dissolve(0.3)
        player "You're just a whore who sleeps with her best friend's boyfriend."
        scene fs emilychapter2degrade3
        emily "[povname] no I-"
        scene fs emilychapter2degrade5
        with hpunch
        emily "AHHHN!!"
        scene fs emilychapter2degrade7
        emily "Ooohh.."
        player "Are you going to be a good girl and listen?"
        scene fs emilychapter2degrade6
        emily "Y-Yes!"
        emily "I-I'll do what you want."
        scene fs emilychapter2degrade7
        player "Good."
        player "Now turn around and give me the only thing you're good for."
        pause
        show emilychapter2endsex movie1
        emily "Hah...hah.."
        player "Ah fuck still so tight."
        emily "Ahn ahn!"
        player "You like it don't you you fucking bitch."
        emily "{i}He's inside me again!{/i}"
        emily "{i}He's cheating on Mia with me again!{/i}"
        player "Seems like my little slut has her mind elsewhere."
        player "Let me pick up the pace."
        pause
        show emilychapter2endsex movie2
        emily "AHN! Oh G-God!"
        player "Yeah there you go."
        emily "{i}His hand's around my neck! It's turning me on so much! {/i}"
        player "Wonder where the others are right now. Maybe looking for you hmmm?"
        emily "UUHN!"
        player "Haha I just felt you get tighter! Fuck I'm getting really close now Em."
        emily "Ahn ahn [povname]!"
        player "Fucking take it!"
        pause
        show emilychapter2endsex movie3
        emily "UUUUHHHN!!!"
        player "FUCK!"
        show emilychapter2endsex movie4
        emily "{i}No!! Yes!! This feels so good I-{/i}"
        emily "{i}I can't think! I know this is wrong but I can't help but give in!{/i}"
        pause
        scene fs blackblank
        with Dissolve(1.0)
        $ emilyquestlog = "I fucked her again at the beach. Seems she really wants my cock."
        $ endchapter2_trigger = "2 emily degredation"
        jump startofchapter3

# start chapter 3

# Chapter 3 and related character scenes.

label emilyphase3interaction1part1:
    hide screen uppergui
    hide screen backbuttonROOM

    "Briing briing"
    scene fs playerroomDay
    with Dissolve(0.5)
    pause
    $ playerSprite = 2
    show fbplayer current:
        xalign 0.5 ypos 120
    player "Who's calling me so early? Ah it's Emily."
    $ playerSprite = 22
    show fbplayer current:
        xalign 0.58 ypos 120
    player "Hello."
    $ playerSprite = 21
    emily "Hey [povname]! You busy tonight?"
    $ playerSprite = 22
    player "I don't have any plans no, you want to hang out?"
    $ playerSprite = 21
    emily "They're playing 'Hide and Sneaks 2' at the theatre! Only this week!"
    emily "You want to join me?"
    $ playerSprite = 22
    player "Hide and Sneaks 2? The famously terrible sequel with god awful CGI that nobody asked for?"
    $ playerSprite = 21
    emily "The exact one."
    $ playerSprite = 22
    player "I will BE there!"
    $ playerSprite = 21
    emily "Haha great! I'll see you tomorrow. They only have day showings."
    $ playerSprite = 22
    player "Alright no problem, see you tomorrow."
    $ playerSprite = 2
    show fbplayer current:
        xalign 0.5 ypos 120
    "*click*"
    player "...."
    $ playerSprite = 7
    player "I'm going to need to bring my own snacks though."
    player "No way I'm paying those terrible theatre prices..."
    player "Hmmm. I'm feeling like candy. Of the strawberry variety..."

    $ emilydaychecker = dayNumber
    $ emilyphase3interaction1 = 1
    $ emilyquestlog = "I'll call Emily from my place tomorrow after I get some Candy from the store"
    jump returnwhereyouare

label emilyphase3interaction1part2:
    hide screen uppergui
    hide screen backbuttonROOM
    hide screen backbuttonROOM
    hide screen questboxpreview
    hide screen backbuttonLIVINGROOM
    hide screen phonecontacts

    scene fs livingroom
    with Dissolve(0.5)
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    player "Alright ready to go?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Ready, let's head out!"
    $ emilySprite = 0
    scene fs blackblank
    with Dissolve(0.7)
    pause
    scene fs emilytheatreandbj1
    with Dissolve(0.7)
    "There was barely anyone else in the theatre"
    "You figured it was because it was the middle of the day"
    "Or the fact this was a shitty 30 year old horror movie"
    "Either way the two of you enjoyed yourselves"
    scene fs emilytheatreandbj2
    "Movie" "Hehehe I'll fiiiiiiinnnnd youuuuu."
    player "Dude just look left."
    scene fs emilytheatreandbj3
    emily "Hehehe."
    player "Haha."
    "Movie" "Ahhhhhh no please ahhhhhh!."
    scene fs emilytheatreandbj5b
    with Dissolve(0.5)
    player "You liking it?"
    scene fs emilytheatreandbj5
    emily "Yeah! It's awful haha."
    emily "Want some popcorn?"
    scene fs emilytheatreandbj5b
    player "Nah I've got my candy."
    player "There's something else I want though."
    emily "Hmm?"
    scene fs emilytheatreandbj6
    with Dissolve(0.5)
    pause
    player "Mmmmmmwuah."
    scene fs emilytheatreandbj5
    with Dissolve(0.5)
    emily "Y-You can have one of those whenever you want!"
    scene fs emilytheatreandbj5b
    player "Hehe great cause I don't think I'm finished yet."
    scene fs emilytheatreandbj6
    with Dissolve(0.5)
    emily "Mmmmhh."
    scene fs emilytheatreandbj7
    with Dissolve(0.5)
    pause
    scene fs emilytheatreandbj8
    pause
    emily "Hmm?"
    scene fs blackblank
    with Dissolve(1.0)
    "Eventually the movie ends and the two of you walk out into the daylight"
    player "It's weird watching a movie in the theatre than going outside and it's still daytime."
    emily "Yeah it really is."
    emily "...."
    emily "How about we go to your place?"
    player "You got time?-"
    emily "Yup!"
    scene fs livingroom
    with Dissolve(0.5)
    pause
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    player "Alrighty home sweet home."
    player "You hungry?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Yes actually. I'm...craving something."
    $ emilySprite = 0
    $ playerSprite = 1
    player "Okay well I can check-"
    $ playerSprite = 0
    $ emilySprite = 1
    show fbemily current:
        xalign 0.45 ypos 120
    with move
    emily "Um wait a sec..."
    $ emilySprite = 0
    scene fs emilytheatreandbj9
    with Dissolve(0.5)
    emily "There's something I want to check."
    scene fs emilytheatreandbj9b
    player "Oh uh sure, go ahead."
    scene fs emilytheatreandbj10
    with Dissolve(0.5)
    player "{i}Oh she wants to make out?{/i}"
    player "{i}I don't have any reasons to refuse!{/i}"
    scene fs emilytheatreandbj11
    with Dissolve(0.5)
    pause
    emily "Mmmh!"
    emily "Auhn..Yesh.."
    scene fs emilytheatreandbj12
    emily "Hah...hah..t-this is it!"
    player "Hah...huh?"
    emily "Take off your pants."
    emily "Actually I can't wait just unzip them!"
    scene fs emilytheatreandbj13
    with Dissolve(0.7)
    player "Fuck Emily what's gotten into you?"
    emily "Just..p-please hurry."
    scene fs emilytheatreandbj14
    emily "!!!"
    emily "{i}This smell...the taste lingering on my tongue...{/i}"
    scene fs emilytheatreandbj15
    player "?"
    scene fs emilytheatreandbj16
    player "Fuck now that is quite the POV."
    scene fs emilytheatreandbj17
    pause
    scene fs emilytheatreandbj18
    player "Oh fuck.."
    emily "Mmmph."
    scene fs emilytheatreandbj19
    pause
    show emilymovie blowjob
    player "Ahhh.."
    player "{i}She's not sucking the whole thing but she doens't need to{/i}"
    player "What is up with you today?"
    emily "MMhn!"
    emily "Eh Neh it!"
    player "Did you just say you need it?"
    emily "Cuhm foa meh!"
    player "Fuck this is so hot Emily I'm gonna fucking cum right now!"
    scene fs emilytheatreandbj20
    pause
    show emilychapter3blowjob movie1
    pause
    emily "Ahh."
    player "UUUUGH!"
    player "Love seeing that cum all over your pretty little face!"
    scene fs emilytheatreandbj22
    with Dissolve(0.5)
    emily "*Gulp*"
    scene fs emilytheatreandbj22b
    emily "This...I don't believe it!"
    player "What do you mean?"
    emily "Your cum it's.."
    player "It's what?"
    scene fs emilytheatreandbj23
    with vpunch
    player "Ah shit!"
    emily "NEEH MOA!!"
    player "Em I just came my cock is super sensitive!"
    scene fs emilytheatreandbj24
    emily "GUHK!"
    player "Fuck fuck fuck!"
    player "How are you sucking so hard Jesus Christ!"
    emily "CUHM!"
    show emilychapter3blowjob movie2
    player "You want more cum you fucking slut?!"
    player "Here you-AHHRGH! Here you go!"
    scene fs emilytheatreandbj25
    pause
    emily "*Gulp* *Gulp*"
    scene fs emilytheatreandbj26
    player "Haaaah."
    player "H-Holy shit."
    player "Emily what's gotten into you?"
    emily "That's..hah..the taste.."
    player "What?"
    emily "I'd know it anywhere.."
    scene fs blackblank
    with Dissolve(1.0)
    "You help Emily clean herself up and get ready to go"
    "You offered to drive her home but she insisted on walking, albeit the whole time kind of in a daze"
    emily "That sweet sweet..."
    emily "Strawberry taste."

    $ emilyphase3interaction1 = 2
    $ emilyquestlog = "No more solo content for Emily this version(ch2.5)"
    jump passtime
