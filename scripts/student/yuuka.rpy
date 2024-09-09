image yk body = "images/characters/yuuka/body.png"
image yk halo = "images/characters/yuuka/halo.png"
image yk 2 = "images/characters/yuuka/2.png"
image yk 3 = "images/characters/yuuka/3.png"
image yk 4 = "images/characters/yuuka/4.png"
image yk 5 = "images/characters/yuuka/5.png"
image yk 6 = "images/characters/yuuka/6.png"
image yk 7 = "images/characters/yuuka/7.png"
image yk 8 = "images/characters/yuuka/8.png"
image yk 1 = "images/characters/yuuka/1.png"

image null1 = "images/emoticon/null.png"

#for testing
# layeredimage null2:
#     anchor(0.5, 0.5)
#     ypos 1
#     zoom 1.7
#     always:
#         "null1"
#     group emoticon:
#         attribute null default:
#             "null"
#         attribute thinking:
#             "_thinking"      
layeredimage yuuka:
    anchor(0.5, 1)
    ypos 0
    zoom 1.7
    always:
        "yk halo" 
    always:
        "yk body"   
    group eyes:
        attribute e2 default: #neutral 1
            "yk 2"
        attribute e1: #embarass
            "yk 1"
        attribute e3: #neutral close eyes
            "yk 3"
        attribute e4: #scare
            "yk 4"
        attribute e5: #neutral 2
            "yk 5"
        attribute e6: #feeling sus
            "yk 6"
        attribute e7: #smile
            "yk 7"
        attribute e8: #smug
            "yk 8"      
    group emoticon:
        attribute null default:
            "null"
        attribute action:
            "yuuka_action"    
        attribute angry:
            "yuuka_angry"       
        attribute anxiety:
            "yuuka_anxiety"    
        attribute chat:
            "yuuka_chat"       
        attribute heart:
            "yuuka_heart"
        attribute note:
            "yuuka_note"     
        attribute redmark:
            "yuuka_redmark"    
        attribute sad:
            "yuuka_sad"  
        attribute shy:
            "yuuka_shy"   
        attribute sigh:
            "yuuka_sigh"            
        attribute sparkle:
            "yuuka_sparkle"       
        attribute sweat:
            "yuuka_sweat"   
        attribute thinking:
            "yuuka_thinking"    
           
# Halo chuyển động           
image yuuka_halo:
    "yk halo"
    subpixel True 
    ease 5.00 yoffset -3
    ease 5.00 yoffset 3 
    repeat
layeredimage yuuka_halo_animated:
    always:
        "yuuka_halo"
                 