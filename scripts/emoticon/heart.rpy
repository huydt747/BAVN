#serika 5 1:15
#gọi balloon_T từ shy.rpy
image heart = "images/emoticon/Emoticon_Heart.png"

image _heart_:
    "heart"
    subpixel True 
    anchor(0.5, 0.5)
    alpha 0
    parallel:
        linear 0.5 alpha 1
    parallel:
        matrixtransform ScaleMatrix(0.6, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        ease 0.50 matrixtransform ScaleMatrix(1.0, 1.2, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
        ease 0.25 matrixtransform ScaleMatrix(1.0, 1.0, 1.0)*OffsetMatrix(0.0, 0.0, 0.0)*RotateMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0)*OffsetMatrix(0.0, 0.0, 0.0) 
    parallel:
        zoom 0.3 
        easein 0.50 zoom 1.0 
        easeout 0.25 zoom 0.75 
        easeout 0.10 zoom 0.85 
    parallel:
        pause 0.85
        linear 0.5 alpha 0    
    #0.85s
layeredimage _heart:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (112, 113)
        "_heart_"