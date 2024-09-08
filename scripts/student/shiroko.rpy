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
    ypos 0.1 
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
                       