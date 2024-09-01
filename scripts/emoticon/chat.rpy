image chat = "images/emoticon/Emoticon_Chat.png"
init -1 python:
    def play_effect_chat(trans, st, at):
        renpy.play("sfx/chat.ogg", channel="sound")
image _chat:
    "chat"
    function play_effect_chat
    zoom 0.4
    anchor (1, 0.5)
    subpixel True 
    rotate 0.0 
    ease 0.25 rotate -10
    ease 0.25 rotate 10
    ease 0.25 rotate -10
    ease 0.25 rotate 10
    ease 0.25 rotate -10
    linear 0.5 alpha 0    

layeredimage yuuka_chat:
    always:
        pos (100, 190) 
        "_chat"
layeredimage serika_chat:
    always:
        pos (120, 190) 
        "_chat"
layeredimage ayane_chat:
    always:
        pos (10, 190) 
        "_chat"

