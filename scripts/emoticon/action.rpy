image action = "images/emoticon/Emoticon_Action.png"

image _action:
    "action"
    
    zoom 0.45
    subpixel True
    alpha 0.0 
    linear 0.10 alpha 1.0 
    linear 0.10 alpha 0.0 
    linear 0.10 alpha 1.0 
    linear 0.90 alpha 1.0 
    linear 0.30 alpha 0.0

image yuuka_action = Composite(
    (0, 0),
    (105, 90), "_action")
image serika_action = Composite(
    (0, 0),
    (105, 90), "_action")   
image ayane_action = Composite(
    (0, 0),
    (15, 90), "_action")         