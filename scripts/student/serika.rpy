image srk body = "images/characters/serika/body.png"
image srk halo = "images/characters/serika/halo.png"
image srk 1 = "images/characters/serika/1.png"
image srk 2 = "images/characters/serika/2.png"
image srk 3 = "images/characters/serika/3.png"
image srk 4 = "images/characters/serika/4.png"
image srk 5 = "images/characters/serika/5.png"
image srk 6 = "images/characters/serika/6.png"
image srk 7 = "images/characters/serika/7.png"
image srk 8 = "images/characters/serika/8.png"
image srk 9 = "images/characters/serika/9.png"
image srk 10 = "images/characters/serika/10.png"
image srk 11 = "images/characters/serika/11.png"
image srk 12 = "images/characters/serika/12.png"
image srk 13 = "images/characters/serika/13.png"
image srk 14 = "images/characters/serika/14.png"

layeredimage serika:
    anchor(0.5, 1)
    ypos 0.05
    zoom 1.7
    always:
        "srk halo"
    always:
        "srk body"
    group eyes:
        attribute e1 default: #smile
            "srk 1"    
        attribute e2: #shout
            "srk 2"
        attribute e3: #worry 1
            "srk 3"
        attribute e4: #talking neutral 1
            "srk 4"
        attribute e5: #talking neutral 2
            "srk 5"
        attribute e6: #laugh
            "srk 6"
        attribute e7: #talking neutral 3
            "srk 7"
        attribute e8: #worry 2
            "srk 8"
        attribute e9: #close eyes
            "srk 9"
        attribute e10: #angry 1
            "srk 10"
        attribute e11: #annoy
            "srk 11"
        attribute e12: #neutral
            "srk 12"
        attribute e13: #angry 2
            "srk 13"
        attribute e14: #embrass
            "srk 14"           
    group emotion:
        attribute null default:
            "null"
        attribute action:
            "serika_action"    
        attribute angry:
            "serika_angry"       
        attribute anxiety:
            "serika_anxiety"    
        attribute chat:
            "serika_chat"       
        attribute heart:
            "serika_heart"
        attribute note:
            "serika_note"     
        attribute redmark:
            "serika_redmark"    
        attribute sad:
            "serika_sad"  
        attribute shy:
            "serika_shy"   
        attribute sigh:
            "serika_sigh"            
        attribute sparkle:
            "serika_sparkle"       
        attribute sweat:
            "serika_sweat"   
        attribute thinking:
            "serika_thinking"    
                
image serika_halo:
    "srk halo"
    subpixel True 
    ease 5.00 yoffset -3
    ease 5.00 yoffset 3 
    repeat
layeredimage serika_halo_animated:
    always:
        "serika_halo"
                 
layeredimage serika_action:
    always:
        pos(105, 90)
        "_action"    
layeredimage serika_angry:
    always:
        pos(180, 120)
        "_angry"    
layeredimage serika_anxiety:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        pos (114, 115)
        "_anxiety"  
#bulb
layeredimage serika_chat:
    always:
        pos (120, 190) 
        "_chat"
#greenqs da lam
layeredimage serika_heart:
    always:
        pos (164, 155)
        "_balloon_N"
    always:
        zoom 0.5
        pos (112, 113)
        "_heart"
layeredimage serika_note:
    always:
        zoom 0.35
        pos (140, 80)
        "_note"
#orange mark
#orange question
layeredimage serika_redmark:
    always:
        pos(180, 130)
        "_redmark"
#red question
layeredimage serika_sad:
    always:
        pos(160, 90)
        "_sad_1"
    always:
        pos(175, 100)
        "_sad_2"
    always:
        pos(190, 80)
        "_sad_3"
layeredimage serika_shy:
    always:
        pos (165, 155)
        "_balloon_N"
    always:
        pos (112, 110)
        "_shy"
layeredimage serika_sigh:
    always:
        pos (150, 185)
        "_sigh"
layeredimage serika_sparkle:
    always:
        zoom 0.4
        pos (175, 110)
        "_sparkle_1"
    always:
        zoom 0.5
        pos (150, 130)
        "_sparkle_2"
    always:
        zoom 0.5
        pos (175, 150)
        "_sparkle_3"                
#steam
layeredimage serika_sweat:
    always:
        pos (160, 60)
        "_sweat_1"
    always:
        pos (190, 60)
        "_sweat_2"
#tear
layeredimage serika_thinking:
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