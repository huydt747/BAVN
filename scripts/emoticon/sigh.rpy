image sigh = "images/emoticon/Emoji_Sigh.png"

image _sigh_:
    "sigh"
    subpixel True 
    zoom 0.5
    easein_quart 0.80 offset (-35.0, 20.0) 
    linear 0.5 alpha 0.0


layeredimage _sigh:
    always:
        pos (120, 185)
        "_sigh_"