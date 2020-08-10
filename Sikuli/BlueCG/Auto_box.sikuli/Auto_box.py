wait(3)
count = 0
A1_img = "A1_img.png"
A2_img = "A2_img.png"
A3_img = "A3_img.png"
A1_flag = 1
A2_flag = 1
A3_flag = 1
trade_icon = "1581328317600.png"
try_icon = "1581341104279.png"
skill_icon = "skill_icon.png"
timmer = 0
period = 61
limited = 432
while( timmer != limited):
    # init
    hover(trade_icon)
    wait(60)
    box = findAll(Pattern("1581327698068.png").similar(0.95))
    for i in box:
        doubleClick(i)
        wait(0.3)
        hover(trade_icon)
        wait(0.1)
    count +=1
    wait(0.5)
    # Recover FP
    if count == period:
        count = 0
        running = 1
        while( running ):
            try:
                wait(0.5)
                kuo = find("1581327886066.png")
                if A1_flag == 1:
                    doubleClick(kuo)
                    wait(0.5)
                    click(A1_img)
                    hover(trade_icon)
                    click(A1_img)
                    # Open Backpack
                    print("Open Backpacks")
                    keyDown(Key.CTRL)
                    keyDown("e")
                    wait(1.0)
                    keyUp(Key.CTRL)
                    keyUp("e")
                    A1_flag = 0
                    
                if A2_flag == 1:
                    doubleClick(kuo)
                    wait(0.5)
                    click(A2_img)
                    hover(trade_icon)
                    click(A2_img)
                    # Open Backpack
                    print("Open Backpacks")
                    keyDown(Key.CTRL)
                    keyDown("e")
                    wait(1.0)
                    keyUp(Key.CTRL)
                    keyUp("e")
                    A2_flag = 0
                    
                if A3_flag == 1:
                    doubleClick(kuo)
                    wait(0.5)
                    click(A3_img)
                    hover(trade_icon)
                    click(A3_img)
                    # Open Backpack
                    print("Open Backpacks")
                    keyDown(Key.CTRL)
                    keyDown("e")
                    wait(1.0)
                    keyUp(Key.CTRL)
                    keyUp("e")
                    A3_flag = 0
                if A1_flag == 0 and A2_flag == 0 and A3_flag == 0:
                    running = 0
            except:
                # Open Kuo from Box
                kuo_box = find("1581328114185.png")
                doubleClick(kuo_box)
                wait(1.8)
        # Reset Flags
        running = 1 
        A1_flag = 1
        A2_flag = 1
        A3_flag = 1
    # Open skill_window
    if exists(skill_icon):
        res = findAll(skill_icon)
        for i in res:
            click(i)
            wait(0.25)
    # Active Skills
    if exists(try_icon):
        res = findAll(try_icon)
        for i in res:
            click(i)
            wait(0.25)
    timmer += 1