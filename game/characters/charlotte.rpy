# Charlotte scenes.

# Chapter 1


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

    charlotte "Ugh. I shouldn't've said that."
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
    player "Well that was interesting. It seems like she hates me but nobody is that straightforward when talking to someone they don't like for the first time, she had no tact at all."
    player "If I'm going to date Mia I'll need her friends to warm up to me. And I don't want to just run to Mia and complain..."
    player "I should go see her at the library in the afternoon."
    $ charlottephase1interaction1 = 1
    $ charlottequesticon = "gui/questboxCharlotte.png"
    if renpy.android:
        $ charlottequestlog = "{size=-25}Meet Charlotte at the library during Day.{/size}"
    else:
        $ charlottequestlog = "Meet Charlotte at the library during Day."
    hide fs classroom3blur
    hide fbplayer
    hide fbcharlotte
    jump classroom3


label charlottewonttalktome:
    hide screen charlotte_school
    hide screen backbuttonCLASSROOM
    player "Charlotte doesn't really want to talk to me right now, I should meet her in the library later."
    jump classroom3


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
    charlotte "Well....sort of, I live at home but they're often too busy to be...i-it doesn't matter! Yes I live with them. Technically."
    scene fs charlottelibraryplayer
    player "Great, so how'd you meet Mia?"
    scene fs charlottelibraryhappytalk
    charlotte "Oh I've known Mia since late grade school! I'm her earliest friend!"
    charlotte "Some bullies stole my lunch so I was crying. She sat down beside me and gave me half of her sandwich without saying anything."
    scene fs charlottelibraryhappyMCtalk
    player "Cucumber?"
    scene fs charlottelibraryhappytalk
    charlotte  "Haha yeah! Weird right? Anyways I was used to high class meals and said I didn't want her crappy sandwiches."
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
    $ charlottequestlog = "Visit Charlotte at the library again during Day."
    hide fs charlottelibrarycharlotte
    jump passtime


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
    charlotte "Well...You still shouldn't sneak up on people from behind. Who knows what your perverted brain was thinking about doing to me."
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

    charlotte "I'm sorry."
    scene fs blackblank
    with Dissolve(0.8)
    "Giving her a little grin you stand up and leave as promised"
    player "Well that was quit the interesting day, never thought I'd find out Charlotte would wet her thighs touching herself in the library of all places."
    player "She didn't even notice she was doing it! She's that starved for sexual....well sexual anything apparently."
    player "She was probably really embarrassed so I should see her again and show her I don't care about it and maybe she'll lay off of me about Mia every now and again."
    $ charlottephase1interaction1 = 3
    $ charlottequestlog = "Talk to Charlotte in Classroom 3 at school during Morning."
    hide fs blackblank
    jump passtime


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
    $ charlottequestlog = "Meet Charlotte at the library during Day."
    jump passtime


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
    $ charlottequestlog = "Bring $75 to the library during Day to buy a library card."
    jump passtime


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
    $ charlottequestlog = "Talk to Mia in Classroom 1 at school during Morning for help with Charlotte."
    $ charlottephase1interaction2 = 2
    jump passtime


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
            if timeofday == "Day":
                scene fs gymareaafternoon
            else:
                scene fs gymarea
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
    $ charlottequestlog = "Visit Charlotte's house at Night."
    jump passtime


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
        $ charlottequestlog = "Visit Charlotte at Cafe Seni in Sunnyside during Morning."
    else:
        $ charlottequestlog = "Continue exploring until the track meet on day 10."
    $ victoriaquesticon = "gui/questboxVictoria.png"
    $ victoriaquestlog = "Continue Charlotte's story in chapter 2 to unlock more visits with Victoria at Charlotte's house."
    jump overworldmap


# Chapter 2


label gohomecharlotte:
    $ sophiaSprite = 1
    sophia "Same here! It was such a hot day!"
    $ sophiaSprite = 0
    show fbava runfliptalk:
        xalign 0.25 ypos 120
    ava "Well thanks again everyone, bye!"
    hide fbava runflip
    with Dissolve(0.7)
    show fbcharlotte current:
        xalign 0.3 ypos 120
    $ charlotteSprite = 11
    charlotte "Bye!"
    $ charlotteSprite = 0
    $ sophiaSprite = 1
    sophia "Bye!"
    show fbsophia defaultfliptalk at surpriseshake:
        xalign 0.5 ypos 120
    sophia "Oh wait Emily did you still want me to come over?"
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ emilySprite = 1
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    emily "Yeah! I still have the ingredients ready for that pie you wanted to try."
    $ emilySprite = 0
    show fbsophia defaultfliptalk at surpriseshake:
        xalign 0.5 ypos 120
    sophia "Oh my gosh yes! Okay let's go!"
    show fbsophia defaultflip:
        xalign 0.5 ypos 120
    $ emilySprite = 1
    emily "Bye guys!"
    $ emilySprite = 0
    $ sophiaSprite = 1
    show fbsophia current:
        xalign 0.5 ypos 120
    sophia "Bye [povname]!"
    $ sophiaSprite = 0
    $ playerSprite = 1
    player "Bye girls."
    $ playerSprite = 0
    hide fbsophia
    with Dissolve(0.5)
    hide fbemily current
    with Dissolve(0.5)
    $ miaSprite = 1
    mia "See you!"
    show fbmia current:
        xalign 0.5 ypos 120
    with move
    mia "Shall we all hang out then?"
    $ miaSprite = 0
    $ oliviaSprite = 1
    show fbolivia current:
        xalign 0.65 ypos 120
    with move
    olivia "Sure. I'm not in a rush s-"
    $ oliviaSprite = 9
    show fbolivia current at surpriseshake:
        xalign 0.65 ypos 120
    show fbmia defaultflip:
        xalign 0.5 ypos 120
    olivia "Gah! I forgot I pre-ordered that new Kerokero game! It arrives today!!"
    olivia "Sorry I gotta go."
    hide fbolivia current
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Woah uh, okay bye."
    $ playerSprite = 0
    $ miaSprite = 3
    show fbmia current:
        xalign 0.5 ypos 120
    mia "Aww."
    $ miaSprite = 2
    show fbcharlotte defaultfliptalk:
        xalign 0.4 ypos 120
    charlotte "Didn't know Olivia could run that fast."
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ playerSprite = 1
    player "Sorry babe but I think I'm gonna leave alone too."
    $ playerSprite = 1
    $ miaSprite = 3
    mia "You are?"
    $ miaSprite = 2
    $ playerSprite = 1
    player "Yeah I'm taking a page in Ava's book and gonna take a shower."
    $ playerSprite = 7
    player "Is that how that expression goes?"
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.35 ypos 120
    charlotte "No?"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Well anyways yeah sorry Mia I feel gross so I'm headed home too."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Alrighty!"
    hide fbmia current
    hide fbplayer current
    show fbmia mcmiamakeout:
        xalign 0.25 ypos 120
    with Dissolve(0.5)
    $ charlotteSprite = 6
    show fbcharlotte current:
        xalign 0.4 ypos 120
    with move
    mia "Mmmmmm!"
    $ miaSprite = 1
    show fbmia current:
        xalign 0.55 ypos 120
    with Dissolve(0.5)
    show fbplayer current:
        xalign 0.3 ypos 120
    with Dissolve(0.5)
    mia "I'll talk to you tomorrow!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "For sure! Bye!"
    player "Charlotte, always a pleasure."
    $ playerSprite = 0
    $ charlotteSprite = 5
    charlotte "Ugh, j-just leave already."
    hide fbplayer current
    with Dissolve(0.7)
    charlotte "...."
    show fbcharlotte defaultfliptalk:
        xalign 0.4 ypos 120
    charlotte "So! You wanna hang out Mia?"
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ miaSprite = 1
    mia "Yeah!"
    $ miaSprite = 4
    mia "I just have to go to [povname]'s house to pick up my lipstick before going home to help my mom!"
    $ miaSprite = 0
    image fbcharlotte surpriseflip = im.Flip("Sprites/charlotte sprite blush.png",horizontal = True)
    image fbcharlotte happyflip = im.Flip("Sprites/charlottehappytalk.png", horizontal = True)
    show fbcharlotte surpriseflip:
        xalign 0.4 ypos 120
    charlotte "Wait, [povname]'s house? He JUST left."
    show fbcharlotte surpriseflip at surpriseshake:
        xalign 0.4 ypos 120
    charlotte "Wait again! You gotta help your mom??"
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ miaSprite = 1
    mia "Yup! we're unpacking some old boxes and she said:"
    $ miaSprite = 7
    show fbmia current:
        xalign 0.53 ypos 120
    mia "'Mia you better not forget you gotta come straight home after your friend's race this will take all night!'"
    $ miaSprite = 0
    show fbmia current:
        xalign 0.55 ypos 120
    mia "...."
    charlotte "...."
    $ miaSprite = 4
    mia ":)"
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk:
        xalign 0.4 ypos 120
    charlotte "But...if your mom said to come straight home then shouldn't you go straight home?"
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ miaSprite = 1
    mia "Yes! After I get my favorite lipstick I left at [povname]'s house I'll go straight home from the track....meet..."
    $ miaSprite = 3
    mia "Oh."
    $ miaSprite = 2
    show fbcharlotte happyflip:
        xalign 0.4 ypos 120
    charlotte "Get it now?"
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ miaSprite = 3
    mia "Oh yeah...darn."
    $ miaSprite = 2
    show fbcharlotte defaultfliptalk:
        xalign 0.4 ypos 120
    charlotte "It's just lipstick you can pick it up later, honestly the less you see of...him."
    charlotte "The better."
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ miaSprite = 3
    mia "But it's the lipstick you gave me for my birthday Charlotte, it's my favorite one!"
    $ miaSprite = 2
    show fbcharlotte surpriseflip:
        xalign 0.4 ypos 120
    charlotte "That...it's your favorite?"
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ miaSprite = 1
    mia "Could you go to [povname]'s house and get it for me? You can give it to me at school later."
    $ miaSprite = 0
    show fbcharlotte surpriseflip:
        xalign 0.4 ypos 120
    charlotte "Oh...I-I don't know Mia.."
    $ miaSprite = 4
    mia "Charlotte pllleeeease?"
    $ miaSprite = 0
    show fbcharlotte defaultfliptalk:
        xalign 0.4 ypos 120
    charlotte "Ugh I...Okay I guess."
    show fbcharlotte defaultflip:
        xalign 0.4 ypos 120
    $ miaSprite = 9
    mia "Thank you!!!"
    $ miaSprite = 4
    mia "Okay I should go bye!!!!"
    $ miaSprite = 0
    hide fbmia current
    with Dissolve(0.2)
    charlotte "{i}Oh God.{/i}"
    charlotte "{i}I'm still uncomfortable around him...when I think about what he did with Vicky I get all...{/i}"
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.4 ypos 120
    charlotte "...Fuck."
    $ charlotteSprite = 0
    hide fbcharlotte
    scene fs blackblank
    with Dissolve(0.7)
    "A little while later"
    scene fs livingroomnight

    show fbplayer toplesstoweltalk:
        xalign 0.3 ypos 120

    player "Phew!"
    player "That feels, SO much better."
    show fbplayer toplesstowel:
        xalign 0.3 ypos 120
    "*Ding Dong*"

    show fbplayer toplesstoweltalk:
        xalign 0.4 ypos 120
    with move

    player "Come in!"
    show fbplayer toplesstowel:
        xalign 0.4 ypos 120

    show fbcharlotte current:
        xalign 0.6 ypos 120

    charlotte "...."
    charlotte "{i}Holy shit his abs!{/i}"
    show fbplayer toplesstoweltalk:
        xalign 0.4 ypos 120
    player "Oh Charlotte. Uh hey?"
    show fbplayer toplesstowel:
        xalign 0.4 ypos 120
    $ charlotteSprite = 1
    charlotte "Hi. Mia left her lipstick here."
    $ charlotteSprite = 5
    show fbplayer toplesstowelfrown:
        xalign 0.4 ypos 120
    player "{i}Hmmm, she's acting a bit weird.{/i}"
    show fbplayer toplesstoweltalk:
        xalign 0.4 ypos 120
    player "Oh yeah, she did."
    player "And you're here to...?"
    show fbplayer toplesstowel:
        xalign 0.4 ypos 120
    $ charlotteSprite = 1
    charlotte "I'm picking it up. She realized right after you left that she had to go help her mom with something so she asked me to pick it up."
    $ charlotteSprite = 0
    show fbplayer toplesstoweltalk:
        xalign 0.4 ypos 120
    player "Why didn't you guys just call me if it was right after I left?"
    player "Could've driven you both home AND given her the lipstick."
    show fbplayer toplesstowel:
        xalign 0.4 ypos 120
    $ charlotteSprite = 6
    charlotte "...."
    $ charlotteSprite = 1
    charlotte "God damn it."
    charlotte "Well whatever, I'm here now so can I have it?"
    $ charlotteSprite = 0
    show fbplayer toplesstoweltalk:
        xalign 0.4 ypos 120
    player "Yeah sure it's in my room, hold this towel real quick and I'll go get it."
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    with Dissolve(0.5)

    show fbcharlotte towelhold:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    charlotte "Sure."
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    player "{i}Why she holding it like that? Weirdo.{/i}"
    hide fbplayer
    with Dissolve(0.5)
    charlotte "{i}Fuck...FUCK! Why can't I stop thinking about him??{/i}"
    charlotte "{i}This towel...he was just using it...smells so good?{/i}"
    charlotte "{i}Is this like...pheromones or something? God Mia...Mia gets fucked by him whenever...she w-wants..{/i}"
    show fbcharlotte towelsniff:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    charlotte "{i}I-I'm just gonna take a little sniff..{/i}"
    charlotte "{i}Before he comes back...ah....{/i}"
    hide window
    show fbcharlotte toweltouch:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    pause
    charlotte "{i}Mmmmm *sniff* yeah...yeah it's...{/i}"
    charlotte "{i}So Good!{/i}"
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    player "....."
    charlotte "Mmmmm."
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    player "*Ahem*."
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    $ charlotteSprite = 8
    show fbcharlotte current at surpriseshake:
        xalign 0.6 ypos 120
    charlotte "AH!"
    charlotte "Uh I...I-I was just-"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    player "You were sniffing my towel."
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    charlotte "No! No no no I was just sweaty and-"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    player "You were ALSO fingering yourself."
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte current:
        xalign 0.7 ypos 120
    with move
    charlotte "You're wrong! I-I gotta go I'm leaving!"
    show fbplayer shirtlessfrowntalk:
        xalign 0.5 ypos 120
    with move
    player "You take one more step towards that door and I'm calling Mia and letting her and everyone else know what you just did."
    show fbplayer shirtlessfrown:
        xalign 0.5 ypos 120
    $ charlotteSprite = 3
    charlotte "Shut the fuck up you fucking perv!"
    charlotte "Don't you threaten me! There's no way they'll believe y-you!"
    $ charlotteSprite = 2
    show fbplayer shirtlesstalk behind fbcharlotte:
        xalign 0.54 ypos 120
    with move
    player "I'm pretty sure Mia isn't the only one who knows about your masturbation problem. Emily seems like a trustworthy person to you."
    $ charlotteSprite = 5
    player "And if Emily knows you might as well tell the whole gang, they'd never give up your secret right?"
    show fbplayer shirtless:
        xalign 0.54 ypos 120
    charlotte "...."
    show fbplayer shirtlesstalk:
        xalign 0.54 ypos 120
    player "But even so. T'would be miiighty embarrassing for your friends to find out about this."
    player "Mia's such a beautiful and kind girl, and here you are betraying her."
    show fbplayer shirtless:
        xalign 0.54 ypos 120
    $ charlotteSprite = 6
    charlotte "I'm not betraying her!"
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    $ charlotteSprite = 5
    player "No no, you're just sneaking in a quick finger bang and towel sniff of your BEST FRIEND'S boyfriend. Did she even really ask you to get her lipstick?"
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    $ charlotteSprite = 4
    charlotte "She did! She d-did ask!"
    charlotte "Stop! S-Stop being *sniff* so mean!"
    $ charlotteSprite = 12
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    player "...."
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "So you're saying you're really just here for the lipsti-"
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    $ charlotteSprite = 4
    charlotte "Yes!"
    $ charlotteSprite = 12
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "The lipstick. And me seeing you touch yourself is just a misunderstanding?"
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    $ charlotteSprite = 4
    charlotte "That's what I said."
    $ charlotteSprite = 12
    show fbplayer shirtlesstalk:
        xalign 0.54 ypos 120
    player "So you're not turned on at all. By me or the situation I believe I caught you in?"
    show fbplayer shirtless:
        xalign 0.54 ypos 120
    $ charlotteSprite = 5
    charlotte "N-No."
    show fbplayer shirtlesstalk:
        xalign 0.54 ypos 120
    player "You're dry as a bone."
    show fbplayer shirtless:
        xalign 0.54 ypos 120
    charlotte "Yeah..."
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "Okay. Prove it."
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    $ charlotteSprite = 6
    charlotte "What?"
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "Lift up your skirt and show me that you're not wet. No not even wet, show me you're not SOAKING wet right now."
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    $ charlotteSprite = 3
    charlotte "You asshole you always fucking perv-"
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "And I'll break up with Mia."
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    $ charlotteSprite = 6
    charlotte "W-What?"
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "I'm tired of you spouting such hypocritical nonsense."
    player "So if you prove to me you're not insanely turned on right now, I will break up with Mia and never talk to you or your friends ever again."
    show fbplayer shirtlesstalk:
        xalign 0.54 ypos 120
    player "Oh, and you're free to punch me in the face and tell them all about how I've been 'perving' on you."
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    $ charlotteSprite = 5
    charlotte "...No I.."
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "We can end this right here, right now."
    player "This is EVERYTHING you wanted, since the moment we met."
    player "If you walk away now you're admitting how much of a closet slut you are."
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    charlotte "{i}No..fuck...FUCK! How did I let him talk me into a corner like this?{/i}"
    show fbplayer shirtlessfrowntalk:
        xalign 0.54 ypos 120
    player "Well?"
    show fbplayer shirtlessfrown:
        xalign 0.54 ypos 120
    charlotte "{i}I have no choice, I HAVE NO CHOICE!{/i}"
    $ charlotteSprite = 6
    charlotte "F-Fine! I'll p-prove it to you!"
    show fbplayer shirtless:
        xalign 0.54 ypos 120
    player "{i}Finally.{/i}"
    scene fs blackblank
    with Dissolve(1.0)
    player "Let me turn the lights on."
    charlotte "D-Do you really have to?"
    player "I want to see you Charlotte."
    charlotte "...."
    scene fs charlottechapter1end1
    with Dissolve(1.0)
    charlotte "Okay."
    scene fs charlottechapter1end2
    charlotte "So j-just a little peek alright?"
    charlotte "That's all."
    player "Uh huh."
    scene fs charlottechapter1end3
    charlotte "{i}Oh my god oh my god!!{/i}"
    scene fs charlottechapter1end4
    with Dissolve(0.7)
    charlotte "{i}What the hell am I doing? Please don't notice how wet I am!!{/i}"
    player "Come closer."
    scene fs charlottechapter1end5
    with Dissolve(0.7)
    player "Wow."
    player "That is...that is a lot."
    charlotte "I-It's just sweat! I'm really nervous!!"
    player "Charlotte you're not fooling anyone. There no way you can't feel that."
    charlotte "Oh God I want to die..."
    player "I've never seen such a cute pussy. I love how smooth you are too."
    charlotte "...."
    player "It just...makes me..."
    charlotte "O-Okay you've looked now can we-"
    player "Wanna..."
    player "...."
    scene fs charlottechapter1end6
    with vpunch
    play sound "audio/charlottegameaudio/charlottesmallmoan.wav"
    charlotte "OH!"
    player "Mphmm."
    charlotte "[povname] what the hell??"
    play sound "audio/charlottegameaudio/charlotteeatoutmoan.wav"
    charlotte "You can't....oh fuck!"
    player "MMMMM!"
    charlotte "{i}Shit shit shit that feels so good!{/i}"
    charlotte "{i}I have to tell him to stop but...t-the words just aren't coming out{/i}"
    "After the inital shock was gone and it was clear that neither of you wanted to stop, Charlotte removed her skirt and grabbed your head"
    scene fs charlottechapter1end7
    with Dissolve(0.7)
    play sound "audio/charlottegameaudio/charlottethisdoesntfeelgoodatall.wav"
    charlotte "This....hah.."
    charlotte "This doesn't feel good at all!"
    scene fs charlottechapter1end9
    with Dissolve(0.7)
    charlotte "I-If you think..hah..that I'm enjoying th-"
    scene fs charlottechapter1end10
    play sound "audio/charlottegameaudio/charlotteeatoutmoan.wav" loop
    charlotte "AHN! This.."
    charlotte "You are dead wrong m-mister!"
    scene fs charlottechapter1end9
    charlotte "AHN!!!"
    scene fs charlottechapter1end11
    charlotte "I am..."
    scene fs charlottechapter1end12
    charlotte "N-Not-"
    charlotte "OH MY GOOOD!"
    scene fs charlottechapter1end13
    charlotte "{i}Fuck fuck fuck!!{/i}"
    scene fs charlottechapter1end12
    charlotte "That's so good that's so goood!!"
    charlotte "I..I'm getting close!!"
    scene fs charlottechapter1end13
    charlotte "I'm...OH GOD!"
    scene fs charlottechapter1end11
    stop sound
    voice "audio/charlottegameaudio/charlottedaddy.wav"
    charlotte "D-Daddy!"
    scene fs charlottechapter1end14
    with flash
    charlotte "Daddy I'm cumming!!"
    scene fs charlottechapter1end8
    with vpunch
    stop sound
    voice "audio/charlottegameaudio/charlottecuming1.wav"
    charlotte "AHHHH! YES DADDY!"
    with flash
    charlotte "My legs are giving out!!"
    player "{i}Holy shit it's getting all over my face!{/i}"
    window hide
    pause
    scene fs blackblank
    with Dissolve(1.0)
    "The two of you stand up and Charlotte regains a little bit of her composure"
    player "Let me get the lights."
    charlotte "Okay."
    scene fs livingroomnight
    with Dissolve(0.7)

    show fbplayer shirtless:
        xalign 0.4 ypos 120
    with Dissolve(0.7)

    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    with Dissolve(0.7)

    charlotte "...."
    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    player "'Daddy'?"
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "Please...just forget about that."
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    player "Haha alright, for now."
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "So..."
    charlotte "Are you going to tell Mia?"
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120


    menu:
        "{color=#3eab33}Romantic{/color}":
            jump charlottechapter1romance
        "{color=#dd3939}Naughty{/color}":
            jump charlottechapter1naughty


label charlottechapter1naughty:
    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    player "That depends."
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "O-On what?"
    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "Do you really think it's fair?"
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "Huh?"
    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "Do you think it's fair that you get to cum and I don't?"
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "What?? N-No you can't be se-"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "Get on your knees."
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "Please! [povname] I-I won't tell Mia or the girls about this just let me leave!"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "ONE. You can leave whenever you want I'm not keeping you here, there'll simply be consequences."
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "Bu-"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "TWO!"
    player "You studied a lot about sex right? You know what blue balls is?"
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "Um y-yes I remember reading about it."
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "What did it say?"
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "That it can be...painful?"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "So you're going to come into my home, seduce me!"
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "I didn't seduc-"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "CUM all over my FACE!"
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "I..."
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "And then just fucking leave?"
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "I'm sorry alright!"
    show fbplayer shirtlessfrowntalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "I don't want your apology Charlotte, I want you on your knees."
    show fbplayer shirtlessfrown:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk at surpriseshake:
        xalign 0.6 ypos 120
    charlotte "O-Okay fine alright!!"
    charlotte "This is just to make things even! I won't enjoy this!"
    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120
    player "Yeah sure."
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    scene fs charlottechapter1endnaughty1
    with Dissolve(1.0)
    window hide
    pause
    scene fs charlottechapter1endnaughty2
    charlotte "S-So what..what should I do?"
    scene fs charlottechapter1endnaughty1
    player "Just stay there like a good girl."
    scene fs charlottechapter1endnaughty3
    with vpunch
    charlotte "Oh my god!"
    scene fs charlottechapter1endnaughty3charlotte
    player "Yeah you like that don't you?"
    scene fs charlottechapter1endnaughty3charlottetalk
    charlotte "N-No!"
    scene fs charlottechapter1endnaughty3charlotte
    player "Pretty different seeing it up close huh?"
    scene fs charlottechapter1endnaughty3
    charlotte "{i}How is that supposed to fit inside..my..{/i}"
    charlotte "...."
    player "You thinking about me fucking Mia with this? Stretching out her pussy?"
    player "Or maybe your maid Victoria? How she wrapped her lips and let me deepthroat her. Fuck did that feel good."
    scene fs charlottechapter1endnaughty3charlottetalk
    charlotte "I'm...no..."
    scene fs charlottechapter1endnaughty3charlotte
    player "Or maybe you're thinking about sucking it yourself?"
    scene fs charlottechapter1endnaughty4
    with Dissolve(0.7)
    window hide
    pause
    player "Yeah that's probably it isn't it?"
    scene fs charlottechapter1endnaughty4b
    charlotte "W-Wait my hair!!"
    scene fs charlottechapter1endnaughty5
    window hide
    play sound "audio/skin smack.wav"
    pause
    scene fs charlottechapter1endnaughty4
    player "Tell me Charlotte, are you a good girl?"
    scene fs charlottechapter1endnaughty4b
    charlotte "H-Huh?"
    scene fs charlottechapter1endnaughty5
    window hide
    play sound "audio/skin smack.wav"
    pause
    scene fs charlottechapter1endnaughty4
    player "I asked you if you were a good girl!??"
    scene fs charlottechapter1endnaughty4b
    voice "audio/charlottegameaudio/charlotteimagoodgirl.wav"
    charlotte "Y-yes I'm...I'm a good girl Daddy."
    scene fs charlottechapter1endnaughty5
    window hide
    play sound "audio/skin smack.wav"
    pause
    scene fs charlottechapter1endnaughty6
    with Dissolve(0.7)
    play sound "audio/charlottegameaudio/charlottedickonlips.wav" loop
    player "Hmmm 'Daddy'. I do like that."
    player "You have such soft lips Charlotte."
    charlotte "Shan keyuu.."
    player "I think I'm going to cum all over your pretty face."
    player "You want that?"
    charlotte "...."
    player "I asked you a question."
    charlotte "Yesh...pwease."
    player "Oh yeah that's it..."
    player "Fuck here it comes!"
    stop sound
    scene fs charlottechapter1endnaughty7
    voice "audio/charlottegameaudio/Charlotteah.wav"
    with vpunch
    window hide
    pause
    with flash
    scene fs charlottechapter1endnaughty8
    pause
    scene fs charlottechapter1endnaughty7
    with flash
    scene fs charlottechapter1endnaughty8
    player "YESS FUCK ME."
    scene fs charlottechapter1endnaughty9
    with Dissolve(1.0)
    player "Ahh that was good baby."
    charlotte "...."
    scene fs blackblank
    with Dissolve(1.0)
    charlotte "W-We're even now right?"
    player "Heh, yeah sure."
    charlotte "...."
    player "You look so sexy covered in my cum."
    voice "audio/charlottegameaudio/charlottethanks.wav"
    charlotte "Thank you Daddy."
    player "That's a good girl."


    $ endchapter1_trigger = "1 charlotte naughty"


    jump startofchapter2


label charlottechapter1romance:

    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    player "No I'm not going to tell Mia anything."
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    charlotte "...."

    show fbplayer shirtlesstalk:
        xalign 0.4 ypos 120
    player "I'm gonna go put my shirt on. You should uh..wash up, bathroom's down the hall."
    show fbplayer shirtless:
        xalign 0.4 ypos 120
    show fbcharlotte skirtlesstalk:
        xalign 0.6 ypos 120
    charlotte "Okay."
    show fbcharlotte skirtless:
        xalign 0.6 ypos 120


    scene fs charlottechapter1endromantic3
    with Dissolve(1.0)
    window hide
    pause
    player "{i}Wow. That really just happened.{/i}"
    player "{i}Can't deny that I enjoyed making her cum all over my face. Making a girl cum must be like a universal thing all guys covet.{/i}"
    player "{i}And that 'Daddy' thing? God damn that really turned me on.{/i}"
    player "{i}It's not crazy to think...that I might like Charlotte more than I thought.{/i}"
    scene fs charlottechapter1endromantic1
    with Dissolve(0.7)
    charlotte "Hey so..."
    charlotte "I'm just gonna go now."
    scene fs charlottechapter1endromantic2
    player "Not yet you aren't."
    scene fs charlottechapter1endromantic1
    charlotte "{i}I knew he was going to keep me here.{/i}"
    charlotte "{i}Is he going to still blackmail me in the end?{/i}"
    scene fs charlottechapter1endromantic2
    player "Your legs must still be tired."
    scene fs charlottechapter1endromantic1
    charlotte "?"
    scene fs charlottechapter1endromantic2
    player "I can't let you go home until you rest a bit so just sit on my lap."
    scene fs charlottechapter1endromantic1
    charlotte "Your lap?"
    scene fs charlottechapter1endromantic2
    player "Yeah."
    scene fs charlottechapter1endromantic1
    charlotte "...."
    scene fs charlottechapter1endromantic4
    charlotte "Okay.."
    charlotte "Like this?"
    player "What the fuck? No Charlotte."
    scene fs charlottechapter1endromantic5charlotte
    with vpunch
    charlotte "Ah!"
    scene fs charlottechapter1endromantic5player
    player "Like this."
    scene fs charlottechapter1endromantic5charlotte
    charlotte "But...we're.."
    scene fs charlottechapter1endromantic5player
    player "You're not a real man if you don't cuddle with a girl after you've made her cum."
    player "S'like a rule."
    scene fs charlottechapter1endromantic5
    charlotte "...."
    scene fs charlottechapter1endromantic5player
    player "Just rest Charlotte. You can leave whenever you want."
    scene fs charlottechapter1endromantic5
    charlotte "...."
    scene fs charlottechapter1endromantic5charlotte
    charlotte "Okay thank you.."
    scene fs charlottechapter1endromantic7
    with Dissolve(1.0)
    "Uncharacteristically, Charlotte put her arms around you and held you while closing her eyes."
    "You felt calm as you took in her scent and closed your own as well"

    scene fs charlottechapter1endromantic8
    with Dissolve(0.7)
    hide window
    pause
    charlotte "*sniff*..."
    player "{i}She's so different when her barriers are down...{/i}"
    scene fs charlottechapter1endromantic9b
    with Dissolve(0.7)
    player "You okay? You're still crying a bit."
    scene fs charlottechapter1endromantic10
    charlotte "Yeah, just...just a bit emotional you know?"
    scene fs charlottechapter1endromantic9b
    player "I'm sorry about being so...aggressive before."
    scene fs charlottechapter1endromantic10
    charlotte "It's okay...I might've been harsh on you before too."
    charlotte "But I DEFINITELY didn't...like it."
    scene fs charlottechapter1endromantic9b
    player "Yeah that must've been a TERRIBLE experience."
    scene fs charlottechapter1endromantic10
    charlotte "I would never..."
    charlotte "Ever forgive someone...who did..."
    charlotte "That to me."
    scene fs charlottechapter1endromantic9
    player "...."
    charlotte "...."
    scene fs charlottechapter1endromantic11
    with Dissolve(0.7)
    play sound "audio/charlottegameaudio/charlottemakeout.wav" loop
    charlotte "Mmmm."
    scene fs charlottechapter1endromantic12
    with Dissolve(0.5)
    player "Mmmhph."
    scene fs charlottechapter1endromantic13
    charlotte "Ah...hah...hah."
    player "...."
    scene fs charlottechapter1endromantic12
    charlotte "MMMM!"
    scene fs charlottechapter1endromantic11
    window hide
    pause
    charlotte "{i}What am I doing?? I can't stop!{/i}"
    scene fs charlottechapter1endromantic12
    with Dissolve(0.5)
    charlotte "{i}He tastes so good..I FEEL so good.{/i}"
    scene fs charlottechapter1endromantic13
    with Dissolve(0.5)
    stop sound
    charlotte "Ahh.."
    scene fs charlottechapter1endromantic9b
    with Dissolve(1.0)
    player "That's the best apology I think I can give you."
    player "Here let me grab the blanket."
    scene fs charlottechapter1endromantic14
    with Dissolve(1.0)
    window hide
    pause
    scene fs blackblank
    with Dissolve(1.0)
    charlotte "...."
    charlotte "It wasn't bad."
    player "Good night Charlotte."
    charlotte "Good night Daddy."
    charlotte "{i}I said it again...{/i}"


    $ endchapter1_trigger = "1 charlotte romantic"


    jump startofchapter2


label charlottephase2interaction1part1:
    hide screen exit_cafe
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbcharlotte current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    $ playerSprite = 1
    player "Charlotte hey!"
    $ charlotteSprite = 1
    charlotte "Oh...hey [povname]."
    charlotte "I didn't think you came here."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Yeah I'm trying to expand my horizons I guess, branch out to more places."
    player "You guys love to come here right? So I figured I should check it out too."
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "That's great.."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I guess we should have a talk huh?"
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "I don't know."
    charlotte "Maybe."
    charlotte "No."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Okay, I think saying your thoughts and feelings might be too hard for you."
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "What?"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "So how about you let me do the talking and we can go from there."
    $ playerSprite = 0
    charlotte "...."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "So, I like you. I do I really do."
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "Um, okay..."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "I love how short you are and how mad you get. At first I thought your whole contrarian 'Tsundere' thing was annoying."
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "Whatdere?"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "But it grew on me and it's kinda endearing now."
    player "Now I know you like me too."
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "I think you're making a lot of assumptions right now."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "So you don't need to tell me if it's too embarrassing for you. I know how you feel."
    player "So let's spend some time together, get closer. See where this goes you know?"
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "I feel like I'm not being heard right now."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "If it's not meant to be then we can just forget it, act like we never happened."
    $ charlotteSprite = 1
    $ playerSprite = 0
    charlotte "'WE' didn't happen! You just took advantag-"
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Ah! Shhh."
    player "It's okay, I got this."
    player "Text me when you're ready to....get closer."
    player "Bye!"
    $ playerSprite = 0
    hide fbplayer current
    with Dissolve(0.7)
    show fbcharlotte current:
        xalign 0.45 ypos 120
    with move
    charlotte "....."
    $ charlotteSprite = 1
    charlotte "Oh no."
    charlotte "No no no no."
    charlotte "You have this all wrong [povname]."
    charlotte "I'm gonna change this dynamic RIGHT NOW."
    $ charlotteSprite = 9
    charlotte "{cps=25}Vicky!{/cps}"
    victoria "{cps=25}Yes?{/cps}"
    charlotte "{cps=25}I'm calling a house meeting right now!{/cps}"
    victoria "{cps=25}What is it concerning Mistress Charlotte?{/cps}"
    charlotte "{cps=25}Taking back control.{/cps}"
    victoria "{cps=25}I'll get everything ready miss.{/cps}"
    charlotte "{cps=25}I'll be there in 15.{/cps}"
    victoria "{cps=25}Understood.{/cps}"

    $ charlottephase2interaction1 = 1
    $ charlottequestlog = "Go to sleep at Night for Charlotte's message."
    jump gotosunnyside


label charlottephase2interaction1part1NIGHT:
    hide screen backbuttonROOM
    hide screen uppergui
    scene fs playerbedneutral
    with Dissolve(0.7)
    player "....."
    "VVVVVP VVVVVP"
    scene fs playerbedthink2
    player "Huh? Who's texting me at this hour?"
    scene fs playerroomNight
    with Dissolve(0.7)
    charlotte "{cps=25}[povname] Wake up!{/cps}"
    player "{cps=25} Charlotte? It's the middle of the night what is it?{/cps}"
    charlotte "{cps=25} I just...I need to see you.{/cps}"
    player "{cps=25} Can't it wait until tomorrow?{/cps}"
    charlotte "{cps=25}No I can't wait. I need to talk to you now!{/cps}"
    player "{cps=25}Alright alright I'm on my way.{/cps}"
    player "Man [povname] you charmer. I bet I could sooth a pissed off lioness given the chance haha!"
    player "I better head over there. See what she's got for me."
    scene fs overworldnight
    with Dissolve(0.5)
    "You hop in your car and make the quick ride over to Charlotte's mansion"
    "You find that the gate and front door are both unlocked, so you let yourself in and head to Charlotte's room"
    scene fs charlotteroom
    with Dissolve(0.7)
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.35 ypos 120
    with Dissolve(0.5)
    player "Hey Charlotte, I'm here."
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    charlotte "Oh [povname]! Thanks so much for coming..."
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "So, what was so urgent you needed to see me in the middle of the night?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "I was just thinking...about what you said."
    charlotte "And you're right, about everything!"
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "Yeah?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Yes and...I just...I just can't hold back!"
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "Hold back?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "My URGES [povname] I can't hold back my URGES!"
    charlotte "I need a MAN, I need..you. To help me find release."
    charlotte "So I can think properly again!"
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "Oh well...you know, I can certainly try my best to help."
    player "Would you like me to...help you tonight?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Well...before we take that one step I-I need you to get some things for me..."
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "What things?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "I-I wrote them down on this piece of paper. It's too embarrassing to say them out loud."
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "Alright no problem."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Once you have them come back...and..well hehe.."
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "Hehe okay I think I understand. I'll get these things real quick alright?"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Please do! I'm getting wetter by the second!"
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "{i}Oh fuck, nice.{/i}"
    player "Alright bye!"
    hide fbplayer current
    with Dissolve(0.5)
    charlotte "...."
    $ charlotteSprite = 1
    charlotte "Idiot."
    hide fbcharlotte current
    with Dissolve(0.5)
    scene overworldnight
    with Dissolve(0.7)
    player "Alright let's see what this paper says..."
    player "One Camera, one...Fuzzy handcuffs, oh wow kinky. And one box of condoms."
    player "Holy shit she's serious! Wonder why she wants the camera...to record us I guess? Kinda hot."
    player "Alright I'll work on getting all this done tomorrow!"
    $ charlottephase2interaction1 = 2
    $ charlottequestlog = "Get a camera, condoms, and handcuffs from the mall store. Visit Charlotte's house at Night."
    jump gotosleep


label charlottephase2interaction1part2:
    stop music fadeout 2
    scene fs charlotteroom
    with Dissolve(0.7)
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.45 ypos 120
    with Dissolve(0.5)
    "As you enter you put all the items you collected on a little corner table"
    player "Hey Charlotte I'm back."
    $ playerSprite = 0
    $ charlotteSprite = 1
    show fbcharlotte current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    charlotte "That's great!"
    charlotte "D-Did you get everything I asked?"
    $ charlotteSprite = 0
    if cameracount == 1 or condomcount == 1 or handcuffcount == 1:
        $ playerSprite = 1
        player "Ah no sorry."
        $ playerSprite = 0
        $ charlotteSprite = 1
        charlotte "Go get them [povname]! I can barely wait anymore!"
        $ charlotteSprite = 0
        jump overworldmap

    $ playerSprite = 1
    player "Yeah I put them on the table over there."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Great!"
    charlotte "So I guess..we should get started then."
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "Okay so...what exactly a-"
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Shhh...you've done such a GOOD job."
    $ charlotteSprite = 0
    $ playerSprite = 1
    player "Well I just bought a couple things."
    $ playerSprite = 0
    $ charlotteSprite = 1
    charlotte "Enough talking. Take off your clothes..."
    $ playerSprite = 1
    $ charlotteSprite = 0
    player "Don't need to tell me twice."
    show fbplayer pullshirt:
        xalign 0.45 ypos 120
    with Dissolve(0.5)
    pause
    show fbplayer shirtless:
        xalign 0.45 ypos 120
    with Dissolve(0.5)
    charlotte "{i}Oh boy...{/i}"
    show fbplayer shirtlessdick:
        xalign 0.45 ypos 120
    with Dissolve(0.5)
    charlotte "{i}Oh God it's really happening.{/i}"
    show fbplayer naked:
        xalign 0.45 ypos 120
    with Dissolve(0.5)
    pause
    $ charlotteSprite = 1
    charlotte "I guess..."
    show fbcharlotte naked2:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    charlotte "I-It's my turn."
    show fbcharlotte naked1:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    charlotte "{i}C'mon Charlotte you can do this, you're almost there!{/i}"
    show fbcharlotte naked2:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    charlotte "I hope y-you're ready [povname]."
    show fbcharlotte naked3:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    player "{i}I'm finally gonna see Charlotte's tits!{/i}"
    show fbcharlotte naked4:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    pause
    show fbcharlotte naked5:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    player "Fuck..."
    player "Charlotte you're beautiful."
    charlotte "Yeah? You like my cute little titties?"
    player "I do."
    show fbcharlotte nakedflip:
        xalign 0.5 ypos 120
    with move
    charlotte "Put the handcuffs on me [povname]"
    player "The handcuffs?"
    charlotte "Yeah I w-want you to...dominate me?"
    player "Sure alright."
    player "{i}She's acting a bit weird but honestly I'm too horny to care right now.{/i}"
    show fbcharlotte naked6:
        xalign 0.6 ypos 120
    with move
    charlotte "Mmmm."

    show fbcharlotte naked7:
        xalign 0.6 ypos 120
    charlotte "Yeah there we go, now I can barely move."
    show fbcharlotte naked6:
        xalign 0.6 ypos 120
    player "I guess so huh?"
    show fbcharlotte naked7:
        xalign 0.6 ypos 120
    charlotte "I'm at your complete mercy!"


    scene fs charlottenakedcummingtrick1charlotte
    with Dissolve(1.0)
    charlotte "Does that turn you on?"
    charlotte "Having such a tiny helpless girl naked in front of you?"
    scene fs charlottenakedcummingtrick1player
    player "Well shit Charlotte I think given the circumstances yeah I'm pretty fucking turned on."
    scene fs charlottenakedcummingtrick3
    with Dissolve(0.5)
    play sound "audio/charlottegameaudio/charlottepanting1.wav" loop
    charlotte "So what do you want to do to me?"
    charlotte "Hmm?"
    charlotte "Do you want to fuck me like I saw you fuck Mia?"
    scene fs charlottenakedcummingtrick4
    with Dissolve(0.5)
    player "Ah..."
    charlotte "Personally I...hah...want it a little rougher."
    charlotte "You could pin me down...hah...on the bed."
    player "Shit..."
    scene fs charlottenakedcummingtrick5
    with Dissolve(0.5)
    charlotte "Stretch my....tight little pussy...ahn...with that huge cock of yours."
    charlotte "Pound me until I can't think anymore."
    player "{i}Fuck why is her skin so soft?! Just listening to her and seeing her naked is really getting me going!{/i}"
    charlotte "Pull my hair and make me scream!"
    charlotte "And then when you're done with me you c-could.."
    charlotte "Cum. ALL over me."
    stop sound
    voice "audio/charlottegameaudio/charlotteplease.wav"
    charlotte "Please!"
    voice "audio/charlottegameaudio/charlottesmallmoan.wav"
    charlotte "Daddy please! Cum for me!!"
    player "Shit Charlotte I.."
    player "FUCK!"
    scene fs charlottenakedcummingtrick6
    with vpunch
    player "AHHHG!"
    scene fs charlottenakedcummingtrick7
    with flash
    player "AHH Fuck that's so good!"
    scene fs charlottenakedcummingtrick8
    with Dissolve(0.5)
    charlotte "...."
    pause

    scene fs charlotteroom
    with Dissolve(0.7)

    show fbplayer nakedcum:
        xalign 0.5 ypos 120
    show fbcharlotte naked8:
        xalign 0.6 ypos 120
    with Dissolve(0.5)

    charlotte "{i}Keep it together! You're almost done now!{/i}"
    voice "audio/charlottegameaudio/charlottephew.wav"
    charlotte "*Phew*..."
    play sound "audio/camerasnap.mp3"
    with flash

    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    player "Huh? What was that flash?"

    show fbcharlotte naked9:
        xalign 0.6 ypos 120
    voice "audio/charlottegameaudio/charlottehehehe.wav"
    charlotte "Hehehehe."
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    voice "audio/charlottegameaudio/charlottehah.wav"
    charlotte "HAH!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "Uhhhh."
    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "YOU FOOL!"
    charlotte "You fell for it, hook line and sinker!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "This is weird. You're being weird."
    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "You're finished [povname]! Vicky you got the picture?"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120

    show fbvictoria camera:
        xalign 0.75 ypos 120
    with Dissolve(0.5)
    victoria "Yes ma'am."
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "Oh hey Victoria."
    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    victoria "Hello Master [povname]."
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "I now have photo evidence of you cumming all over me while I'm naked!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "Kay?"
    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "Now you're gonna do everything I say or I'll show it to Mia and the other girls!"
    charlotte "Your true nature will be revealed! Do I still look like I'm too embarrassed to function around sex huh??"
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    player "Yeah it does seem like you're getting over that. So this is...blackmail?"
    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "Yes!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "But you're in the picture too?"
    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "Look at me, my clothes are gone and I'm handcuffed with spunk all over me. All I have to do is say you forced me into some nefarious situation."
    charlotte "And everyone will see me as the victim, 100 percent!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "So you let me see you naked, acted all naughty, touched my dick, and let me cum all over you so you could hold this over my head?"
    show fbplayer nakedcumsurprise:
        xalign 0.5 ypos 120
    charlotte "...."
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "Yeah!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "Wow you uh. You sure got me!"
    show fbplayer nakedcum:
        xalign 0.5 ypos 120
    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "I sure did!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "I guess I have no choice but to do as you say for the next few weeks at least."
    show fbplayer nakedcum:
        xalign 0.5 ypos 120

    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "That's right!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "Okay so...can I go home?"
    show fbplayer nakedcum:
        xalign 0.5 ypos 120

    show fbcharlotte naked9b:
        xalign 0.6 ypos 120
    charlotte "Uh...yes! I allow you to leave!"
    show fbcharlotte naked9c:
        xalign 0.6 ypos 120
    show fbplayer nakedcumtalk:
        xalign 0.5 ypos 120
    player "Alrighty great. Hey Vicky could you send me a copy of that picture you took when you get the chance."
    victoria "Yes of course master [povname]."
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.5)
    player "Thanks. Bye!"
    $ playerSprite = 0

    hide fbplayer
    with Dissolve(0.5)
    charlotte "....."
    show fbcharlotte naked10 at surpriseshake:
        xalign 0.6 ypos 120
    charlotte "Ohmygodohmygodohmygod!"
    charlotte "Vicky Viiiicky!"
    $ victoriaSprite = 1
    show fbvictoria current:
        xalign 0.75 ypos 120
    with Dissolve(0.5)
    victoria "Shhhh, you did very well Miss Charlotte."
    $ victoriaSprite = 0
    charlotte "I-It's all oooover meee!"
    $ victoriaSprite = 1
    victoria "Let's get you cleaned up."
    $ victoriaSprite = 0
    scene fs blackblank
    with Dissolve(1.0)
    player "Well that was interesting. I really don't give a shit about her 'blackmail' but it should be fun to play along with her for now."
    $ charlottephase2interaction1 = 3
    $ charlottephase2interaction2 = 1
    $ charlotteblackmailday = dayNumber + 1
    $ charlottequestlog = "Get some sleep at Night, then return to your bedroom during Morning for Charlotte's message."
    $ victoriaquestlog = "Visit Victoria at Charlotte's house at Night."
    jump gotosleep


label charlottephase2interaction2part1:
    scene fs playerroomMorn
    with Dissolve(0.7)

    "Briiing briiing"
    player "Hello?"
    mia "[povname]! Good morning!"
    player "Morning Mia."
    mia "Come to the cafe! Charlotte and I are having brunch and I wanted to invite you!"
    player "Oh sure yeah that'll be fun. See you there."
    $ charlottequestlog = "Join Mia and Charlotte at Cafe Seni during Morning."
    $ charlottephase2interaction2 = 3
    jump returnwhereyouare


label charlottephase2interaction2part2:
    stop music fadeout 5
    stop sound fadeout 5
    hide screen exit_cafe

    $ miaSprite = 0
    $ charlotteSprite = 0
    $ playerSprite = 1
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbmia current:
        xalign 0.5 ypos 120
    show fbcharlotte current:
        xalign 0.6 ypos 120
    with Dissolve(0.7)
    player "Good morning."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "Morning!"
    $ miaSprite = 0
    $ charlotteSprite = 1
    charlotte "Hi."
    $ charlotteSprite = 0
    charlotte "{i}Why did Mia have to invite him this time??{/i}"
    charlotte "{i}I can't threaten him with blackmail if she's here.{/i}"
    $ playerSprite = 1
    player "Let's order some food then sit down."
    $ playerSprite = 0
    $ miaSprite = 1
    mia "I'm getting ice cream!"
    $ miaSprite = 0
    $ playerSprite = 1
    player "Haha okay."
    $ playerSprite = 0
    scene fs charlotteseesmiamc1a
    with Dissolve(0.7)
    player "{i}I like sleeping in but this is nice too.{/i}"
    scene fs charlotteseesmiamc1b
    mia "*Girl talk*"
    scene fs charlotteseesmiamc1a
    charlotte "*More girl talk*"
    scene fs charlotteseesmiamc2
    with Dissolve(0.5)
    player "How's everyone's stuff? My mocha is pretty good!"
    play sound "audio/straw-slurp.wav"
    charlotte "*Siiiip*"
    scene fs charlotteseesmiamc3
    mia "Oh yeah for sure! This ice cream is great!"
    mia "I love all the new flavors they have!"
    charlotte "S'good."
    scene fs charlotteseesmiamc4
    mia "Ah!"
    charlotte "Geez Mia again?"
    mia "It's fine!"
    mia "Let me just.."
    scene fs charlotteseesmiamc5
    player "Haha."
    charlotte "Why do you do that in public?"
    mia "I'd be such a waste!"
    charlotte "Do you have to point your giant boobs my way when you do it though?"
    player "{i}...I gotta say.{/i}"
    player "{i}I'm totally turned on now.{/i}"
    scene fs charlotteseesmiamc6
    with Dissolve(0.5)
    mia "There! All done."
    player "...."
    scene fs charlotteseesmiamc7
    mia "Hmm?"
    scene fs charlotteseesmiamc8
    mia "Oh!"
    scene fs charlotteseesmiamc9
    mia "Hehe.."
    mia "Um excuse me Charlotte."
    mia "I gotta go to the bathroom."
    player "Uh me too. Won't be long."
    charlotte "Sure."
    scene fs charlotteseesmiamc10
    charlotte "..."
    play sound "audio/straw-slurp.wav"
    charlotte "Siiiip."
    charlotte "..."
    scene fs charlotteseesmiamc11
    play sound "audio/charlottegameaudio/charlottemmm.wav"
    pause
    pause
    scene fs charlotteseesmiamc12
    voice "audio/charlottegameaudio/charlottewait.wav"
    charlotte "Wait."
    charlotte "There's only one bathroom here..."
    show miabathroomsex movie1
    play sound "audio/miagameaudio/miamoan1.wav" loop
    mia "AH!"
    charlotte "{i}Oh my god they really are doing it!{/i}"
    show miabathroomsex movie2
    play sound "audio/miagameaudio/miamoan2.wav" loop
    player "You like that big cock baby?"
    mia "Yes!"
    mia "YES AHN!!"
    pause
    show miabathroomsex movie3
    stop sound fadeout 5
    player "I'm gonna fucking cum Mia!"
    player "I'm gonna fill your pretty little pussy!"
    pause
    show miabathroomsex movie4
    voice "audio/miagameaudio/miaorgasm2.wav"

    mia "AHHH [povname]!"
    pause
    scene fs blackblank
    with Dissolve(0.7)
    "A few miuntes later.."
    scene fs charlotteseesmiamc17
    with Dissolve(1.0)
    mia "Hah...hah.."
    mia "W-We should get going now huh?"
    player "Yeah this uh, this was great!"
    play sound "audio/straw-slurp.wav"
    charlotte "*Siiiip*"

    pause
    $ charlottequestlog = "Get some rest. Charlotte's next event starts when you go to sleep at Night on a later day."
    $ charlottephase2interaction2 = 4
    $ charlottedaychecker1 = dayNumber
    jump passtime


label charlottephase2interaction3part1:
    scene fs charlotteroom
    with Dissolve(0.7)
    "Meanwhile at Charlotte's home..."
    show fbcharlotte current:
        xalign 0.4 ypos 120
    show fbvictoria current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    pause
    charlotte "Mmmnn."
    $ victoriaSprite = 1
    victoria "What's wrong miss?"
    $ victoriaSprite = 0
    $ charlotteSprite = 1
    charlotte "Vicky I.."
    charlotte "Something happened and I uh-"
    charlotte "I want to do something and I need your help.."
    $ charlotteSprite = 0
    $ victoriaSprite = 1
    victoria "Of course miss, anything you need."
    $ victoriaSprite = 0
    scene fs blackblank
    with Dissolve(0.7)
    charlotte "*Whispers*"
    victoria "Oh."
    charlotte "*Whispers more*"
    victoria "I see. Okay yes, go ahead and call him."
    scene fs playerroomNight
    with Dissolve(0.7)
    "Briiing Briiing"
    player "Huh? Hello?"
    charlotte "Come over to my house."
    player "Now?"
    charlotte "Right now. This is a blackmail threat!"
    player "..."
    player "Okay I guess."
    scene fs blackblank
    with Dissolve(0.7)
    "You put your clothes on and head over to Charlotte's mansion"
    scene fs charlottebj2
    with Dissolve(0.7)
    player "Hello again."
    player "I'm starting to get used to these late night booty calls."
    scene fs charlottebj1
    charlotte "You won't be laughing for too much longer buster."
    charlotte "Now do exactly what I say."
    scene fs charlottebj3
    charlotte "Now..."
    charlotte "Take out your penis!"
    scene fs charlottebj4
    pause
    scene fs charlottebj4b
    charlotte "Oh...that was quick."
    player "Are we bringing back the fuzzy handcuffs?"
    scene fs charlottebj5b
    with Dissolve(0.5)
    victoria "That won't be necessary master [povname]."
    scene fs charlottebj5
    player "Victoria! Always a pleasure."
    scene fs charlottebj5b
    victoria "Likewise."
    charlotte "Alright enough of the pleasentries!"
    victoria "It seems you're excited to start Miss."
    scene fs charlottebj6
    charlotte "N-No!"
    charlotte "I'm just..."
    charlotte "Shut up!"
    scene fs charlottebj7
    player "Hahaha."
    player "This is great, but can I know why my dick is hanging out? It's getting cold."
    scene fs charlottebj8
    with Dissolve(0.5)
    victoria "Miss Charlotte here simply wanted some more hands on experience."
    charlotte "W-Wait Vicky I-"
    scene fs charlottebj9
    voice "audio/charlottegameaudio/charlottestuffmouth.wav"
    charlotte "Mhn!"
    scene fs charlottebj9b
    victoria "Well, maybe hands on isn't the correct way to phrase it right now."
    scene fs charlottebj10
    with Dissolve(0.5)
    play sound "audio/charlottegameaudio/charlotteblowjob.wav" loop
    charlotte "MMM!"
    player "Ahh.."
    scene fs charlottebj9
    with Dissolve(0.5)
    pause
    scene fs charlottebj10
    with Dissolve(0.5)
    pause
    player "{i}Fuck this is really hot..{/i}"
    player "{i}Victoria keeps staring right at me as Charlotte sucks me off{/i}"
    scene fs charlottebj11
    with Dissolve(0.5)
    pause
    scene fs charlottebj12
    player "Oh fuck.."
    victoria "Does it feel good Master [povname]?"
    victoria "Having miss Charlotte stuff your meaty cock down her tight little throat?"
    scene fs charlottebj13
    charlotte "UGHK!"
    player "Holy shit okay, I'm definitely gonna cum."
    player "Charlotte that feels really fucking good!"
    scene fs charlottebj14
    with vpunch
    stop sound
    voice "audio/charlottegameaudio/charlottestuffmouth.wav"
    player "AHHH!"
    scene fs charlottebj15
    with Dissolve(0.7)
    play sound "audio/charlottegameaudio/charlottebjpant.wav"
    charlotte "Hah..hah..ahhh."
    victoria "How was it Miss?"
    charlotte "Oh just terrible..hah.."
    charlotte "Yeah..haha..I didn't like that at all."
    scene fs blackblank
    with Dissolve(1.0)
    victoria "Uh huh, I'm sure you didn't Miss."
    player "Alright that was..really great."
    player "But I should...you okay Charlotte?"
    voice "audio/charlottegameaudio/charlottehehehe2.wav"
    charlotte "Ahhh...hahaha.."
    victoria "I'll take care of her don't worry, you have a good night Master [povname]."
    player "Sure thing Victoria, have a good night."
    $ charlottephase2interaction2 = 5
    $ charlottephase2interaction3 = 1
    $ charlottequestlog = "Go to sleep at Night again to continue Charlotte's story."
    jump passtime


label charlottephase2interaction3part2:
    scene fs charlottenosleep1
    with Dissolve(1.0)
    voice "audio/charlottegameaudio/charlottemmm.wav"
    charlotte "Ahh...time for comfy sleep."
    charlotte "No more school or...other things to worry about right now."
    pause
    scene fs charlottenakedcummingtrick6
    with Dissolve(0.5)
    with vpunch
    player "AHHHG!"
    scene fs charlottenakedcummingtrick7
    with flash
    player "AHH Fuck that's so good!"
    scene fs charlottenakedcummingtrick8
    with Dissolve(0.5)
    charlotte "...."

    scene fs charlottenosleep2
    voice "audio/charlottegameaudio/charlotteannoyedsound.wav"
    charlotte "Hnnn."
    hide textbox
    pause
    scene fs charlottenosleep1
    with Dissolve(0.5)
    pause
    show miabathroomsex movie2
    play sound "audio/miagameaudio/miamoan2.wav" loop
    player "You like that big cock baby?"
    mia "Yes!"
    mia "YES AHN!!"
    stop sound
    scene fs charlottenosleep2
    voice "audio/charlottegameaudio/charlotteannoyedsound.wav"
    charlotte "Ugh!"
    scene fs charlottenosleep1
    with Dissolve(0.5)
    pause
    scene fs charlottebj13
    play sound "audio/charlottegameaudio/charlotteblowjob.wav" loop
    charlotte "UGHK!"
    player "Holy shit okay, I'm definitely gonna cum."
    player "Charlotte that feels really fucking good!"
    scene fs charlottebj14
    with vpunch
    player "AHHH!"
    scene fs charlottebj15
    with Dissolve(0.7)
    play sound "audio/charlottegameaudio/charlottebjpant.wav"
    charlotte "Hah..hah..ahhh."
    stop sound
    scene fs charlottenosleep2
    pause
    scene fs charlottenosleep3
    charlotte "Fuck."
    pause
    show charlottenosleep movie1
    play sound "audio/charlottegameaudio/charlottemasturbating2.wav" loop
    charlotte "AH AH AH!!!"
    charlotte "[povname]!!! FUCK ME!"
    charlotte "C-CUM!"
    charlotte "C-Cum inside me!!!"
    show charlottenosleep movie2
    play sound "audio/charlottegameaudio/charlotteorgasm1.wav"
    charlotte "DADDY!!!"
    pause
    $ charlottephase2interaction3 = 2
    $ charlottequestlog = "Wait two days after Charlotte's last visit, then go to sleep at Night to continue her story."
    $ charlottedaychecker2 = dayNumber
    jump passtime


label charlottephase2interaction4part1:
    pause
    "Briiiing Briiing"
    player "Now I wonder who that could be?"
    player "Hello?"
    charlotte "Hey..."
    player "I'd say this was getting old and annoying but given what's been happening at your place I'm not complaining."
    player "Did you call to 'blackmail' me again?"
    charlotte "No..not this time."
    charlotte "I just want you to come over."
    player "Oh uh...okay. I'll see you soon."
    charlotte "Okay. Bye."
    player "Huh. She sounds a bit different, let's go see what's up."
    scene fs overworldnight
    with Dissolve(1.0)
    "You get in your car and take a quick drive to Charlotte's place"
    scene fs blackblank
    with Dissolve(0.5)
    "*Ding Dong*"
    "*Bzzzz*"
    victoria "Come on in Master [povname], everything is unlocked for you."
    player "Sure uh, okay."
    "You go through the gates and doors, up the stairs on the right and slowly open Charlotte's door"
    scene fs charlottechapter2sex1
    with Dissolve(2.0)
    pause
    player "Oh my God."
    scene fs charlottechapter2sex1b
    charlotte "P-Please don't make this more awkward than it already is."
    scene fs charlottechapter2sex1
    victoria "Come now Charlotte, greet your guest properly."
    scene fs charlottechapter2sex2
    charlotte "Ah!"
    player "I'm feeling way more aroused than awkward right now Charlotte."
    scene fs charlottechapter2sex2b
    player "You're absolutely beautiful."
    charlotte "!!!"
    victoria "Isn't she?"
    charlotte "...."
    victoria "I assume you know why we want you here now Master [povname]?"
    victoria "If you wouldn't mind-"
    player "Already on it."
    scene fs charlottechapter2sex3
    with Dissolve(0.7)
    player "You ready?"
    scene fs charlottechapter2sex3b
    charlotte "God why does it look bigger every time I see it??"
    scene fs charlottechapter2sex4
    with Dissolve(0.5)
    victoria "It'll go in easier if you relax Miss."
    player "I don't think we're gonna have a problem with that, she's incredibly wet!"
    scene fs charlottechapter2sex5
    voice "audio/charlottegameaudio/charlottesmallmoan.wav"
    charlotte "Ahn!"
    charlotte "Stop talking about me!"
    scene fs charlottechapter2sex6
    voice "audio/charlottegameaudio/charlottepanting1.wav"
    charlotte "Oh my god!!"
    charlotte "H-He's stretching me open so much Vicky!"
    victoria "Good girl Miss Charlotte."
    player "{i}This is so hot, the way Victoria is coaching her!{/i}"
    scene fs charlottechapter2sex7
    with hpunch
    player "{i}Get's me fucking pumped!{/i}"
    play sound "audio/charlottegameaudio/charlottesex1.wav" loop
    charlotte "AHHHHH!"
    victoria "Feels good doesn't it?"
    charlotte "Y-Yes! Yes it does!"
    charlotte "It's so overwhelming!"
    victoria "This is how your friend Mia feels all the time."
    charlotte "Oh no.."
    victoria "She gets pumped and fucked by this very same cock that's inside you."
    charlotte "V-Vicky! Please! Stop!"
    victoria "I wonder what she would think about this?"
    charlotte "UUUUHN!!!"
    player "Holy shit she just clenched up on me like a fucking vice!"
    player "I'm getting really close ladies!"
    victoria "Hmmm?"
    player "{i}Victoria is glancing at me...I think I know what she wants{/i}"

    scene fs charlottechapter2sex8
    stop sound
    pause
    charlotte "Huh? W-Why'd you stop?"
    scene fs charlottechapter2sex9
    with Dissolve(0.5)
    voice "audio/charlottegameaudio/charlottemoanhey.wav"
    charlotte "What? Hey no!"
    scene fs charlottechapter2sex9b
    victoria "Ahhn.."
    charlotte "Stop! Don't kiss!"
    player "I'm gonna cum!"
    scene fs charlottechapter2sex10
    with vpunch
    player "MMHHN!!"
    voice "audio/charlottegameaudio/charlotteorgasm1.wav"
    charlotte "You can't! You can't kiss each other while cumming inside me!!"
    charlotte "N-Nnooo G-God it feels so good!"
    pause
    scene fs blackblank
    with Dissolve(1.0)
    "Turns out dispite all her rage Charlotte came the same time as you did"
    "So she passed out soon after you pumped her full"
    "You said your goodbyes to Victoria, got dressed and headed home"
    $ charlottephase2interaction3 = 3
    if currentchapter == 3:
        $ charlottequestlog = "Talk to Charlotte in Classroom 3 at school during Morning."
    else:
        $ charlottequestlog = "Continue exploring until the beach trip on day 20. Charlotte's next event starts in chapter 3."
    jump passtime


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
        charlotte "{i}Every time I see this thing I'm surprised. How did it fit inside me?{/i}"
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
        $ charlottequestlog = "Talk to Charlotte in Classroom 3 at school during Morning."
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
        charlotte "{i}Every time I see this thing I'm surprised. How did it fit inside me?{/i}"
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
        $ charlottequestlog = "Talk to Charlotte in Classroom 3 at school during Morning."
        jump startofchapter3

# Chapter 3


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
    $ charlottequestlog = "Visit Charlotte's house during Day or Night to take her home."
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
    $ charlottequestlog = "No more content for Charlotte in this version."
    jump passtime
