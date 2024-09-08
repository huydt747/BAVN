label demo:
    scene bg classroom2
    "Tôi cố gắng đến sớm để khỏi bị Yuuka cằn nhằn. Tuy nhiên, khi tôi đến đây, không có ai ở đây cả."
    ss "Kì thật, bõ công đến sớm..."
    "Sau đó, tôi thấy bóng của ai đó ngoài cửa đang lấp ló vào trong."
    show yuuka at hidden:
        xpos 1.3
    show yuuka at hidden:
        subpixel True 
        xpos 1.3 
        ease 1.00 xpos 0.5 
    pause 1
    show yuuka at hiddentoshow
    pause 0.5
    show yuuka loud
    play music "bgm/Theme_15.ogg" fadein 1.0 
    yk "Ô, là Sensei. Em chào thầy."
    show yuuka null
    show yuuka e8
    yk "Hmm? Nay thầy biết lên đúng giờ à? Ghê vậy."
    ss "Thế bữa giờ em nghĩ xấu về thầy à?"
    ss "Mà mọi người đâu hết rồi em?"
    show yuuka e6
    show yuuka redmark
    yk "Ủa."
    show yuuka null
    yk "Em tưởng là giờ này. Đợi tí, em kiểm tra điện thoại."
    show yuuka at shake
    ss "(Tự nhiên Yuuka cảm thấy đáng sợ,... mình không nên hỏi thì-)"
    stop music fadeout 0.5
    show yuuka at bounceup
    pause 0.5
    show yuuka angry
    play music "bgm/Theme_07.ogg" fadein 1.0
    yk "Làm ăn kiểu gì vậy? Đợi đến 3 giờ sáng mới thông báo đổi lịch?"
    show yuuka null
    yk "Giờ đó đang ngủ với lại sáng ai thèm coi thông báo."
    show yuuka e3
    stop music fadeout 0.5
    pause 0.5
    play music "bgm/Theme_86.ogg" fadein 1.0
    yk "Em xin lỗi Sensei, tại em không chuyển tin nhắn cho thầy biết, lại làm thầy tốn thời gian..."
    ss "Không có gì là không tốn cả..."
    ss "Chơi bài không em?"
    show yuuka e2
    yk "Bài à? Lâu lắm rồi em mới có dịp chơi..."
    show yuuka e6
    yk "À khoan, lần trước thầy ăn gian một lần."
    yk "Thầy bỏ áo khoác ra thì chơi."
    ss "(Tôi bỏ áo khoác và tiện bỏ vài cúc áo sơ mi để chọc em ấy.)"
    show yuuka e1 at shake
    yk "Sensei! Ai bảo thầy cởi áo đó, áo khoác thôi!"
    yk "Mồ!!!"
    stop music fadeout 1.0
    scene black with fade
    scene bg classroom2 with fade
    show yuuka e3 at hidden:
        xpos 0.5 
    pause 0.1
    show yuuka at hiddentoshow
    pause 0.5
    show yuuka e2
    play music "bgm/Theme_16.ogg" fadein 1
    "Thầy thích xì dách đúng không, phát bài đi."
    show yuuka e3
    show yuuka at bouncedown
    "..."
    scene black with fade
    show yuuka e3
    show yuuka thinking
    yk "Mình được 17 điểm. Mình chỉ có thể thắng khi thầy quắc hoặc dằn dơ. Cửa thắng là quá nhỏ."
    yk "Nếu thầy có 16, chắc chắn là sẽ rút, mình thấy ai cũng chơi như vậy."
    yk "Có lẽ mình cũng nên rút, 17 vẫn là quá nhỏ nếu theo tỉ lệ trung bình. Cả hai đều quắc thì ít nhất được hòa."
    scene bg classroom2 with fade
    show yuuka e2
    yk "Em muốn rút."
    show yuuka e3
    yk "..."
    scene black with fade
    show yuuka e3
    yk "Bà mẹ... Quắc thật."
    yk "Mình phải dùng chiêu đánh tâm lí."
    show yuuka e8
    yk "Giả bộ mỉm cười một cái. Thầy sẽ biết mình có con bài to và chắc chắn sẽ rút."
    scene bg classroom2 with fade
    show yuuka loud
    yk "Em dằn!"
    show yuuka null
    show yuuka e8
    yk "(Để xem thầy diễn như nào.)"
    stop music fadeout 1.0
    ss "Lật bài đi em."
    show yuuka e6 redmark
    yk "Hả?"
    show yuuka null
    play music "bgm/Theme_07.ogg" fadein 1.0
    ss "Quắc... Hahahahaha..."
    show yuuka e1 at shake
    yk "Cười cái gì, cho em xem bài coi!"
    show yuuka at bouncedown
    yk "16... Không thể nào... Sao thầy dám dằn dơ thế này?"
    show yuuka at bounceup:
        zoom 1.2
    "Thôi không chơi nữa, em nghỉ!"
    show yuuka e1 null:
        subpixel True 
        xpos 0.5 
        easein 0.50 xpos 1.3 
    ss "..."
    ss "Sao con gái thời nay bị gì ấy nhỉ."
    "Yuuka rời đi, tôi cất bộ bài và đi về."
    stop music fadeout 3.0
    scene black with fade
    pause
    return
