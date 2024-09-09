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
                 