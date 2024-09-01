image ayn body = "images/characters/ayane/body.png"
image ayn halo = "images/characters/ayane/halo.png"
image ayn glasses = "images/characters/ayane/glasses.png"
image ayn 1 = "images/characters/ayane/1.png"
image ayn 2 = "images/characters/ayane/2.png"
image ayn 3 = "images/characters/ayane/3.png"
image ayn 4 = "images/characters/ayane/4.png"
image ayn 5 = "images/characters/ayane/5.png"
image ayn 6 = "images/characters/ayane/6.png"
image ayn 7 = "images/characters/ayane/7.png"
image ayn 8 = "images/characters/ayane/8.png"
image ayn 9 = "images/characters/ayane/9.png"
image ayn 10 = "images/characters/ayane/10.png"
image ayn 11 = "images/characters/ayane/11.png"
image ayn 12 = "images/characters/ayane/12.png"
image ayn 13 = "images/characters/ayane/13.png"
image ayn 14 = "images/characters/ayane/14.png"
image ayn 15 = "images/characters/ayane/15.png"
image ayn 16 = "images/characters/ayane/16.png"

layeredimage ayane:
    anchor(0.5, 1)
    ypos 0
    zoom 1.7
    always:
        "ayn halo"   
    always:
        "ayn body"      
    group eyes:
        attribute e1 default:
            "ayn 1"
        attribute e2:
            "ayn 2"    
        attribute e3:
            "ayn 3"   
        attribute e4:
            "ayn 4"   
        attribute e5:
            "ayn 5"   
        attribute e6:
            "ayn 6"   
        attribute e7:
            "ayn 7"   
        attribute e8:
            "ayn 8"   
        attribute e9:
            "ayn 9"   
        attribute e10:
            "ayn 10"   
        attribute e11:
            "ayn 11"   
        attribute e12:
            "ayn 12"   
        attribute e13:
            "ayn 13"   
        attribute e14:
            "ayn 14"   
        attribute e15:
            "ayn 15"   
        attribute e16:
            "ayn 16"  
    group glasses:
        attribute on default:
            "ayn glasses"   
        attribute off:
            "null"                 
    group emoticon:
        attribute null default:
            "null"
        attribute action:
            "ayane_action"    
        attribute angry:
            "ayane_angry"       
        attribute anxiety:
            "ayane_anxiety"    
        attribute chat:
            "ayane_chat"       
        attribute heart:
            "ayane_heart"
        attribute note:
            "ayane_note"     
        attribute redmark:
            "ayane_redmark"    
        attribute sad:
            "ayane_sad"  
        attribute shy:
            "ayane_shy"   
        attribute sigh:
            "ayane_sigh"            
        attribute sparkle:
            "ayane_sparkle"       
        attribute sweat:
            "ayane_sweat"   
        attribute thinking:
            "ayane_thinking"    
           