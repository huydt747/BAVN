image dot_1 = "images/emoticon/Emoticon_Idea_1.png"
image dot_2 = "images/emoticon/Emoticon_Idea_2.png"
image dot_3 = "images/emoticon/Emoticon_Idea_3.png"
image balloon_T = "images/emoticon/Emoticon_Balloon_T.png"


image _balloon_T:
    "balloon_T"
    subpixel True
    transform_anchor True anchor(1.0, 1.0)
    zoom 0.3
    easeout 0.1 zoom 0.6
    pause 0.8
    linear 0.5 alpha 0 
image _dot_1:
    pause 0.1
    "dot_1"
    alpha 0.0
    linear 0.2 alpha 1.0
    pause 1.2
    linear 0.5 alpha 0 
image _dot_2:
    pause 0.4
    "dot_2"
    alpha 0.0 
    linear 0.1 alpha 0.0 
    linear 0.2 alpha 1.0   
    pause 0.8
    linear 0.5 alpha 0   
image _dot_3:
    pause 0.7
    "dot_3"
    alpha 0.0 
    linear 0.2 alpha 0.0 
    linear 0.2 alpha 1.0 
    pause 0.4
    linear 0.5 alpha 0 

# broken, use layerdimage under there instead    
# image _thinking = Composite(
#     (0, 0),
#     (30, 50), "_balloon_T",
#     (15, 40), "_dot_1",
#     (15, 40), "_dot_2",
#     (15, 40), "_dot_3")

layeredimage _thinking:
    always:
        pos (164, 155) #164
        "_balloon_T"
    always:
        pos (15, 40)
        "_dot_1"
    always:
        pos (15, 40)
        "_dot_2"
    always:
        pos (15, 40)
        "_dot_3"