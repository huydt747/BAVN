image dot_1 = "images/emoticon/Emoticon_Idea_1.png"
image dot_2 = "images/emoticon/Emoticon_Idea_2.png"
image dot_3 = "images/emoticon/Emoticon_Idea_3.png"
image balloon_T = "images/emoticon/Emoticon_Balloon_T.png"
init -1 python:
    def play_effect_thinking(trans, st, at):
        renpy.play("sfx/thinking.ogg", channel="sound")

image _balloon_T:
    "balloon_T"
    subpixel True
    transform_anchor True anchor(1.0, 1.0)
    zoom 0.2
    easeout 0.1 zoom 0.4
    pause 1.1
    linear 0.5 alpha 0
image _dot_1:
    function play_effect_thinking
    pause 0.1
    "dot_1"
    zoom 0.7
    alpha 0.0
    linear 0.2 alpha 1.0
    pause 1
    linear 0.5 alpha 0 
image _dot_2:
    pause 0.4
    "dot_2"
    zoom 0.7
    alpha 0.0
    linear 0.1 alpha 0.0 
    linear 0.2 alpha 1.0   
    pause 0.6
    linear 0.5 alpha 0  
image _dot_3:
    pause 0.7
    "dot_3"
    zoom 0.7
    alpha 0.0 
    linear 0.2 alpha 0.0 
    linear 0.2 alpha 1.0 
    pause 0.2
    linear 0.5 alpha 0 

# broken, use layerdimage under there instead    
# image _thinking = Composite(
#     (0, 0),
#     (30, 50), "_balloon_T",
#     (15, 40), "_dot_1",
#     (15, 40), "_dot_2",
#     (15, 40), "_dot_3")

layeredimage yuuka_thinking:
    always:
        pos (165, 155) #164
        "_balloon_T"
    always:
        pos (55, 60)
        "_dot_1"
    always:
        pos (55, 60)
        "_dot_2"
    always:
        pos (55, 60)
        "_dot_3"
layeredimage serika_thinking:
    always:
        pos (165, 155) #164
        "_balloon_T"
    always:
        pos (55, 60)
        "_dot_1"
    always:
        pos (55, 60)
        "_dot_2"
    always:
        pos (55, 60)
        "_dot_3"
layeredimage ayane_thinking:
    always:
        pos (90, 155) #164
        "_balloon_T"
    always:
        pos (-20, 60)
        "_dot_1"
    always:
        pos (-20, 60)
        "_dot_2"
    always:
        pos (-20, 60)
        "_dot_3"                