image action = "images/emoticon/Emoticon_Action.png"
init -1 python:
    def play_effect_action(trans, st, at):
        renpy.play("sfx/action.ogg", channel="sound")

image _action:
    "action"
    function play_effect_action
    zoom 0.45
    subpixel True
    alpha 0.0 
    linear 0.10 alpha 1.0 
    linear 0.10 alpha 0.0 
    linear 0.10 alpha 1.0 
    linear 0.90 alpha 1.0 
    linear 0.30 alpha 0.0