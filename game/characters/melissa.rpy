# chapter 2
# scene 1

label melissadancescene:
    hide screen backbuttonCLUB
    hide screen questboxpreview
    hide screen backbuttonCLUBRESTROOM
    hide screen gotoclubrestroom
    hide screen gotoclubrestroomDay
    show fbplayer current:
        xalign 0.5 ypos 120
    with Dissolve(0.7)
    player "{i}Man it's so loud in here when they got the music going!{/i}"
    player "Huh is that...Meli-"
    show fbmelissa current at surpriseshake:
        xalign 0.65 ypos 120
    melissa "OH MY GOD HEY!"
    player "HEY!"
    player "WHAT ARE YOU DOING HERE?"
    melissa "COME DANCE WITH ME!"
    player "WHAT?"
    melissa "COME ON!"
    show fbplayer current:
        xalign 1.5 ypos 120
    show fbmelissa defaultflip:
        xalign 1.65 ypos 120
    with move
    pause
    scene fs melissadancepov1
    with Dissolve(1.0)
    "Once Melissa took you to the dance floor it was clear what she wanted"
    scene fs melissadancepov2
    with Dissolve(0.5)
    "She had some intesting dance moves.."
    scene fs melissadancepov3
    with Dissolve(0.5)
    "But you had to admit it was still pretty hot"
    scene fs melissadancepov4
    "She really knew how to make her assets...move"
    "You had no idea how well you were dancing"
    "But you figured she was used to guys being distracted while on the dance floor"
    scene fs melissadancepov5
    "Wait is that a Sailor Star pose?"
    scene fs blackblank
    with Dissolve(0.7)
    scene fs melissadance1a
    melissa "Woooo!"
    scene fs melissadance1b
    melissa "Hahaha!"
    player "Damn girl!"
    scene fs melissadance2
    pause
    scene fs melissadance3a
    pause
    scene fs melissadance3b
    melissa "That was a lot of fun!"
    scene fs melissadance3c
    player "Hah..hah..yeah! The music has finally gone down a bit."
    scene fs melissadance3b
    melissa "Wanna have some more fun?"
    scene fs melissadance3c
    player "What do you m-"
    scene fs melissadance4 at surpriseshake
    player "!!!"
    melissa "Mmmm!"
    scene fs melissadance5a
    melissa "...."
    player "...."
    scene fs melissadance5b
    pause
    scene fs melissadance5c
    "*Pop*"
    scene fs melissadance6
    melissa "Hahaha!"
    melissa "You're so funny!"
    player "Thanks!"
    scene fs melissadance7
    with Dissolve(1.0)
    melissa "I think I wanna cash in that favor of mine..."
    melissa "Girl's bathroom, third stall."
    scene fs blackblank
    with Dissolve(1.0)
    "Melissa quickly ran off towards the restrooms"
    "With the sultry look, she beconed you to follow her"
    $ melissascene1 = 1
    jump insideclub

# scene 2

label melissadancescene2:
    hide screen backbuttonCLUBRESTROOM
    scene fs melissagh1
    with Dissolve(1.0)
    pause
    player "...."
    player "{i}I know this could be really stupid.{/i}"
    scene fs melissagh2
    player "{i}But I'm incredibly horny right now.{/i}"
    scene fs melissagh3
    with Dissolve(0.7)
    player "{i}Oh? I can feel someone's breath.{/i}"
    scene fs melissagh4
    melissa "Hahaha! It's huge!"
    player "{i}Yeah that's definitely M-{/i}"
    show melissagh movie
    player "{i}Oh shit!{/i}"
    player "{i}Yeah that is...{/i}"
    player "{i}She knows what she's doing!{/i}"
    show melissagh movie2
    pause
    melissa "Guhk Guhk Guhk!"
    player "{i}Fuck I can hear her gagging on my cock!{/i}"
    player "{i}I'm gonna fucking cum already!{/i}"
    player "Ahh!"
    show melissagh movie3
    melissa "Ahnnn!"
    player "Holy shit!"
    scene fs melissagh8
    melissa "Hah...hah.."
    scene fs blackblank
    with Dissolve(0.6)
    player "That might've been the best blowjob I've ever had."
    melissa "Hehehe."
    player "What is sh-"
    show melissaselfie postnutbathroom
    with flash
    pause
    player "Did she just take a picture?"
    melissa "{i}The girls are gonna LOVE this.{/i}"
    $ renpy.notify("Got Melissa's Picture!")
    $ phone_pictures.append("bullies selfies mel")
    hide melissaselfie postnutbathroom
    with Dissolve(0.5)
    scene fs blackblank
    with Dissolve(1.0)
    "A little embarrassed at your public promiscuity, you leave the bathroom and then the club"
    
    player "I wonder what she's gonna be like next time I talk to her..."
    $ melissascene1 = 2
    $ melissaquestlog = "No more solo content for Melissa in this version (Ch2.5B)"
    jump passtime