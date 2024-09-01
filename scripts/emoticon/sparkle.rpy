image sparkle_1 = "images/emoticon/Emoticon_Twinkle.png"
image sparkle_2 = "images/emoticon/Emoticon_Twinkle.png"
image sparkle_3 = "images/emoticon/Emoticon_Twinkle.png"

image _sparkle_1:
    "sparkle_1"

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

layeredimage yuuka_sparkle:
    always:
        zoom 0.4
        pos (155, 110)
        "_sparkle_1"
    always:
        zoom 0.5
        pos (130, 132)
        "_sparkle_2"
    always:
        zoom 0.5
        pos (155, 155)
        "_sparkle_3"
layeredimage serika_sparkle:
    always:
        zoom 0.4
        pos (175, 110)
        "_sparkle_1"
    always:
        zoom 0.5
        pos (150, 132)
        "_sparkle_2"
    always:
        zoom 0.5
        pos (175, 155)
        "_sparkle_3"
layeredimage ayane_sparkle:
    always:
        zoom 0.4
        pos (75, 110)
        "_sparkle_1"
    always:
        zoom 0.5
        pos (50, 132)
        "_sparkle_2"
    always:
        zoom 0.5
        pos (75, 155)
        "_sparkle_3"
