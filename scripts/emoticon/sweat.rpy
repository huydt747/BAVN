image sweat_1 = "images/emoticon/Emoticon_Sweat_1.png"
image sweat_2 = "images/emoticon/Emoticon_Sweat_2.png"
init -1 python:
    def play_effect_sweat(trans, st, at):
        renpy.play("sfx/sweat.ogg", channel="sound")
image _sweat_1:
    "sweat_1"
    function play_effect_sweat
    alpha 0.0
    zoom 0.5
    subpixel True
    linear 0.2 alpha 1
    yoffset 0.0 
    ease_quint 1.5 yoffset 40
    pause 0.6
    linear 1 alpha 0

image _sweat_2:
    "sweat_2"

    alpha 0.0
    zoom 0.5
    subpixel True
    pause 0.4
    linear 0.2 alpha 1
    yoffset 0.0 
    ease_quint 1.5 yoffset 30 
    linear 1 alpha 0

layeredimage yuuka_sweat:
    always:
        pos (140, 60)
        "_sweat_1"
    always:
        pos (175, 60)
        "_sweat_2"
layeredimage serika_sweat:
    always:
        pos (160, 60)
        "_sweat_1"
    always:
        pos (195, 60)
        "_sweat_2"
layeredimage ayane_sweat:
    always:
        pos (70, 60)
        "_sweat_1"
    always:
        pos (105, 60)
        "_sweat_2"                