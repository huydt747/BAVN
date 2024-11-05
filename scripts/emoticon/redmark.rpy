image redmark = "images/emoticon/Emoticon_ExclamationMark.png"
init -1 python:
    def play_effect_exclamationmark(trans, st, at):
        renpy.play("sfx/exclamationmark.ogg", channel="sound")
image _redmark:
    "redmark"
    function play_effect_exclamationmark
    subpixel True
    transform_anchor True anchor(1.0, 1.0)
    matrixtransform ScaleMatrix(1.0, 0.2, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    parallel:   
        easein_quart 0.30 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    parallel:
        zoom 0.4 
        easeout_quad 0.2 zoom 0.5 
        linear 0.05 zoom 0.5 
        easein_quad 0.2 zoom 0.45 
    parallel:
        alpha 1.0 
        linear 0.80 alpha 1.0 
        linear 0.50 alpha 0.0 
