img_w4_1 = "w4_1.png"
img_w5_1 = Pattern("w5_1.png").similar(0.92)
img_w6_1 = Pattern("w6_1.png").similar(0.92)

text_w4_1 = "text_w4_1.png"
text_w5_1 = "text_w5_1.png"
text_w6_1 = "text_w6_1.png"
mat_box =  "1578238799075.png"
M = [text_w4_1, text_w5_1, text_w6_1]
running = True
mat = img_w6_1

while( running ):
    try:
        boxes = findAll(mat_box)
        running = False
    except:
        print("Fuck")
        auto_trader.trade(M)
        flag = 1
        while(flag == 1):
            a = "a.png"
            if exists(a):
                click(a)
            else:
                flag = 0
        
        hover("1579087525768.png")
        wait(1.0)
        keyDown(Key.CTRL)
        keyDown("e")
        wait(1)
        keyUp(Key.CTRL)
        keyUp("e")
if mat == img_w4_1:
    running = True
    while (running):
        boxes = findAll(mat_box)
        for i in boxes:
            hover(i)
            string =  text_w4_1
            if exists( string,1):
                running = False
                doubleClick(i)
                break
        # Trade with mat_container to get Box
        if running :
            auto_trader.trade([string])
            # Open Backpack
            print("Open Backpacks")
            keyDown(Key.CTRL)
            keyDown("e")
            wait(1.0)
            keyUp(Key.CTRL)
            keyUp("e")
elif mat == img_w5_1:
    running = True
    while(running):
        boxes = findAll(mat_box)
        for i in boxes:
            hover(i)     
            string = text_w5_1
            if exists(string, 1):
                running = False
                doubleClick(i)
                break
        if running:
            # Trade with mat_container to get Box
            auto_trader.trade([string])
            # Open Backpack
            print("Open Backpacks")
            keyDown(Key.CTRL)
            keyDown("e")
            wait(1.0)
            keyUp(Key.CTRL)
            keyUp("e")
elif mat ==    img_w6_1:
    running = True
    while(running):
        boxes = findAll(mat_box)
        for i in boxes:
            hover(i)   
            string =text_w6_1
            if exists(string,1):
                running = False
                doubleClick(i)
                break
        if running:
            # Trade with mat_container to get Box
            auto_trader.trade([string])
            wait(0.5)
            # Open Backpack
            print("Open Backpacks")
            keyDown(Key.CTRL)
            keyDown("e")
            wait(1.0)
            keyUp(Key.CTRL)
            keyUp("e")
else:
    raise("Mat_error")