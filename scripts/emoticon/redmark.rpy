image redmark = "images/emoticon/Emoticon_ExclamationMark.png"

image _redmark_:
    "redmark"
    subpixel True
    transform_anchor True anchor(1.0, 1.0)
    parallel:
        zoom 0.4 
        easeout 0.50 zoom 0.6 
        linear 0.05 zoom 0.6 
        easein 0.25 zoom 0.45 
    parallel:
        alpha 1.0 
        linear 0.80 alpha 1.0 
        linear 0.50 alpha 0.0 

# image _redmark = Composite(
#     (0, 0),
#     (0, 0), "_redmark_"
# )

layeredimage _redmark:
    always:
        pos(180, 130)
        "_redmark_"
