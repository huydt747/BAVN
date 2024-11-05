image greenqs = "images/emoticon/Emoticon_QuestionMark.png"

image _greenqs:
    "greenqs"
    anchor (0, 0)
    zoom 0.10
    yzoom 0.50
    subpixel True 
    parallel:
        yanchor 1.0 
        linear 0.20 yanchor 1.0 
    parallel:
        xzoom 1.0 
        linear 0.15 xzoom 1.0 
        linear 0.25 xzoom 1.25 
        ease 0.40 xzoom 1.1 
    parallel:
        yzoom 0.5 
        ease 0.20 yzoom 1.0 
        linear 0.20 yzoom 1.25 
        ease 0.40 yzoom 1.1 
    parallel:
        linear 0.01 zoom 0.4 
    parallel:
        pause 1
        linear 0.5 alpha 0.0
