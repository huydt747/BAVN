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
        attribute greenqs:
            "yuuka_greenqs"        
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

layeredimage yuuka_action:
    always:
        pos(105, 90)
        "_action"    
layeredimage yuuka_angry:
    always:
        pos(170, 120)
        "_angry" 
layeredimage yuuka_anxiety:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        pos (114, 115)
        "_anxiety"           
#bulb
layeredimage yuuka_chat:
    always:
        pos (100, 190) 
        "_chat"
layeredimage yuuka_greenqs:
    always:
        pos (130, 170)
        "_greenqs"
layeredimage yuuka_heart:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (112, 113)
        "_heart"
layeredimage yuuka_note:
    always:
        zoom 0.35
        pos (140, 80)
        "_note"        
#orangemark
#orangequestion
layeredimage yuuka_redmark:
    always:
        pos(180, 130)
        "_redmark"
#redquestion
layeredimage yuuka_sad:
    always:
        pos(130, 90)
        "_sad_1"
    always:
        pos(145, 100)
        "_sad_2"
    always:
        pos(160, 80)
        "_sad_3"
layeredimage yuuka_shy:
    always:
        pos (165, 155)
        "_balloon_N"
    always:
        pos (115, 110)
        "_shy" 
layeredimage yuuka_sigh:
    always:
        pos (120, 185)
        "_sigh"
layeredimage yuuka_sparkle:
    always:
        zoom 0.4
        pos (155, 110)
        "_sparkle_1"
    always:
        zoom 0.5
        pos (130, 130)
        "_sparkle_2"
    always:
        zoom 0.5
        pos (155, 150)
        "_sparkle_3"                       
#steam
layeredimage yuuka_sweat:
    always:
        pos (140, 60)
        "_sweat_1"
    always:
        pos (170, 60)
        "_sweat_2"
#tear
layeredimage yuuka_thinking:
    always:
        pos (165, 155)
        "_balloon_T"
    always:
        pos (55, 60)
        "_dot_1"
    always:
        pos (55, 60)
        "_dot_2"
    always:
        pos (55, 60)
        "_dot_3"
#zzz

####################### template for my uses
#bulb

#greenqs

#orangemark
#orangequestion

#redquestion

#steam

#tear

#zzz