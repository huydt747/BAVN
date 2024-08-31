#balloon_T import từ shy.rpy
image anxiety = "images/emoticon/Emoticon_Anxiety.png"

image _anxiety_:
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

layeredimage _anxiety:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        pos (114, 115)
        "_anxiety_"