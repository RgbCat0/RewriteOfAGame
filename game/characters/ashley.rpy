# Ashley scenes.

label ashleyinteraction1part1:
    hide screen uppergui
    $ playerSprite = 7
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.5)
    player "Hmm."
    player "{i}I've been spending a lot of money at ShortSkirt lately.{i}"
    player "{i}Do I have a crush on Ashley?{i}"
    player "{i}I should pay her another visit.{i}"
    $ ashleychecker = 1
    jump playerRoom

label ashleyinteraction1part2:
    scene fs store
    with Dissolve(0.7)
    $ playerSprite = 0
    $ ashleySprite = 4
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbashley current:
        xalign 0.6 ypos 120

    $ ashleySprite = 5
    ashley "[povname]! I had a feeling you might be visiting today."
    $ ashleySprite = 4
    $ playerSprite = 1
    player "Really?"
    player "I woke up this morning and honestly just felt like coming to see you."
    $ playerSprite = 0
    $ ashleySprite = 5
    ashley "Haha is that why you've been buying so much recently?"
    ashley "Just an excuse to see me?"
    $ ashleySprite = 4
    $ playerSprite = 1
    player "Haha hey, two things can be true at once."
    player "So what are you doing? You look busy."
    player "I don't think I've ever seen you out from behind the counter."
    $ playerSprite = 0
    $ ashleySprite = 5
    show fbashley current:
        xalign 0.7 ypos 120
    with move
    ashley "Oh?"
    show fbashley current:
        xalign 0.8 xzoom -1.0 ypos 120
    ashley "Like what you see haha?"
    show fbashley current:
        xalign 0.6 xzoom 1.0 ypos 120
    with move
    $ ashleySprite = 4
    $ playerSprite = 1
    player "Very."
    $ playerSprite = 0
    $ ashleySprite = 5
    ashley "Well the truth is handsome, that I'm short on hands today. One of my underlings called in sick."
    $ ashleySprite = 4
    $ playerSprite = 17
    player "Oh that's too bad. Nothing I can do?"
    $ playerSprite = 0
    ashley "...."
    $ ashleySprite = 6
    show fbashley current:
        xalign 0.5 xzoom 1.0 ypos 120
    with move
    pause
    $ ashleySprite = 7
    $ playerSprite = 11
    ashley "Well...isn't that sweet of you to ask."
    ashley "Actually yes. Think you can man the register for a few hours?"
    $ ashleySprite = 4
    $ playerSprite = 17
    player "What?"
    $ playerSprite = 11
    $ ashleySprite = 5
    ashley "Hehe wait a second."
    $ ashleySprite = 4
    hide fbashley current
    pause
    $ ashleySprite = 8
    show fbashley current:
        xalign 0.5 ypos 120
    ashley "Okay put this on handsome."
    $ playerSprite = 17
    player "I-really?"
    $ playerSprite = 11
    ashley "Yeah I really need to de-stress, go over some..assets behind the counter."
    $ playerSprite = 17
    player "Okay I guess...bu-"
    $ playerSprite = 11
    ashley "Alright so the new lingerie from Bonjour Aujourd'hui are late and arriving next week."
    ashley "The batteries have a new spot at the back."
    ashley "If customers want to duplicate keys they can do it the next store down on the left side."
    ashley "Crop tops, Short Jorts, Booty Shorts, and Thongs are all half off for the next 3 days."
    ashley "Oh and if anyone asks for my PERSONAL merchandise. All the prepaid orders are in boxes by the window ready for pickup."
    ashley "Got all that hun?"
    $ playerSprite = 17
    player "Uh...merchandise..left side...booty shorts?"
    $ playerSprite = 11
    ashley "I'm sure you'll do fine!"
    ashley "Now get behind the register, and don't mind me while I'm down there..."
    $ ashleySprite = 4
    $ playerSprite = 17
    hide fbashley current
    player "Down there?"
    $ playerSprite = 11
    hide fbplayer current

    scene fs ashleybj7
    with Dissolve(1.0)
    pause
    "Make sure to help the customers perfectly"
    "The more you help them, the further Ashley will go"
    player "{i}Okay this should be fine, just a little customer service for a while.{/i}"
    player "{i}...I hate customer service.{/i}"
    scene fs ashleybj1
    player "{i}Huh? Oh that's Ashley, must've brushed up against my crotch by acciden-{/i}"
    scene fs ashleybj2
    player "{i}That's not an accident!{/i}"
    "*Ding*"
    "Customer" "Hello there young fella!"
    scene fs ashleybj3
    player "{i}OH GOD NO{/i}"
    player "H-Hello there sir! How can I help you?"
    "Customer" "I wanna get some batteries, where dey at?"
    menu:
        "They're at the back":
            jump continueashleybj1
        "They're down the hall":
            jump ashleybadending1
        "I dunno.":
            jump ashleybadending1
label continueashleybj1:
    player "There's just at the back sir."
    scene fs ashleybj4
    pause
    scene fs ashleybj6
    "Customer" "Ah right I see em now."
    player "I'll ring you up."
    "*Beep*"
    scene fs ashleybj5
    pause
    scene fs ashleybj8
    with Dissolve(0.7)
    "Customer" "Thank you young fella"
    player "No problem sir you have a beautiful day."
    "*Ding*"
    "Customer" "Hey do you guys still cut keys?"
    menu:
        "Yes they're in the back":
            jump ashleybadending1
        "No, check down the left hall":
            jump continueashleybj2
        "No, check down the right hall":
            jump ashleybadending1

label continueashleybj2:
    player "No sorry, but if you go left down the hall that store will cut keys for you."
    "Customer" "Awesome thanks."
    show ashleyblowjob movie1
    player "No pro-AHH-blem"
    "*Ding*"
    "Customer" "Hiiii"
    player "Hello ma'am, how can I help you today?"
    "Customer" "Me and some girlfriends are getting together next weekend to complain about our husbands."
    "Customer" "I want to show off my new look. I've been working out to get a killer body, they should see it!"
    player "As should everyone ma'am you look great."
    "Customer" "Oh yeah?"
    menu:
        "Killer ugly, you won't look good in anything":
            jump ashleybadending2
        "Our sundresses are half off right now!":
            jump ashleybadending2
        "Our crop tops and booty shorts are half off right now!":
            jump continueashleybj3

label continueashleybj3:
    player "Trust me. You'd look amazing in one of our crop tops and booty shorts, they're half off!"
    player "And so are our thongs if you're feeling bold enough."
    "Customer" "That's wonderful! I'll take...this, this, and this one!"
    "*Beep*"
    show ashleyblowjob movie2
    player "Wonderful choiCESSS ma'am. H-Have a great day."
    "Customer" "Thank you!"
    player "{i}I don't know how much longer I can hold on.{/i}"
    player "{i}Ashley's taking my entire cock down her throat like it's nothing!{/i}"
    "*Ding*"
    player "{i}Shit a group of scantily-clad highschool girls!{/i}"
    "Customer" "Hehehe stop it!"
    "Customer" "Hehe sorry, hi."
    player "Hey."
    player "How can I help you ladies?"
    "Customer" "Your like, crop tops are half off right now yeah?"
    player "Yes they are."
    "Customer" "Awesome, we were also looking for like.."
    "Customer" "She wants to get some sexy underwear!"
    "Customer" "OHMYGOD Jennifer."
    "Customer" "You're gonna have to ask if you wanna look good for last prom next month just sayinnng."
    menu:
        "We don't sell lingerie":
            jump ashleybadending2
        "Our lingerie is late":
            jump continueashleybj4
        "We're out of lingerie":
            jump ashleybadending2

label continueashleybj4:
    player "Sounds like fun. Unfortunately our Bonjour Aujourd'hui selection is late and will be arriving next week."

    show ashleyblowjob movie3
    pause
    "Customer" "Oh that's okay, we can come back next week no problem."
    "Customer" "Especially if YOU'RE here."
    "Customer" "JENNIFER."
    "Customer" "Hehehe"
    player "Haha."
    "Customer" "Um there was actually like one more thing."
    player "Of course."
    "Customer" "I-Is Ashley in today?"
    player "She's in today but currently has her mouth full."
    player "But I promise I can answer any questions you have."
    "Customer" "Oh uh okay."
    "Customer" "Just assssskkk."
    "Customer" "I ordered uh..like..something from her?"
    "Customer" "Oh my God, You got that Giant dildo didn't you!?"
    "Customer" "JENNIFER I SWEAR TO GOD."
    "Customer" "Don't get mad! I got one too I was about to ask about it."
    player "Miss, don't worry."
    "Customer" "Y-Yeah?"
    player "Ashley told me You and Jennifer's packages are right by the window over there."
    "Customer" "T-Thanks."
    player "Not a problem."
    "Customer" "Hey Mr.Cashier guy! Can I get a pic?"
    player "Yeah?"
    "*Snap*"
    player "How do I look?"
    "Customer" "Oh I am totally using this when I break in my Cock-Rocket tonight."
    "Customer" "Here's something to rememeber us by!"

    show ashleyblowjob movie4
    "The energetic girl turns around and flips her skirt up exposing an absolute unit of an ass which had no business being attached to someone so lean"
    player "OH FUCK!"
    "Customer" "JENNIFER I'M LITERALLY GOING TO KILL YOU."

    scene fs ashleybj12
    with Dissolve(0.7)
    "Customer" "Hahaha!"
    "*Ding*"
    pause

    scene fs store
    with Dissolve(0.7)
    $ playerSprite = 0
    $ ashleySprite = 4
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbashley current:
        xalign 0.6 ypos 120

    $ ashleySprite = 5
    ashley "Not bad for your first day!"
    $ ashleySprite = 4
    $ playerSprite = 1
    player "Jesus Christ Ashley, you're incredible."
    $ playerSprite = 0
    $ ashleySprite = 5
    ashley "Oh well..haha I don't know about that."
    $ ashleySprite = 4
    $ playerSprite = 1
    player "Seriously that was so fucking hot."
    player "Were you able to de-stress?"
    $ playerSprite = 0
    $ ashleySprite = 5
    ashley "Oh honey I defintiely got what I needed."
    $ ashleySprite = 4
    $ playerSprite = 1
    player "Ashame, cause I definitely want more sometime."
    $ playerSprite = 0
    $ ashleySprite = 5
    ashley "I...can't say I disagree."
    $ ashleySprite = 4
    $ playerSprite = 1
    player "See you later?"
    $ playerSprite = 0
    $ ashleySprite = 5
    ashley "See you later."
    $ ashleySprite = 4

    $ ashleychecker = 2
    jump passtime

label ashleybadending1:
    scene fs ashleybj11
    ashley "Hey sorry about that he's new!"
    scene fs blackblank
    with Dissolve(0.5)
    "Ashley deals with the customer and shoos you out the door, better to come back another time.."
    jump passtime

label ashleybadending2:
    scene fs ashleybj9
    pause
    scene fs ashleybj10
    pause
    scene fs ashleybj11
    ashley "Hey sorry about that he's new!"
    scene fs blackblank
    with Dissolve(0.5)
    "Ashley deals with the customer and shoos you out the door, better to come back another time.."
    jump passtime
