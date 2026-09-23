# chapter 1
# interaction 1
# part 1

label charlottephase1interaction1part1:
    hide screen charlotte_library
    hide screen charlotte_school
    hide screen backbuttonCLASSROOM
    scene fs classroom3blur
    with Dissolve(1.0)
    show fbcharlotte current:
        xalign 0.6 ypos 120
    with Dissolve(1.0)

    player "{i}Oh it's Mia's short friend, maybe I should say hi.{/i}"
    player "{i}Her name was Charlotte right?{/i}"
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    player "Hey Charlotte good morning."
    $ playerSprite = 0
    $ charlotteSprite = 1
    voice "audio/charlottegameaudio/charlotteugh.wav"
    charlotte "Oh it's you. Mia's boyfriend."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Yeah uh hi, how are yah?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Good thanks, talk to you later."
    $ charlotteSprite = 0
    $ playerSprite = 5
    player "Sorry...have I pissed you off somehow?"
    $ playerSprite = 4
    $ charlotteSprite = 1
    charlotte "Yes, you exist. Now if you'd kindly leave me alone!"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I was thinking maybe Mia and the girls and I could hang out after school did you want to join us?"
    $ playerSprite = 4
    $ charlotteSprite = 1
    charlotte "No thank you I'd rather be at the library then watch some pervert take advantage of my friend. Plus I have work to do so I can't be wasting my time with you."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "So you'll be at the library huh?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    #voice "audio/charlottegameaudio/charlotteugh.wav"
    charlotte "Ugh. I shouldnt've said that."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I'll see you there then."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Please don't."
    hide fbcharlotte current
    with Dissolve(0.5)
    $ charlotteSprite = 0
    $ playerSprite = 7
    player "Well that was interesting. It seems like she hates me but nobody is that straightforward when talking to someone they dont like for the first time, she had no tact at all."
    player "If I'm going to date Mia I'll need her friends to warm up to me. And I don't want to just run to Mia and complain..."
    player "I should go see her at the library in the afternoon."
    $ charlottephase1interaction1 = 1
    $ charlottequesticon = "gui/questboxCharlotte.png"
    if renpy.android:
        $ charlottequestlog = "{size=-25}I can find Charlotte in the library during the day.{/size}"
    else:
        $ charlottequestlog = "I can find Charlotte in the library during the day."
    hide fs classroom3blur
    hide fbplayer
    hide fbcharlotte
    jump classroom3

# part 1 post convo

label charlottewonttalktome:
    hide screen charlotte_school
    hide screen backbuttonCLASSROOM
    player "Charlotte doesn't really want to talk to me right now, I should meet her in the library later."
    jump classroom3

# part 2

label charlottephase1interaction1part2:
    hide screen charlotte_library
    scene fs charlottelibrary1
    with Dissolve(1.0)


    player "Hey there's Charlotte at that table!"
    player "Oh yeah it's a library I should be quiet."

    scene fs charlottelibrary2
    with Dissolve(0.7)
    player "...."
    scene fs charlottelibrary3
    player "Hey Charlotte."
    scene fs charlottelibrary4
    voice "audio/charlottegameaudio/Charlotteah.wav"
    charlotte "Gah!!"
    scene fs charlottelibrarycharlotte
    charlotte "What the hell! What are you doing here?"
    scene fs charlottelibraryplayer
    player "Came to talk to you, may I sit down?"
    scene fs charlottelibrarycharlotte
    charlotte "No."
    scene fs charlottelibraryplayer
    player "That's alright I'll stand."
    scene fs charlottelibrarycharlotte
    charlotte "Ugh."
    scene fs charlottelibraryplayer
    player "Listen I know you're busy...studying?"
    scene fs charlottelibrarycharlotte
    charlotte "Yes. Researching."
    scene fs charlottelibraryplayer
    player "Right. I know you're busy studying and researching but I can't let you hate me without good reason, so I want to get to know you better."
    scene fs charlottelibrarycharlotte
    charlotte "I'm not interested in having some pervert scumbag know about me!"
    scene fs charlottelibrary5
    play sound "audio/Shush Sound Effect.wav"
    "Library" "Shhhhh!"
    scene fs charlottelibrary6
    charlotte "Sorry..."
    scene fs charlottelibraryplayer
    player "Just a couple of questions, please."
    scene fs charlottelibrarycharlotte
    charlotte "Hmph. If it'll get you to leave me alone fine."
    scene fs charlottelibraryplayer
    player "Thanks."
    player "So...where are you from?"
    scene fs charlottelibrarycharlotte
    charlotte "I'm from here you idiot."
    scene fs charlottelibraryplayer
    player "Oh."
    scene fs charlottelibrarycharlotte
    charlotte "But I'm assuming you're asking me that because of my name and my looks."
    scene fs charlottelibraryplayer
    player "Yeah you're really pretty."
    scene fs charlottelibraryblushtalk
    charlotte "Wha...I..."
    scene fs charlottelibraryblush
    charlotte "*Ahem*."
    scene fs charlottelibrarycharlotte
    charlotte "My mother's from Grance and Daddy's from The United Provinces of Amerika."
    charlotte "Both are business people and we're very well off."
    scene fs charlottelibraryplayer
    player "Ah I see, you live with them then?"
    scene fs charlottelibraryblushtalk
    charlotte "Well....sort of, I live at home but they're often too busy to be...i-it doesnt matter! Yes I live with them. Technically."
    scene fs charlottelibraryplayer
    player "Great, so how'd you meet Mia?"
    scene fs charlottelibraryhappytalk
    charlotte "Oh I've known Mia since late grade school! I'm her earliest friend!"
    charlotte "Some bullies stole my lunch so I was crying. She sat down beside me and gave me half of her sandwhich without saying anything."
    scene fs charlottelibraryhappyMCtalk
    player "Cucumber?"
    scene fs charlottelibraryhappytalk
    charlotte  "Haha yeah! Weird right? Anyways I was used to high class meals and said I didn't want her crappy sandwhiches."
    charlotte "But she just kept quiet and I got so hungry I ate it anyways."
    charlotte "It was the tastiest thing I've ever had, I started crying again."
    charlotte "So she gave me a hug and took me to the teacher to report the bullies. We've been best friends ever since!"
    scene fs charlottelibraryhappyMCtalk
    player "Wow that is a really nice story."
    scene fs charlottelibraryhappytalk
    charlotte "Uh huh! Mia's a saint! It's been just the two of us until we met Emily."
    charlotte "She introduced us to the rest of the girls, and over the last couple of years we went through a lot of things together."
    charlotte "And those things made our friendship stronger than ever!"
    scene fs charlottelibrarycharlotte
    charlotte "....Until YOU showed up."
    scene fs charlottelibraryplayer
    player "Well I don't know about that last part but I'm quite aware of how awesome Mia is."
    scene fs charlottelibraryblushtalk
    charlotte "A-And she's way too good for you!"
    scene fs charlottelibrarycharlotte
    charlotte "That's enough questions I have to get back to work!"
    scene fs charlottelibraryplayer
    player "Alright Charlotte, thanks for talking to me I'll see you later."
    scene fs charlottelibrarycharlotte
    charlotte "Whatever I don't care."
    scene fs charlottelibrary1
    with Dissolve(1.0)
    player "{i}I think she's starting to warm up to me. Seems we can find some middle ground when it comes to Mia. I should visit her here again tomorrow.{/i}"
    scene fs charlottelibrarycharlotte
    $ charlottephase1interaction1 = 2
    $ charlottequestlog = "Is she warming up to me? I should visit her again."
    hide fs charlottelibrarycharlotte
    jump passtime

# part 3

label charlottephase1interaction1part3:
    hide screen charlotte_library
    scene fs libraryBLUR
    with Dissolve(1.0)


    scene fs charlottelibrary1
    with Dissolve(0.7)
    "You see Charlotte sitting in the same seat as before on the table that's in the corner of the library"

    scene fs charlottelibrary3
    with Dissolve(0.5)
    player "Charlotte!"
    scene fs charlottelibrary2
    "You walk up behind her and realize she's too engrossed in what she's reading and still hasn't noticed you"
    "You peer over her shoulder and take a look at her book."
    scene fs charlottelibrary3
    player "'Sexual relations and the Human need to procreate.'"
    scene fs charlottelibrary4
    with vpunch
    voice "audio/charlottegameaudio/Charlotteah.wav"
    charlotte "AHH! W-What the fuck!"
    scene fs charlottelibraryplayer
    player "Woah sorry-"
    scene fs charlottelibrarycharlotte
    charlotte "Again??! What the FUCK is wrong with yo-"
    scene fs charlottelibrary5
    play sound "audio/Shush Sound Effect.wav"
    "Library" "SHHHH!!"
    scene fs charlottelibrary6
    with Dissolve(0.3)
    voice "audio/charlottegameaudio/charlottesorry.wav"
    charlotte "Sorry!"
    scene fs charlottelibrarycharlotte
    charlotte "*Ahem* {size=15}What the fuck is wrong with you?{/size}"
    scene fs charlottelibraryplayer
    player "I tried to get your attention but you couldn't notice me with your eyes glued to that book so I wanted to know what it was."
    scene fs charlottelibrarycharlotte
    charlotte "Well...You still shouldnt sneak up on people from behind. Who knows what your perverted brain was thinking about doing to me."
    scene fs charlottelibraryplayer
    player "Funny you should call ME perverted miss sexual relations."
    scene fs charlottelibrary7
    charlotte "I-I-I'm n-not-"
    scene fs charlottelibrary8
    player "Relax Charlotte I'm just teasing. Can I sit?"
    scene fs charlottelibrarycharlotte
    charlotte "No!"
    scene fs charlottelibraryplayer
    player "I think Mia and the girls would be very interested to know what kind of material you're using for-"
    scene fs charlottelibrary7
    charlotte "Okay okay just sit down already then."
    scene fs charlottelibrary11
    with Dissolve(0.7)
    charlotte "...."
    scene fs charlottelibrary16bhd
    charlotte "I'm just....doing research for my essay okay? It's on base human funcionality and innate behaviour."
    scene fs charlottelibrary17hd
    charlotte "A lot of it has to do with s-sex so...I'm studying."
    scene fs charlottelibrary16hd
    player "Hmm, I'm going to guess you went to a preppy girls school when you were young."
    scene fs charlottelibrary16bhd
    charlotte "H-How would you know that?"
    scene fs charlottelibrary16
    with Dissolve(0.7)
    player "Well you're a rich girl so your parents could afford it, but I'm thinking you never properly learned to socialize with other boys your age."
    player "So you never had a crush on a boy."
    scene fs charlottelibrary17
    player "Never dated one, never kissed one."
    player "Definitely never had sex."
    player "So when you were older you couldn't really make things work relationship wise and now you just have a dislike or distrust of men in general yet are extremely curious about sexual relations."
    scene fs charlottelibrary16
    player "How'd I do?"
    charlotte "...."
    scene fs charlottelibrary17
    with Dissolve(0.7)
    window hide
    pause
    player "That is just a guess of course. Oh and that's probably why you love your friends so much too, Mia told me."
    scene fs charlottelibrary9
    charlotte "Do you have a point or are you just going to make fun of me?"
    scene fs charlottelibrary11
    player "*sigh* I'm not going to make fun of you Charlotte I just wanted to point out most of the stuff in these books are common sense to people who've been in a relationship."
    scene fs charlottelibrary9
    charlotte "Well that's great I haven't so that's why I'm HERE."
    scene fs charlottelibrary11
    player "Well despite what you may think I'm NOT here to upset you, please just continue what you were doing."
    scene fs charlottelibrary16bhd
    charlotte "I don't need you to tell me that."
    scene fs charlottelibrary17hd
    charlotte "Hmph."
    scene fs blackblank
    with Dissolve(0.8)
    "Charlotte continues to read her books for a while, you're on your phone for most of the time"
    "Eventually you get bored and just start watching her as she concentrates"
    scene fs charlottelibrary11
    with Dissolve(0.7)
    window hide
    pause
    player "{i}God damn she is a terrible person to deal with.{/i}"
    player "{i}I don't know how she's gonna interact with the rest of the world once she finishes school.{/i}"
    player "{i}She is really cute though. Guess I'll just chill for a bit got nothing better to do.{/i}"
    scene fs blackblank
    with Dissolve(1.5)
    "After a bit of time..."
    image charlottelibrarymasterbate:
        "charlotte CG8.png"
        0.7
        "charlotte CG9.png"
        0.7
        repeat

    scene charlottelibrarymasterbate
    with Dissolve(0.8)
    play sound "audio/charlottegameaudio/charlottepanting1.wav" loop
    charlotte "Hmmm..."
    charlotte "The male glands extend..."
    charlotte "Puts the.....into her..."
    player "{i}What is she mumbling?{/i}"
    window hide
    pause
    player "{i}Wait...is she...she's not...{/i}"
    player "{i}Charlottes' masturbating! She's full on jilling it through her clothes.{/i}"
    charlotte "mmmm...penetrates..."
    player "I gotta watch this, how long will she keep going?"
    window hide
    pause
    charlotte "Hah...hah..."
    scene fs charlottelibrary16bhd
    with Dissolve(0.5)
    stop sound
    voice "audio/charlottegameaudio/charlotteugk.wav"
    charlotte "W-Wait what? What is it? Why are you staring at me like that."
    scene fs charlottelibrary16hd
    player "Charlotte...did you really not realize?"
    scene fs charlottelibrary16bhd
    charlotte "Realize what? Stop freaking me out pervert."
    scene fs charlottelibrary16
    player "You were just masturbating for like 20 minutes."
    scene fs charlottelibrary17
    charlotte "What?"
    scene fs charlottelibrary16hd
    player " In a library."
    scene fs charlottelibrary17hd
    charlotte "Shut up!"
    scene fs charlottelibrary11
    player "In front of ME."
    scene fs charlottelibrary9
    charlotte "I'm leaving!"
    scene fs charlottelibrary15
    with Dissolve(0.5)
    #charlotte is about to leave but then realises she's wet and doesnt leave
    charlotte "{i}Shit! My thighs are soaked again! God dammit why'd he have to be here this time?!{/i}"
    scene fs charlottelibrary11
    with Dissolve(0.7)
    charlotte "......"
    player "I think I understand what the situation is. And I'm willing to help you out."
    player "For a price."
    scene fs charlottelibrary9
    charlotte "Fuck you I don't know what you're talking about!"
    scene fs charlottelibrary11
    player "...."
    player "Since you're not looking up. I'll tell you there's barely anyone else in here, so apologize and I'll leave first so nobody will see."
    scene fs charlottelibrary16bhd
    charlotte "S-See what?!"
    scene fs charlottelibrary17hd
    player "C'mon Charlotte. See how wet you are, I'm guessing your thighs are soaking right now right?"
    player "I swear I won't say anything to anyone, not even Mia."
    charlotte "....."
    scene fs charlottelibrary9
    #voice "audio/charlottegameaudio/charlottesorry2.wav"
    charlotte "I'm sorry."
    scene fs blackblank
    with Dissolve(0.8)
    "Giving her a little grin you stand up and leave as promised"
    player "Well that was quit the interesting day, never thought I'd find out Charlotte would wet her thighs touching herself in the library of all places."
    player "She didn't even notice she was doing it! She's that starved for sexual....well sexual anything apparently."
    player "She was probably really embarrassed so I should see her again and show her I don't care about it and maybe she'll lay off of me about Mia every now and again."
    $ charlottephase1interaction1 = 3
    $ charlottequestlog = "I can't believe what I just saw! I feel a bit bad though I should talk to her at school."
    hide fs blackblank
    jump passtime

# part 4 (according to the var its not interaction 2 yet)

label charlottephase1interaction2part1A:
    scene fs blackblank
    with Dissolve(0.7)
    "Professor" "Alright class that's it for today, remember to work on those essays they're worth 60\%\ of your final grade!"
    scene fs classroom3blur
    with Dissolve(0.7)
    $ charlotteSprite = 0
    show fbcharlotte current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)

    voice "audio/charlottegameaudio/charlotteehn.wav"
    charlotte "{i}Ugh. What am I doing to do?{/i}"
    show fbcharlotte defaultflip:
        xalign 0.8 ypos 120
    with move
    charlotte "{i}I'm never going to finish this essay at the rate I'm going let alone write a good one!{/i}"
    show fbcharlotte current:
        xalign 0.6 ypos 120
    with move
    charlotte "{i}Not to mention [povname] keeps...distracting me.{/i}"
    charlotte "{i}I still can't believe he saw m-{/i}"
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.7)
    player "Hey."
    $ playerSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte current at surpriseshake:
        xalign 0.65 ypos 120
    with move
    #voice "audio/charlottegameaudio/charlotteyou.wav"
    charlotte "You! Oh no no leave me alone! I'm about to have class!"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I saw the professor leave Charlotte I know your class is done."
    player "How's the essay coming?"
    $ playerSprite = 0
    $ charlotteSprite = 6
    charlotte "What?"
    $ charlotteSprite = 5
    charlotte "Oh uh i-it's going great! Almost finished! I probably won't even need to go to the library any more!"
    $ playerSprite = 1
    player "Hmm that bad huh? Am I distracting you?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Yes! I-I mean no! I mean you're the one distracting me b-but I'm almost done anyways like I said."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Hard to believe with all that masturbating you're doing."
    show fbcharlotte defaultflip at surpriseshake:
        xalign 0.65 ypos 120
    pause
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.65 ypos 120
    voice "audio/charlottegameaudio/charlotteshush.wav"
    charlotte "Hey! Shhhh shut up!"
    $ charlotteSprite = 5
    $ playerSprite = 1
    player "Which by the way I'm pretty sure was happening BEFORE we even met. I actually came here to tell you I DON'T care about it."
    player "It's not a big deal to me and I feel bad about embarrassing you. So why not let me help you with the essay?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Che, YOU help ME?!"
    charlotte "I don't think so."
    $ charlotteSprite = 0
    $ miaSprite = 1
    image fbmia talkflip = im.Flip("Sprites/miatalk.png", horizontal=True, vertical=False)
    image fbmia defaultflip = im.Flip("Sprites/miadefault/png", horizontal=True, vertical=False)
    show fbmia talkflip:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    mia "Hi Charlotte! Is your class done?"
    show fbmia current:
        xalign 0.5 ypos 120
    mia "[povname]!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Hello beautiful!"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Hehe why are you here?"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Came to see you but ran into Charlotte here. She seems to be struggling with an essay of hers and I want to help."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "That is NOT what is happening."
    $ charlotteSprite = 0
    $ miaSprite = 1
    show fbmia talkflip:
        xalign 0.5 ypos 120
    mia "You should let him help Charlotte, what is the topic on?"
    show fbmia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 0
    $ charlotteSprite = 5
    charlotte "It's....i-it's-"
    $ charlotteSprite = 0
    $ playerSprite = 1
    show fbmia current:
        xalign 0.5 ypos 120
    player "Sexual relations and human interaction."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "S-see? There's no way he can help me with something like that."
    $ charlotteSprite = 0
    $ miaSprite = 5
    show fbmia talkflip:
        xalign 0.5 ypos 120
    mia "Hmmm no I think he can!"
    show fbmia defaultflip:
        xalign 0.5 ypos 120
    $ miaSprite = 0
    $ charlotteSprite = 1
    charlotte "What?"
    $ charlotteSprite = 0
    $ miaSprite = 4
    show fbmia current:
        xalign 0.5 ypos 120
    mia "[povname] is really good at sex! He makes me cum all the time."
    $ miaSprite = 0
    charlotte "...."
    $ charlotteSprite = 1
    charlotte "I didn't need to know that Mia. And that's not what the essay is ab-"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Speaking of Mia, you want to come over to my place tonight?"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Hehe yeah I think I have the time."
    $ miaSprite = 0
    $ charlotteSprite = 1
    charlotte "Oi..."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "You ever hear of pronebone? Think I'd like to try that out."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Um...hello."
    $ charlotteSprite = 0
    $ miaSprite = 1
    mia "Ohh I can't wait!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Let's go get some lunch."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Yes I'm starving!"
    $ miaSprite = 0
    hide fbplayer current
    with Dissolve(0.7)
    $ charlotteSprite = 1
    #voice "audio/charlottegameaudio/charlotteangryhey.wav"
    charlotte "Hey don't ignore me! Hey!"
    hide fbmia current
    with Dissolve(0.7)
    charlotte "Hey!"
    $ charlotteSprite = 0
    charlotte "...."
    $ charlotteSprite = 1
    voice "audio/charlottegameaudio/charlotterude.wav"
    charlotte "RUDE."
    $ charlotteSprite = 0
    $ charlottephase1interaction1 = 4
    $ charlottequestlog = "Totally got sidetracked by Mia..I should find her in the library again."
    jump passtime

# interaction 2
# part 1

label charlottephase1interaction2part1:
    hide screen charlotte_library
    scene fs charlottelibrary2
    with Dissolve(1.0)
    player "{i}Hmmm. 'The Art of Non-Penetrative Pleasure'."
    player "{i}Ho ho! We got a good one today!{/i}"
    scene fs charlottelibrary11
    with Dissolve(0.7)
    player "{i}I wonder if she's ignoring me, or if she just hasn't noticed.{/i}"
    player "{i}Gotta admit it's kinda hot watching her touch herself so shamelessly, especially after the way she talks to me.{/i}"
    scene fs charlottelibrary9
    charlotte "I see you're back."
    scene fs charlottelibrary11
    player "Yeah haha, forgot my popcorn though."
    scene fs charlottelibrary9
    charlotte "Ugh you're such an asshole."
    scene fs charlottelibrary11
    "Librarian" "Um excuse me, sir?"
    scene fs charlottelibrary12
    player "Hey!"
    "Librarian" "Sir!"
    player "I'm not an ass-"
    scene fs charlottelibrarycumming1b
    "Librarian" "SIIRRR??!"
    with vpunch
    scene fs charlottelibrarycumming2b
    player "Woah what is it lady geez?!"
    player "I thought libraries were supposed to be quiet."
    scene fs charlottelibrarycumming2
    "Librarian" "You seem new here young man, may I see your library card?"
    scene fs charlottelibrarycumming2b
    player "Library card?"
    scene fs charlottelibrarycumming2
    "Librarian" "One must have an official library card to be in this section of the library."
    scene fs charlottelibrarycumming2c
    voice "audio/charlottegameaudio/charlottehehehe.wav"
    charlotte "Hehehe."
    scene fs charlottelibrarycumming2b
    player "Wha? Can't I just sit here?"
    scene fs charlottelibrarycumming2
    "Librarian" "I'm afraid not young man."
    scene fs charlottelibrarycumming2c
    voice "audio/charlottegameaudio/charlottehehehe2.wav"
    charlotte "Hehehehe!"
    player "{i}God damn it, Charlotte's really eating this up!{/i}"
    scene fs charlottelibrarycumming2b
    player "Listen I don't even want to take out any books. I just want to keep my friend here company."
    scene fs charlottelibrarycumming2
    "Librarian" "I'm sorry but rules are rules. I must escort you out."
    scene fs charlottelibrarycumming2c
    charlotte "Oh what a shame! Too bad you don't have a card [povname]."
    scene fs charlottelibrarycumming2b
    player "Ugh."
    scene fs charlottelibrarycumming2c
    charlotte "Hehehe why didn't I think of this before?"
    scene fs blackblank
    player "{i}I'm gonna get her back for this.{/i}"
    "You follow the librarian out of that particular section"
    "Before she leaves, you inquire about the library card and she tells you it's {color=#3eab33}75{/color} dollars."
    player "I'm gonna have to buy a card if I want to talk to charlotte again."
    $ charlottephase1interaction2 = 1
    $ charlottephase1interaction1 = 5
    $ charlottequestlog = "I'm gonna need to buy a library card if I want to talk to Charlotte again."
    jump passtime

# part 2

label charlottephase1interaction2part2:
    hide screen charlotte_library
    hide screen uppergui
    scene fs charlottelibrary11
    with Dissolve(1.0)
    player "{i}Here we are again.{/i}"
    player "{i}She must've thought it'd take me a while to get a card. Cause she seems to be really concentrating today.{/i}"
    scene charlottelibrarymasterbate
    with Dissolve(0.8)
    play sound "audio/charlottegameaudio/charlottepanting1.wav" loop
    window hide
    pause
    player "{i}Oh here we go...{/i}"
    player "{i}That's right you little slut. No matter how much you try to play it off you're just as naughty as I am.{/i}"
    player "{i}You know what? I'm going to give you a taste of your own medicine!{/i}"
    "*Ziiiip*"
    image charlottelibrarymasterbatetogether:
        "library scene 4.png"
        0.2
        "library scene 4b.png"
        0.2
        "library scene 3.png"
        0.2
        "library scene 3b.png"
        0.2
        repeat

    show charlottelibrarymasterbatetogether
    window hide
    pause
    player "{i}Fuck I'm so turned on, she literally has no idea!{/i}"
    player "{i}I do love how short she is, and I can't deny her cuteness.{/i}"
    player "{i}God I want to just pick her up, put her legs over her head and pound her tight little pussy.{/i}"
    player "{i}Shit I'm gonna cum! I gotta keep quiet!{/i}"
    scene fs charlottelibrarycumming5
    with hpunch
    player "UGH!"
    window hide
    pause
    player "{i}Oh fuck yes!{/i}"
    stop sound
    scene fs charlottelibrarycumming6
    with Dissolve(0.7)
    window hide
    pause
    player "Hah...hah..."
    scene fs charlottelibrarycumming7
    player "How's it feel huh? Not so fun on the other side of that?"
    player "Now you know...that you can't.."
    player "Charlotte?"
    scene fs charlottelibrarycumming8
    player "Woah hey hey! You can't get angry at me!"
    scene fs charlottelibrarycumming9
    charlotte "I am going to rip off your cock."
    charlotte "And shove it SO far up your a-"
    scene fs charlottelibrarycumming8
    player "Wait no y-you can't get angry! All I did."
    player "ALL I DID, was the same thing you were doing."
    charlotte "....."
    player "Now I'm a guy so our orgasms have different results! I k-know that!"
    player "But it's not my fault how my body works right?"
    player "R-Right Charlotte?"
    scene fs charlottelibrarycumming9
    voice "audio/charlottegameaudio/charlotteyouredead.wav"
    charlotte "If I EVER. See you again. Not only am I telling Mia EVERYTHING, I'm going to murder you."
    scene fs charlottelibrarycumming8
    player "But you'd admit that you were also m-"
    scene fs charlottelibrarycumming9
    charlotte "I don't care."
    charlotte "Do you understand?"
    scene fs charlottelibrarycumming8
    player "....yes ma'am."
    charlotte "...."
    scene fs charlottelibrarycumming10
    with Dissolve(0.7)
    player "...Oh boy."
    player "How am I gonna get out of this one?"
    player "Charlotte hangs out with Mia and the girls all the time so not seeing her is a problem."
    player "...wait a minute. MIA!"
    player "If I word it right...I'm sure I can get her to stop Charlotte from...well...I don't wanna think about it."
    $ charlottequestlog = "Charlotte is PISSED. I'm gonna need Mia's help with this one..."
    $ charlottephase1interaction2 = 2
    jump passtime

# part 3 pre convo or not in classroom1

label charlottephaseMiaDelegation:
    hide screen mia_sophia_atschool
    if charlottephase1interaction2 == 2 and whereami == "classroom1" and timeofday == "Morning":
        jump charlottephase1interaction2part3
    else:
        if whereami == "playerRoom" and timeofday == "Morning":
            scene fs playerroomMorn
            hide screen backbuttonROOM
        elif whereami == "playerRoom" and timeofday == "Day":
            scene fs playerroomDay
            hide screen backbuttonROOM
        elif whereami == "playerRoom" and timeofday == "Night":
            scene fs playerroomNight
            hide screen backbuttonROOM
        elif whereami == "livingRoom":
            hide screen questboxpreview
            hide screen backbuttonLIVINGROOM
            if timeofday == "Night":
                scene fs livingroomnight
            else:
                scene fs livingroom
        elif whereami == "overworldmap" and timeofday == "Night":
            scene fs overworldnight
        elif whereami == "overworldmap":
            scene fs overworld
        elif whereami == "gym":
            scene fs gym
        elif whereami == "library":
            scene fs library
        elif whereami == "arcade":
            scene fs arcade
        elif whereami == "gfhouse":
            scene fs gfhouse
        elif whereami == "sophiahouse":
            scene fs sophiahouse
        elif whereami == "school":
            scene fs schoolhallway
        elif whereami == "schoolhallway":
            scene fs schoolhallway2
        elif whereami == "classroom1":
            hide screen mia_atschool
            hide screen sophia_atschool
            hide screen mia_sophia_atschool
            scene fs classroom
        elif whereami == "mall":
            hide screen backbuttonMALL
            scene fs mall
        player "{cps=25}Hey Mia do you have some time to talk? It's about Charlotte and her essay.{/cps}"
        mia "{cps=25}Oh no not now sorry, come find me at school in the morning.{/cps}"
        player "{cps=25}Alright no problem, see you there.{/cps}"
        mia "{cps=25}<3{/cps}"
        jump returnwhereyouare

# part 3

label charlottephase1interaction2part3:
    hide screen mia_atschool
    hide screen sophia_atschool
    hide screen mia_sophia_atschool
    scene fs classroomZOOM
    with Dissolve(0.7)

    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)

    show fbmia current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    $ playerSprite = 1
    player "Hey Mia!"
    $ playerSprite = 0
    $ miaSprite = 4
    mia "Hey [povname]!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "I wanted to talk to you about Charlotte. I kinda need your help."
    $ playerSprite = 0
    $ miaSprite = 4
    mia "Oh? What can I do?"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Well I went to the library again and we talked and...well you know how she doesn't hide the fact that she doesn't like me?"
    player "I kinda was a bit rude to her as payback and now she's really really pissed."
    $ playerSprite = 0
    $ miaSprite = 4
    mia "Oh geez [povname]! You should know by now Charlotte's a really sensitive girl."
    $ miaSprite = 0
    $ playerSprite = 11
    player "{i}She is?{/i}"
    $ playerSprite = 0
    $ miaSprite = 1
    mia "I know how emotional she can get."
    $ miaSprite = 0
    $ playerSprite = 1
    player "Uh huh."
    $ playerSprite = 0
    $ miaSprite = 4
    mia "But when she does, all you have to do is be firm with her!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Firm?"
    $ playerSprite = 0
    $ miaSprite = 4
    mia "Yes! Almost like...a parent disciplining a child."
    $ miaSprite = 1
    mia "Be clear, and give concise instructions!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "That's...wow that's really cool you know how to handle your friend like that."
    $ playerSprite = 0
    $ miaSprite = 4
    mia "Hehe well sometimes you need your friends to help you even if you don't want them to!"
    mia "Here, let's go and solve this right now!"
    $ miaSprite = 0
    player "{i}Nice. Mia to the rescue.{/i}"
    player "{i}I hope this doesn't blow up in my face....{/i}"

    scene fs classroom3
    with Dissolve(0.7)



    show fbmia current:
        xalign 0.7 ypos 120
    with Dissolve(0.5)

    image fbcharlotte talkflip = im.Flip("Sprites/charlottetalk.png", horizontal=True, vertical=False)
    image fbcharlotte defaultflip = im.Flip("Sprites/charlottedefault/png", horizontal=True, vertical=False)

    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    with Dissolve(0.5)

    $ miaSprite = 1
    mia "Charlotte!"
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    $ miaSprite = 0
    show fbcharlotte happytalkflip:
        xalign 0.55 ypos 120
    charlotte "Mia! My class just finished you wanna go to Moonbucks?"
    
    show fbcharlotte current:
        xalign 0.5 ypos 120
    pause
    $ charlotteSprite = 3
    show fbcharlotte current:
        xalign 0.48 ypos 120
    #voice "audio/charlottegameaudio/charlotteyou.wav"
    charlotte "Wait. Why are you here? I told you I don't ever want to see you again!"
    charlotte "I am gonna beat y-"
    show fbcharlotte defaultflip at surpriseshake:
        xalign 0.55 ypos 120
    $ miaSprite = 3
    mia "Charlotte."
    $ miaSprite = 2
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    charlotte "W-What?"
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    $ miaSprite = 3
    mia "Apologize to [povname] right now!"
    $ miaSprite = 2
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    charlotte "What?! No! Why would I say sorry to this perverted fr-"
    $ miaSprite = 12
    mia "STOP insulting my boyfriend."
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    charlotte "!!"
    $ playerSprite = 1
    player "It's okay Mia I should apologize first anyways."
    $ charlotteSprite = 0
    show fbcharlotte current:
        xalign 0.55 ypos 120
    player "Charlotte I'm really sorry I upset you, I asked Mia to mediate things cause I know you wouldn't listen to me if I didn't."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "[povname] is here because he wanted to apologize and still wants to help you with your essay."
    $ miaSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    charlotte "But-"
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    $ miaSprite = 3
    mia "The essay we ALL know you're struggling with."
    $ miaSprite = 2
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    charlotte "No Mia you don't understand he-"
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    $ miaSprite = 1
    mia "You are going to accept his help."
    $ miaSprite = 0
    $ charlotteSprite = 3
    show fbcharlotte current:
        xalign 0.55 ypos 120
    charlotte "H-He MASTURBATED!"
    $ charlotteSprite = 2
    $ playerSprite = 11
    $ miaSprite = 2
    mia "...."
    player "...."
    $ miaSprite = 12
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    mia "Everybody masturbates Charlotte...why are you being weird?"
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    charlotte "No...no Mia h-"
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    mia "That's enough."
    charlotte "...."
    $ miaSprite = 11
    show fbmia current:
        xalign 0.75 ypos 120
    mia "You and [povname] are going to work on your research when you're free."
    mia "You can even meet at your home so you're more comfortable."
    mia "You're going to stop being mean and jealous."
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    charlotte "I'm not j-"
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    $ miaSprite = 12
    mia "....."
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    $ miaSprite = 0
    charlotte "Okay."
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    $ miaSprite = 1
    mia "And everybody is going to be happy. Understand?"
    $ miaSprite = 0
    show fbcharlotte talkflip:
        xalign 0.55 ypos 120
    charlotte "Yes Mia."
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    $ miaSprite = 1
    mia "Good! I'm going to go home and take a bath, see you later [povname]!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Uh...yeah babe sure, see you later."
    $ playerSprite = 0
    hide fbmia current
    with Dissolve(0.7)
    player "{i}Man that was...so hot. I need to fuck Mia again as soon as I get the chance.{/i}"
    $ charlotteSprite = 0
    show fbcharlotte current:
        xalign 0.55 ypos 120
    player "...."
    $ playerSprite = 1
    player "When should I visit you? Wait I don't even know where you live."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Evening. My house is beside the big arcade."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Um okay I'll see you there I guess. Bye Charlotte."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Bye..."
    $ charlotteSprite = 0
    hide fbcharlotte current
    with Dissolve(0.7)
    $ playerSprite = 7
    player "{i}That was incredible, Mia handled her like a pro.{/i}"
    player "{i}I guess they have been friends for a long time.{/i}"
    player "{i}I wonder if I can do the same thing to get back at her when she's being bitchy.{/i}"
    player "{i}Or does it only work with Mia? Hmmm.{/i}"
    $ charlottephase1interaction2 = 3
    $ charlottephase1interaction3 = 1
    $ charlottequestlog = "Mia sure knows how to handle Charlotte, I gotta visit her house tonight."
    jump passtime

# part 3

label charlottephase1interaction3part1:
    scene fs blackblank
    with Dissolve(0.7)
    stop music fadeout 5
    player "{i}Hmmm, I guess I should just ring the buzzer? Man this house is huge.{/i}"
    "BBBBZZZZ"
    "Soft Voice" "Hello?"
    player "Yeah uh hi, my name's [povname] and I'm here to see Charlotte?"
    "Soft Voice" "We've been expecting you Master [povname]."
    player "{i}Master [povname]? Can't say I don't like the sound of that!{/i}"
    "Soft Voice" "I'll unlock the gate, once you open the entrance doors head up the staircase to your right and enter the 2nd room."
    player "Uhhh, sure. Up the right stairs and 2nd room. Got it."
    "*Unlocking Sound*"
    "You follow the voice's instructions and enter the massive estate."
    scene fs charlotteroom
    with Dissolve(1.0)
    $ victoriaSprite = 0
    show fbvictoria current:
        xalign 0.7 ypos 120
    with Dissolve(0.6)

    $ playerSprite = 0

    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.6)

    $ victoriaSprite = 1
    victoria "Welcome to the estate Master [povname]."
    $ victoriaSprite = 0
    $ playerSprite = 11
    player "{i}Wow she's gorgeous....wait who is she?{/i}"
    $ playerSprite = 0
    $ playerSprite = 1
    player "Uh thank you."
    $ playerSprite = 0
    $ victoriaSprite = 1
    victoria "I'm Mistress Charlotte's personal maid Victoria."
    $ victoriaSprite = 0
    $ playerSprite = 1
    player "Nice to meet you."
    $ playerSprite = 0
    $ victoriaSprite = 1
    victoria "You as well. Mistress Charlotte should be returning soon."
    $ victoriaSprite = 0
    $ playerSprite = 1
    player "Sure no problem. So how long have you been with...uh working here?"
    $ playerSprite = 0
    $ victoriaSprite = 1
    victoria "I've been with the family since not long after the Mistress was born."
    $ victoriaSprite = 0
    $ playerSprite = 1
    player "Cool."
    $ playerSprite = 0
    victoria "...."

    $ charlotteSprite = 1

    show fbcharlotte talkflip:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    charlotte "I'm back Vicky is he here ye-"

    show fbcharlotte current:
        xalign 0.5 ypos 120

    charlotte "Ah, you've arrived."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Heh, yeah I've arrived."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Ugh."
    charlotte "Let's get this over with."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "You're still mad that I used Mia to set this up."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "What gave it away. I still can't believe you...you did that to me."
    $ charlotteSprite = 5
    charlotte "With your....foul...thick...p-penis."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Jesus Charlotte even now you can't decide if you're disgusted or turned on. You gotta pick one."
    $ playerSprite = 0
    $ charlotteSprite = 8
    charlotte "I am n-not turned on! You...you!"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Baka?"
    $ playerSprite = 0
    $ charlotteSprite = 6
    charlotte "What?"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Nothing. How long has she been like this Victoria?"
    $ playerSprite = 0
    $ victoriaSprite = 1
    victoria "Since around puberty started master [povname]."
    $ victoriaSprite = 0
    $ charlotteSprite = 8
    image fbcharlotte surpriseflip = im.Flip("Sprites/charlotte sprite embarrassed.png", horizontal=True, vertical=False)
    show fbcharlotte surpriseflip at surpriseshake:
        xalign 0.55 ypos 120
    charlotte "Hey! Don't be so familiar with him! A-And don't tell him things l-like that!"
    $ charlotteSprite = 5
    show fbcharlotte current:
        xalign 0.5 ypos 120
    $ playerSprite = 1
    player "Okay everybody calm down. Let's just start shall we?"
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "Fine."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "In my opinion the first thing we need to do is desensitize you."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "What?"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Well as soon as you get into the research you get turned on, and that distracts you and you start to...uh..."
    $ victoriaSprite = 1
    $ playerSprite = 0
    victoria "You told him about that?"
    show fbcharlotte surpriseflip:
        xalign 0.55 ypos 120
    $ victoriaSprite = 0
    charlotte "No! I-I didn't mean to let him see!"
    $ charlotteSprite = 1
    charlotte "He came to me in the library and wouldn't go away and...and then he came ON me too!"
    $ charlotteSprite = 0
    show fbcharlotte current:
        xalign 0.5 ypos 120
    $ playerSprite = 1
    player "Haha yeah....yeah I did."
    $ playerSprite = 0
    victoria "...."
    $ playerSprite = 1
    player "Anyways. I think you're like this cause you just weren't really exposed to sexual stuff until a later age."
    player "So! We flood your innocent little head with some basic vanilla normal naughty stuff and eventually it won't be that big of a deal."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "I don't know. This seems to be another one of your perverted schemes."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Just enough that you can still get turned on but not so much that you soak your panties when a nipple shows up."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "ehhh...."
    $ charlotteSprite = 0
    $ victoriaSprite = 1
    victoria "He has a point Miss. Nothing else has helped you."
    $ victoriaSprite = 0
    $ charlotteSprite = 5
    charlotte "I still don't think this will work but..."
    charlotte "It can't hurt to try I suppose."
    charlotte "What do I have to do?"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "We'll start with something simple. Just watch some porn."
    $ playerSprite = 0
    $ charlotteSprite = 6
    charlotte "What?"
    $ charlotteSprite = 8
    charlotte "Ew...."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Right here and now, just for a few minutes. Try it without getting flustered, should be easy no?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Ugh okay."
    $ charlotteSprite = 0
    $ playerSprite = 2
    player "Alright let me find something here....Oh I know. This should do."
    player "Sent."
    $ playerSprite = 0
    $ charlotteSprite = 9
    charlotte "Okay...play."
    show fbvictoria current:
        xalign 0.60 ypos 120
    with move
    "Phone" "....."
    $ charlotteSprite = 10
    play sound "audio/miagameaudio/miaphonemoan.wav" loop
    "Phone" "Mmmmm yeah..."
    $ victoriaSprite = 1
    victoria "Oh."
    $ victoriaSprite = 0
    "Phone" "Feels good baby?"
    $ charlotteSprite = 9
    "Phone" "Yes! Oh my gosh!!"
    $ victoriaSprite = 1
    victoria "That man is quite well endowed."
    $ victoriaSprite = 0
    $ playerSprite = 1
    player "Why thank you."
    $ playerSprite = 0
    $ charlotteSprite = 10
    "Phone" "Ahn! Ahn!"
    $ charlotteSprite = 9
    charlotte "Wait..."
    "Phone" "So good! You feel so good inside me!"
    $ victoriaSprite = 1
    victoria "That sounds like..."
    $ victoriaSprite = 0
    stop sound
    play sound "audio/miagameaudio/miaphoneorgasm.wav"
    "Phone" "[povname]! [povname] give it to me! AHN!!!!"
    $ charlotteSprite = 10
    show fbcharlotte current at surpriseshake:
        xalign 0.5 ypos 120
    charlotte "T-T-This is you and Mia!!!"
    $ charlotteSprite = 9
    "Phone" "You like this big cock baby?"
    "Phone" "Yes I love it cum inside me!!"
    $ victoriaSprite = 1
    victoria "Miss Mia seems...healthy."
    $ victoriaSprite = 0
    $ charlotteSprite = 10
    "Phone" "AHHHNN yesss! [povname]!"
    $ victoriaSprite = 1
    $ charlotteSprite = 9
    victoria "Her breasts have gotten larger since I've last seen her."
    $ victoriaSprite = 0
    $ charlotteSprite = 10
    "Phone" "Take it! Take it bitch! I'm gonna cum!"
    $ charlotteSprite = 1
    charlotte "W-Why would you show me this??! I knew this was a bad idea you disgusting pervert!"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Hey relax! It was just quicker than looking something up on the internet. At least this way you can see how your friends do it."
    $ playerSprite = 0
    $ charlotteSprite = 9
    "Phone" "Wait wait! Cum on my face!"
    "Phone" "Ahhh shit!"
    $ charlotteSprite = 10
    charlotte "Why...why were you filming..."
    $ charlotteSprite = 9
    "Phone" "*slurp* *slurp*"
    $ charlotteSprite = 10
    charlotte "Oh god...Oh this...I c-can't watch this."
    "Phone" "*Gulp*"
    $ charlotteSprite = 9
    charlotte "{i}What has he done to you Mia...{/i}"
    charlotte "{i}She looks so happy...and turned on..{/i}"
    charlotte "{i}I think I'm starting to...no! I can't get wet now!{/i}"
    $ charlotteSprite = 3
    show fbcharlotte current at surpriseshake:
        xalign 0.48 ypos 120
    charlotte "I'm done. This is over get out!"
    $ charlotteSprite = 2
    $ playerSprite = 1
    player "See what I mean? You get so angry so easily."
    $ playerSprite = 0
    $ charlotteSprite = 3
    charlotte "I'm not angry!!"
    $ charlotteSprite = 0
    $ playerSprite = 1
    show fbcharlotte current:
        xalign 0.5 ypos 120
    player "Alright flustered then."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "It's just the way you made her...suck..y-your...it's like she was a different person."
    $ playerSprite = 1
    player "Blowjobs aren't that big a deal, it's usually like step one of foreplay. And she acted like that because I like it."
    player "She feels sexy pleasing me and I feel good getting my cock sucked. That's all there is to it."
    $ playerSprite = 0
    $ charlotteSprite = 8
    charlotte "No..I-I can't."
    $ charlotteSprite = 0
    $ victoriaSprite = 1
    show fbvictoria current:
        xalign 0.7 ypos 120
    with move
    show fbcharlotte defaultflip:
        xalign 0.55 ypos 120
    victoria "Sigh. He has a point Mistress. Unless you go celibate or become a lesbian this is a part of life you're going to have to do."
    $ victoriaSprite = 0
    $ charlotteSprite = 1

    show fbcharlotte surpriseflip at surpriseshake:
        xalign 0.55 ypos 120
    charlotte "BLOWJOBS are a part of life?"
    $ charlotteSprite = 0
    victoria "Physical intimacy is. That's what your essay is on is it not?"
    charlotte "If you think it's so easy to suck him off Victoria why don't you go ahead and do it huh??!"
    $ charlotteSprite = 3
    show fbcharlotte current:
        xalign 0.5 ypos 120
    charlotte "Blow him right here!"
    $ charlotteSprite = 2
    victoria "...."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Charlotte. You're being ch-"
    hide fbplayer current
    show fbvictoria victoriabj1:
        xalign 0.2 ypos 120
    with Dissolve(0.7)
    $ charlotteSprite = 6
    player "....Uh.."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Che y-you can't fool me Vicky I know you're not...really gonna.."
    $ charlotteSprite = 0
    $ victoriaSprite = 1
    victoria "It is my job is to do what the Mistress says."
    $ playerSprite = 1
    player "Uh...but Victoria you don't-"
    $ charlotteSprite = 8
    show fbcharlotte current at surpriseshake:
        xalign 0.5 ypos 120
    show fbvictoria victoriabj2
    player "Okay that's my cock."
    charlotte "O-Okay I believe you Victoria y-you don't have to actua-"
    victoria "This can serve as a good lesson for you too Miss Charlotte."
    victoria "He's quite girthy."
    charlotte "...."
    player "{i}I'm just gonna...let this play out. I'm not responsible for what happens right?{/i}"
    image fbvictoria victoriahandjob1:
        "Sprites/victoriasuck2.png"
        0.7
        "Sprites/victoriasuck3.png"
        0.7
        repeat
    $ charlotteSprite = 5
    show fbvictoria victoriahandjob1:
        xalign 0.2 ypos 120
    window hide
    pause
    victoria "You want to have a strong and firm grip."
    player "Oh man."
    victoria "Most men can handle a tighter grip than you'd think."
    charlotte "...."
    image fbvictoria victoriahandjob2:
        "Sprites/victoriasuck2.png"
        0.35
        "Sprites/victoriasuck3.png"
        0.35
        repeat
    show fbvictoria victoriahandjob2:
        xalign 0.2 ypos 120
    window hide
    pause
    victoria "Clean strokes, the closer your face is to it the better."
    player "Jesus Victoria how are you so good at this?"
    victoria "See how he's getting excited already?"
    $ charlotteSprite = 8
    charlotte "I-I don't care."
    $ charlotteSprite = 3
    charlotte "And you! You're dating Mia you shouldn't be getting hard right now."
    $ charlotteSprite = 6
    player "This is NOT my fa-"
    image fbvictoria victoriahandjob3:
        "Sprites/victoriasuck2.png"
        0.15
        "Sprites/victoriasuck3.png"
        0.15
        repeat
    show fbvictoria victoriahandjob3:
        xalign 0.2 ypos 120
    player "Gah! Shit!"
    window hide
    pause
    victoria "When he's approaching climax, even more stimulation is recommended for the best possible orgasm."
    $ charlotteSprite = 5
    charlotte "{i}I can't look at them I'm too...too I don't know!{/i}"
    victoria "Showing one's breasts are an optimal way of achieving this."
    show fbvictoria victoriabj4:
        xalign 0.2 ypos 120
    with Dissolve(0.7)
    show fbcharlotte current at surpriseshake:
        xalign 0.5 ypos 120
    $ charlotteSprite = 8
    charlotte "Oh my god Vicky! What the hell!"
    player "{i}God Damn!{/i}"
    $ charlotteSprite = 5
    victoria "Even yours would do nicely Mistress, I know you're paranoid about your size."
    $ charlotteSprite = 8
    charlotte "I am n-not shut up!!"
    $ charlotteSprite = 6
    victoria "All men like breasts, is that not correct [povname]?"
    player "Yeah Charlotte your tits are fine no need to feel inse-"
    $ charlotteSprite = 8
    charlotte "I am NOT insecure!"
    show fbvictoria victoriabj5:
        xalign 0.2 ypos 120
    with Dissolve(0.7)
    player "Oh okay now you're blowing me."
    $ charlotteSprite = 7
    player "How are you doing that with you-"
    show fbvictoria victoriabj6:
        xalign 0.2 ypos 120
    player "Oh fuck I'm gonna cum. Was not expec-"
    show fbvictoria victoriabj6:
        xalign 0.2 ypos 120
    with vpunch
    player "AHHH! SHIT YES!!"
    with flash
    victoria "*Gulp gulp*"
    player "Shit Charlotte she's sucking every drop out of me!"
    charlotte "I...I-I..can see that..."
    player "How are your lungs so strong??!"
    show fbvictoria victoriabj7:
        xalign 0.2 ypos 120
    with vpunch
    player "Fuck!"
    charlotte "{i}He's still cumming?!{/i}"
    window hide
    pause
    show fbvictoria victoriabj8:
        xalign 0.2 ypos 120
    with Dissolve(1.0)
    victoria "Was that satisfactory Master [povname]?"
    player "You bitch you already know how...hah...how good that was.."
    victoria "Heh...maybe so."
    $ charlotteSprite = 5
    show fbvictoria victoriabj9:
        xalign 0.34 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 8
    show fbplayer current:
        xalign 0.2 ypos 120
    with Dissolve(0.5)
    charlotte "Uh...I'm....I gotta..."
    $ playerSprite = 9
    $ charlotteSprite = 6
    player "No it's fine Charlotte I understand."
    $ playerSprite = 8
    player "I don't think anybody in the world could blame you for wanting to rub one out right now."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "Don't...I'm not..."
    $ playerSprite = 1
    player "I'm gonna leave you to yourself. Have a good night alright?"
    $ playerSprite = 0
    charlotte "Okay..."
    $ playerSprite = 1
    player "Um it was nice meeting you Victoria."
    $ playerSprite = 0
    victoria "The pleasure was mine Master [povname]."
    $ playerSprite = 8
    player "You sure it's not the other way around?"
    $ playerSprite = 0
    victoria "Heh, perhaps you're right."
    scene fs blackblank
    with Dissolve(1.0)
    "Charlotte was all too happy to see the two of you leave her room"
    "You said your goodbyes to Victoria, still surprised at how good she was at fallatio."
    "It wouldn't do any harm to have a chat with her every once and a while you thought to yourself"
    $ charlottephase1interaction3 = 2
    $ charlottephase1interaction2 = 4
    if currentchapter >= 2:
        $ charlottequestlog = "I should explore Sunnyside some more during the morning."
    else:
        $ charlottequestlog = "Think I should avoid Charlotte till after the track meet."
    $ victoriaquesticon = "gui/questboxVictoria.png"
    $ victoriaquestlog = "Victoria is quite the beautiful woman..and sucks a mean dick."
    jump overworldmap

# end chapter 1