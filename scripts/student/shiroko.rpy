image shrk body = "images/characters/shiroko/body.png"
image shrk halo = "images/characters/shiroko/halo.png"
image shrk 1 = "images/characters/shiroko/1.png"
image shrk 2 = "images/characters/shiroko/2.png"
image shrk 3 = "images/characters/shiroko/3.png"
image shrk 4 = "images/characters/shiroko/4.png"
image shrk 5 = "images/characters/shiroko/5.png"
image shrk 6 = "images/characters/shiroko/6.png"
image shrk 7 = "images/characters/shiroko/7.png"

layeredimage shiroko:
    anchor(0.5, 0)
    ypos 0.05
    xpos 0.46   
    zoom 1.6
    always:
        "shrk halo"
    always:
        "shrk body"
    group eyes:
        attribute e1 default:
            "shrk 1"  
        attribute e2:
            "shrk 2"  
        attribute e3:
            "shrk 3"  
        attribute e4:
            "shrk 4"  
        attribute e5:
            "shrk 5"  
        attribute e6:
            "shrk 6"  
        attribute e7:
            "shrk 7"  
    group emoticon:
        attribute null default:
            "null"
        attribute action:
            "shiroko_action"    
        attribute angry:
            "shiroko_angry"       
        attribute anxiety:
            "shiroko_anxiety"    
        attribute chat:
            "shiroko_chat"
        attribute greenqs:
            "shiroko_greenqs"           
        attribute heart:
            "shiroko_heart"
        attribute note:
            "shiroko_note"     
        attribute redmark:
            "shiroko_redmark"    
        attribute sad:
            "shiroko_sad"  
        attribute shy:
            "shiroko_shy"   
        attribute sigh:
            "shiroko_sigh"            
        attribute sparkle:
            "shiroko_sparkle"       
        attribute sweat:
            "shiroko_sweat"   
        attribute thinking:
            "shiroko_thinking"    
                       
image shiroko_halo:
    "shrk halo"
    subpixel True 
    ease 5.00 yoffset -3
    ease 5.00 yoffset 3 
    repeat
layeredimage shiroko_halo_animated:
    always:
        "shiroko_halo"

layeredimage shiroko_action:
    always:
        pos(130, 90)
        "_action"
layeredimage shiroko_angry:
    always:
        pos(230, 120)
        "_angry"                                        
layeredimage shiroko_anxiety:
    always:
        pos (200, 155)
        "_balloon_N"
    always:
        pos (150, 115)
        "_anxiety"
#bulb
layeredimage shiroko_chat:
    always:
        pos (140, 200) 
        "_chat"
layeredimage shiroko_greenqs:
    always:
        pos (170, 170)
        "_greenqs"
layeredimage shiroko_heart:
    always:
        pos (200, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (148, 113)
        "_heart"
layeredimage shiroko_note:
    always:
        zoom 0.35
        pos (160, 100)
        "_note"        
#orangemark
#orangequestion
layeredimage shiroko_redmark:
    always:
        pos(210, 130)
        "_redmark"
#redquestion
layeredimage shiroko_sad:
    always:
        pos(180, 90)
        "_sad_1"
    always:
        pos(195, 100)
        "_sad_2"
    always:
        pos(210, 80)
        "_sad_3"
layeredimage shiroko_shy:
    always:
        pos (210, 155)
        "_balloon_N"
    always:
        pos (160, 110)
        "_shy"
layeredimage shiroko_sigh:
    always:
        pos (170, 200)
        "_sigh" 
layeredimage shiroko_sparkle:
    always:
        zoom 0.4
        pos (185, 110)
        "_sparkle_1"
    always:
        zoom 0.5
        pos (160, 130)
        "_sparkle_2"
    always:
        zoom 0.5
        pos (185, 150)
        "_sparkle_3"                       
#steam
layeredimage shiroko_sweat:
    always:
        pos (190, 60)
        "_sweat_1"
    always:
        pos (220, 60)
        "_sweat_2"
#tear
layeredimage shiroko_thinking:
    always:
        pos (210, 155) 
        "_balloon_T"
    always:
        pos (100, 60)
        "_dot_1"
    always:
        pos (100, 60)
        "_dot_2"
    always:
        pos (100, 60)
        "_dot_3"
#zzz                