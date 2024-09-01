image sparkle_1 = "images/emoticon/Emoticon_Twinkle.png"
image sparkle_2 = "images/emoticon/Emoticon_Twinkle.png"
image sparkle_3 = "images/emoticon/Emoticon_Twinkle.png"

image _sparkle_1_:
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

image _sparkle_2_:
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

image _sparkle_3_:
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

layeredimage _sparkle:
    always:
        zoom 0.4
        pos (155, 110)
        "_sparkle_1_"
    always:
        zoom 0.5
        pos (130, 132)
        "_sparkle_2_"
    always:
        zoom 0.5
        pos (155, 155)
        "_sparkle_3_"
