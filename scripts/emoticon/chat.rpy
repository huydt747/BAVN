image chat = "images/emoticon/Emoticon_Chat.png"

image _chat_:
    "chat"
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

layeredimage _chat:
    always:
        pos (100, 190) 
        "_chat_"
