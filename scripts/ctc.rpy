image ctc = "gui/ctc.png"
screen ctc(arg=None):

    frame:
        at ctc_appear
        background "gui/ctc.png"

transform ctc_appear:
    subpixel True 
    pos (1800, 1000)
    easeout_quad 0.40 ypos 1030 
    linear 0.05 ypos 1030 
    easein_quart 0.35 ypos 1000 
    linear 0.20 ypos 1000 
    repeat
