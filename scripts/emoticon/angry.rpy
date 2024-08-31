image angry = "images/emoticon/Emoticon_Aggro.png"

image _angry_:
    "angry"
    subpixel True
    transform_anchor True anchor(0.5, 0.5)
    parallel:
        zoom 0.5 
        easein 0.25 zoom 0.6
        linear 0.05 zoom 0.6 
        easein 0.20 zoom 0.5 
        easein 0.50 zoom 0.6 
    parallel:
        alpha 1.0 
        linear 1.00 alpha 1.0 
        linear 0.30 alpha 0.0 
  
# image _angry = Composite(
#     (0, 0),
#     (150, 100), "_angry_"
# )

layeredimage _angry:
    always:
        pos(170,120)
        "_angry_"