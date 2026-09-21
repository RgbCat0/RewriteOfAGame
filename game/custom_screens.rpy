# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#Screen Styles

style phonegui:
    xpadding 150
    top_padding 100
    xsize 406
    ysize 829
    xalign 0.5
    yalign 0.1
    #padding gui.frame_borders.padding
    background Frame("gui/items/bigboyphone.png", gui.frame_borders, tile=gui.frame_tile)

style imagegallerygui:
    xpadding 150
    top_padding 100
    xsize 406
    ysize 600
    xalign 0.5
    yalign 0.1
    padding gui.frame_borders.padding
    background Frame("gui/items/bigboyphone.png", gui.frame_borders, tile=gui.frame_tile)

style backpack:
    xpadding 240
    top_padding 410
    xsize 1000
    ysize 1100
    xalign 0.5
    yalign 0.5
    #padding gui.frame_borders.padding
    background Frame("gui/openbagBG.png", gui.frame_borders, tile=gui.frame_tile)

style questing:
    xpadding 380
    top_padding 150
    xsize 1500
    ysize 1100
    xalign 0.5
    yalign 0.5
    #padding gui.frame_borders.padding
    background Frame("gui/questboxBG.png", gui.frame_borders, tile=gui.frame_tile)

# Places
screen myRoom(fsbackground,backgroundhover):

    imagemap:
        ground fsbackground
        hover backgroundhover


        hotspot (530, 440, 220, 175) clicked Jump("gotowork")
        hotspot (940, 750, 990, 530) clicked Jump("gotosleep")
        hotspot (70, 322, 210, 160) clicked Jump("displaycalender")

screen mylivingroom(fsbackground,backgroundhover):

    imagemap:
        ground fsbackground
        hover backgroundhover

        hotspot (570, 300, 200, 490) clicked Jump("overworldmap")


screen overworld:

    #iamge buttons
    default is_reversed = False
    default lastplacehovered = "arcade"
    fixed:
        order_reverse is_reversed

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/libraryDay.png"
            hover "overworldmapParts/libraryDayHover.png"

            hovered SetScreenVariable("lastplacehovered", "library"), SetVariable("hovertext","Library")
            unhovered SetVariable("hovertext", "")

            action Jump("library")

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/schoolDayButton.png"
            hover "overworldmapParts/schoolDayButtonHover.png"

            hovered SetVariable("hovertext","School"), SetScreenVariable("lastplacehovered", "school")
            unhovered SetVariable("hovertext", "")

            action Jump("school")

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/gymDayButton.png"
            hover "overworldmapParts/gymDayButtonHover.png"

            hovered SetVariable("hovertext","Gym"), SetScreenVariable("lastplacehovered", "gym")
            unhovered SetVariable("hovertext", "")

            action Jump("outsidegym")



        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/miahouseDayButton.png"
            hover "overworldmapParts/miaHouseDayButtonHover.png"

            hovered SetVariable("hovertext","Mia's House"), SetScreenVariable("lastplacehovered", "gfhouse")
            unhovered SetVariable("hovertext", "")

            action Jump("gfhouse")


        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/parkDay.png"
            hover "overworldmapParts/parkDayHover.png"

            hovered SetVariable("hovertext","Park"), SetScreenVariable("lastplacehovered", "park")
            unhovered SetVariable("hovertext", "")

            action Jump("park")


        imagebutton:
            focus_mask True
            idle "overworldmapParts/yourhouseDay.png"
            hover "overworldmapParts/yourhouseDayHover.png"

            hovered SetVariable("hovertext","Home"), SetScreenVariable("lastplacehovered", "yourhouse")
            unhovered SetVariable("hovertext", "")

            action Jump("playerlivingroom")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/sophiahouseDay.png"
            hover "overworldmapParts/sophiahouseDayHover.png"

            hovered SetVariable("hovertext","Sophia's House"), SetScreenVariable("lastplacehovered", "sophiahouse")
            unhovered SetVariable("hovertext", "")

            action Jump("sophiahouse")

        imagebutton:

            focus_mask True
            idle "overworldmapParts/arcadeDay.png"
            hover "overworldmapParts/arcadeDayHover.png"

            hovered SetVariable("hovertext","Arcade"), SetScreenVariable("lastplacehovered", "arcade")
            unhovered SetVariable("hovertext", "")

            action Jump("arcade")

        imagebutton:

            focus_mask True
            idle "overworldmapParts/charlotteshouseDay.png"
            hover "overworldmapParts/charlotteshouseDayHover.png"

            hovered SetVariable("hovertext","Mansion"), SetScreenVariable("lastplacehovered", "charlotteshouse")
            unhovered SetVariable("hovertext", "")

            action Jump("charlotteshouse")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/mallDayButton.png"
            hover "overworldmapParts/mallDayButtonHover.png"

            hovered SetVariable("hovertext","The Mall"), SetScreenVariable("lastplacehovered", "mall")
            unhovered SetVariable("hovertext", "")

            action Jump("malllabel")


screen overworldnight:

    #iamge buttons
    default is_reversed = False
    fixed:
        order_reverse is_reversed
        imagebutton:
            focus_mask True
            idle "overworldmapParts/arcadeNight.png"
            hover "overworldmapParts/arcadeNightHover.png"

            hovered SetVariable("hovertext","Arcade"), SetScreenVariable("lastplacehovered", "arcade")
            unhovered SetVariable("hovertext", "")

            action Jump("arcade")

        imagebutton:

            focus_mask True
            idle "overworldmapParts/charlotteshouseNight.png"
            hover "overworldmapParts/charlotteshouseNightHover.png"

            hovered SetVariable("hovertext","Mansion"), SetScreenVariable("lastplacehovered", "charlotteshouse")
            unhovered SetVariable("hovertext", "")

            action Jump("charlotteshouse")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/yourhouseNight.png"
            hover "overworldmapParts/yourhouseNightHover.png"

            hovered SetVariable("hovertext","Home"), SetScreenVariable("lastplacehovered", "yourhouse")
            unhovered SetVariable("hovertext", "")

            action Jump("playerlivingroom")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/gymNight.png"
            hover "overworldmapParts/gymNightHover.png"

            hovered SetVariable("hovertext","Gym"), SetScreenVariable("lastplacehovered", "gym")
            unhovered SetVariable("hovertext", "")

            action Jump("outsidegym")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/mallNight.png"
            hover "overworldmapParts/mallNightHover.png"

            hovered SetVariable("hovertext","The Mall"), SetScreenVariable("lastplacehovered", "mall")
            unhovered SetVariable("hovertext", "")

            action Jump("malllabel")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/miahouseNight.png"
            hover "overworldmapParts/miaHouseNightHover.png"

            hovered SetVariable("hovertext","Mia's House"), SetScreenVariable("lastplacehovered", "gfhouse")
            unhovered SetVariable("hovertext", "")

            action Jump("gfhouse")


        imagebutton:
            focus_mask True
            idle "overworldmapParts/parkNight.png"
            hover "overworldmapParts/parkNightHover.png"

            hovered SetVariable("hovertext","Park"), SetScreenVariable("lastplacehovered", "park")
            unhovered SetVariable("hovertext", "")

            action Jump("park")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/schoolNight.png"
            hover "overworldmapParts/schoolNightHover.png"

            hovered SetVariable("hovertext","School"), SetScreenVariable("lastplacehovered", "school")
            unhovered SetVariable("hovertext", "")

            action Jump("school")

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/sophiahouseNight.png"
            hover "overworldmapParts/sophiahouseNightHover.png"

            hovered SetVariable("hovertext","Sophia's House"), SetScreenVariable("lastplacehovered", "sophiahouse")
            unhovered SetVariable("hovertext", "")

            action Jump("sophiahouse")

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/libraryNight.png"
            hover "overworldmapParts/libraryNightHover.png"

            hovered SetScreenVariable("lastplacehovered", "library"), SetVariable("hovertext","Library")
            unhovered SetVariable("hovertext", "")


            action Jump("library")

screen screen_sunnyside:

    #iamge buttons
    default is_reversed = False
    default lastplacehovered = "club"
    fixed:
        order_reverse is_reversed

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/cafeDay.png"
            hover "overworldmapParts/cafeDayHover.png"

            hovered SetScreenVariable("lastplacehovered", "cafe"), SetVariable("hovertext","Cafe")
            unhovered SetVariable("hovertext", "")

            action Jump("insidecafe")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/clubDay.png"
            hover "overworldmapParts/clubDayHover.png"

            hovered SetVariable("hovertext","Club"), SetScreenVariable("lastplacehovered", "club")
            unhovered SetVariable("hovertext", "")

            action Jump("insideclub")


        imagebutton:
            focus_mask True
            idle "overworldmapParts/sunnysideapartmentDay.png"
            hover "overworldmapParts/sunnysideapartmentDayHover.png"

            hovered SetVariable("hovertext","Apartment"), SetScreenVariable("lastplacehovered", "apartment")
            unhovered SetVariable("hovertext", "")

            action Jump("apartmentlobbymenu")

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/officeDay.png"
            hover "overworldmapParts/officeDayHover.png"

            hovered SetVariable("hovertext","Office Building"), SetScreenVariable("lastplacehovered", "office")
            unhovered SetVariable("hovertext", "")

            action Jump("outsideoffice")



        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/beachDay.png"
            hover "overworldmapParts/beachDayHover.png"

            hovered SetVariable("hovertext","Beach"), SetScreenVariable("lastplacehovered", "beach")
            unhovered SetVariable("hovertext", "")

            action Jump("beach")


screen screen_sunnysidenight:

    #iamge buttons
    default is_reversed = False
    default lastplacehovered = "club"
    fixed:
        order_reverse is_reversed

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/cafeNight.png"
            hover "overworldmapParts/cafeNightHover.png"

            hovered SetScreenVariable("lastplacehovered", "cafe"), SetVariable("hovertext","Cafe")
            unhovered SetVariable("hovertext", "")

            action Jump("insidecafe")

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/clubNight.png"
            hover "overworldmapParts/clubNightHover.png"

            hovered SetVariable("hovertext","Club"), SetScreenVariable("lastplacehovered", "club")
            unhovered SetVariable("hovertext", "")

            action Jump("insideclub")

        imagebutton:
            focus_mask True
            idle "overworldmapParts/sunnysideapartmentNight.png"
            hover "overworldmapParts/sunnysideapartmentNightHover.png"

            hovered SetVariable("hovertext","Apartment"), SetScreenVariable("lastplacehovered", "apartment")
            unhovered SetVariable("hovertext", "")

            action Jump("apartmentlobbymenu")


        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/officeNight.png"
            hover "overworldmapParts/officeNightHover.png"

            hovered SetVariable("hovertext","Office Building"), SetScreenVariable("lastplacehovered", "office")
            unhovered SetVariable("hovertext", "")

            action Jump("outsideoffice")

        imagebutton:
            #xalign 0.75 yalign 0.3
            focus_mask True
            idle "overworldmapParts/beachNight.png"
            hover "overworldmapParts/beachNightHover.png"

            hovered SetVariable("hovertext","Beach"), SetScreenVariable("lastplacehovered", "beach")
            unhovered SetVariable("hovertext", "")

            action Jump("beach")



screen mall:

    imagemap:
        ground "mall extras A.png"
        hover "mallhover.png"

        hotspot(710,360,350,525) clicked Jump("mallstore")
        #hotspot(100,230,160,150) clicked Jump("overworldmap")


screen shoptime:

    imagemap:
        ground "Supermarket counter.png"
        hover "Supermarket Counter.png"

screen arcade:

    imagemap:
        ground "arcade.png"
        hover "arcadeHover.png"

        hotspot(50,910,400,300) clicked Jump("overworldmap")




screen sophiahouse:

    imagemap:
        ground "gfhousemain.png"
        hover "gfhousemainHover.png"

        hotspot(1335,540,260,295) clicked Jump("gotooverworldfromgfhouse")


screen outsidesophiahouse:

    imagemap:
        ground "City_CG.png"
        hover "City_CG.png"

        #hotspot(1335,540,260,295) clicked Jump("gotooverworldfromgfhouse")

screen gym:

    imagemap:
        ground "gymmain.png"
        hover "gymmain.png"

screen gymAftertoon:

    imagemap:
        ground "gymmainafternoon.png"
        hover "gymmainafternoon.png"


screen gfhouse:

    imagemap:
        ground "gfhousemain.png"
        hover "gfhousemainHover.png"

        hotspot(1335,540,260,295) clicked Jump("gotooverworldfromgfhouse")
        hotspot(800,100,480,830) clicked Jump("miatopsteps")


screen miahallway:

    imagemap:
        ground "miahousecorridor.png"
        hover "miahousecorridor.png"


screen gfroom:

    imagemap:
        ground "gfroom.png"
        hover "gfroomHover.png"

        hotspot (30,900, 240,200) clicked Jump("gfhousehallway")

screen gfhousehallway:

    imagemap:
        ground "gfhousehallway.png"
        hover "gfhousehallwayHover.png"

        hotspot(550,0,260,550) clicked Jump("gfroom1")
        hotspot(1300,0,600,1080) clicked Jump("gfhouse")

#below are the doors for mia's hallway in her house
screen miasroomdoor:
    zorder 1
    imagebutton:
        focus_mask True

        idle "miasroomdoor.png"
        hover "miasroomdoorhover.png"

        action Jump("gfroom1")

screen katiesroomdoor:
    zorder 1
    imagebutton:
        focus_mask True

        idle "katiesroomdoor.png"
        hover "katiesroomdoorhover.png"

        action Jump("katiesroom")


screen library:

    imagemap:
        ground "library.png"
        hover "libraryhover.png"

        hotspot(535,450,150,230) clicked Jump("leavelibrary")

screen school:

    imagemap:
        ground "School corridor extras.png"
        hover "School_corridorHover.png"

        hotspot(50,250,90,100) clicked Jump("overworldmap")
        #hotspot(150,130,240,380) clicked Jump("classroom1")
        hotspot(1620,325,250,545) clicked Jump("classroom1")
        hotspot(520,90,775,800) clicked Jump("schoolhallway")
        hotspot(50,325, 250, 545) clicked Jump ("classroom3")

screen schoolhallway:

    imagemap:
        ground "extras BG1.png"
        hover "School corridor_2Hover.png"

        hotspot(170,300,120,80) clicked Jump("school")
        hotspot(640,470,120,275) clicked Jump("classroom2")



screen classroom1:

    imagemap:
        ground "classroom extras.png"
        hover "classroomHoverextras.png"

        hotspot(530,450,100,400) clicked Jump("school")

screen classroom1Day:

    imagemap:
        ground "classroom.png"
        hover "classroomHover.png"

        hotspot(530,450,100,400) clicked Jump("school")


screen classroom2:

    imagemap:
        ground "classroom.png"
        hover "classroomHover.png"

        hotspot(530,450,100,400) clicked Jump("schoolhallway")

screen classroom3:

    imagemap:
        ground "Classroom2 extras.png"


screen outsidethegym:

    imagemap:
        ground "Gym_2.png"
        hover "Gym_2 hover.png"

        hotspot(1050,400,150,400) clicked Jump("gym")
        hotspot(240,350,410,730) clicked Jump("avaphase1interaction1part3")

screen outsidetheoffice:

    imagemap:
        ground "outside_office.png"
        hover "outside_office.png"

screen outsidetheofficenight:

    imagemap:
        ground "outside_office_night.png"
        hover "outside_office_night.png"

screen inside_cafe:

    imagemap:
        ground "insidecafe.png"
        hover "insidecafe.png"

screen exit_cafe:
    zorder 1
    imagebutton:
        focus_mask True
        idle "cafeexit.png"
        hover "cafeexitHover.png"

        action Jump ("gotosunnyside")

screen inside_club_night:

    imagemap:
        ground "clubextras.png"
        hover "clubextras.png"

screen inside_club:

    imagemap:
        ground "insideclub.png"
        hover "insideclub.png"

screen clubrestroom:

    imagemap:
        ground "clubRestroom_1.png"
        hover "clubRestroom_1.png"

screen clubrestroomstall:
    zorder 1
    imagebutton:
        focus_mask True
        idle "clubRestroomDoor.png"
        hover "clubRestroomDoorHover.png"

        action Jump ("goinsidestall")



screen beach_screen:

    imagemap:
        ground "beachBG.png"
        hover "beachBG.png"

screen beach_screen_day:

    imagemap:
        ground "beachBG extras.png"
        hover "beachBG extras.png"

screen beach_screen_night:

    imagemap:
        ground "beachBGnight.png"
        hover "beachBGnight.png"

#Screens for puzzles/games-------------------------------

screen secondpuzzlegame:

    # A map as background.
    add "livingroom.png"

    # A drag group ensures that the detectives and the cities can be
    # dragged to each other.
    draggroup:

        # Our detectives.
        drag:
            drag_name "Piece1"
            child "Puzzles/2ndpuzzle1.png"
            droppable False
            xpos 800 ypos 100
        drag:
            drag_name "Piece2"
            child "Puzzles/2ndpuzzle2.png"
            droppable False
            xpos 100 ypos 100
        drag:
            drag_name "Piece3"
            child "Puzzles/2ndpuzzle3.png"
            droppable False
            xpos 300 ypos 900


        # The cities they can go to.
        drag:
            drag_name "input1"
            child "Puzzles/2ndpuzzle1.png"
            draggable False
        drag:
            drag_name "input2"
            child "Puzzles/2ndpuzzle2.png"
            draggable False
        drag:
            drag_name "input3"
            child "Puzzles/2ndpuzzle3.png"
            draggable False



screen puzzle_paper1:
    zorder 1
    imagebutton:
        focus_mask True
        idle "Puzzles/paperpuzzle1.png"
        hover "Puzzles/paperpuzzle1.png"

screen puzzle_paper2:

    imagebutton:
        focus_mask True
        idle "paperpuzzle2"
        hover "paperpuzzle2"

        action Jump("rotatepaper2")

screen puzzle_paper3:
    imagebutton:
        focus_mask True
        idle "Puzzles/paperpuzzle3.png"
        hover "Puzzles/paperpuzzle3.png"

screen puzzle_paper4:
    imagebutton:
        focus_mask True
        idle "Puzzles/paperpuzzle4.png"
        hover "Puzzles/paperpuzzle4.png"

screen puzzle_paper5:
    imagebutton:
        focus_mask True
        idle "Puzzles/paperpuzzle5.png"
        hover "Puzzles/paperpuzzle5.png"

screen puzzle_paper6:
    imagebutton:
        focus_mask True
        idle "Puzzles/paperpuzzle6.png"
        hover "Puzzles/paperpuzzle6.png"


# Buttons/character clickables---------------------------



screen gotoclubrestroom:
    zorder 1
    imagebutton:
        focus_mask True
        idle "clubextrasrestroom.png"
        hover "clubextrasrestroomhover.png"

        action Jump ("clubbathroom")

screen gotoclubrestroomDay:
    zorder 1
    imagebutton:
        focus_mask True
        idle "clubextrasrestroomDay.png"
        hover "clubextrasrestroomDayHover.png"

        action Jump ("clubbathroom")

screen officedoor:
    zorder 1
    imagebutton:
        focus_mask True
        idle "officedoor_button.png"
        hover "officedoor_buttonhover.png"

        action Jump("office")

screen questboxpreview:
    zorder 1
    imagebutton:
        focus_mask True
        idle "gui/questboxpreview.png"
        hover "gui/questboxpreviewhover.png"

        action Jump("viewquests")


screen backbuttonROOM:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("playerlivingroom")


screen backbuttonLIVINGROOM:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.8 yalign 0.9
        idle "returnButtonRight.png"
        hover "returnButtonRightHover.png"

        action Jump("playerRoom")

screen backbuttonCLASSROOM:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("school")

screen backbuttonGFROOM:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("miahousehallway")

screen backbuttonGFHALLWAY:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.92
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("miatopsteps")

screen backbuttonMALL:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("overworldmap")

screen backbuttonSTORE:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("malllabel")

screen backbuttonGYM:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("outsidegym")

screen backbuttonSOPHIAOUTSIDE:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("overworldmap")

screen backbuttonGYMOUTSIDE:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.05 yalign 0.1
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("overworldmap")

screen backbuttonOUTSIDEOFFICE:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.1 yalign 0.9
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("gotosunnyside")

screen backbuttonCLUB:

    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.9 yalign 0.9
        idle "returnButtonRight.png"
        hover "returnButtonRightHover.png"

        action Jump("gotosunnyside")

screen backbuttonCLUBRESTROOM:

    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.9 yalign 0.9
        idle "returnButtonRight.png"
        hover "returnButtonRightHover.png"

        action Jump("insideclub")

screen tosunnyside:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.9 yalign 0.9
        idle "returnButtonRight.png"
        hover "returnButtonRightHover.png"

        action Jump("gotosunnyside")

screen tonormalmap:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.05 yalign 0.7
        idle "returnButton.png"
        hover "returnButtonHover.png"

        action Jump("overworldmap")

## buttons for the girls at places
screen emily_atschool:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.7 yalign 0.6
        idle "butonemily_TR.png"
        hover "butonemily_TRhover.png"

        action Jump("emilyPivot")

screen emily_atlibrary:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.83 yalign 0.75
        idle "emilybutton.png"
        hover "emilybuttonHover.png"

        action Jump("emilyPivot")

screen melissa_club:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.4 yalign 0.75
        idle "melissabutton1.png"
        hover "melissabutton1hover.png"

        action Jump("melissaPivot")

screen raven_mall:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.2 yalign 0.9
        idle "ravenbuttonmall.png"
        hover "ravenbuttonmallhover.png"

        action Jump("ravenPivot")

screen ava_atschool:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.75 yalign 0.7
        idle "ava buttontr.png"
        hover "ava buttontr hover.png"

        action Jump("avaPivot")

screen ava_atschoolhallway:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.2 yalign 0.7
        idle "avabutton.png"
        hover "avabuttonhover.png"

        action Jump("avaPivot")

screen ava_atgym:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.7 yalign 0.7
        idle "ava BG alone.png"
        hover "ava BG alone hover.png"

        action Jump("avaPivot")

screen mia_atschool:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.6 yalign 0.3
        idle "miaclassroomButton.png"
        hover "miaclassroomButtonHover.png"

        action Jump("miaPivot")

screen mia_sophia_atschool:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.6 yalign 0.3
        idle "miasophiaclassroomButton.png"
        hover "miasophiaclassroomButtonHover.png"

        action Jump("miaPivot")

screen olivia_atschool:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.7 yalign 0.5
        idle "olivia class bg alone.png"
        hover "olivia class bg alone hover.png"

        action Jump("oliviaPivot")

screen sophia_atcafe:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.6 yalign 0.3
        idle "sophia cafe.png"
        hover "sophia cafe hover.png"

        action Jump("sophiaPivot")


screen sophia_atschool:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.6 yalign 0.3
        idle "sophiaclassroomButton.png"
        hover "sophiaclassroomButtonHover.png"

        action Jump("sophiaPivot")

screen julia_kitchen:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.22 yalign 0.75
        idle "juliabutton.png"
        hover "juliabuttonHover.png"

        action Jump("juliaPivot")

screen charlottemia_room:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.35 yalign 0.8
        idle "charlottemiabutton.png"
        hover "charlottemiabuttonHover.png"

        action Jump("charlottesmiaquiz")

screen mia_room:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.35 yalign 0.8
        idle "miaroombutton.png"
        hover "miaroombuttonhover.png"

        action Jump("miaPivot")

screen charlotte_library:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.5 yalign 0.5
        idle "charlotte_library.png"
        hover "charlotte_libraryhover.png"

        action Jump("charlottePivot")

screen charlotte_school:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.5 yalign 0.7
        idle "charlottebutton2.png"
        hover "charlottebutton2hover.png"

        action Jump("charlottePivot")

screen charlotte_atcafe:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.5 yalign 0.7
        idle "charlotte cafe.png"
        hover "charlotte cafe hover.png"

        action Jump("charlottePivot")

screen mia_phone:
    zorder 1
    imagebutton:
        xalign 0.55 yalign 0.78
        idle "miaphonebutton.png"
        hover "miaphonebuttonHover.png"

        action Jump("miaphase1interaction3part3")


#------GIRL BUTTONS FOR CHAPTER 2 ENDING-------------

screen charlotte_beach:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons charlotte.png"
        hover "beach buttons charlotte hover.png"

        action Jump("charlottebeachchapter2end")

screen olivia_beach:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons olivia.png"
        hover "beach buttons olivia hover.png"

        action Jump("oliviabeachchapter2end")

screen ava_beach:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons ava.png"
        hover "beach buttons ava hover.png"

        action Jump("avabeachchapter2end")

screen mia_beach1:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons mia1.png"
        hover "beach buttons mia1 hover.png"

        action Jump("miabeachchapter2end")

screen mia_beach2:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons mia2.png"
        hover "beach buttons mia2 hover.png"

        action Jump("miabeachchapter2end")

screen mia_beach3:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons mia3.png"
        hover "beach buttons mia3 hover.png"

        action Jump("miabeachchapter2end")

screen sophia_beach:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons sophia.png"
        hover "beach buttons sophia hover.png"

        action Jump("sophiabeachchapter2end")

screen emily_beach:
    zorder 1
    imagebutton:
        focus_mask True
        idle "beach buttons emily.png"
        hover "beach buttons emily hover.png"

        action Jump("emilybeachchapter2end")

screen backbuttonBEACH:

    zorder 1
    imagebutton:
        focus_mask True
        xalign 0.9 yalign 0.9
        idle "returnButtonRight.png"
        hover "returnButtonRightHover.png"

        action Jump("endofchapter2")
#------------------OBJECT SCREENS--------------------

screen gym_machine:
    zorder 1
    imagebutton:
        focus_mask True
        xalign 1.0 yalign 1.0
        idle "gymmachinebutton.png"
        hover "gymmachinebuttonhover.png"

        action Jump("machinePivot")







#screen guidisplayables(money, day):

screen locationname:
    zorder 2
    text "{font=gui/KentuckyFriedFont.ttf}{color=#dd3939}[hovertext]{/color}{/font}" size 120

screen uppergui:
    zorder 2

    hbox:
        xalign 0.85 ypos 0
        spacing 40

        vbox:
            yalign 0.2
            text "{color=#EA8400}{b}{size=30}[dayName]{/size}{/b}{/color}"

        if timeofday == "Morning":
            imagebutton:
                idle "gui/iconmorning.png"
        elif timeofday == "Day":
            imagebutton:
                idle "gui/iconday.png"
        else:
            imagebutton:
                idle "gui/iconnight.png"


        imagebutton:

            idle "phone.png"
            hover "phoneHover.png"

            action Jump("checkphone")#Jump("activatephone")


        imagebutton:
            idle "money.png"
            hover "moneyhover.png"

            action Jump("howmuchmoneydoihave")

        imagebutton:

            idle "gui/icon_bag.png"
            hover "gui/icon_bag_open.png"

            action Jump("useinventory")

    imagebutton:
        xalign 0.95
        idle "mapbutton.png"
        hover "mapbuttonHover.png"

        action Jump("overworldmap")


#i called it contacts but this is basically "phone" now
screen contacts:
    zorder 2
    modal True

    frame:
        style "phonegui"


        grid 2 1:
            spacing 50
            xalign 0.5
            yalign 0.1

            imagebutton:
                idle "gui/items/phonecontacts.png"
                hover "gui/items/phonecontactshover.png"

                action Show("phonecontacts")

            imagebutton:
                idle "gui/items/phoneimages.png"
                hover "gui/items/phoneimageshover.png"

                action Jump("gotopicturesfromphone")

    textbutton _("CLOSE"):
        xalign 0.5 ypos 700
        xfill False
        action Jump("deactivatephone")#[ Hide("contacts")]# Return(Null) #


screen phonecontacts:
    zorder 2
    modal True

    frame:
        style "phonegui"

        vbox:
            for person in contact_list:
                if person == "Mia":
                    textbutton "Mia":
                        action Jump("miaPivot")
                elif person == "Sophia":
                    textbutton "Sophia":
                        action Jump("sophiaPivot")
                elif person == "Katie":
                    textbutton "Katie":
                        action Jump("katiePivot")
                elif person == "Emily":
                    textbutton "Emily":
                        action Jump("emilyPivot")
                elif person == "Olivia":
                    textbutton "Olivia":
                        action Jump("oliviaPivot")

    textbutton _("Return"):
        xalign 0.5 ypos 700
        xfill False
        action Jump("gotophonefromcontacts")#[ Hide("contacts")]# Return(Null) #


screen gameGallery():
    zorder 2
    modal True


    if lightbox_image != "":
        frame:
            style "phonegui"

            imagebutton:
                idle "galleryimages/" + lightbox_image + ".png"
                hover "galleryimages/" + lightbox_image + ".png"
                xalign 0.5
                yalign 0.1
                focus_mask True
                action SetVariable("lightbox_image", "")


    else:
        frame:
            style "phonegui"


            vpgrid:

                rows len(phone_pictures)/2 + 1
                cols 2
                spacing 5
                draggable True
                mousewheel True
                xsize 600
                #xfill True
                ysize 565
                xpos -132

                #scrollbars "vertical"

                #side_xalign 1.0


                for q in phone_pictures:
                    $ qimage = "galleryimages/" + q + ".png"
                    $ Ib_image = im.Scale(qimage, 180, 220)
                    imagebutton:
                        idle Ib_image
                        hover Ib_image
                        action SetVariable("lightbox_image", q)

                for i in range(0, round((len(phone_pictures)/2 + 1) * 2) - (len(phone_pictures))):# i rounded the first number, be wary
                    null



        textbutton _("Return"):
            xalign 0.5 ypos 700
            xfill False
            action Jump("gotophonefromcontacts")


screen questbox():
    zorder 2
    modal True
    #draggable True
    #mousewheel True


    frame:
        style "questing"

        vpgrid:
            rows 15
            cols 2
            draggable True
            mousewheel True
            ysize 700
            xsize 750


            imagebutton:
                idle "gui/questboxMia.png"
                hover "gui/questboxMia.png"

            textbutton ("{color=#f2f03b}[miaquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[avaquesticon]"
                hover "[avaquesticon]"

            textbutton ("{color=#f2f03b}[avaquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[emilyquesticon]"
                hover "[emilyquesticon]"

            textbutton ("{color=#f2f03b}[emilyquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[sophiaquesticon]"
                hover "[sophiaquesticon]"

            textbutton ("{color=#f2f03b}[sophiaquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[oliviaquesticon]"
                hover "[oliviaquesticon]"

            textbutton ("{color=#f2f03b}[oliviaquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[charlottequesticon]"
                hover "[charlottequesticon]"

            textbutton ("{color=#f2f03b}[charlottequestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[katiequesticon]"
                hover "[katiequesticon]"

            textbutton ("{color=#f2f03b}[katiequestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[juliaquesticon]"
                hover "[juliaquesticon]"

            textbutton ("{color=#f2f03b}[juliaquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[victoriaquesticon]"
                hover "[victoriaquesticon]"

            textbutton ("{color=#f2f03b}[victoriaquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[josyquesticon]"
                hover "[josyquesticon]"

            textbutton ("{color=#f2f03b}[josyquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[cassandraquesticon]"
                hover "[cassandraquesticon]"

            textbutton ("{color=#f2f03b}[cassandraquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[pennyquesticon]"
                hover "[pennyquesticon]"

            textbutton ("{color=#f2f03b}[pennyquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[stephaniequesticon]"
                hover "[stephaniequesticon]"

            textbutton ("{color=#f2f03b}[stephaniequestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[ravenquesticon]"
                hover "[ravenquesticon]"

            textbutton ("{color=#f2f03b}[ravenquestlog]{/color}"):
                yalign 0.5
                xsize 500

            imagebutton:
                idle "[melissaquesticon]"
                hover "[melissaquesticon]"

            textbutton ("{color=#f2f03b}[melissaquestlog]{/color}"):
                yalign 0.5
                xsize 500




        #has side "c r b"

        # vpgrid:
        #
        #     rows len(item_list)/2 + 1
        #     cols 2
        #     spacing 50
        #     draggable True
        #     mousewheel True
        #     xalign 0.5
        #     #xsize 600
        #     #xfill True
        #     ysize 565
        #     #xpos -132
        #
        #     #yadjustment adj



        textbutton _("{font=gui/KentuckyFriedFont.ttf}{size=100}Exit{/size}{/font}"):
            xpos 250
            yalign 0.85
            xsize 200
            xfill True
            action Jump("returnwhereyouare")
            top_margin 10


screen inventory(item_list,adj):
    zorder 2
    modal True

    frame:
        style "backpack"

        #has side "c r b"

        vpgrid:

            rows len(item_list)/2 + 1
            cols 2
            spacing 50
            draggable True
            mousewheel True
            xalign 0.5
            #xsize 600
            #xfill True
            ysize 565
            #xpos -132

            #yadjustment adj

            for item in item_list:
                if item == "Paint":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/item_paintBag.png"
                        hover "ITEMS/item_painthoverBag.png"
                        action Jump("itspaint")
                elif item == "Movie":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/item_movieBag.png"
                        hover "ITEMS/item_moviehoverBag.png"
                        action Jump("itsmovie")
                elif item == "Video Game":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/item_videogameBag.png"
                        hover "ITEMS/item_videogamehoverBag.png"
                        action Jump("itsvideogame")
                elif item == "Candy":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/item_candyBag.png"
                        hover "ITEMS/item_candyhoverBag.png"
                        action Jump("itscandy")
                elif item == "HP-CheckWatch-3000":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/item_watchBag.png"
                        hover "ITEMS/item_watchhoverBag.png"
                        action Jump("itswatch")
                elif item == "Camera":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/M_camera.png"
                        hover "ITEMS/M_camerahover.png"
                        action Jump("itscamera")
                elif item == "Condoms":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/M_condom.png"
                        hover "ITEMS/M_condomhover.png"
                        action Jump("itscondom")
                elif item == "Handcuffs":
                    imagebutton:
                        focus_mask True
                        xysize(110,150)
                        idle "ITEMS/M_handcuffs.png"
                        hover "ITEMS/M_handcuffshover.png"
                        action Jump("itshandcuffs")


            for i in range(0, round((len(item_list)/2 + 1) * 2) - (len(item_list))):
                null



            # for item in item_list:
            #     if item == "Paint":
            #         textbutton "Paint":
            #             action Jump("itspaint")
            #     elif item == "Movie":
            #         textbutton "Movie":
            #             action Jump("itsmovie")
            #     elif item == "Video Game":
            #         textbutton "Video Game":
            #             action Jump("itsvideogame")
            #     elif item == "Candy":
            #         textbutton "Candy":
            #             action Jump("itscandy")
            #     elif item == "HP-CheckWatch-3000":
            #         textbutton "HP-CheckWatch-3000":
            #             action Jump("itswatch")


        #bar adjustment adj style "backpackscrollbar"

        textbutton _("Exit Inventory"):
            xpos 120
            yalign 0.9
            xfill True
            action Jump("returnwhereyouare")
            top_margin 10


screen patroncredits(adj):

    modal True

    frame:
        xsize 450
        xalign .5
        yalign .5
        ysize 800


        has side "c r b"

        viewport:
            yadjustment adj
            mousewheel True

            vbox:
               # style "patreon_text"

                null height 10
                text "Twentyfive Dollar Patrons"
                null height 5

                textbutton "Dal Vispu"
                textbutton "Joel"
                textbutton "Ahhhhhhhhhhh"
                textbutton "Joseph"
                textbutton "giodude2015"
                textbutton "bobby lewis"
                textbutton "Wade Bowen"
                textbutton "Aaron Webb"
                textbutton "Akadan"
                textbutton "Azazeres"
                textbutton "Blockyblob"
                textbutton "Bob Murray"
                textbutton "coupdetat"
                textbutton "Dal Vispu"
                textbutton "Demiurge"
                textbutton "ElysianReign"
                textbutton "greenarrow25"
                textbutton "Gribbitz"
                textbutton "J"
                textbutton "James Sullivan"
                textbutton "José Salas"
                textbutton "Matthew Malone"


                null height 10
                text "Ten Dollar Patrons"
                null height 5


                textbutton "å®¶ç¦Ž è¬"
                textbutton "Aaron Grandy"
                textbutton "Aegisjalmur"
                textbutton "Age of Empire 123"
                textbutton "Allen"
                textbutton "Anthony Evett-beadon"
                textbutton "andrew"
                textbutton "Ape"
                textbutton "Ateo"
                textbutton "B C W D"
                textbutton "BeGamerz45"
                textbutton "Benis"
                textbutton "Brett"
                textbutton "Byron"
                textbutton "caleb root"
                textbutton "citi96"
                textbutton "Daniel Campbell"
                textbutton "Darky"
                textbutton "Darcour"
                textbutton "Demiurge "
                textbutton "DIRKxTHExDARING "
                textbutton "diseasedrobot"
                textbutton "Dominik Becher"
                textbutton "DRAGNEEL"
                textbutton "Draschka"
                textbutton "Eden"
                textbutton "Eisen baren"
                textbutton "eliot tsekenis"
                textbutton "Emanon"
                textbutton "Erick Lopez"
                textbutton "Flat Hwy"
                textbutton "Ghostboy"
                textbutton "GoldwolfThePyrate"
                textbutton "good breakfast"
                textbutton "green blood ?"
                textbutton "Grodanjon"
                textbutton "Hunter Williams"
                textbutton "Ilya Veziko"
                textbutton "ITWeeb"
                textbutton "Jake"
                textbutton "JollyR "
                textbutton "Jules"
                textbutton "King Ko"
                textbutton "Kyle Doherty"
                textbutton "Lewis Brook"
                textbutton "Luke Horton"
                textbutton "Mal"
                textbutton "Mama J"
                textbutton "Matthew Downing"
                textbutton "man-stash"
                textbutton "Marco Harps"
                textbutton "Mon Key"
                textbutton "mrfeeny24"
                textbutton "Mulan szechuan"
                textbutton "My Name Is Kline"
                textbutton "Nijo"
                textbutton "NIUBIGGS 1"
                textbutton "Patrick McMurry"
                textbutton "Pau"
                textbutton "player1543"
                textbutton "Profile007"
                textbutton "Ryan Duchesne"
                textbutton "Sergio Pina"
                textbutton "Setosu "
                textbutton "Shiro"
                textbutton "Shugo"
                textbutton "Sindormi"
                textbutton "Siwinger"
                textbutton "Sky Wood"
                textbutton "Sumo"
                textbutton "Tara Nicole"
                textbutton "Teodor Jakop"
                textbutton "Thanatos"
                textbutton "Tonuxol"
                textbutton "Twistedinhead"
                textbutton "Van"
                textbutton "Vendetta!"
                textbutton "William Leetch"
                textbutton "Zamster"
                textbutton "1960's Where It's At"
                textbutton "_TheNineTailz_"
                textbutton "A Mere Shadow"
                textbutton "A U"
                textbutton "Aaron"
                textbutton "Aaron Rogers"
                textbutton "Aaron Seay"
                textbutton "Aaron V."
                textbutton "Adam Massacre"
                textbutton "Adam Tropf"
                textbutton "Adan Mejay-Pedraza"
                textbutton "Aegisjalmur"
                textbutton "Agarom032"
                textbutton "Ahau"
                textbutton "Aidanuro"
                textbutton "Akt1"
                textbutton "Alberto jose María de los campos"
                textbutton "Alex"
                textbutton "Alex Cortez"
                textbutton "Alex Maguire"
                textbutton "Alix"
                textbutton "Allisfiction"
                textbutton "Alygness"
                textbutton "Ambaw"
                textbutton "Ambrozioz"
                textbutton "Amon256"
                textbutton "Anarion01"
                textbutton "Andre"
                textbutton "Andreas Schöllhorn"
                textbutton "Andrew"
                textbutton "Andrew Hines"
                textbutton "Andrew In"
                textbutton "André Chay Sonda"
                textbutton "Andy"
                textbutton "AngryBlueTorle"
                textbutton "Anime Anilty"
                textbutton "anonymouse john"
                textbutton "Antonio"
                textbutton "Ape"
                textbutton "apfel"
                textbutton "Aquis Hyperion"
                textbutton "ArchAngel Reed"
                textbutton "Aric"
                textbutton "Articbezercer"
                textbutton "Ateo"
                textbutton "Ayoman"
                textbutton "Azazel"
                textbutton "Banj0afterdark"
                textbutton "Banque_Route"
                textbutton "Bayley Draper"
                textbutton "BeGamerz45"
                textbutton "Ben"
                textbutton "Benny"
                textbutton "BFTBGCory"
                textbutton "Bin Juice"
                textbutton "BlackKnight1945"
                textbutton "Blackwolf36"
                textbutton "Blaster177"
                textbutton "Blue Cabaret"
                textbutton "bob srig"
                textbutton "Boneless Waffle"
                textbutton "Boopergooch"
                textbutton "Brandon"
                textbutton "Brendan"
                textbutton "Brian Sweeney"
                textbutton "Brianevan Handoyo"
                textbutton "Brotasz"
                textbutton "Bruce Candy"
                textbutton "Bryan Lyon"
                textbutton "BumbleHumble"
                textbutton "C3D"
                textbutton "Caden Wiley"
                textbutton "Caleb Ramos"
                textbutton "Carter Roy"
                textbutton "Chamiou"
                textbutton "Charles Stecks"
                textbutton "Charles-Etienne Blaise"
                textbutton "Chris Kellerman"
                textbutton "Chris"
                textbutton "Chris Kuhl"
                textbutton "Chris Vang"
                textbutton "Christopher"
                textbutton "Christopher Schmader"
                textbutton "Christopher Stroud"
                textbutton "Cloud_4"
                textbutton "Clutch Mannhauser"
                textbutton "Colton Stirsman"
                textbutton "Conrad Josh"
                textbutton "Cosmic"
                textbutton "CrazyBearT"
                textbutton "Crustykins"
                textbutton "Dan Frost"
                textbutton "Daniel"
                textbutton "darius"
                textbutton "DarkKnight"
                textbutton "Dave"
                textbutton "David Jackson"
                textbutton "David Pruitt"
                textbutton "Davidjr"
                textbutton "Davin Benoit"
                textbutton "Dawjaw"
                textbutton "Demindran"
                textbutton "Dennes Diaz"
                textbutton "Dennis Gremory"
                textbutton "Destroyer333"
                textbutton "DevilsArmada"
                textbutton "Devoun"
                textbutton "dieispro"
                textbutton "DMan4g00d"
                textbutton "dojan hades"
                textbutton "Dominik Modsching"
                textbutton "Domino"
                textbutton "Doug Dimmadome"
                textbutton "Douglas"
                textbutton "dr dong"
                textbutton "Dr Gus"
                textbutton "draig"
                textbutton "Dreddras"
                textbutton "Duncan DeVore II"
                textbutton "Duncan Hook"
                textbutton "Dustin Millin"
                textbutton "Dylan H"
                textbutton "Ea7gign"
                textbutton "Elvis Gulbis"
                textbutton "Elwood Blakk"
                textbutton "ephiram"
                textbutton "Eric Mathews"
                textbutton "Espressointro"
                textbutton "EvolRofEvil"
                textbutton "Fabrice Alexander"
                textbutton "Fal Squall"
                textbutton "Squared"
                textbutton "FarColt"
                textbutton "Fera"
                textbutton "Feyth"
                textbutton "FinleyFresh"
                textbutton "fleffy"
                textbutton "Florian Seidel"
                textbutton "Flyingdrull"
                textbutton "Freya Wright"
                textbutton "Frogman139"
                textbutton "Gabriel"
                textbutton "Gandalf'ın 50 Tonu"
                textbutton "Garrick Bradley"
                textbutton "geeknolife"
                textbutton "Genthir"
                textbutton "George Abril"
                textbutton "George Bishop"
                textbutton "Geth Who"
                textbutton "Ginimy Huff"
                textbutton "Glocksinner"
                textbutton "Gogito03"
                textbutton "Goldenpackage"
                textbutton "Goldteiger2000"
                textbutton "Golgothan"
                textbutton "Graves"
                textbutton "Gravymix"
                textbutton "Gray Fox"
                textbutton "GSander"
                textbutton "Gwenllian"
                textbutton "H2O"
                textbutton "Harry"
                textbutton "Hart Stop"
                textbutton "Havik"
                textbutton "Helok"
                textbutton "hildyhoff"
                textbutton "Hoisenborg"
                textbutton "hunner"
                textbutton "I'm bored"
                textbutton "Ian Sommer"
                textbutton "Ice"
                textbutton "idkman"
                textbutton "IrviJai13"
                textbutton "Isaiah Sagayo"
                textbutton "Ish My Ale"
                textbutton "ItsLarry"
                textbutton "Jack"
                textbutton "Jacob"
                textbutton "Jacob"
                textbutton "Jacob"
                textbutton "Jacob Siedenberg"
                textbutton "jaidin"
                textbutton "Jake the Snake"
                textbutton "Jakh"
                textbutton "James Galati"
                textbutton "James Gibbs"
                textbutton "Jameson Rice"
                textbutton "Jared"
                textbutton "Jasonoy"
                textbutton "Jayson miller"
                textbutton "JC"
                textbutton "JDems21"
                textbutton "jeff edge"
                textbutton "Jeff Go"
                textbutton "Jelmer Meijer"
                textbutton "JJ Smith"
                textbutton "Johan Azeta"
                textbutton "John Snow"
                textbutton "Johnny Mee"
                textbutton "Jonathan hashimoto"
                textbutton "Jonathon Chasteler"
                textbutton "Jordan Armour"
                textbutton "jordan tawse"
                textbutton "Jorge Holt"
                textbutton "Joseph Carney"
                textbutton "joseph cochran"
                textbutton "Josh McGinnis"
                textbutton "Joshua Acevedo"
                textbutton "Joshua Bergman"
                textbutton "Joshua Hendricks"
                textbutton "Joshua Neal"
                textbutton "Justin Griggs"
                textbutton "Justinminers"
                textbutton "Kaizen"
                textbutton "Kalios"
                textbutton "Kantan"
                textbutton "keelall"
                textbutton "Keenen Reading"
                textbutton "KekkoNoTsuita"
                textbutton "Kevin Karashi"
                textbutton "Kevin Mays"
                textbutton "Kill Bill"
                textbutton "KingKudu"
                textbutton "KingzBTW"
                textbutton "Kortland Wood"
                textbutton "Kris Anderson"
                textbutton "kriz guy"
                textbutton "Kyle Kevin"
                textbutton "kyle smithart"
                textbutton "Kyuca"
                textbutton "Lahiik"
                textbutton "Lederpusmaximus"
                textbutton "Legna"
                textbutton "Leo"
                textbutton "Leonardo Meza"
                textbutton "Levi Nix"
                textbutton "Liam Richardson"
                textbutton "LM anthony"
                textbutton "Loco"
                textbutton "loman"
                textbutton "LORD DUSK"
                textbutton "Lucky"
                textbutton "MadKingNeks"
                textbutton "Maju"
                textbutton "Marco Pedroso"
                textbutton "Marduk mercado"
                textbutton "Mariul"
                textbutton "Marluistufa"
                textbutton "marsh"
                textbutton "Matt"
                textbutton "Matthew Cook"
                textbutton "Matthew L Youngblood"
                textbutton "Mav"
                textbutton "Maverick555119"
                textbutton "Maximilian Schwausch"
                textbutton "Maximilian Stünkel"
                textbutton "Mens Rea"
                textbutton "Mephistokiller"
                textbutton "Mercury Knyght"
                textbutton "Michael Downing"
                textbutton "Michael Peters"
                textbutton "MisterLama"
                textbutton "MisterSoftOwl"
                textbutton "Mr.OniChan"
                textbutton "Mr.smooth"
                textbutton "Nae Nae The Pain Away"
                textbutton "Nathan Baughman"
                textbutton "Nbts"
                textbutton "NewbiesLE"
                textbutton "Nicholas Vetterli"
                textbutton "Nirvous"
                textbutton "No Fucking Way"
                textbutton "Nonchalanto"
                textbutton "NopeToThat"
                textbutton "Obamasnow"
                textbutton "Optomus Rhymes"
                textbutton "Ozky"
                textbutton "Patrick Wittgens"
                textbutton "Paulson"
                textbutton "Phaedrus"
                textbutton "Phaeron Amarkun"
                textbutton "Phan"
                textbutton "Phillip T"
                textbutton "Pixelized"
                textbutton "pokepal"
                textbutton "poly"
                textbutton "Prism Paladin"
                textbutton "Prof Hulk"
                textbutton "Quekisol (formerly Isaiah A. Rodman)"
                textbutton "Queldroma32"
                textbutton "Raime Yule"
                textbutton "randy hummer"
                textbutton "Reddog69er"
                textbutton "Reece Wilson"
                textbutton "Reiseki"
                textbutton "Reze"
                textbutton "RLM Gamers Network"
                textbutton "Robert Newhall"
                textbutton "Robert Wallace"
                textbutton "Roman"
                textbutton "Ronin"
                textbutton "Ronokki"
                textbutton "Rowan Harth"
                textbutton "RTR20"
                textbutton "Ryan"
                textbutton "Ryuk"
                textbutton "Sander P. Rudolf"
                textbutton "santos hernandez"
                textbutton "savagegod"
                textbutton "Scott Carnegie"
                textbutton "Scumknuckles"
                textbutton "Sean Collins"
                textbutton "Sel"
                textbutton "selfminusone"
                textbutton "shadole"
                textbutton "shane larson"
                textbutton "Shaun Cline"
                textbutton "Sieg Warheidt"
                textbutton "Slaiior"
                textbutton "SmoothxPenguin"
                textbutton "Snipez5546"
                textbutton "sometimes lol"
                textbutton "Sora Kumuzu"
                textbutton "soullaw"
                textbutton "Stan Bridge"
                textbutton "Spartan117"
                textbutton "Spatenbiest"
                textbutton "Spencer Hawthorne"
                textbutton "Tarik Bastard"
                textbutton "Taylor Phommahaxay"
                textbutton "TFUHF"
                textbutton "tgwatp tgwatp"
                textbutton "that girl"
                textbutton "Thatchman21"
                textbutton "The Jerg"
                textbutton "the rgames"
                textbutton "Thomas Bruel"
                textbutton "Thomas Partin"
                textbutton "Thunderstorm586"
                textbutton "Tigh Aoibhneas"
                textbutton "timbolt2008"
                textbutton "Tom Delta"
                textbutton "trujillo"
                textbutton "Ty Farquharson"
                textbutton "Tyler Moses"
                textbutton "Tyler Winningham"
                textbutton "Ulfric Stormcloak"
                textbutton "Umbrus Shadowfell"
                textbutton "Valentine Lance"
                textbutton "Valentino Fontaine"
                textbutton "Valtyr"
                textbutton "Van"
                textbutton "Very Epic Name"
                textbutton "Virgil the Void Ray"
                textbutton "Vlynt"
                textbutton "Volkin Rose"
                textbutton "WaywarJB"
                textbutton "Weasely"
                textbutton "Will Romeo"
                textbutton "William Smith"
                textbutton "WolffeNGNM"
                textbutton "Xeliu"
                textbutton "Xiaoxue"
                textbutton "YellowLotr"
                textbutton "Ynik"
                textbutton "Zach"
                textbutton "Zachary Arntz"
                textbutton "Zachary Duran"
                textbutton "Zachary Schott"
                textbutton "Zaikon"
                textbutton "Zekken"
                textbutton "Ziggy"
                textbutton "Иван Иванович"
                textbutton "Максим Игнатьев"
                textbutton "家禎 萬"




                null height 10
                text "Five Dollar Patrons"
                null height 5

                textbutton "Aaron Lutz"
                textbutton "ACN GUY"
                textbutton "Adam PovolnÃ"
                textbutton "Adam Sun"
                textbutton "ADuditude"
                textbutton "Aeryn Monet"
                textbutton "Akira"
                textbutton "Alek Klock"
                textbutton "Alex Serrano"
                textbutton "Alexis"
                textbutton "Alixander Borja"
                textbutton "Andrew Mason"
                textbutton "Anonymous"
                textbutton "Apex_Aphelion"
                textbutton "Arikazei "
                textbutton "Artty the Dodge"
                textbutton "Asuh Duuude"
                textbutton "Bartelemys "
                textbutton "Ben"
                textbutton "Ben Weaver"
                textbutton "Benjamin Contart"
                textbutton "BigNin"
                textbutton "Black Flame Fox"
                textbutton "bleblebleble"
                textbutton "BlissfulDarkness "
                textbutton "Bloop Boop"
                textbutton "bob srig"
                textbutton "bobichuk"
                textbutton "Borkzilla"
                textbutton "Brandon Angelo Arcari"
                textbutton "Brandon Roode"
                textbutton "Brayden Schulz"
                textbutton "Brian Santiago"
                textbutton "Bryce Broom"
                textbutton "CÃ©dric"
                textbutton "CaliJ "
                textbutton "CaptainJohnsonPants "
                textbutton "Carlos de las Alas"
                textbutton "Chad Dreaney"
                textbutton "christian nicolas gonzalez pereira"
                textbutton "Clever Boi"
                textbutton "CompletelyPointlessUsername"
                textbutton "Corbyn Strickland"
                textbutton "DaddyKharn"
                textbutton "Daniel Nelson"
                textbutton "danny "
                textbutton "Darsh "
                textbutton "DatGameGuy "
                textbutton "David "
                textbutton "David Todd"
                textbutton "ddog006 "
                textbutton "Ddy14 "
                textbutton "Death of Rats"
                textbutton "Decoder"
                textbutton "DeMorgan"
                textbutton "Devon Patterson"
                textbutton "dimi"
                textbutton "Doug"
                textbutton "Dracyllion "
                textbutton "Drag"
                textbutton "Dragonas22"
                textbutton "D U"
                textbutton "duuuude"
                textbutton "Dylan Roussel"
                textbutton "Ed Romero"
                textbutton "Eggrollington "
                textbutton "EgilJarl "
                textbutton "ethanskully"
                textbutton "Fabian Hsl"
                textbutton "flamenessneel "
                textbutton "frank dailey"
                textbutton "FunBlameMonster"
                textbutton "GrayRaven "
                textbutton "Greg Bloomberg"
                textbutton "griplx"
                textbutton "gripping raccoon"
                textbutton "Gunner9213 "
                textbutton "Hamster Ball"
                textbutton "Havillard "
                textbutton "hayden general"
                textbutton "Hayden S."
                textbutton "Hendrik Meinke"
                textbutton "Hiezy"
                textbutton "Hunter Glad"
                textbutton "Ignis"
                textbutton "IIILegend"
                textbutton "Isaac Ruddell"
                textbutton "J"
                textbutton "Jack badman"
                textbutton "Jackie Vue"
                textbutton "Jacob Letter"
                textbutton "James Birch"
                textbutton "James Williams"
                textbutton "Jared25"
                textbutton "Jason Gardner"
                textbutton "Jesse Xiong"
                textbutton "Jive Clemens"
                textbutton "jo "
                textbutton "Joel Hubbard"
                textbutton "John Voss"
                textbutton "John Wendriks"
                textbutton "Jorge Cortes"
                textbutton "Josh Button"
                textbutton "just4porn"
                textbutton "kaiden haun"
                textbutton "Kamiriss Lumas"
                textbutton "Kane Macrone"
                textbutton "Keoson Huot"
                textbutton "Kevin Allen"
                textbutton "Kid Kami"
                textbutton "Kipren Martin"
                textbutton "Kit hansen"
                textbutton "kristian mercado"
                textbutton "Kyle leon"
                textbutton "Largeboi"
                textbutton "Laughing Jack"
                textbutton "Layne Scott"
                textbutton "legendarybort "
                textbutton "lego gear"
                textbutton "Levi Lanier"
                textbutton "Lucius the Eternal, Fulgrim's Champion"
                textbutton "Ludwig Tamari"
                textbutton "Lurifix "
                textbutton "v"
                textbutton "Lux"
                textbutton "Mad Lion"
                textbutton "madnessoreilli "
                textbutton "MadWorkYo "
                textbutton "Mal Solencis"
                textbutton "Mario4"
                textbutton "Master Cruz"
                textbutton "MasturbAsian"
                textbutton "Matheus Pereira"
                textbutton "Maximilian Datzmann"
                textbutton "Meandering Otaku"
                textbutton "MikeP"
                textbutton "Milen medway"
                textbutton "molly"
                textbutton "Muhammed Iqbal"
                textbutton "nero "
                textbutton "Nick Vo"
                textbutton "Nicolas Urrea"
                textbutton "Omynous "
                textbutton "Oskar SvÃ¤rd"
                textbutton "Paul "
                textbutton "Pdelaure"
                textbutton "Phynix "
                textbutton "Quentin Palmisano"
                textbutton "Quentin Ruelle"
                textbutton "Ramnezka"
                textbutton "Reegus Rockus"
                textbutton "Riley Faber"
                textbutton "Rillin "
                textbutton "robert eggers"
                textbutton "RoughIsTheBest"
                textbutton "Ruiner_Krauss"
                textbutton "Ryan"
                textbutton "Ryan Dwyer"
                textbutton "Ryan Hutchings"
                textbutton "SantaKlaus"
                textbutton "Sara Kline"
                textbutton "Sean Gregory"
                textbutton "Sebastian"
                textbutton "Seetinq"
                textbutton "shinra1997 "
                textbutton "Simon"
                textbutton "snow "
                textbutton "Sora"
                textbutton "Soxcutter"
                textbutton "ssths ."
                textbutton "Steve Sombdy"
                textbutton "Sunamiwater ."
                textbutton "SuperMadNess"
                textbutton "Talon Savage"
                textbutton "Tao Dude"
                textbutton "tattarattat "
                textbutton "Taylor Ohl"
                textbutton "ThatDude"
                textbutton "TheAmazingRando"
                textbutton "Thomas Whelan"
                textbutton "Tictacaddict "
                textbutton "Tinykodiak 9958"
                textbutton "TooneeLunes "
                textbutton "Trosy "
                textbutton "VÃ©steinn "
                textbutton "Vegna"
                textbutton "Victor Martins"
                textbutton "Vincent Darsigny"
                textbutton "Vincent Wedemann"
                textbutton "Walker Sparrow"
                textbutton "WeebLord483 "
                textbutton "william kappler"
                textbutton "William Patton"
                textbutton "Wirglays "
                textbutton "Zak699"
                textbutton "Zeku"
                textbutton "Zer0xx"
                textbutton "Zhong Ping"
                textbutton "Drake Whitlock"
                textbutton "Dralco"
                textbutton "Art Lopez"
                textbutton "Darkman"
                textbutton "Keef Stephens"
                textbutton "Coda_118"
                textbutton "JavonteEarl"
                textbutton "E"
                textbutton "Randall Wingert"
                textbutton "Jaiden bailey"
                textbutton "AmericanTZAR"
                textbutton "Shrockronson"
                textbutton "Jayten Treadwell"
                textbutton "Dat Dude"
                textbutton "Manuel Hernandez"
                textbutton "Farida Osman"
                textbutton "John Bigler"
                textbutton "Djmaxn"
                textbutton "bone lord"
                textbutton "MQ333"
                textbutton "oTEmber"
                textbutton "999devil997"
                textbutton "Dallas Selig"
                textbutton "robert tinnin"
                textbutton "tito"
                textbutton "Paxton Chapman"
                textbutton "Anese Richardson"
                textbutton "Logan Tomson"
                textbutton "ron"
                textbutton "Charles Orsborn"
                textbutton "Voktrenx Delevore"
                textbutton "Harley Lee"
                textbutton "Sara_Something"
                textbutton "HarukoCZE"




                null height 10
                text "One Dollar Patrons"
                null height 5

                textbutton "A R"
                textbutton "AbsentArmy "
                textbutton "Alex Dodge"
                textbutton "Andrej26 "
                textbutton "Alex Tavarez"
                textbutton "Anon "
                textbutton "Austin K"
                textbutton "Azula"
                textbutton "Bala Voine"
                textbutton "BeastlyPM "
                textbutton "Blubidiblub "
                textbutton "Bob Deca"
                textbutton "Boros "
                textbutton "Brian Shields"
                textbutton "Bugspit"
                textbutton "Buster Blader"
                textbutton "C B"
                textbutton "Cas vH"
                textbutton "Catlady972 "
                textbutton "Charles Styles"
                textbutton "Chris Woods"
                textbutton "Cody Cantrell"
                textbutton "Connor Speak"
                textbutton "Cosplayv"
                textbutton "Craig Zlist"
                textbutton "crazyhamp"
                textbutton "cv"
                textbutton "Cyber "
                textbutton "Dacotah Gunderson"
                textbutton "Dan"
                textbutton "D'andre "
                textbutton "Daniel Young"
                textbutton "Danny Parray"
                textbutton "David Johnson"
                textbutton "David Turton"
                textbutton "DelloS "
                textbutton "der koplose"
                textbutton "DeRoxas"
                textbutton "dogface"
                textbutton "Emmanuel Wil-Jeff"
                textbutton "Enos Dirk"
                textbutton "Esteban Vasquez"
                textbutton "F4ll3nN1nj4"
                textbutton "Ferninater"
                textbutton "Fewtch "
                textbutton "FezDisturbed"
                textbutton "Gambargin "
                textbutton "Gauthier Kreilmann"
                textbutton "Gavas"
                textbutton "Gerrit "
                textbutton "Golden Phoenix"
                textbutton "Goldenhand "
                textbutton "ironkoolart"
                textbutton "Israel Quintanar"
                textbutton "Itayoro "
                textbutton "jack ryan"
                textbutton "Jack3246 "
                textbutton "Jake Streets"
                textbutton "James Dean"
                textbutton "james trup"
                textbutton "Jake Nixon"
                textbutton "Jason Baxter"
                textbutton "Jeff Ellicott"
                textbutton "jeroen verboom"
                textbutton "Jesus Rodriguez"
                textbutton "Joe Clifton"
                textbutton "Joe mama"
                textbutton "John "
                textbutton "John Donahoe"
                textbutton "John Emmanuel Chua"
                textbutton "John Hall"
                textbutton "Johnathan Ellis"
                textbutton "Johnny Boy"
                textbutton "Josselyn Ramirez"
                textbutton "Jordan Ficca"
                textbutton "jordan tawse"
                textbutton "Karan Verma"
                textbutton "Kevin Reese"
                textbutton "King Kupo"
                textbutton "kingliu "
                textbutton "KingOfSalt "
                textbutton "Kukli"
                textbutton "Lastrosade "
                textbutton "Lata Meomu"
                textbutton "Lauren "
                textbutton "Les Clark"
                textbutton "Levan Nemsadze"
                textbutton "Levone W."
                textbutton "lilTedo"
                textbutton "Litia Raine"
                textbutton "Lockpitz"
                textbutton "Lord Hercules"
                textbutton "Lyubomir Georgiev"
                textbutton "managerW"
                textbutton "Marcelo Eduardo"
                textbutton "Markof"
                textbutton "Mateo Leon Torres Fun"
                textbutton "Matt"
                textbutton "Merlin1967 "
                textbutton "MGF "
                textbutton "MINIJD"
                textbutton "mspaintdrip "
                textbutton "Mylow Kay"
                textbutton "Naturebee "
                textbutton "NexFalx19 "
                textbutton "Nick Whittington"
                textbutton "Nickolas Cain"
                textbutton "Nico Bats"
                textbutton "NotDave "
                textbutton "notsurewhattotypehere"
                textbutton "Oats "
                textbutton "Ob Nixillis"
                textbutton "OsmiumAlt "
                textbutton "Ozxecho "
                textbutton "Palmer"
                textbutton "Paul "
                textbutton "phoenixsbane"
                textbutton "piotr natan"
                textbutton "plpolakpl"
                textbutton "PHSYCODELIC"
                textbutton "Quaxel"
                textbutton "Raife "
                textbutton "Randall "
                textbutton "Raspado"
                textbutton "Ravren "
                textbutton "Ricky"
                textbutton "Robo DaD"
                textbutton "rockyworld1"
                textbutton "Ryan Keever"
                textbutton "Ryan Wang"
                textbutton "Ryker Taylor"
                textbutton "Saul Gonzalez"
                textbutton "Sacke"
                textbutton "Scott McDonald"
                textbutton "Shambles"
                textbutton "Shaquille Robinson"
                textbutton "SilentChaos "
                textbutton "Skayph "
                textbutton "Smittykinick "
                textbutton "Styrka"
                textbutton "Someone "
                textbutton "summer100"
                textbutton "SUOCREZ"
                textbutton "SwitchB1ade"
                textbutton "ther3algurl"
                textbutton "tjx34"
                textbutton "Toastersock "
                textbutton "Todor"
                textbutton "Totemzero "
                textbutton "Travis Brewer"
                textbutton "Tu "
                textbutton "Vidschi"
                textbutton "vinny8boberano"
                textbutton "Whyze "
                textbutton "Will M"
                textbutton "Wyatt Wooden"
                textbutton "Z.orxy"
                textbutton "Zachary Goldwater"
                textbutton "zack vitali"
                textbutton "Friedrich"
                textbutton "user12345679"
                textbutton "CJ"
                textbutton "Mr. Argaz"
                textbutton "說 胡"
                textbutton "Nick Cloar"
                textbutton "Ahmad Masri"
                textbutton "Okamaru"
                textbutton "Maciej Roszak"
                textbutton "Brian Holbrook"
                textbutton "gourav singh"
                textbutton "Elonoic"
                textbutton "Ethan Santos"
                textbutton "Accel Down"
                textbutton "Rapture"
                textbutton "Justinius"
                textbutton "unknowntome"
                textbutton "Ariel Pomerance"
                textbutton "Beau merrick"
                textbutton "Unoriginal Trash Name"
                textbutton "Big Boagzy"
                textbutton "Metal_01"
                textbutton "Jeremy Ray"
                textbutton "Dan Fogel"
                textbutton "xxfenderbenderxx"
                textbutton "Cody"
                textbutton "Beanibus"
                textbutton "IceeSpicee"
                textbutton "syrup maple"
                textbutton "Chancetaker117"
                textbutton "Yoshmar Muriel"
                textbutton "Patchesssss"


        bar adjustment adj style "vscrollbar"

        textbutton _("Finished Looking."):
            xfill True
            action [ Hide("patroncredits"), Return(None)]
            top_margin 10
