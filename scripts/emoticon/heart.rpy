#serika 5 1:15
image heart = "images/emoticon/Emoticon_Heart.png"
init -1 python:
    def play_effect_heart(trans, st, at):
        renpy.play("sfx/heart.ogg", channel="sound")
image _heart:
    "heart"
    function play_effect_heart
    subpixel True 
    anchor(0.5, 0.5)
    alpha 0
    parallel:
        linear 0.5 alpha 1
    parallel:
        matrixtransform ScaleMatrix(0.6, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        ease 0.50 matrixtransform ScaleMatrix(1.0, 1.2, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        ease 0.25 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    parallel:
        zoom 0.3 
        easein 0.50 zoom 1.0 
        easeout 0.25 zoom 0.75 
        easeout 0.10 zoom 0.85 
    parallel:
        pause 0.85
        linear 0.5 alpha 0    
    #0.85s
layeredimage yuuka_heart: #-52
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (112, 113)
        "_heart"
layeredimage serika_heart:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (112, 113)
        "_heart"
layeredimage ayane_heart:
    always:
        pos (90, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (38, 113)
        "_heart"
layeredimage hoshino_heart:
    always:
        pos (200, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (148, 113)
        "_heart"                
layeredimage nonomi_heart:
    always:
        pos (150, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (98, 113)
        "_heart"                                