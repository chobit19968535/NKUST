from sikuli import *
def trade(X, chest_flag):
    mat_locate = Location(228, 278)
    maker_locate = Location(229, 100)
    page1 = "page1.png"
    page2 = "page2.png"
    pages = [page1, page2]
    
    mat_box = "1579049773957.png"
    trade_icon1 = "trade_icon1.png"
    trade_icon2 = "trade_icon2.png"
    click("1578775575481.png")
    wait(0.25)
    click("1578775585587.png")
    wait(0.25)
    click(trade_icon1)
    game = "game.png"
    hover(game)
    wait(2)
    click(mat_locate) # windows of mat_container
    while(len(X) != 0 ):
        goal = X[0]
        if goal == "1578239824046.png":
            mat_box = "sugar_img.png"
        try:
            results = findAll(mat_box)
        except:
            # Close all windows
            running = 1
            while ( running ):
                if exists("icon_-.png"):
                    click("icon_-.png")
                else:
                    running = 0
            # Open backpack
            print("Open Backpacks")
            wait(0.25)
            keyDown(Key.CTRL)
            keyDown("e")
            wait(1.0)
            keyUp(Key.CTRL)
            keyUp("e")
            # Open Chest
            doubleClick("chest_icon.png")
            wait(0.5)
            # Get mat_box from Chest
            flag = 0
            for p in pages:
                click(p)
                wait(2)
                if exists (mat_box):
                    candicates = findAll(mat_box)
                    for c in candicates:
                        hover(c)
                        wait(0.25)
                        if exists(goal, 0.5):
                            doubleClick(c)
                            print("x_sort:", X)
                            print("success", goal)
                            click("chest_ok.png")
                            flag = 1
                            break
                    if flag == 1:
                        break
                else:
                    continue
            hover(game)
            wait(2)
            click(maker_locate) # windows of Producter
            click("1578775575481.png")
            wait(0.25)
            click("1578775585587.png")
            wait(0.25)
            click(trade_icon1)
            hover(game)
            wait(2)
            click(mat_locate) # windows of mat_container
            continue
        for j in results:
            hover(j)
            if exists(goal, 0.5):
                doubleClick(j)
                del X[0]
                wait(1)
                break    
    wait(0.3)
    click(trade_icon1)
    wait(0.3) 
    click(trade_icon2)
    hover(game)
    wait(2)
    click(maker_locate) # windows of Producter
    wait(0.3)
    click(trade_icon2)
    hover("1594962436409.png")
    type("/re" + Key.ENTER)
    return()