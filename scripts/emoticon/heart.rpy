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
