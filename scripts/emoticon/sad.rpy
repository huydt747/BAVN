image sad_1 = "images/emoticon/Emoji_Sad.png"
image sad_2 = "images/emoticon/Emoji_Sad.png"
image sad_3 = "images/emoticon/Emoji_Sad.png"
init -1 python:
    def play_effect_sad(trans, st, at):
        renpy.play("sfx/sad.ogg", channel="sound")
image _sad_1:
    "sad_1"
    function play_effect_sad
    subpixel True 
    zoom 0.55
    xzoom 0.8
    alpha 0
    parallel:
        linear 0.3 alpha 1
    parallel:
        yoffset 0.0 
        easein_quint 0.75 yoffset 30 
    parallel:
        yzoom 0.5 
        easein 0.75 yzoom 0.9 
    parallel:
        pause 1.6
        linear 0.5 alpha 0    
    #Pause(1.10)

image _sad_2:
    "sad_2"

    subpixel True
    zoom 0.55
    xzoom 0.8
    alpha 0
    parallel:
        pause 0.3
        linear 0.3 alpha 1
    parallel:
        pause 0.3
        yoffset 0.0 
        easein_quint 0.75 yoffset 30
    parallel:
        pause 0.3
        yzoom 0.5 
        easein 0.75 yzoom 0.9
    parallel:
        pause 1.6
        linear 0.5 alpha 0      
image _sad_3:
    "sad_3"

    subpixel True
    zoom 0.55
    xzoom 0.8
    alpha 0
    parallel:
        pause 0.6
        linear 0.3 alpha 1
    parallel:
        pause 0.6
        yoffset 0.0 
        easein_quint 0.75 yoffset 30
    parallel:
        pause 0.6
        yzoom 0.5 
        easein 0.75 yzoom 0.9  
    parallel:
        pause 1.6
        linear 0.5 alpha 0           

layeredimage yuuka_sad: # x + 15
    always:
        pos(130, 90)
        "_sad_1"
    always:
        pos(145, 100)
        "_sad_2"
    always:
        pos(160, 80)
        "_sad_3"
layeredimage serika_sad:
    always:
        pos(160, 90)
        "_sad_1"
    always:
        pos(175, 100)
        "_sad_2"
    always:
        pos(190, 80)
        "_sad_3"
layeredimage ayane_sad:
    always:
        pos(50, 90)
        "_sad_1"
    always:
        pos(65, 100)
        "_sad_2"
    always:
        pos(80, 80)
        "_sad_3"        
layeredimage hoshino_sad:
    always:
        pos(170, 90)
        "_sad_1"
    always:
        pos(185, 100)
        "_sad_2"
    always:
        pos(200, 80)
        "_sad_3"        
layeredimage nonomi_sad:
    always:
        pos(130, 90)
        "_sad_1"
    always:
        pos(145, 100)
        "_sad_2"
    always:
        pos(160, 80)
        "_sad_3"        
layeredimage shiroko_sad:
    always:
        pos(160, 90)
        "_sad_1"
    always:
        pos(175, 100)
        "_sad_2"
    always:
        pos(190, 80)
        "_sad_3"                