#balloon_N import từ thinking.rpy
image anxiety = "images/emoticon/Emoticon_Anxiety.png"

image _anxiety:
    "anxiety"
    subpixel True
    anchor(0.5, 0.5)
    zoom 0.4
    alpha 0.0
    parallel:
        linear 0.5 alpha 1
    parallel:
        rotate 0.0 
        ease 0.40 rotate -18.0 
        ease 0.40 rotate 10.0 
        ease 0.20 rotate 0.0 
    parallel:
        xzoom 1.0 
        ease 1.00 xzoom 0.9 
    parallel:
        yzoom 1.0 
        ease 0.20 yzoom 1.1 
        ease 0.20 yzoom 0.9 
        ease 0.20 yzoom 1.1 
        ease 0.20 yzoom 1.0 
        ease 0.20 yzoom 1.07 
    parallel:
        pause 0.8
        linear 0.5 alpha 0  

layeredimage yuuka_anxiety:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        pos (114, 115)
        "_anxiety"
layeredimage serika_anxiety:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        pos (114, 115)
        "_anxiety"
layeredimage ayane_anxiety:
    always:
        pos (80, 155)
        "_balloon_N"
    always:
        pos (30, 115)
        "_anxiety"                