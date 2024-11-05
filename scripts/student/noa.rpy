layeredimage noa:
    anchor(0.37, 1)
    ypos 0.05
    zoom 1.5  
    always:
        "images/characters/noa/halo.png"   
    always:
        "images/characters/noa/body.png"      
    group eyes:
        attribute e1 default:
            "images/characters/noa/1.png"
        attribute e2:
            "images/characters/noa/2.png"
        attribute e3:
            "images/characters/noa/3.png"
        attribute e4:
            "images/characters/noa/4.png"
        attribute e5:
            "images/characters/noa/5.png"
        attribute e6:
            "images/characters/noa/6.png"
        attribute e7:
            "images/characters/noa/7.png"
        attribute e8:
            "images/characters/noa/8.png"                            
    group emoticon:
        attribute null default:
            "null"
        attribute action:
            "noa_action"    
        attribute angry:
            "noa_angry"       
        attribute anxiety:
            "noa_anxiety"    
        attribute chat:
            "noa_chat"   
        attribute greenqs:
            "noa_greenqs"        
        attribute heart:
            "noa_heart"
        attribute note:
            "noa_note"     
        attribute redmark:
            "noa_redmark"    
        attribute sad:
            "noa_sad"  
        attribute shy:
            "noa_shy"   
        attribute sigh:
            "noa_sigh"            
        attribute sparkle:
            "noa_sparkle"       
        attribute sweat:
            "noa_sweat"   
        attribute thinking:
            "noa_thinking"   

layeredimage noa_action:
    always:
        pos(100, 90)
        "_action" 
layeredimage noa_angry:
    always:
        pos(180, 120)
        "_angry"
layeredimage noa_anxiety:
    always:
        pos (180, 155)
        "_balloon_N"
    always:
        pos (130, 115)
        "_anxiety"        
#bulb
layeredimage noa_chat:
    always:
        pos (100, 200) 
        "_chat"
layeredimage noa_greenqs:
    always:
        pos(140, 170)
        "_greenqs"
layeredimage noa_heart:
    always:
        pos (180, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (128, 113)
        "_heart" 
layeredimage noa_note:
    always:
        zoom 0.35
        pos (140, 100)
        "_note"        
#orangemark
#orangequestion
layeredimage noa_redmark:
    always:
        pos(180, 130)
        "_redmark"
#redquestion
layeredimage noa_sad:
    always:
        pos(150, 70)
        "_sad_1"
    always:
        pos(165, 80)
        "_sad_2"
    always:
        pos(180, 60)
        "_sad_3"
layeredimage noa_shy:
    always:
        pos (180, 155)
        "_balloon_N"
    always:
        pos (130, 110)
        "_shy"
layeredimage noa_sigh:
    always:
        pos (150, 210)
        "_sigh"
layeredimage noa_sparkle:
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
layeredimage noa_sweat:
    always:
        pos (160, 60)
        "_sweat_1"
    always:
        pos (190, 60)
        "_sweat_2"
#tear
layeredimage noa_thinking:
    always:
        pos (160, 155) 
        "_balloon_T"
    always:
        pos (50, 60)
        "_dot_1"
    always:
        pos (50, 60)
        "_dot_2"
    always:
        pos (50, 60)
        "_dot_3"
#zzz                   