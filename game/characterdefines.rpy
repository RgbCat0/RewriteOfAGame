# Ren'Py automatically loads all script files ending with .rpy. To use this
# file, define a label and jump to it from another file.

#list of characters and their definitions


define player = Character("[povname]", image = "player", color = "#FFFFFF", what_outlines=[ (2, "#000000") ])
image fbplayer current = ConditionSwitch("playerSprite == 0", "playerblink",\
"playerSprite == 1", "playerblinktalk", "playerSprite == 2", "Sprites/MC phone 1080.png",\
"playerSprite == 4", "playerblinkfrown",\
"playerSprite == 5","playerblinkfrowntalk", "playerSprite == 6","Sprites/MC pose nono.png",\
"playerSprite == 7", "Sprites/playerthinking.png", "playerSprite == 8", "Sprites/playerweaksmile.png",\
"playerSprite == 9", "playerwave", "playerSprite == 10", "playerwavetalk", "playerSprite == 11", "Sprites/playershock.png",\
"playerSprite == 12", "Sprites/playerahem.png", "playerSprite == 13", "Sprites/playerbigsmile.png",\
"playerSprite == 14", "Sprites/MC bad news.png", "playerSprite == 15", "Sprites/MC bad news talk.png",\
"playerSprite == 16", "Sprites/playerweaksmiletalk.png",  "playerSprite == 17", "Sprites/MC sprite 1080 surprised talk.png",\
"playerSprite == 18", "Sprites/MC sprite 1080 swimsuit.png", "playerSprite == 19", "Sprites/MC sprite 1080 swimsuit talk.png",\
"playerSprite == 20", "Sprites/MC swimsuit shock.png", "playerSprite == 21","Sprites/MC phone_hearing.png","playerSprite == 22","Sprites/MC phonetalk.png","True", "Sprites/playerdefault.png")

define mia = Character("Mia", image = "Mia", color = "#EBB0F4", what_outlines=[ (2, "#000000") ]) #For pink color use #FF00FF
image fbmia current = ConditionSwitch("miaSprite == 0", "miablink",\
"miaSprite == 1", "miablinktalk", "miaSprite == 2", "Sprites/miafrown.png","miaSprite == 3", "Sprites/miafrowntalk.png",\
"miaSprite == 4", "Sprites/miasmile.png", "miaSprite == 5", "Sprites/mialaugh.png","miaSprite == 6", "Sprites/mia yell.png",\
"miaSprite == 7", "Sprites/mia thinking hard.png","miaSprite == 8", "Sprites/mia sigh.png","miaSprite == 9", "Sprites/miaclapclap.png",\
"miaSprite == 10", "Sprites/miasurprise.png", "miaSprite == 11", "Sprites/mia pointing.png","miaSprite == 12","Sprites/miaupset.png",\
"miaSprite == 13", "Sprites/miaupset talk.png", "miaSprite == 14", "Sprites/mia bikini1 default.png",\
"miaSprite == 15", "Sprites/mia bikini2 default.png","miaSprite == 16", "Sprites/mia bikini3 default.png","miaSprite == 17", "Sprites/mia bikini1 happytalk.png",\
"True", "Sprites/miadefault.png")

define ava = Character("Ava", image = "Ava", color = "#18C514", what_outlines=[ (2, "#000000") ])
image fbava current = ConditionSwitch("avaSprite == 0", "avablink",\
"avaSprite == 1", "avablinktalk","avaSprite == 2", "avanosweaterblink", "avaSprite == 3", "avanosweaterblinktalk", \
"avaSprite == 4","Sprites/ava sprite blush.png","avaSprite == 5","Sprites/ava tired.png","avaSprite == 6","Sprites/ava stretch up.png",\
"avaSprite == 7","Sprites/ava stretch down.png","avaSprite == 8","Sprites/ava wtf.png", "avaSprite == 9", "Sprites/ava hair down default.png",\
"avaSprite == 10", "Sprites/ava hair down talk.png", "avaSprite == 11", "Sprites/ava blush talk.png", \
"avaSprite == 12", "Sprites/ava blank blush.png", "avaSprite == 13", "Sprites/ava turned on sweater.png",\
"avaSprite == 14", "Sprites/ava embarrassed.png", "avaSprite == 15", "Sprites/ava sprite sadsweater.png", "avaSprite == 16", "Sprites/ava sprite sadtalksweater.png",\
"avaSprite == 17", "Sprites/ava sprite surprised.png", "avaSprite == 18", "Sprites/ava sprite sad.png", "avaSprite == 19", "Sprites/ava sprite sadtalk.png",\
"avaSprite == 20", "Sprites/avanosweaterblushtalk.png", "avaSprite == 21", "Sprites/avasad.png", "avaSprite == 22", "Sprites/ava bikini.png",  
"avaSprite == 23", "Sprites/ava bikini talk.png", "True", "Sprites/avadefault.png")

define emily = Character("Emily", image = "Emily", color = "#5F1E84", what_outlines=[ (2, "#000000") ])
image fbemily current = ConditionSwitch("emilySprite == 0", "emilyblink",\
"emilySprite == 1", "emilyblinktalk", "emilySprite == 2", "Sprites/emily sprite blush.png",\
"emilySprite == 3", "Sprites/emily sprite sweet smile2.png", "emilySprite == 4", "Sprites/emily upset.png",\
"emilySprite == 5", "Sprites/emily upsettalk.png", "emilySprite == 6", "Sprites/emily bikini default.png",\
"emilySprite == 7", "Sprites/emily sprite blush2.png", "emilySprite == 8", "Sprites/emily bikini talk.png",\
"emilySprite == 9", "Sprites/emily blush.png", "True", "emilyblink")

define olivia = Character("Olivia", image = "Olivia", color = "#91D3EC", what_outlines=[ (2, "#000000") ])
image fbolivia current = ConditionSwitch("oliviaSprite == 0", "oliviablink",\
"oliviaSprite == 1", "oliviablinktalk", "oliviaSprite == 2", "Sprites/olivia sprite cringe.png",\
"oliviaSprite == 3", "Sprites/olivia sprite angery.png", "oliviaSprite == 4", "Sprites/olivia sprite angery talk.png",\
"oliviaSprite == 5", "Sprites/olivia sprite victory.png", "oliviaSprite == 6", "Sprites/olivia pointing at her boobs.png",\
"oliviaSprite == 7", "Sprites/olivia pointing at her boobs talk.png", "oliviaSprite == 8", "olivialookblink",\
"oliviaSprite == 9", "olivialookblinktalk", "oliviaSprite == 10", "Sprites/olivia sprite hands back headdown.png",\
"oliviaSprite == 11", "Sprites/olivia cry B.png", "oliviaSprite == 12", "Sprites/olivia cry2 B.png",\
"oliviaSprite == 13", "Sprites/olivia embarrassed B.png", "oliviaSprite == 14", "Sprites/olivia cute smile B.png",\
"oliviaSprite == 15", "Sprites/olivia bikini.png","oliviaSprite == 16", "Sprites/olivia bikini topless.png",\
"oliviaSprite == 17", "Sprites/olivia bikini talk.png", "oliviaSprite == 18", "Sprites/olivia blush handsback headdown mouthclosed.png",\
"oliviaSprite == 19", "Sprites/olivia bikini topless talk.png", "True", "Sprites/oliviadefault.png")

define sophia = Character("Sophia", image = "Sophia", color = "#C51425", what_outlines=[ (2, "#000000") ])
image fbsophia current = ConditionSwitch("sophiaSprite == 0", "sophiablink",\
"sophiaSprite == 1", "sophiatalk", "sophiaSprite == 2", "Sprites/sophia sprite sad.png",\
"sophiaSprite == 3", "Sprites/sophia sprite angery1.png", "sophiaSprite == 4", "Sprites/sophia sprite angery2.png",\
"sophiaSprite == 5", "Sprites/sophiaplayerhug.png", "sophiaSprite == 6", "Sprites/sophia rain.png",\
"sophiaSprite == 7", "Sprites/sophiasurpriseblushuptalk.png", "sophiaSprite == 8", "Sprites/sophiasurpriseblush.png", \
"sophiaSprite == 9", "Sprites/sophiasurpriseblushup.png", "sophiaSprite == 10","Sprites/sophia sprite sad notalk.png", \
"sophiaSprite == 11", "Sprites/sophia bikini.png", "sophiaSprite == 12", "Sprites/sophia bikini default.png", "True", "Sprites/sophiadefault.png")

define charlotte = Character("Charlotte", image = "Charlotte", color = "#F4F962", what_outlines=[ (2, "#000000") ])
image fbcharlotte current = ConditionSwitch("charlotteSprite == 0", "charlotteblink",\
"charlotteSprite == 1", "charlotteblinktalk", "charlotteSprite == 2", "Sprites/charlotte pointing.png",\
"charlotteSprite == 3", "Sprites/charlotte pointing talk.png", "charlotteSprite == 4", "Sprites/charlotte crying.png",\
"charlotteSprite == 5", "Sprites/charlotte sprite hugging arms.png", "charlotteSprite == 6", "Sprites/charlotte sprite blush.png",\
"charlotteSprite == 7", "Sprites/charlotte sprite bit lip.png", "charlotteSprite == 8", "Sprites/charlotte sprite embarrassed.png",\
"charlotteSprite == 9", "Sprites/charlotte phone.png", "charlotteSprite == 10", "Sprites/charlotte phone 1080.png",\
"charlotteSprite == 11", "Sprites/charlottehappytalk.png", "charlotteSprite == 12", "Sprites/charlotte crying B.png",\
"charlotteSprite == 13", "Sprites/charlotte sprite hugging arms talk.png", "charlotteSprite == 14", "Sprites/charlotte swimsuit default.png",\
"charlotteSprite == 15", "Sprites/charlotte swimsuit talk.png", "charlotteSprite == 16", "Sprites/charlottehappy.png","True", "Sprites/charlottedefault.png")


define cassandra = Character("Cassandra", image = "Cassandra", color = "#e5726e", what_outlines=[ (2, "#000000") ])
image fbcassandra current = ConditionSwitch("cassSprite == 0", "cassblink", "cassSprite == 1", "cassblinktalk",\
"True", "Sprites/cassandradefault.png")

define julia = Character("Julia", image = "Julia", color = "#7f4e6e", what_outlines=[ (2, "#000000") ])
image fbjulia current = ConditionSwitch("juliaSprite == 0", "juliablink", "juliaSprite == 2", "Sprites/juliapose1.png", \
"juliaSprite == 3", "juliablinktalk","juliaSprite == 4", "juliadefaultflip","juliaSprite == 5", "juliatalkflip",\
"juliaSprite == 6", "Sprites/juliasmile.png","juliaSprite == 7", "Sprites/julia liftbreasts.png", "juliaSprite == 8", "Sprites/julia formal base.png", \
"juliaSprite == 9", "Sprites/julia formal talk.png","juliaSprite == 10", "Sprites/julia formal arms crossed.png", \
"juliaSprite == 11", "Sprites/julia 1080p sexy.png", "True", "Sprites/juliadefault.png")

define katie = Character("Katie", image = "Katie", color ="#983236", what_outlines=[ (2, "#000000") ])
image fbkatie current = ConditionSwitch("katieSprite == 0", "katieuniformblink",\
"katieSprite == 1","katieuniformblinktalk","katieSprite == 2", "katieuniformchinblink", "katieSprite == 3","katieuniformchinblinktalk",\
"katieSprite == 4","katieblink","katieSprite == 5","katieblinktalk",\
"katieSprite == 6","Sprites/katiehips.png","katieSprite == 7","Sprites/katiehipstalk.png", "True", "katieuniformblink")

define ashley = Character("Ashley", image = "ashley", what_outlines=[ (2, "#000000") ])
image hbashley current = ConditionSwitch("ashleySprite == 0", "Sprites/ashley no BG.png",\
"ashleySprite == 1","Sprites/ashley talk no BG.png", "ashleySprite == 2","Sprites/ashley surprised.png",\
"ashleySprite == 3","Sprites/ashley confused.png")
image fbashley current = ConditionSwitch("ashleySprite == 4","Sprites/ashleydefault.png",\
"ashleySprite == 5","Sprites/ashleytalk.png", "ashleySprite == 6","Sprites/ashleytouch.png",\
"ashleySprite == 7","Sprites/ashleytouchtalk.png", "ashleySprite == 8","Sprites/ashleyvest.png",\
"True", "Sprites/ashley no BG.png")

define victoria = Character("Victoria", image = "victoria", what_outlines=[ (2, "#000000") ])
image fbvictoria current = ConditionSwitch("victoriaSprite == 0", "Sprites/victoriadefault.png",\
"victoriaSprite == 1", "Sprites/victoriatalk.png" ,"True", "Sprites/victoria sprite.png")

define josy = Character("Josy", image = "josy", what_outlines=[ (2, "#000000") ])
image fbjosy current = ConditionSwitch("josySprite == 0", "Sprites/josy1080default.png", "josySprite == 1", "Sprites/josy1080talk.png",\
"josySprite == 2", "Sprites/josy1080toothy.png", "josySprite == 3", "Sprites/jos1080 shrug.png", "josySprite == 4", "Sprites/josy uniform.png",\
"josySprite == 5", "Sprites/josy uniform talk.png", "josySprite == 6", "Sprites/josy uniform toothy.png",\
"True", "Sprites/josy1080default.png")

define stephanie = Character("Stephanie", image = "stephanie", color = "#e8bd8b", who_outlines = [(1, "#000000")], what_outlines = [(2,"#000000")])
image fbstephanie current = ConditionSwitch("stephanieSprite == 0", "stephanieblink", "stephanieSprite == 1", "stephanieblinktalk",\
"stephanieSprite == 2", "Sprites/stephaniearms.png","stephanieSprite == 3", "Sprites/stephaniearmstalk.png",\
"stephanieSprite == 4", "Sprites/stephanie1080 surprised.png","stephanieSprite == 5", "Sprites/stephanie1080 angry.png","True", "Sprites/stephaniedefault.png")

define raven = Character("Raven", image = "raven", color = "#280750", what_outlines = [(2,"#000000")])
image fbraven current = ConditionSwitch("ravenSprite == 0", "ravenblink", "ravenSprite == 1", "raventalk",\
 "ravenSprite == 2", "Sprites/ravenblush.png", "True", "Sprites/ravendefault.png")

define melissa = Character("Melissa", image = "melissa", color = "#507298", what_outlines = [(2,"#000000")])
image fbmelissa current = ConditionSwitch("melissaSprite == 0", "melissablink", "melissaSprite == 1", "melissatalk",\
 "melissaSprite == 2", "Sprites/melissa 1080 angry.png", "True", "Sprites/melissadefault.png")

define penny = Character("Penny", image = "penny", color = "#9782c5", what_outlines = [(2,"#000000")])
image fbpenny current = ConditionSwitch("pennySprite == 0", "pennyblink", "pennySprite == 1", "pennyblinktalk",\
"pennySprite == 2","Sprites/penny re pajamas.png","pennySprite == 3","Sprites/penny re pajamas talk.png", "True", "Sprites/melissadefault.png")

define narrarator = Character("", image = "", what_outlines=[(2,"#000000")])

# New games enter through label start in script.rpy.
