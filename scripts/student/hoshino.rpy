image hsn body = "images/characters/hoshino/body.png"
image hsn bang = "images/characters/hoshino/bang.png"
image hsn halo1 = "images/characters/hoshino/halo1.png"
image hsn halo2 = "images/characters/hoshino/halo2.png"
image hsn halo3 = "images/characters/hoshino/halo3.png"
image hsn 1 = "images/characters/hoshino/1.png"
image hsn 2 = "images/characters/hoshino/2.png"
image hsn 3 = "images/characters/hoshino/3.png"
image hsn 4 = "images/characters/hoshino/4.png"
image hsn 5 = "images/characters/hoshino/5.png"
image hsn 6 = "images/characters/hoshino/6.png"
image hsn 7 = "images/characters/hoshino/7.png"
image hsn 8 = "images/characters/hoshino/8.png"
image hsn 9 = "images/characters/hoshino/9.png"
image hsn 10 = "images/characters/hoshino/10.png"
image hsn 11 = "images/characters/hoshino/11.png"
image hsn 12 = "images/characters/hoshino/12.png"
image hsn 13 = "images/characters/hoshino/13.png"
image hsn 14 = "images/characters/hoshino/14.png"
image hsn 15 = "images/characters/hoshino/15.png"
image hsn 16 = "images/characters/hoshino/16.png"
image hsn 17 = "images/characters/hoshino/17.png"
image hsn 18 = "images/characters/hoshino/18.png"
image hsn 19 = "images/characters/hoshino/19.png"

layeredimage hoshino:
    anchor(0.5, 0)
    ypos 0.1    
    zoom 1.5
    always:
        "hsn halo1"
    always:    
        "hsn halo2"
    always:    
        "hsn halo3"   
    always:
        "hsn body"    
    group eyes:
        attribute e1 default:
            "hsn 1"
        attribute e2:
            "hsn 2"    
        attribute e3:
            "hsn 3" 
        attribute e4:
            "hsn 4"      
        attribute e5:
            "hsn 5"  
        attribute e6:
            "hsn 6"      
        attribute e7:
            "hsn 7"    
        attribute e8:
            "hsn 8" 
        attribute e9:
            "hsn 9"      
        attribute e10:
            "hsn 10"  
        attribute e11:
            "hsn 11"
        attribute e12:
            "hsn 12"    
        attribute e13:
            "hsn 13" 
        attribute e14:
            "hsn 14"      
        attribute e15:
            "hsn 15"  
        attribute e16:
            "hsn 16"
        attribute e17:
            "hsn 17"    
        attribute e18:
            "hsn 18" 
        attribute e19:
            "hsn 19"      
    always:
        "hsn bang"
    group emoticon:
        attribute null default:
            "null"
        attribute action:
            "hoshino_action"    
        attribute angry:
            "hoshino_angry"       
        attribute anxiety:
            "hoshino_anxiety"    
        attribute chat:
            "hoshino_chat"       
        attribute heart:
            "hoshino_heart"
        attribute note:
            "hoshino_note"     
        attribute redmark:
            "hoshino_redmark"    
        attribute sad:
            "hoshino_sad"  
        attribute shy:
            "hoshino_shy"   
        attribute sigh:
            "hoshino_sigh"            
        attribute sparkle:
            "hoshino_sparkle"       
        attribute sweat:
            "hoshino_sweat"   
        attribute thinking:
            "hoshino_thinking"    
           