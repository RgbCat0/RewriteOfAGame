# starting with katie's phone convos
# convo 1
label conversationkatie1:
    $ katieconversationday = dayNumber
    player "{cps=25}Hey.{/cps}"
    katie "{cps=25}Oh? Texting me already huh?{/cps}"
    katie "{cps=25}That didn't take too long.{/cps}"
    player "{cps=25}Sorry I messaged you by accident!{/cps}"
    katie "{cps=25}Lol if you say so.{/cps}"
    jump returnwhereyouare

# convo 2
label conversationkatie2:
    if katieconversationday == dayNumber:
        player "I already texted her I should wait until tomorrow at least..."
        jump returnwhereyouare
    else:
        $ katieconversation = 2
        player "{cps=25}What's up?{/cps}"
        katie "{cps=25}Once is an accident, twice not so much.{/cps}"
        player "{cps=25}It really was I swear!{/cps}"
        katie "{cps=25}Suuuuure.{/cps}"
        katie "{cps=25}Well since I have you here, how's my sis in bed?{/cps}"
        player "{cps=25}I'm not telling you that.{/cps}"
        katie "{cps=25}C'mon! I'm basically just a fun sized version of her I'm only curious.{/cps}"
        katie "{cps=25}We even have the same sized tits!{/cps}"
        player "...."
        player "{cps=25}Not sayin.{/cps}"
        katie "{cps=25}Alright fine you're no fun.{/cps}"
        katie "{cps=25}Different question then.{/cps}"
        katie "{cps=25}What do you like most about her?{/cps}"
        player "....."
        player "{cps=25}Her tits.{/cps}"
        katie "{cps=25}Interesting.{/cps}"
        katie "{cps=25}You do know I JUST said we're pretty much equal in that regard?{/cps}"
        player "{cps=25}Yeah.{/cps}"
        katie "{cps=25}I take it back. You ARE fun.{/cps}"
        $ katieconversationday = dayNumber
        jump returnwhereyouare

# convo 3
label conversationkatie3:
    if katieconversationday == dayNumber:
        player "I already texted her I should wait until tomorrow at least..."
        jump returnwhereyouare
    else:
        $ katieconversation = 3
        player "Fuck what am I doing...."
        player "{cps=25}Hey Katie.{/cps}"
        katie "{cps=25}Haha you just can't get enough huh?{/cps}"
        player "{cps=25}I just wanna talk.{/cps}"
        katie "{cps=25}Yeah, like your cock isn't in your hand right now.{/cps}"
        player "....."
        katie "{cps=25}I know what you want, here I'll even help you...{/cps}"
        katie "{cps=25}I love it when a guy grabs my waist from behind and just fucks me senseless in front of a mirror so he can see my big tits bouncing as he pounds me.{/cps}"
        player "Jesus Christ...I can't ever let Mia see my phone..."
        katie "{cps=25}That something you'd be into doing?{/cps}"
        player "{cps=25}.....Yes.{/cps}"
        katie "{cps=25}With my sister of course ;){/cps}"
        player "{cps=25}Of course.{/cps}"
        katie "{cps=25}Knew you'd agree.{/cps}"
        $ katieconversationday = dayNumber
        jump returnwhereyouare

#convo 4
label conversationkatie4:
    if katieconversationday == dayNumber:
        player "I already texted her I should wait until tomorrow at least..."
        jump returnwhereyouare
    else:
        hide screen questboxpreview
        $ katieconversation = 4
        player "{cps=25}Katie?{/cps}"
        katie "{cps=25}Wow here we are again, you should be rewarded for your tenacity don't you think?{/cps}"
        player "....."
        katie "{cps=25}You aren't getting anything unless you respond.{/cps}"
        katie "{cps=25}What do you want?{/cps}"
        player "{cps=25}I want to be rewarded.{/cps}"
        katie "{cps=25}Good boy.{/cps}"
        katie "{cps=25}I'm a little busy right now so this'll have to do.{/cps}"
        katie "{cps=25}Sent.{/cps}"
        katie "{cps=25}Don't tell big sis ;){/cps}"
        player "I should check my images to see what she sent."
        $ renpy.notify("Got Katie's Selfie!")
        $ phone_pictures.append("katiebathselfie")
        $ katieconversationday = -1  # (jep note: certainly a way of not activating the convos anymore lmao)
        if currentchapter > 1:
            $ katiequestlog = "Maybe I should stop by Katie's room?"
        else:
            $ katiequestlog = "Katie is a naughty girl for sure, I should keep my distance for now.."

        jump returnwhereyouare

# end convo (5)
label conversationkatie5:
    player "I might get in trouble if I text her anymore..."
    jump returnwhereyouare

# chapter 1 end too ^