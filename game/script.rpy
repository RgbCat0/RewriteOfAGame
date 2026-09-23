# The script of the game goes in this file.

# Declare characters used by this game. The color argument colorizes the
# name of the character.

# The game starts here.

label start:

    jump definevariables

label postIntro:
    jump introductions

#locations-----------------------------------------------------------------------------------------------------------

label playerRoom:
    hide screen locationname
    hide screen backbuttonLIVINGROOM
    hide screen questboxpreview
    $ whereami = "playerRoom"
    show screen uppergui
    show screen backbuttonROOM

    if currentchapter > 2 and emilyphase2interaction2 >= 3 and emilyphase3interaction1 == 0 and dayNumber != 21:
        scene fs playerroomMorn
        with Dissolve(0.3)
        jump emilyphase3interaction1part1

    if timeofday == "Night" and emilyphase2interaction1 == 4:
        jump emilyphase2interaction1part5

    if timeofday == "Night" and sophiaphase2interaction3 == 1:
        jump sophiaphase2interaction3part2

    if timeofday == "Night" and miaphase2interaction2 == 3:
        jump miaphase2interaction2part4

    if timeofday == "Morning" and pennyscene1 == 1:
        jump pennywakeup

    if timeofday == "Morning":
        scene fs playerroomMorn
        if miaphase2interaction2 == 4 and currentchapter == 3 and dayNumber > 21:
            jump specialwakeup
        if miaphase1interaction2 == 4:          #Use these lines to call specialwakeup when something
            jump specialwakeup                  #needs to happen in the morning when player wakes up
        if avaphase2interaction1 == 1 and avadaycheck < dayNumber:
            jump specialwakeup
        # if dayNumber >= charlotteblackmailday and charlottephase2interaction2 == 1:
        #     jump specialwakeup
        if charlottephase2interaction2 == 2:
            jump specialwakeup
        
        if amountspent >= 350 and ashleychecker == 0:
            jump specialwakeup
        call screen myRoom("playerroomMorning.png", "playerroomMorningHover.png")

    elif timeofday == "Day":
        scene fs playerroomDay
        call screen myRoom("playerroomDay.png", "playerroomDayHover.png")
    elif timeofday == "Night":
        scene fs playerroomNight
        call screen myRoom("playerroomNight.png", "playerroomNightHover.png")

label playerlivingroom:
    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    hide screen tosunnyside
    hide screen locationname
    hide screen backbuttonROOM
    stop music fadeout 2
    $ whereami = "livingRoom"

    if timeofday == "Night" and stephaniescene2 >= 1 and ravenscene1 >= 2 and melissascene1 >= 1 and bullieschecker == 0 and currentchapter == 3:
        jump chapter3bulliesmassage

    if timeofday == "Day" and katiephase3interaction1 == 1:
        jump katiephase3interaction1part2
    if timeofday == "Night" and miaphase2interaction2 == 3:
        jump miaphase2interaction2part4

    if dayNumber >= (josiedaycheck + 1) and currentchapter >= 2 and timeofday == "Day" and josyscene1 == 0:
        jump josykatiehangout1
    if avaphase2interaction2 == 2 and timeofday == "Night":
        jump avaphase2interaction2part2

    if josyscene1 == 1 and miaphase2interaction2 == 3 and timeofday == "Day":
        jump josykatiehangout2
    
    if timeofday == "Night" and katiephase2interaction1 == 5 and miaphase2interaction2 >= 4:
        jump pizzapartykatiefuck

    show screen uppergui
    show screen questboxpreview
    show screen backbuttonLIVINGROOM

    if timeofday == "Day" or timeofday == "Morning":
        scene fs livingroom
        call screen mylivingroom("livingroom.png", "livingroomhover.png")
    elif timeofday == "Night":
        scene fs livingroomnight
        call screen mylivingroom("livingroomnight.png", "livingroomnighthover.png")

label startofchapter1:
    $ currentchapter = 1
    scene fs blackblank
    pause
    show chapter chapter1
    with Dissolve(2.0)
    pause
    hide chapter chapter1
    jump continuegamechapter1

label startofchapter2:
    $ currentchapter = 2
    $ dayNumber += 1
    $ avaphase1interaction3 = 10
    if charlottequestlog == "Think I should avoid Charlotte till after the track meet.":
        $ charlottequestlog = "I should explore Sunnyside some more during the morning."

    scene fs blackblank
    pause
    show chapter chapter2
    with Dissolve(2.0)
    pause
    hide chapter chapter1
    jump continuegamechapter2

label startofchapter3:
    $ currentchapter = 3
    $ dayNumber += 1
    
    if oliviaphase2interaction3 == 1:
        $ oliviaquestlog = "That was some incredible sex. I should chat up Olivia at the school."

    if avaphase2interaction3 == 2:
        $ avaquestlog = "That sex with Ava was incredible. I wonder how she's doing? I should stop by the school."

    if miaphase2interaction2 == 4:
        $ miaquestlog = "I've been patient. It's time Mia..." 

    scene fs blackblank
    pause
    show chapter chapter3
    with Dissolve(2.0)
    pause
    hide chapter chapter1
    jump continuegamechapter3



label overworldmap:

    if currentchapter > 2 and emilyphase2interaction2 >= 3 and emilyphase3interaction1 == 0 and dayNumber != 21:
        jump emilyphase3interaction1part1


    hide screen officedoor
    hide screen store_Ashley
    hide screen backbuttonROOM
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonCLASSROOM
    hide screen backbuttonGFROOM
    hide screen backbuttonGFHALLWAY
    hide screen backbuttonMALL
    hide screen backbuttonSTORE
    hide screen backbuttonGYM
    hide screen backbuttonSOPHIAOUTSIDE
    hide screen backbuttonGYMOUTSIDE
    hide screen backbuttonOUTSIDEOFFICE
    hide screen backbuttonCLUB
    hide screen miasroomdoor
    hide screen katiesroomdoor
    hide screen clubrestroom
    hide screen gotoclubrestroom
    hide screen backbuttonCLUBRESTROOM
    hide screen tonormalmap
    hide screen gotoclubrestroom
    hide screen gotoclubrestroomDay

    hide screen emily_atschool
    hide screen emily_atlibrary
    hide screen melissa_club
    hide screen raven_mall
    hide screen ava_atschool
    hide screen ava_atschoolhallway
    hide screen ava_atgym
    hide screen mia_atschool
    hide screen mia_sophia_atschool
    hide screen olivia_atschool
    hide screen sophia_atcafe
    hide screen sophia_atschool
    hide screen julia_kitchen
    hide screen charlottemia_room
    hide screen mia_room
    hide screen charlotte_library
    hide screen charlotte_school
    hide screen charlotte_atcafe
    hide screen mia_phone
    hide screen gym_machine
    hide screen store_camera
    hide screen store_watch
    hide screen store_paint
    hide screen store_candy
    hide screen store_movie
    hide screen store_videogame

    if whereami != "overworldmap":
        if whereami != "sunnysidemap" and timeofday != "Night":
            stop music
            stop sound
            play music "audio/Main theme (Double Loop).mp3" fadein 20

        elif whereami != "sunnysidemap" and timeofday == "Night":
            stop music
            stop sound
            play music "audio/Night Theme single loop.mp3" fadein 20

    $ whereami = "overworldmap"

    show screen uppergui
    show screen questboxpreview

    show screen locationname

    if headtosunnyside == 1:
        hide screen questboxpreview
    if headtooffice == 1:
        hide screen questboxpreview

    if currentchapter > 1:
        show screen tosunnyside

    if timeofday == "Morning" or timeofday == "Day":
        scene fs overworld
        call screen overworld
    else:
        scene fs overworldnight
        call screen overworldnight

label gotosunnyside:

    if whereami == "club" or whereami == "beach":
        stop music fadeout 2

    $ whereami = "sunnysidemap"

    hide screen exit_cafe
    hide screen tosunnyside
    hide screen officedoor
    hide screen store_Ashley
    hide screen backbuttonROOM
    hide screen backbuttonLIVINGROOM
    hide screen backbuttonCLASSROOM
    hide screen backbuttonGFROOM
    hide screen backbuttonGFHALLWAY
    hide screen backbuttonMALL
    hide screen backbuttonSTORE
    hide screen backbuttonGYM
    hide screen backbuttonSOPHIAOUTSIDE
    hide screen backbuttonGYMOUTSIDE
    hide screen backbuttonOUTSIDEOFFICE
    hide screen backbuttonCLUB
    hide screen miasroomdoor
    hide screen katiesroomdoor
    hide screen clubrestroom
    hide screen gotoclubrestroom
    hide screen backbuttonCLUBRESTROOM
    hide screen gotoclubrestroom
    hide screen gotoclubrestroomDay

    hide screen emily_atschool
    hide screen emily_atlibrary
    hide screen melissa_club
    hide screen raven_mall
    hide screen ava_atschool
    hide screen ava_atschoolhallway
    hide screen ava_atgym
    hide screen mia_atschool
    hide screen mia_sophia_atschool
    hide screen olivia_atschool
    hide screen sophia_atcafe
    hide screen sophia_atschool
    hide screen julia_kitchen
    hide screen charlottemia_room
    hide screen mia_room
    hide screen charlotte_library
    hide screen charlotte_school
    hide screen charlotte_atcafe
    hide screen mia_phone
    hide screen gym_machine
    hide screen store_camera
    hide screen store_watch
    hide screen store_paint
    hide screen store_candy
    hide screen store_movie
    hide screen store_videogame




    show screen uppergui
    show screen questboxpreview

    if headtosunnyside == 1:
        hide screen questboxpreview
    
    if headtooffice == 1:
        hide screen questboxpreview

    show screen locationname

    show screen tonormalmap

    if timeofday == "Morning" or timeofday == "Day":
        scene fs sunnysidemap
        call screen screen_sunnyside
    else:
        scene fs sunnysidenight
        call screen screen_sunnysidenight




label displaycalender:
    hide screen uppergui
    hide screen backbuttonROOM
    if timeofday == "Night":
        player "Ugh I'm too tired to look at that right now."
        jump playerRoom
    if dayNumber > 30:
        image currentday = "calenderdays/calender30.png"
    else:
        image currentday = "calenderdays/calender" + "[dayNumber]" + ".png"

    scene currentday
    with Dissolve(1.0)
    window hide
    pause
    jump playerRoom

#--------------------SUNNYSIDE BGs----------------------------------

label office:
    hide screen uppergui
    hide screen backbuttonOUTSIDEOFFICE
    hide screen officedoor

    if timeofday == "Night":
        player "It's night time, nobody's here."
        jump gotosunnyside
    elif timeofday == "Day":
        if juliachecker >= 4:
            jump officejulia1
        else:
            player "Wow Julia really works here? Crazy."
            jump gotosunnyside
    else:
        player "I think Julia only works during the Day."
        jump gotosunnyside

    scene fs officeExtras


label outsideoffice:
    $ whereami = "outsideoffice"

    hide screen tonormalmap
    hide screen locationname

    scene fs outsideoffice

    if headtosunnyside == 1:
        jump meetMiaAndKatieAtOffice
    else:
        if headtooffice == 1:
            jump continuechapter3intro

        show screen backbuttonOUTSIDEOFFICE
        if timeofday == "Night":
            call screen outsidetheofficenight
        else:
            call screen officedoor
            call screen outsidetheoffice


label insidecafe:
    $ whereami = "cafe"

    hide screen uppergui
    hide screen tonormalmap
    hide screen locationname
    hide screen questboxpreview

    
    if headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump gotosunnyside

    if avaphase2interaction2 == 1 and timeofday == "Day":
        jump avaphase2interaction2part2

    scene fs insidecafe

    show screen exit_cafe
    if headtosunnyside != 1:
        if timeofday == "Day" and sophiaphase2interaction1 > 0 and sophiaphase2interaction1 != 3:

            call screen sophia_atcafe
                                                                #we're skipping interaction2
        if timeofday == "Day" and sophiaphase2interaction1 == 3 and sophiaphase2interaction3 == 0:
            jump sophiaphase2interaction3part1

        if timeofday == "Morning" and currentchapter > 1 and charlottephase2interaction1 == 0 and charlottephase1interaction3 >= 2:

            call screen charlotte_atcafe
        elif timeofday == "Morning" and currentchapter > 1 and charlottephase2interaction2 == 3:

            call screen charlotte_atcafe

    call screen inside_cafe



label insideclub:
    hide screen uppergui
    hide screen questboxpreview
    hide screen clubrestroomstall


    hide screen tonormalmap
    hide screen locationname

    if headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump gotosunnyside

    if whereami != "club bathroom":
        play music "audio/clubBG.mp3"

    $ whereami = "club"

    if timeofday != "Night":
        scene fs insideclub
    else:
        scene fs insideclubextras

    if timeofday == "Night":
        show screen gotoclubrestroom
    else:
        show screen gotoclubrestroomDay
    show screen backbuttonCLUB

    if timeofday == "Night" and emilyphase2interaction1 >= 3 and melissascene1 == 0:
        call screen melissa_club
    if timeofday == "Night":
        call screen inside_club_night
    else:
        call screen inside_club

label clubbathroom:
    $ whereami = "club bathroom"
    hide screen uppergui
    hide screen questboxpreview
    hide screen gotoclubrestroom
    hide screen backbuttonCLUB

    show screen backbuttonCLUBRESTROOM
    show screen clubrestroomstall
    call screen clubrestroom

label goinsidestall:

    scene fs clubrestroom
    hide screen clubrestroomstall
    hide screen gotoclubrestroom
    hide screen gotoclubrestroomDay
    if melissascene1 == 1:
        jump melissadancescene2
    else:

        player "No reason to go in there right now..."
    jump clubbathroom

label beach:
    $ whereami = "beach"

    hide screen tonormalmap
    hide screen locationname
    hide screen uppergui
    hide screen questboxpreview

    if headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump gotosunnyside

    if emilyphase2interaction2 == 1 and timeofday == "Night":
        jump emilyphase2interaction2part2

    if timeofday != "Day":
        play music "audio/justbeach.mp3" fadein 10
    else:
        play music "audio/beachsounds.mp3" fadein 5

    if timeofday == "Morning":
        scene fs beach
    elif timeofday == "Day":
        scene fs lockerroom
    else:
        scene fs beach


    show screen backbuttonCLUB
    if timeofday == "Night":
        call screen beach_screen_night
    elif timeofday == "Day":
        call screen beach_screen_day
    else:
        call screen beach_screen

#---------------------------END OF SUNNYSIDE BG---------------------------------------


label outsidegym:
    $ whereami = "outsidegym"
    hide screen questboxpreview
    hide screen tosunnyside
    hide screen ava_atgym
    hide screen backbuttonGYM
    hide screen uppergui
    hide screen locationname
    hide screen locationname
    hide screen overworld
    stop music fadeout 5
    stop sound fadeout 5
    scene fs outsidegym
    show screen backbuttonGYMOUTSIDE
    call screen outsidethegym

label gym:
    hide screen backbuttonGYMOUTSIDE

    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    $ whereami = "gym"
    if timeofday == "Morning":
        scene fs gymarea
    elif timeofday == "Day":
        scene fs gymareaafternoon

    # $ avaphase1interaction3 = 10
    if currentchapter == 2 and avaphase1interaction3 == 10 and timeofday == "Morning" and avaphase2interaction1 == 0:
        show screen ava_atgym

    if timeofday == "Day" and avaphase1interaction1 == 1:
        jump avaphase1interaction1part2

    if timeofday == "Day" and avaphase1interaction1 >= 1 and avaphase1interaction2 != 1 and avaphase1interaction2 != 2 and avaphase1interaction2 != 4 and avaphase2interaction1 == 0:
        show screen ava_atgym

    if timeofday == "Day" and avaphase2interaction3 == 1:
        show screen ava_atgym

    if timeofday == "Night":
        "Pretty sure the Gym is closed at night."
        jump overworldmap

    show screen uppergui
    show screen backbuttonGYM

    if avaphase1interaction1 == 4:
        hide screen ava_atgym

    if timeofday == "Morning":
        call screen gym
    elif timeofday == "Day":
        call screen gymAftertoon

label library:
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside

    stop music fadeout 2
    if timeofday == "Night":
        scene fs overworldnight
        player "Library's closed at night."
        hide fs overworldnight
        jump overworldmap

    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    $ whereami = "library"
    scene fs library

    if timeofday == "Day" and (miaphase1interaction3 == 2 or miaphase1interaction3 == 3):
        show screen charlotte_library


    if miaphase1interaction3 == 3:
        show screen mia_phone

    if currentchapter >= 2 and timeofday != "Night" and stephaniescene1 == 1:
        show screen emily_atlibrary

    if currentchapter >= 2 and timeofday == "Day" and emilyphase2interaction1 > 2 and emilyphase2interaction1 != 5:
        show screen emily_atlibrary


    if librarycard == 1 and timeofday == "Day" and charlottephase1interaction2 != 4:
        $ librarycard = 2
        jump charlottephase1interaction2part2
    elif librarycard == 1 and timeofday == "Morning" and charlottephase1interaction2 != 4:
        player "I should come back here in the day when Charlotte's here."
        jump overworldmap
    elif charlottephase1interaction2 == 1 and money < 75 and librarycard == 0:
        player "There's no point comming here if I don't have 75 dollars."
        jump overworldmap
    elif charlottephase1interaction2 == 1 and money >= 75:
        hide screen uppergui
        "Would you like to pay the 75 dollars for a library card?"
        "You currently have {color=#3eab33}[money]{/color}  dollars."
        menu:
            "Buy the library card":
                if timeofday == "Day":
                    $ money = money - 75
                    $ librarycard = 1
                    jump charlottephase1interaction2part2
                else:
                    "You bought the card"
                    $ money = money - 75
                    $ librarycard = 1
                    jump overworldmap

            "Don't buy it":
                jump overworldmap





    show screen uppergui
    if timeofday == "Morning" and miaphase1interaction3 == 2:

        player "Hmm I don't really know my way around this place I should wait until later to ask someone for help."
        jump overworldmap
    if timeofday == "Day" and charlottephase1interaction2 != 4 and charlottephase1interaction1 != 0 and (charlottephase1interaction2 != 3 and charlottephase1interaction3 != 1):
        if miaphase1interaction3 == 3:
            show screen mia_phone
        show screen charlotte_library


    call screen library

label leavelibrary:
    hide screen charlotte_library
    hide screen mia_phone
    jump overworldmap

label gfhouse:
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside
    hide screen mia_room
    stop music fadeout 5
    stop sound fadeout 5

    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    $ whereami = "gfhouse"
    hide screen charlottemia_room

#---------TO BE UNCOMMENTED WHEN chapter 2 is fully done--------------------
  #  if timeofday == "Morning" and miaphase2interaction2 == 4:
      #  "MC talks with Mia and they're gonna have a pizza party"
       # $ miaphase2interaction2 = 4
      #  jump overworldmap
#----------------------------------------------------------------------------

    if timeofday == "Night" and miaphase2interaction2 == 2:
        jump miaphase2interaction2part2 # Dinner with mia family scene

    if timeofday == "Night" and miaphase1interaction3 != 4:
        scene fs overworldnight
        player "Mia and her family are probably asleep I shouldn't wake them up."
        hide fs overworldnight
        jump overworldmap
    if miaphase1interaction1 == 0:
        scene fs overworld
        if timeofday == "Morning":
            player "Mia shouldn't be home right now she's probably at school."
        elif timeofday == "Day":
            player "I'm supposed to meet Mia at her school in the morning."
        hide fs overworld
        jump overworldmap
    elif miaphase1interaction1 == 1 and timeofday == "Morning":
        scene fs overworld
        player "It's still morning Mia won't be home right now, I should pass the time by working or sleeping."
        hide fs overworld
        jump overworldmap
    elif miaphase1interaction1 == 1 and timeofday == "Night":
        scene fs overworldnight
        player "Ah damn it's night time, I shouldn't bother Mia's family now, should come back during the day."
        hide fs overworldnight
        jump overworldmap
    elif miaphase1interaction1 >= 1:
        if miaphase1interaction3 == 4:
            jump miaifoundyourphone
        if miaphase1interaction1 == 1 and timeofday == "Day":
            jump miaphase1interaction1part2

        else:
            scene fs gfhouse
            show screen uppergui
            if juliachecker < 1:
                show screen julia_kitchen
            if juliachecker == 3:
                show screen julia_kitchen
            call screen gfhouse

    else:

        jump overworldmap

label miatopsteps:
    hide screen julia_kitchen
    hide screen katiesroomdoor
    hide screen mia_room
    hide screen backbuttonGFHALLWAY
    hide screen miasroomdoor
    hide screen uppergui
    scene fs gftopsteps
    with Dissolve(0.5)
    menu:
        "Go Down The Hallway":
            jump miahousehallway
        "Go To Master Bedroom":
            jump juliaroom
        "Go Back":
            jump gfhouse

label miahousehallway:
    $ whereami = "miashallway"
    hide screen charlottemia_room
    hide screen mia_room
    show screen uppergui
    hide screen julia_kitchen
    hide screen backbuttonGFROOM
    scene fs gfhousehallway
    show screen miasroomdoor
    show screen katiesroomdoor
    show screen backbuttonGFHALLWAY
    call screen miahallway


label juliaroom:


    if juliachecker == 4:
        "There's no one inside"
        jump miatopsteps
    elif juliachecker == 3:
        "There's no one inside"
        jump miatopsteps
    elif juliachecker == 2 and currentchapter > 1 and dayNumber > juliatouchday2:
        jump juliascene2

    elif juliachecker >= 1 and juliatouchday < dayNumber and juliachecker < 2:
        "As you approach the door you can hear someone making noise"
        julia "{size=-15}Ohhhh OHHHH YES!{/i}"
        julia "{size=-15}That's it mmmmm!{/i}"
        julia "{size=-15}God I wish I had the real thing right now!{/i}"
        julia "{size=-15}AHHN yesyesyesyes!{/size}"
        with vpunch
        julia "{size=-15}I'm CUMMING!!!{/size}"
        player "{i}Wow...I don't even know what to say.{/i}"
        player "{i}I wonder if I can peek in on her next time if I'm careful?{/i}"
        $ juliatouchday2 = dayNumber
        $ juliachecker = 2
        $ juliaquestlog = "Did I really hear Julia moaning in her room right? I should check again soon.."

        jump miatopsteps
    else:
        player "Hmmm, it's locked. Better not intrude."
    jump miatopsteps

label gfroom1:
    $ whereami = "gfroom"
    hide screen uppergui
    hide screen miasroomdoor
    hide screen katiesroomdoor
    hide screen backbuttonGFHALLWAY
    hide screen julia_kitchen
    if miaphase3interaction1 == 1 and timeofday == "Morning" and currentchapter == 3:
        jump miaphase3interaction1part2
    if miaphase1interaction1 == 3:
        jump miaisnthome
    if (miaphase1interaction2 == 0 or miaphase1interaction2 == 1) and miaphase1interaction1 > 2:
        if timeofday == "Day":
            show screen charlottemia_room

    if miaphase2interaction1 == 1 and miaphase1interaction3 >= 5 and currentchapter == 2 and timeofday != "Night":
        show screen mia_room

    scene fs gfroom
    call screen backbuttonGFROOM

label katiesroom:
    hide screen katiesroomdoor
    hide screen miasroomdoor
    if katiephase2interaction1 == 0:
        hide screen backbuttonGFHALLWAY
        hide screen uppergui
        player "Oh no, I'm not brave enough to go in there."
        player "Yet."
    elif katiephase2interaction1 == 1 and miaphase1interaction3 < 5:
        player "I know Katie asked me to talk to her in her room but I think I should get closer to Mia first before.."
        player "Dealing with her at all."
    elif katiephase2interaction1 == 1 and miaphase1interaction3 >= 5 and katieconversation >= 4:
        jump katiefootmassage
    elif katiephase2interaction1 == 2:
        player "I can't go back in there just yet. Katie's more than I can handle right now."
    jump miahousehallway

label gfhousehallway:
    hide screen julia_kitchen
    hide screen mia_room
    hide screen tosunnyside
    $ whereami = "gfhousehallway"
    show screen uppergui
    call screen gfhousehallway

label sophiahouse:
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside
    hide screen uppergui
    stop music fadeout 5


    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    if sophiaphase2interaction1 == 0 and currentchapter == 2 and sophiaphase1interaction2 > 1:
        jump sophiaphase2interaction1part1

    if sophiaphase1interaction2 == 1:
        jump sophiaphase1interaction2part2

    if timeofday == "Night":
        scene fs overworldnight
        player "Soph's probably sleeping, she'd kill me if I woke her up. Such a hypocrite."
        hide fs overworldnight
        jump overworldmap

    $ whereami = "sophiahouse"
    scene fs sophiahouseoutside
    if sophiaphase1interaction1 == 1: # should be time mattered but isnt great dev once again
        jump sophiaphase1interaction1part2

    show screen uppergui
    show screen backbuttonSOPHIAOUTSIDE
    call screen outsidesophiahouse

label apartmentlobbymenu:
    jump apartmentlobbyolivia


label apartmentlobbyolivia:
    hide screen locationname
    hide screen uppergui
    hide screen tonormalmap
    hide screen questboxpreview
    #######################################you can fix/change these withif statements to make them better
    
    if headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump gotosunnyside
    
    if oliviaphase2interaction1 == 0 and emilyphase2interaction1 < 2:
        player "That's a pretty big apartment building. Wonder if I know anyone who lives in there."
        jump gotosunnyside
    else:
        menu:
            "Buzz Olivia" if oliviaphase2interaction1 == 1:
                jump visitoliviabuilding
            "Buzz Olivia" if oliviaphase3interaction1 == 1 and timeofday == "Night":
                jump visitoliviabuilding
            "Buzz Stephanie" if emilyphase2interaction1 >= 2:
                jump visitstephaniebuilding
            "Buzz Penny" if pennyscene5 == 2 and timeofday == "Night":
                jump pennyphase2sex2
            "Back":
                jump gotosunnyside

label visitstephaniebuilding:
    #"[emilyphase2interaction1], [stephaniescene1]"
    if emilyphase2interaction1 == 2:
        jump emilyphase2interaction1part3
    elif emilyphase2interaction1 == 3:
        "BZZZZ"
        "....."
        "Nobody's home"
        jump gotosunnyside
    elif emilyphase2interaction1 >= 5:
        if stephaniescene1 == 0:
            jump stephaniescene1part1
        elif stephaniescene1 == 1:
            jump stephaniePivot
        elif stephaniescene1 == 2:
            jump stephaniePivot
        else:
            "BZZZZ"
            "....."
            "Nobody's home"
            jump gotosunnyside
    else:
        "BZZZ"
        player "No answer, I should come back later."
        jump gotosunnyside




label visitoliviabuilding:
    #"[oliviaphase3interaction1], [timeofday]"
    if oliviaphase2interaction1 == 1:
        if timeofday != "Night":
            player "Olivia told me to visit her at night, so I should come back then!"
            jump gotosunnyside
        else:
            jump oliviaphase2interaction1part2
    
    if oliviaphase3interaction1 == 1 and timeofday == "Night":
        jump oliviaphase3interaction1part2



label arcade:
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside
    
    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    $ whereami = "arcade"
    stop music fadeout 5
    if miaphase1interaction3 == 2:
        jump lookingforphonearcade



    if pennyscene5 == 1 and timeofday != "Night" and oliviaphase2interaction3 >= 1:
        jump pennyphase2sex1

    if (oliviaphase2interaction1 == 1 or oliviaphase2interaction1 == 2) and timeofday == "Morning":
        "You look around the arcade and don't see Olivia, she did mention she'd be at school in the Morning."
        jump overworldmap

    if oliviaphase2interaction1 == 1:
        player "I'm supposed to meet Olivia at her place at night."
        player "She said she lives in Sunnyside."
        jump overworldmap
    elif oliviaphase2interaction1 >= 2 and timeofday == "Day" and pennyscene1 == 0:
        jump pennyarcadescene
    elif oliviaphase2interaction1 >= 2 and timeofday == "Day" and pennyscene1 != 0:
        player "I don't currently have a reason to go to the arcade"
        jump overworldmap
    elif oliviaphase2interaction1 == 2 and timeofday != "Night" and pennyscene1 == 1:
        player "I don't currently have a reason to go to the arcade"
        jump overworldmap

    if oliviaphase1interaction3 == 2:
        if timeofday == "Morning":
            "You look around the arcade and don't see Olivia. So you go back outside."
            jump overworldmap

        elif timeofday == "Day" and currentchapter == 2:
            $ oliviaphase1interaction3 = 3
            jump oliviaphase2interaction1part1


    if oliviaphase1interaction1 == 1 and timeofday == "Day":
        jump oliviaphase1interaction1part2
    elif oliviaphase1interaction1 == 2 and timeofday == "Day":
        jump oliviaphase1interaction1part3
    elif oliviaphase1interaction1 == 3 and timeofday == "Day":
        "You look around but can't find Olivia, maybe you'll catch her in the morning at the school"
        jump overworldmap
    elif oliviaphase1interaction1 == 0:
        player "I don't have a reason to go to the arcade just yet."
        jump overworldmap
    elif oliviaphase1interaction2 == 1 and videogamecount == 1:
        player "I should try and find that game Olivia mentioned. It'll be a nice surprise."
        player "Maybe the mall sells it?"
        jump overworldmap
    elif oliviaphase1interaction2 == 1 and videogamecount == 1:
        jump oliviaphase1interaction2part2
    elif oliviaphase1interaction2 == 2 and timeofday == "Day":
        jump oliviaphase1interaction2part2
    elif oliviaphase1interaction2 == 1 and videogamecount == 0 and timeofday == "Day":
        jump oliviaphase1interaction2part2
    elif oliviaphase1interaction2 == 0 and videogamecount == 0 and timeofday == "Day":
        "You don't feel like going to the arcade right now. Maybe hang with Olivia in the morning?"
        jump overworldmap
    elif oliviaphase1interaction2 == 2 and timeofday != "Day":
        player "Olivia wouldn't be here right now, I should return during the afternoon."
        jump overworldmap
    elif oliviaphase1interaction2 == 3 and timeofday == "Day":
        jump oliviaphase1interaction2part3
    elif oliviaphase1interaction2 == 3 and timeofday != "Day":
        player "Olivia wouldn't be here right now, I should return during the afternoon."
        jump overworldmap
    elif oliviaphase1interaction2 == 4 and timeofday != "Night":
        player "I should just call Olivia from my room tonight."
        jump overworldmap



    elif timeofday == "Night":
        if oliviaquestlog == "Olivia's tournament is tonight!" and oliviaphase2interaction2 == 2:
            jump oliviaphase2interaction3part1
        else:
            player "I don't have a reason to go to the arcade at night."
            jump overworldmap
    elif timeofday == "Morning":
        player "Olivia wouldn't be at the arcade in the morning so there's no point in going there right now."
        jump overworldmap


    show screen olivia_atschool

label charlotteshouse:
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside
    hide screen uppergui
    $ whereami == "charlotteshouse"

    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    if dayNumber == 24 and timeofday == "Night":
        jump chapter3event1

    if charlottephase3interaction1 == 1 and timeofday != "Morning":
        jump charlottephase3interaction1part2

    if charlottephase2interaction1 == 2 and currentchapter == 2 and timeofday == "Night":
        if handcuffcount != 1 and condomcount != 1 and cameracount != 1:
            jump charlottephase2interaction1part2
        else:
            player "I should come back with all the items Charlotte wanted."
            jump overworldmap
    elif charlottephase2interaction1 == 2 and currentchapter == 2 and timeofday != "Night":
        player "I should come back at night with all the things Charlotte wanted me to get."
        player "A camera, some condoms, and some...handcuffs?"
        jump overworldmap
    elif charlottephase2interaction1 == 3 and currentchapter >= 2 and timeofday != "Night":
        "No reason to go there right now."
        jump overworldmap
    elif charlottephase2interaction1 >= 3 and currentchapter >= 2 and timeofday == "Night":
        jump victoriaPivot
    elif charlottephase1interaction2 == 3 and timeofday != "Night":
        player "Charlotte's not home right now. I'll come back at night."
        jump overworldmap
    elif charlottephase1interaction2 == 3 and timeofday == "Night":
        jump charlottephase1interaction3part1
    elif charlottephase1interaction3 == 2:
        "I don't need to go there right now."
        jump overworldmap

    else:
        player "Wow what a huge house. I wonder who lives there."
        jump overworldmap


label school:
    scene fs schoolhallwayextras
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside
    if timeofday == "Night":
        scene fs overworldnight
        player "Got no reason to go to the school at night."
        hide fs overworldnight
        jump overworldmap

    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    stop music fadeout 10
    if  whereami != "schoolhallway" and whereami != "school" and whereami != "classroom1" and whereami != "classroom3":
        stop sound
    if whereami != "schoolhallway" and whereami != "school" and whereami != "classroom1" and whereami != "classroom3":
        play sound "audio/schoolBG.mp3" loop fadein 5

    $ whereami = "school"

    hide screen sophia_atschool
    hide screen mia_atschool
    hide screen mia_sophia_atschool
    hide screen charlotte_library
    hide screen emily_atschool
    hide screen charlotte_school
    hide screen backbuttonCLASSROOM
    show screen uppergui

    

    if timeofday == "Morning" and avaphase1interaction2 != 4:
        show screen ava_atschool

    if timeofday == "Morning" and avaphase3interaction1 == 0 and avaphase2interaction3 == 2 and currentchapter == 3:
        show screen ava_atschool

    call screen school

label schoolhallway:
    $ whereami = "schoolhallway"
    hide screen questboxpreview
    hide screen uppergui
    hide screen ava_atschool
    hide screen locationname
    hide screen olivia_atschool
    scene fs schoolhallway2extras
    #"[emilyphase1interaction1],[emilyphase1interaction2],[emilyphase2interaction1],[emilyphase2interaction2]"

    if timeofday == "Morning" and emilyphase1interaction1 != 4 and (emilyphase2interaction1 <=4 and emilyphase2interaction1 != 1) :
        show screen emily_atschool
    #elif emilyphase1interaction2 == 6:
        #hide screen emily_atschool
    
    if timeofday == "Morning":
        if currentchapter == 2 and avaphase1interaction2 == 10:
            show screen ava_atschoolhallway
        if currentchapter == 2 and emilyphase1interaction2 >= 5 and (emilyphase2interaction1 >= 5 or emilyphase2interaction1 == 1) and emilyphase2interaction2 == 0:
            show screen emily_atschool

    if timeofday == "Day" and emilyphase1interaction1 >=1 and emilyphase1interaction1 != 4 and emilyphase1interaction2 < 6 :
        show screen emily_atschool

   


    call screen schoolhallway

label classroom1:
    $ whereami = "classroom1"
    hide screen questboxpreview
    hide screen ava_atschool
    #"[sophiaphase2interaction3], [currentchapter],[timeofday]"
    

    if miaphase1interaction1 >= 1 and timeofday == "Morning" and sophiaphase2interaction1 == 0:
        show screen sophia_atschool
    if sophiaphase1interaction2 != 2:
        if sophiaphase2interaction1 != 0:
            show screen sophia_atschool
    if sophiaphase2interaction1 == 0 and currentchapter == 2 and sophiaphase1interaction2 > 1:
        hide screen sophia_atschool
    if sophiaphase2interaction3 >= 2:
        hide screen sophia_atschool
    if sophiaphase1interaction1 == 5 and sophiaphase1interaction2 == 3 and sophiaphase2interaction1 == 2:
        hide screen sophia_atschool
        
    if miaphase1interaction3 == 4:
        hide screen sophia_atschool
        scene fs classroom
        player "Hmm, Mia's class is still going on. I'll just visit her house during the day to give her phone back."
        call screen classroom1

    if sophiaphase1interaction1 == 2 and timeofday != "Night": # should be morning tho bro wat
        jump sophiaphase1interaction1part3

    scene fs classroomextras
    hide screen uppergui
    if timeofday == "Morning":
        if miaphase1interaction1 == 0:
            show screen mia_sophia_atschool
        elif miaphase1interaction3 == 5 and charlottephase1interaction2 != 2:
            hide screen mia_atschool
        elif miaphase2interaction2 == 1:
            show screen mia_atschool
        elif miaphase2interaction1 == 2:
            hide screen mia_atschool
        elif miaphase2interaction2 != 4:
            show screen mia_atschool

    if timeofday == "Morning" and sophiaphase2interaction3 == 2 and currentchapter >= 3:
        show screen sophia_atschool

    if timeofday == "Morning":
        call screen classroom1
    else:
        call screen classroom1Day

label classroom2:
    $ whereami = "classroom2"
    hide screen emily_atschool
    scene fs classroom
    #if currentchapter == 2 and timeofday == "Day":
        #show screen ava_atschool

    if timeofday == "Morning" and oliviaphase1interaction3 != 2 and oliviaphase2interaction1 != 1:
        show screen olivia_atschool
    if timeofday == "Morning" and currentchapter >= 2 and oliviaphase1interaction2 == 2:
        hide screen olivia_atschool
        player "Hmmm, Olivia doesn't seem to be here right now."
        player "Maybe I can find her at the arcade again during the day."
        jump schoolhallway
    if timeofday == "Morning" and oliviaphase2interaction1 == 3 and oliviaphase2interaction2 == 1:
        hide screen olivia_atschool
    if timeofday == "Morning" and oliviaphase2interaction3 == 1 and currentchapter >=3:
        show screen olivia_atschool
    call screen classroom2


label classroom3:
    $ whereami = "classroom3"
    hide screen ava_atschool
    scene fs classroom3
    show screen backbuttonCLASSROOM
    if timeofday == "Morning" and charlottephase1interaction2 != 4:
        show screen charlotte_school
    
    if timeofday == "Morning" and charlottephase2interaction3 == 3 and currentchapter == 3:
        show screen charlotte_school

    call screen classroom3

label malllabel:
    hide screen uppergui
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside
    hide screen backbuttonSTORE
    hide hbashley current
    hide screen store_paint
    hide screen store_movie
    hide screen store_videogame
    hide screen store_candy
    hide screen store_watch
    hide screen store_Ashley
    hide screen store_camera

    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap


    #"[whereami]"
    if whereami != "mallstore":
        play music "audio/mallaudio.wav" fadein 10
    $ whereami = "mall"

    if miaphase1interaction3 == 2:
        jump lookingforphonemall

    if timeofday == "Day" and emilyphase2interaction1 >= 3 and ravenscene1 == 0:
        show screen raven_mall

    show screen backbuttonMALL
    call screen mall

label mallstore:
    hide screen questboxpreview
    hide screen backbuttonMALL
    hide screen uppergui
    hide screen raven_mall

    if timeofday == "Night":
        scene fs mall
        "The stores in the mall are closed at night."
        jump returnwhereyouare
    scene fs store

    $ whereami = "mallstore"

    if ashleychecker == 1 and amountspent >= 350 and watchcount == 0:
        jump ashleyinteraction1part2


    show hbashley current
    if firsttimestore == 0:
        jump storeintro
    else:
        show screen backbuttonSTORE
        show screen store_Ashley
        if watchcount > 0:
            show screen store_watch
        if paintcount > 0:
            show screen store_paint
        if moviecount > 0:
            show screen store_movie
        if candycount > 0:
            show screen store_candy
        if videogamecount > 0:
            show screen store_videogame
        if cameracount > 0:
            show screen store_camera
        call screen shoptime

    jump buysomething

label park:
    hide screen questboxpreview
    hide screen locationname
    hide screen tosunnyside

    if headtosunnyside == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to Sunnyside to pick up Mia and Katie."
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap

    $ whereami = "park"
    show screen uppergui
    if timeofday == "Night":
        scene fs parknight
    else:
        scene fs park
    window hide
    pause
    if miaphase1interaction3 == 2:
        jump lookingforphonepark
    if timeofday == "Night" and avaphase1interaction2 == 1:
        jump avaphase1interaction2part1
    elif timeofday == "Night" and avaphase1interaction2 == 2:
        jump avaphase1interaction2part3B
    
    if timeofday == "Night" and avaphase3interaction1 == 1:
        jump avaphase3interaction1part2
    jump overworldmap


label gotooverworldfromgfhouse:
    hide screen julia_kitchen
    jump overworldmap

# functions------------------------------------------------------------------------------------------------

label changetextbox:
    if hiden_textbox == False:
        $ hiden_textbox = True
    else:
        $ hiden_textbox = False


label viewquests:
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
        if timeofday == "Night":#------------------------------this will be the updated whereami code!!-------------
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
    elif whereami == "miashallway":
        scene fs gfhousehallway
    elif whereami == "sophiahouse":
        scene fs sophiahouse
    elif whereami == "school":
        hide screen ava_atschool
        scene fs schoolhallway
    elif whereami == "schoolhallway":
        hide screen emily_atschool
        scene fs schoolhallway2extras
    elif whereami == "classroom1":
        hide screen mia_atschool
        hide screen sophia_atschool
        hide screen mia_sophia_atschool
        scene fs classroom
    elif whereami == "mall":
        hide screen backbuttonMALL
        scene fs mall

    call screen questbox

label useinventory:
    #hide screen uppergui

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
        if timeofday == "Night":#------------------------------this will be the updated whereami code!!-------------
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
    elif whereami == "miashallway":
        scene fs gfhousehallway
    elif whereami == "sophiahouse":
        scene fs sophiahouse
    elif whereami == "school":
        hide screen ava_atschool
        scene fs schoolhallway
    elif whereami == "schoolhallway":
        hide screen emily_atschool
        scene fs schoolhallway2extras
    elif whereami == "classroom1":
        hide screen mia_atschool
        hide screen sophia_atschool
        hide screen mia_sophia_atschool
        scene fs classroom
    elif whereami == "mall":
        hide screen backbuttonMALL
        scene fs mall

    call screen inventory(item_list,adj=tutorials_adjustment)

label gotosleep:
    hide screen uppergui
    hide screen backbuttonROOM
    #$ katiephase3interaction1 = 0 #delete this liiiiiinnne afterrrr you test the katie scene---------------------------------

    if dayNumber == 24 and timeofday == "Night":
        player "It's the sleepover night!"
        player "I should head to Charlotte's house."
        jump playerRoom

    if miaphase3interaction1 >= 2 and currentchapter == 3 and katiephase3interaction1 == 0 and dayNumber > 22 and timeofday == "Night":
        jump katiephase3interaction1part1
    if miaphase2interaction1 == 2 and currentchapter > 1 and katiephase2interaction1 == 2 and timeofday == "Night":
        jump katiesecondselfie

    if miaphase2interaction1 >= 2 and currentchapter > 1 and katiephase2interaction1 == 3 and timeofday == "Night":
        if katiebjday != dayNumber:
            jump katieblowjob

    if emilyphase1interaction1 == 2 and timeofday == "Night":
        $ emilyphase1interaction1 = 3
        jump thinkaboutemilybeforesleep
    elif emilyphase1interaction1 == 4 and timeofday == "Night":
        $ emilyphase1interaction1 = 5
        jump thinkaboutemilybeforesleep2

    if sophiaphase1interaction1 == 3 and timeofday == "Night":
        jump sophiaphase1interaction1part4

    elif sophiaphase2interaction1 == 2 and timeofday == "Night":
        if sophiascenedaycheck == 1:
            $ sophiascenedaycheck = 2
        else:
            jump sophiaphase2interaction2part3
    elif sophiaphase2interaction1 == 3 and timeofday == "Night" and cassandrascene1 == 0:
        jump cassandraboobjob
    
    if sophiaphase3interaction1 == 1 and timeofday == "Night" and currentchapter == 3:
        jump sophiaphase3interaction1part2

    if charlottephase2interaction1 == 1 and timeofday == "Night" and currentchapter > 1:
        jump charlottephase2interaction1part1NIGHT

    if charlottephase2interaction2 == 1 and timeofday == "Night":
        $ charlottephase2interaction2 = 2
    

    if charlottephase2interaction2 == 4 and charlottedaychecker1 < dayNumber and timeofday == "Night":
        jump charlottephase2interaction3part1
    elif charlottephase2interaction3 == 1 and timeofday == "Night":
        jump charlottephase2interaction3part2
    
    if charlottephase2interaction3 == 2 and charlottedaychecker2 < (dayNumber - 1) and timeofday == "Night":
        jump charlottephase2interaction4part1


    if ravenscene1 == 1 and timeofday == "Night":
        jump ravenPivot

    if avajobinterview != 999 and timeofday == "Night":
        jump didshemakeit
        

    if oliviaquestlog == "I gotta wait for the tournament in 2 days!":
        $ oliviaquestlog = "I gotta wait for the tournament tomorrow!"
    elif oliviaquestlog == "I gotta wait for the tournament tomorrow!":
        $ oliviaquestlog = "Olivia's tournament is tonight!"


    scene fs playerroomDay
    if timeofday == "Morning":
        scene fs playerroomMorn
        $ timeofday = "Day"
    elif timeofday == "Day":
        scene fs playerroomDay
        $ timeofday = "Night"
    elif timeofday == "Night":
        scene fs playerroomNight
        $ dayNumber += 1
        $ timeofday = "Morning"
        if dayName == "Monday":
            $ dayName = "Tuesday"
        elif dayName == "Tuesday":
            $ dayName = "Wednesday"
        elif dayName == "Wednesday":
            $ dayName = "Thursday"
        elif dayName == "Thursday":
            $ dayName = "Friday"
        elif dayName == "Friday":
            $ dayName = "Saturday"
        elif dayName == "Saturday":
            $ dayName = "Sunday"
        elif dayName == "Sunday":
            $ dayName = "Monday"

        #"Day Number [dayNumber]"


    scene fs blackblank
    with Dissolve(0.3)
    pause 0.3
    if dayNumber == 10:
        jump phase1ending
    elif dayNumber == 20:
        jump phase2ending
    jump playerRoom

label explorebeach:
    #scene fs beachwithgirls

    with Dissolve(0.7)
    show screen charlotte_beach
    if swimsuitchoice == "white":
        show screen mia_beach1
    elif swimsuitchoice == "green":
        show screen mia_beach2
    elif swimsuitchoice == "purple":
        show screen mia_beach3
    else:
        show screen mia_beach1
    show screen sophia_beach
    show screen ava_beach
    show screen emily_beach
    show screen olivia_beach
    show screen backbuttonBEACH
    scene fs beach
    with Dissolve(0.5)
    "You can now explore the beach and talk to whomever you like"
    
    call screen beach_screen

label endofchapter2:
    "You've reached the end of chapter 2"
    "If you cannot progress with any of the girls you have not explored enough of their content up to this point"
    "I recommend going to a previous save or restarting to explore more content!"
    "Thanks for playing!"
    jump explorebeach

label howmuchmoneydoihave:
    hide screen uppergui
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
        if timeofday == "Night":#------------------------------this will be the updated whereami code!!-------------
            scene fs livingroomnight
        else:
            scene fs livingroom
    elif whereami == "overworldmap" and timeofday == "Night":
        scene fs overworldnight
    elif whereami == "overworldmap":
        scene fs overworld
    elif whereami == "gym":
        scene fs gymarea
    elif whereami == "library":
        scene fs library
    elif whereami == "arcade":
        scene fs arcade
    elif whereami == "gfhouse":
        scene fs gfhouse
    elif whereami == "miashallway":
        hide screen katiesroomdoor
        hide screen miasroomdoor
        scene fs gfhousehallway
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
    "I have {color=#3eab33}[money]{/color} Dollars."
    jump returnwhereyouare

label passtime:

    if dayNumber == 24 and timeofday == "Night":
        $ dayNumber += 1
         
    if timeofday == "Morning":
        scene fs playerroomMorn
        $ timeofday = "Day"
    elif timeofday == "Day":
        scene fs playerroomDay
        $ timeofday = "Night"
    elif timeofday == "Night":
        scene fs playerroomNight
        $ timeofday = "Morning"
        if dayName == "Monday":
            $ dayName = "Tuesday"
        elif dayName == "Tuesday":
            $ dayName = "Wednesday"
        elif dayName == "Wednesday":
            $ dayName = "Thursday"
        elif dayName == "Thursday":
            $ dayName = "Friday"
        elif dayName == "Friday":
            $ dayName = "Saturday"
        elif dayName == "Saturday":
            $ dayName = "Sunday"
        elif dayName == "Sunday":
            $ dayName = "Monday"
    
    

    scene fs blackblank
    with Dissolve(0.3)
    pause 0.3
    jump overworldmap

label checkphone:
    if headtosunnyside == 1:
        player "No time to call anyone I should head go pick up Mia and Katie"
        jump overworldmap
    elif headtooffice == 1:
        hide screen uppergui
        hide screen tosunnyside
        player "I should head to the office building in Sunnyside."
        jump overworldmap
    show screen contacts

label gotophonefromcontacts:
    hide screen gameGallery
    hide screen phonecontacts
    call screen contacts



label gotopicturesfromphone:
    hide contacts
    hide screen ava_atschool
    hide screen uppergui
    if whereami == "playerRoom" and timeofday == "Morning":
        scene fs playerroomMorn
    elif whereami == "playerRoom" and timeofday == "Day":
        scene fs playerroomDay
    elif whereami == "playerRoom" and timeofday == "Night":
        scene fs playerroomNight
    elif whereami == "livingRoom":
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
    elif whereami == "miashallway":
        scene fs gfhousehallway
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
        scene fs mall

    call screen gameGallery

label lookatkatieselfie:
    scene fs katieselfie2
    pause
    jump gotowork

label gotowork:
    if timeofday == "Morning":
        hide screen uppergui
        hide screen backbuttonROOM
        hide screen locationname
        scene fs computerscreen
        "How long would you like to work for?"
        menu:
            "One Shift":
                jump workoneshift
            "Two Shifts":
                jump worktwoshifts
            "Check Katie's Email" if katiephase2interaction1 >= 3:
                jump lookatkatieselfie
            "Nevermind":
                jump returnwhereyouare
            "Patrons":
                jump creditlist
            #"Test":
                #jump test4
                #jump test2
                #jump sophiaphase1interaction2part2

    elif timeofday == "Day":
        hide screen uppgui
        hide screen backbuttonROOM
        hide screen locationname
        scene fs computerscreen
        "Would you like to work?"
        menu:
            "One Shift":
                jump workoneshift
            "Nevermind":
                jump returnwhereyouare
            #"Tester":
                #"[miaphase2interaction1],[miaphase2interaction2]"

    elif timeofday == "Night":
        if oliviaphase2interaction2 == 1 or pennyscene2 >= 1:
            hide screen uppergui
            hide screen backbuttonROOM

            menu:
                "Game with Olivia" if oliviaphase2interaction2 == 1:
                    jump oliviaphase2interaction2part2
                "Watch Penny's Stream" if pennyscene2 == 1:

                    jump pennyfirststream
                "Watch Penny's Stream" if pennyscene3 == 1:

                    jump pennysecondstream
                "Watch Penny's Stream" if pennyscene4 == 1:
                    jump pennythirdstream
                "Nevermind":
                    jump playerRoom

        hide screen backbuttonROOM
        hide screen uppergui
        "You're too tired to work at this time of night"
        jump returnwhereyouare

label test2:
    image charlottetest1 movie = Movie(channel="charlottetest", play="images/animations/40_11 Charlotte self touch on bed.webm")
    image charlottetest2 movie = Movie(channel="charlottetest", play="images/animations/40_12 Charlotte self touch on bed.webm")
    show charlottetest1 movie
    ""
    show charlottetest2 movie
    ""
label test4:
    image jacuzzi movie = Movie(channel="jacuzzi", play="images/animations/CG72_10 - Mia gives boobjob.webm")
    show jacuzzi movie
    pause
    image jacuzzi2 movie = Movie(channel="jacuzzi", play="images/animations/CG72_11 - Mia gives boobjob faster.webm")
    show jacuzzi2 movie
    pause
    image jacuzzi3 movie = Movie(channel="jacuzzi", play="images/animations/CG72_12 - Mia gives head and jerks MC pp.webm")
    show jacuzzi3 movie
    pause
    image jacuzzi4 movie = Movie(channel="jacuzzi", play="images/animations/CG72_13 - Mia deepthroats as MC cums.webm")
    show jacuzzi4 movie
    pause

label testpuzzles:
    #show screen puzzle_paper2
    #show screen puzzle_paper3
    #show screen puzzle_paper4
    #show screen puzzle_paper5
    #show screen puzzle_paper6
    #show paperpuzzle2
    #show paperpuzzle3
    #show paperpuzzle4
    #show paperpuzzle5
    #show paperpuzzle6
    #show screen puzzle_paper1
    #pause
    call screen secondpuzzlegame

    "Alright lets test this"



label rotatepaper2:
    image newpaperpuzzle2 = Transform("paperpuzzle2", rotate=30)
    image paperpuzzle2 = "newpaperpuzzle2"
    jump testpuzzles


label creditlist:
    "Thank you to all the Patrons who have been supporting me and this project!"
    call screen patroncredits(adj=tutorials_adjustment)
    jump returnwhereyouare

label workoneshift:
    $ money += 50
    jump passtime

label worktwoshifts:
    $ money += 100
    scene fs playerroomNight
    $ timeofday = "Night"
    jump returnwhereyouare

label deactivatephone:
    hide screen contacts
    hide screen phonecontacts
    if whereami == "playerRoom":
        jump playerRoom
    elif whereami == "livingRoom":
        if timeofday == "Night":
            scene fs livingroomnight
        else:
            scene fs livingroom
    elif whereami == "overworldmap":
        jump overworldmap
    elif whereami == "gym":
        jump gym
    elif whereami == "library":
        jump library
    elif whereami == "arcade":
        jump arcade
    elif whereami == "gfhouse":
        jump gfhouse
    elif whereami == "miashallway":
        jump miahousehallway
    elif whereami == "sophiahouse":
        jump sophiahouse
    elif whereami == "school":
        jump school
    elif whereami == "schoolhallway":
        jump schoolhallway
    elif whereami == "classroom1":
        jump classroom1
    elif whereami == "classroom2":
        jump classroom2
    elif whereami == "classroom3":
        jump classroom3
    elif whereami == "mall":
        jump malllabel
    elif whereami == "beach":
        jump beach
    elif whereami == "cafe":
        jump insidecafe


label returnwhereyouare:
    if whereami == "mall":
        jump malllabel
    elif whereami == "classroom1":
        jump classroom1
    elif whereami == "classroom2":
        jump classroom2
    elif whereami == "classroom3":
        jump classroom3
    elif whereami == "schoolhallway":
        jump schoolhallway
    elif whereami == "school":
        jump school
    elif whereami == "arcade":
        jump arcade
    elif whereami == "sophiahouse":
        jump sophiahouse
    elif whereami == "gfhousehallway":
        jump gfhousehallway
    elif whereami == "gfhouse":
        jump gfhouse
    elif whereami == "miashallway":
        jump miahousehallway
    elif whereami == "gfroom":
        jump gfroom1
    elif whereami == "library":
        jump library
    elif whereami == "gym":
        jump gym
    elif whereami == "park":
        jump park
    elif whereami == "outsidegym":
        jump outsidegym
    elif whereami == "overworldmap":
        jump overworldmap
    elif whereami == "sunnysidemap":
        jump gotosunnyside
    elif whereami == "livingRoom":
        jump playerlivingroom
    elif whereami == "playerRoom":
        jump playerRoom
    elif whereami == "beach":
        jump beach
    elif whereami == "cafe":
        jump insidecafe
    elif whereami == "club":
        jump insideclub
    elif whereami == "outsideoffice":
        jump outsideoffice

transform surpriseshake:
    linear 0.1 yoffset -6
    linear 0.1 yoffset 0
    linear 0.1 yoffset -4
    linear 0.1 yoffset 0

transform fuckleft:
    linear 0.1 xoffset -6
    linear 0.7 xoffset 0
    repeat

transform slowfingerfuck:
    linear 0.5 yoffset 3
    linear 1.0 yoffset 0
    repeat

transform slowfingerfuck2:
    linear 0.2 yoffset 3
    linear 0.5 yoffset 0
    repeat
transform slowfingerfuck3:
    linear 0.08 yoffset 3
    linear 0.2 yoffset 0
    repeat

# ---------------------------MALL AND STORES AND ITEM DESCRIPTIONS--------------------------------------------------------

label buysomething:
    scene fs mall
    if avaphase1interaction2 == 6:
        player "Let's check out what I can buy."
        menu:
            "Fit Bitonator":
                jump buyfitbit
            "Back":
                jump returnwhereyouare
    else:
        menu:
            "Back":
                jump returnwhereyouare

label buyfitbit:

    player "Huh it's some sort of smart watch, $105 Dollars. Should I get it?"
    menu:
        "Buy":
            jump buyfitbit2
        "Don't Buy":
            jump buysomething

    label buyfitbit2:
        if money >= 105:
            $ money -= 105
            $ avaphase1interaction2 = 7
            player "Hey Ava, meet me at the park tonight. It's important."
            ava "Why can't you just tell me here?"
            player "Wear your gym clothes."
            ava "I'm not going unless you tell me why!"
            player "See you there."
            jump buysomething
        else:
            player "Don't have enough money. Should do some work and come back."
            jump buysomething



label itspaint:

    "It's a bucket of paint, seems as though it'll paint whatever color you need."
    call screen inventory(item_list, adj=tutorials_adjustment)
label itsmovie:

    player "It's a cheesy horror movie. Wouldn't mind cuddling up to someone to watch it."
    call screen inventory(item_list, adj=tutorials_adjustment)
label itsvideogame:

    player "Mortal Street Caliber 3, man what a classic!"
    call screen inventory(item_list, adj=tutorials_adjustment)
label itscandy:

    player "Strawberry flavored candy. Ashley said that the town banned it's import."
    if emilyphase1interaction2 >= 2:
        player "I should be able to use this to manipulate Emily in some way."
        player "You know...if that was something I wanted to do."
    call screen inventory(item_list, adj=tutorials_adjustment)
label itswatch:

    player "It's that super watch I bought from Ashley at the mall."
    player "She said in a later build she's gonna suck me off when I buy it."
    player "Wonder who's future content this is?"
    call screen inventory(item_list, adj=tutorials_adjustment)

label itscamera:
    player "A Pixon 2020T. Seems like a decent quality camera."
    call screen inventory(item_list, adj=tutorials_adjustment)
label itscondom:
    player "A pack of extra large extra thin condoms."
    player "I try to stay humble about the size of my dick but...it's pretty awesome."
    call screen inventory(item_list, adj=tutorials_adjustment)
label itshandcuffs:
    player "Some fuzzy toy handcuffs, I'm sure I can have some fun using these with someone."
    player "Hmmmm."
    call screen inventory(item_list, adj=tutorials_adjustment)







# CHARACTER PIVOTS-----------------------------------------------------------------------------------
label machinePivot:
    hide screen uppergui
    hide screen ava_atgym

    if avaphase1interaction1 == 2:
        jump avaphase1interaction1part3
    else:
        "Machine" "Leave me alone meat bag."
        player "Wait what?"
        jump returnwhereyouare

label avaPivot:


    hide screen uppergui
    hide screen ava_atschool

    #location matters
    if whereami != "Park" and timeofday != "Night" and avaphase1interaction2 == 2:
        scene fs schoolhallway
        player "I'm meeting Ava at the park at night, I should leave her alone for now."
        jump returnwhereyouare

    if whereami == "school":

        if timeofday == "Morning":

            if avaphase3interaction1 == 0 and avaphase2interaction3 == 2 and currentchapter == 3:
                jump avaphase3interaction1part1

            if avaphase1interaction1 == 0:
                jump avaphase1interaction1part1
            elif avaphase1interaction1 == 1:
                jump avaphase1interaction1part1postconvo
            elif avaphase1interaction1 == 2:
                jump avayoushouldbuygympass
            elif avaphase1interaction1 == 3:
                jump igotthepassava
            elif avaphase1interaction1 == 4:
                jump avaatschoolinteraction1
            elif avaphase1interaction1 == 5:
                if avaphase1interaction2 == 1:
                    scene fs schoolhallway
                    player "Wait I'm meeting her at the park tonight right? I'll see her later."
                    jump returnwhereyouare
                else:
                    "shouldn't be here"
                    jump returnwhereyouare
            elif avaphase1interaction1 == 6:
                if avaphase1interaction2 == 3:
                    jump avaphase1interaction2part3C
                else:
                    "You shouldn't be here 2"
                    jump returnwhereyouare


    elif whereami == "gym":

        if timeofday == "Morning":
            if avaphase2interaction1 == 0:
                jump avaphase2interaction1part1
            elif avaphase2interaction1 == 1:
                jump avaphase2whereshouldwemeetagain
            elif avaphase2interaction1 == 2:
                jump avaphase2interaction1part3

        elif timeofday == "Day":

            if avaphase2interaction3 == 1:
                jump avaphase2interaction3part1

            if avaphase1interaction1 == 1:
                jump avaphase1interaction1part2
            elif avaphase1interaction1 == 2:
                jump avayoushouldbuygympass
            elif avaphase1interaction1 == 3:
                jump avaphase1interaction1part4
            elif avaphase1interaction1 == 4:
                jump avaphase1interaction2part1

            if avaphase1interaction2 == 2: # unreachable look at start of label
                jump avaphase1interaction2part2
            elif avaphase1interaction2 == 4:
                jump avaseemsfocused
            elif avaphase1interaction1 == 6:
                if avaphase1interaction2 == 3:
                    jump avaphase1interaction2part3C



    elif whereami == "park":

        #location doesn't matter
        if whereami != "Park" and avaphase1interaction2 == 5:
            jump letsmeetatthepark

        #location matters
        if timeofday == "Night":
            if avaphase1interaction2 == 3:
                jump avaphase1interaction2part3


    elif whereami == "classroom2":
        if timeofday == "Day":
            if avaphase2interaction1 == 1:
                if currentchapter > 1:
                    jump avaphase2interaction1part2
            elif avaphase2interaction1 == 2:
                if currentchapter > 1:
                    jump avaphase2whereshouldwemeetagain2



    #
    # hide screen uppergui
    # hide screen ava_atschool
    #
    # # Note: phase interaction numbers should be backwards to have the newest possible action happen first
    #
    #
    # if whereami == "classroom2" and timeofday == "Day" and avaphase2interaction1 == 1 and currentchapter > 1:
    #     jump avaphase2interaction1part2
    # elif whereami == "classroom2" and timeofday == "Day" and avaphase2interaction1 == 2 and currentchapter > 1:
    #     jump avaphase2whereshouldwemeetagain2
    #
    #
    # if whereami == "school" and timeofday == "Morning" and avaphase1interaction1 == 0:
    #     jump avaphase1interaction1part1
    # elif whereami == "school" and timeofday == "Morning" and avaphase1interaction1 == 1:
    #     jump avaphase1interaction1part1postconvo
    # elif whereami == "school" and timeofday == "Morning" and avaphase1interaction1 == 2:
    #     jump avayoushouldbuygympass
    # elif whereami == "school" and timeofday == "Morning" and avaphase1interaction1 == 3:
    #     jump igotthepassava
    # elif whereami == "school" and timeofday == "Morning" and avaphase1interaction1 == 4:
    #     jump avaatschoolinteraction1
    # elif whereami == "school" and timeofday == "Morning" and avaphase1interaction1 == 5 and avaphase1interaction2 == 1:
    #     scene fs schoolhallway
    #     player "Wait I'm meeting her at the park tonight right? I'll see her later."
    #     jump returnwhereyouare
    # elif whereami == "school" and timeofday == "Morning" and avaphase1interaction1 == 6 and avaphase1interaction2 == 3:
    #     scene fs schoolhallway
    #     jump avaphase1interaction2part3C
    # elif whereami != "Park" and timeofday != "Night" and avaphase1interaction2 == 2:
    #     scene fs schoolhallway
    #     player "I'm meeting Ava at the park at night, I should leave her alone for now."
    #     jump returnwhereyouare
    #
    # if whereami == "gym" and timeofday == "Morning" and avaphase2interaction1 == 0:
    #     jump avaphase2interaction1part1
    # elif whereami == "gym" and timeofday == "Morning" and avaphase2interaction1 == 1:
    #     jump avaphase2whereshouldwemeetagain
    # elif whereami == "gym" and timeofday == "Morning" and avaphase2interaction1 == 2:
    #     jump avaphase2interaction1part3
    # elif whereami == "gym" and timeofday == "Day" and avaphase1interaction2 == 2:
    #     jump avaphase1interaction2part2
    # elif whereami == "park" and timeofday == "Night" and avaphase1interaction2 == 3:
    #     jump avaphase1interaction2part3
    # elif whereami == "gym" and timeofday == "Day" and avaphase1interaction2 == 4:
    #     jump avaseemsfocused
    # elif whereami == "gym" and timeofday == "Day" and avaphase1interaction1 == 1:
    #     jump avaphase1interaction1part2
    # elif whereami == "gym" and timeofday == "Day" and avaphase1interaction1 == 2:
    #     jump avayoushouldbuygympass
    # elif whereami == "gym" and timeofday == "Day" and avaphase1interaction1 == 3:
    #     jump avaphase1interaction1part4
    # elif whereami == "gym" and timeofday == "Day" and avaphase1interaction1 == 4:
    #     jump avaphase1interaction2part1
    #
    #
    #
    #
    #
    # if whereami != "Park" and avaphase1interaction2 == 5:
    #     jump letsmeetatthepark



label emilyPivot:
   # "[emilyphase1interaction1][emilyphase1interaction2][emilyphase1interaction3]"
    #"[emilyphase2interaction1][emilyphase2interaction2][emilyphase2interaction3]"
    #location doesn't matter
    #"[emilyphase3interaction1], [whereami], [currentchapter]"
    if emilyphase3interaction1 == 1 and currentchapter == 3:
        if (whereami == "playerRoom" or whereami == "livingRoom"):
            if emilydaychecker < dayNumber:
                if timeofday != "Night":
                    if "Candy" in item_list:
                        jump emilyphase3interaction1part2
                    else:
                        hide screen uppergui
                        hide screen phonecontacts
                        hide screen backbuttonLIVINGROOM
                        hide screen backbuttonROOM
                        hide screen questboxpreview

                        player "{i}Oh damn I don't have any snacks! I should get candy from the store{/i}"
                        jump returnwhereyouare

                else:
                    hide screen uppergui
                    hide screen phonecontacts
                    hide screen backbuttonLIVINGROOM
                    hide screen backbuttonROOM
                    hide screen questboxpreview

                    player "{i}We're not seeing the movie at night, I'll call her tomorrow with snacks{/i}"
                    jump returnwhereyouare
            else:
                hide screen uppergui
                hide screen phonecontacts
                hide screen backbuttonLIVINGROOM
                hide screen backbuttonROOM
                hide screen questboxpreview
                player "{i}We're not seeing the movie today I'll call her during the day tomorrow with snacks{/i}"
                jump returnwhereyouare
        else:
            hide screen uppergui
            hide screen phonecontacts
            player "{i}I'll call her from home when I have snacks.{/i}"
            jump returnwhereyouare
            


            
    if emilyphase2interaction1 == 2:
        hide screen contacts
        hide screen phonecontacts
        emily "Sorry I can't talk right now!"
        jump returnwhereyouare

    elif emilyphase1interaction2 == 6 and currentchapter == 1:
        hide screen uppergui
        hide screen contacts
        hide screen phonecontacts
        player "She probably wants to make the finishing touches on the banner, I'll see her at the track meet."
        jump returnwhereyouare

    if emilyphase2interaction2 == 2 and currentchapter >= 2 and (whereami == "playerRoom" or whereami == "livingRoom") and timeofday == "Night":
        hide screen phonecontacts
        hide screen uppergui
        jump emilyphase2interaction2part3
    elif emilyphase2interaction2 == 2:
        hide screen phonecontacts
        hide screen uppergui
        hide screen questboxpreview
        player "I should call Emily over tonight, I want to take the next step."
        jump returnwhereyouare

    #location is negative
    if whereami != "schoolhallway":
        if emilyphase1interaction2 == 3:
            hide screen phonecontacts
            hide screen contacts
            player "No reason to call her until I have the paint."
            jump returnwhereyouare
        elif emilyphase1interaction2 == 5:
            hide screen uppergui
            hide screen contacts
            hide screen phonecontacts
            player "I don't want to text Emily just yet, I'll talk to her at the school in person."
            jump returnwhereyouare

        elif emilyphase1interaction2 == 6:
            if emilyphase2interaction1 == 0:
                if currentchapter > 1:
                    hide screen contacts
                    hide screen phonecontacts
                    player "I'll find Emily at school still in the morning, no need to text her."
                    jump returnwhereyouare

        if emilyphase2interaction1 == 1:
            hide screen phone
            hide screen phonecontacts
            player "I should check in with Emily in person at school again."
            jump returnwhereyouare



    if whereami != "livingRoom" and whereami != "playerRoom":
        if emilyphase1interaction2 == 4:
            player "I'll call her from my place. I want her to get used to being there."
            jump returnwhereyouare

    if whereami == "livingRoom" or whereami == "playerRoom":
        if timeofday != "Night":
            if emilyphase1interaction2 == 4:
                jump emilyphase1interaction2part3
        elif timeofday == "Night":
            if emilyphase1interaction2 == 4:
                hide screen phonecontacts
                hide screen contacts
                hide screen backbuttonROOM
                hide screen backbuttonLIVINGROOM
                player "I think I'll call her during the day, atmosphere might be better."
                player "Don't want her getting any hints about my intentions just yet."
                jump returnwhereyouare

    if whereami != "schoolhallway" and whereami != "library":
        if emilyphase2interaction1 == 3:
            hide screen contacts
            hide screen phonecontacts
            emily "Hello?"
            player "Hey I got the papers!"
            emily "No way! Please get them to me as soon as possible!!"
            jump returnwhereyouare


    if whereami != "playerRoom":
        if emilyphase2interaction1 == 4:
            hide screen contacts
            hide screen phonecontacts
            player "I should call Emily from my room."
            jump returnwhereyouare


    if whereami == "schoolhallway":


        #timeofday doesnt matter
        if emilyphase1interaction2 == 1:
            jump emilyphase1interaction2part1
        elif emilyphase1interaction2 == 3:
            scene fs schoolhallway2extras
            hide screen emily_atschool
            player "No point in talking to her right now, I should find some paint first."
            jump returnwhereyouare
        elif emilyphase1interaction2 == 6:
            if emilyphase2interaction1 == 0:
                if currentchapter > 1:
                    jump emilyphase2interaction1part1
                else:
                    scene fs schoolhallway2
                    player "She probably wants to make the finishing touches on the banner, I'll see her at the track meet."
                    jump returnwhereyouare

        #timeofday matters
        if timeofday == "Morning":
            if emilyphase1interaction1 == 0:
                jump emilyphase1interaction1part1
            elif emilyphase1interaction1 == 1:
                jump emilyisbusy
            elif emilyphase1interaction1 == 2:
                jump whensthepaintagain2

            if emilyphase2interaction1 == 1:
                jump emilyphase2interaction1part2

            if emilyphase1interaction2 == 2:
                jump emilyrunsaway

            if emilyphase1interaction2 >= 5 and emilyphase2interaction1 >= 5 and emilyphase2interaction2 == 0:
                jump emilyphase2interaction2part1

        elif timeofday == "Day":
            if emilyphase1interaction1 == 1:
                jump emilyphase1interaction1part2

            if emilyphase1interaction2 == 2:
                jump emilyphase1interaction2part2
        if timeofday != "Night":
            if emilyphase1interaction1 == 3:
                jump emilyphase1interaction1part3
            if emilyphase1interaction2 == 5:
                jump emilyphase1interaction2part4

            if emilyphase2interaction1 == 3:
                jump emilyphase2interaction1part4

    if whereami == "library":
        if timeofday != "Night":
            if emilyphase2interaction1 == 3:
                jump emilyphase2interaction1part4








    # if emilyphase1interaction2 == 6 and emilyphase2interaction1 == 0 and currentchapter == 2 and whereami == "schoolhallway":
    #     jump emilyphase2interaction1part1
    # elif emilyphase2interaction1 == 1 and timeofday == "Morning" and whereami == "schoolhallway" and emilyphase2interaction1 != 2:
    #     jump emilyphase2interaction1part2
    # elif emilyphase2interaction1 == 3 and timeofday != "Night" and (whereami == "schoolhallway" or whereami == "library"):
    #     jump emilyphase2interaction1part4
    # elif emilyphase2interaction1 == 2:
    #     hide screen contacts
    #     hide screen phonecontacts
    #     emily "Sorry I can't talk right now!"
    #     jump returnwhereyouare
    # elif emilyphase2interaction1 == 3:
    #     hide screen contacts
    #     hide screen phonecontacts
    #     emily "Hello?"
    #     player "Hey I got the papers!"
    #     emily "No way! Please get them to me as soon as possible!!"
    #     jump returnwhereyouare
    # elif emilyphase2interaction1 == 4 and whereami != "playerRoom":
    #     hide screen contacts
    #     hide screen phonecontacts
    #     player "I should call Emily from my room."
    #     jump returnwhereyouare
    #
    #
    #
    # if emilyphase1interaction1 == 0 and whereami == "schoolhallway" and timeofday == "Morning":
    #     hide screen uppergui
    #     jump emilyphase1interaction1part1
    # elif emilyphase1interaction1 == 1 and whereami == "schoolhallway" and timeofday == "Morning":
    #     jump emilyisbusy
    # elif emilyphase1interaction1 == 1 and whereami == "schoolhallway" and timeofday == "Day":
    #     jump emilyphase1interaction1part2
    # elif emilyphase1interaction1 == 2 and whereami == "schoolhallway" and timeofday == "Morning":
    #     jump whensthepaintagain2
    # elif emilyphase1interaction1 == 3 and whereami == "schoolhallway" and timeofday != "Night":
    #     jump emilyphase1interaction1part3
    #
    # if emilyphase1interaction2 == 1 and whereami == "schoolhallway":
    #     hide screen uppergui
    #     jump emilyphase1interaction2part1
    # elif emilyphase1interaction2 == 2 and whereami == "schoolhallway":
    #     hide screen uppergui
    #     if timeofday == "Day":
    #         jump emilyphase1interaction2part2
    #     else:
    #         jump emilyrunsaway
    # elif emilyphase1interaction2 == 3 and whereami != "schoolhallway":
    #     player "No reason to call her until I have the paint."
    #     jump returnwhereyouare
    # elif emilyphase1interaction2 == 3 and whereami == "schoolhallway":
    #     scene fs schoolhallway2extras
    #     hide screen emily_atschool
    #     player "No point in talking to her right now, I should find some paint first."
    #     jump returnwhereyouare
    # elif emilyphase1interaction2 == 4 and whereami != "livingRoom" and whereami != "playerRoom":
    #
    #
    #     if whereami == "playerRoom" and timeofday == "Morning":
    #         scene fs playerroomMorn
    #     elif whereami == "playerRoom" and timeofday == "Day":
    #         scene fs playerroomDay
    #     elif whereami == "playerRoom" and timeofday == "Night":
    #         scene fs playerroomNight
    #     elif whereami == "livingRoom":
    #         if timeofday == "Night":
    #             scene fs livingroomnight
    #         else:
    #             scene fs livingroom
    #     elif whereami == "overworldmap" and timeofday == "Night":
    #         scene fs overworldnight
    #     elif whereami == "overworldmap":
    #         scene fs overworld
    #     elif whereami == "gym":
    #         scene fs gym
    #     elif whereami == "library":
    #         hide screen charlotte_library
    #         scene fs library
    #     elif whereami == "arcade":
    #         scene fs arcade
    #     elif whereami == "gfhouse":
    #         scene fs gfhouse
    #     elif whereami == "miashallway":
    #         scene fs gfhousehallway
    #     elif whereami == "gfroom":
    #         scene fs gfroom
    #     elif whereami == "sophiahouse":
    #         scene fs sophiahouse
    #     elif whereami == "school":
    #         hide screen ava_atschool
    #         scene fs schoolhallway
    #     elif whereami == "schoolhallway":
    #         hide screen emily_atschool
    #         scene fs schoolhallway2
    #     elif whereami == "classroom1":
    #         hide screen mia_atschool
    #         hide screen sophia_atschool
    #         hide screen mia_sophia_atschool
    #         scene fs classroom
    #     elif whereami == "classroom2":
    #         hide screen olivia_atschool
    #         scene fs classroom
    #     elif whereami == "classroom3":
    #         hide screen charlotte_school
    #         hide screen backbuttonCLASSROOM
    #         scene fs classroom3
    #     elif whereami == "mall":
    #         scene fs malllabel
    #     player "I'll call her from my place. I want her to get used to being there."
    #     jump returnwhereyouare
    # elif emilyphase1interaction2 == 4 and (whereami == "livingRoom" or whereami == "playerRoom") and timeofday != "Night":
    #     jump emilyphase1interaction2part3
    #
    # elif emilyphase1interaction2 == 4 and (whereami == "livingRoom" or whereami == "playerRoom") and timeofday == "Night":
    #     hide screen phonecontacts
    #     hide screen contacts
    #     hide screen backbuttonROOM
    #     hide screen backbuttonLIVINGROOM
    #     player "I think I'll call her during the day, atmosphere might be better."
    #     player "Don't want her getting any hints about my intentions just yet."
    #     jump returnwhereyouare
    # elif emilyphase1interaction2 == 5 and whereami == "schoolhallway" and timeofday != "Night":
    #     jump emilyphase1interaction2part4
    # elif emilyphase1interaction2 == 5:
    #     hide screen uppergui
    #     hide screen contacts
    #     hide screen phonecontacts
    #     player "I don't want to text Emily just yet, I'll talk to her at the school in person."
    #     jump returnwhereyouare
    # elif emilyphase1interaction2 == 6:
    #     if whereami == "schoolhallway":
    #         scene fs schoolhallway2
    #     player "She probably wants to make the finishing touches on the banner, I'll see her at the track meet."
    #     jump returnwhereyouare

label stephaniePivot:
    
    if currentchapter >= 2 and timeofday != "Night" and whereami == "sunnysidemap" and stephaniedaychecker != dayNumber and stephaniescene1 == 2:
        jump stephaniescene1part3
    elif currentchapter >= 2 and timeofday != "Night" and whereami == "sunnysidemap" and stephaniedaychecker != dayNumber:
        jump stephaniescene1part2
    else:
        "..."
        "Nobody's Home"
        jump gotosunnyside

label melissaPivot:
    if melissascene1 == 0:
        jump melissadancescene
    else:
        jump overworldmap

label ravenPivot:
    if ravenscene1 == 0:
        jump raventattooscene
    elif ravenscene1 == 1 and timeofday == "Night":
        jump ravenbjscene


label miaPivot:
    #"[miaphase1interaction1],[miaphase1interaction2],[miaphase1interaction3],[miaphase2interaction1]"
    #"[charlottephase1interaction1], [charlottephase1interaction2],[charlottephase1interaction3]"
    hide screen uppergui
    hide screen phonecontacts
    hide screen contacts
    #location doesn't matter nor does timeofday-------
    if charlottephase1interaction2 == 2:
        if whereami == "classroom1" and timeofday == "Morning":
            jump charlottephaseMiaDelegation
        else:
            player "I should talk to her in person about Charlotte."
            jump returnwhereyouare

    if miaphase1interaction1 == 3:
        if timeofday != "Night" or whereami != "playerRoom" or miaroutecurrentday == dayNumber:
            hide screen backbuttonROOM
            hide screen sophia_atschool
            player "She already sent me a selfie, I should text her again from my room at night."
            jump returnwhereyouare
    elif miaphase1interaction1 == 1:
        player "Mia wants me to visit her home in the afternoon."
        jump returnwhereyouare

    if miaphase1interaction3 == 4:
        hide screen phonecontacts
        hide screen contacts
        player "Can't wait to call Mia and tell her I found her phone."
        player "....."
        player "Huh? Why is my pocket vibra-oh my god I’m so stupid."
        jump returnwhereyouare

    if miaphase1interaction3 == 5:
        if currentchapter > 1:
            $ miaphase1interaction3 = 6
            jump miaPivot
        hide screen phonecontacts
        hide screen contacts
        "Mia isn't picking up her phone, she must be busy."
        jump returnwhereyouare

    if miaphase2interaction1 == 1 and miaphase1interaction3 == 6 and whereami != "gfroom":
        player "No need to text her, I'll just meet her in her room when I'm ready to go."
        jump returnwhereyouare

    
    if miaphase2interaction2 >= 4 and katiephase2interaction1 == 4:
        hide screen uppergui
        hide screen questboxpreview
        hide screen locationname
        hide screen tosunnyside
        hide screen backbuttonSTORE
        hide hbashley current
        hide screen store_paint
        hide screen store_movie
        hide screen store_videogame
        hide screen store_candy
        hide screen store_watch
        hide screen store_Ashley
        hide screen store_camera
        hide screen backbuttonROOM
        hide screen backbuttonLIVINGROOM
        hide screen backbuttonCLASSROOM
        hide screen backbuttonGFROOM
        hide screen backbuttonGFHALLWAY
        hide screen backbuttonMALL
        hide screen backbuttonGYM
        hide screen backbuttonSOPHIAOUTSIDE
        hide screen backbuttonGYMOUTSIDE
        hide screen backbuttonOUTSIDEOFFICE
        hide screen backbuttonCLUB
        hide screen backbuttonCLUBRESTROOM
        hide screen tosunnyside

        jump talkaboutpizzaparty

    

    if whereami != "classroom1" and miaphase2interaction1 == 2:
        mia "Hey! I'm busy come talk to me at my school!"
        jump returnwhereyouare

    if whereami != "livingRoom" and miaphase2interaction2 == 3:
        player "I should call her from my livingroom at night."
        jump returnwhereyouare

#-------------------------------------------------------------------------------


    #Location matters---------------------------------
    if whereami == "classroom1":
        if timeofday == "Morning":
            if charlottephase1interaction2 == 2:
                jump charlottephaseMiaDelegation
            if miaphase1interaction1 == 0:
                jump miaphase1interaction1part1
            elif miaphase1interaction1 == 1:
                hide screen mia_atschool
                jump miaphase1interaction1part1postconvo
            elif miaphase1interaction1 == 2:
                hide screen sophia_atschool
                player "I should text Mia at night in my room so I can uh...be alone."
                jump returnwhereyouare
            elif miaphase1interaction1 == 3:
                hide screen sophia_atschool
                player "{i}She's getting ready for class I should text her to come over during the night in my room.{/i}"
                jump returnwhereyouare
            elif miaphase1interaction1 == 4:
                hide screen mia_atschool
                hide screen sophia_atschool
                $ miaSprite = 1
                show fbmia current:
                    xalign 0.5 ypos 120
                with Dissolve(0.5)
                mia "Busy right now sorry! Come over again during the afternoon."
                player "Okay no problem."
                $ miaSprite = 0
                jump returnwhereyouare

            if miaphase1interaction2 == 2:
                hide screen sophia_atschool
                player "Mia looks busy, I'll just contact her from my place again tonight."
                jump returnwhereyouare

            if miaphase1interaction3 == 1:
                jump miaphase1interaction3part1
            elif miaphase1interaction3 == 2:
                jump miaphase1interaction3part1postconvo
            if miaphase2interaction2 == 1:
                hide screen sophia_atschool
                hide screen mia_atschool
                jump miaphase2interaction2part1


    elif whereami == "playerRoom":
        hide screen backbuttonROOM
        #Time of day doesn't matter--------------------
        if miaphase1interaction1 == 4:
            hide screen phonecontacts
            hide screen contacts
            mia "{cps=25}Busy right now sorry! Come over again during the afternoon.{/cps}"
            player "{cps=25}Okay no problem.{/cps}"
            jump returnwhereyouare

        if miaphase1interaction3 == 1:
            "*Ring Ring*"
            player "Huh, no answer."
            jump returnwhereyouare
        elif miaphase1interaction3 == 2 or miaphase1interaction3 == 3:
            #"here?"
            player "{cps=25}Hey I know your class is starting soon sorry, but where did you visit again?{/cps}"
            mia "{cps=25}It was...the park for a walk, the mall for some shopping, stopped by the arcade to see Olivia. And the library to give charlotte her book back.{/cps}"
            jump returnwhereyouare


        #Time of day Matters--------------------

        if timeofday == "Morning":
            if miaphase1interaction1 == 0:
                player "Hey babe!"
                mia "Come visit me at school during the morning when you have time XD."
                call screen phonecontacts
            elif miaphase1interaction1 == 3:
                hide screen contacts
                player "{i}I should text her to come over in my room at night.{/i}"
                call screen phonecontacts
        if timeofday == "Day":
            if miaphase1interaction1 == 0:
                player "Hey babe!"
                mia "Come visit me at school during the morning when you have time XD."
                call screen phonecontacts
            elif miaphase1interaction1 == 3:
                hide screen contacts
                player "{i}I should text her to come over in my room at night.{/i}"
                call screen phonecontacts

        if timeofday == "Night":
            if miaphase1interaction1 == 0:
                player "Hey babe!"
                mia "Come visit me at school during the morning when you have time XD."
                call screen phonecontacts

            elif miaphase1interaction1 == 2:
                jump textmiafornudes
            elif miaphase1interaction1 == 3:
                    jump textmiatocomeover

            if miaphase1interaction2 == 2:
                jump miaphase1interaction2part3
        else:
            if miaphase1interaction2 == 2:
                player "I should text Mia to come over from my room tonight."
                jump returnwhereyouare



    elif whereami == "livingRoom":
        #"dowe get here? [miaphase1interaction1]"
        #Timeofday Doesn't matter----------------------
        if miaphase1interaction1 == 0:
            hide screen phone
            hide screen phonecontacts
            player "Hey babe!"
            mia "Come visit me at school during the morning when you have time XD."
            call screen phonecontacts
        elif miaphase1interaction1 == 1:
            if timeofday == "Night":
                player "Huh no answer, she must be sleeping."
            else:
                player "Huh no answer, maybe she's preparing for my visit in the afternoon."
            call screen phonecontacts
        elif miaphase1interaction1 == 2:
            hide screen backbuttonLIVINGROOM
            player "I should text Mia at night in my room so I can uh...be alone."
            call screen phonecontacts
        elif miaphase1interaction1 == 3:
            hide screen contacts
            player "{i}I should text her to come over in my room at night.{/i}"
            call screen phonecontacts
        elif miaphase1interaction1 == 4:
            hide screen mia_atschool
            hide screen sophia_atschool
            mia "Busy right now sorry! Come over again during the afternoon."
            player "Okay no problem."
            jump returnwhereyouare

        if miaphase1interaction3 == 1:
            "*Ring Ring*"
            player "Huh, no answer."
            jump returnwhereyouare
        elif miaphase1interaction3 == 2 or miaphase1interaction3 == 3:
            #"here2?"
            player "{cps=25}Hey I know your class is starting soon sorry, but where did you visit again?{/cps}"
            mia "{cps=25}It was...the park for a walk, the mall for some shopping, stopped by the arcade to see Olivia. And the library to give charlotte her book back.{/cps}"
            jump returnwhereyouare




        #Timeofday matters-----------------------------
        if timeofday == "Night":
            if miaphase1interaction2 == 2:
                jump miaphase1interaction2part3
            if miaphase2interaction2 == 5:
                jump miaphase2interaction3part1
        else:
            if miaphase1interaction2 == 2:
                player "I should text Mia to come over from my room tonight."
                jump returnwhereyouare



    elif whereami == "gfroom" and currentchapter > 1 and miaphase2interaction1 == 1:
        jump miaphase2interaction1part1


    else: #if you're NOT in the Classroom or your Bedroom or Livingroom
        if miaphase1interaction1 == 0:
            player "Hey babe!"
            mia "Come visit me at school during the morning when you have time XD."
            call screen phonecontacts
        elif miaphase1interaction1 == 1:
            if timeofday == "Night":
                player "Huh no answer, she must be sleeping."
            else:
                player "Huh no answer, maybe she's preparing for my visit in the afternoon."
            call screen phonecontacts
        elif miaphase1interaction1 == 2:
            player "I should text Mia at night in my room so I can uh...be alone."
            jump returnwhereyouare
        elif miaphase1interaction1 == 3:
            hide screen contacts
            player "{i}I should text her to come over in my room tonight.{/i}"
            call screen phonecontacts
        elif miaphase1interaction1 == 4:
            hide screen phonecontacts
            hide screen contacts
            mia "{cps=25}Busy right now sorry! Come over again during the afternoon.{/cps}"
            player "Okay no problem."
            jump returnwhereyouare

        if miaphase1interaction2 == 2:
            player "I should text Mia to come over from my room tonight."
            jump returnwhereyouare

        if miaphase1interaction3 == 1:
            "*Ring Ring*"
            player "Huh, no answer."
            jump returnwhereyouare
        if (miaphase1interaction3 == 2 or miaphase1interaction3 == 3) and  whereami == "classroom1":
            player "{cps=25}Hey I know your class is starting soon sorry, but where did you visit again?{/cps}"
            mia "{cps=25}It was...the park for a walk, the mall for some shopping, stopped by the arcade to see Olivia. And the library to give charlotte her book back.{/cps}"
            jump returnwhereyouare
        if miaphase1interaction3 == 2 or miaphase1interaction3 == 3:
            "*Ring Ring*"
            player "Huh, no answer."
            jump returnwhereyouare










    # if charlottephase1interaction2 == 2:
    #     jump charlottephaseMiaDelegation
    #
    # if miaphase2interaction1 == 1 and currentchapter == 2 and whereami == "gfroom":
    #     jump miaphase2interaction1part1
    #
    # if whereami == "playerRoom" and timeofday == "Morning":
    #     scene fs playerroomMorn
    # elif whereami == "playerRoom" and timeofday == "Day":
    #     scene fs playerroomDay
    # elif whereami == "playerRoom" and timeofday == "Night":
    #     scene fs playerroomNight
    # elif whereami == "livingRoom":
    #     if timeofday == "Night":
    #         scene fs livingroomnight
    #     else:
    #         scene fs livingroom
    # elif whereami == "overworldmap" and timeofday == "Night":
    #     scene fs overworldnight
    # elif whereami == "overworldmap":
    #     scene fs overworld
    # elif whereami == "gym":
    #     scene fs gym
    # elif whereami == "library":
    #     scene fs library
    # elif whereami == "arcade":
    #     scene fs arcade
    # elif whereami == "gfhouse":
    #     scene fs gfhouse
    # elif whereami == "miashallway":
    #     scene fs gfhousehallway
    # elif whereami == "sophiahouse":
    #     scene fs sophiahouse
    # elif whereami == "school":
    #     scene fs schoolhallway
    # elif whereami == "schoolhallway":
    #     scene fs schoolhallway2
    # elif whereami == "classroom1":
    #     hide screen mia_atschool
    #     hide screen sophia_atschool
    #     hide screen mia_sophia_atschool
    #     scene fs classroom
    # elif whereami == "mall":
    #     scene fs malllabel
    #
    # if miaphase1interaction3 == 1 and whereami != "classroom1":
    #
    #     if whereami == "playerRoom" and timeofday == "Morning":
    #         scene fs playerroomMorn
    #     elif whereami == "playerRoom" and timeofday == "Day":
    #         scene fs playerroomDay
    #     elif whereami == "playerRoom" and timeofday == "Night":
    #         scene fs playerroomNight
    #     elif whereami == "livingRoom":
    #         if timeofday == "Night":
    #             scene fs livingroomnight
    #         else:
    #             scene fs livingroom
    #     elif whereami == "overworldmap" and timeofday == "Night":
    #         scene fs overworldnight
    #     elif whereami == "overworldmap":
    #         scene fs overworld
    #     elif whereami == "gym":
    #         scene fs gym
    #     elif whereami == "library":
    #         scene fs library
    #     elif whereami == "arcade":
    #         scene fs arcade
    #     elif whereami == "gfhouse":
    #         scene fs gfhouse
    #     elif whereami == "miashallway":
    #         scene fs gfhousehallway
    #     elif whereami == "sophiahouse":
    #         scene fs sophiahouse
    #     elif whereami == "school":
    #         hide screen ava_atschool
    #         scene fs schoolhallway
    #     elif whereami == "schoolhallway":
    #         hide screen emily_atschool
    #         scene fs schoolhallway2
    #     elif whereami == "classroom1":
    #         hide screen mia_atschool
    #         hide screen sophia_atschool
    #         hide screen mia_sophia_atschool
    #         scene fs classroom
    #     elif whereami == "mall":
    #         scene fs malllabel
    #
    #     "*Ring Ring*"
    #     player "Huh, no answer."
    #     jump returnwhereyouare
    #
    # elif miaphase1interaction3 == 1 and whereami == "classroom1":
    #
    #     scene fs classroomZOOM
    #     with Dissolve(0.5)
    #     jump miaphase1interaction3part1
    #
    # elif miaphase1interaction3 == 2 and whereami == "classroom1":
    #     hide screen mia_atschool
    #     scene fs classroomZOOM
    #     with Dissolve(0.5)
    #     jump miaphase1interaction3part1postconvo
    # elif miaphase1interaction3 == 2:
    #     if whereami == "playerRoom" and timeofday == "Morning":
    #         scene fs playerroomMorn
    #     elif whereami == "playerRoom" and timeofday == "Day":
    #         scene fs playerroomDay
    #     elif whereami == "playerRoom" and timeofday == "Night":
    #         scene fs playerroomNight
    #     elif whereami == "livingRoom":
    #         if timeofday == "Night":
    #             scene fs livingroomnight
    #         else:
    #             scene fs livingroom
    #     elif whereami == "overworldmap" and timeofday == "Night":
    #         scene fs overworldnight
    #     elif whereami == "overworldmap":
    #         scene fs overworld
    #     elif whereami == "gym":
    #         scene fs gym
    #     elif whereami == "library":
    #         hide screen charlotte_library
    #         scene fs library
    #     elif whereami == "arcade":
    #         scene fs arcade
    #     elif whereami == "gfhouse":
    #         scene fs gfhouse
    #     elif whereami == "miashallway":
    #         scene fs gfhousehallway
    #     elif whereami == "gfroom":
    #         scene fs gfroom
    #     elif whereami == "sophiahouse":
    #         scene fs sophiahouse
    #     elif whereami == "school":
    #         hide screen ava_atschool
    #         scene fs schoolhallway
    #     elif whereami == "schoolhallway":
    #         hide screen emily_atschool
    #         scene fs schoolhallway2
    #     elif whereami == "classroom1":
    #         hide screen mia_atschool
    #         hide screen sophia_atschool
    #         hide screen mia_sophia_atschool
    #         scene fs classroom
    #     elif whereami == "classroom2":
    #         hide screen olivia_atschool
    #         scene fs classroom
    #     elif whereami == "classroom3":
    #         hide screen charlotte_school
    #         hide screen backbuttonCLASSROOM
    #         scene fs classroom3
    #     elif whereami == "mall":
    #         scene fs malllabel
    #
    #     player "{cps=25}Hey I know your class is starting soon sorry, but where did you visit again?{/cps}"
    #     mia "{cps=25}It was...the park for a walk, the mall for some shopping, stopped by the arcade to see Olivia. And the library to give charlotte her book back.{/cps}"
    #     jump returnwhereyouare
    #
    #
    # elif miaphase1interaction3 == 4:
    #     if whereami == "playerRoom" and timeofday == "Morning":
    #         hide screen backbuttonROOM
    #         scene fs playerroomMorn
    #     elif whereami == "playerRoom" and timeofday == "Day":
    #         hide screen backbuttonROOM
    #         scene fs playerroomDay
    #     elif whereami == "playerRoom" and timeofday == "Night":
    #         hide screen backbuttonROOM
    #         scene fs playerroomNight
    #     elif whereami == "livingRoom":
    #         if timeofday == "Night":
    #             scene fs livingroomnight
    #         else:
    #             scene fs livingroom
    #     elif whereami == "overworldmap" and timeofday == "Night":
    #         scene fs overworldnight
    #     elif whereami == "overworldmap":
    #         scene fs overworld
    #     elif whereami == "gym":
    #         hide screen backbuttonGYM
    #         scene fs gymarea
    #     elif whereami == "library":
    #         scene fs library
    #     elif whereami == "arcade":
    #         scene fs arcade
    #     elif whereami == "gfhouse":
    #         scene fs gfhouse
    #     elif whereami == "miashallway":
    #         scene fs gfhousehallway
    #     elif whereami == "gfroom":
    #         scene fs gfroom
    #     elif whereami == "sophiahouse":
    #         scene fs sophiahouse
    #     elif whereami == "school":
    #         hide screen ava_atschool
    #         scene fs schoolhallway
    #     elif whereami == "schoolhallway":
    #         hide screen emily_atschool
    #         scene fs schoolhallway2
    #     elif whereami == "classroom1":
    #         scene fs classroom
    #     elif whereami == "mall":
    #         hide screen backbuttonMALL
    #         scene fs mall
    #     elif whereami == "park" and timeofday == "Night":
    #         scene fs parknight
    #     elif whereami == "park":
    #         scene fs park
    #
    #     player "Can't wait to call Mia and tell her I found her phone."
    #     player "....."
    #     player "Huh? Why is my pocket vibra-oh my god I’m so stupid."
    #     jump returnwhereyouare
    #
    # if miaphase1interaction2 == 2:
    #     if timeofday == "Night" and (whereami == "livingRoom" or whereami == "playerRoom"):
    #         hide screen contacts
    #         jump miaphase1interaction2part3
    #     else:
    #         player "I should text Mia to come over from my room tonight."
    #         jump returnwhereyouare
    #
    # if miaphase1interaction1 == 0 and whereami == "classroom1":
    #     hide screen mia_atschool
    #     scene fs classroomZOOM
    #     with Dissolve(0.5)
    #     jump miaphase1interaction1part1
    #
    # elif miaphase1interaction1 == 0:
    #     hide screen contacts
    #     if whereami == "mall":
    #         hide screen backbuttonMALL
    #         scene fs mall
    #     elif whereami == "classroom1":
    #         scene fs classroom
    #     elif whereami == "classroom2":
    #         hide screen olivia_atschool
    #         scene fs classroom
    #     elif whereami == "classroom3":
    #         hide screen charlotte_school
    #         hide screen backbuttonCLASSROOM
    #         scene fs classroom3
    #     elif whereami == "schoolhallway":
    #         hide screen emily_atschool
    #         scene fs schoolhallway2
    #     elif whereami == "school":
    #         scene fs schoolhallway
    #         hide screen ava_atschool
    #     elif whereami == "arcade":
    #         scene fs arcade
    #     elif whereami == "sophiahouse":
    #         hide screen backbuttonSOPHIAOUTSIDE
    #         scene fs sophiahouseoutside
    #     elif whereami == "gfhouse":
    #         scene fs gfhouse
    #     elif whereami == "miashallway":
    #         scene fs gfhousehallway
    #     elif whereami == "gfroom":
    #         scene fs gfroom
    #     elif whereami == "library":
    #         scene fs library
    #     elif whereami == "gym":
    #         scene fs gymarea
    #     elif whereami == "outsidegym":
    #         scene fs outsidegym
    #     elif whereami == "overworldmap":
    #         if timeofday != "Night":
    #             scene fs overworld
    #         else:
    #             scene fs overworldnight
    #     elif whereami == "livingRoom":
    #         hide screen backbuttonLIVINGROOM
    #         if timeofday == "Night":
    #             scene fs livingroomnight
    #         else:
    #             scene fs livingroom
    #     elif whereami == "playerRoom":
    #         hide screen backbuttonROOM
    #         if timeofday == "Night":
    #             scene fs playerroomNight
    #         else:
    #             scene fs playerroomDay
    #     player "Hey babe!"
    #     mia "Come visit me at school during the morning when you have time XD."
    #     jump deactivatephone
    #
    # elif miaphase1interaction1 == 1 and whereami != "classroom1":
    #     hide screen contacts
    #     if whereami == "mall":
    #         scene fs mall
    #     elif whereami == "classroom1":
    #         scene fs classroom
    #     elif whereami == "classroom2":
    #         hide screen olivia_atschool
    #         scene fs classroom
    #     elif whereami == "classroom3":
    #         hide screen charlotte_school
    #         hide screen backbuttonCLASSROOM
    #         scene fs classroom3
    #     elif whereami == "schoolhallway":
    #         hide screen emily_atschool
    #         scene fs schoolhallway2
    #     elif whereami == "school":
    #         scene fs schoolhallway
    #         hide screen ava_atschool
    #     elif whereami == "arcade":
    #         scene fs arcade
    #     elif whereami == "sophiahouse":
    #         scene fs sophiahouse
    #     elif whereami == "gfhouse":
    #         scene fs gfhouse
    #     elif whereami == "miashallway":
    #         scene fs gfhousehallway
    #     elif whereami == "gfroom":
    #         scene fs gfroom
    #     elif whereami == "library":
    #         scene fs library
    #     elif whereami == "gym":
    #         scene fs gymarea
    #     elif whereami == "outsidegym":
    #         scene fs outsidegym
    #     elif whereami == "overworldmap":
    #         if timeofday != "Night":
    #             scene fs overworld
    #         else:
    #             scene fs overworldnight
    #     elif whereami == "livingRoom":
    #         if timeofday == "Night":
    #             scene fs livingroomnight
    #         else:
    #             scene fs livingroom
    #     elif whereami == "playerRoom":
    #         if timeofday == "Morning":
    #             scene fs playerroomMorn
    #         elif timeofday == "Day":
    #             scene fs playerroomDay
    #         elif timeofday == "Night":
    #             scene fs playerroomNight
    #
    #     player "Huh no answer, maybe she's preparing for my visit in the afternoon."
    #
    #     jump deactivatephone
    #
    # elif miaphase1interaction1 == 1 and timeofday == "Night":
    #     player "Huh no answer, she must be sleeping."
    #
    #     jump deactivatephone
    #
    # elif miaphase1interaction1 == 1:
    #     hide screen mia_atschool
    #     scene fs classroomZOOM
    #     with Dissolve(0.5)
    #     jump miaphase1interaction1part1postconvo
    #
    # elif miaphase1interaction1 == 2:
    #     if whereami == "mall":
    #         scene fs mall
    #     elif whereami == "classroom1":
    #         scene fs classroom
    #     elif whereami == "classroom2":
    #         scene fs classroom3
    #     elif whereami == "schoolhallway":
    #         scene fs schoolhallway2
    #     elif whereami == "school":
    #         scene fs schoolhallway
    #     elif whereami == "arcade":
    #         scene fs arcade
    #     elif whereami == "sophiahouse":
    #         scene fs sophiahouse
    #     elif whereami == "gfhouse":
    #         scene fs gfhouse
    #     elif whereami == "miashallway":
    #         scene fs gfhousehallway
    #     elif whereami == "gfroom":
    #         scene fs gfroom
    #     elif whereami == "library":
    #         scene fs library
    #     elif whereami == "gym":
    #         scene fs gymarea
    #     elif whereami == "outsidegym":
    #         scene fs outsidegym
    #     elif whereami == "overworldmap":
    #         if timeofday != "Night":
    #             scene fs overworld
    #         else:
    #             scene fs overworldnight
    #     elif whereami == "livingRoom":
    #         if timeofday == "Night":
    #             scene fs livingroomnight
    #         else:
    #             scene fs livingroom
    #     elif whereami == "playerRoom":
    #         scene fs playerRoom
    #
    #     if whereami == "playerRoom" and timeofday == "Night":
    #         $ todayis = dayName
    #         hide screen contacts
    #         jump textmiafornudes
    #     else:
    #         player "I should text Mia at night in my room so I can uh...be alone."
    #         jump returnwhereyouare
    #
    # elif miaphase1interaction1 == 3:
    #     if todayis != dayName and whereami == "playerRoom" and timeofday == "Night":
    #         hide screen contacts
    #         jump textmiatocomeover
    #     else:
    #
    #         hide screen contacts
    #         if whereami == "mall":
    #             scene fs mall
    #         elif whereami == "classroom1":
    #             scene fs classroom
    #         elif whereami == "classroom2":
    #             hide screen olivia_atschool
    #             scene fs classroom
    #         elif whereami == "classroom3":
    #             hide screen charlotte_school
    #             hide screen backbuttonCLASSROOM
    #             scene fs classroom3
    #         elif whereami == "schoolhallway":
    #             hide screen emily_atschool
    #             scene fs schoolhallway2
    #         elif whereami == "school":
    #             scene fs schoolhallway
    #             hide screen ava_atschool
    #         elif whereami == "arcade":
    #             scene fs arcade
    #         elif whereami == "sophiahouse":
    #             scene fs sophiahouse
    #         elif whereami == "gfhouse":
    #             scene fs gfhouse
    #         elif whereami == "miashallway":
    #             scene fs gfhousehallway
    #         elif whereami == "gfroom":
    #             scene fs gfroom
    #         elif whereami == "library":
    #             scene fs library
    #         elif whereami == "gym":
    #             scene fs gymarea
    #         elif whereami == "outsidegym":
    #             scene fs outsidegym
    #         elif whereami == "overworldmap":
    #             if timeofday != "Night":
    #                 scene fs overworld
    #             else:
    #                 scene fs overworldnight
    #         elif whereami == "livingRoom":
    #             if timeofday == "Night":
    #                 hide screen backbuttonLIVINGROOM
    #                 scene fs livingroomnight
    #             else:
    #                 hide screen backbuttonLIVINGROOM
    #                 scene fs livingroom
    #         elif whereami == "playerRoom":
    #             hide screen backbuttonROOM
    #             if timeofday == "Night":
    #                 scene fs playerroomNight
    #             else:
    #                 scene fs playerroomDay
    #
    #         if timeofday == "Night":
    #             player "{i}I should text her to come over in my room.{/i}"
    #         else:
    #             player "{i}She's getting ready for class I should text her to come over during the night in my room.{/i}"
    #         jump returnwhereyouare
    #
    # elif miaphase1interaction1 == 4:
    #     hide screen phonecontacts
    #     hide screen contacts
    #     mia "Busy right now sorry! Come over again during the afternoon."
    #     player "Okay no problem."
    #     jump returnwhereyouare
    #
    # elif miaphase1interaction3 == 5:
    #     hide screen phonecontacts
    #     hide screen contacts
    #     "Mia isn't picking up her phone, she must be busy."
    #     jump returnwhereyouare


label oliviaPivot:
    if oliviaphase3interaction1 == 1:
        hide screen olivia_atschool
        "I should go to her house in the afternoon to hang out"
        jump returnwhereyouare
    if timeofday == "Morning" and oliviaphase2interaction3 == 1 and currentchapter >=3 and whereami == "classroom2":
        jump oliviaphase3interaction1part1
        
    elif oliviaphase2interaction3 == 1 and currentchapter >=3 and whereami != "classroom2":
        hide screen contacts
        hide screen phonecontacts
        hide screen uppergui
        hide screen questboxpreview
        olivia "{cps=25}Sup?{/cps}"
        player "{cps=25}Nothing really, just wanted to see you.{/cps}"
        olivia "{cps=25}Aww me too, come find me before class starts{/cps}"
        jump returnwhereyouare

    if oliviaphase2interaction1 == 2 and whereami != "classroom2":
        hide screen contacts
        hide screen phonecontacts
        hide screen uppergui
        hide screen questboxpreview
        olivia "{cps=25}Sup?{/cps}"
        player "{cps=25}Nothing really, just wanted to see you.{/cps}"
        olivia "{cps=25}Aww me too, come find me before class starts{/cps}"
        jump returnwhereyouare
    elif oliviaphase2interaction1 == 2 and oliviaphase2interaction2 == 0 and whereami == "classroom2":
        jump oliviaphase2interaction2part1
    elif oliviaphase2interaction1 == 1:
        hide screen contacts
        hide screen phonecontacts
        player "I'm meeting Olivia at her apartment tonight in Sunnyside"
        jump returnwhereyouare
    if whereami == "classroom2" and oliviaphase1interaction1 == 0:
        jump oliviaphase1interaction1part1
    elif whereami == "classroom2" and oliviaphase1interaction1 == 1:
        jump oliviameetmeatarcade
    elif whereami == "classroom2" and timeofday == "Morning" and oliviaphase1interaction1 == 2:
        jump oliviameetmeatarcade
    elif whereami == "classroom2" and timeofday == "Morning" and oliviaphase1interaction1 == 3:
        jump oliviaphase1interaction2part1
    elif whereami == "classroom2" and timeofday == "Morning" and oliviaphase1interaction1 == 4 and oliviaphase1interaction2 == 1:
        jump oliviaisinclass
    elif whereami == "classroom2" and oliviaphase1interaction2 == 3:
        scene fs classroom
        player "I should go back and meet her in the arcade."
        player "The school has too many people around and I wanna keep this personal."
        jump returnwhereyouare
    elif whereami != "arcade" and oliviaphase1interaction2 == 2:
        player "I think I should give her the game at the arcade, looks like she's busy at the moment."
        jump returnwhereyouare
    elif (whereami != "livingRoom" and whereami != "playerRoom" and oliviaphase1interaction3 == 1) or (timeofday != "Night" and oliviaphase1interaction3 == 1):
        hide screen uppergui
        hide screen phonecontacts
        hide screen contacts
        player "Let's not disturb her right now. I'll call her from my place at night."
        jump returnwhereyouare
    elif (whereami == "livingRoom" or whereami == "playerRoom") and oliviaphase1interaction3 == 1 and timeofday == "Night":
        jump oliviaphase1interaction2part4
    elif oliviaphase1interaction3 == 2:
        player "{i}I have no reason to call her right now.{/i}"
        hide screen phonecontacts
        hide screen contacts
        jump returnwhereyouare



label juliaPivot:
    hide screen uppergui
    if currentchapter >= 2 and juliachecker == 3:
        if miaphase2interaction1 >= 2:
            jump juliascene3
        else:
            hide screen julia_kitchen
            player "{i}I should go shopping with Mia, she's waiting for me.{/i}"
            jump gfhouse

    if miaphase1interaction1 < 2:
        jump overworldmap
    else:
        if miaphase1interaction1 >= 4:
            if miaphase1interaction2 == 0:
                jump miaphase1interaction2part1
            elif miaphase1interaction2 == 5:
                jump juliascene1
            else:
                jump miaphase1interaction2part1postconvo
        elif miaphase1interaction1 == 2:
            jump talkwithjulia
        elif miaphase1interaction1 == 3:
            jump miaisnthome


label sophiaPivot:
    #"[sophiaphase1interaction1],[sophiaphase1interaction2],[sophiaphase2interaction1]"

    if timeofday == "Morning" and sophiaphase2interaction3 == 2 and currentchapter >= 3:
        jump sophiaphase3interaction1part1

    if sophiaphase1interaction1 == 0:
        jump sophiaphase1interaction1part1
    elif sophiaphase1interaction1 == 1 and whereami == "classroom1":
        jump sophianottalkingtome
    elif sophiaphase1interaction1 == 2 and whereami == "classroom1": # unreachable i think
        jump sophiaphase1interaction1part4
    elif sophiaphase1interaction1 == 4:
        hide screen sophia_atschool
        $ sophiaphase1interaction2 = 0
        $ sophiaphase1interaction1 = 5
        jump sophiaphase1interaction2part1
    elif sophiaphase1interaction2 == 1 and whereami == "classroom1":
        jump cantwaitforvisitsophia

    if sophiaphase2interaction1 == 1 and whereami == "cafe" and timeofday == "Day":
        jump sophiaphase2interaction2part2
    elif sophiaphase2interaction1 == 2:
        if whereami == "cafe" and timeofday == "Day":
            player "I already had lunch with Sophia. I should just go home and call it a night."
            jump insidecafe
        elif (whereami == "livingRoom" or whereami == "playerRoom") and timeofday == "Night":
            jump sophiaphase2interaction3part1
    
    
    "Nothing left in chapter"
    jump returnwhereyouare





label katiePivot:
    hide screen uppergui
    hide screen backbuttonROOM
    hide screen contacts
    hide screen phonecontacts
    if whereami == "playerRoom" and timeofday == "Morning":
        scene fs playerroomMorn
    elif whereami == "playerRoom" and timeofday == "Day":
        scene fs playerroomDay
    elif whereami == "playerRoom" and timeofday == "Night":
        scene fs playerroomNight
    elif whereami == "livingRoom":
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
    elif whereami == "miashallway":
        scene fs gfhousehallway
    elif whereami == "gfroom":
        scene fs gfroom
    elif whereami == "sophiahouse":
        scene fs sophiahouse
    elif whereami == "school":
        hide screen ava_atschool
        scene fs schoolhallway
    elif whereami == "schoolhallway":
        hide screen emily_atschool
        scene fs schoolhallway2
    elif whereami == "classroom1":
        hide screen mia_atschool
        hide screen sophia_atschool
        hide screen mia_sophia_atschool
    elif whereami == "classroom3":
        hide screen charlotte_school
        scene fs classroom3
    elif whereami == "mall":
        scene fs malllabel


    if katieconversation == 0:
        $ katieconversation = 1
        jump conversationkatie1

    elif katieconversation == 1:
        jump conversationkatie2

    elif katieconversation == 2:
        jump conversationkatie3

    elif katieconversation == 3:
        jump conversationkatie4
    else:
        jump conversationkatie5



label charlottePivot:
    #"[charlottephase1interaction1],[charlottephase1interaction2]"

    hide screen uppergui
    #Not part of Charlotte's route
    if miaphase1interaction3 == 2 and whereami != "classroom3":
        jump looking4miaphone

    if miaphase1interaction3 == 3:
        jump looking4miaphonepostconvo



    #location matters
    if whereami == "classroom3":
        if timeofday == "Morning":
            hide screen charlotte_school
            hide screen backbuttonCLASSROOM

            if charlottephase2interaction3 == 3 and currentchapter == 3:
                jump charlottephase3interaction1part1

            if charlottephase1interaction1 == 0:
                jump charlottephase1interaction1part1
            elif charlottephase1interaction1 == 1:
                jump charlottewonttalktome
            elif charlottephase1interaction1 == 2:
                jump charlottewonttalktome
            elif charlottephase1interaction1 == 3:
                hide screen backbuttonCLASSROOM
                jump charlottephase1interaction2part1A
            elif charlottephase1interaction1 == 4:
                hide screen backbuttonCLASSROOM
                player "I don't think I can talk to her easily here, should meet her back at the library."
                jump returnwhereyouare


            if charlottephase1interaction2 == 2:
                player "I shouldn't talk to Charlotte until I've gotten Mia's help to deal with her."
                jump returnwhereyouare

    elif whereami == "library":
        if timeofday == "Day":
            if charlottephase1interaction1 == 1:
                jump charlottephase1interaction1part2
            elif charlottephase1interaction1 == 2:
                jump charlottephase1interaction1part3
            elif charlottephase1interaction1 == 3:
                hide screen charlotte_school
                hide screen backbuttonCLASSROOM
                player "Charlotte's pissed. I should talk to her in the morning in class so there's...witnesses."
                jump returnwhereyouare
            elif charlottephase1interaction1 == 4:
                jump charlottephase1interaction2part1
            elif charlottephase1interaction2 == 2:
                hide screen charlotte_library
                player "I shouldn't talk to Charlotte until I've gotten Mia's help to deal with her."
                jump returnwhereyouare

    elif whereami == "cafe":
        if timeofday != "Night":
            if charlottephase2interaction1 == 0:
                if currentchapter > 1:
                    jump charlottephase2interaction1part1
            if charlottephase2interaction2 == 3:
                if currentchapter > 1:
                    jump charlottephase2interaction2part2





    #location doens't matter


    if charlottephase1interaction2 == 1:
        hide screen charlotte_school
        hide screen backbuttonCLASSROOM
        player "Charlotte won't talk to me at school and the librarian won't let me near her in the library."
        player "I gotta visit the library with  {color=#3eab33}75{/color} dollars ready."
        jump returnwhereyouare










     # hide screen uppergui
     # if miaphase1interaction3 == 2 and whereami != "classroom3":
     #     jump looking4miaphone
     #
     # if miaphase1interaction3 == 3:
     #     jump looking4miaphonepostconvo
     #
     # if miaphase1interaction3 == 4 and whereami == "library" and foundphonevariable == 1:
     #     jump foundmiaphoneconvo
     #
     #
     #
     #
     # if charlottephase2interaction1 == 0 and currentchapter > 1 and whereami == "cafe" and timeofday != "Night":
     #     jump charlottephase2interaction1part1
     #
     #
     # if charlottephase1interaction1 == 0:
     #     jump charlottephase1interaction1part1
     # elif charlottephase1interaction1 == 1 and whereami == "classroom3" and timeofday == "Morning":
     #     jump charlottewonttalktome
     # elif charlottephase1interaction1 == 1 and whereami == "library" and timeofday == "Day":
     #     jump charlottephase1interaction1part2
     # elif charlottephase1interaction1 == 2 and whereami == "classroom3" and timeofday == "Morning":
     #     jump charlottewonttalktome
     # elif charlottephase1interaction1 == 2 and whereami == "library" and timeofday == "Day":
     #     jump charlottephase1interaction1part3
     # elif charlottephase1interaction1 == 3 and whereami == "classroom3" and timeofday == "Morning":
     #     hide screen backbuttonCLASSROOM
     #     hide screen charlotte_school
     #     jump charlottephase1interaction2part1A
     # elif charlottephase1interaction1 == 3 and whereami != "classroom3":
     #     hide screen charlotte_school
     #     hide screen backbuttonCLASSROOM
     #     player "Charlotte's pissed. I should talk to her in the morning in class so there's...witnesses."
     #     jump returnwhereyouare
     # elif charlottephase1interaction1 == 4 and whereami != "library":
     #     hide screen charlotte_school
     #     hide screen backbuttonCLASSROOM
     #     player "I don't think I can talk to her easily here, should meet her back at the library."
     #     jump returnwhereyouare
     # elif charlottephase1interaction1 == 4 and whereami == "library" and timeofday == "Day":
     #     jump charlottephase1interaction2part1
     # elif charlottephase1interaction2 == 1:
     #     player "Charlotte won't talk to me at school and the librarian won't let me near her in the library."
     #     player "I gotta visit the library with  {color=#3eab33}75{/color} dollars ready."
     #     jump returnwhereyouare
     # elif charlottephase1interaction2 == 2:
     #     "There's no more content for Charlotte currently sorry"
     #     jump returnwhereyouare




label victoriaPivot:
    if victoriascene1part1 == 0:
        jump victoriamakeout1
    elif victoriascene1part1 == 1:
        jump victoriamakeout2
    elif victoriascene1part1 == 2:
        jump victoriafirstsex
    else:
        jump overworldmap


#Defaults are here
default lightbox_image = ""

label patroncredits:
    "This is tier 1:"
    "A R"
    "AbsentArmy"
    "Alex Dodge"
    "Alex Tavarez"
    "Andrej26"
    "Anon"
    "Austin K"
    "Azula"
    "Bala Voine"
    "BeastlyPM"
    "Blubidiblub"
    "Bob Deca"
    "Boros"
    "Brian Shields"
    "Buster Blader"
    "C B"
    "Cas vH"
    "Catlady972"
    "Charles Styles"
    "Chris Woods"
    "Cody Cantrell"
    "Connor Speak"
    "Cosplay"
    "Craig Zlist"
    "crazyhamp"
    "cv"
    "Cyber"
    "Dacotah Gunderson"
    "Dan"
    "D'andre"
    "Daniel Young"
    "Danny Parray"
    "David Johnson"
    "David Turton"
    "DelloS"
    "der koplose"
    "DeRoxas"
    "dogface"
    "Emmanuel Wil-Jeff"
    "Enos Dirk"
    "Esteban Vasquez"
    "F4ll3nN1nj4"
    "Ferninater"
    "Fewtch"
    "FezDisturbed"
    "Gambargin"
    "Gauthier Kreilmann"
    "Gavas"
    "Gerrit"
    "Golden Phoenix"
    "Goldenhand"
    "ironkoolart"
    "Israel Quintanar"
    "Itayoro"
    "jack ryan"
    "Jack3246"
    "Jake Streets"
    "James Dean"
    "james trup"
    "Jason Baxter"
    "Jeff Ellicott"
    "jeroen verboom"
    "Jesus Rodriguez"
    "Joe Clifton"
    "Joe mama"
    "John"
    "John Donahoe"
    "John Emmanuel Chua"
    "John Hall"
    "Johnathan Ellis"
    "Johnny Boy"
    "Jordan Ficca"
    "Karan Verma"
    "Kevin Reese"
    "King Kupo"
    "kingliu"
    "KingOfSalt"
    "Kukli"
    "Lastrosade"
    "Lata Meomu"
    "Lauren"
    "Les Clark"
    "Levan Nemsadze"
    "Levone W."
    "lilTedo"
    "Litia Raine"
    "Lockpitz"
    "Lord Hercules"
    "Lyubomir Georgiev"
    "managerW"
    "Marcelo Eduardo"
    "Markof"
    "Mateo Leon Torres Fun"
    "Matt"
    "Merlin1967"
    "MGF"
    "MINIJD"
    "mspaintdrip"
    "Mylow Kay"
    "Naturebee"
    "NexFalx19"
    "Nick Whittington"
    "Nickolas Cain"
    "Nico Bats"
    "NotDave"
    "notsurewhattotypehere"
    "Oats"
    "Ob Nixillis"
    "OsmiumAlt"
    "Ozxecho"
    "Palmer"
    "Paul"
    "phoenixsbane"
    "piotr natan"
    "plpolakpl"
    "Quaxel"
    "Raife"
    "Randall"
    "Raspado"
    "Ravren"
    "Ricky"
    "Robo DaD"
    "rockyworld1"
    "Ryan Keever"
    "Ryan Wang"
    "Ryker Taylor"
    "Sacke"
    "Scott McDonald"
    "Shambles"
    "Shaquille Robinson"
    "SilentChaos"
    "Skayph"
    "Smittykinick"
    "Someone"
    "summer100"
    "SUOCREZ"
    "SwitchB1ade"
    "ther3algurl"
    "tjx34"
    "Toastersock"
    "Todor"
    "Totemzero"
    "Travis Brewer"
    "Tu "
    "Vidschi"
    "vinny8boberano"
    "Whyze"
    "Will M"
    "Wyatt Wooden"
    "Z.orxy"
    "Zachary Goldwater"
    "zack vitali"


label endgame:

# This ends the game.

return
