image angry = "images/emoticon/Emoticon_Aggro.png"
init -1 python:
    def play_effect_angry(trans, st, at):
        renpy.play("sfx/angry.ogg", channel="sound")
image _angry:
    "angry"
    function play_effect_angry
    subpixel True
    transform_anchor True anchor(0.5, 0.5)
    parallel:
        zoom 0.5 
        easein 0.25 zoom 0.6
        linear 0.05 zoom 0.6 
        easein 0.20 zoom 0.5 
        easein 0.50 zoom 0.6 
    parallel:
        alpha 1.0 
        linear 1.00 alpha 1.0 
        linear 0.30 alpha 0.0 
                  
        
         