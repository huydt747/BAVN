image balloon_N = "images/emoticon/Emoticon_Balloon_N.png"
image shy = "images/emoticon/Emoticon_Shy.png"

image _balloon_N:
    "balloon_N"
    subpixel True
    anchor(1.0, 1.0)
    zoom 0.3
    easeout 0.1 zoom 0.6
    pause 0.8
    linear 0.5 alpha 0

image _shy:
    "shy"
    subpixel True
    anchor(0.5, 0.5)
    zoom 0.3
    alpha 0
    parallel:
        linear 0.1 alpha 1
    parallel:
        rotate -10.0 
        ease 0.25 rotate 10.0 
        ease 0.25 rotate -10.0 
        ease 0.25 rotate 10.0 
        ease 0.25 rotate -10.0 
        ease 0.25 rotate 10.0 
    parallel:
        zoom 0.4 
        easein 0.10 zoom 0.45 
    parallel:
        pause 0.8
        linear 0.5 alpha 0  
    #1.25s



layeredimage yuuka_shy:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        pos (115, 110)
        "_shy"
layeredimage serika_shy:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        pos (112, 110)
        "_shy"
layeredimage ayane_shy:
    always:
        pos (100, 155)
        "_balloon_N"
    always:
        pos (48, 110)
        "_shy"        
