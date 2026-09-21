# shop screens from custom_screens.rpy
screen store_camera:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.5 yalign 0.135
        idle "ITEMS/M_camera.png"
        hover "ITEMS/M_camerahover.png"

        action Jump("conversationcamera")
screen store_watch:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 1.0 yalign 1.0
        idle "ITEMS/item_watch.png"
        hover "ITEMS/item_watchhover.png"

        action Jump("conversationwatch")
screen store_paint:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 1.0 yalign 1.0
        idle "ITEMS/item_paint.png"
        hover "ITEMS/item_painthover.png"

        action Jump("conversationpaint")
screen store_candy:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 1.0 yalign 1.0
        idle "ITEMS/item_candy.png"
        hover "ITEMS/item_candyhover.png"

        action Jump("conversationcandy")
screen store_movie:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 1.0 yalign 1.0
        idle "ITEMS/item_movie.png"
        hover "ITEMS/item_moviehover.png"

        action Jump("conversationmovie")
screen store_videogame:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 1.0 yalign 1.0
        idle "ITEMS/item_videogame.png"
        hover "ITEMS/item_videogamehover.png"

        action Jump("conversationvideogame")
screen store_Ashley:
    zorder 1
    imagebutton:
        focus_mask True
        idle "Sprites/ashley no BG.png"
        hover "Sprites/ashley no BG Hover.png"

        action Jump("ashleyconversation")


# gamedialogues.rpy

label storeintro:
    hide screen backbuttonSTORE
    $ ashleySprite = 1
    ashley "Hey there! I haven't seen your face around here before."
    $ ashleySprite = 0
    player "Yeah I'm pretty new to town, only been here for just over a month."
    $ ashleySprite = 1
    ashley "In that case welcome to Short-Skirt, I'm Ashley!"
    $ ashleySprite = 0
    player "Nice to meet you Ashley."
    player "{i}Huh this girl's actually pretty hot.{/i}"
    $ ashleySprite = 1
    ashley "The feeling's mutual! Let me know if you have any questions."
    $ ashleySprite = 0
    player "Actually I do have one question, why's the store called short skirt?"
    $ ashleySprite = 1
    ashley "Cause all our products are quick and easy to access haha."
    $ ashleySprite = 0
    player "Ooohhh haha alright I get it."
    $ ashleySprite = 1
    ashley "Handsome boy like you? I'd believe it."
    $ ashleySprite = 0
    player "Careful Ashley I'm quite succeptable to compliments."
    $ ashleySprite = 1
    ashley "Something else we have in common haha."
    ashley "I'll leave you to your shopping!"
    $ ashleySprite = 0
    $ firsttimestore = 1
    $ cameracount = 1 #might need to delete this later cause i have one in variables
    jump mallstore

label ashleyconversation:
    scene fs store
    $ ashleySprite = 1
    show hbashley current
    hide screen store_Ashley
    hide screen backbuttonSTORE
    hide screen store_paint
    hide screen store_movie
    hide screen store_candy
    hide screen store_watch
    hide screen store_videogame
    hide screen store_camera
    if cameracount == 0:
        ashley "Hey there [povname], would you like to buy something from MY store?"
        menu:
            "Fuzzy Handcuffs" if handcuffcount == 1:
                jump conversationhandcuffs
            "Condoms" if condomcount == 1:
                jump conversationcondoms
            "Nothing":
                jump mallstore
    else:
        ashley "Hey there handsome, what can I help you with today?"
        $ ashleySprite = 0
        player "Hey Ashley. I'm just browsing."
        $ ashleySprite = 1
        ashley "Take your time, and feel free to ask me about any of our products!"
        $ ashleySprite = 0
        player "Thanks."
        jump mallstore



label conversationhandcuffs:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    player "How much are the handcuffs?"
    $ ashleySprite = 1
    ashley "Haha I gotta say I'm surprised you asking."
    ashley "Are they for you or for someone else?"
    $ ashleySprite = 0
    player "Haha both I guess, sometimes I like to see what the girl can get up to in a position of power."
    $ ashleySprite = 1
    ashley "That, is a very sexy opinion to have Mr. [povname]."
    ashley "It's {color=#3eab33}35{/color} Dollars."
    $ ashleySprite = 0
    "You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy handcuffs":
            if money < 35:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                $ handcuffcount = handcuffcount - 1
                hide screen store_watch
                $ money = money - 35
                $ amountspent += 35
                $ item_list.append("Handcuffs")
                $ ashleySprite = 1
                ashley "They're all yours handsome!"
                $ ashleySprite = 0
                player "Thanks Ashley."
                $ ashleySprite = 1
                ashley "Have fuuuun."
            jump mallstore
        "Don't Buy":
            jump mallstore


label conversationcondoms:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    player "What size are the condoms?"
    $ ashleySprite = 1
    ashley "I actually just sold a bunch to a couple let's see..."
    ashley "Oh sorry, only extra large is available right now."
    $ ashleySprite = 0
    player "Oh, alright that'll work then."
    $ ashleySprite = 1
    ashley ".....For real? EXTRA large?"
    $ ashleySprite = 0
    player "Yup."
    $ ashleySprite = 1
    ashley "God damn handsome okay. It's {color=#3eab33}35{/color} Dollars. You want it?"
    $ ashleySprite = 0
    "You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy Condoms":
            if money < 35:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                $ condomcount = condomcount - 1
                $ money = money - 35
                $ amountspent += 35
                $ item_list.append("Condoms")
                $ ashleySprite = 1
                ashley "Hehe some lucky girl is gonna have some fun!"
                player "If we end up using them."
                ashley "Mmmm so naughty hehe."
                jump mallstore
        "Don't Buy":
            jump mallstore


label conversationwatch:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    player "Hey that's a fancy watch."
    ashley "Yeah that's the HP-CheckWatch-3000."
    ashley "Not just a watch, a heart-rate monitor, mini-tablet, and phone!"
    player "Woah that's impressive."
    ashley "Top of the line stuff."
    ashley "Expensive too, {color=#3eab33}150{/color} Dollars. You want it?"
    "You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy Watch":
            if money < 150:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                $ watchcount -= 1
                hide screen store_watch
                $ money -= 150
                $ amountspent += 150
                $ item_list.append("HP-CheckWatch-3000")
                $ ashleySprite = 1
                ashley "Wow! You really got it! Even though it's not usable in this build?"
                $ ashleySprite = 0
                player "Build? What are you talking about?"
                $ ashleySprite = 1
                ashley "Did you know Kyle Mercury has a plan for me to give you a blowjob after you buy that?"
                $ ashleySprite = 0
                player "What?? Who's Ky-"
                $ ashleySprite = 1
                ashley "And if you buy everything, eventually you bend me over this counter and pound me raw."
                ashley "God I can't wait."
                $ ashleySprite = 0
                player "I'm just...gonna take the watch now."
                jump mallstore
        "Don't Buy":
            jump mallstore


label conversationvideogame:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    $ ashleySprite = 0
    player "Oh man that looks like a classic."
    $ ashleySprite = 1
    ashley "Oh Mortal Street Caliber 2? It's awesome!"
    ashley "It's too bad they dropped the ball so hard on the sequels with the microtransactions and 'Live Service' models."
    $ ashleySprite = 0
    player "I don't know how you did it Ashley but somehow I like you even more now."
    $ ashleySprite = 1
    ashley "Aww thanks [povname]. Keep talking like that and I may have to suck your cock."
    $ ashleySprite = 0
    player "I...wait what?"
    $ ashleySprite = 1
    ashley "That'll be {color=#3eab33}100{/color} Dollars."
    $ ashleySprite = 0
    "You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy Videogame":
            if money < 100:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                $ videogamecount = videogamecount - 1
                hide screen store_videogame
                $ money = money - 100
                $ amountspent += 100
                $ item_list.append("Video Game")
                $ ashleySprite = 1
                ashley "Alright, hope you enjoy it!"
                $ ashleySprite = 0
                player "Um about what you sa-"
                $ ashleySprite = 1
                ashley "Please have a pleasant day customer!"
                $ ashleySprite = 0
                player "....."
                if oliviaphase1interaction2 == 1: #edit this variable later its just a placeholder
                    player "{i}Sweet! Now I can give this to Olivia, hope she's as stoked as I am.{/i}"
                    player "{i}I wonder if she has the game console to play it.{/i}"
                    $ oliviaquestlog = "I should give Olivia the game, I hope she'll like it."
                    $ oliviaphase1interaction2 = 2

                jump mallstore
        "Don't Buy":
            jump mallstore


label conversationcandy:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    player "Oh that looks tasty. Can I get that please?"
    $ ashleySprite = 1
    ashley "Sure I-"
    $ ashleySprite = 2
    ashley "Oh uh...no I..I'm not sure I can sell this to you sorry."
    $ ashleySprite = 3
    player "Huh? What do you mean?"
    $ ashleySprite = 2
    ashley "I think this flavor's been banned in the entire town."
    $ ashleySprite = 3
    player "What? There's no way."
    $ ashleySprite = 2
    ashley "Okay I don't think it was banned they just they stopped importing it."
    ashley "There was some big incident last year with some girl who went crazy, I don't know the details."
    ashley "Must've slipped through unnoticed until someone stocked it here sorry."
    $ ashleySprite = 3
    player "Come on, only candy with that flavor in town? I gotta have it now."
    ashley "I dunno..."
    player "Hey look at me, I'm clearly not a girl. I'll just go home and binge eat it while watching a show or something."
    $ ashleySprite = 2
    ashley "*Sigh* fine. But there's only {color=#ed2323}[candycount]{/color} candies left alright so that's all I can give you."
    ashley " {color=#3eab33}25{/color} Dollars each."
    $ ashleySprite = 0
    "You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy Candy":
            if money < 25:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                $ candycount = candycount - 1
                if candycount == 0:
                    hide screen store_candy
                $ money = money - 25
                $ amountspent += 25
                $ item_list.append("Candy")
                $ ashleySprite = 1
                ashley "Alright, enjoy your forbidden candy yah weirdo."
                $ ashleySprite = 0
                player "Best kind there is!"
                $ ashleySprite = 1
                ashley "Haha."
                $ ashleySprite = 0
                if emilyphase1interaction2 == 6:
                    player "{i}Nice, I'm not sure how yet but I know I'll be able to use this for Emily somehow.{/i}"

                jump mallstore
        "Don't Buy":
            jump mallstore


label conversationmovie:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    player "Hmmm you guys sell movies too?"
    $ ashleySprite = 1
    ashley "Yeah it's kinda like the bargain bin kinda deal."
    ashley "But instead of the bin it's on the main shelf...sigh.."
    $ ashleySprite = 0
    player "You don't sound all that happy about it."
    $ ashleySprite = 1
    ashley "I mean I wouldn't mind if it was a good movie but this thing looks like garbage."
    $ ashleySprite = 0
    player "One mans trash..."
    $ ashleySprite = 1
    ashley "You really want this terrible horror movie? Cause it costs {color=#3eab33}50{/color} bucks."
    $ ashleySprite = 0
    player "Jesus! You just said it was garbage!"
    $ ashleySprite = 1
    ashley "Collectors Edition baby."
    $ ashleySprite = 0
    "Would you like to buy the movie? You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy Movie":
            if money < 50:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                hide screen store_movie
                $ money = money - 50
                $ amountspent += 50
                $ item_list.append("Movie")
                $ ashleySprite = 1
                ashley "Haha sucker!"
                $ ashleySprite = 0
                player "You know I'm still standing right here."
                $ ashleySprite = 1
                ashley "Oh I know handsome."
                $ ashleySprite = 0
                if emilyphase1interaction2 == 6:
                    player "{i}Well I got a good movie to watch with Emily now.{/i}"
                    player "{i}Maybe I'll ask her to watch it with me after the track meet.{/i}"
                $ moviecount = moviecount - 1

                jump mallstore
        "Don't Buy":
            jump mallstore


label conversationpaint:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    player "Hey so about this paint?"
    $ ashleySprite = 1
    ashley "Yes?"
    $ ashleySprite = 0
    player "Why the rainbow?"
    $ ashleySprite = 1
    ashley "Ah that's the 7 in 1 any paint."
    $ ashleySprite = 0
    player "7 in 1?"
    $ ashleySprite = 1
    ashley "Yeah it paints any color you need."
    $ ashleySprite = 0
    player "H.....how-"
    $ ashleySprite = 1
    ashley "New paint technology!"
    $ ashleySprite = 0
    player "Uh....okay. How much?"
    $ ashleySprite = 1
    ashley "It's {color=#3eab33}100{/color} dollars!"
    $ ashleySprite = 0
    "Would you like to buy the paint? You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy Paint":
            if money < 100:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                hide screen store_paint
                $ money = money - 100
                $ amountspent += 100
                $ item_list.append("Paint")
                player "Thanks!"
                $ ashleySprite = 1
                ashley "No thank YOU handsome hehe."
                $ ashleySprite = 0
                $ paintcount = paintcount - 1
                if emilyphase1interaction2 == 3:
                    player "{i}Can't believe I'm going this far for Emily of all people.{/i}"
                    player "{i}But I bought the paint. I'll call her from my place and tell her to come pick it up.{/i}"
                    player "{i}This had better be worth it!{/i}"
                    $ emilyphase1interaction2 = 4


                jump mallstore
        "Don't Buy":
            jump mallstore


label conversationcamera:
    hide screen store_Ashley
    hide screen backbuttonSTORE
    player "That camera looks pretty decent."
    $ ashleySprite = 1
    ashley "Yeah it's the second latest model!"
    $ ashleySprite = 0
    player "Second latest?"
    $ ashleySprite = 1
    ashley "That's right."
    $ ashleySprite = 0
    player "Uh...okay, how much?"
    $ ashleySprite = 1
    ashley "It's {color=#3eab33}100{/color} dollars!"
    "You have {color=#3eab33}[money]{/color} Dollars."
    menu:
        "Buy Camera":
            if money < 100:
                "You don't have enough money to purchase this"
                jump mallstore
            else:
                hide screen store_camera
                $ money = money - 100
                $ amountspent += 100
                $ item_list.append("Camera")
                $ ashleySprite = 0
                player "Thanks!"
                $ ashleySprite = 1
                ashley "No thank YOU handsome hehe."
                $ ashleySprite = 0
                $ cameracount = cameracount - 1
                $ ashleySprite = 1
                ashley "Hmmmm. You know..."
                $ ashleySprite = 0
                player "What?"
                $ ashleySprite = 1
                ashley "You seem to be a man who has some purchasing power."
                $ ashleySprite = 0
                player "I mean I guess I...buy things."
                $ ashleySprite = 1
                ashley "You see. I'm trying to start a little business of my own, this job is just to hold me until things get off the ground."
                ashley "But for potential customers like yourself I like to give a chance to view the catalogue if you know what I'm saying."
                $ ashleySprite = 0
                player "Well...what are you selling?"
                $ ashleySprite = 1
                ashley "It's gonna be an adult toy business! From Dildos to wireless vibrators, lube and everything in between!"
                $ ashleySprite = 1
                ashley "I'm gonna call it Ashley's toys for girls and boys!"
                $ ashleySprite = 0
                player "Name's a bit long innit?"
                $ ashleySprite = 1
                ashley "Innit?"
                $ ashleySprite = 0
                player "I don't know, felt right to say."
                $ ashleySprite = 1
                ashley "Okay well I'll work on the name. You interested in products like that? Currently I only have two items in stock right now."
                $ ashleySprite = 0
                player "What are they?"
                $ ashleySprite = 1
                ashley "Handcuffs and condoms."
                $ ashleySprite = 0
                player "Specific but...alright."
                $ ashleySprite = 1
                ashley "Come talk to me directly if you ever want to buy from MY store okay?"
                $ ashleySprite = 0
                player "Sure alright."
                $ ashleySprite = 1
                ashley "Thanks honey, have a VERY pleasant day."

                jump mallstore
        "Don't Buy":
            jump mallstore
