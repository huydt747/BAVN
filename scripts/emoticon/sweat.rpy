image sweat_1 = "images/emoticon/Emoticon_Sweat_1.png"
image sweat_2 = "images/emoticon/Emoticon_Sweat_2.png"

image sweat_1_:
    "sweat_1"

    alpha 0.0
    zoom 0.5
    subpixel True
    linear 0.2 alpha 1
    yoffset 0.0 
    ease_quint 1.5 yoffset 40
    pause 0.6
    linear 1 alpha 0

image sweat_2_:
    "sweat_2"

    alpha 0.0
    zoom 0.5
    subpixel True
    pause 0.4
    linear 0.2 alpha 1
    yoffset 0.0 
    ease_quint 1.5 yoffset 30 
    linear 1 alpha 0

layeredimage _sweat:
    always:
        pos (140, 60)
        "sweat_1_"
    always:
        pos (175, 60)
        "sweat_2_"