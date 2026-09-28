# scene 1

label pennyarcadescene:
    hide screen uppergui
    hide screen tosunnyside
    stop music fadeout 5
    stop sound fadeout 5

    scene fs arcade
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.35 ypos 120
    $ pennySprite = 0
    show fbpenny current:
        xalign 0.7 ypos 120
    $ playerSprite = 15
    player "Huh?"
    $ pennySprite = 1
    $ playerSprite = 4
    penny "Oh, hey you."
    $ pennySprite = 0
    $ playerSprite = 5
    player "Right. Have you seen Olivia?"
    $ pennySprite = 1
    $ playerSprite = 4
    penny "She's not here."
    $ pennySprite = 0
    $ playerSprite = 5
    player "Alright bye."
    $ pennySprite = 1
    $ playerSprite = 0
    penny "Why you being like that? You hate me that much?"
    $ pennySprite = 0
    $ playerSprite = 5
    player "I don't know you enough to hate you but you've done nothing but be a bitch during both of our encounters."
    player "I mean aren't you purposfully here just to beat Olivia's high score on all the games?"
    $ pennySprite = 1
    $ playerSprite = 0
    penny "Heh. Yeah."
    $ pennySprite = 0
    $ playerSprite = 5
    player "Yeah I'm out."
    $ playerSprite = 4
    penny "{i}After taking a good look at this guy he is pretty hot.{/i}"
    penny "{i}Hehe I just got a good idea!{/i}"
    $ pennySprite = 1
    penny "Wait!"
    $ pennySprite = 0
    $ playerSprite = 5
    player "What?"
    $ pennySprite = 1
    $ playerSprite = 4
    penny "I'm sorry. I know all this shit I'm doing is overkill."
    $ pennySprite = 0
    $ playerSprite = 5
    player "Kay.."
    $ pennySprite = 1
    $ playerSprite = 11
    penny "I think I'm just jealous."
    $ pennySprite = 0
    $ playerSprite = 1
    player "Jealous?"
    $ pennySprite = 1
    $ playerSprite = 0
    penny "Yeah, I don't have a boyfriend or anything right now and seeing you and Olivia together kinda made me feel bad."
    penny "I wanna bury the hatchet."
    $ pennySprite = 0
    $ playerSprite = 1
    player "For real?"
    $ pennySprite = 1
    $ playerSprite = 0
    penny "Yeah. Wanna help me beat this one last game? Then I promise I won't be an asshole...well purposefully."
    $ pennySprite = 0
    $ playerSprite = 1
    player "Well if you really mean that sure, I like playing games too."
    player "What should I do?"
    $ pennySprite = 1
    $ playerSprite = 0
    penny "Okay there's this real new tech discovered for this older arcade game's speedrun."
    penny "It's a single player game but you need two people to pull it off, go kneel in front of that arcade machine there."
    $ pennySprite = 0
    $ playerSprite = 1
    player "Alright. Super weird but if it works..."
    $ playerSprite = 0

    scene fs pennyarcadehump1b
    with Dissolve(0.7)
    player "Uh...like this?"
    scene fs pennyarcadehump1
    penny "Yeah...just like that."
    player "...."
    scene fs pennyarcadehump1b
    player "Why are you taking your pants of-"
    scene fs pennyarcadehump2
    with vpunch
    player "Hmmph!??"
    penny "Now stay right there."
    scene fs pennyarcadehump4a
    with Dissolve(0.7)
    player "...."
    scene fs pennyarcadehump4b
    player "...."
    scene fs pennyarcadehump4a
    player "...."
    scene fs pennyarcadehump4b
    player "...."
    scene fs pennyarcadehump4a
    player "I'm starting to think this has nothing to do with helping her game."
    scene fs pennyarcadehump4b
    player "...."
    scene fs pennyarcadehump4c
    penny "How's it going down there huh?"
    show pennyarcadehump movie1
    with Dissolve(0.7)
    penny "Enjoying yourself you fuckin perv?"
    player "{i}I'm the perv? She's straight up grinding her pussy on my face!{/i}"
    scene fs pennyarcadehump5a
    penny "Hmph!"
    scene fs pennyarcadehump5b
    penny "God I am so fucking cracked right now!"
    penny "C'mon c'mon!"
    show pennyarcadehump movie2
    penny "G-Give me that new highscore!!!"
    player "MMMMPH!!"
    penny "AHN!"
    "Game" "Congratulations!"
    penny "YEEEESS!!"
    "Game" "New High score! You're number 1!"
    scene fs pennyarcadehump6
    with vpunch
    penny "Oh my God!"
    penny "Beating Olivia's high score while her boyfriend's mouth is grinding my pussy!"
    penny "I-I'm SO!!"
    penny "I'm gonnna!"
    scene fs pennyarcadehump7
    with vpunch
    penny "AHHHNN!!!!"
    penny "YEEESSSS!"
    penny "FUCK!"
    scene fs arcade
    with Dissolve(1.0)
    $ pennySprite = 1
    $ playerSprite = 11
    show fbplayer current:
        xalign 0.35 ypos 120
    show fbpenny current:
        xalign 0.7 ypos 120
    with Dissolve(0.7)
    penny "Hah...hah."
    player "....."
    $ pennySprite = 0
    $ playerSprite = 15
    player "So."
    $ playerSprite = 5
    player "The fuck was that?"
    $ playerSprite = 4
    penny "....."
    show fbpenny defaultflip:
        xalign 1.5 ypos 120
    with move

    $ playerSprite = 11
    player "Seriously??!"
    $ playerSprite = 0
    $ pennyscene1 = 1
    $ pennyquestlog = "Penny is absolutely insane!"

    jump overworldmap

# scene after

label pennywakeup:
    hide screen uppergui
    hide screen backbuttonROOM
    scene fs playerroomMorn
    with Dissolve(0.7)
    $ playerSprite = 7
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "Hmmm.."
    player "I can't stop thinking about that girl Penny."
    player "I guess that's hard to do when she shoves her crotch in your face.."
    player "Olivia said she streamed right?"
    player "Maybe I should check it out tonight?"

    $ pennyscene1 = 2
    $ pennyscene2 = 1
    $ pennyquestlog = "I'm curious about Penny's stream.."
    jump playerlivingroom

# penny scene 2

label pennyfirststream:
    scene fs blackblank
    with Dissolve(1.0)
    player "Alright since she's a big streamer she should be on Twitchturbate.."
    player "I remember she said something about 'Penny Arcade'. Could that be her username?"
    scene fs pennyfirststream1
    with Dissolve(0.7)
    "It didn't take long before you found Penny's stream"
    scene fs pennyfirststream1b
    penny "Hey guys, thanks for tuning into another stream."
    scene fs pennyfirststream2
    with Dissolve(0.7)
    player "Ah, I must've just caught the end of it." 
    scene fs pennyfirststream3
    penny "Thank you to all the good boys who donated I weally appreciate it!"
    player "Haha what?"
    player "That's kinda cute."
    scene fs pennyfirststream4
    with Dissolve(0.7)
    penny "It's thanks to you guys that I was able to get this new KittyMeow headset."
    penny "Remember we're not even halfway to our goal!"
    penny "I have something special in mind for when we reach it."
    player "Hmm, I'm curious about that donation goal."
    player "I should make an account, why not? No harm in just that.."
    "Please create an account name"
    python:
        username = renpy.input("")
        username = username.strip()

        if not username:
            username = "Anon-Kun"
    player "Alright good, now she won't know it's me."
    penny "So if you wouldn't mind donating towards the goal that would be super awesome."
    penny "I promise I'll make it worth your while."
    menu:
        "Donate $25":
            if money < 25:
                player "I uh...don't feel like spending any money on her right now."
                player "I could always come back another night."
                jump gotosleep
            else:
                $ money = money - 25
                "Diiiiing"
                scene fs pennyfirststream5
                penny "Oh! Thank you....[username] for the 25! That's a lot of money!"
                scene fs pennyfirststream3
                with Dissolve(0.5)
                penny "Dat's meowwy nice of you!"
                player "Ah...my heart."
                scene fs pennyfirststream5b
                penny "Thanks again for watching guys. I'll see you tomorrow night."
                pause
                if oliviaphase2interaction2 == 1:
                    $ pennyquestlog = "I'm not sure if I want to keep spending money on Penny's stream.."
                    $ pennyscene2 = 2
                elif oliviaphase2interaction2 >= 2:
                    $ pennyscene2 = 3
                    $ pennyscene3 = 1
                    $ pennyquestlog = "Penny seemed to really like it when I donated, I should watch her stream again"
                jump gotosleep
        "Don't Donate":
            player "I uh...don't feel like spending any money on her right now."
            player "I could always come back another night."
            jump gotosleep

# scene 3

label pennysecondstream:
    scene fs blackblank
    with Dissolve(0.7)
    "It doesn't take you long to find Penny's stream again"
    scene fs pennysecondstream1
    with Dissolve(0.7)
    pause
    scene fs pennysecondstream1b
    penny "Hey everyone, I got an announcement to make."
    scene fs pennysecondstream1
    pause
    penny "...."
    scene fs pennysecondstream1b
    penny "Fine fine I'll do it."
    scene fs pennysecondstream2
    with Dissolve(0.5)
    pause
    penny "...."
    scene fs pennysecondstream2b
    penny "Nyah."
    scene fs pennysecondstream2
    player "How is her apatheticness so cute??"
    scene fs pennysecondstream1b
    penny "Anyways as I was saying."
    penny "Thanks to your generous donations we're over halfway to the stream goal."
    scene fs pennysecondstream1
    player "Oh yeah. I wonder what that's all about?"
    scene fs pennysecondstream1b
    penny "So you know what that means."
    penny "Time to drink my milk."
    scene fs pennysecondstream1
    player "What? Milk?"
    scene fs pennysecondstream3
    with Dissolve(0.7)
    pause
    penny "Milk is so good for you and your bones."
    player "What the hell?"
    scene fs pennysecondstream4
    penny "*Gulp*"
    pause
    scene fs pennysecondstream5
    penny "*Gulp*"
    player "I...Do I like this?"
    pause
    scene fs pennysecondstream6
    penny "Ahhhh."
    penny "Thank you for your milk chat."
    pause
    menu:
        "Donate $50":
            if money < 50:
                player "I uh...don't feel like spending any money on her right now."
                player "I could always come back another night."
                jump gotosleep
            else:
                $ money = money - 50
                player "Fuck, something about this is so hot I have to donate!"
                scene fs pennysecondstream7
                with Dissolve(0.7)
                "Diiiing"
                penny "Oh my gosh!"
                penny "[username]! You've donated so much thank you!"
                penny "If you keep that up you'll earn designated chatter."
                player "Designated chatter? What's that?"
                player "I should ask before she l-"
                scene fs pennysecondstream1b
                penny "Well guys thanks again for joining me, hope you liked the 'gameplay'."
                penny "I'll see you all tomorrow night!"
                player "Damn, it'll have to be next time..."
                $ pennyscene3 = 2
                $ pennyscene4 = 1
                $ pennyquestlog = "Penny said she does private streams if you donate enough..."
                jump gotosleep
        "Don't Donate":
            player "I uh...don't feel like spending any money on her right now."
            player "I could always come back another night."
            jump gotosleep
        
# scene 4

label pennythirdstream:
    scene fs pennysecondstream1
    with Dissolve(0.7)
    pause
    scene fs pennysecondstream1b
    penny "Gwettings my chatters."
    penny "Today we'll be playing a new horror game."
    scene fs pennysecondstream1
    player "Okay if I'm going to get her attention I'll need to donate a lot, and right now!"
    menu:
        "Donate $100":
            scene fs pennysecondstream1
            "Diiiing Diiiiing Diiiiiiiiiing!!"
            scene fs pennysecondstream7
            with vpunch
            penny "Oh my God!"
            penny "[username] just donated 100 moneys!!!"
            penny "That means we reached our goal!!"
            penny "Sorry guys looks like we'll have to game another stream."
            penny "[username] has earned himself a private stream as the top donator when we reached our goal!"
            player "Woah what? That was the goal reward? A private stream?"
            scene fs pennysecondstream1b
            with Dissolve(0.5)
            penny "Stay online [username], I'm going to switch to private now."
            scene fs pennysecondstream2b
            penny "Bwye everywon."
            player "So...cute."
            scene fs blackblank
            with Dissolve(0.7)
            pause
            "The stream goes black for a bit and then you get a DM from Penny"
            penny "{cps=25}Okay I'm ready for you now. Refresh the page.{/cps}"
            player "I'm so curious where this is gonna go..."
            scene fs pennythirdstream1b
            with Dissolve(1.0)
            player "Holy shit."
            scene fs pennythirdstream2
            penny "Hey there."
            penny "I'm here to thank you for the generosity Mr. [username]."
            scene fs pennythirdstream3
            pause
            player "Wait she has a tail.."
            player "How is it..."
            scene fs pennythirdstream3b
            penny "Nyaah."
            penny "I hope to have yow continued suppowt in da future."
            penny "Is there anything I can do fow you?"
            player "Hmmm. I think I want to see how naughty she is."
            player "{cps=25}You just have some fun, I'll enjoy the show.{/cps}"
            penny "Ohhh, whatever you say."
            scene fs pennythirdstream4
            with Dissolve(1.0)
            penny "I hope you like this pussycat's pussy."
            pause

            image pennymasturbate1:
                "penny chat 5.png"
                0.7
                "penny chat 6.png"
                0.7
                repeat

            image pennymasturbate2:
                "penny chat 5.png"
                0.5
                "penny chat 6.png"
                0.5
                repeat

            image pennymasturbate3:
                "penny chat 5.png"
                0.25
                "penny chat 6.png"
                0.25
                repeat

            show pennymasturbate1
            pause
            penny "Mmmm.."
            show pennymasturbate2
            penny "Oh [username] thank you..."
            penny "Thank you SO much."
            pause
            show pennymasturbate3
            penny "AHN!!"
            penny "I'm gonna cum!"
            penny "I'm gonna cum for you [username]!"
            pause
            scene fs pennythirdstream7
            with vpunch
            penny "AHHHH FUCK!"
            penny "MMMMHH!!!"
            pause
            scene fs blackblank
            with Dissolve(0.7)
            penny "Thanks again for your support!"

            $ pennyscene4 = 2
            $ pennyscene5 = 1
            if oliviaphase2interaction3 >= 1:
                $ pennyquestlog = "Penny is a full blown internet whore...I kinda wanna talk to her about it.Maybe at the arcade?"
            else:
                $ pennyquestlog = "Watching Penny whore herself out for internet money was really hot"
            jump gotosleep
        "Don't Donate":
            player "I uh...don't feel like spending any money on her right now."
            player "I could always come back another night."
            jump gotosleep

# scene 5

label pennyphase2sex1:
    stop music fadeout 5
    stop sound fadeout 5
    hide screen uppergui
    scene fs arcade
    with Dissolve(0.7)
    show fbpenny current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    player "Ah there she is."
    player "What am I even gonna say to her?"
    player "Meh I'll just wing it."
    show fbplayer current:
        xalign 0.4 ypos 120
    with Dissolve(0.5)
    $ playerSprite = 1
    player "Penny! Hey."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "Uhhh hi."
    $ pennySprite = 0
    $ playerSprite = 1
    player "How are you doing?"
    $ playerSprite = 0
    $ pennySprite = 1
    penny "...What is this?"
    penny "Why are you so chipper? Also I'm tired because SOMEBONE kept me up all night with their fucking."
    $ playerSprite = 1
    $ pennySprite = 0
    player "Ah right...sorry."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "So what do you want?"
    $ playerSprite = 16
    $ pennySprite = 0
    player "Nothing! I'm just looking to...talk to you."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "Wait....is this about what I said about wanting to sleep with me?"
    penny "Oh my god I wasn't serious."
    penny "I just said that to make Olivia angry."
    $ pennySprite = 0
    player "Mhmm?"
    $ playerSprite = 0
    $ pennySprite = 1
    penny "I would NOT touch you with a ten fo-"
    $ playerSprite = 1
    player "[username]."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "foot...pole...what did you just say?"
    $ pennySprite = 0
    $ playerSprite = 1
    player "I've just been browsing sites recently and found a really interesting one."
    player "Made a new account."
    player "Found this really cute girl on there. Big cat theme. Very cute."
    $ playerSprite = 0
    penny "...."
    $ pennySprite = 1
    
    show fbpenny current at surpriseshake:
        xalign 0.6 ypos 120
    penny "Are you [username]??!!"
    $ pennySprite = 0
    $ playerSprite = 1
    player "A very recent but generous fan of one Penny Arcade."
    player "Loved the private stream by the way."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "Holy shit you...okay this changes things."
    $ pennySprite = 0
    $ playerSprite = 1
    player "It does?"
    $ pennySprite = 1
    $ playerSprite = 0
    penny "Do you understand how hot it is knowing that Olivia's boyfriend sent me so much money to watch me finger myself?"
    $ pennySprite = 0
    $ playerSprite = 1
    player "{i}Well I'm not her boyfriend but she doesn't need to know that.{/i}"
    player "Yeah I'm aware. And why I'm here."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "Oh.."
    penny "You wanna fuck me don't you? Hehe..."
    $ pennySprite = 0
    $ playerSprite = 1
    player "Well...I'm just.."
    $ playerSprite = 0
    $ pennySprite = 1
    penny "Tonight. Come over."
    $ playerSprite = 1
    player "But what about-"
    $ playerSprite = 0
    $ pennySprite = 1
    penny "I'll take care of Olivia."
    $ pennySprite = 0
    $ pennyquestlog = "Penny wants me to come over tonight..."
    $ pennyscene5 = 2
    jump overworldmap

# scene 6

label pennyphase2sex2:
    hide screen uppergui
    stop music fadeout 5
    stop sound fadeout 5
    "BZZZZ"
    player "Hey it's me."
    penny "Come up."
    scene fs oliviahouse
    with Dissolve(0.7)
    show fbplayer current:
        xalign 0.4 ypos 120
    show fbpenny current:
        xalign 0.6 ypos 120
    with Dissolve(0.5)
    $ pennySprite = 1
    penny "There you are."
    $ pennySprite = 0
    $ playerSprite = 1
    player "Is Olivia out?"
    $ playerSprite = 0
    $ pennySprite = 1
    penny "No she's in her room. I told her I was having a boy over so she shouldn't come out."
    $ pennySprite = 0
    $ playerSprite = 1
    player "Oh okay, pretty simple solution."
    player "But shouldn't she recognize my voice?"
    $ playerSprite = 0
    $ pennySprite = 1
    penny "That's why you should stop fucking talking, get into my room, and start fucking my brains out."
    $ pennySprite = 0
    $ playerSprite = 11
    player "...."
    $ playerSprite = 1
    player "Yes ma'am."
    show pennysextime movie1
    with Dissolve(0.7)
    pause
    penny "Hah...hah...hah."
    player "Fuck you're so tight!"
    penny "Hah...harder!"
    show pennysextime movie2
    penny "AHN!!"
    penny "How are you s-so BIG??!"
    penny "You've been AHN!"
    penny "She's been getting pounded by this thing the whole time??"
    pause
    scene fs pennysextime5
    with Dissolve(0.5)
    penny "Ah AHN! YES!"
    scene fs pennysextime4
    penny "JUST LIKE THAT JUST LIKE THAT!"
    pause
    olivia "God damn."
    show pennysextime movie3
    penny "I'm CUMMING!!"
    pause
    scene fs pennysextime2
    with Dissolve(0.7)
    penny "Hah...hah."
    penny "You think she heard us?"
    scene fs pennysextime1
    player "She definitely heard YOU."
    scene fs pennysextime3
    with Dissolve(0.5)
    penny "Hehe, well then let's finish up here."
    pause
    show pennysextime movie4
    player "UGH!!"
    penny "Hehe!"
    pause
    scene fs blackblank
    with Dissolve(0.7)
    penny "Okay. We're gonna have to meet up again sometime."
    player "Haha will I have to donate some more?"
    penny "You keep making me cum like that Mr. [username], you won't have to donate shit."
    $ pennyquestlog = "No more content for Penny in this version (ch2.5B)"
    $ pennyscene5 = 3
    jump passtime