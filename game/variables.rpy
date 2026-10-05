# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

label definevariables:
    $ quest_hint_version = 2
    $ miaSprite = 0
    $ avaSprite = 0
    $ sophiaSprite = 0
    $ emilySprite = 0
    $ charlotteSprite = 0
    $ oliviaSprite = 0
    $ playerSprite = 0
    $ juliaSprite = 0
    $ katieSprite = 0
    $ cassSprite = 0
    $ pennySprite = 0
    $ ashleySprite = 0

    #random variables for character reasons

    #endchapter triggers(chapter 1 true or false, then route, then repeated for other chapters)
    $ currentchapter = 1
    $ Mia_endchapter1_trigger = "0"
    $ Sophia_endchapter1_trigger = "0"
    $ Ava_endchapter1_trigger = "0"
    $ Olivia_endchapter1_trigger = "0"
    $ Charlotte_endchapter1_trigger = "0"
    $ Emily_endchapter1_trigger = "0"

    $ Mia_endchapter2_trigger = "0"
    $ Sophia_endchapter2_trigger = "0"
    $ Ava_endchapter2_trigger = "0"
    $ Olivia_endchapter2_trigger = "0"
    $ Charlotte_endchapter2_trigger = "0"
    $ Emily_endchapter2_trigger = "0"

    $ Mia_endchapter3_trigger = "0"
    $ Sophia_endchapter3_trigger = "0"
    $ Ava_endchapter3_trigger = "0"
    $ Olivia_endchapter3_trigger = "0"
    $ Charlotte_endchapter3_trigger = "0"
    $ Emily_endchapter3_trigger = "0"

    #counter for amount of money spent at ashleys
    default amountspent = 0

    $ headtosunnyside = 0
    $ headtooffice = 0
    
    $ juliachecker = 0

    $ bullieschecker = 0

    $ ashleychecker = 0

    $ contact_list = ["Mia"]
    $ gallery_list = []

    $ item_list = []

    $ phone_pictures = []

    $ whereami = "playerRoom"

    $ miaphase1interaction1 = 0
    $ miaphase1interaction2 = 0
    $ miaphase1interaction3 = 0

    $ miaphase2interaction1 = 0
    $ miaphase2interaction2 = 0
    $ miaphase2interaction3 = 0

    $ miaphase3interaction1 = 0
    $ miaphase3interaction2 = 0
    $ miaphase3interaction3 = 0

    $ swimsuitchoice = "white"

    $ katiephase2interaction1 = 0
    $ katiephase3interaction1 = 0
    $ juliaphase2interaction1 = 0

    $ avaphase1interaction1 = 0
    $ avaphase1interaction2 = 0
    $ avaphase1interaction3 = 0

    $ avaphase2interaction1 = 0
    $ avaphase2interaction2 = 0
    $ avaphase2interaction3 = 0

    $ avaphase3interaction1 = 0
    $ avaphase3interaction2 = 0
    $ avaphase3interaction3 = 0

    $ avanaughtylevel = 0
    $ avanicelevel = 0
    $ avajobinterview = 999
    $ avadaycheck = 999

    $ emilyphase1interaction1 = 0
    $ emilyphase1interaction2 = 0
    $ emilyphase1interaction3 = 0

    $ emilyphase2interaction1 = 0
    $ emilyphase2interaction2 = 0
    $ emilyphase2interaction3 = 0

    $ emilyphase3interaction1 = 0
    $ emilyphase3interaction2 = 0
    $ emilyphase3interaction3 = 0

    $ emilynaughtylevel = 0
    $ emilynicelevel = 0
    $ emilydepravedlevel = 0

    $ emilydaychecker = 999

    $ sophiaphase1interaction1 = 0
    $ sophiaphase1interaction2 = 0
    $ sophiaphase1interaction3 = 0

    $ sophiaphase2interaction1 = 0
    $ sophiaphase2interaction2 = 0
    $ sophiaphase2interaction3 = 0

    $ sophiaphase3interaction1 = 0
    $ sophiaphase3interaction2 = 0
    $ sophiaphase3interaction3 = 0

    $ sophianaughtylevel = 0
    $ sophianicelevel = 0

    $ oliviaphase1interaction1 = 0
    $ oliviaphase1interaction2 = 0
    $ oliviaphase1interaction3 = 0

    $ oliviaphase2interaction1 = 0
    $ oliviaphase2interaction2 = 0
    $ oliviaphase2interaction3 = 0

    $ oliviaphase3interaction1 = 0
    $ oliviaphase3interaction2 = 0
    $ oliviaphase3interaction3 = 0

    $ olivianaughtylevel = 0
    $ olivianicelevel = 0
    $ oliviatournyday = 0

    $ charlottephase1interaction1 = 0
    $ charlottephase1interaction2 = 0
    $ charlottephase1interaction3 = 0

    $ charlottephase2interaction1 = 0
    $ charlottephase2interaction2 = 0
    $ charlottephase2interaction3 = 0

    $ charlottephase3interaction1 = 0
    $ charlottephase3interaction2 = 0
    $ charlottephase3interaction3 = 0

    $ charlottedaychecker1 = 999
    $ charlottedaychecker2 = 999

    $ victoriascene1part1 = 0
    $ victoriascene1part2 = 0
    $ victoriascene1part3 = 0

    $ cassandrascene1 = 0

    $ pennyscene1 = 0
    $ pennyscene2 = 0
    $ pennyscene3 = 0
    $ pennyscene4 = 0
    $ pennyscene5 = 0


    $ stephaniescene1 = 0
    $ stephaniescene2 = 0
    $ stephaniedaychecker = 0

    $ melissascene1 = 0
    $ melissascene2 = 0

    $ ravenscene1 = 0
    $ ravenscene2 = 0

    $ josyscene1 = 0
    $ josyscene2 = 0
    $ josiedaycheck = 100000

    if renpy.android:
        $ miaquestlog = "{size=-25}Meet Mia in Classroom 1 at school during Morning.{/size}"
    else:
        $ miaquestlog = "Meet Mia in Classroom 1 at school during Morning."
    $ avaquestlog = ""
    $ emilyquestlog = ""
    $ sophiaquestlog = ""
    $ oliviaquestlog = ""
    $ charlottequestlog = ""
    $ katiequestlog = ""
    $ juliaquestlog = ""
    $ victoriaquestlog = ""
    $ josyquestlog = ""
    $ cassandraquestlog = ""
    $ pennyquestlog = ""
    $ stephaniequestlog = ""
    $ ravenquestlog = ""
    $ melissaquestlog = ""

    $ avaquesticon = "gui/questboxAvagrey.png"
    $ emilyquesticon = "gui/questboxEmilygrey.png"
    $ sophiaquesticon = "gui/questboxSophiagrey.png"
    $ oliviaquesticon = "gui/questboxOliviagrey.png"
    $ charlottequesticon = "gui/questboxCharlottegrey.png"
    $ katiequesticon = "gui/questboxKatiegrey.png"
    $ juliaquesticon = "gui/questboxJuliagrey.png"
    $ victoriaquesticon = "gui/questboxVictoriagrey.png"
    $ josyquesticon = "gui/questboxJosygrey.png"
    $ cassandraquesticon = "gui/questboxCassandragrey.png"
    $ pennyquesticon = "gui/questboxPennygrey.png"
    $ stephaniequesticon = "gui/questboxStephaniegrey.png"
    $ ravenquesticon = "gui/questboxRavengrey.png"
    $ melissaquesticon = "gui/questboxMelissagrey.png"

    #$ hadcharlotteconvo = 0
    $ charlottenaughtylevel = 0
    $ charlottenicelevel = 0
    $ foundphonevariable = 1

    $ katieconversation = 0

    # Non Player Variables
    $ timeofday = "Morning" # (Morning, Day, Night)
    $ dayName = "Monday"
    $ dayNumber = 1
    $ money = 0
    $ hovertext = ""
    $ firsttimestore = 0
    $ watchcount = 1
    $ paintcount = 1
    $ moviecount = 1
    $ candycount = 3
    $ videogamecount = 1
    $ cameracount = 1
    $ condomcount = 1
    $ handcuffcount = 1
    $ librarycard = 0
    $ mysteryhouse = "Mansion"
    $ failedoliviatest = 0

    default tutorials_adjustment = ui.adjustment()

    # Initialization must enter the intro explicitly rather than end the game.
    jump gameIntro
