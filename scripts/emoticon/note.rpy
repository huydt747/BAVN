image note = "images/emoticon/Emoticon_Note.png"

# init -1 python:
#     def play_effect(trans, st, at):
#         renpy.play("effect.ogg", channel="sound")

image _note_:
    "note"

    subpixel True  
    parallel:
        offset (0.0, 0.0) 
        easein 1.00 offset (-30.0, -20.0) 
        linear 0.5 alpha 0
        #function play_effect
    parallel:
        rotate 0.0 
        linear 0.15 rotate 5.0 
        linear 0.15 rotate -5.0 
        linear 0.15 rotate 0.0 
        linear 0.15 rotate -5.0 
        easein 0.20 rotate 0.0 
    parallel:
        zoom 1.0 
        linear 0.15 zoom 1.05 
        linear 0.15 zoom 0.95 
        linear 0.15 zoom 1.05    
    #with Pause(1.10)

layeredimage _note:
    always:
        zoom 0.35
        pos (140, 80) #164
        "_note_"

