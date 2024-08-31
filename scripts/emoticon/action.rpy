image action = "images/emoticon/Emoticon_Action.png"

image _action_:
    "action"
    
    zoom 0.45
    subpixel True
    alpha 0.0 
    linear 0.10 alpha 1.0 
    linear 0.10 alpha 0.0 
    linear 0.10 alpha 1.0 
    linear 0.90 alpha 1.0 
    linear 0.30 alpha 0.0

image _action = Composite(
    (0, 0),
    (105, 90), "_action_")