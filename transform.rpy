# all transform only affect characters or objects
# mọi transform chỉ ảnh hưởng đến nhân vật hoặc đổi tượng

# how to use: syntax: show <student_name> at <name_of_transform>
#            ex:     show yuuka at hidden
# cách dùng: cú pháp: show <tên_học_sinh> at <tên_transform>
#           vd:      show yuuka at hidden


# silhouette of the character
# hình bóng đen của nhân vật
transform hidden: 
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 

# turn silhouette to fully shown
# chuyển bóng đen sang ảnh rõ ràng
transform hiddentoshow:
    subpixel True 
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 
    easeout 0.50 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
transform showtohidden:
    subpixel True 
    matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(0.0)*HueMatrix(0.0) 
    easeout 0.50 matrixcolor InvertMatrix(0.0)*ContrastMatrix(1.0)*SaturationMatrix(1.0)*BrightnessMatrix(-1.0)*HueMatrix(0.0) 

# bounce down once
# nhún xuống 1 lần
transform bouncedown1:
    subpixel True 
    ease 0.50 yoffset 50
    linear 0.10 yoffset 50 
    easein 0.30 yoffset 0 

# nhún xuống 2 lần
# double bounce down
transform bouncedown2:
    subpixel True 
    ease 0.50 yoffset 50 
    linear 0.10 yoffset 50 
    easein 0.30 yoffset 0 
    linear 0.1 yoffset 0
    ease 0.50 yoffset 50 
    linear 0.10 yoffset 50
    easein 0.4 yoffset 0

# bounce up once
# nhún lên 1 lần
transform bounceup1:
    subpixel True 
    easeout 0.2 yoffset -50 
    easein 0.2 yoffset 0 

# double up down
# nhún lên 2 lần
transform bounceup2: #0.5
    subpixel True 
    easeout 0.2 yoffset -50 
    easein 0.2 yoffset 0 
    easeout 0.2 yoffset -50 
    easein 0.2 yoffset 0 



# move the character from current position to your ideal position, all predefined
# di chuyển nhân vật từ vị trí hiện tại, đến vị trí kia mà bạn muốn, tất cả đã định sẵn
transform x1: #phía trái ngoài màn hình, left most out of screen
    subpixel True 
    easein 1.00 xpos -1.0
transform x2: # phía trái, khuyến nghị dùng/left, recommend position
    subpixel True 
    easein 1.00 xpos 0.2 
transform x3:
    subpixel True 
    easein 1.00 xpos 0.3
transform x4:
    subpixel True
    easein 0.5 xpos 0.4
transform x5: # chính giữa, khuyến nghị dùng/Middle, recommend position
    subpixel True
    easein 0.5 xpos 0.5 
transform x6:
    subpixel True
    easein 0.5 xpos 0.6     
transform x7:
    subpixel True
    easein 0.5 xpos 0.7 
transform x8: # phía phải, khuyến nghị dùng/Right, recommend position
    subpixel True
    easein 0.5 xpos 0.8 
transform x9: # phía phải ngoài màn hình, right most out of screen
    subpixel True 
    easein 1.00 xpos 2.0
transform zoomin:
    zoom 1.3
transform zoomout:
    zoom 1.0            

# hiệu ứng lắc, khuyến nghị dùng cho nhân vật
# shake effect, recommend to use with character
transform shake:
    subpixel True 
    xoffset 0
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5 
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5 
    linear 0.05 xoffset 5
    linear 0.05 xoffset -5 
    linear 0.05 xoffset 5
    linear 0.05 xoffset 0 

