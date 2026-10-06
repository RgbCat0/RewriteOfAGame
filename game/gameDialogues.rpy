# Shared story scenes and chapter events.

# Startup and chapter 2 skip presets

label gameIntro:

    $ miaphase1interaction3 = 0
    $ avaphase1interaction2 = 0
    $ sophiaphase1interaction2 = 0
    $ oliviaphase1interaction3 = 0
    $ emilyphase1interaction2 = 0
    $ charlottephase1interaction3 = 0

    scene fs kylemercurylogo
    pause
    scene fs adultwarningpage
    pause
    scene fs askforname

    python:
        povname = renpy.input("")
        povname = povname.strip()

        if not povname:
            povname = "Anon"

    scene fs kylemercurylogo
    "Would you like to skip to chapter 2?"
    menu:
        "Yes":
            jump skiptochapter2
        "No":
            jump startthegame


label skiptochapter2:
    scene fs chapter2background
    with Dissolve(0.5)
    "Who did you spend time with after the track meet?"
    $ miaphase1interaction1 = 5
    $ miaphase1interaction2 = 5
    $ miaphase1interaction3 = 5
    $ miaquestlog = "Contact Mia on your phone, then visit her room during Day for the shopping trip."
    $ miaquesticon = "gui/questboxMia.png"

    $ katiequestlog = "Text Katie using your phone. Wait until a later day between conversations."
    $ katiequesticon = "gui/questboxKatie.png"
    $ contact_list.append("Katie")

    $ avaphase1interaction1 = 6
    $ avaphase1interaction2 = 4
    $ avaquestlog = "Visit Ava at the gym during Morning."
    $ avaquesticon = "gui/questboxAva.png"

    $ sophiaphase1interaction1 = 5
    $ sophiaphase1interaction2 = 3
    $ sophiaquestlog = "Visit Sophia's house during Morning."
    $ sophiaquesticon = "gui/questboxSophia.png"

    $ oliviaphase1interaction1 = 4
    $ oliviaphase1interaction3 = 2
    $ oliviaquestlog = "Meet Olivia at the arcade during Day."
    $ oliviaquesticon = "gui/questboxOlivia.png"

    $ emilyphase1interaction2 = 6
    $ emilyphase1interaction1 = 5
    $ emilyquestlog = "After the track meet on day 10, meet Emily in the school hallway during Morning."
    $ contact_list.append("Emily")
    $ emilyquesticon = "gui/questboxEmily.png"

    $ charlottephase1interaction1 = 5
    $ charlottephase1interaction2 = 4
    $ charlottephase1interaction3 = 2
    $ charlottequestlog = "Visit Charlotte at Cafe Seni in Sunnyside during Morning."
    $ charlottequesticon = "gui/questboxCharlotte.png"

    $ victoriaquesticon = "gui/questboxVictoria.png"
    $ victoriaquestlog = "Continue Charlotte's story in chapter 2 to unlock more visits with Victoria at Charlotte's house."

    $ firsttimestore = 1

    $ dayNumber = 10
    menu:
        "Mia":
            jump startchapter2Mia
        "Ava":
            jump startchapter2Ava
        "Sophia":
            jump startchapter2Sophia
        "Olivia":
            jump startchapter2Olivia
        "Emily":
            jump startchapter2Emily
        "Charlotte":
            jump startchapter2Charlotte
        "Nobody":
            jump startchapter2Nobody
        "Restart":
            jump gameIntro


label startchapter2Mia:
    $ endchapter1_trigger = "1 mia neutral"
    jump startofchapter2


label startchapter2Ava:
    menu:
        "Romantic":
            $ endchapter1_trigger = "1 ava romantic"
        "Naughty":
            $ endchapter1_trigger = "1 ava naughty"

    jump startofchapter2


label startchapter2Sophia:
    menu:
        "Romantic":
            $ endchapter1_trigger = "1 sophia romantic"
        "Naughty":
            $ endchapter1_trigger = "1 sophia naughty"

    jump startofchapter2


label startchapter2Olivia:
    menu:
        "Romantic":
            $ endchapter1_trigger = "1 olivia romantic"
        "Naughty":
            $ endchapter1_trigger = "1 olivia naughty"

    jump startofchapter2


label startchapter2Emily:
    menu:
        "Romantic":
            $ endchapter1_trigger = "1 emily romantic"
        "Naughty":
            $ endchapter1_trigger = "1 emily naughty"
        "Degradation":
            $ endchapter1_trigger = "1 emily degredation"

    jump startofchapter2


label startchapter2Charlotte:
    menu:
        "Romantic":
            $ endchapter1_trigger = "1 charlotte romantic"
        "Naughty":
            $ endchapter1_trigger = "1 charlotte naughty"

    jump startofchapter2


label startchapter2Nobody:
    jump esch1_check


# Chapter 1: introduction

label startthegame:
    scene fs blackblank
    with Dissolve(0.5)
    play sound "audio/miagameaudio/miastartingmoan.wav"

    mia "Hah..hah..hah!"
    mia "Ah!"
    player "You like that?"
    mia "Y-Yes! I'm getting close."
    player "Your pussy's so good!"
    mia "AHN! AHN! AHN!"
    $ hiden_textbox = True
    scene fs firstsexmia1
    with Dissolve(1.0)
    window hide
    pause
    mia "I'm cumming!"
    player "Fuck me too!"
    scene fs firstsexmia2
    with hpunch
    play sound "audio/miagameaudio/miastartcum.wav"
    with flash
    window hide
    pause
    mia "AHHHHHHH!"
    player "ERGGH!"
    window hide
    pause
    scene fs blackblank
    with Dissolve(1.0)

    player "{i}You may be wondering why we're starting this story with a sex scene.{/i}"
    player "{i}Well, that's cause it's where my story begins.{/i}"
    player "{i}Or rather, it's where THE story begins.{/i}"
    player "{i}I’m a freelance programmer and it’s my first year after college.{/i}"
    player "{i}The girl you just saw who let me cum inside her (She’s amazing) is my girlfriend Mia. She’s in her last year of college and we started dating just over a month ago.{/i}"

    player "{i}She's really close to her friends and to really know her, you have to know them too.{/i}"
    jump startofchapter1


label continuegamechapter1:
    scene fs miamorning1
    with Dissolve(2.0)
    window hide
    pause
    scene fs miamorning2

    mia "Good morning."
    scene fs miamorning1
    player "Haha morning."
    player "Were you watching me sleep?"
    scene fs miamorning3

    mia "Just for a little bit hehe!"
    scene fs miamorning1
    player "Well this is quite the sight to wake up to."
    scene fs miamorning3
    mia "I thought you might like it."
    scene fs miamorning2
    mia "Last night was amazing."
    scene fs miamorning1
    player "Sure was. I loved every second of it."
    player "At least I think I did, we should try again to make sure."
    scene fs miamorning3
    mia "Haha yeah I wouldn't mind doing it again soon!"
    scene fs miamorning1
    player "Nice."
    scene fs miamorning4
    with Dissolve(0.7)
    mia "I should probably get ready."

    scene fs miamorning5
    with Dissolve(0.7)
    mia "Are you still going to stop by the café?"
    player "Huh? Oh yeah I’ll head over after I take a shower."

    scene fs miamorning6
    with Dissolve(0.7)
    player "{i}God damn I am one lucky S.O.B.{/i}"
    scene fs miamorning8
    with Dissolve(0.7)
    mia "Great! I can’t wait to introduce you to everyone!"

    scene fs miamorning7
    player "Oh yeah..."
    scene fs miamorning8
    mia "You didn't forget did you?"

    scene fs miamorning7
    player "No no of course not, I'll be there."
    scene fs miamorning8
    mia "Great! See you soon then!"
    scene fs miamorning7
    player "See you soon babe."
    scene fs miafalling1
    with Dissolve(1.0)

    play music "audio/Main theme (Double Loop).mp3" fadein 5

    player "{i}How should I explain this to you? You know those shows that have a bunch of female characters all with different personality types but they're great friends anyways?{/i}"

    player "{i}And even if it’s a smaller group but there’s a main generic girl the story follows who believes in friendship or magic that always saves the day?{/i}"

    player "{i}Yeah that’s EXACTLY the dynamic of my girlfriend's group. But she isn’t the main character oh no.{/i}"
    player "{i}There is ALWAYS that one bumbling side character with huge tits who’s a lovable, clumsy moron who never gets the spotlight.{/i}"

    player "{i}I’m not saying Mia’s a moron but she spaces out real easy and has a hard time being aware of her immediate surroundings...{/i}"
    voice "audio/miagameaudio/miaah.wav"
    scene fs miafalling2

    window hide
    pause
    scene fs blackblank
    pause
    scene fs miafalling3
    with Dissolve(0.5)
    voice "audio/miagameaudio/mialaugh2.wav"
    player "{i}But that’s why I like her, she’s super chill and goes with the flow. Hardly ever disagrees with me and did I mention she has huge tits?{/i}"
    scene fs miafalling1
    with Dissolve(1.0)
    player "{i}Anyways the point is, I went for the ‘side character’ that everybody seems to forget about.{/i}"
    player "{i}And although I have no idea why she’s going out with me I  definitely love her, and I'm going to take advantage of everything I can while we're together!{/i}"

    scene fs grouptablechat0
    with Dissolve(1.5)
    window hide
    pause
    scene fs tablenomcAva
    ava "...I dunno I kinda like these tall seat table things..."
    scene fs tablenomcMia
    voice "audio/miagameaudio/miaheygirls.wav"
    mia "Hey girls!"
    scene fs tablenomcCharlottehappy
    voice "audio/charlottegameaudio/charlottehimia.wav"
    charlotte "Hi Mia!"
    scene fs tablenoMCEmilyMiaturn
    voice "audio/emilygameaudio/emilyhimia.wav"
    emily  "Mia, Welcome!"
    scene fs tablenoMCOliviaMiaturn
    voice "audio/oliviagameaudio/oliviahimia.wav"
    olivia "{size=-5}Hi Mia..{/size}"
    scene fs tablehiolivia
    with Dissolve(0.3)
    voice "audio/miagameaudio/miahehe.wav"
    mia "Hehe hello Olivia."
    scene fs tablenomcAva
    ava "Sooooo where is he??!"
    scene fs tablenomcSophia
    voice "audio/sophiagameaudio/sophiahimia.wav"
    sophia "Hi Mia! Where’s who?"
    scene fs tablenomcAva
    ava "Mia's showing us her boyfriend today!"
    scene fs tablenomcCharlottesurprise
    charlotte "WHAT??!"
    scene fs tablenomcEmilysurprise
    emily "Boyfriend!?"
    scene fs tablenomcSophia
    sophia "Ohmygosh Mia congratulations! I didn’t even know you were dating anyone."
    scene fs tablenomcMia
    mia "We wanted to keep it um, 'on the down low' before we knew we were serious."
    scene fs tablenomcAva
    ava "Oh so you’re serious now are you?"
    scene fs tablenomcMia
    voice "audio/miagameaudio/miahehe.wav"
    mia "Hehe!"
    scene fs grouptablechat1
    olivia "....."
    scene fs tablenomcMia
    mia "So what did you guys do for the weekend?"
    scene fs tablenomcAvaZ
    with Dissolve(0.5)
    ava "Well I went shopping for a new track suit."
    player "{i}This is Ava, typical sporty girl who loves doing all things athletic and working out. To be honest I don’t know anything else about her.{/i}"
    scene fs tablenomcSophiaZ
    with Dissolve(0.5)
    sophia "I baked some cookies! I’ve almost perfected the recipe hehehe."
    scene fs tablenomcSophiaZ2
    with Dissolve(0.5)
    player "{i}Sophia. If you’re wondering how cliché we can get strap yourself in cause she’s my childhood friend.{/i}"
    player "{i}Yes I know I know, but don’t worry we’re strictly friends. We never dated or flirted, just hung out and had good times like any normal pair of good friends, I don’t have any feelings for her and I’m sure she doesn’t have any for me.{/i}"
    player "{i}Perfectly sure, one hundred percent...probably."
    player "{i}Well I’m dating Mia now so it wouldn’t matter anyways.{/i}"
    scene fs tablenomcCharlotte
    with Dissolve(0.5)
    charlotte "GAH! One of you guys should’ve invited me to something I just lounged around the house all day!"
    scene fs tablenomcMia
    mia "I thought your dad was coming to visit though?"
    scene fs tableCharlotteSadZOOM
    with Dissolve(0.5)
    charlotte "Daddy could only stay for an hour before he had to go on another business trip..."
    player "{i}Charlotte is, as you might’ve guessed, a rich girl with foreign parents.{/i}"
    player "{i}You’ll never find another person on the planet who says and does the opposite of what they want to say and do.{/i}"
    player "{i}She does care a lot for her friends though.{/i}"

    scene fs tablenomcOliviaZ
    with Dissolve(0.5)
    olivia "I won a local kerokero fight tournament."
    player "{i}Ah Olivia, if the other girls didn’t drag her out of her house every now and then she’d stay at home playing video games and commenting on message boards.{/i}"
    player "{i}For any normal person this’d be a problem but apparently she has a genius level  IQ and aces every test she takes.{/i}"

    scene fs tablenomcEmilyZA
    with Dissolve(0.5)
    emily "Congrats Olivia! The other contestants didn’t stand a chance I’m sure."

    player "{i}Ugh.{/i}"
    scene fs tablenomcEmilyZ
    with Dissolve(0.5)
    emily "I spent the day organizing the upcoming track meet and picking up the team banner so we can paint it this week."

    player "{i}Alright lastly we come to Emily. She is my least favorite of all the girls.{/i}"
    player "{i}Emily is the ‘Main Character’ to this group of friends. The leader, protagonist, whatever else you want to call her.{/i}"
    player "{i}A perfect yet flawed flower who the audience can relate to, always solves troubles with the power of friendship or whatever.{/i}"
    player "{i}If she went by another name, it'd be 'Mary-Sue'.{/i}"
    player "{i}Sorry about that. I guess I have a bias, I'm not happy about Mia and the rest of them playing second fiddle to a girl who doesn't have any distinguishing facial features.{/i}"
    scene fs blackblank
    with Dissolve(1.0)
    player "{i}But hey I should probably shut up and let you decide for yourself what to think about her. I just rather stick with my big titty angel.{/i}"
    scene fs grouptablechat1
    with Dissolve(1.0)
    player "{i}Well enough of my exposition and inner monologue or whatever, let’s continue the story.{/i}"
    hide fs grouptablechat1
    jump postIntro


label introductions:
    scene fs tablenomcEmily
    emily "We’re all working really hard to cheer you on next week Ava!"
    scene fs tablenomcCharlottehappy
    charlotte "Yeah you’re gonna cream the competition!"
    scene fs tablenomcSophiaht
    sophia "We’ll be right there in the stands cheering!"
    scene fs tablenomcAva
    ava "Aww thanks guys!"
    scene fs tablenomcMiaYawn

    mia "You *Yaaaawwwnn* g-got this Ava!"
    scene fs tablenomcEmily
    emily "Mia? Why are you so tired it’s almost noon."
    scene fs tablehiolivia
    mia "Oh I didn’t get much sleep last night, sorry."
    scene fs tablenomcSophia
    sophia "Oh? What kept you up?"
    scene fs tablenomcMia
    mia "My boyfriend and I had sex for pretty much the whole night so I didn’t get a wink of sleep..."
    scene fs tablesurprisedrop
    sophia "...."
    emily "...."
    "Everyone Else Too" "...."
    scene fs tablenomcSurpriseCeptMia
    voice "audio/everybodyhuh.wav"
    "Everyone" "WHAT!!?? "
    scene fs tablenomcsurpriseAva
    ava "Hahahaha!"
    scene fs tablenoMCSophiaDepressed
    with Dissolve(0.5)
    sophia "It actually happened, I can’t believe Mia had sex before me. I can’t let Olivia get ahead too!"
    olivia "...."
    scene fs tablenoMCCharlottewhatwasitlike
    charlotte "W-What was it like?"
    scene fs tablenomcMia
    with Dissolve(0.5)
    mia "Well we had to go slow at first but once we hit a rythm and it felt really good it was um....intense?"
    mia "At one point he put my legs above my head an-"
    scene fs tablenomcEmily
    emily "OKAAAY!"
    emily "Mia don't you think that’s a really private thing that maybe you should keep to yourself?"
    scene fs grouptablechat1
    charlotte "{size=-5} Damn...{/size}"
    scene fs tablenoMCMiaEmbarassed
    mia "Oh...OH my gosh! What am I saying I’m so stupid!"
    scene fs tablenomcAva
    ava "Little late to be embarrassed now haha."
    scene fs tablenomcSophia
    sophia "I still can’t belie-"
    scene fs tableMC
    player "Hello Ladies!"
    scene fs tableSophiasurprise
    with vpunch
    sophia "OOH!"
    scene fs tableSophia
    sophia "Girls this is-"
    scene fs tableMia
    mia "[povname]!"
    scene fs tableMiaKiss

    mia "*Chuu*"

    scene fs tableSophiasurprise
    sophia "W-What!?"
    scene fs tableohheysophia
    with Dissolve(0.3)
    player "Oh hey Sophia."
    scene fs tableMCYourTheBoyfriend
    with Dissolve(0.3)
    sophia "Y-Y-You’re dating Mia? YOU’RE the boyfriend?!"
    scene fs tableohheysophia
    player "Yeah, you didn’t know? I thought Mia would've told you."
    scene fs tableMia
    mia "I didn’t know you knew each other!"
    scene fs tableMCYourTheBoyfriend
    sophia "So...You two had s-s-se-se-"
    scene fs tableHadSomeSecret
    ava "Had some secret! Where were you hiding such a hunk Mia?"
    scene fs tableCharlottepfft
    charlotte "pfft."
    scene fs tableHadSomeSecret
    ava "Name’s Ava!"
    scene fs tableMClookleftMC
    with Dissolve(0.3)
    player "Well I like you already Ava nice to meet you!"
    scene fs tableSohpiacantbelieve
    sophia "I can’t believe this..."
    scene fs tableOliviasaidthatalready
    olivia "You said that like three times Sophia."
    scene fs tablebequietOlivia
    sophia "And I like you better when you’re quiet Olivia."
    olivia "...."
    scene fs tableMia
    with Dissolve(0.5)
    mia "So uh, a bit late on the introductions but, girls this is my boyfriend [povname]."
    scene fs tableMC
    player "Hey."
    scene fs tableMia
    mia "And this is, Emily, Charlotte, Olivia, and you already know Sophia and Ava now."
    scene fs tableEmily
    emily "Nice to meet you!"
    scene fs tableCharlotte
    charlotte "Hmph. Hello."
    scene fs tableOlivia
    olivia "Hi.."
    scene fs tableAva
    ava "Hey again!"
    scene fs tableSohpiacantbelieve
    with Dissolve(0.5)
    sophia "I gotta sit down.."
    scene fs tableOliviasaidthatalready
    olivia "You are sitting down."
    scene fs tablebequietOlivia
    sophia "Shut it Olivia!"
    scene fs tableMC
    with Dissolve(0.5)
    player "Well uh, sorry I have to keep it so brief but I gotta get back to work to finish up a big project."
    scene fs tableMia
    mia "But after tonight you’ll be free for a while right?"
    scene fs tableMC
    player "Yeah I’ll have a pretty open schedule for about a month."
    scene fs tableMia
    mia "So you can stop by our school and visit us?"
    scene fs tableMC
    player "Yeah sure, I’d love to see you when you’re free."
    scene fs tableMia
    mia "Teehee, great!"
    scene fs tableMC
    player "Bye girls."
    scene fs tableSophiaSadZOOM
    with Dissolve(1.0)
    sophia "{i}I've liked [povname] for years! And Mia's the one who's dating him??{/i}"
    scene fs tableNoMCSophiaBoobs
    with Dissolve(0.5)
    sophia "{i}Why couldn't Mom've given me bigger boobs...{/i}"
    window hide
    pause
    scene fs blackblank
    with Dissolve(0.8)
    "Welcome to My Girlfriend’s Friends!"
    scene fs playerroomMorn
    with Dissolve(1.0)
    "Now that the intro is finished, after a few things are explained you are free to start playing the game"
    "You are a freelance programmer and can pick up a quick coding job whenever you want, although it will move time forward by one stage"
    "Each day is separated into morning, day time, and night. Characters will be at different locations at different times"
    "Most actions and a few conversations will move time forward as well, so make sure you choose correct options lest you run out of time"
    "There are three chapters in this game, in this version (Ch2.0C) you will be able to play all of the first chapter and a decent amount of chapter 2."
    "Moving on."
    "The Calender in your room will tell you how many days are left in the chapter"
    "There is now a quest button on the left side of the screen that you can click to help you on what to do next"
    "You can use your phone and access the travel map or bag by clicking the appropriate buttons in the top right"
    "The world is now open to you, you may talk to and interact with whomever you choose but be wary of who you spend your time with, if you spread your time out too equally you might end up wasting it"
    "Please keep in mind chapter 2.0C is unfinished, future updates will add more dialogue, art, and overall content to make a fuller experience."
    "So you may notice not everything flows perfectly right now."
    "Also with this version we've added some audio, you can adjust the volume in the menu as you like."
    "With that said have fun, and if you want to support the game please visit my {a=https://Patreon.com/KyleMercury}Patreon{/a} or my {a=https://kyle-mercury.itch.io/my-girlfriends-friend}Itch.io{/a} page"
    "Cheers!"
    hide fs playerroomMorn
    jump playerRoom


# Shared wakeup routing

label specialwakeup:
    hide screen backbuttonROOM
    if special_wakeup_target() is not None:
        jump expression special_wakeup_target()
    jump returnwhereyouare


# Chapter 1 ending: track meet

label phase1ending:
    scene fs blackblank
    hide screen uppergui
    hide screen backbuttonROOM
    "The day of the track meet has arrived."
    scene fs playerroomMorn
    with Dissolve(1.0)
    show fbplayer current:
        xalign 0.5 ypos 120

    player "I gotta leave quickly and meet up with everyone."
    scene fs blackblank
    with Dissolve(0.7)
    "You get yourself ready and head out the door to your car"
    "You haven't really gotten a chance to drive it yet so you're pretty excited"
    "However your excitement was short lived since it didn't take long before you arrived at the sports field"
    player "Alright now where are they? We're supposed to meet out front I think."

    scene fs trackmeet
    with Dissolve(0.7)

    $ emilySprite = 0
    $ sophiaSprite = 0
    $ playerSprite = 0
    $ miaSprite = 0
    $ oliviaSprite = 8
    $ emilySprite = 0
    $ charlotteSprite = 0

    image fbcharlotte defaultflip = im.Flip("charlotteblink", horizontal=True)
    image fbcharlotte defaultfliptalk = im.Flip("charlotteblinktalk", horizontal=True)
    image fbcharlotte stumpedfliptalk = im.Flip("Sprites/charlotte sprite blush.png", horizontal=True)
    image fbsophia apprehensiveflip = im.Flip("Sprites/sophia sprite angery1.png", horizontal=True)

    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    with Dissolve(0.5)

    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    with Dissolve(0.5)

    show fbolivia current:
        xalign 0.8 ypos 120
    with Dissolve(0.5)

    show fbmia current:
        xalign 0.65 ypos 120
    with Dissolve(0.5)

    show fbemily current:
        xalign 0.9 ypos 120
    with Dissolve(0.5)

    $ emilySprite = 3
    emily "OOH I’m just so excited!"
    $ emilySprite = 0
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    sophia "Our girl Ava is gonna wipe the floor with those chumps!!"
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 9
    mia "Ahhhh I can’t wait!"
    $ miaSprite = 0
    $ oliviaSprite = 9
    olivia "Yay."
    $ oliviaSprite = 8
    "Everyone" "...."
    show fbcharlotte stumpedfliptalk:
        xalign 0.4 ypos 120
    charlotte "Wow! I think that’s the most excited I’ve seen you in a month Olivia."
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ emilySprite = 5
    emily "And she's not even playing her Game-Man!"
    $ emilySprite = 0
    $ oliviaSprite = 13
    olivia "H-Hey c'mon I don't play it non stop! I can at least cheer for Ava properly!"
    $ oliviaSprite = 8
    show fbsophia apprehensiveflip:
        xalign 0.5 ypos 120
    sophia "Hmmm I don't know..."
    $ sophiaSprite = 0
    $ oliviaSprite = 4
    olivia "HEY!"
    $ oliviaSprite = 3
    "Everyone" "...."
    $ emilySprite = 3
    $ miaSprite = 1
    $ oliviaSprite = 14
    image fbcharlotte charlottehappyflip = im.Flip("Sprites/charlottehappytalk.png",horizontal=True)
    show fbcharlotte charlottehappyflip:
        xalign 0.4 ypos 120
    show fbsophia defaultfliptalk:
        xalign 0.5 ypos 120
    "Everyone" "Hahahaha!"

    $ emilySprite = 0
    $ sophiaSprite = 0
    $ playerSprite = 10
    $ miaSprite = 0
    $ oliviaSprite = 8
    $ emilySprite = 0
    $ charlotteSprite = 6

    show fbcharlotte current:
        xalign 0.3 ypos 120
    show fbsophia current:
        xalign 0.5 ypos 120

    show fbplayer current:
        xalign 0.2 ypos 120
    with Dissolve(0.7)
    player "Hey girls! I found the place."
    $ charlotteSprite = 0
    $ miaSprite = 5
    mia "[povname]!!! you made iiiit!"
    $ miaSprite = 0
    $ playerSprite = 13
    player "Haha yeah, I heard you guys hyping up Ava on my way over so I'm pretty hyped too!"
    $ playerSprite = 0
    $ sophiaSprite = 4
    sophia "Ava's gonna kick their FUCKING asses!"
    $ sophiaSprite = 3
    $ emilySprite = 1
    emily "Hahaha Sophia!"
    $ emilySprite = 0
    $ playerSprite = 13
    player "Hahahaha! Let's goooo!"
    $ playerSprite = 0

    $ avaSprite = 3
    image fbava runflip = im.Flip("Sprites/avanosweater.png", horizontal=True, vertical=False)
    image fbava runfliptalk = im.Flip("Sprites/avanosweatertalk.png", horizontal=True, vertical=False)


    show fbava runfliptalk:
        xalign 0 ypos 120
    with Dissolve(0.5)

    ava "Hey girls!"
    show fbplayer defaultflip:
        xalign 0.1 ypos 120
    ava "Oh! [povname] too, thanks for coming!"
    show fbava runflip:
        xalign 0 ypos 120
    $ emilySprite = 1
    emily "Ava!"
    $ emilySprite = 0
    show fbava runfliptalk:
        xalign 0 ypos 120
    ava "Saw you all in a group and I wanted to say hi before I head off to the prep area!"
    show fbava runflip:
        xalign 0 ypos 120
    $ charlotteSprite = 11
    charlotte "Give em hell girl!"
    $ charlotteSprite = 0
    $ miaSprite = 1
    mia "Gah I’m so happy we get to see you before you start!!"
    $ miaSprite = 0
    show fbava runfliptalk:
        xalign 0 ypos 120
    ava "Haha thanks Mia me too."
    show fbplayer fliptalk:
        xalign 0.1 ypos 120
    player "Good luck Ava, you're not gonna need it."
    show fbplayer defaultflip:
        xalign 0.1 ypos 120
    show fbava runfliptalk:
        xalign 0 ypos 120
    ava "I appreciate it [povname], was really nice of you to come..."
    show fbava runflip:
        xalign 0 ypos 120
    show fbplayer fliptalk:
        xalign 0.1 ypos 120
    player "Wouldn't miss it for anything."
    show fbplayer defaultflip:
        xalign 0.1 ypos 120
    $ sophiaSprite = 4
    sophia "She's got BEAUTY she's got GRACE she's gonna smash the record in the FACE!"
    $ sophiaSprite = 3
    $ charlotteSprite = 11
    charlotte "WOOOOO!"
    $ charlotteSprite = 0
    show fbava runfliptalk:
        xalign 0 ypos 120
    ava "Hahaha."
    ava "Well it was great to see you all before the race but I should head out now."
    $ miaSprite = 5
    mia "Beauty AND bronze! WOOOO!"
    $ miaSprite = 0
    $ emilySprite = 1
    emily "That's 'and brains' Mia."
    $ emilySprite = 0
    show fbava runfliptalk:
        xalign 0 ypos 120
    ava "Alright alright haha save it for the race I gotta go! Bye guys!"
    show fbava runflip:
        xalign 0 ypos 120

    $ oliviaSprite = 14
    $ sophiaSprite = 1
    $ charlotteSprite = 11
    $ emilySprite = 1
    $ miaSprite = 5
    show fbplayer fliptalk:
        xalign 0.1 ypos 120
    "Everyone" "Bye!!"
    scene fs blackblank
    with Dissolve(1.0)

    $ oliviaSprite = 0
    $ sophiaSprite = 0
    $ charlotteSprite = 0
    $ emilySprite = 0
    $ miaSprite = 0

    if sophiaphase1interaction2 == 2:
        $ sophiaquestlog = "Visit Sophia's house during Morning."

    if oliviaphase1interaction3 == 2:
        $ oliviaquestlog = "Meet Olivia at the arcade during Day."

    "The girls yell their final 'good lucks' to Ava as she walks away before heading to the bleachers."
    "The wind was howling when as they sat down, twas a breezy day"
    "You let the girls go first and sit down before heading up yourself"
    pause
    "The bright sunny day was charged with energy from the spectators and participants"
    scene fs crowdcheer1
    with Dissolve(0.7)
    "You spend the first hour watching and cheering for the girl's school teams"
    scene fs trackrace0
    with Dissolve(0.7)
    "Then finally Ava's race was next."
    "With bated breath you all watched her explode from the starting line"
    scene fs trackrace1
    with Dissolve(0.7)
    "And any worries you had were quickly quelled when she easily took first place position, and kept it"
    scene fs crowdcheer2
    with Dissolve(0.7)
    "Didn't take long before the finish line was in sight"
    scene fs trackrace2
    with Dissolve(0.7)
    "The other runners gained a little distance on her"
    scene fs trackrace3
    with Dissolve(0.7)
    "But not nearly enough to catch up, it was a clear victory"
    scene fs crowdcheer3
    with Dissolve(0.7)
    "You and your girlfriend's friends all cheered in elation."
    scene fs blackblank
    with Dissolve(1.0)
    player "{i}Well it's been an interesting 10 days. I've learned a lot about Mia and her friends.{/i}"
    player "{i}I don't have any plans this evening after the meet, who should I spend some time with?{/i}"
    menu:
        "Mia" if miaphase1interaction3 == 5:
            $ esch1_choice = "mia"
        "Charlotte" if charlottephase1interaction3 == 2:
            $ esch1_choice = "charlotte"
        "Sophia" if sophiaphase1interaction2 == 2:
            $ esch1_choice = "sophia"
        "Olivia" if oliviaphase1interaction3 == 2:
            $ esch1_choice = "olivia"
        "Emily" if emilyphase1interaction2 == 6 and moviecount == 0:
            $ esch1_choice = "emily"
        "Ava" if avaphase1interaction2 == 4:
            $ esch1_choice = "ava"
        "Nobody":
            $ esch1_choice = "nobody"
    if esch1_choice != "ava":
        "A little while later..."

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
        show fbplayer current:
            xalign 0.25 ypos 120
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
        show fbcharlotte charlottehappyflip:
            xalign 0.4 ypos 120
        charlotte "And I see Olivia is back on the Game-Man."
        show fbcharlotte defaultflip:
            xalign 0.4 ypos 120
        $ oliviaSprite = 1
        olivia "What? The races are over."
        $ oliviaSprite = 0
        $ playerSprite = 1
        player "Haha true."
        $ playerSprite = 0
        show fbava runflip:
            xalign 0.1 ypos 120
        with Dissolve(0.5)

        show fbjosy defaultflip:
            xalign -0.05 ypos 120
        with Dissolve(0.5)

        $ emilySprite = 1
        emily "Ahhh here's the girls of the hour!"
        $ emilySprite = 0

        show fbcharlotte current:
            xalign 0.32 ypos 120

        show fbsophia current:
            xalign 0.5 ypos 120

        show fbplayer defaultflip behind fbcharlotte:
            xalign 0.18 ypos 120

        show fbava runfliptalk:
            xalign 0.1 ypos 120
        ava "Haha hey!"
        show fbava runflip:
            xalign 0.1 ypos 120

        show fbjosy talkflip:
            xalign -0.05 ypos 120
        josy "Hey girls!"
        show fbjosy defaultflip:
            xalign -0.05 ypos 120

        $ miaSprite = 4
        mia "Josy! So nice to see you!"
        $ miaSprite = 0
        $ sophiaSprite = 1
        sophia "Yeah you did awesome!!"
        $ sophiaSprite = 0
        $ charlotteSprite = 11
        charlotte "Yeah you both did! First place each I can't believe it!"
        $ charlotteSprite = 0
        player "{i}This is really a great atmosphere huh?{/i}"
        show fbjosy talkflip:
            xalign -0.05 ypos 120
        josy "Thanks guys really, so nice of you to all show up and support us!"
        image fbjosy smileflip = im.Flip("Sprites/josy1080toothy.png", horizontal=True)
        show fbjosy smileflip:
            xalign -0.05 ypos 120

        josy "But is anyone going to tell me who this handsome slice of man is?"
        show fbjosy defaultflip:
            xalign -0.05 ypos 120

        show fbava runfliptalk:
            xalign 0.1 ypos 120
        ava "Oh shoot, [povname] you haven't met Josy yet have you?!"
        ava "Josy this is [povname], and [povname] this is my good friend and teammate Josy!"
        ava "She won the long jump today."
        show fbava runflip:
            xalign 0.1 ypos 120

        show fbplayer fliptalk behind fbcharlotte:
            xalign 0.18 ypos 120
        player "Wait so that was you who set the record today?!"
        show fbplayer defaultflip behind fbcharlotte:
            xalign 0.18 ypos 120

        show fbjosy talkflip:
            xalign -0.05 ypos 120
        josy "Yes sir!"
        show fbjosy defaultflip:
            xalign -0.05 ypos 120

        show fbplayer fliptalk behind fbcharlotte:
            xalign 0.18 ypos 120
        player "Damn girl I thought you were flying! Congrats once again."
        show fbplayer defaultflip behind fbcharlotte:
            xalign 0.18 ypos 120

        show fbjosy smileflip:
            xalign -0.05 ypos 120
        josy "Hehe thanks so much! I know a few ways you can congratulate me in private if you're interested?"
        show fbjosy defaultflip:
            xalign -0.05 ypos 120
        $ oliviaSprite = 8
        $ emilySprite = 2
        $ sophiaSprite = 7
        $ charlotteSprite = 6

        show fbplayer weaksmileflip:
            xalign 0.18 ypos 120

        "Everyone" "...."
        $ emilySprite = 4
        emily "Um...Mia? You want to speak up?"
        $ emilySprite = 0
        josy "?"
        show fbplayer fliptalk behind fbcharlotte:
            xalign 0.18 ypos 120
        player "Uh well I'd love to show you a good time but Mia and I are going out."
        show fbplayer defaultflip behind fbcharlotte:
            xalign 0.18 ypos 120

        $ miaSprite = 10
        mia "OH!"
        $ miaSprite = 4
        mia "Yes sorry [povname] and I are dating!"
        $ miaSprite = 0
        $ emilySprite = 0
        $ oliviaSprite = 0
        $ sophiaSprite = 0
        $ charlotteSprite = 0
        "Everyone" "Sigh..."
        show fbjosy smileflip:
            xalign -0.05 ypos 120
        josy "Ohhhh haha okay sorry sorry!"
        show fbjosy talkflip:
            xalign -0.05 ypos 120
        josy "Yeah I remember Katie telling me you're dating someone now."
        josy "So this is him? She also said you're getting the D on the regular."
        show fbjosy defaultflip:
            xalign -0.05 ypos 120
        $ miaSprite = 1
        mia "Oh yes [povname] gets in the mood quite a lot so he fucks me pretty often!"
        $ miaSprite = 4
        mia "The sex is really good!"
        $ miaSprite = 0
        show fbplayer weaksmileflip:
            xalign 0.18 ypos 120
        player "Um..."
        $ charlotteSprite = 1
        charlotte "I really want to leave this conversation right now."
        $ charlotteSprite = 0
        $ sophiaSprite = 2
        sophia "Yeah I don't know how much more I can take.."
        $ miaSprite = 10
        mia "Oh that...that was too much information again wasn't it..."
        $ playerSprite = 8
        show fbplayer current:
            xalign 0.25 ypos 120
        player "Maybe a bit babe yeah haha."
        show fbplayer defaultflip behind fbcharlotte:
            xalign 0.18 ypos 120

        show fbjosy smileflip:
            xalign -0.05 ypos 120
        josy "Hahaha well I definitely don't mind! But I do have to leave now though."
        show fbjosy talkflip:
            xalign -0.05 ypos 120
        josy "Is Katie still good for shopping tonight Mia?"
        show fbjosy defaultflip:
            xalign -0.05 ypos 120

        $ miaSprite = 1
        mia "Yes she said she'll be meeting you at the regular spot!"
        $ miaSprite = 0

        show fbjosy talkflip:
            xalign -0.05 ypos 120
        josy "Great, see you later girls! Thanks again!"
        josy "Oh and great meeting you [povname]."
        show fbjosy defaultflip:
            xalign -0.05 ypos 120

        show fbplayer fliptalk behind fbcharlotte:
            xalign 0.18 ypos 120
        player "You too Josy it was...interesting!"
        show fbplayer defaultflip behind fbcharlotte:
            xalign 0.18 ypos 120

        show fbjosy talkflip:
            xalign -0.05 ypos 120
        josy "Hehe."
        josy "See yah Ava."
        show fbjosy defaultflip:
            xalign -0.05 ypos 120

        $ avaSprite = 3
        show fbava current:
            xalign 0.05 ypos 120
        ava "Bye!"
        hide fbjosy defaultflip
        with Dissolve(0.5)
        pause
        hide fbplayer defaultflip
        hide fbava current

        show fbplayer current:
            xalign 0.0 ypos 120
        with Dissolve(0.3)

        show fbava current:
            xalign 0.15 ypos 120
        with Dissolve(0.3)
        ava "Welp. Sorry about that?"
        $ avaSprite = 2
        $ playerSprite = 1
        player "Haha I'm fine with it if Mia is. Babe are you upset at all?"
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Upset about what?"
        $ miaSprite = 0
        $ playerSprite = 1
        player "Looks like it's cool."
        $ playerSprite = 0
        $ charlotteSprite = 1
        charlotte "Figures she'd be close friends with Katie."
        $ charlotteSprite = 0
        $ emilySprite = 2
        emily "Charlotte!"
        $ emilySprite = 4
        show fbava runflip:
            xalign 0.25 ypos 120
        show fbcharlotte defaultfliptalk:
            xalign 0.4 ypos 120
        charlotte "What? I'm just saying they're both..."
        show fbcharlotte defaultflip:
            xalign 0.4 ypos 120
        $ emilySprite = 5
        emily "Still! It's not nice to be mean and talk behind someone's back."
        $ emilySprite = 4
        show fbava runfliptalk:
            xalign 0.25 ypos 120
        ava "No it's fine Em, she's a big time slut."
        $ emilySprite = 0
        show fbava runflip:
            xalign 0.25 ypos 120
        $ emilySprite = 5
        emily "Ehhh d-don't use that word..."
        $ emilySprite = 4
        show fbava runfliptalk:
            xalign 0.25 ypos 120
        ava "Relax I'm still friends with her!"
        ava "Just cause someone gobbles cock like a sword swallower doesn't mean they're a bad person."
        show fbava runflip:
            xalign 0.25 ypos 120
        $ playerSprite = 1
        player "Hahaha!"
        $ playerSprite = 0
        $ emilySprite = 4
        emily "Eeeh.."
        $ avaSprite = 3
        show fbava current:
            xalign 0.15 ypos 120
        ava "Anyways, [povname]. Just keep your wits about you when you're around her."
        $ avaSprite = 2
        player "{i}Hmmm interesting.{/i}"
        $ playerSprite = 1
        player "Sure thing."
        $ playerSprite = 0
        $ avaSprite = 3
        $ emilySprite = 0
        ava "Ugh I am exhausted, I gotta take a shower then head home."

    if esch1_choice == "mia":
        jump gohomemia
    elif esch1_choice == "charlotte":
        jump gohomecharlotte
    elif esch1_choice == "sophia":
        jump gohomesophia
    elif esch1_choice == "ava":
        jump esch1_ava
    elif esch1_choice == "emily":
        jump gohomeemily
    elif esch1_choice == "olivia":
        jump gohomeolivia
    elif esch1_choice == "nobody":
        jump esch1_check
    scene fs blackblank
    "Rgbcat" "broke script ahh"
    "Rgbcat" "If you see this, something of the mod didn't work. Please send me your save file on f95!"
    "Rgbcat" "Continuing on mia's chapter 1 ending..."
    jump gohomemia


label esch1_check:
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
    olivia "Sorry, no."
    $ oliviaSprite = 8
    $ playerSprite = 15
    player "No?"
    $ playerSprite = 14
    $ oliviaSprite = 9
    olivia "I ordered the new Kerokero Fight game and it comes in today."
    olivia "I'm headed home now to go play it."
    $ oliviaSprite = 8
    $ playerSprite = 15
    player "Oh that's...too bad."
    $ playerSprite = 14
    $ oliviaSprite = 9
    olivia "Yeah...you probably should've spent your time better."
    $ oliviaSprite = 8
    $ playerSprite = 11
    player "Huh?"
    $ playerSprite = 14
    $ oliviaSprite = 9
    olivia "Nothing bye. See you later."
    $ oliviaSprite = 8
    $ playerSprite = 8
    player "See yah..."
    hide fbolivia current
    with Dissolve(0.7)
    $ playerSprite = 7
    player "{i}Spent my time better huh?{/i}"

    $ endchapter1_trigger = "1 nobody"
    jump startofchapter2


# Chapter 2: introduction and office pickup

label continuegamechapter2:
    $ hiden_textbox = True
    "Sometime later the next day..."
    with Dissolve(1.0)
    scene fs tablenomcnomiaAva
    with Dissolve(0.7)
    ava "So turns out the guy was one of those sport recruiters."
    scene fs tablenomcnomiaEmily
    emily "Wow okay so you have a real shot then??"
    scene fs tablenomcnomiaAva
    ava "Yeah it seems so."
    scene fs tablenomcnomiaSophia
    sophia "That’s so awesome!"
    scene fs tablenomcnomiaOlivia
    olivia "Yeah good luck Ava."
    scene fs tablenomcnomiaCharlotte
    charlotte "Does anyone want anything else? I’m going to get another Coffee."
    scene fs tablenomcnomiaAva
    ava "Well I was gonna wait for Mia but she’s still not here yet."
    scene fs tablenomcnomiasophiahmmm
    with Dissolve(0.5)
    sophia "Yeah, [povname] was supposed to be coming too. I wonder where they are…"
    show miagroupchatfuck2 movie
    play sound "audio/miagameaudio/miadoggysex.wav" loop
    mia "Ahn! Ahn!"
    mia "Ohh!"
    hide miagroupchatfuck2 movie
    show miagroupchatfuck5 movie
    player "Fuck yes!"
    mia "We’re gonna be late!"
    player "You think I give a shit?"
    hide miagroupchatfuck5 movie
    show miagroupchatfuck1 movie
    with Dissolve(0.5)
    stop sound
    play sound "audio/miagameaudio/miapanting.wav"
    player "We’re not leaving until I fill your pretty little pussy."
    play sound "audio/miagameaudio/miammm.wav"
    mia "Uhn! Mmmm!!"
    hide miagroupchatfuck1 movie
    show miagroupchatfuck4 movie
    with Dissolve(0.5)
    player "You like it slow too don't you?"
    mia "Yeah..."
    player "You’re gonna talk, laugh, and hang out with your friends all while filled to the brim with my cum."
    mia "Mmmmm."
    player "Do you understand??!"
    voice "audio/miagameaudio/miayyes.wav"
    mia "Y-Yes!"
    hide miagroupchatfuck4 movie
    show miagroupchatfuck2 movie
    play sound "audio/miagameaudio/miadoggysex.wav" loop
    player "What was that??"
    mia "YES! AHN!"
    mia "AHHH!"
    hide miagroupchatfuck2 movie
    show miagroupchatfuck5 movie
    player "Fuck you’re so wet, you gonna cum baby?"
    mia "Uh huh!"
    player "Cum on my cock baby go ahead!"
    with vpunch
    stop sound
    voice "audio/miagameaudio/miabigyes.wav"
    mia "AAHHH! Yeeeeess!"
    player "That’s it, feels so fucking good."
    hide miagroupchatfuck5 movie
    show miagroupchatfuck3 movie
    play sound "audio/miagameaudio/miaorgasm2.wav"
    player "UGH!!!"
    mia "I can feel you cumming too!"
    player "How is it?"
    mia "So good [povname] you feel so good inside me!"
    window hide
    pause
    hide miagroupchatfuck3 movie

    scene fs livingroom
    with Dissolve(1.0)
    $ playerSprite = 0
    $ miaSprite = 1
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)

    show fbmia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    mia "Hah...hah..."
    if endchapter1_trigger == "1 mia neutral":
        $ playerSprite = 1
        player "You alright?"
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Yes I just need to catch my breath, my pussy also needs some time to recover haha."
        $ miaSprite = 0
        $ playerSprite = 1
        player "Fuck me I think I gave you everything I had."
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Hehe good! I don’t want your cum going anywhere else."
        $ miaSprite = 0
        $ playerSprite = 1
        player "How’s your neck? Was I too rough?"
        player "Remember I can hold back on things if you w-"
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Shhhh."
        mia "It’s fine. I want you to..Fuck me."
        mia "However you want to fuck me."
        mia "Soft and gentle, hard and rough."
        mia "It turns me on seeing you want me in different ways. So don’t worry about it!"
        mia "Even if, you know. It might take some getting used to at first."
        $ miaSprite = 0
        $ playerSprite = 1
        player "Mia.."
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Hehe."
        $ miaSprite = 0
        $ playerSprite = 1
        player "So what you’re saying is..Anal?"
        $ playerSprite = 0
        $ miaSprite = 1

        mia "!!!"
        show fbmia talkflip:
            xalign 0.6 ypos 120
        mia "WELL would you look a the time we should really get going huh??"
        $ miaSprite = 0
        $ playerSprite = 1
        show fbplayer current:
            xalign 0.5 ypos 120
        with move
        player "That sounds like you’re open to anal."
        $ playerSprite = 0
        $ miaSprite = 1
        show fbmia talkflip:
            xalign 0.7 ypos 120
        with move
        mia "Oh the girls are gonna be really mad at us when we get back!"

        show fbmia defaultflip:
            xalign 0.7 ypos 120
        $ playerSprite = 1
        player "Haha yeah probably."
        $ playerSprite = 13
        show fbplayer current:
            xalign 0.6 ypos 120
        with move
        player "Don’t think I’ll forget about anal though."
        $ playerSprite = 0

        show fbmia talkflip:
            xalign 1.2 ypos 120
        with move
        mia "Such a bright, sunny day today!"
        hide fbmia defaultflip
        $ miaSprite = 0
        $ playerSprite = 11

        show fbplayer current:
            xalign 1.4 ypos 120
        with move
        player "Hey wait up!"
        hide fbplayer current
        with Dissolve(0.5)
        scene fs blackblank
        with Dissolve(0.7)
    else:
        $ playerSprite = 1
        player "You alright?"
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Yes I just need to catch my breath, my pussy also needs some time to recover haha."
        $ miaSprite = 0
        $ playerSprite = 1
        player "Think you can handle the car?"
        $ playerSprite = 0
        $ miaSprite = 1
        mia "Hah...Yeah I should be fine. Geez [povname] that was really good..."
        $ miaSprite = 0
        $ playerSprite = 1
        player "Heh glad to know we're on the same page. So have you given any thought to anal yet?"
        $ playerSprite = 0
        $ miaSprite = 1
        show fbmia talkflip:
            xalign 0.7 ypos 120
        with move
        mia "WELL I GUESS WE SHOULD GO NOW THEN!"
        $ miaSprite = 0
        hide fbmia talkflip
        with Dissolve(0.5)
        $ playerSprite = 1
        player "Hahaha wait up!"
        hide fbplayer current
        with Dissolve(0.5)
        scene fs blackblank
        with Dissolve(0.7)


    "A little while later..."
    scene fs tableMiacharlottecoffee
    with Dissolve(1.0)
    mia "Hey girls!"
    scene fs tableCharlottecoffeetalk
    charlotte "Hey!"
    scene fs tablesophiasurprisecharlottecoffee
    sophia "What took you?"
    scene fs tablemclookleftcharlottecoffee
    player "Yeah sorry we're late we got held up."
    player "Uh...doing stuff."
    scene fs tablesophiasadcharlottecoffee
    sophia "...."
    scene fs tableEmilycharlottecoffee
    emily "No problem, we don't mind but Charlotte's just had her 2nd cup of coffee so shes gonna be hopped up on caffeine all day."
    scene fs tableCharlottecoffeetalk
    charlotte "I told you i c-can handle i-it!"
    scene fs tableAvacharlottecoffee
    ava "But the rest of us are fine haha."
    scene fs tableMiacharlottecoffee
    mia "Great!"
    mia "So any updates? Can we all go?"
    scene fs tableCharlottecoffeetalk
    charlotte "Is anybody else like super hot?"
    scene fs tableEmilycharlottecoffee
    emily "Yes! We all have open schedules!"
    scene fs tableCharlottecoffeetalk
    charlotte "I feel like going for a run, Ava you wanna race?"
    scene fs tablemclookleftcharlottecoffee
    player "What's going on?"
    scene fs tableMiacharlottecoffee
    mia "We're all going to the beach!"
    scene fs tableMCcharlottecoffee
    player "Woah! Nice, when??"
    scene fs tablesophiasurprisecharlottecoffee
    sophia "In two weeks!"
    scene fs tableEmilycharlottecoffee
    emily "Ten days to be precise."
    scene fs tableCharlottecoffeepoint
    charlotte "How about you Olivia? I bet I can kick your ass in a race, your stupid boobs would slow you down."
    scene fs tableCharlottecoffeepointheh
    olivia "Heh."
    scene fs tableMiacharlottecoffee
    mia "Would you like to join us?"
    scene fs tablesophiasurprisecharlottecoffee
    sophia "Oh you gotta go!"
    scene fs tableMCcharlottecoffee
    player "Beach day with my girlfriend and her friends?"
    player "Uh yeah I think I can make some room in my schedule for that. Now are we all wearing bikinis cause I don't want to show up with the same outfit as one of you guys. SO embarrassing."
    scene fs tableMiacharlottecoffee
    mia "Omg stop it haha!"
    mia "Speaking of bikinis, I need to go shopping!"
    mia "[povname] will you go with me?"
    scene fs tableMCcharlottecoffee
    player "Ugh shopping...."
    player "But bikinis..."
    scene fs tableMiacharlottecoffee
    mia "I'll let you look at my choices!"
    scene fs tableAvacharlottecoffee
    ava "That's a pretty good offer [povname]! You really turning down seeing this bombshell do a bikini montage?"
    scene fs tableMCcharlottecoffee
    player "Alright alright I'll think about it!"
    scene fs tableMiacharlottecoffee
    mia "What about you guys?"
    mia "Anyone else need to go shopping for the beach?"
    scene fs tableEmilycharlottecoffee
    emily "Hmmm maybe, I think I'm doing something but there may still be time."
    scene fs tableCharlottecoffeetalk
    charlotte "I can go I just got some errands to run first."
    scene fs tablesophiasurprisecharlottecoffee
    sophia "Same actually..."
    sophia "{i}I really want to run interference between [povname] and Mia! UGH!{/i}"
    scene fs tableEmilycharlottecoffee
    emily "Alright how about when you two are ready to go just come find us or give us a call to see if we're ready?"
    scene fs tableMiacharlottecoffee
    mia "Sounds good to me, [povname]?"
    scene fs tableMCcharlottecoffee
    player "Yeah that's great."
    scene fs blackblank
    with Dissolve(1.0)
    "The girls and you talk about nonsense, you can only handle an hour before heading home to take a nap"
    scene fs livingroom
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)

    player "Man girls can just talk for hours about nothing geez."
    $ playerSprite = 0
    player "I think getting up early for morning sex with Mia has caught up with me, I need a power nap."
    scene fs blackblank
    with Dissolve(1.0)
    pause
    play sound "audio/phonevibration.wav"
    "Vvvvvvp Vvvvp!"
    player "Hmm? Wonder who's calling me."
    scene fs playerroomMorn
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 2
    player "Hello?"
    mia "Hey [povname]!"
    player "Oh hey babe what's up?"
    mia "Can you do me a big favor?"
    player "Yeah of course, what is it?"
    mia "I'm still in Sunnyside but Katie walked here from our place."
    player "Sunnyside?"
    mia "Yeah, you know the area where the café is?"
    player "Oh, yeah of course."
    mia "Yeah we met up to see our mom but turns out she's not at work and we kinda don't feel like walking or bussing back home."
    katie "My feet are tiiiiired!!"
    mia "Katie don't yell!"
    mia "Sorry, so yeah can you pick us up? If it's not too much trouble."
    player "It's no trouble at all babe I'll be there in twenty minutes."
    mia "Thank youuu!!! We're at the big office building next to the café."
    katie "Yaaayyy~"
    mia "Katie! What did i just tell you??"
    player "Welp. Looks like I'm heading out."
    player "I better head over to Sunnyside."
    scene fs blackblank
    with Dissolve(1.0)
    "You can now head to the town over by clicking the arrow in the bottom right of the map!"
    $ headtosunnyside = 1
    jump overworldmap


label meetMiaAndKatieAtOffice:
    hide screen uppergui
    "You make the quick drive back towards the café and quickly spot the big office building"
    "You park your car in the parking lot and walk around to the front"
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.7)
    player "Okay they should be around here some-"
    show fbmia current:
        xalign 0.55 ypos 120
    with Dissolve(0.5)
    $ katieSprite = 6
    show fbkatie current:
        xalign 0.65 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Ah there they are!"
    player "Hey Mia."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "[povname] you're here!"
    $ miaSprite = 0
    $ katieSprite = 5
    show fbkatie dressarmsup:
        xalign 0.65 ypos 120
    katie "OHMYGODTHANKYOUUUU."
    $ playerSprite = 1
    $ katieSprite = 6
    player "Haha Happy to help. Nice outfit by the way, you look really cute."
    $ playerSprite = 0
    show fbkatie current:
        xalign 0.65 ypos 120
    katie "{i}Hehe yeah I bet you think that don't you?{/i}"
    $ katieSprite = 7
    katie "Thanks, it was hot today so I figured I'd wear it!"
    $ playerSprite = 1
    $ katieSprite = 6
    player "How's your feet?"
    $ playerSprite = 0
    show fbkatie dresshipswhine:
        xalign 0.65 ypos 120
    katie "Ugh. Something's wrong with me for walking that far."
    $ miaSprite = 1
    $ katieSprite = 6
    mia "I told you to take the bus!"
    $ miaSprite = 0
    $ katieSprite = 7
    katie "Josy does it all the time and she jogs here!"
    katie "I figured hey why not get some exercise, it's a nice day!"
    $ playerSprite = 1
    $ katieSprite = 4
    player "Haha big mistake."
    $ playerSprite = 0
    $ katieSprite = 5
    katie "Ugh. I know that now."
    $ playerSprite = 1
    $ katieSprite = 4
    player "Well I'm here to rescue the both of yah."
    $ playerSprite = 0
    $ katieSprite = 7
    show fbkatie current:
        xalign 0.65 ypos 120
    katie "My Hero!"
    $ miaSprite = 1
    $ katieSprite = 6
    mia "Ummm pretty sure he's MY hero."
    $ miaSprite = 0
    $ katieSprite = 7
    katie "Hehe he can be both!"
    $ miaSprite = 1
    $ katieSprite = 6
    mia "Sorry, girlfriend has exclusivity rights."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Ummm so, your guy's mom works here?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Yeah she's the CEO of Inuen Co."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Wait isn't that a huge conglomerate??!"
    player "I thought she was a stay at home mom to be honest, she just gave off that vibe."
    $ playerSprite = 0
    $ katieSprite = 7
    katie "Yeah we get that a lot. When she's working though it's like she's an entirely different person!"
    $ katieSprite = 6
    $ miaSprite = 1
    mia "She's super strict and mean! Thankfully we don't see her like that often though."
    $ miaSprite = 0
    $ katieSprite = 7
    katie "Since she has such a high position she doesn't do much actual work nowadays."
    katie "Only comes to the office to say 'yes' or 'no' to stuff before the decisions are finalized."
    $ playerSprite = 1
    $ katieSprite = 6
    player "Huh you seem quite knowledgeable about it Katie."
    $ playerSprite = 0
    $ katieSprite = 7
    katie "Well one day I'm gonna take over! So I better know what to do once I'm in charge!"
    $ playerSprite = 1
    $ katieSprite = 6
    player "Haha impressive! And what about you babe? You're not studying business at school right?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Nope! I don't have any interest in taking over I wanna do my own thing! But I'm very confident that Katie has what it takes!"
    mia "Mom's company is in good hands!"
    $ miaSprite = 0
    $ katieSprite = 7
    katie "Aww sis!"
    $ miaSprite = 1
    $ katieSprite = 6
    mia "Hehe."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Cute. Alright shall we hit the road?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Let's go!"
    $ miaSprite = 0
    show fbkatie dressarmsup:
        xalign 0.65 ypos 120
    katie "Woooo!"
    $ playerSprite = 1
    player "Hahaha."
    $ playerSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    "The three of you get in your car and you drive them back home."
    scene fs gfhouse
    with Dissolve(0.5)
    $ katieSprite = 7
    show fbmia current:
        xalign 0.65 ypos 120
    show fbkatie current:
        xalign 0.75 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    katie "Finally home!"
    $ katieSprite = 6
    $ juliaSprite = 5
    show fbjulia current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    julia "Welcome home girls."
    $ juliaSprite = 3
    julia "Oh [povname]!"
    julia "How nice to see you!"
    $ juliaSprite = 0
    $ playerSprite = 11
    show fbplayer current:
        xalign 0.38 ypos 120
    with move
    player "{i}Woah she's close!{/i}"
    player "{i}God it's so hard not staring at her huge fucking tits!{/i}"
    $ katieSprite = 7
    show fbkatie current at surpriseshake:
        xalign 0.75 ypos 120
    katie "Moooom where were you??"
    $ katieSprite = 6
    $ juliaSprite = 5
    $ playerSprite = 0
    julia "Huh?"
    $ juliaSprite = 4
    $ miaSprite = 1
    mia "We went to your office because we thought you were working, Katie walked from school."
    $ miaSprite = 0
    $ juliaSprite = 5
    julia "Oh dear I'm so sorry no I didn't need to go into work today. Why didn't you call me?"
    $ juliaSprite = 4
    $ katieSprite = 7
    katie "We didn't bother because we assumed you were there, you're always working at this time."
    $ katieSprite = 6
    $ juliaSprite = 5
    show fbjulia current:
        xalign 0.51 ypos 120
    with move
    julia "No not today. Oh sweetie I'm so sorry, your feet must be killing you after walking there and back."
    $ juliaSprite = 4
    $ miaSprite = 1
    mia "Actually [povname] came and drove us back after I called him for help."
    $ miaSprite = 0
    $ juliaSprite = 3
    julia "What?? You helped out both my girls?"
    $ juliaSprite = 0
    $ playerSprite = 6
    player "It was no big deal Julia I was happy to do it."
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Well you really are quite the gentleman aren't you. I can't thank you enough."
    $ juliaSprite = 0
    $ katieSprite = 7
    katie "Yeah thanks again!"
    $ katieSprite = 6
    $ miaSprite = 4
    mia "Hehe you're the best!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Girls c'mon I'm getting embarrassed haha."
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Well you're welcome here anytime you like."
    $ juliaSprite = 0
    $ playerSprite = 1
    player "Thanks."
    $ playerSprite = 11
    $ juliaSprite = 3
    julia "ANY. Time."
    $ juliaSprite = 0
    $ playerSprite = 1
    player "O-Okay."
    $ playerSprite = 0
    $ katieSprite = 7
    katie "Alright I'm headed to my room to rest. My dogs are fucking."
    $ katieSprite = 6
    $ juliaSprite = 5
    show fbjulia current at surpriseshake:
        xalign 0.51 ypos 120
    julia "Katie!"
    $ juliaSprite = 4
    $ katieSprite = 7
    katie "What??"
    $ katieSprite = 6
    $ juliaSprite = 5
    julia "It's 'barking'."
    $ juliaSprite = 4
    $ katieSprite = 7
    katie "Ohhh..."
    $ katieSprite = 6
    if katieconversation == 4:
        $ katieSprite = 7
        katie "Well, toodles!"
        $ katieSprite = 6
        show fbkatie current:
            xalign 0.25 ypos 120
        with move
        katie "*whisper* Psss hey [povname]. Come sneak into my room when you get the chance."
        show fbplayer frownflip:
            xalign 0.35 ypos 120
        player "Uh, I don't know about that Katie I-"
        show fbkatie katiefliptalk:
            xalign 0.25 ypos 120
        katie "Relax, I'm just gonna blindfold you, tie you down and fuck your brains out."
        show fbkatie katieflip:
            xalign 0.25 ypos 120
        show fbplayer surpriseflip:
            xalign 0.35 ypos 120
        player "!!!"
        show fbkatie katiefliptalk:
            xalign 0.25 ypos 120
        katie "Hahaha!"
        show fbkatie katieflip:
            xalign 0.25 ypos 120
        mia "?"
    hide fbkatie current
    with Dissolve(0.5)
    hide fbkatie katieflip
    with Dissolve(0.5)
    show fbplayer current:
        xalign 0.38 ypos 120
    $ juliaSprite = 5
    julia "Well I better head back to the kitchen, I want to get the oven ready for dinner before I finish the book I'm reading."
    $ juliaSprite = 4
    $ miaSprite = 1
    mia "Sure thing mom, I'm going to head upstairs as well actually."
    mia "Thanks again [povname]."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Anytime babe."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Come talk to me in my room when you have the chance."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Sure thing."
    $ playerSprite = 0
    hide fbmia current
    with Dissolve(0.5)
    $ juliaSprite = 0
    julia "...."
    $ playerSprite = 11
    player "?"
    $ juliaSprite = 3
    julia "Don't think I didn't notice you staring at my chest young man."
    $ juliaSprite = 0
    $ playerSprite = 16
    player "I...w-what?"
    $ playerSprite = 8
    $ juliaSprite = 3
    julia "Your eyes."
    $ juliaSprite = 11
    show fbjulia current:
        xalign 0.52 ypos 120
    $ playerSprite = 11
    julia "They were GLUED to my breasts."
    $ juliaSprite = 11
    $ playerSprite = 15
    player "Shit Julia I'm sorry I don't have an excuse th...they're just incredible."
    $ playerSprite = 14
    $ juliaSprite = 3
    if juliachecker == 1 or juliachecker == 2:
        julia "Hehe why so embarrassed? After what you did to them in the kitchen the other day I thought you wouldn't care."
        $ juliaSprite = 0
        $ playerSprite = 11
        player "Eh...I uh.."
        player "{i}That's true, but it was kinda happenstance combined with me being too horny.{/i}"
        $ juliaSprite = 3
        julia "I may not have minded but you shouldn't do it in front of my daughters."
        $ juliaSprite = 0
        $ playerSprite = 16
        player "You..don't mind?"

    $ juliaSprite = 3
    $ playerSprite = 8
    julia "Heh. I'll let you off the hook this time because you drove them home and Mia can't stop talking about how great you are."
    $ playerSprite = 0
    $ juliaSprite = 6
    julia "Clearly you're doing something right."
    $ juliaSprite = 0
    $ playerSprite = 1
    player "Uh thank you ma'am."
    $ playerSprite = 0
    $ juliaSprite = 3
    julia "Julia."
    $ juliaSprite = 0
    $ playerSprite = 1
    player "Julia. I'll get out of your hair and keep that in mind."
    $ playerSprite = 8
    $ juliaSprite = 2
    julia "Oh don't worry I still want to talk to you, we should get together again soon for another chat."
    $ juliaSprite = 0
    $ playerSprite = 16
    player "Sure uh..yeah okay."
    $ playerSprite = 0
    hide fbjulia current
    with Dissolve(0.5)

    $ miaphase2interaction1 = 1
    $ katiephase2interaction1 = 1
    $ juliaphase2interaction1 = 1
    $ headtosunnyside = 2


    if endchapter1_trigger != "1 mia neutral":
        jump overworldmap
    else:
        jump gfhouse


# Chapter 2 ending: beach trip

label phase2ending:
    scene fs blackblank
    hide screen uppergui
    hide screen backbuttonROOM
    "Beach day has arrived."
    scene fs playerroomMorn
    with Dissolve(1.0)
    show fbplayer current:
        xalign 0.5 ypos 120

    player "*Yawn*."
    player "I gotta go pick up Mia now so we can head out early!"
    scene fs blackblank
    with Dissolve(0.7)
    "After you arrive at Mia's place you find out everyone is already there"
    scene fs carscene1
    with Dissolve(1.0)
    pause
    scene fs carscene3
    player "You all look great!"
    player "I'll have to change when we get there."
    scene fs carscene2
    mia "Sorry I forgot to tell you!"
    mia "But at least we're already changed and will save some time there and back."
    scene fs carscene3
    player "True."
    scene fs carscene4
    charlotte "I still am not happy with this arrangment."
    scene fs carscene5
    emily "Oh c'mon it's not that bad, there wasn't enough room."
    emily "and it's kinda fun, it feels like my little sister is sitting on my lap!"
    scene fs carscene4
    charlotte "You're not the little sister in this situation."
    scene fs carscene3
    player "At least you're not in the back like Sophia."
    scene fs carscene6
    mia "You doing okay back there Soph?"
    pause
    scene fs carscene7
    sophia "Y-Yeah!"
    sophia "Never better!"
    scene fs blackblank
    with Dissolve(0.7)
    "It didn't take too much longer before you all arrived at your destination..."
    scene fs beach
    "The beach!"
    play music "audio/justbeach.mp3" fadein 5
    $ charlotteSprite = 15
    $ avaSprite = 22
    $ sophiaSprite = 11
    $ oliviaSprite = 15
    $ emilySprite = 6

    if swimsuitchoice == "white":
        show fbmia swimsuit1happytalk:
            xalign 0.5 ypos 120
    elif swimsuitchoice == "purple":
        show fbmia swimsuit2happytalk:
            xalign 0.5 ypos 120
    else:
        show fbmia swimsuit3happytalk:
            xalign 0.5 ypos 120


    mia "Woohoo!"


    show fbcharlotte current:
        xalign 0.6 ypos 120

    charlotte "Finally."
    $ charlotteSprite = 14
    $ avaSprite = 23
    show fbava current behind fbmia:
        xalign 0.4 ypos 120

    ava "Let's have some fun!"
    $ avaSprite = 22
    show fbsophia current:
        xalign 0.7 ypos 120
    sophia "UMIIII!"
    $ sophiaSprite = 12
    $ oliviaSprite = 17
    show fbolivia current:
        xalign 0.85 ypos 120
    olivia "Yay~"
    $ oliviaSprite = 15
    $ emilySprite = 8
    show fbemily current:
        xalign 0.3 ypos 120
    emily "I'm so excited! Let's go girls!"
    $ emilySprite = 6
    show fbplayer current:
        xalign 0.2 ypos 120
    $ playerSprite = 1
    player "I'll get changed real quick then meet up with you guys!"
    $ playerSprite = 0
    $ emilySprite = 8
    emily "Sounds great!"
    $ emilySprite = 6
    scene fs volleyball1
    with Dissolve(1.0)
    "It was early in the day but the whole group was excited and energetic"
    scene fs volleyball2
    with Dissolve(0.5)
    ava "Ava made sure everyone played some volleyball first"

    if swimsuitchoice == "white":
        scene fs volleyball3a
    elif swimsuitchoice == "purple":
        scene fs volleyball3b
    else:
        scene fs volleyball3c
    pause
    if swimsuitchoice == "white":
        scene fs volleyball4a
    elif swimsuitchoice == "purple":
        scene fs volleyball4b
    else:
        scene fs volleyball4c
    voice "audio/miagameaudio/miaah2.wav"
    mia "Ouch!"
    ava "Sorry!"
    scene fs volleyball5
    with Dissolve(0.7)
    "It was a great time"
    "Well at least I certainly enjoyed it"
    scene fs volleyball6
    with Dissolve(0.5)
    player "Hup!"
    scene fs volleyball7
    with Dissolve(0.7)
    voice "audio/sophiagameaudio/sophiaAhh.wav"
    sophia "Ahh!"
    play sound "audio/whistleaudio.ogg"
    charlotte "*Whistles*"
    if swimsuitchoice == "white":
        scene fs volleyball8a
    elif swimsuitchoice == "purple":
        scene fs volleyball8b
    else:
        scene fs volleyball8c
    with Dissolve(1.0)
    "After volleyball the group split up to have fun doing whatever"
    if swimsuitchoice == "white":
        scene fs volleyball9a
    elif swimsuitchoice == "purple":
        scene fs volleyball9b
    else:
        scene fs volleyball9c
    "It was exactly what everyone needed after the stress of school and everything else"
    if swimsuitchoice == "white":
        scene fs volleyball10a
    elif swimsuitchoice == "purple":
        scene fs volleyball10b
    else:
        scene fs volleyball10c
    pause
    "And seeing everyone in their bikinis I mean c'mon"
    if swimsuitchoice == "white":
        scene fs volleyball11a
    elif swimsuitchoice == "purple":
        scene fs volleyball11b
    else:
        scene fs volleyball11c
    with Dissolve(0.7)
    "It was great"
    scene fs blackblank
    with Dissolve(1.0)
    emily "Alright everyone! Gather for a picture!"
    charlotte "Do I have to?"
    olivia "Can I finish my ice cream first?"
    sophia "No who cares? Get over here!"
    mia "Hehe."
    scene fs beachpicture
    with Dissolve(1.0)
    emily "Smile everyone!"
    pause
    play sound "audio/camerasnap.mp3"
    with flash
    pause
    jump explorebeach


# Chapter 3: introduction

label continuegamechapter3:
    $ hidden_textbox = True
    stop music
    stop sound
    "After a great time at the beach you have a very well earned rest back at home"
    "The next day..."
    with Dissolve(1.0)
    scene fs carblowjob1
    player "Hmm hm hmmm."
    mia "Guhk!"
    player "Hmhm hmm."
    pause
    "Car Speaker" "*Riiiiing*"
    scene fs carblowjob3
    pause
    scene fs carblowjob4
    player "Heeeello."
    scene fs carblowjob1
    sophia "[povname]!"
    scene fs carblowjob1b
    player "Hey Soph what's up? I'm uh..."
    scene fs carblowjob1
    player "...."
    scene fs carblowjob1b
    player "On the way to pick up Mia then head over, shouldn't be long now."
    scene fs carblowjob1
    sophia "Oh okay great! That's actually why I'm calling."
    sophia "Me and the girls were talking at the café and we were like 'Oh my God it's so nice out!'"
    sophia "And Ava was like well let's go for a walk and Charlotte was like but what about Mia and I was like but what about [povname]?"
    scene fs carblowjob5
    player "Mmhm?"
    sophia "Right? So then Ava was all 'We can just meet them outside we don't have to be in the café every single time there's a new chapter'."
    sophia "Then there was all this back and forth about should we go outside or shouldn't we."
    sophia "We all knew Ava just wanted to walk outside cause she's a nut about fitness and always trying to get us to do something."
    sophia "But then it's still not that big a deal to just meet you guys outside."
    scene fs carblowjob5b
    player "Oh shit that's...yup."
    scene fs carblowjob5
    sophia "So everyone just kept going over the same points over and over again."
    sophia "Until Emily finally calmed everyone down and made everyone feel silly about the argument in the first place."
    sophia "So long story short come meet us outside the office building in Sunnyside."
    scene fs carblowjob7
    player "F-Fuck okay that's good."
    sophia "Uh...yeah I guess it is, you alright?"
    player "Yeah! I'll see you there. Bye!"
    sophia "Bye!"
    player "Ugh..."
    scene fs carblowjob6
    with vpunch
    player "Ahhhhh fuck!"
    player "That feels so good holy shit."
    scene fs carblowjob8
    mia "*Gulp* Ahhh.."
    scene fs carblowjob10
    mia "How was that?"
    scene fs carblowjob10b
    player "Insane how good you've gotten baby. Please don't start charging me I'll go broke."
    scene fs carblowjob10
    mia "Haha you're lucky I love sucking your big dick as much you like my blowjobs!"
    scene fs carblowjob10b
    player "Very lucky, I'm aware."
    scene fs carblowjob9
    mia "By the way have you been eating like crazy fruits or something lately because you keep cumming so much and somehow it seems way tastier?"
    sophia "Um guys..."
    sophia "You never hung up."
    pause
    scene fs carblowjob11
    "*Smack*"
    mia "Is...is it just you?"
    emily "She's been on speaker this whole time."
    player "...."
    mia "Um..."
    mia "We'll be there soon."
    sophia "O-Okay..."
    $ headtooffice = 1
    jump overworldmap


label continuechapter3intro:
    hide screen uppergui
    $ avaSprite = 4
    $ charlotteSprite = 5
    $ emilySprite = 9
    $ sophiaSprite = 9
    $ oliviaSprite = 18
    $ miaSprite = 2
    $ playerSprite = 8
    pause
    show fbava current:
        xalign 0.55 ypos 120
    show fbcharlotte current:
        xalign 0.7 ypos 120
    show fbsophia current:
        xalign 0.45 ypos 120
    show fbolivia current:
        xalign 0.3 ypos 120
    show fbemily current:
        xalign 0.85 ypos 120
    with Dissolve(0.7)
    pause
    show fbmia current:
        xalign 0.2 xzoom -1.0 ypos 120
    show fbplayer current:
        xalign 0.05 ypos 120
    with Dissolve(0.5)

    mia "..."
    $ miaSprite = 3
    mia "Hi girls."
    $ miaSprite = 2
    $ emilySprite = 3
    emily "H-Hey Mia.."
    $ emilySprite = 4
    $ miaSprite = 3
    mia "Sorry...I keep messing up huh?"
    $ miaSprite = 2
    $ avaSprite = 1
    ava "Babe no one is mad at you don't worry! Just made us all blush a bit haha."
    $ avaSprite = 0
    $ miaSprite = 3
    mia "Just another classic dumb Mia the pervert mistake."
    $ miaSprite = 2
    $ oliviaSprite = 10
    olivia "Don't be silly, you're dating, we get it. It's fine."
    $ charlotteSprite = 5
    charlotte "{size=25}Kinda impossible not to get it...{/size}"
    $ emilySprite = 5
    emily "Mia it's fine, like Ava said it just turned us on a little bit."
    $ emilySprite = 4
    $ avaSprite = 15
    show fbava current:
        xalign 0.63 xzoom -1.0
    pause
    ava "{i}Dats not what I said.{/i}"
    show fbava current:
        xalign 0.55 xzoom 1.0
    $ avaSprite = 0
    $ emilySprite = 1
    emily "We don't care, RIGHT Charlotte?"
    $ emilySprite = 0
    $ charlotteSprite = 6
    show fbcharlotte current:
        xalign 0.75 xzoom -1.0
    charlotte "Huh? I uh..."
    $ charlotteSprite = 13
    show fbcharlotte current:
        xalign 0.7 xzoom 1.0
    charlotte "*Ahem* Yes it's fine Mia, don't worry about it."
    $ charlotteSprite = 1
    charlotte "I mainly blame [povname] anyways."
    $ charlotteSprite = 0
    $ playerSprite = 11
    show fbmia current:
        xzoom 1.0
    player "...."
    $ playerSprite = 10
    player "As a man. Road head by law must be accepted."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Pffft!"
    $ avaSprite = 0
    $ oliviaSprite = 14
    olivia "Hehehe!"
    $ oliviaSprite = 10
    $ miaSprite = 4
    mia "Hehe. Not helping!"
    $ miaSprite = 0
    $ sophiaSprite = 8
    sophia "I'm just straight up jealous."
    $ sophiaSprite = 9
    $ miaSprite = 2
    $ avaSprite = 15
    $ emilySprite = 4
    show fbolivia current:
        xzoom -1.0
    show fbmia current:
        xzoom -1.0
    "Everyone" "....."
    $ sophiaSprite = 7
    sophia "Straight up."
    $ sophiaSprite = 9
    pause
    $ avaSprite = 16
    ava "What's wrong with you?"
    $ avaSprite = 15
    $ oliviaSprite = 4
    olivia "Keep that to yourself."
    $ oliviaSprite = 3
    $ emilySprite = 1
    show fbemily current at surpriseshake:
        xalign 0.85 ypos 120
    emily "OKAY!"
    $ avaSprite = 0
    $ sophiaSprite = 0
    $ oliviaSprite = 8
    show fbava current:
        xalign 0.63 xzoom -1.0
    show fbsophia current:
        xzoom -1.0
    show fbcharlotte current:
        xalign 0.75 xzoom -1.0
    emily "Well, enough of that."
    emily "Let's get to the reason we're here!"
    $ emilySprite = 0
    emily "Ummmm."
    $ emilySprite = 1
    emily "Oh Charlotte! Plans?"
    $ emilySprite = 0
    $ charlotteSprite = 8
    charlotte "Right!"
    $ charlotteSprite = 6
    show fbcharlotte current:
        xalign 0.7 xzoom 1.0
    charlotte "So everything's pretty much ready. Vicky's gonna pick up the beer today."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Oh, beer?"
    $ playerSprite = 0
    $ emilySprite = 1
    emily "For the sleepover!"
    $ emilySprite = 0
    $ playerSprite = 1
    player "Oh yeah!"
    $ playerSprite = 0
    $ miaSprite = 1
    show fbmia current:
        xzoom 1.0
    mia "It's in three days."
    $ miaSprite = 0
    $ sophiaSprite = 1
    show fbsophia current:
        xzoom 1.0
    sophia "It's gonna be SO much fun!"
    $ sophiaSprite = 0
    $ oliviaSprite = 9
    olivia "It's been a while since we last did one."
    $ oliviaSprite = 8
    $ charlotteSprite = 11
    charlotte "I'm pretty excited I can't lie."
    $ charlotteSprite = 0
    $ miaSprite = 1
    show fbmia current:
        xzoom -1.0
    mia "Oh oh! Can [povname] come?"
    $ miaSprite = 0
    $ sophiaSprite = 1
    show fbsophia current:
        xzoom -1.0
    sophia "Ohpleaseohpleaseohplease Charlotte can [povname] join us??"
    $ sophiaSprite = 0
    $ charlotteSprite = 8
    charlotte "Huh? B-But..."
    $ avaSprite = 1
    ava "He's pretty much part of the group now."
    $ avaSprite = 0
    charlotte "But he's a guy..."
    $ sophiaSprite = 4
    sophia "That's racial discrimination!!"
    $ sophiaSprite = 3
    $ charlotteSprite = 1
    charlotte "No it's not Sophia."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Haha, Charlotte ignore all of them."
    $ charlotteSprite = 6
    player "I'd love to join, only if YOU are cool with it."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "Uggggh."
    "Everyone" "....."
    $ charlotteSprite = 8
    charlotte "Well I have to let you after that.."
    $ charlotteSprite = 0
    $ miaSprite = 9
    mia "Yay!!"
    $ sophiaSprite = 1
    sophia "Wooooo!"
    $ sophiaSprite = 0
    $ avaSprite = 1
    show fbava current at surpriseshake:
        xalign 0.55 xzoom 1.0 ypos 120
    ava "We got some SAUSAGE at dis parteehhh."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Heh."
    $ playerSprite = 0
    $ emilySprite = 1
    emily "Hahaha okay Ava take it easy!"
    show fbcharlotte current:
        xzoom -1.0 xalign 0.75
    emily "Thank you Charlotte that's very kind of you to let him join us at your house."
    $ emilySprite = 0
    $ charlotteSprite = 3
    show fbcharlotte current:
        xzoom 1.0 xalign 0.7
    charlotte "There'll be some rules though!"
    $ charlotteSprite = 2
    $ playerSprite = 10
    player "No problem."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I'll be the perfect gentleman."
    $ playerSprite = 0
    $ miaSprite = 0
    $ oliviaSprite = 0
    show fbava current:
        xzoom -1.0 xalign 0.63
    "Charlotte continues to explain when everyone should get there, the plans, the food, etc."
    $ charlotteSprite = 1
    charlotte "Yeah and then four on the bed, two-oh wait, three on the floor."
    $ charlotteSprite = 0
    $ miaSprite = 1
    mia "Sounds good!"
    $ miaSprite = 0
    $ emilySprite = 1
    emily "Alright everyone got it? Three days from now?"
    $ emilySprite = 0
    $ avaSprite = 1
    ava "Yup."
    $ avaSprite = 0
    $ oliviaSprite = 1
    olivia "Got it."
    $ oliviaSprite = 0
    $ sophiaSprite = 1
    show fbsophia current:
        xzoom 1.0 xalign 0.45
    sophia "Soooo excited! [povname] I'm so excited!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "I can tell."
    $ playerSprite = 0
    $ emilySprite = 1
    show fbsophia current:
        xzoom -1.0
    emily "Alright then I gotta get back to school, see you guys later."
    $ emilySprite = 0
    hide fbemily current
    with Dissolve(0.5)
    $ charlotteSprite = 1
    charlotte "Yeah I gotta get home, Vicky should be getting back now."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I'm driving Mia home, we can drop you off on the way if you want."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Sure thanks."
    $ charlotteSprite = 0
    $ miaSprite = 1
    mia "Let's get something to eat on the way!"
    $ miaSprite = 0
    hide fbplayer current
    hide fbmia current
    hide fbcharlotte current
    with Dissolve(0.5)
    $ sophiaSprite = 1
    $ oliviaSprite = 8
    show fbava current:
        xzoom 1.0
    sophia "Alright guess I'll head out too."

    show fbsophia current:
        xalign 0.2 xzoom -1.0
    show fbolivia current:
        xalign 0.45 xzoom 1.0
    with move
    sophia "Bye girls!"
    $ sophiaSprite = 0
    $ avaSprite = 1
    ava "Bye Soph."
    $ avaSprite = 0
    $ oliviaSprite = 9
    olivia "Bye."
    $ oliviaSprite = 8
    hide fbsophia current
    pause
    show fbolivia current:
        xalign 0.45 xzoom -1.0
    ava "...."
    olivia "...."
    $ avaSprite = 1
    ava "She was right I was totally jealous too."
    $ avaSprite = 0
    $ oliviaSprite = 9
    olivia "It was SO hot."
    $ oliviaSprite = 8
    ava "...."
    olivia "...."
    $ oliviaSprite = 14
    $ avaSprite = 1
    "Olivia & Ava" "Hahahaha"
    $ oliviaSprite = 8
    ava "See yah girl. Love yah."
    $ avaSprite = 0
    $ oliviaSprite = 9
    olivia "Heh love you too. Bye."
    $ oliviaSprite = 8
    $ headtooffice = 2
    jump overworldmap


# Chapter 3: shared events

label chapter3bulliesmassage:
    hide screen uppergui
    hide screen questboxpreview
    scene fs blackblank
    with Dissolve(0.7)
    "Meanwhile..."
    scene fbbullies massage1
    with Dissolve(1.0)
    pause
    stephanie "Mmmmm.."
    scene fbbullies massage2
    stephanie "God these specialty late night massage places are just heavenly aren't they?"
    scene fbbullies massage2b
    melissa "You said it! Just takes all the day's stress right out of me!"
    scene fbbullies massage2d
    melissa "Thanks again for always bringing us with you."
    scene fbbullies massage2c
    stephanie "Oh you know, it'd be boring without you two around."
    stephanie "Your constant bickering has become a calming white noise to me at this point."
    "Masseuse" "Miss are you ready?"
    stephanie "Yes we're ready!"
    scene fbbullies massage3
    with Dissolve(1.0)
    pause
    melissa "Mmmmm..."
    scene fbbullies massage3c
    melissa "You know you love ussss. Even like, with our bickering."
    scene fbbullies massage3b
    stephanie "Hehe."
    stephanie "By the way, your skin is looking absolutely radiant."
    scene fbbullies massage3c
    melissa "Thank youuuu. It's cause'a that skin cream you gave me!"
    scene fbbullies massage3b
    stephanie "It works great right? Came from Milan."
    scene fbbullies massage3c
    melissa "They make creams from Melons now??"
    scene fbbullies massage4
    raven "Hey girls, sorry I'm late."
    melissa "Raven!"
    scene fbbullies massage5
    raven "What you talking about?"
    melissa "Melons! Haha."
    raven "YOUR big melons or the other kind?"
    melissa "Hey my melons ar-"
    melissa "OHMYGOD."
    stephanie "Wait."
    raven "Hmm?"
    melissa "Bitch don't hmm us, your butt!"
    scene fbbullies massage6b
    with Dissolve(0.7)
    raven "Huh? Oh yeah. Told you I had a tat."
    scene fbbullies massage6
    melissa "Cute lil skully!"
    scene fbbullies massage6b
    raven "Hehe Skully's a good name I like that."
    scene fbbullies massage6
    stephanie "So you weren't lying to seem edgy, you've proven us wrong."
    stephanie "My apologies."
    melissa "Yeah me too, I really didn't believe you sorry."
    scene fbbullies massage6b
    raven "Bahhhh it's no big deal."
    scene fbbullies massage6
    melissa "Sooooo."
    melissa "Has anyone else seen skully? Hehehe."
    scene fbbullies massage6b
    raven "Maybe one...white knight."
    scene fbbullies massage6
    stephanie "Hahaha!"
    melissa "I remember that pic you sent! His dong didn't look all that white after you were done with it heh."
    scene fbbullies massage6b
    raven "Some of my best work I must say."
    raven "I'm not alone though am I? Seems like we all had the same idea for our 'favor'."
    scene fbbullies massage6
    melissa "Hehehe, well at least I danced with him first!"
    stephanie "Ah, that's how she got him."
    stephanie "Big boobs bouncing around to some music? Gets any guy."
    scene fbbullies massage6b
    raven "I bet it was probably when she did the blowjob gesture and pointed to the bathroom."
    scene fbbullies massage6
    melissa "Hey! I'll have you know it was a very sultry whisper in his ear!"
    scene fbbullies massage6b
    "Everyone" "Hahaha."
    scene fbbullies massage6
    pause
    scene fbbullies massage7
    with Dissolve(1.0)
    "Everyone" "Mmmmm..."
    pause
    pause
    scene fbbullies massage7b
    raven "That cock though amiright?"
    scene fbbullies massage7c
    stephanie "It's HUGE!"
    melissa "OHMYGOD right??"
    scene fs blackblank
    with Dissolve(0.7)
    melissa "Steph just HOW did you take that thing?"
    stephanie "Honestly he took ME really, helped that I was SO fucking wet."
    raven "He must've absolutely filled you from that pic you sent."
    raven "Emily was really on the other side of the door?"
    stephanie "She. Heard. EVERYTHING."
    melissa "God that's hot."
    stephanie "[povname] seemed to think so!"
    melissa "Hahaha!"
    raven "Hehehe."

    $ bullieschecker = 1
    jump passtime


label chapter3event1:
    "You drive up to Charlotte's house"
    "It's not quite dark yet but the sun is setting"
    "*BZZZZZZ*"
    ava "Yo it's [povname]! [povname]'s here!"
    player "Hi Ava."
    ava "Charlotte how do I buzz him in??!"
    charlotte "You're already drunk Ava just press the button!"
    ava "No I'm not!"
    $ playerSprite = 1
    scene fs charlottelivingroom
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.25 ypos 120
    with Dissolve(0.3)
    player "I'm heeeere!"
    $ playerSprite = 0
    $ emilySprite = 1
    show fbemily current:
        xalign 0.5 ypos 120
    with Dissolve(0.3)
    emily "He's heeeeere!"
    $ emilySprite = 0
    $ miaSprite = 1
    show fbmia current:
        xalign 0.4 ypos 120
    with Dissolve(0.3)
    mia "He's heeeere!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Hey baby, hey everyone."
    $ playerSprite = 0
    $ oliviaSprite = 5
    show fbolivia current behind fbemily:
        xalign 0.65 ypos 120
    with Dissolve(0.3)
    olivia "HE'S!"
    $ oliviaSprite = 9
    olivia "Here, Hi [povname]."
    $ oliviaSprite = 8
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.7 ypos 120
    charlotte "Welcome."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Hey Charlotte, thanks again. I brought snacks."
    $ playerSprite = 0
    $ avaSprite = 1
    show fbava current:
        xalign 0.8 ypos 120
    ava "He's heeeeeere!"
    $ avaSprite = 0
    $ emilySprite = 1
    emily "Haha we already did that Ava."
    $ emilySprite = 0
    $ avaSprite = 1
    ava "Dun care."
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "Alright well that means almost everyone's here."
    $ charlotteSprite = 0
    show fbsophia current:
        xalign 0.15 xzoom -1.0 ypos 120
    with Dissolve(0.5)
    $ sophiaSprite = 4
    sophia "Ugh."
    sophia "Finally freaking made it."
    $ sophiaSprite = 3
    $ miaSprite = 1
    mia "Sophia!"
    $ miaSprite = 0
    $ emilySprite = 1
    emily "Everything alright? We were wondering where you were."
    $ emilySprite = 0
    $ sophiaSprite = 4
    sophia "I had, the WORSE day oh my god."
    sophia "Idonevenwannatalkaboutit."
    $ playerSprite = 15
    $ sophiaSprite = 3
    player "Oh, sorry about that Soph."
    $ playerSprite = 14
    $ sophiaSprite = 4
    sophia "Thanks [povname]."
    sophia "Charlotte, PLEASE can we get into the hot tub? I need stress relief like yesterday."
    $ sophiaSprite = 3
    $ charlotteSprite = 1
    charlotte "Oh uh, yeah sure. We're all here now."
    charlotte "Follow me everyone. Don't forget to grab a towel."
    $ charlotteSprite = 0
    hide fbcharlotte current
    $ sophiaSprite = 4
    sophia "THANK you."
    $ sophiaSprite = 3
    hide fbsophia current
    hide fbemily current
    with Dissolve(0.5)
    pause
    hide fbolivia current
    hide fbava current
    with Dissolve(0.5)
    $ miaSprite = 3
    mia "Oh!"
    mia "But what about-"
    $ miaSprite = 2
    $ playerSprite = 1
    player "It's okay Mia, go relax with your friends."
    $ playerSprite = 0
    $ miaSprite = 3
    mia "Okay...."
    scene fs blackblank
    with Dissolve(0.5)
    "A few minutes later.."
    scene fs sleepoverpartone5
    with Dissolve(1.0)
    "Everyone" "Ahhhhh...."
    sophia "Heaven..."
    emily "So good.."
    scene fs sleepoverpartone3
    with Dissolve(0.5)
    "Everyone" "Mmmmmm."
    scene fs sleepoverpartone6
    charlotte "I don't like to flaunt my wealth often but when it comes to this?"
    charlotte "It's good to be rich."
    mia "..."
    scene fs sleepoverpartone7
    olivia "Something wrong Mia?"
    scene fs sleepoverpartone8
    mia "No...it's just."
    mia "We're relaxing and enjoying the hot tub out here."
    mia "While [povname]'s inside."
    mia "We already agreed to let him join us but then we leave him out of our group bonding?"
    charlotte "Sorry Mia, in my house boys aren't allowed to see girls naked."
    ava "Stupid rule."
    mia "Hmmm!"
    scene fs sleepoverpartone9
    mia "I got an idea!!"
    mia "I'll be right back!"
    emily "What's she up to now?"
    ava "Whatever it is, I know it's crazy and I'm gonna love it."
    scene fs sleepoverpartone10
    charlotte "Bah, it'll be fine."
    mia "Okay now careful stepping in!"
    player "Alright I think I got it.."
    scene fs sleepoverpartone11
    mia "There!"
    mia "Guys I brought [povname]! But I used a blindfold so he can't see anything!"
    charlotte "...."
    player "Genius idea Mia."
    scene fs sleepoverpartone12
    player "Mwah! Reward kiss."
    scene fs sleepoverpartone13
    "Everyone" "*Gasp*"
    emily "!!!!!!"
    scene fs sleepoverpartone14
    player "Wait a minute..."
    scene fs sleepoverpartone15
    pause
    emily "Ehn..."
    player "...."
    scene fs sleepoverpartone16
    player "YOU'RE NOT MIA!!!"
    scene fs sleepoverpartone17
    charlotte "Then fucking stop groping her you bastard!!"
    scene fs sleepoverpartone18
    ava "AHAHAHAHAHA!"
    ava "Oh my God it's already the best sleepover we've done!"
    scene fs sleepoverpartone19
    with Dissolve(0.7)
    ava "Okay okay guys I just got an idea for a game thanks to [povname]."
    player "Oh?"
    ava "Okay."
    scene fs sleepoverpartone23
    with Dissolve(0.5)
    ava "Take your hand."
    player "Kay."
    scene fs sleepoverpartone21
    ava "And grab this real good."
    scene fs sleepoverpartone20
    ava "Ahn."
    charlotte "Wha-AVA!"
    ava "Would you relax Charlotte?"
    ava "Okay give it a good squeeze or two."
    scene fs sleepoverpartone20b
    player "Mhmm."
    ava "Alright nice."
    scene fs sleepoverpartone22
    ava "So. Who's boobs are these?"
    player "...."
    player "They're yours."
    scene fs blackblank
    ava "Okay maybe it doesn't work with me since I explained it haha."
    olivia "I get it!"
    ava "Everyone ready to try it?"
    mia "Okay!"
    sophia "YES!"
    emily "I'm not sure.."
    ava "Oh don't be a prude bitch!"
    emily "Wha!? I'm no-"
    ava "Okay who's up? Let's start with you!"
    "You hear some water sloshing towards you"
    "You put your hands up and are greeted by some tits."
    "They're on the smaller side, but perky and firm."
    $ correctanswer = 0
    $ answerguess = ""
    "Who's boobs are they?"
    menu:
        "Mia's":
            $ correctanswer += 0
            $ answerguess = "Mia"
        "Olivia's":
            $ correctanswer += 0
            $ answerguess = "Olivia"
        "Emily's":
            $ correctanswer += 0
            $ answerguess = "Emily"
        "Sophia's":
            $ correctanswer += 0
            $ answerguess = "Sophia"
        "Ava's":
            $ correctanswer += 0
            $ answerguess = "Ava"
        "Charlotte's":
            $ correctanswer += 1
            $ answerguess = "Charlotte"

    scene fs sleepoverpartone24
    with Dissolve(0.5)
    charlotte "...."
    charlotte "{i}Can't believe I'm doing this in front of the girls.{/i}"
    player "Hmmm, these are [answerguess]'s. I'm sure of it."
    scene fs sleepoverpartone25
    ava "Interesting interesting."
    pause

    scene fs blackblank
    ava "Okay who's next? How about this lovely lady!?"
    "You hear another girl approach you, you lift up your hands once again"
    "These breasts are big for sure, they droop down ever so slightly but have a firm shape"
    "Who's boobs are they?"
    menu:
        "Mia's":
            $ correctanswer += 0
            $ answerguess = "Mia"
        "Olivia's":
            $ correctanswer += 1
            $ answerguess = "Olivia"
        "Emily's":
            $ correctanswer += 0
            $ answerguess = "Emily"
        "Sophia's":
            $ correctanswer += 0
            $ answerguess = "Sophia"
        "Ava's":
            $ correctanswer += 0
            $ answerguess = "Ava"
        "Charlotte's":
            $ correctanswer += 0
            $ answerguess = "Charlotte"

    scene fs sleepoverpartone33
    with Dissolve(0.5)
    olivia "...."
    olivia "{i}This is kinda nice.{/i}"
    scene fs sleepoverpartone34
    with hpunch
    olivia "Ahn!"
    ava "Hey no slapping the merchandise!"
    scene fs sleepoverpartone33
    olivia "No..it's okay."
    ava "I see! nevermind then!"
    player "I think...these are [answerguess]'s."
    pause

    scene fs blackblank
    ava "Step right up step right up who's next? This beautiful maiden over here!"
    "You hear some of the girls giggling, clearly this little game has gotten them in a silly mood"
    "These boobs feel average in size, if not slightly larger. Decent firmness, decent shape, overall some good boobs."
    "Who's boobs are they?"
    menu:
        "Mia's":
            $ correctanswer += 0
            $ answerguess = "Mia"
        "Olivia's":
            $ correctanswer += 0
            $ answerguess = "Olivia"
        "Emily's":
            $ correctanswer += 1
            $ answerguess = "Emily"
        "Sophia's":
            $ correctanswer += 0
            $ answerguess = "Sophia"
        "Ava's":
            $ correctanswer += 0
            $ answerguess = "Ava"
        "Charlotte's":
            $ correctanswer += 0
            $ answerguess = "Charlotte"

    scene fs sleepoverpartone28
    with Dissolve(0.7)
    emily "{i}This is fine! I'm not turned on by this!{/i}"
    player "Hmmm. Very nice."
    player "These are [answerguess]'s boobs!"
    scene fs sleepoverpartone29
    emily "{i}I'm definitely not turned on by everyone watching me getting groped...{/i}"
    emily "{i}Thank God I'm in a hot tub{/i}"
    pause
    scene fs blackblank
    ava "Not too many left now! Who's next? Step right up!"
    "These next tits had very hard nipples, maybe slightly less than average size but not tiny by any means"
    "Who's boobs are they?"
    menu:
        "Mia's":
            $ correctanswer += 0
            $ answerguess = "Mia"
        "Olivia's":
            $ correctanswer += 0
            $ answerguess = "Olivia"
        "Emily's":
            $ correctanswer += 0
            $ answerguess = "Emily"
        "Sophia's":
            $ correctanswer += 1
            $ answerguess = "Sophia"
        "Ava's":
            $ correctanswer += 0
            $ answerguess = "Ava"
        "Charlotte's":
            $ correctanswer += 0
            $ answerguess = "Charlotte"

    scene fs sleepoverpartone30
    player "Hmmm."
    sophia "Hehehe!"
    scene fs sleepoverpartone31
    sophia "!!!"
    ava "Uh..you can keep going for a bit if you want?"
    player "Nope"
    player "I'm good."
    ava "You sure? The volunteer doesn't mind."
    player "I know it's [answerguess]."
    scene fs sleepoverpartone32
    sophia "What??"
    sophia "UGH!"
    scene fs blackblank
    ava "Okay just one girl left!"
    "You can feel these tits are huge, tied at least in size with the other large ones"
    "Your hands push into them with a slight amount of give. Fantastic shape, very soft, and small perky nipples"
    "Who's boobs are they?"
    menu:
        "Mia's":
            $ correctanswer += 1
            $ answerguess = "Mia"
        "Olivia's":
            $ correctanswer += 0
            $ answerguess = "Olivia"
        "Emily's":
            $ correctanswer += 0
            $ answerguess = "Emily"
        "Sophia's":
            $ correctanswer += 0
            $ answerguess = "Sophia"
        "Ava's":
            $ correctanswer += 0
            $ answerguess = "Ava"
        "Charlotte's":
            $ correctanswer += 0
            $ answerguess = "Charlotte"

    scene fs sleepoverpartone27
    with Dissolve(0.5)
    mia "Hehe."
    player "Ah...very nice."
    ava "Well?"
    player "I'd know these anywhere Ava, these tits belong to [answerguess]."
    scene fs sleepoverpartone26
    mia "..."
    ava "Okay! That's everyone thanks for playing!"
    scene fs sleepoverpartone2
    with Dissolve(0.5)
    player "Haha that was actually pretty fun girls thanks for that."
    player "And for letting me in here."
    charlotte "You better appreciate how lucky you are."
    charlotte "Getting to touch all our breasts like that."
    charlotte "Rubbing and pinching them, and for free no less!"
    charlotte "Freely taking your hands and having your fill of our bodies!"
    scene fs sleepoverpartone35
    player "I appreciate it don't you worry about that!"
    if correctanswer == 5:
        jump miahelpwithboner
    else:
        jump getoutoftub


label getoutoftub:
    "Everyone" "!!!"
    charlotte "Oh my God!"
    player "What is it?"
    mia "You've got a boner [povname]."
    player "Oh shit uh."
    scene fs sleepoverpartone36
    with Dissolve(0.5)
    player "Sorry guys. That's cause and effect for you."
    player "I'll get out of the tub now, you guys enjoy the rest of it I'll see you inside."
    scene fs blackblank
    with Dissolve(0.7)
    "The girls relaxed for a bit longer, processing the sight of your giant hard cock"
    "Each with their own thoughts about it.."
    jump continuesleepover2


label miahelpwithboner:
    player "...."
    player "Why'd it get quiet?"
    mia "You have a boner [povname]."
    scene fs sleepoverpartone36
    player "Oh shit I do. Girls I'm so sorry."
    player "I should probably-"
    scene fs sleepoverpartone38
    with Dissolve(0.5)
    mia "No! Don't worry everyone!"
    mia "I want to make sure everyone is comfortable at Charlotte's party!"
    scene fs sleepoverpartone37
    charlotte "Huh?"
    scene fs sleepoverpartone38
    mia "I will take care of this real quick! Then we can go back to relaxing."
    player "What do you mean Mia?"
    show miajaccuzziboobjob movie1
    player "Oh that's...that's what you mean."
    charlotte "{size=25}Mia what the hell are you doing??{/size}"
    show miajaccuzziboobjob movie2
    mia "I know the quickest way to get rid of [povname]'s hard on!"
    mia "Don't worry everyone!"
    ava "Oh I am NOT worried hehe."
    player "Oh man Mia your tits feel incredible as always."
    charlotte "{i}Even [povname]'s huge penis can still be covered with Mia's boobs!{/i}"
    pause
    show miajaccuzziboobjob movie3
    mia "Mmm!"
    mia "*Suck*"
    player "Oh Fuck baby that's it!"
    olivia "{i}I can't look away.{/i}"
    player "The other...hah...girls are gone right?"
    emily "{i}She's so good at this! When did she get so good at this??{/i}"
    player "Fuck baby I'm gonna cum!"
    pause
    show miajaccuzziboobjob movie4
    player "AGH FUCK."
    player "YES!"
    "Everyone" "!!!!"
    mia "*Gulp* *Gulp*"
    pause
    scene fs blackblank
    with Dissolve(0.5)
    player "You drained me, I gotta go clean up babe."
    mia "Okay! See you soon :D"
    scene fs sleepoverpartone4
    with Dissolve(1.0)
    mia "Ahhh there."
    mia "Now we can all relax again."
    emily "You said it..."
    scene fs sleepoverpartone40
    with vpunch
    emily "NOT!"
    scene fs sleepoverpartone39
    mia "Huu?"
    scene fs sleepoverpartone40
    emily "Mia have you ANY idea how inappropriate that was??"
    emily "You made your friends watch as you brought your boyfriend to climax IN CHARLOTTE'S HOT TUB."
    emily "WHERE WE ALL CURRENTLY ARE."
    scene fs sleepoverpartone39
    mia "But I swallowed so none of it would get in the tub..."
    scene fs sleepoverpartone40
    emily "The issue is that you think it's alright to subject us to such lewd antics!"
    emily "Did you stop to think how we would feel at all?"
    emily "This is a sleepover not some sex party!"
    scene fs sleepoverpartone41
    mia "Oh..."
    mia "Oh geez."
    olivia "Don't worry Mia, Emily's spouting some bullshit."
    emily "What?!"
    olivia "I saw her fingering herself while you were giving [povname] that boobjob."
    emily "N-No I wasn't!"
    olivia "Oh, you totally were."
    olivia "You were really going at it too, did you cum?"
    scene fs sleepoverpartone42
    emily "I WAS NOT TOUCHING MYSELF!!"
    scene fs sleepoverpartone43
    olivia "My mistake then, I saw the fast, short movements of your arm in and out of the water and just assumed."
    ava "Hehehe."
    ava "Like I said, best sleepover ever."
    jump continuesleepover2


label continuesleepover2:

    scene fs blackblank
    with Dissolve(1.0)
    "You got changed into your sleepwear once you got out of the hot tub"
    "Everyone else joined you not too long after in the living room"

    scene fs sleepoverparttwo1
    pause
    player "Well this certainly takes me back."
    ava "Spin the bottle!"
    ava "Pretty much truth or dare, someone spins it and whoever it lands on has to take on the spinner's truth or dare."
    sophia "Ohhhh much fun!"
    mia "Hehe!"
    emily "Hmmm."
    charlotte "Who's going first?"
    scene fs mcbottle
    player "This is my first time here so I'll go first!"
    emily "Alrighty go ahead."
    player "I don't like to cloud my judgement when I know who I'm asking."
    player "So I'm going to dare whoever this lands on to....kiss the person opposite them."
    scene fs spinbottle1
    ava "Oooohh. I like it!"
    scene fs spinbottle4
    emily "Okay! That's Charlotte."
    charlotte "So that means.."
    scene fs spinbottlesophiachar1
    sophia "Charlooootte!!"
    charlotte "S-Sophia?"
    scene fs spinbottlesophiachar2
    sophia "MMMWAH!"
    charlotte "??"
    scene fs spinbottlesophiachar3
    sophia "Charlotte. My short Queen. My friend. Comrade in arms."
    sophia "We must stick together more!"
    scene fs spinbottlesophiachar3b
    charlotte "Oh hehe...um what?"
    scene fs spinbottlesophiachar4
    sophia "Our enemies surround us. Simply look and you will see."
    scene fs spinbottlesophiachar4b
    charlotte "I don't know what you..."
    scene fs spinbottlesophiachar5
    with vpunch
    pause
    scene fs spinbottlesophiachar6
    with vpunch
    pause
    scene fs spinbottlesophiachar7
    with vpunch
    pause
    scene fs spinbottlesophiachar8
    charlotte "I...I see."
    scene fs spinbottlesophiachar9
    charlotte "I see now sister!"
    scene fs spinbottlesophiachar9b
    sophia "We must stand up and fight back against our oppressors!"
    sophia "Small boobs are love!"
    scene fs spinbottlesophiachar9c
    "Sophia & Charlotte" "Small boobs are life!"
    player "Amen!"
    scene fs spinbottle4
    with Dissolve(0.7)
    emily "Okay who's spinning next?"
    scene fs sophiabottle
    sophia "I will!"
    scene fs spinbottle1
    sophia "Okay c'mon c'mon c'mon!"
    scene fs spinbottle2
    emily "Ava!"
    sophia "No!"
    ava "Hey that's me!"
    ava "Whut you gonna do to me Soph??"
    sophia "Ugh. Go kiss Mia or something."
    mia "Oh hehe!"
    emily "You know you don't have to keep making people kiss.."
    scene fs spinbottleavamia1
    with Dissolve(0.5)
    pause
    mia "Okay!"
    scene fs spinbottleavamia1b
    mia "Chuuu."
    scene fs spinbottleavamia2
    ava "Hey babe."
    mia "Huh?"
    ava "Let's make your boyfriend jealous."
    mia "??"
    scene fs spinbottleavamia3
    ava "Mmmm."
    scene fs spinbottleavamia4
    mia "Uhnn."
    ava "Mlmmm.."
    sophia "Oh right...Ava gets super horny when she drinks.."
    scene fs spinbottleavamia5
    ava "Ahn..hah.."
    mia "Ahh.."
    scene fs spinbottleavamia5b
    pause
    scene fs spinbottleavamia5c
    player "Is...is she taunting me?"
    sophia "Oh for sure."
    olivia "100 percent"
    ava "Hehehe."
    scene fs spinbottleavamia6
    mia "Hah.."
    ava "You like that Mia?"
    scene fs spinbottleavamia6b
    mia "Yes you're a very good kisser!"
    ava "Hehe."
    scene fs spinbottleavamia6c
    mia "I think I prefer [povname] though sorry."
    ava "W-What?"
    mia "He's just a bit better, really good with his tongue!"
    mia "Nothing personal!"
    ava "I..."
    ava "T-Tongue?"
    sophia "Ah. She broke."
    scene fs spinbottle2
    emily "Next!"
    scene fs miabottle
    mia "Oh let me!"
    scene fs spinbottle1
    pause
    scene fs spinbottle3
    emily "Ah!"
    emily "Oh that's me."
    mia "Okay who hasn't...Olivia kiss Emily!"
    emily "Again with the kissing?!"
    scene fs spinbottleemilyolivia1
    with Dissolve(0.7)
    pause
    emily "H-Hey Olivia.."
    olivia "Hey there beautiful."
    scene fs spinbottleemilyolivia2
    emily "Oh I don't know if I'm beautiful.."
    scene fs spinbottleemilyolivia3
    pause
    scene fs spinbottleemilyolivia4
    pause
    olivia "Would these lips lie to you?"
    emily "N-No.."
    olivia "Let me prove it."
    scene fs spinbottleemilyolivia5
    pause
    scene fs spinbottleemilyolivia6
    pause
    scene fs spinbottleemilyolivia7
    pause
    emily "Mmmmm."
    olivia "Mmmmm."
    scene fs spinbottleemilyolivia8
    "Olivia & Emily" "MMMM!"
    pause
    pause
    scene fs spinbottleemilyolivia7
    ava "Booooo"
    ava "Lame! No passion!"
    scene fs spinbottleemilyolivia9
    emily "WHAT DO YOU MEAN NO PASSION!"
    ava "No passion! No Tongue!"
    emily "YOU DON'T NEED TONGUE TO HAVE PASSION!"
    ava "Booo"
    ava "No sex! Boooo!"
    emily "AVA!!"
    olivia "Hehehe."
    scene fs blackblank
    with Dissolve(0.7)
    pause
    "You and the girls continue playing around and having fun"
    "Food gets ordered and drinks are had"
    "Overall it was a great night, you had much more fun than you were expecting"
    "And eventually the time came to head to bed and a question you had at the back of your mind had to finally be answered"
    "Who do you want to sleep with?"
    $ chosenchick = ""

    menu:
        "Emily" if emilyphase3interaction1 >= 2:
            $ chosenchick = "Emily"
        "Mia" if miaphase3interaction1 >= 2:
            $ chosenchick = "Mia"
        "Sophia" if sophiaphase3interaction1 >= 2:
            $ chosenchick = "Sophia"
        "Ava" if avaphase3interaction1 >= 2:
            $ chosenchick = "Ava"
        "Olivia" if oliviaphase3interaction1 >= 2:
            $ chosenchick = "Olivia"
        "Charlotte" if charlottephase3interaction1 >= 2:
            $ chosenchick = "Charlotte"
        "Nobody":
            $ chosenchick = "Nobody"

    jump continuephase3event1bedtime


label continuephase3event1bedtime:

    if chosenchick == "Charlotte":
        jump sleepwithcharlotte
    elif chosenchick == "Mia":
        jump sleepwithmia
    elif chosenchick == "Emily":
        jump sleepwithemily
    elif chosenchick == "Olivia":
        jump sleepwitholivia
    elif chosenchick == "Ava":
        jump sleepwithava
    elif chosenchick == "Sophia":
        jump sleepwithsophia
    elif chosenchick == "Nobody":
        jump passtime


label sleepwithcharlotte:
    scene fs sleepoverbedpovcharlotte
    with Dissolve(0.7)
    "Unfortunately Charlotte's content for this event is not finished"
    scene fs groupbedsexcharlotte1
    with Dissolve(0.5)
    "Her scene will be complete in the next update! Only Mia's is complete for now."
    scene fs groupbedsexcharlotte2
    pause
    "Would you like to end the night or watch Mia's content instead?"
    menu:
        "Watch Mia":
            jump sleepwithmia
        "End the night":
            jump passtime


label sleepwithemily:
    scene fs sleepoverbedpovemily
    with Dissolve(0.7)
    "Unfortunately Emily's content for this event is not finished"
    scene fs groupbedsexemily1
    pause
    scene fs groupbedsexemily2
    pause
    "Would you like to end the night or watch Mia's content instead?"
    menu:
        "Watch Mia":
            jump sleepwithmia
        "End the night":
            jump passtime


label sleepwithsophia:
    scene fs sleepoverbedpovsophia
    with Dissolve(0.7)
    "Unfortunately Sophia's content for this event is not finished"
    scene fs groupbedsexsophia1
    pause
    scene fs groupbedsexsophia2
    pause
    "Would you like to end the night or watch Mia's content instead?"
    menu:
        "Watch Mia":
            jump sleepwithmia
        "End the night":
            jump passtime


label sleepwithava:
    scene fs sleepoverbedpovava
    with Dissolve(0.7)
    "Unfortunately Ava's content for this event is not finished"
    scene fs groupbedsexava1
    pause
    scene fs groupbedsexava2
    pause
    scene fs groupbedsexava3
    pause
    "Would you like to end the night or watch Mia's content instead?"
    menu:
        "Watch Mia":
            jump sleepwithmia
        "End the night":
            jump passtime


label sleepwitholivia:
    scene fs sleepoverbedpovolivia
    with Dissolve(0.7)
    "Unfortunately Olivia's content for this event is not finished"
    scene fs groupbedsexolivia1
    pause
    scene fs groupbedsexolivia2
    pause
    "Would you like to end the night or watch Mia's content instead?"
    menu:
        "Watch Mia":
            jump sleepwithmia
        "End the night":
            jump passtime
