image nnm body = "images/characters/nonomi/body.png"
image nnm bang = "images/characters/nonomi/bang.png"
image nnm halo1 = "images/characters/nonomi/halo1.png"
image nnm halo2 = "images/characters/nonomi/halo2.png"
image nnm 1 = "images/characters/nonomi/1.png"
image nnm 2 = "images/characters/nonomi/2.png"
image nnm 3 = "images/characters/nonomi/3.png"
image nnm 4 = "images/characters/nonomi/4.png"
image nnm 5 = "images/characters/nonomi/5.png"
image nnm 6 = "images/characters/nonomi/6.png"
image nnm 7 = "images/characters/nonomi/7.png"
image nnm 8 = "images/characters/nonomi/8.png"
image nnm 9 = "images/characters/nonomi/9.png"
image nnm 10 = "images/characters/nonomi/10.png"
image nnm 11 = "images/characters/nonomi/11.png"
image nnm 12 = "images/characters/nonomi/12.png"
image nnm 13 = "images/characters/nonomi/13.png"
image nnm 14 = "images/characters/nonomi/14.png"
image nnm 15 = "images/characters/nonomi/15.png"
image nnm 16 = "images/characters/nonomi/16.png"
image nnm 17 = "images/characters/nonomi/17.png"
image nnm 18 = "images/characters/nonomi/18.png"
image nnm 19 = "images/characters/nonomi/19.png"

layeredimage nonomi:
    anchor(0.35, 1)
    ypos 0.05    
    xpos 0.50
    zoom 1.7
    always:
        "nnnm halo2"
    always:
        "nnnm halo1"    
    always:
        "nnm body"   
    group eyes:
        attribute e1 default:
            "nnm 1"
        attribute e2:
            "nnm 2"
        attribute e3:
            "nnm 3"
        attribute e4:
            "nnm 4"
        attribute e5:
            "nnm 5"
        attribute e6:
            "nnm 6"   
        attribute e7:
            "nnm 7"
        attribute e8:
            "nnm 8"
        attribute e9:
            "nnm 9"
        attribute e10:
            "nnm 10"
        attribute e11:
            "nnm 11"  
        attribute e12:
            "nnm 12"
        attribute e13:
            "nnm 13"
        attribute e14:
            "nnm 14"
        attribute e15:
            "nnm 15"
        attribute e16:
            "nnm 16"  
        attribute e17:
            "nnm 17"
        attribute e18:
            "nnm 18"
        attribute e19:
            "nnm 19"                         
    always:
        "nnm bang"    
    group emoticon:
        attribute null default:
            "null"
        attribute action:
            "nonomi_action"    
        attribute angry:
            "nonomi_angry"       
        attribute anxiety:
            "nonomi_anxiety"    
        attribute chat:
            "nonomi_chat"       
        attribute heart:
            "nonomi_heart"
        attribute note:
            "nonomi_note"     
        attribute redmark:
            "nonomi_redmark"    
        attribute sad:
            "nonomi_sad"  
        attribute shy:
            "nonomi_shy"   
        attribute sigh:
            "nonomi_sigh"            
        attribute sparkle:
            "nonomi_sparkle"       
        attribute sweat:
            "nonomi_sweat"   
        attribute thinking:
            "nonomi_thinking"    
                   
image nonomi_halo1:
    "nnm halo1"
    subpixel True 
    pause 0.5
    ease 5.00 yoffset -3
    ease 5.00 yoffset 3 
    repeat
image nonomi_halo2:
    "nnm halo2"
    subpixel True 
    ease 5.00 yoffset -3
    ease 5.00 yoffset 3 
    repeat

layeredimage nonomi_halo_animated:
    always:
        "nonomi_halo1"
    always:
        "nonomi_halo2"
                                