image sparkle_1 = "images/emoticon/Emoticon_Twinkle.png"
image sparkle_2 = "images/emoticon/Emoticon_Twinkle.png"
image sparkle_3 = "images/emoticon/Emoticon_Twinkle.png"
init -1 python:
    def play_effect_sparkle(trans, st, at):
        renpy.play("sfx/sparkle.ogg", channel="sound")
image _sparkle_1:
    "sparkle_1"
    function play_effect_sparkle
    subpixel True
    anchor (0.5, 0.5)
    zoom 0.75    
    alpha 0
    parallel:
        linear 0.5 alpha 1
    parallel:
        ease 0.50 zoom 0.9 
        ease 0.50 zoom 0.75
        ease 0.50 zoom 0.9
        ease 0.50 zoom 0.75
    parallel:    
        pause 1.5
        linear 0.9 alpha 0

image _sparkle_2:
    "sparkle_2"

    subpixel True
    anchor (0.5, 0.5)  
    alpha 0
    parallel:
        linear 0.5 alpha 1
    parallel:  
        ease 0.50 zoom 0.85 
        ease 0.50 zoom 1
        ease 0.50 zoom 0.85 
        ease 0.50 zoom 1 
    parallel:    
        pause 1.5
        linear 0.9 alpha 0

image _sparkle_3:
    "sparkle_3"

    subpixel True
    anchor (0.5, 0.5)  
    zoom 0.5
    alpha 0
    parallel:
        linear 0.5 alpha 1
    parallel:  
        ease 0.50 zoom 0.7 
        ease 0.50 zoom 0.5
        ease 0.50 zoom 0.7 
        ease 0.50 zoom 0.5 
    parallel:    
        pause 1.5
        linear 0.9 alpha 0
