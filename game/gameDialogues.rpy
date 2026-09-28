#THIS IS DIALOGUE THAT ISN'T ASSOCIATED WITH ANY SINGLE CHARACTER OR QUESTLINE----------------------------------------

label gameIntro:

    $ miaphase1interaction3 = 0
    $ avaphase1interaction2 == 0
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
    $ miaquestlog = "I wonder if I should bring anyone else along with me to Mia's shopping trip..."
    $ miaquesticon = "gui/questboxMia.png"

    $ katiequestlog = "I should text Katie!...Or should I?"
    $ katiequesticon = "gui/questboxKatie.png"
    $ contact_list.append("Katie")

    $ avaphase1interaction1 = 6
    $ avaphase1interaction2 = 4
    $ avaquestlog = "I feel like I'm making a real connection with Ava, I should see her at the gym again."
    $ avaquesticon = "gui/questboxAva.png"

    $ sophiaphase1interaction1 = 5
    $ sophiaphase1interaction2 = 3
    $ sophiaquestlog = "I feel bad about skipping out on lunch, I should see her again."
    $ sophiaquesticon = "gui/questboxSophia.png"

    $ oliviaphase1interaction1 = 4
    $ oliviaphase1interaction3 = 2
    $ oliviaquestlog = "That was so hot! I should really talk to her about where to go from here though."
    $ oliviaquesticon = "gui/questboxOlivia.png"

    $ emilyphase1interaction2 = 6
    $ emilyphase1interaction1 = 5
    $ emilyquestlog = "Is Emily becoming a friend? Or do I really just want to fuck her?"
    $ contact_list.append("Emily")
    $ emilyquesticon = "gui/questboxEmily.png"

    $ charlottephase1interaction1 = 5
    $ charlottephase1interaction2 = 4
    $ charlottephase1interaction3 = 2
    $ charlottequestlog = "I should explore Sunnyside some more during the morning."
    $ charlottequesticon = "gui/questboxCharlotte.png"

    $ victoriaquesticon = "gui/questboxVictoria.png"
    $ victoriaquestlog = "Victoria is quite the beautiful woman..and sucks a mean dick."

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
    #$ hiden_textbox = False
    mia "Good morning."
    scene fs miamorning1
    player "Haha morning."
    player "Were you watching me sleep?"
    scene fs miamorning3
    ##voice "audio/miagameaudio/mialaugh.wav"
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
    #mia gets up
    scene fs miamorning5
    with Dissolve(0.7)
    mia "Are you still going to stop by the café?"
    player "Huh? Oh yeah I’ll head over after I take a shower."
    # mia bends over
    scene fs miamorning6
    with Dissolve(0.7)
    player "{i}God damn I am one lucky S.O.B.{/i}"
    scene fs miamorning8
    with Dissolve(0.7)
    mia "Great! I can’t wait to introduce you to everyone!"
    #mia pulls her panties up
    scene fs miamorning7
    player "Oh yeah..."
    scene fs miamorning8
    mia "You didn't forget did you?"
    #mia turns around fully dressed
    scene fs miamorning7
    player "No no of course not, I'll be there."
    scene fs miamorning8
    mia "Great! See you soon then!"
    scene fs miamorning7
    player "See you soon babe."
    scene fs miafalling1
    with Dissolve(1.0)
    ##voice "audio/miagameaudio/miahum.wav"
    play music "audio/Main theme (Double Loop).mp3" fadein 5

    player "{i}How should I explain this to you? You know those shows that have a bunch of female characters all with different personality types but they're great friends anyways?{/i}"

    player "{i}And even if it’s a smaller group but there’s a main generic girl the story follows who believes in friendship or magic that always saves the day?{/i}"

    player "{i}Yeah that’s EXACTLY the dynamic of my girlfriend's group. But she isn’t the main character oh no.{/i}"
    player "{i}There is ALWAYS that one bumbling side character with huge tits who’s a lovable, clumsy moron who never gets the spotlight.{/i}"

    player "{i}I’m not saying Mia’s a moron but she spaces out real easy and has a hard time being aware of her immediate surroundings...{/i}"
    voice "audio/miagameaudio/miaah.wav"
    scene fs miafalling2
   # with vpunch
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

label specialwakeup:
    hide screen backbuttonROOM

    if amountspent >= 350 and ashleychecker == 0 and watchcount == 0:
        jump ashleyinteraction1part1

    if miaphase2interaction2 == 4 and currentchapter == 3 and dayNumber > 21:
        jump miaphase3interaction1part1
    if miaphase1interaction2 == 4:
        jump miaphase1interaction2part3wakeup
    if avaphase2interaction1 == 1:
        jump avaphase2interaction2part1
    if whereami == "playerRoom":
        jump charlottephase2interaction2part1
    # if charlottephase2interaction2 == 1:
    #     "Mia calls and asks MC to join her and Charlotte to breakfast"
    #     $ charlottequestlog = "Mia invited me to breakfast at the café"
    #     $ charlottephase2interaction2 = 2
    #     jump playerRoom

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
   #voice "audio/miagameaudio/miayawn.wav"
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
    #voice "audio/miagameaudio/miamwahkiss.wav"
    mia "*Chuu*"
    #they kiss here
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
    mia "I didn’t know you knew eachother!"
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

label charlottephase3interaction1part1:

    "Alright class, that'll be it for today."
    show fbcharlotte current:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Charlotte! Hey what's up?"
    $ playerSprite = 0
    $ charlotteSprite = 11
    charlotte "[povname]!"
    $ charlotteSprite = 16
    $ playerSprite = 1
    player "Haha I don't think I've ever seen you greet me with a smile."
    $ charlotteSprite = 6
    $ playerSprite = 0
    charlotte "Oh you're right hang on."
    $ charlotteSprite = 0
    show fbcharlotte current:
        xzoom -1.0 xalign 0.7
    charlotte "*Ahem*"
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.6 xzoom 1.0 ypos 120
    charlotte "What do YOU want?"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Ah there she is!"
    $ playerSprite = 0
    $ charlotteSprite = 11
    charlotte "Hehe."
    $ charlotteSprite = 16
    $ playerSprite = 1
    player "Class just finish?"
    $ playerSprite = 0
    $ charlotteSprite = 11
    charlotte "Yup I was just headed out."
    $ charlotteSprite = 16
    $ playerSprite = 1
    player "Let me walk with you."
    $ playerSprite = 0
    $ charlotteSprite = 11
    charlotte "Thanks."
    $ charlotteSprite = 16
    hide fbcharlotte current
    hide fbplayer current
    scene fs schoolhallway
    with Dissolve(0.8)
    pause
    $ oliviaSprite = 0

    show fbolivia current:
        xalign 0.6 xzoom -1.0 ypos 120
    show fbmia current:
        xalign 0.7 xzoom -1.0 ypos 120
    show fbava current:
        xalign 0.8 ypos 120
    with Dissolve(0.5)
    pause

    $ avaSprite = 1
    ava "No I'm telling you, they wanna smack em around!"
    $ avaSprite = 0
    $ miaSprite = 1
    mia "Definitely not. I know from experience!"
    $ miaSprite = 0
    $ oliviaSprite = 1
    olivia "One guy doesn't dictate the whole gender. Overall I'm definitely right."
    $ oliviaSprite = 0

    show fbplayer current:
        xalign 0.5 ypos 120
    show fbcharlotte current:
        xalign 0.4 xzoom -1.0 ypos 120
    with Dissolve(0.5)
    pause
    $ charlotteSprite = 11
    charlotte "Hey girls, what the heck are you talking about?"
    $ charlotteSprite = 16
    show fbolivia current:
        xalign 0.6 xzoom 1.0 ypos 120
    show fbmia current:
        xalign 0.7 xzoom 1.0 ypos 120
    
    $ oliviaSprite = 1
    olivia "Hey Charlotte."
    $ oliviaSprite = 0
    $ miaSprite = 1
    mia "[povname]! Great timing!"
    $ miaSprite = 0
    $ avaSprite = 1
    ava "True [povname] can totally solve this!"
    $ avaSprite = 0
    player "Hmm?"
    $ charlotteSprite = 11
    charlotte "What can he solve?"
    $ charlotteSprite = 16
    $ avaSprite = 1
    $ playerSprite = 11
    ava "[povname]. When guys see big tits, what do they want to do most?"
    $ avaSprite = 0
    charlotte "...."
    $ charlotteSprite = 1
    charlotte "What."
    $ charlotteSprite = 0
    $ oliviaSprite = 9
    olivia "And not your personal preferences, guys in general."
    $ oliviaSprite = 8
    $ miaSprite = 1
    mia "Ava thinks they want to use their hands to-"
    $ miaSprite = 0
    $ avaSprite = 1
    ava "Squeeze em, grope em, slap em around, even pinch a nipple or two. I mean it's obvious."
    ava "There's literally the phrase 'You can't keep your hands to yourself'."
    $ avaSprite = 0
    $ oliviaSprite = 9
    show fbolivia current:
        xalign 0.6 xzoom -1.0 ypos 120
    olivia "Wrong."
    $ oliviaSprite = 8
    $ miaSprite = 8
    mia "Olivia thinks they want to eh...."
    $ oliviaSprite = 9
    show fbolivia current:
        xalign 0.6 xzoom 1.0 ypos 120
    olivia "Fuck them. When you're thinking with your dick obviously it's your dick you want to use right?"
    olivia "It's just logic. Guys want boobjobs."
    $ oliviaSprite = 8
    $ miaSprite = 1
    mia "Ah ah I'm afraid it's not the dick neurons that activate the most!"
    $ miaSprite = 0
    $ charlotteSprite = 1
    charlotte "Dick...neurons?"
    $ charlotteSprite = 0
    $ miaSprite = 13
    mia "Guys want to suck them! It's like a primal brain thing from when we're babies."
    $ miaSprite = 1
    mia "Right [povname]?"
    $ miaSprite = 0
    $ playerSprite = 11
    menu:
        "Squeeze em":
            jump continuebooboconvo
        "Fuck em":
            jump continuebooboconvo
        "Suck em":
            jump continuebooboconvo

label continuebooboconvo:
    $ playerSprite = 17
    player "Oh I dun-"
    $ playerSprite = 15
    $ miaSprite = 1
    show fbmia current at surpriseshake:
        xalign 0.7 xzoom 1.0 ypos 120
    mia "And the bigger they are the more they want to!"
    $ miaSprite = 0
    $ avaSprite = 1
    ava "Well we agree on that. They definitely prefer big tiddies, the pervs."
    $ avaSprite = 0
    $ oliviaSprite = 9
    olivia "It is known."
    $ oliviaSprite = 8
    $ playerSprite = 6
    player "Girls girls. You're all getting ahead of yourselves a bit I think."
    $ playerSprite = 0
    charlotte "...."
    $ playerSprite = 16
    player "I mean yeah I PERSONALLY love some big...a large bust."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Hehe."
    $ miaSprite = 0
    $ playerSprite = 17
    player "But all guys love boobs in general, if they're bigger there's just more to...love."
    $ playerSprite = 8
    "...."
    $ avaSprite = 16
    ava "Yeah that's Bullshit."
    $ avaSprite = 15
    $ miaSprite = 3
    mia "You never really gave me that impression.."
    $ miaSprite = 2
    $ oliviaSprite = 9
    olivia "They like them bigger, I'm sure there's some science behind it."
    $ oliviaSprite = 8
    $ avaSprite = 1
    $ charlotteSprite = 5
    show fbcharlotte current:
        xalign 0.3 ypos 120
    with move
    ava "If they're larger the dicks be getting harde-"
    $ avaSprite = 16
    ava "Oh...."
    $ playerSprite = 14
    show fbplayer current:
        xalign 0.4 xzoom -1.0
    ava "Oh Charlotte I didn't uh.."
    $ miaSprite = 3
    mia "Oh gosh Charlotte we don't mean you don't...I mean you do!"
    $ miaSprite = 2
    $ oliviaSprite = 13
    olivia "Yours are very perky."
    $ oliviaSprite = 10
    $ charlotteSprite = 1
    charlotte "Stop."
    $ charlotteSprite = 0
    $ miaSprite = 10
    show fbmia current:
        xalign 0.15 ypos 120
    with move
    show fbmia current:
        xzoom -1.0
    mia "They're beautiful Charlotte, I've seen your boobs!"
    $ avaSprite = 1
    ava "Honestly shape matters more than anything else."
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "Stop talking about my breasts."
    $ charlotteSprite = 0
    $ oliviaSprite = 9
    show fbolivia current:
        xalign 0.4
    show fbplayer current:
        xalign 0.5
    with move
    olivia "You don't need to be able to wrap them around a dick in order-"
    $ oliviaSprite = 8
    $ charlotteSprite = 1
    charlotte "I hate this."
    $ charlotteSprite = 0
    $ miaSprite = 3
    mia "Oh Charlotte I'm so sorry!"
    $ miaSprite = 2
    $ oliviaSprite = 9
    olivia "Yeah sorry. We didn't mean to upset you."
    $ oliviaSprite = 8
    $ miaSprite = 1
    mia "You are a cute and amazing girl with a beautiful body!"
    $ miaSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte current:
        xzoom 1.0 xalign 0.25
    charlotte "Stop talking."
    $ charlotteSprite = 0
    
    hide fbmia current
    show fbcharlotte boobhug1:
        xalign 0.2 ypos 140
    mia "C'mere!"
    charlotte "...."
    hide fbolivia current
    show fbcharlotte boobhug2:
        xalign 0.2 ypos 140
    olivia "Me too!"
    charlotte "!!!!!!"
    pause
    scene angrycharlotte boobhug4
    with Dissolve(1.0)
    pause
    charlotte "...."
    scene fs schoolhallway
    show fbolivia current:
        xalign 0.4 ypos 120
    show fbmia current:
        xalign 0.2 ypos 120
    show fbcharlotte current:
        xalign 0.3 ypos 120
    show fbava current:
        xalign 0.8 ypos 120
    show fbplayer current:
        xalign 0.5 xzoom -1.0 ypos 120
    pause
    show fbcharlotte current:
        xalign 0.1 ypos 120
    with move
    show fbcharlotte current:
        xzoom -1.0
    $ charlotteSprite = 1
    charlotte "Okay!"
    charlotte "Thanks girls, you're right!"
    $ charlotteSprite = 0
    $ miaSprite = 1
    mia "Yay?"
    $ miaSprite = 0
    charlotte "I don't need Giant fat bags in order to get guys to fuck me!"
    $ avaSprite = 11
    ava "Well we didn't exactly say it like that..."
    $ avaSprite = 0
    $ charlotteSprite = 1
    charlotte "I just need a good attitude, and confidence in my body!"
    $ charlotteSprite = 0
    $ oliviaSprite = 9
    olivia "Yup."
    $ oliviaSprite = 8
    $ charlotteSprite = 1
    charlotte "[povname], would you be so KIND as to drive me home?"
    charlotte "I'm a bit...too tired today to walk."
    $ charlotteSprite = 0
    $ playerSprite = 17
    player "Oh uh yeah sure, no problem."
    $ playerSprite = 1
    player "See you guys."
    $ oliviaSprite = 9
    olivia "Bye."
    $ oliviaSprite = 8
    $ avaSprite = 1
    ava "Drive safe!"
    $ avaSprite = 0
    $ miaSprite = 1
    mia "Bye you two!"
    $ miaSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte current:
        xzoom 1.0
    hide fbcharlotte current
    charlotte "See yaaaaah."
    player "Woah wait up."

    $ charlottephase2interaction3 = 4
    $ charlottephase3interaction1 = 1
    $ charlottequestlog = "Charlotte seems pretty upset after Mia and Olivia accidently teased her. I should drive her at home"
    jump passtime

label charlottephase3interaction1part2:
    player "Okay we're here."
    charlotte "Park and come in."
    player "Okay.."
    scene fs charlotteroom
    with Dissolve(0.7)
    pause
    $ playerSprite = 11
    show fbcharlotte current:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ charlotteSprite = 1
    charlotte "They think just because *Grumble Grumble*"
    charlotte "I DON'T NEED...*Grumble*"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Charlotte I don't mind hanging out bu-"
    scene fs blackblank
    charlotte "Sit on the bed, and take out your c-cock!"
    player "What? Really-"
    player "Oh there goes your panties."
    charlotte "BED!"
    scene fs charlottejealoussex1
    with Dissolve(0.5)
    charlotte "Hah...hah."
    charlotte "I don't need...stupid big boobs!"
    player "No you don't."
    charlotte "We're gonna FUCK."
    player "Yes we are."
    charlotte "And you...you're gonna CUM inside me!"
    charlotte "Because you're so turned on by my non big-boob-having body!"
    scene fs charlottejealoussex2
    charlotte "Now just...slide it in.."
    player "Fuck you are really wet."
    scene fs charlottejealoussex12b
    with Dissolve(0.5)
    charlotte "Oh God..."
    charlotte "You fill so much of me Daddy.."
    scene fs charlottejealoussex3
    with Dissolve(0.5)
    charlotte "Ahn!"
    charlotte "You're getting bigger inside me!"
    scene fs charlottejealoussex4
    player "It's cause my babygirl feels so fucking good."
    scene fs charlottejealoussex12
    with vpunch
    charlotte "AHN AHN AHN!"
    player "That's right keep bouncing on my cock!"
    charlotte "YES! YESSSS!"
    scene fs charlottejealoussex4
    charlotte "[povname]! [povname]!!!!"
    
    victoria "Excuse me miss."
    charlotte "AHN!"
    victoria "Mistress Charlotte."
    scene fs charlottejealoussex5
    with Dissolve(0.5)
    victoria "Apologies for the...interruption."
    charlotte "V-Vicky??"
    victoria "You have a call."
    charlotte "Tell them I'll call them back!"
    victoria "It's your father."
    charlotte "!!!"
    scene fs charlottejealoussex6
    with Dissolve(0.5)
    charlotte "H-Hi Daddy."
    charlotte "No! I'm just with a friend."
    charlotte "Yes Daddy."
    charlotte "What do you mea-"
    scene fs charlottejealoussex7
    charlotte "MMph!"
    scene fs charlottejealoussex7b
    with Dissolve(0.5)
    charlotte "Ahn..."
    charlotte "Mmmm.."
    scene fs charlottejealoussex8
    charlotte "H-Huh?"
    charlotte "No I- of course!"
    scene fs charlottejealoussex12b
    with Dissolve(0.5)
    charlotte "Yes Daddy!"
    scene fs charlottejealoussex12
    charlotte "YES DADDY!"
    charlotte "I'm CUMMING!!"
    charlotte "I-I mean I'll go!"
    charlotte "I love you!!"
    scene fs charlottejealoussex9
    with Dissolve(0.7)
    charlotte "Hah..hah.."
    player "You like talking to your father while I'm balls deep inside your pussy?"
    charlotte "N-No."
    scene fs charlottejealoussex10
    charlotte "Y-Yes.."
    player "I can feel it coming babygirl, you ready?"
    scene fs charlottejealoussex10b
    charlotte "Yes."
    player "Fuck."
    scene fs charlottejealoussex12b
    with Dissolve(0.5)
    player "Tell me what you want!"
    charlotte "Cum inside me Daddy!"
    charlotte "PLEASE!!"
    scene fs charlottejealoussex13
    with vpunch
    charlotte "AHN!!"
    scene fs charlottejealoussex11
    with Dissolve(0.5)
    player "FUCK BABY!"
    scene fs charlottejealoussex14
    with Dissolve(1.0)
    charlotte "Hah...hah."
    charlotte "T-Thank you Daddy."
    player "That's a good girl."
    scene fs blackblank
    with Dissolve(0.7)
    player "Oh yeah, what did your dad want?"
    charlotte "He uh...wants me to go to some fancy art Gala in a few days."
    charlotte "A bunch of stuffy assholes in suits pretending like they understand paintings."
    charlotte "Food is good so usually I go but he said I need a plus one this time-"
    player "I'll go."
    charlotte "Huh?"
    player "I'll go with you. Let's make it a date, should be a lot more fun that way."
    charlotte "Oh uh...yeah okay great. Thanks."
    victoria "I hope you two have a good time."
    charlotte "VICKY YOU'RE STILL HERE???"
    $ charlottephase3interaction1 = 2
    $ charlottequestlog = "No more content for Charlotte this version (ch2.5)"
    jump passtime

label avaphase3interaction1part1:
    show fbava current:
        xalign 0.6 ypos 120
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ avaSprite = 1
    ava "[povname]! Hey man."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Sup."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "How you doing? Get a good sleep?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Haha sleep? Yeah it was fine."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Sleep is very important for your health! It's when your body recovers and you build bigger muscles!"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Huh. I'll keep that in mind. Did YOU sleep well?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Like a LOG oh my God."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Haha great to hear. So what are you up to?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Well I'm usually at the track around this time but I'm skipping today, so mainly just waiting around for one of the girls."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Wait why are you skipping? That's not like you."
    $ playerSprite = 0
    $ avaSprite = 4
    ava "Oh uh..well I'm *Ahem*."
    ava "Sore."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Sore? From what?"
    $ playerSprite = 14
    ava "...."
    $ avaSprite = 11 
    ava "From YOU. Thanks for letting me be subtle."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Ohhhh. Oh shit."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Yeah."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Sorry."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "But it's okay I've been resting since we...did it. And I should be good after today."
    $ avaSprite = 0
    $ playerSprite = 1
    player "What about tonight?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Tonight? Yeah I should be fine."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Another run at the park together then?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Uh yeah okay. I can do that."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Awesome see you then."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "See you later!"
    $ avaSprite = 0
    $ avaquestlog = "Another run with Ava tonight at the park!"
    
    $ avaphase3interaction1 = 1
    jump school

label avaphase3interaction1part2:
    hide screen uppergui
    $ avaSprite = 7
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.7)
    pause
    player "Hate to see you leave."
    $ avaSprite = 6
    show fbplayer shortsbonertalk:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    
    player "But love to see you walk away."
    show fbplayer shortsboner
    $ avaSprite = 3
    ava "Haha shut up you dork that's not even the situation for that."
    $ avaSprite = 2
    show fbplayer shortsbonertalk
    player "Close enough."
    player "Ready to run?"
    $ avaSprite = 3
    ava "Let's do it."
    scene fs avarun1
    with Dissolve(0.7)   
    "You run along the familiar park path with Ava once again"
    "The cool breeze was refreshing as it hit your skin"
    "You could hear Ava's rhythmic breath as she pulled away from you"
    scene fs avarun4
    with Dissolve(0.5)
    "But this time you caught up"
    scene fs avarun5
    with Dissolve(0.5)
    "And stayed there, right beside her"
    scene fs avarun4
    with Dissolve(0.5)
    pause
    scene fs parknight
    with Dissolve(0.7) 
    show fbplayer shortstired1:
        xalign 0.4 ypos 120
    $ avaSprite = 5
    show fbava current:
        xalign 0.6 ypos 120
    with Dissolve(0.7) 
    
    ava "Hah..dude!"
    ava "You did it!"
    player "I...hah."
    show fbplayer shortstired2
    player "Did it!"
    show fbplayer shortstired1
    ava "I'm so proud of you. Great job keeping up."
    show fbplayer shortstired2
    player "You...hah..didn't make it easy."
    ava "Nothing good in life ever is."
    show fbplayer shortstired1
    player "I dunno..hah..if true..can't think."
    ava "Haha let's go to your car, we can rest back at your place."
    player "Good idea."
    scene fs blackblank
    with Dissolve(0.7)
    "You drive you and Ava's sweaty bodies back to your place"
    scene fs avacouchprank2b
    player "Alright last chance if you want to shower first."
    scene fs avacouchprank2
    ava "I told you it's fine, I'll just shower at home."
    scene fs avacouchprank2b
    player "Kay. Looks like we won't be doing anything naughty then."
    player "No way I'm touching a nasty sweaty Tomboy."
    scene fs avacouchprank2
    ava "Oh I'm your Tomboy now?"
    scene fs avacouchprank2b
    player "Yup."
    play music "audio/showersounds.wav"
    "*Shower noises*"
    scene fs avacouchprank2
    ava "Heh."
    scene fs avacouchprank2b
    ava "..."
    scene fs avacouchprank3
    ava "Wait what does he mean he wouldn't touch me if I was sweaty?"
    ava "Is that a challenge??"
    ava "I bet a perv like him would get even more turned on!"
    ava "I'm gonna prove it!"
    scene fs avacouchprank3b
    ava "With just a little underboob and some 'innocent vulnerability'..."
    scene fs avacouchprank4
    ava "He won't be able to keep his hands off me!"
    scene fs blackblank
    with Dissolve(0.5)
    stop music fadeout 5
    "A little while later.."
    scene fs avacouchprank5
    with Dissolve(0.5)
    player "Hey I'm back, do you-oh?"
    player "Looks like she fell asleep."
    player "{i}Why is her top pulled up so much?{/i}"
    ava "*Obvious fake snoring*"
    player "{i}Ahhhhh she's not asleep. She must've got upset at my little joke.{/i}"
    player "{i}Let's have a little fun with her.{/i}"
    scene fs avacouchprank5b
    player "Damn Ava, sometimes I forget how fucking hot your body is."
    player "I don't normally do something like this but your tits have me rock hard."
    player "I have to jack off!"
    scene fs avacouchprank5
    ava "{i}Heh. I knew it!{/i}"
    scene fs avacouchprank5b
    player "Mmmm yeah, don't wake up baby stay just like that."
    player "I remember just how good your pussy felt. You're such a tight little slut."
    scene fs avacouchprank5
    ava "{i}I'm kinda getting a little wet from this..{/i}"
    scene fs avacouchprank5b
    player "Fuck I can feel it coming! I'm gonna cum all over your perfect tits!"
    scene fs avacouchprank5
    ava "{i}Yes!{/i}"
    scene fs avacouchprank5b
    player "Your pretty little face!"
    scene fs avacouchprank5
    ava "{i}Do it!{/i}"
    scene fs avacouchprank5b
    player "Your beautiful hair!"
    scene fs avacouchprank6
    with vpunch
    ava "NOT THE HAIR!!"
    scene fs avacouchprank7
    player "Hahahaha."
    ava "Huh??"
    player "Oh man, that reaction was perfect."
    ava "That's not funny!"
    scene fs avacouchprank8b
    with Dissolve(0.7)
    player "Aww c'mon babe."
    scene fs avacouchprank8
    ava "Hmph."
    scene fs avacouchprank8b
    player "Did my cute, tanned little tomboy get upset at my little prank?"
    scene fs avacouchprank8c
    ava "No."
    scene fs avacouchprank8b
    player "No?"
    scene fs avacouchprank8c
    ava "I'm not little."
    scene fs avacouchprank9
    player "*Kiss*"
    player "Of course not."
    player "I was teasing you but I really would fuck a post-workout Ava."
    scene fs avacouchprank9b
    ava "Y-You said I was stinky and sweaty!"
    scene fs avacouchprank10
    with Dissolve(0.5)
    player "Mmmm"
    player "Did I?"
    show avacouchfinger movie1
    player "Did I really?"
    ava "Ahn..."
    ava "No."
    player "You want me to make you cum?"
    ava "Yes."
    player "You really want me to?"
    ava "YES."
    player "Are you my cute little tomboy?!"
    scene fs avacouchprank11
    with vpunch
    ava "YESSS!!!"
    ava "Ahhhmygod."
    pause
    scene fs blackblank
    with Dissolve(0.7)
    ava "Hah...hah.."
    player "Ava?"
    ava "Mmm?"
    player "Do you want to go out on a date with me?"
    ava "Really dude?"
    player "Yeah."
    ava "I...yeah I-I'd like that *Ahem*."
    $ avaphase3interaction1 = 2
    $ avaquestlog = "No more content for Ava this version (Ch2.5)"
    jump overworldmap

label avaphase2whereshouldwemeetagain: # unused
    hide screen ava_atgym
    hide screen backbuttonGYM
    "MC asks ava where she'll be again"
    "Just somehwere at school in an empty room come find me"
    jump gym

label avaphase2whereshouldwemeetagain2: # unused
    "MC asks ava where she'll be again"
    "in the gym again, in the morning"
    jump classroom2


label avaphase2interaction1part3: # unused
    hide screen ava_atgym
    hide screen backbuttonGYM
    "mc goes to the gym again and josy is there as well as ava"
    "ava sees that josy is flirting with mc"
    "she asks him to help her out in the yoga room with an excercise"
    "crunch kisses scene happens"
    $ avaphase2interaction1 = 3
    jump passtime

label josysendsselfie: # unused
    "VVVVP"
    player "Huh? Josy just texted me."
    josy "{cps=25}Thanks again for the study sesh and the cum on our faces.{/cps}"
    player "Wow just straight up says it huh?"
    player "{cps=25}No problem. Thanks too?{/cps}"
    $ renpy.notify("Got Josy Selfie!")
    josy "{cps=25}Here's something to tide you over until our next one!{/cps}"
    player "She sent me a pic? I should check it out!"
    $ josyquestlog = "No more current content for Josy in this version (Ch2.0B)"
    $ josyscene1 = 3
    jump playerRoom

#------below is the part i wrote before going through the imatges properly
# I may incorporate them at some point (the watch)

label avaphase1interaction2part2: # unused
    hide screen ava_atgym
    hide screen gym_machine
    scene fs gymarea

    $ avaSprite = 2
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    ava "{i}Ugh [povname] is driving me nuts!{/i}"
    ava "{i}I mean seriously! I can't just straight up deal with him because he's dating Mia, she's the sweetest girl I know she'd be devastated finding out her boyfriend is...is being so sleezy.{/i}"
    ava "{i}On the other hand I can't deny..that..I-I like the attention..and the whole...wrongness of it all turns me on like a freaking light switch. I'd never let him know that though.{/i}"
    ava "{i}I don't know what I'm going to do if I don't stop this early on it might not end well..{/i}"

    show fbplayer current:
        xalign 0.3 ypos 120

    $ playerSprite = 1
    player "Hey there you are! What's up?"
    $ playerSprite = 0
    $ avaSprite = 1
    show fbava current at surpriseshake
    ava "GAH! Jesus! You're here. *Ahem*, like you said."
    $ avaSprite = 0
    $ playerSprite = 1
    player "So I thought of a good way to help us both work out."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Okay..."
    $ avaSprite = 0
    $ playerSprite = 1
    player "I want to try some cardio, it'll keep the calories down and you can use it to practice your running."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh okay, that's actually a good idea, we have some decent treadmills here."
    $ avaSprite = 0
    ava "{i}I dont think he can do anything dirty to me if it's just running, maybe he's finally serious?{/i}"
    $ playerSprite = 1
    player "Nah I don't want to use the treadmills, I'd rather just a natural running area outside, moving my legs and not going anywhere messes with my brain."
    player "Not to mention, you won't be using treadmills for your race at the track meet."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Oh uh yeah I guess that's true. Well I run around the park paths sometimes when it's nice out.."
    $ avaSprite = 0
    $ playerSprite = 1
    player "That's perfect! let's meet in the park at night for a run?"
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Yeah sure, I'll see you there [povname]."
    $ avaSprite = 0
    $ playerSprite = 1
    player "Can't wait."
    $ playerSprite = 0
    hide fbplayer current
    with Dissolve(1.0)
    ava "{i}Running outside with him? It seems like a good idea....{/i}"
    ava "{i}I mean there wouldn't be anyone around though.{/i}"
    ava "{i}Just the two of us at night...{/i}"
    ava "{i}Damn it the thought excites me a little, I'm terrible...{/i}"
    $ avaphase1interaction2 = 3
    hide fs gymarea
    hide fbava
    hide fbplayer
    jump passtime

label avaphase1interaction2part3: # unused
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    player "It's a bit dark but at least it's pretty warm, now where is Ava?"
    player "Ah there she is near the bench."

    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Sup."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Hey! Finally ready to get serious?"
    $ playerSprite = 1
    player "What do you mean? I was serious before too."
    $ playerSprite = 0
    $ avaSprite = 1
    ava "Um. Yeah of course."
    ava "Let's just run. You know proper breathing techniques right?"
    $ avaSprite = 0
    $ playerSprite = 1
    player "Proper what now?"
    $ playerSprite = 0
    scene fs avarun1
    "You starting jogging with Ava as she explains the correct way to breath and expend energy while you're running"
    "Even with her sports top on you could see her tits bouncing after each stride, which was pretty good motivation to keep up"
    scene fs avarun2
    with Dissolve(1.0)
    "Eventually you had to slow down, you told yourself it was so you could see her ass but you were just out of shape"
    scene fs avarun3
    "After some more time you were just lagging behind, but you never stopped and that was something."
    scene fs parknightZOOM
    show fbplayer shortstired1:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    ava "Hah...hah...we did it good job."
    $ playerSprite = 1
    player "Yeah no....no problem hah...."
    ava "Since this is your first run honestly I wasn't expecting you to keep up but I'm impressed."
    show fbplayer shortstired2:
        xalign 0.3 ypos 120
    player "Hey I gotta k..hah...keep you on your toes, can't let you slip up your practice."
    ava "Haha thanks, whenever I convinced one of the girls to run with me I always had to stop at least once."
    show fbplayer shortsboner:
        xalign 0.3 ypos 120
    player "{i}Nice I can see her clevage. This run was totally worth it.{/i}"
    ava "Man I'm sweating something fierce!"
    ava "Brrr I didn't notice it cause the run kept me warm but it's actually getting kinda cold out now..."
    show fbplayer shortsboner:
        xalign 0.5 ypos 120
    with move
    player "{i}Doth mine eyes deceive me? Her nipples are hard...{/i}"
    ava "{i}Why is he getting so close to me? I'm-{/i}"
    ava "{i}Oh my god my nipps are freaking hard as a rock! No wonder he looks so freaking horny.{/i}"
    ava "Um....ah..."
    player "Hmm?"
    ava "{i}He's looking at me...looking at my tits...his cock is probably hard right now..{/i}"
    player "You alright?"
    "YOU ARE HERE, this is avaphase1interaction2part3"
    ava "{i}His gaze is piercing right through me...he'd only do this if he thought I was hot right? W-Which means he wants to fuck me right?{/i}"
    ava "{i}E-Even though he's dating Mia he wants to fuck ME! Wants to to pound my pu-{/i}"
    player "AVA."
    ava "Huh? Oh sorry one..hah..sec..."
    $ avaSprite = 6
    player "What are you doing?"
    ava "Just s-some post run stretches."
    player "{i}is it just me or is she streching so I can see her tits better against her clothes?{/i}"
    $ avaSprite = 7
    ava "Ahhhnn..."
    player "{i}Well that pretty much answered my question.{/i}"
    ava "UHN....OOOhhh yeah that's good right theeeere..."
    player "{i}She's not even trying to hide it!{/i}"
    $ avaSprite = 8
    ava "Oh my god you...you have a boner!"
    show fbplayer shortsbonerlookdown:
        xalign 0.3 ypos 120
    player "Wha?"
    player "Oh."
    show fbplayer shortsboner:
        xalign 0.5 ypos 120
    player "Well if you're not going to be subtle why should I?"
    ava "What..What do you mean? I don't kno-"
    show fbplayer shortsbonerpoint:
        xalign 0.5 ypos 120
    player "You're one step away from cumming and all I've done is LOOK at you."
    ava "Fuck....you're right..I'm terrible. Jesus that thing is massive."
    player "Thank you. But Ava you need to relax, you're not terrible. We didn't even do anything."
    ava "...True."
    player "We're both really tired and horny so let's just go home for tonight hmm?"
    ava "Yeah that's a good idea."
    player "Thanks for running with me, it was a real pleasure."
    ava "Oh yeah I bet it was huh."
    player "I'm not taking it back, see yah!"
    hide fbplayer current
    with Dissolve(1.0)
    ava "{i}Haha man that guy....I definitely like him...{/i}"
    ava "{i}Why does he have to be Mia's boyfriend god dammit!{/i}"
    ava "{i}Wait...I swear I've had that thought before....{/i}"
    scene fs blackblank
    with Dissolve(1.0)
    "You go home and lie down, tired after running for so long"
    player "Man I'm exhausted but it was worth it, Ava's tits are amazing."
    player "They're not as big as Mia's but man do they have shape."
    player "She's actually was pretty cool about me perving on her. Even if it WAS her own fault."
    player "I should ask her to run again soon."
    $ avaphase1interaction2 = 4
    jump gotosleep

label avamorningletsrun: # unused
    scene fs schoolhallwayzoomblur
    with Dissolve(0.5)
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    player "Hey! Down to run again soon?"
    ava "Yeah just promise me no more messing around."
    player "What do you mean?"
    ava "You know what I mean c'mon! It was a little exciting but there's like fifty reasons we can't...you know."
    player "You got excited?"
    ava "Dude!"
    player "Okay okay I promise!"
    ava "I'll see you tonight."
    ava "Oh wait, hold off on that sorry!"
    player "Huh?"
    ava "I actually misplaced something I need before we run, can't go without it."
    player "Can't run without it?"
    ava "Yeah it's nothing, just come see me later at the gym and I'll let you know if we're good to go."
    player "Um yeah okay, anything I can do?"
    ava "No no it's cool, just stop by."
    player "Alright see you at the gym then."
    #$ avaphase1interaction2 = 5
    jump returnwhereyouare

# label avadaytimeletsrun:
#     scene fs gymarea
#     with Dissolve(0.5)
#     show fbplayer current:
#         xalign 0.3 ypos 120
#     with Dissolve(0.5)
#
#     show fbava current:
#         xalign 0.7 ypos 120
#     with Dissolve(0.5)
#
#     player "Hey! Down to run again soon?"
#     ava "Yeah just promise me no more messing around."
#     player "What do you mean?"
#     ava "You know what I mean c'mon! It was a little exciting but there's like fifty reasons we can't...you know."
#     player "You got excited?"
#     ava "Dude!"
#     player "Okay okay I promise!"
#     ava "I'll see you tonight."
#     jump returnwhereyouare

label avaseemsfocused: # unused
    player "Hmmm, Ava seems focused I don't think I want to mess with her right now."
    player "I'll come back another day after letting her know in the morning that I'm coming."
    jump returnwhereyouare

label avaphase1interaction2part4: # unused
    hide screen ava_atgym
    scene fs gymarea
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)

    show fbava defaultflip:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    ava "I told you It’s a black and fits around my wrist, it looks like a watch!"
    ava "No it’s not actually a watch but that doesn’t mat-"
    ava  "No I don’t know when-"
    ava  "Yes okay. Okay. OKAY!"
    ava "Alright thanks anyways, yeah love you too."
    ava "UGH!"

    show fbava current:
        xalign 0.7 ypos 120
    with Dissolve(0.3)
    player "Hey Ava, I don’t mean to pry but you look pretty upset about something. Can I help?"
    ava "What? Oh [povname]…I can’t deal with…with you right now sorry I don’t need the stress."
    player "Okay firstly ouch, secondly relax. I just want to help, I swear."
    ava "No stress!"
    player "No stress."
    ava "Hah..I can’t find my Fit Bitonator."
    player "Fit Bitonator?"
    ava "It’s been missing for about a week now and I thought I knew where it was but I checked where I thought it was and it wasn’t THERE and now I’m freaking out because I really need it cause it’s right before the meet and-"
    player "Hey slow down, what’s a fit bito..nator?"
    ava "It wraps around your wrist like a watch, but it keeps track of everything you need while you’re running, lap times, pulse rate, speed, acceleration."
    ava "It’s a must have tool if you’re working on keeping your heart rate at a steady pace for a long time. And it’s like freaking a hundred bucks and I LOST mine!"
    player "Is there anything I can do to help?"
    ava "No man I can’t even tell you where or when I last saw it, I just have to hope it pops up somewhere…"
    player "Do you really need this thing?"
    ava "It’s not…It’s not a necessity I mean, I don’t need it to run you know but…but there’s so much PRESSURE on me and I really need things to NOT fuck u-up a-a-a-and"
    player "Woah hey hey don’t cry it’s cool I’ll do something about it."
    ava "No don’t plea-"
    player "I WANT to help you with this, let me."
    ava "I know you’re up to something I’m not gonna f-fall for it!"
    player "Okay how about this, if you let me figure this out for you AND you win the race, I’ll give you a reward."
    ava "A reward?"
    player "A prize. For winning."
    ava "What is it?"
    player "A surprise. Until you win."
    ava "*sigh*…fine, it’s not like you’ll find it anyways."
    player "It’s a deal then. I’ll see you later."
    hide fbplayer default
    with Dissolve(0.5)
    ava "Curse my  hormones. I shouldn’t even be entertaining his ideas. "
    ava "Well he got me to stop crying and freaking out I guess…..And if he were to somehow find it…."
#    $ avaphase1interaction2 = 6
    $ timeofday = "Night"
    jump overworldmap
    #player can buy a new fit bitonator


label miaisnthome:
    hide screen julia_kitchen
    $ juliaSprite = 3
    show fbjulia current:
        xalign 0.5 ypos 120
    julia "Sorry handsome, Mia isn't home right now. Maybe call her tonight?"
    $ juliaSprite = 0
    jump gfhouse

label talkwithjulia:
    "I shouldn't bother Mia's mom right now."
    jump returnwhereyouare

label miaphase3interaction1part1:
    hide screen uppergui
    scene fs playerroomMorn
    with Dissolve(0.5)
    $ playerSprite = 4
    show fbplayer current:
        xalign 0.5 ypos 120
    player "...."
    player "It's time Mia."
    $ miaphase2interaction2 = 5
    $ miaphase3interaction1 = 1
    $ miaquestlog = "Finish the fight(Find Mia in her room)"
    jump playerlivingroom

label miaphase3interaction1part2:
    scene fs blackblank
    with Dissolve(0.7)
    katie "And then heeere's when we went bowling."
    sophia "Oh my God look at Josy haha!"
    emily "That's super cute."
    mia "Hehe."
    emily "Mia! Show us those 1st date pics you said you had!"
    katie "Oh yeah I've wanted to see those forever."
    mia "Haha okay, I haven't seen them myself since we took them."
    scene fs miaanal1
    with Dissolve(0.7)
    mia "Alrighty soooo.."
    scene fs miaanal2
    show selfieshare 1stdateselfie1:
        xalign 0.75 ypos 50
    mia "Here's us at the start."
    mia "He asked me out to a flower festival."
    scene fs miaanal3b
    show selfieshare 1stdateselfie1:
        xalign 0.75 ypos 50
    sophia "Aww!"
    katie "Very cute."
    emily "That's a great picture."
    scene fs miaanal1
    show selfieshare 1stdateselfie1:
        xalign 0.75 ypos 50
    mia "And then we walked around."
    scene fs miaanal2
    show selfieshare 1stdateselfie2:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal3b
    show selfieshare 1stdateselfie2:
        xalign 0.75 ypos 50
    emily "Oh my gosh."
    sophia "Ugh. You look so adorable."
    katie "Ugh this is way too sweet for me."
    scene fs miaanal1
    show selfieshare 1stdateselfie2:
        xalign 0.75 ypos 50
    mia "I don't remember what we did after."
    scene fs miaanal2
    show selfieshare 1stdateselfie3:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal3
    show selfieshare 1stdateselfie3:
        xalign 0.75 ypos 50
    pause
    katie "I have an idea or two."
    mia "T-That's yogurt!"
    katie "On the first date sis? Wow."
    emily "...."
    mia "It's YOGURT!"
    mia "Moving on!"
    scene fs miaanal4
    show selfieshare 1stdateselfie4:
        xalign 0.75 ypos 50
    pause
    "Everyone" "Awww!"
    mia "Oh yeah! We met Mr. Frog."
    sophia "I love Mr. Frog."
    katie "I'd die for Mr. Frog."
    mia "And then.."
    scene fs miaanal2
    show selfieshare 1stdateselfie5:
        xalign 0.75 ypos 50
    
    pause
    scene fs miaanal3b
    show selfieshare 1stdateselfie5:
        xalign 0.75 ypos 50
    sophia "Wooooow!"
    emily "This is a beautiful shot Mia."
    josy "This shit belongs in a movie, holy."
    mia "Aww thanks girls."
    scene fs miaanal2
    show selfieshare 1stdateselfie6:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal3
    show selfieshare 1stdateselfie6:
        xalign 0.75 ypos 50
    "!!!!"
    scene fs miaanal4b
    show selfieshare 1stdateselfie6:
        xalign 0.75 ypos 50

    katie "MIA!"
    emily "O-Oh my."
    sophia "Holy!"
    mia "N-No no no!"
    scene fs miaanal3c
    show selfieshare 1stdateselfie7:
        xalign 0.75 ypos 50
    pause
    scene fs miaanal4b
    show selfieshare 1stdateselfie7:
        xalign 0.75 ypos 50
    katie "MIA ON A FIRST DATE???!!!"
    mia "...."
    scene fs miaanal6
    pause
    scene fs miaanal7
    with Dissolve(0.7)
    pause
    mia "It wasn't yogurt."
    "...."
    player "*knock knock*"
    player "Oh, hey everyone!"
    scene fs miaanal5
    with vpunch
    "Everyone" "[povname]!"
    scene fs gfroom
    $ playerSprite = 0
    show fbplayer current:
        xalign 0.3 ypos 120
    show fbsophia current:
        xalign 0.4 ypos 120
    show fbkatie current:
        xalign 0.5 ypos 120
    show fbemily current:
        xalign 0.6 ypos 120
    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.7)
    pause
    $ playerSprite = 1
    player "Hey now, no need for you all to get up cause'a me."
    emily "No it's okay, we were just about to leave anyways."
    sophia "We were?"
    katie "Yah, were we?"
    emily "Yes of COURSE we were. Plus [povname] clearly came to visit Mia right?"
    player "Uh yeah."
    emily "So let's not bother them and let them get to it!"
    sophia "Ohhhh.."
    katie "Alright I was gonna meet up with Josy after this anyways, see yah everyone."
    hide fbkatie current
    emily "C'mon Sophia. Bye Mia!"
    mia "Bye!"
    hide fbemily current
    sophia "Ugh."
    hide fbsophia current
    player "Everyone left in a rush huh?"
    mia "*Ahem* Y-Yes. Seems they were busy."
    mia "You wanted to see me?"
    player "Ah yes. Very important."
    mia "Important?"
    player "Mia."
    player "Whisper whisper Anal whisper whisper."
    mia "W-What??!"
    player "Whisper whisper right now whisper."
    mia "R-Right now?"
    player "Please. We've already talked about it."
    mia "Why were you SAYING whisper?"
    player "Mia I love you with all my cock. I yearn for your body!"
    player "Let me make you feel good, in a new way."
    mia "Ohhh well...I mean...maybe we can try?"
    scene fs miaanal8
    with vpunch
    mia "Wha-How did you take off your clothes so fast?!"
    scene fs miaanal9
    player "Practice."
    scene fs miaanal8
    mia "And we don't even have lube! I'm not doing it without lu-"
    scene fs miaanal10
    "*Squirt*"
    scene fs miaanal8
    mia "Where di-Where did you get that?!"
    scene fs miaanal9
    player "We can go as slow as you need."
    scene fs miaanal8
    mia "...."
    scene fs miaanal11
    with Dissolve(0.5)
    mia "I swear the things you do to me..."
    scene fs miaanal14
    with Dissolve(0.7)
    player "There you go, now lift yourself up slowly."
    scene fs miaanal13
    with Dissolve(0.5)
    mia "Ehhh.."
    player "You're doing great babe keep going."
    scene fs miaanal12
    with Dissolve(0.5)
    player "Perfect, now slowly put it in, I'll hold you."
    mia "[povname] I-I don't think I'm ready for this I didn't think you'd actua-"
    scene fs miaanal15
    with vpunch
    mia "OHHHHH MAH GAWD."
    player "Fuck Fuck baby holy shit."
    mia "I slipped!"
    player "Yeah no kidding!"
    player "You're so tight baby oh my god."
    scene fs miaanal16
    with Dissolve(0.5)
    mia "Ohhhh!"
    scene fs miaanal17
    with Dissolve(0.5)
    player "Here baby let me help you."
    scene fs miaanal17b
    pause
    scene fs miaanal18
    mia "Oh that's...that's a little better."
    player "Let's lie down slowly."
    scene fs miaanal19
    with Dissolve(0.5)
    player "Mia your ass feels incredile."
    player "I'm so fucking hard."
    mia "I-I can tell!"
    show miatakingituptheass1
    pause
    mia "Oh..."
    mia "OH."
    player "Yeah baby that's it."
    mia "Ahn..."
    player "You're feeling good aren't you?"
    mia "NnNNyEaHHhhHHh..."
    player "C'mon baby."
    show miatakingituptheass2
    player "C'MON BABY!"
    mia "AHHH!"
    mia "[povname]!"
    mia "[povname] I'm gonna CUM!"
    scene fs miaanal21
    pause
    scene fs miaanal21b
    with vpunch
    mia "AHHHH!!!"
    player "FUCK!"
    scene fs blackblank
    with Dissolve(0.3)
    "A few moments earlier..."
    scene fs miaanal22
    with Dissolve(0.5)
    pause
    mia "AHHH!"
    scene fs miaanal23
    ava "Heeey girl I'm he-"
    mia "[povname] I'm gonna CUM!"
    scene fs miaanal24
    with vpunch
    mia "AHHHH!!!"
    player "FUCK!"
    pause
    ava "{i}Goddamn Mia, all that in your ass?{/i}"
    mia "Hah...hah."
    ava "{i}I should...come back later...{/i}"
    mia "Oh [povname]...Ahn.."
    player "You feel so good baby."
    mia "Feel...so full.."
    ava "{i}It'd be the polite thing to do.{/i}"
    scene fs miaanal22
    pause
    mia "Mmmm..."
    scene fs miaanal25
    play sound "audio/camerasnap.mp3"
    $ renpy.notify("Got Mia's 1st date pics!")
    $ phone_pictures.append("mia selfie1a")
    $ phone_pictures.append("mia selfie2")
    $ phone_pictures.append("mia selfie 3 flower")
    $ phone_pictures.append("mia selfies4")
    $ phone_pictures.append("mia selfies5")
    $ phone_pictures.append("mia selfies6")
    $ phone_pictures.append("mia selfies7")
    pause
    $ miaphase3interaction1 = 2
    $ miaquestlog = "No more solo content for Mia this version(Ch2.5)"
    jump passtime

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

#CHAPTER 3 EVENTS HERE-------------------------------------------------------------------------------------------------
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
    player "YOUR NOT MIA!!!"
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

label sleepwithmia:
    scene fs charlotteroom
    with Dissolve(1.0)
    show fbcharlotte pajama:
        xalign 0.4 ypos 120
    show fbava pajama:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    pause
    show fbmia pajama:
        xalign 0.6 ypos 120
    show fbsophia pajama:
        xalign 0.7 ypos 120
    with Dissolve(0.5)
    pause
    show fbolivia pajama:
        xalign 0.9 ypos 120
    show fbemily pajama:
        xalign 1.0 ypos 120
    show fbplayer pajama:
        xalign 0.1 ypos 120
    with Dissolve(0.5)
    pause
    show fbemily pajamatalk:
        xalign 1.0 ypos 120
    emily "Okay! *Yawn* Where's everyone sleeping?"
    show fbemily pajama:
        xalign 1.0 ypos 120
    show fbplayer pajamatalk:
        xalign 0.1 ypos 120
    player "Well I think Charlotte should get the bed, how many can fit on it?"
    show fbplayer pajama:
        xalign 0.1 ypos 120
    show fbcharlotte pajamatalk:
        xalign 0.4 ypos 120
    charlotte "Thank you [povname]. It can fit four."
    show fbcharlotte pajama:
        xalign 0.4 ypos 120
    show fbmia pajamatalk:
        xalign 0.6 ypos 120
    mia "I don't care as long as I can sleep next to [povname]."
    show fbmia pajama:
        xalign 0.6 ypos 120
    show fbplayer pajamatalk:
        xalign 0.1 ypos 120
    player "Babe I don't think any of our sleeping bags can fit both of us."
    show fbplayer pajama:
        xalign 0.1 ypos 120
    show fbava pajamatalk:
        xalign 0.3 ypos 120
    ava "Fine, you two also get the bed. Who's last?"
    show fbava pajama:
        xalign 0.3 ypos 120
    show fbolivia pajamatalk:
        xalign 0.9 ypos 120
    olivia "Emily should."
    show fbolivia pajama:
        xalign 0.9 ypos 120
    show fbemily pajamatalk:
        xalign 1.0 ypos 120
    emily "Me? No it's okay Sophia how abou-"
    show fbemily pajama:
        xalign 1.0 ypos 120
    show fbsophia pajamatalk:
        xalign 0.7 ypos 120
    sophia "It's fine Emily, I'm so tired it really doesn't matter to me right now."
    show fbsophia pajama:
        xalign 0.7 ypos 120
    show fbemily pajamatalk:
        xalign 1.0 ypos 120
    emily "Okay then! Thanks guys."
    show fbemily pajama:
        xalign 1.0 ypos 120
    
    scene fs sleepoverbedpovmia
    with Dissolve(1.0)
    pause
    "Most of the girls fell asleep even with the strong moonlight bursting through the windows"
    "But surrounded by all these beautiful girls kept your mind wandering, and your sleep restless.."
    scene fs groupbedsex3
    with Dissolve(0.7)
    pause
    scene fs groupbedsex3b
    with Dissolve(0.5)
    pause
    emily "*Snore*"        
    scene fs groupbedmiasex1
    pause
    scene fs groupbedmiasex1b 
    pause
    scene fs groupbedmiasex1c 
    pause
    scene fs groupbedmiasex2
    mia "Hmm?"
    scene fs groupbedmiasex2b 
    mia "..."
    player "..."
    scene fs groupbedmiasex2c 
    mia "Hehehe."
    scene fs groupbedmiasex3
    pause
    scene fs groupbedmiasex4
    mia "!!!"
    scene fs groupbedmiasex4b
    player "Try not to make any noise."
    scene fs groupbedmiasex5
    pause
    scene fs groupbedmiasex6
    mia "Ah!"
    mia "I don't know...if I can do that."
    scene fs groupbedmiasex7 
    mia "Mmm!"
    player "Auhn.."
    scene fs groupbedmiasex8 
    with Dissolve(0.7)
    pause
    scene fs groupbedmiasex9
    with Dissolve(0.7)
    pause
    scene fs groupbedmiasex10 
    player "Don't cover your mouth."
    mia "But what if they hear me? What if they wake up?"
    player "Good."
    scene fs groupbedmiasex11
    pause
    scene fs groupbedmiasex11b
    mia "Ehnnn!"
    scene fs groupbedmiasex122
    with Dissolve(0.5)
    mia "Hah..."
    scene fs groupbedmiasex12b
    with vpunch
    mia "Ahn!"
    scene fs groupbedmiasex122
    with Dissolve(0.3)
    mia "Oh.."
    scene fs groupbedmiasex12b
    with vpunch 
    mia "AHN!"
    scene fs groupbedmiasex13
    mia "Hah..hah.."
    player "You like that baby?"
    scene fs groupbedmiasex13b
    mia "Yes!"
    player "You like it when I fuck you next to your friends?"
    scene fs groupbedmiasex13b2
    mia "I love it hehehe!"
    scene fs groupbedmiasex122
    with Dissolve(0.5)
    player "Take this fat fucking cock!"
    scene fs groupbedmiasex12b
    with vpunch
    mia "[povname]!"
    scene fs groupbedmiasex14
    with Dissolve(0.7)
    mia "[povname] I'm gonna cum!"
    player "Cum with me baby, let me fill you up!"
    mia "Please! Please!"
    pause
    scene fs groupbedmiasex122
    with Dissolve(0.5)
    player "What do you want?!"
    mia "I want you to cum inside me while everyone listens!"
    scene fs groupbedmiasex12b
    with vpunch
    player "AHHHGH!"
    mia "YES!!!"
    pause
    scene fs groupbedmiasex12c
    with Dissolve(0.7)
    pause
    scene fs blackblank
    with Dissolve (1.0)
    "The night passed by quickly for you and Mia, not so much for everyone else"
    "In the morning everyone was cordial but you noticed a lack of sleep in the girls eyes"
    "You said your goodbyes and headed back home"
    jump passtime

    scene fs groupbedsex1
    pause
    scene fs groupbedsex1b
    pause
    scene fs groupbedsex2
    pause
    scene fs groupbedsex2b
    pause
    scene fs groupbedsex3
    pause
    scene fs groupbedsex3b
    pause
    scene fs groupbedsex4
    pause
    scene fs groupbedsex4b
    pause
    scene fs groupbedsex5
    pause
    scene fs groupbedsex5b
    pause
    scene fs groupbedsex6
    pause
    scene fs groupbedsex6b
    pause

    scene fs groupbedmiasex1
    pause
    scene fs groupbedmiasex1b 
    pause
    scene fs groupbedmiasex1c 
    pause
    scene fs groupbedmiasex2
    pause
    scene fs groupbedmiasex2b 
    pause
    scene fs groupbedmiasex2c 
    pause
    scene fs groupbedmiasex3
    pause
    scene fs groupbedmiasex4
    pause
    scene fs groupbedmiasex4b
    pause
    scene fs groupbedmiasex5
    pause
    scene fs groupbedmiasex6
    pause
    scene fs groupbedmiasex7 
    pause
    scene fs groupbedmiasex8 
    pause
    scene fs groupbedmiasex9
    pause
    scene fs groupbedmiasex10 
    pause
    scene fs groupbedmiasex11
    pause
    scene fs groupbedmiasex11b
    pause
    scene fs groupbedmiasex12
    pause
    scene fs groupbedmiasex122 
    pause
    scene fs groupbedmiasex12b 
    pause
    scene fs groupbedmiasex12c
    pause
    scene fs groupbedmiasex13
    pause
    scene fs groupbedmiasex13b
    pause
    scene fs groupbedmiasex13b2
    pause
    scene fs groupbedmiasex14
    pause

    jump passtime

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

    #voice "audio/miagameaudio/miahehe.wav"
    mia "Woohoo!"
    #hide fbmia
    #show fbmia current:
    #    xalign 0.5 ypos 120
    #$ miaSprite = 14
    show fbcharlotte current:
        xalign 0.6 ypos 120
    #voice "audio/charlottegameaudio/charlotteugh.wav"
    charlotte "Finally."
    $ charlotteSprite = 14
    $ avaSprite = 23
    show fbava current behind fbmia:
        xalign 0.4 ypos 120
    #voice "audio/avagameaudio/avagiggle.wav"
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

label charlottebeachchapter2end:
    hide screen mia_beach1
    hide screen mia_beach2
    hide screen mia_beach3
    hide screen sophia_beach
    hide screen charlotte_beach
    hide screen ava_beach
    hide screen emily_beach
    hide screen olivia_beach
    hide screen backbuttonBEACH

    scene fs charlottechapter2end1
    with Dissolve(0.7)
    player "Charlotte hey!"
    charlotte "Mmmm."
    player "Mind if I join you?"
    scene fs charlottechapter2end1b
    charlotte "Sure."
    scene fs charlottechapter2end2
    with Dissolve(0.5)
    player "Ahhh. Oh this is relaxing!"
    charlotte "Yup."
    scene fs charlottechapter2end3
    player "Crazy how little people there are here."
    player "Usually whenever I pass by there's tons!"
    charlotte "S'cause I rented the place out."
    player "Wait you did? You can RENT a beach?!"
    charlotte "If you pay enough. I didn't want us to be bothered by other people."
    player "Wow Charlotte. New found respect I gotta say!"
    charlotte "Mmhmm. Now if you quiet down we might actually enjoy my rented beach."
    player "Haha sorry."
    #$ charlottephase2interaction3 = 2
    if charlottephase2interaction3 >= 2:
        "Would you like to end the day with Charlotte?"
        menu:
            "Romance":
                jump charlottechapter2romance
            "Naughty":
                jump charlottechapter2naughty
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach
    
    label charlottechapter2romance:
        scene fs charlottechapter2end2
        player "Mmmmm."
        charlotte "...."
        scene fs charlottechapter2end3
        player "It's pretty hot out, I'm gonna find something to drink, would you like anything?"
        charlotte "A drink?"
        player "Yeah?"
        scene fs charlottechapter2end4
        pause
        "Charlotte's phone" "Beep boop boop"
        player "Huh? What're you doing?"
        charlotte "...."
        player "Alright keep your secrets geez"
        scene fs charlottechapter2end2
        with Dissolve(0.5)
        player "...."
        victoria "Miss Charlotte."
        charlotte "You're here Vicky."
        scene fs charlottechapter2end5
        with Dissolve(0.5)
        player "Wait what? Victoria??"
        victoria "Hello Master [povname]."
        player "But how did..."
        player "And your swimsuit!"
        player "I..."
        player "{i}God damn! This woman is a ninja!{/i}"
        player "{i}A big titted...maid bikini wearing...red-headed sexy ninja..{/i}"
        scene fs charlottechapter2end6b
        with Dissolve(0.5)
        victoria "And for you as well. Miss Charlotte asked me to bring you a glass."
        scene fs charlottechapter2end6
        player "Oh uh...thanks so much Charlotte.."
        charlotte "Yup."
        scene fs charlottechapter2end6b
        player "{i}Clevage! Maid Bikini clevage!{/i}"
        scene fs charlottechapter2end6c
        with Dissolve(0.7)
        victoria "Hehe, I see you're happy to see me."
        victoria "I should go though, in case I'm needed elsewhere."
        scene fs charlottechapter2end6c
        player "Sure yeah no problem..."
        scene fs charlottechapter2end7b
        with Dissolve(0.5)
        player "Thanks again Charlotte, this looks really good!"
        scene fs charlottechapter2end7
        charlotte "You're welcome, now shut up and drink it."
        scene fs charlottechapter2end8
        "Clink!"
        player "Yes ma'am."
        scene fs charlottechapter2end9
        pause
        charlotte "Siiiiip"
        player "Siiiiip"
        charlotte "{i}Is that what I think it is?{/i}"
        scene fs charlottechapter2end10
        with Dissolve(0.7)
        charlotte "{i}He's got a huge hard on right now!{/i}"
        charlotte "...."
        pause
        scene fs charlottechapter2end9
        charlotte "Ahem. Um [povname]?"
        player "Hmm?"
        charlotte "As you can tell I'm feeling generous today."
        player "Yeah it's great!"
        scene fs blackblank
        with Dissolve(1.0)
        charlotte "....Meet me in the 2nd girls shower stall in 5 minutes."
        player "Uh...okay sure?"
        charlotte "Don't bother bringing your clothes."
        player "{i}Holy shit...{/i}"
        stop sound
        play music "audio/showersounds.wav" fadein 5
        scene fs charlottechapter2end11
        with Dissolve(0.7)    
        pause
        charlotte "{i}I'm just taking control of my lust. That's all...yeah..{/i}"
        scene fs charlottechapter2end11b
        with Dissolve(0.5)
        player "Hey."
        scene fs charlottechapter2end11c
        pause
        charlotte "{i}Everytime I see this thing I'm surprised. How did it fit inside me?{/i}"
        player "Do you want me to-"
        scene fs charlottechapter2end12c
        charlotte "No."
        charlotte "J-Just....don't talk."
        scene fs charlottechapter2end12
        pause
        scene fs charlottechapter2end12b
        pause
        scene fs charlottechapter2end12c
        charlotte "You...you're really hard."
        player "Yeah...don't stop."
        scene fs charlottechapter2end12
        pause
        scene fs charlottechapter2end12b
        pause
        show rs avashowersright
        with Dissolve(0.5)
        ava "Mmmmm..."
        show ls miashowersleft
        with Dissolve(0.5)
        mia "*whistles*"
        show fs charlottechapter2end13
        player "Ahhh..That feels really good."
        show fs charlottechapter2end13b
        player "Yeah.."
        charlotte "{i}H-His hand is around my neck! Why does that turn me on so much?{/i}"
        charlotte '{i}And did I hear people beside us?{/i}'
        show fs charlottechapter2end13c
        charlotte "Uhn..."
        scene fs charlottechapter2end14
        with Dissolve(0.7)
        player "Charlotte..."
        player "You're so fucking beautiful."
        show fs charlottechapter2end15
        with Dissolve(0.7)
        charlotte "I..."
        charlotte "Thank you."
        player "I want to touch every inch of your body."
        scene fs charlottechapter2end16
        with Dissolve(0.7)
        charlotte "Ah..."
        ava "Hmm? Did someone say something?"

        scene fs charlottechapter2end17
        with Dissolve(0.7)
        mia "Huh? Ava?"
        charlotte "{size=20}Mia and Ava are beside us!{/size}"
        scene fs charlottechapter2end18
        with Dissolve(0.7)
        ava "I thought I heard something sorry."
        player "{size=20}You better be quiet then.{/size}"
        scene fs charlottechapter2end19
        with Dissolve(0.7)
        charlotte "Uhhh..."
        scene fs charlottechapter2end20
        charlotte "Oh god!"
        scene fs charlottechapter2end21
        charlotte "{i}Why am I doing this?{/i}"
        charlotte "{i}Am I just desperate for any attention?{/i}"
        charlotte "{i}Or am I....f..falling in..{/i}"
        player "Get ready."
        charlotte "Huh?"
        
        show charlottebeachsex movie1
        charlotte "Uhn uhn uhn!"
        charlotte "{i}It's good it's so good!{/i}"
        pause
        show charlottebeachsex movie2
        charlotte "AHH!!"
        ava "Okay now I KNOW I heard something."
        charlotte "G-God...FUUCK!!!"
        mia "Is that...Charlotte?"
        charlotte "YEESSS!!!"
        ava "Are you okay?"
        pause
        scene fs blackblank
        with Dissolve(0.7)
        "A few minutes later.."
        scene fs charlottechapter2end22
        charlotte "Hey."
        scene fs charlottechapter2end25
        ava "Don't hey us, what the hell was that? You got a guy in there?"
        scene fs charlottechapter2end22b
        charlotte "Don't be ridiculous."
        scene fs charlottechapter2end23
        charlotte "I got stung by a Jellyfish, I was just pulling out the little stinger thingies."
        scene fs charlottechapter2end26
        mia "Really? It sounded like you were...in distress?"
        scene fs charlottechapter2end22b
        charlotte "I was! It freaking hurt."
        charlotte "You guys are being silly, you really think I was having sex with some random guy I picked up from the beach?"
        scene fs charlottechapter2end27
        with Dissolve(0.7)
        ava "Hmmm."
        mia "Hmmm."
        scene fs charlottechapter2end22
        charlotte "Hmph."
        scene fs charlottechapter2end22b
        charlotte "Can we get dressed now or are we going to stand around naked all day?"
        with Dissolve(0.5)
        
        scene fs blackblank
        with Dissolve(0.7)
        ava "Alright whatever, keep your mystery man a mystery."
        mia "Haha."
        charlotte "I'm telling you there's no mystery man!"
        $ charlottequestlog = "Started off rocky, but I really like Charlotte now. Guess sex will do that. She at school?"
        $ endchapter2_trigger = "2 charlotte romantic"
        jump startofchapter3

    label charlottechapter2naughty:
        scene fs charlottechapter2end2
        player "Mmmmm."
        charlotte "...."
        scene fs charlottechapter2end3
        player "It's pretty hot out, I'm gonna find something to drink, would you like anything?"
        charlotte "A drink?"
        player "Yeah?"
        scene fs charlottechapter2end4
        pause
        "Charlotte's phone" "Beep boop boop"
        player "Huh? What're you doing?"
        charlotte "...."
        player "Alright keep your secrets geez"
        scene fs charlottechapter2end2
        with Dissolve(0.5)
        player "...."
        victoria "Miss Charlotte."
        charlotte "You're here Vicky."
        scene fs charlottechapter2end5
        with Dissolve(0.5)
        player "Wait what? Victoria??"
        victoria "Hello Master [povname]."
        player "But how did..."
        player "And your swimsuit!"
        player "I..."
        player "{i}Holy shit never mind where she came from, what is she wearing?!{/i}"
        player "{i}It's some sort of sexy maid bikini{/i}"
        scene fs charlottechapter2end6b
        with Dissolve(0.5)
        victoria "And for you as well. Miss Charlotte asked me to bring you a glass."
        scene fs charlottechapter2end6
        player "Oh uh...thanks so much Charlotte.."
        charlotte "Yup."
        scene fs charlottechapter2end6b
        player "{i}Victoria's got some nice fucking tits.{/i}"
        scene fs charlottechapter2end6c
        with Dissolve(0.7)
        victoria "Hehe, I see you're happy to see me."
        victoria "I should go though, in case I'm needed elsewhere."
        scene fs charlottechapter2end6c
        player "Sure yeah no problem..."
        scene fs charlottechapter2end7b
        with Dissolve(0.5)
        player "Thanks again Charlotte, this looks really good!"
        scene fs charlottechapter2end7
        charlotte "You're welcome, now shut up and drink it."
        scene fs charlottechapter2end8
        "Clink!"
        player "Yes ma'am."
        scene fs charlottechapter2end9
        pause
        charlotte "Siiiiip"
        player "Siiiiip"
        charlotte "{i}Is that what I think it is?{/i}"
        scene fs charlottechapter2end10
        with Dissolve(0.7)
        charlotte "{i}He's got a huge hard on right now!{/i}"
        charlotte "...."
        pause
        scene fs charlottechapter2end9
        charlotte "Ahem. Um [povname]?"
        player "Hmm?"
        charlotte "As you can tell I'm feeling generous today."
        player "Yeah?"
        scene fs blackblank
        with Dissolve(1.0)
        charlotte "Maybe we should...go somewhere private."
        player "Ah, you saw my boner and want to fuck."
        charlotte "H-Hey! No I'm just...in the mood."
        player "Don't worry princess, I'll give you what you want."
        stop sound
        play music "audio/showersounds.wav" fadein 5
        scene fs charlottechapter2end11
        with Dissolve(0.7)
        pause
        charlotte "{i}I'm just taking control of my lust. That's all...yeah..{/i}"
        scene fs charlottechapter2end11b
        with Dissolve(0.5)
        player "Hey."
        scene fs charlottechapter2end11c
        pause
        charlotte "{i}Everytime I see this thing I'm surprised. How did it fit inside me?{/i}"
        player "Go ahead."
        scene fs charlottechapter2end12c
        charlotte "I-I don't need your permission!"
        scene fs charlottechapter2end12
        pause
        scene fs charlottechapter2end12b
        pause
        scene fs charlottechapter2end12c
        charlotte "You...you're really hard."
        player "Yeah...don't stop."
        scene fs charlottechapter2end12
        pause
        scene fs charlottechapter2end12b
        pause
        show rs avashowersright
        with Dissolve(0.5)
        ava "Mmmmm..."
        show ls miashowersleft
        with Dissolve(0.5)
        mia "*whistles*"
        show fs charlottechapter2end13
        player "Ahhh..That feels really good."
        show fs charlottechapter2end13b
        player "Yeah.."
        charlotte "{i}H-His hand is around my neck! Why does that turn me on so much?{/i}"
        charlotte '{i}And did I hear people beside us?{/i}'
        show fs charlottechapter2end13c
        charlotte "Uhn..."
        scene fs charlottechapter2end14
        with Dissolve(0.7)
        player "Let me have a good look at you."
        show fs charlottechapter2end15
        with Dissolve(0.7)
        pause
        scene fs charlottechapter2end16
        with Dissolve(0.7)
        charlotte "Ahn..."
        mia "Huh?"
        scene fs charlottechapter2end17
        with Dissolve(0.7)
        charlotte "{size=20}Mia and Ava are beside us!{/size}"
        scene fs charlottechapter2end18
        with Dissolve(0.7)
        mia "Did you hear something Ava?"
        ava "I thought I did, I dunno though sorry."
        player "{size=20}You better be quiet then.{/size}"
        scene fs charlottechapter2end19
        with Dissolve(0.7)
        charlotte "Uhhh..."
        scene fs charlottechapter2end20
        charlotte "Oh god!"
        scene fs charlottechapter2end21
        charlotte "{i}Why am I doing this?{/i}"
        charlotte "{i}Am I just desperate for any attention?{/i}"
        charlotte "{i}This is wrong! Mia's RIGHT THERE!{/i}"
        player "Get ready."
        charlotte "Huh?"
        
        show charlottebeachsex movie1
        charlotte "Uhn uhn uhn!"
        charlotte "{i}It's good it's so good!{/i}"
        player "{size=20}Does it feel good fucking your best friend's boyfriend right beside her?{/size}"
        pause
        show charlottebeachsex movie2
        charlotte "AHH! N-No!"
        ava "Okay now I KNOW I heard something."
        player "{size=20}I can feel you getting tighter Charlotte, I know how much of a slut you are!{/size}"
        charlotte "G-God...FUUCK!!!"
        mia "Is that...Charlotte?"
        charlotte "YEESSS!!!"
        ava "Are you okay?"
        mia "Let's meet outside.."
        charlotte "I'm cumming!!"
        pause
        scene fs blackblank
        with Dissolve(0.7)
        "A few minutes later.."
        scene fs charlottechapter2end22b
        charlotte "Hey."
        scene fs charlottechapter2end25
        ava "Don't hey us, what the hell was that? You got a guy in there?"
        scene fs charlottechapter2end22b
        charlotte "Don't be ridiculous."
        charlotte "I got stung by a Jellyfish, I was just pulling out the little stinger thingies."
        scene fs charlottechapter2end26
        mia "Really? It sounded like you were...in distress?"
        scene fs charlottechapter2end22b
        charlotte "I was! It freaking hurt."
        scene fs charlottechapter2end25
        ava "You're sure you weren't with a guy in there?"
        scene fs charlottechapter2end24
        charlotte "What guy would I even be with? Think about it."
        scene fs charlottechapter2end27
        with Dissolve(0.5)
        mia "Hmmm."
        ava "Hmmm."
        scene fs charlottechapter2end28
        with Dissolve(0.5)
        charlotte "...." 
        scene fs charlottechapter2end22b
        charlotte "*A-Ahem*. Are we gonna get dressed or stand around naked all day?"
        
        scene fs blackblank
        with Dissolve(0.7)
        ava "Alright whatever, keep your mystery man a mystery."
        mia "Haha."
        charlotte "I'm telling you there's no mystery man!"
        stop music fadeout 5
        $ endchapter2_trigger = "2 charlotte naughty"
        $ charlottequestlog = "Started off rocky, but I really like Charlotte now. Guess sex will do that. She at school?"
        jump startofchapter3

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
    #$ oliviaphase2interaction3 = 1
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

label avabeachchapter2end:
    #"test ava"
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
    $ playerSprite = 19
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbava current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    player "Ava!"
    $ avaSprite = 23
    $ playerSprite = 18
    ava "[povname]! Just the man I was looking for."
    $ avaSprite = 22
    $ playerSprite = 19
    player "Haha, looking for me?"
    $ playerSprite = 18
    $ avaSprite = 23
    ava "Uh huh, time for some good ol' fasion competition!"
    $ avaSprite = 22
    $ playerSprite = 19
    player "What, the volleyball game wasn't enough?"
    $ playerSprite = 18
    $ avaSprite = 23
    ava "Not even close!"
    $ avaSprite = 22
    $ playerSprite = 19
    player "Alright then, what are we doing?"
    $ playerSprite = 18
    $ avaSprite = 23
    ava "Everything!"
    $ avaSprite = 22
    $ playerSprite = 19
    player "Bring it on!"
    scene fs blackblank
    with Dissolve(0.7)
    "Ava and I then started to compete in every beach themed game you could think of"
    scene fs avabeachfun1
    with Dissolve(0.7)
    pause
    scene fs avabeachfun2
    ava "21!"
    "And some, not so beach themed"
    scene fs avabeachfun3
    player "Feeling tired yet?"
    scene fs avabeachfun2
    ava "You wish!"
    scene fs avabeachfun4
    sophia "C'mon guys keep going you can do it!"
    charlotte "Why am I here?"
    scene fs avabeachfun1
    pause
    scene fs avabeachfun2
    ava "22!"
    scene fs avabeachfun5
    with Dissolve(1.0)
    olivia "Grrrr!"
    ava "Haha c'mon Olivia, show me that gamer girl strength!"
    sophia "This...hah..doesn't even make sense!"
    sophia "Why am I the one on the bottom??!"
    scene fs blackblank
    with Dissolve(1.0)
    "It was a lot of fun!"
    #"[avaphase2interaction3]"
    if avaphase2interaction3 >= 2:
        "Would you like to end the day with Ava?"
        menu:
            "Romance":
                jump avachapter2romance
            "Naughty":
                jump avachapter2naughty
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach
    
    label avachapter2romance:
        scene fs beachpictureempty
        with Dissolve(1.0)
        show fbplayer current:
            xalign 0.4 ypos 120
        show fbava current:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        player "Well..hah..seems like we tied?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Yeah haha."
        ava "I think I tied more though."
        $ avaSprite = 22
        $ playerSprite = 19
        player "What does that even mean lol?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Did you just lol?"
        $ avaSprite = 22
        player "..."
        $ avaSprite = 23
        ava "Moving so much did work up a good sweat, and it's getting later in the day."
        $ avaSprite = 22
        $ playerSprite = 19
        player "Yeah for sure. You...feeling dirty?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "I could really use a shower."
        $ avaSprite = 22
        $ playerSprite = 19
        show fbplayer current:
            xalign 0.55 ypos 120
        with move
        player "A dirty...tomboy shower?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Hahaha dude what the hell?"
        $ avaSprite = 22
        $ playerSprite = 19
        player "Haha sorry."
        $ playerSprite = 18
        ava "...."
        $ avaSprite = 23
        show fbava current:
            xzoom -1.0
        ava "C'mon. I need your cock inside me right now."
        $ playerSprite = 20
        player "Oh shit...uh.."
        player "Yes ma'am."
        pause
        show avabeachsex movie2
        ava "Hah hah hah.."
        player "Fuck you're tight!"
        ava "And you're so FUCKING big!"
        scene fs avabeachsex4
        with Dissolve(0.5)
        ava "Doing it in the shower is so HOT!"
        show rs oliviashowerright
        with Dissolve(0.7)
        player "You really like this huh?"
        show ls sophiashowerleft
        with Dissolve(0.7)
        ava "Feels so fucking good!"
        show rs oliviashowerlook
        ava "GOD dude. I want to marry your dick!"
        olivia "Huh?"
        ava "You better not pull out!"
        show ls sophiashowerlook
        sophia "Hmm?"
        olivia "Ava?"
        show fs avabeachsex6 behind ls 
        with vpunch
        ava "Ah!"
        ava "Uh yeah?"
        show avabeachsex movie2
        olivia "You okay?"
        ava "Y-Yeah! Ahn!"
        sophia "You sound kinda weird.."
        
        scene fs avabeachsex5
        show ls sophiashowerlook
        show rs oliviashowerlook
        with Dissolve(0.5)
        ava "Oh my god! N-No I'm F-"
        ava "FUCK!"
        sophia "Do you need help?"
        olivia "I think we should open the d-"
        show avabeachsex movie2
        ava "N-No!"
        ava "T-The truth is there's a guy in here!"
        olivia "Ohhhh..."
        sophia "What?"
        ava "There's a guy in here w-AHN! With me. We're having s-SEX!"
        ava "God I'm gonna fucking cum!"
        sophia "Ohmygod. Uh okay sorry."
        show avabeachsex movie3
        ava "FUCK YES YES AHN!!!"
        player "UGGGH!!"
        scene fs avabeachsex3
        with Dissolve(1.0)
        ava "God I feel it..I feel it spilling out..."
        sophia "Oooookay."
        olivia "Haha, okay enjoy then, we'll get out first"
        scene fs blackblank
        with Dissolve(1.0)
        $ avaquestlog = "Can't believe someone saw Ava and I in the locker room. I should see her at the gym again."
        $ endchapter2_trigger = "2 ava romantic"
        jump startofchapter3

    label avachapter2naughty:
        scene fs beachpictureempty
        with Dissolve(1.0)
        $ playerSprite = 19
        show fbplayer current:
            xalign 0.4 ypos 120
        show fbava current:
            xalign 0.6 ypos 120
        with Dissolve(0.7)
        player "Well..hah..seems like we tied?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Yeah haha."
        ava "I think I tied more though."
        $ avaSprite = 22
        $ playerSprite = 19
        player "What does that even mean lol?"
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Did you just lol?"
        $ avaSprite = 22
        player "..."
        $ avaSprite = 23
        ava "Moving so much did work up a good sweat, and it's getting later in the day."
        $ avaSprite = 22
        $ playerSprite = 19
        player "Let's go to the shower then."
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Huh?"
        $ avaSprite = 22
        $ playerSprite = 19
        player "Let's go hit the showers. Together."
        $ playerSprite = 18
        $ avaSprite = 23
        ava "Oh."
        $ avaSprite = 22
        $ playerSprite = 19
        player "I'm not giving you a choice."
        $ playerSprite = 18
        ava "...."
        show fbplayer current:
            xalign 0.7 ypos 120
        with move
        $ playerSprite = 19
        player "{size=20}I'm gonna pound your tight fucking pussy while all your friends have no idea.{/size}"
        $ playerSprite = 18
        ava "Y-Yes please."
        pause
        scene fs blackblank
        with Dissolve(0.5)
        "A little later on..."
        scene fs avabeachsex1
        with Dissolve(1.0)
        player "Tell me what you it."
        ava "I-I want it!"
        scene fs avabeachsex2
        ava "O-Oooohhh..."
        show avabeachsex movie1
        player "Mmmh yeah nice and slow."
        player "That's how you like it right?"
        ava "Uhn...N-No.."
        player "Soft...safe...boring.."
        pause
        scene fs avabeachsex4
        with Dissolve(0.5)
        ava "M-More.."
        show rs oliviashowerright
        with Dissolve(0.5)
        olivia "*Hums*"
        player "What was that? I can't hear you."
        show ls sophiashowerleft
        with Dissolve(0.5)
        sophia "Dum de dum"
        ava "H...HARDER!"
        player "Beg me."
        ava "Please! Please pound my fucking pussy!"
        show rs oliviashowerlook
        olivia "What the hell?"
        show ls sophiashowerlook
        sophia "Huh??"
        show avabeachsex movie2
        ava "AHN!!!"
        olivia "Ava? Is that you?"
        ava "Oh G-God!"
        ava "Olivia??"
        sophia "Ava are you okay?"
        ava "So-AHN! Sophia?"
        ava "What are you guys doing here?"
        sophia "Uhhh taking a shower?"
        player "{size=20}Don't let them know Ava.{/size}"
        ava "F-Fuck!"
        player "{size=20}Don't let them know you're fucking your friend's boyfriend right next to them.{/size}"
        ava "P-Please..."
        scene fs avabeachsex5
        show rs oliviashowerlook
        show ls sophiashowerlook
        with Dissolve(0.5)
        ava "GGGHHH!!"
        olivia "Are you okay?"
        ava "{i}Fuck fuck fuck what do I do??{/i}"
        ava "Yes! Yes I'm F-Fine!"
        sophia "You're absolutely sure?"
        show avabeachsex movie2
        ava "Yes Yes YES YES!!"
        olivia "Alright, are you gonna come out soon?"
        ava "YES!"
        player "UUUGHH!"
        ava "I'm CUMMING!!"
        pause
        show avabeachsex movie3
        pause
        ava "UHHHN!!!"
        scene fs avabeachsex3
        with Dissolve(0.7)
        sophia "Uh okay...see you soon."
        
        $ endchapter2_trigger = "2 ava naughty"

        jump startofchapter3

        scene fs avabeachsex2
        player "What was that?"
        ava "I WANT IT!!"
        pause
        show avabeachsex movie2
        ava "Hah hah hah.."
        player "Fuck you're tight!"
        ava "And you're so FUCKING big!"
        scene fs avabeachsex4
        with Dissolve(0.5)
        ava "Doing it in the shower is so HOT!"
        show rs oliviashowerright
        with Dissolve(0.7)
        player "You really like this huh?"
        show ls sophiashowerleft
        with Dissolve(0.7)
        ava "Feels so fucking good!"
        show rs oliviashowerlook
        ava "GOD dude. I want to marry your dick!"
        olivia "Huh?"
        ava "You better not pull out!"
        show ls sophiashowerlook
        sophia "Hmm?"
        olivia "Ava?"
        show fs avabeachsex6 behind ls 
        with vpunch
        ava "Ah!"
        ava "Uh yeah?"
        show avabeachsex movie2
        olivia "You okay?"
        ava "Y-Yeah! Ahn!"
        sophia "You sound kinda weird.."
        
        scene fs avabeachsex5
        show ls sophiashowerlook
        show rs oliviashowerlook
        with Dissolve(0.5)
        ava "Oh my god! N-No I'm F-"
        ava "FUCK!"
        sophia "Do you need help?"
        olivia "I think we should open the d-"
        show avabeachsex movie2
        ava "N-No!"
        ava "T-The truth is there's a guy in here!"
        olivia "Ohhhh..."
        sophia "What?"
        ava "There's a guy in here w-AHN! With me. We're having s-SEX!"
        ava "God I'm gonna fucking cum!"
        sophia "Ohmygod. Uh okay sorry."
        show avabeachsex movie3
        ava "FUCK YES YES AHN!!!"
        player "UGGGH!!"
        scene fs avabeachsex3
        with Dissolve(1.0)
        ava "God I feel it..I feel it spilling out..."
        sophia "Oooookay."
        scene fs blackblank
        with Dissolve(1.0)

        jump startofchapter3

label miabeachchapter2end:
    hide screen mia_beach1
    hide screen mia_beach2
    hide screen mia_beach3
    hide screen sophia_beach
    hide screen charlotte_beach
    hide screen ava_beach
    hide screen emily_beach
    hide screen olivia_beach
    hide screen backbuttonBEACH

    scene fs miabeachcute1
    with Dissolve(0.7)
    player "Ahhh."
    pause
    mia "[povname]!"
    if swimsuitchoice == "white":
        scene fs miabeachcute2a
    elif swimsuitchoice == "purple":
        scene fs miabeachcute2b
    else:
        scene fs miabeachcute2c
    with Dissolve(0.7)
    voice "audio/miagameaudio/miaugh.wav"
    mia "Uggggh."
    player "Hey baby."
    mia "Ava made me play SO much volleyball..."
    player "Haha sorry, you can rest here for a bit."
    mia "Thanks.."

    mia "I don't even wanna rest though, we're at the beeeeach."
    player "Haha okay. Let me think about it."
    #$ miaphase2interaction2 = 6
    #if miaphase2interaction2 >= 6:
    #change the above back when chapter 2 is fully done------------------------------
    if miaphase2interaction2 == 4:
        "Would you like to end the day with Mia?"
        menu:
            "Yes":
                jump miachapter2endsex
            "Go back to beach":
                jump explorebeach
    else:
        jump explorebeach

    label miachapter2endsex:
        player "You wanna eat something?"
        mia "No..."
        player "Play something other than volleyball?"
        mia "No..."
        player "It's hard to think with your big t-"
        player "Oh I know what to do."
        
        if swimsuitchoice == "white":
            scene fs miabeachcute3a
        elif swimsuitchoice == "purple":
            scene fs miabeachcute3b
        else:
            scene fs miabeachcute3c
        mia "Yeah??"
        player "Hehe oh yeah."
        player "You wanna sneak off for a little secret sex?"
        
        if swimsuitchoice == "white":
            scene fs miabeachcute4a
        elif swimsuitchoice == "purple":
            scene fs miabeachcute4b
        else:
            scene fs miabeachcute4c
        voice "audio/miagameaudio/miahehe.wav"
        mia "Oh...hehe."
        mia "I never thought about that.."
        mia "Let's do it!"
        scene fs blackblank
        with Dissolve(0.7)
        stop music fadeout 3
        "A few minutes later..."
        play music "audio/showersounds.wav" fadein 5
        scene fs miabeachsex1
        with Dissolve(0.5)
        mia "Mmmm."
        scene fs miabeachsex2
        with Dissolve(0.5)
        player "Hey there beautiful."
        mia "[povname]! Hehe glad you made it."
        scene fs miabeachsex3
        with Dissolve(0.5)
        mia "Mmmm!"
        player "Mmph."
        scene fs miabeachsex4
        with Dissolve(0.5)
        player "I ever tell you how much I love your tits?"
        show rs charlotteshowersright
        with Dissolve(0.7)
        charlotte "Haaa..."
        mia "You may have mentioned it haha."
        show fs miabeachsex5
        show ls emilyshowersleft
        with Dissolve(0.7)
        emily "Hmm hm hmmm."
        mia "Oh? Where are those hands going?"
        show fs miabeachsex6
        voice "audio/miagameaudio/miaah2.wav"
        mia "Ah! Oh my gosh!"
        show rs charlotteshowerslook
        charlotte "Huh? Mia?"
        player "My hands are occupied so you're gonna have to put it in."
        show fs miabeachsex7
        mia "So hard..."
        show ls emilyshowerslook
        emily "Oh? Someone else here?"
        charlotte "Emily? Is that you?"
        emily "Yeah I thought I heard Mia."
        show fs miabeachsex8
        mia "O-Oh! Yes sorry I was-"
        show fs miabeachsex9
        with vpunch
        voice "audio/miagameaudio/miaah.wav"
        mia "AHH!"
        player "{i}God I love this girl's pussy!{/i}"
        charlotte "Mia! Are you okay?"
        show miabeachsex movie1
        play sound "audio/miagameaudio/miamoaning.wav" loop
        mia "Ahn Ahn Ahn!"
        mia "I-I'm Finnnne!!"
        emily "It sounds like she's struggling Charlotte!"
        charlotte "Mia do you need help!??"
        mia "YESYESYESYES!!!"
        emily "Charlotte go get Ava!"
        scene fs blackblank
        with Dissolve(0.5)
        mia "N-No wait!"
        show fs miabeachsex10
        ava "Mia!? We're coming in to help!"
        play sound "audio/miagameaudio/miamoanno.wav"
        mia "N-No PLEEEASE!"
        show fs miabeachsex11
        with vpunch
        ava "Who's fucking with our-"
        scene fs miabeachsex14
        with Dissolve(0.7)
        ava "....friend."
        scene fs miabeachsex12
        mia "Nooo don't look!"
        player "Uh babe...I'm gonna-"
        scene fs miabeachsex13
        with vpunch
        play sound "audio/miagameaudio/miaorgasm2.wav"
        mia "C-Cumming!"
        player "Fuck!"
        scene fs miabeachsex14
        with Dissolve(0.5)
        "...."
        scene fs carscene8
        with Dissolve(1.2)
        stop music fadeout 3
        "It was an awkward drive back for mostly everyone"
        "You didn't really mind though. You fucked a pretty girl and came inside her while all her friends watched."
        "On paper that's pretty good!"
        pause
        pause
        pause
        scene fs carscene9
        with vpunch
        sophia "Gah!"
        $ endchapter2_trigger = "2 mia neutral"
        $ miaquestlog = "I've been patient. It's time Mia..."
        jump startofchapter3

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

label phase1ending: # aka chapter 2 begins
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
    "You haven't really gotten a chance to drive it yet so youre pretty excited"
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
    mia "[povname!!!] you made iiiit!"
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
        $ sophiaquestlog = "I feel bad about skipping out on lunch, I should see her again."

    if oliviaphase1interaction3 == 2:
        $ oliviaquestlog = "That was so hot! I should really talk to her about where to go from here though."

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

        #$ hiden_textbox = False
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
    "Rgbcat" "If you see this, something of the mod didnt work. Please send me your save file on f95!"
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

label esch1_mia: # rgbcat note: commented out section should be reworked when touching up the game

    # scene fs crowdcheer1
    # with Dissolve(0.7)
    # "The bright sunny day was charged with energy from the spectators and participants"
    # "You spend the first hour watching and cheering for the girl's school teams"
    # scene fs trackrace0
    # with Dissolve(0.7)
    # "Finally Ava's race was announced to be next."
    # scene fs crowdcheer1
    # with Dissolve(0.7)
    # player "Man your school is killing it! I'm glad Ava is up next though."
    # scene fs miacrowd1
    # mia "Brrrr!"
    # scene fs miacrowd1mia
    # mia "Y-yeah me too, it's getting kind of chilly."
    # scene fs miacrowd1b
    # player "Well hey I brought a blanket for this exact situation, want to cuddle up?"
    # mia "Really?!"
    # scene fs miacrowd1bplayer
    # player "Yeah come sit on my lap."
    # scene fs miacrowd2
    # with Dissolve(0.7)
    # mia "Ahh so much better!"
    # sophia "Hmph."
    # scene fs trackrace0
    # with Dissolve(0.7)
    # charlotte "I think I can see Ava walking out to the track!"
    # emily "Yeah they're getting ready to run!"
    # scene fs miacrowd3
    # with Dissolve(0.7)
    # "As Mia tried to get comfortable and warm she wiggled her butt directly on your crotch"
    # "As any man will tell you this usually results in immediate blood flow to the nether regions"
    # "And dirty thoughts to the head."
    # "*BAM!*"
    # scene fs trackrace1
    # with Dissolve(0.7)
    # sophia "Oh there they go!"
    # charlotte "She's in the lead!"
    # mia "Woohoo Ava!!"
    # scene fs miacrowd3
    # with Dissolve(0.7)
    # player "{i}Hehe I dind't plan on it but...now might be a great time to get a little naughty.{/i}"
    # player "{i}I don't think anyone would notice with this blanket on us.{/i}"
    # emily "Run Ava run!"
    # player "{i}This is your own fault Mia for wiggling your butt on my dick.{/i}"
    # scene fs miacrowd4
    # with Dissolve(0.7)
    # mia "Ava let's go-OH!"
    # player "{i}Mmmm I won't ever get tired of these boobs.{/i}"
    # scene fs miacrowd4b
    # mia "{size=-10} [povname] what are you d-doing??{/size}"
    # scene fs miacrowd5
    # player "{size=-10}I wanna touch you a little.{/size}"
    # mia "{size=-10}Here?? Everyone's around us!{/size}"
    # player "{size=-10}No one's paying attention just relax.{/size}"
    # scene fs miacrowd5b
    # mia "{size=-10}N-No you...{/size}"
    # scene fs miacrowd5
    # mia "Ahn.."
    # scene fs trackrace2
    # with Dissolve(0.5)
    # "Ava's lead was shortening after they turned the corner"
    # player "{size=-10}Yeah that's it, I can feel how wet you're getting.{/size}"
    # scene fs miacrowd5b
    # with Dissolve(0.7)
    # mia "Ehhhnn!"
    # image fingermia:
    #     "ava crowd b5.png"
    #     0.7
    #     "ava crowd b5b.png"
    #     0.7
    #     repeat

    # show fingermia
    # player "{size=-10}You like it when I finger you with all your friends around us?{/size}"
    # mia "{size=-10}[povname]!{/size}"
    # window hide
    # pause
    # scene fs trackrace2
    # with Dissolve(0.5)
    # mia "{size=-10}You have to stop I-I'm gonna cum!{/size}"
    # "Running down the straight lanes Ava burst ahead with incredible speed!"
    # scene fs trackrace3
    # with vpunch
    # "Crowd" "WOOOOO!!"
    # scene fs miacrowd6
    # with Dissolve(0.7)
    # mia "AHNNNNN!!!"
    # "Crowd" "YEAAAHHHH!!"
    # player "{i}Fuck she's clamping down on my fingers!{/i}"
    # scene fs miacrowd7
    # with Dissolve(0.7)
    # mia "Ooohh yes!!"
    # sophia "Huh?"
    # scene fs blackblank
    # with Dissolve(1.0)
    # player "{i}Well that was a lot of fun.{/i}"
    # player "{i}Nice to know I can get Mia to do public stuff.{/i}"
    

    
    jump gohomemia

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

# -----------ALL THE NONE INDIVIDUAL GIRL SCENES FOR CHAPTER 2--------------------------------------------------------------------------------------
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
#    with Dissolve(0.5)
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
    player "Whats going on?"
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
    player "Uh yeah I think I can make some room in my schedule for that. Now are we all wearing bikinis cause I dont want to show up with the same outfit as one of you guys. SO embarrassing."
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
    mia "Oh thank you so much!"
    katie "Yaaayyy~"
    mia "Katie!"
    player "Welp. Looks like I'm heading out."
    player "I better head over to Sunnyside."
    scene fs blackblank
    with Dissolve(1.0)
    "You can now head to the town over by clicking the arrow in the bottom right of the map!"
    $ headtosunnyside = 1
    jump overworldmap

# continue phase 1 end
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

# end file frfr