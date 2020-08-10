from sikuli import *
import auto_trader
import skill_window

def open_box(mat, rank, method, chest_flag):
    def mat_check(mat):
        icon = "icon.png"
        for index, val in enumerate(img_list):
            if (val == mat):
                if val == img_h6_1:
                    running = 1
                    hover(icon)
                    wait(0.25)
                    if exists (img_h6_1):
                        condidates = find(val)
                        doubleClick(condidates)
                        wait(0.7)
                        doubleClick(condidates)
                        wait(0.3)
                        type("/re" + Key.ENTER)
                        break
                    else:
                        # Trade with mat_container to get Box
                        string =  text_list[index]
                        auto_trader.trade([string],chest_flag)
                        # Open Backpack
                        print("Open Backpacks")
                        keyDown(Key.CTRL)
                        keyDown("e")
                        wait(1.0)
                        keyUp(Key.CTRL)
                        keyUp("e")
                        # Open sugar 
                        condidates = find(val)
                        doubleClick(condidates)
                        wait(0.7)
                        doubleClick(condidates)
                        wait(0.3)
                        type("/re" + Key.ENTER)
                        break
                running = True
                while (running):
                    hover("logo.png")
                    wait(0.3)
                    boxes = findAll(mat_box)
                    for i in boxes:
                        hover(i)
                        string =  text_list[index]
                        if exists( string,1):
                            running = False
                            doubleClick(i)
                            break
                    # Trade with mat_container to get Box
                    if running :
                        auto_trader.trade([string],chest_flag)
                        # Open Backpack
                        print("Open Backpacks")
                        keyDown(Key.CTRL)
                        keyDown("e")
                        wait(1.0)
                        keyUp(Key.CTRL)
                        keyUp("e")
        return()
        
    mat_box =  "1578238799075.png"
    ##### Texts ######
    text_h1_3 = "text_h1_3.png"
    text_h1_4 = "1578675333208.png"
    text_h2_1 = "text_h2_1.png"
    text_h2_2 = "1578675354944.png"
    text_h3_1 = "1578239688504.png"
    text_h3_2 = Pattern("1578239742771.png").similar(0.50)
    text_h4_3 = "text_h4_3.png"
    text_h4_4 = "1578542482103.png"
    text_h5_1 = Pattern("1578239774858.png").similar(0.50)
    text_h5_4 = "1595052549070.png"
    text_h5_5 = Pattern("1578542460520.png").similar(0.80)
    text_h6_1 = "1578239824046.png"
    text_h6_2 = "1578542392435.png"
    text_h7_2 = "text_h7_2.png"
    text_h7_3 = "1578542495348.png"
    text_h8_1 = "text_h8_1.png"
    text_h9_1 = "text_h9_1.png"
    text_h9_2 = "text_h9_2.png"
    text_h10_1= "1595052709020.png"

    text_w4_1 = "text_w4_1.png"
    text_w5_1 = "text_w5_1.png"
    text_w6_1 = "text_w6_1.png"
    text_list = [text_h1_3, text_h1_4, text_h2_1, text_h2_2, text_h3_1, text_h3_2, text_h4_3, text_h4_4, text_h5_1, text_h5_4, text_h5_5, text_h6_1, text_h6_2, text_h7_2, text_h7_3, text_h8_1, text_h9_1, text_h9_2, text_h10_1
                    ,text_w4_1, text_w5_1, text_w6_1]

    ###### Images #####
    img_h1_3 = "h1_3.png"
    img_h1_4 =  "h1_4.png"
    img_h2_1 =  "h2_1.png"
    img_h2_2 =  "h2_2.png"
    img_h3_1 =  "h3_1.png"
    img_h3_2 =  "h3_2.png"
    img_h4_3 = "h4_3.png"
    img_h4_4 = "h4_4.png"
    img_h5_1 =  "h5_1.png"
    img_h5_4 = "h5_4.png"
    img_h5_5 = "h5_5.png"
    img_h6_1 =  "h6_1.png"
    img_h6_2 = "h6_2.png"
    img_h7_2 = "h7_2.png"
    img_h7_3 = "h7_3.png"
    img_h8_1 = "h8_1.png"
    img_h9_1 = "h9_1.png"
    img_h9_2 = "h9_2.png"
    img_h10_1 = "h10_1.png"

    img_w4_1 = "w4_1.png"
    img_w5_1 = "w5_1.png"
    img_w6_1 = "w6_1.png"
    img_list = [  img_h1_3, img_h1_4,  img_h2_1,  img_h2_2,  img_h3_1,  img_h3_2, img_h4_3,  img_h4_4,  img_h5_1, img_h5_4,  img_h5_5,  img_h6_1,  img_h6_2, img_h7_2,  img_h7_3, img_h8_1, img_h9_1, img_h9_2, img_h10_1
                      ,img_w4_1, img_w5_1, img_w6_1]
##################################################################
    if method == 0:
        if rank == 21:
            M = [text_h1_4, text_h2_2, text_h3_1]
            try:
                boxes = findAll(mat_box)
            except:
                # If no founding any boxes, trade with mat_container to get All mat_boxes
                print("into except mode, name = get all boxes")
            
            if mat == img_h1_4:
                count = 0
                for i in boxes:
                    hover(i)
                    if exists( text_h1_4,1):
                        doubleClick(i)
                        break
                    else:
                        # Trade with mat_container to get Box    \
                        print("")
            elif mat == img_h2_2:
                count = 0
                for i in boxes:
                    hover(i)     
                    if exists(text_h2_2 , 1):
                        doubleClick(i)
                        break
                    else:
                        # Trade with mat_container to get Box
                        print("")
            elif mat == img_h3_1:
                count = 0
                for i in boxes:
                    hover(i)    
                    if exists(text_h3_1,1):
                        doubleClick(i)
                        break
                    else:
                        # Trade with mat_container to get Box
                        print("")
    ######################################################################################
        if rank == 61:
            M = [text_h2_1, text_h3_1, text_h3_2, text_h5_1, text_h6_1]
            running = True
            while( running ):
                try:
                    boxes = findAll(mat_box)
                    running = False
                except:
                    print("Nice boat!!!")
                    auto_trader.trade(M, chest_flag)
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
            mat_check(mat)
    #########################################################################################
        if rank == 70:
            M = [text_h1_3, text_h3_1, text_h5_1, text_h6_2, text_h7_2]
            running = True
            while( running ):
                try:
                    boxes = findAll(mat_box)
                    running = False
                except:
                    print("Nice boat!!!")
                    auto_trader.trade(M, chest_flag)
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
            mat_check(mat)
    #########################################################################################
        if rank == 71:
            M = [text_h6_2, text_h2_1, text_h4_4, text_h5_5, text_h7_3]
            running = True
            while( running ):
                try:
                    boxes = findAll(mat_box)
                    running = False
                except:
                    print("Nice boat!!!")
                    auto_trader.trade(M, chest_flag)
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
            mat_check(mat)
    #########################################################################################
        if rank == 80:
            M = [text_h2_1, text_h3_2, text_h5_5, text_h7_2, text_h8_1]
            running = True
            while( running ):
                try:
                    boxes = findAll(mat_box)
                    running = False
                except:
                    print("Nice boat!!!")
                    auto_trader.trade(M, chest_flag)
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
            mat_check(mat)
    #########################################################################################
        if rank == 101:
            M = [text_h1_3, text_h2_1, text_h3_1, text_h5_4, text_h10_1]
            running = True
            while( running ):
                try:
                    boxes = findAll(mat_box)
                    running = False
                except:
                    print("Nice boat!!!")
                    auto_trader.trade(M, chest_flag)
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
            mat_check(mat)
    #########################################################################################
        if rank == 91:
            M = [text_h1_3, text_h3_2, text_h4_3, text_h9_1, text_h9_2]
            running = True
            while( running ):
                try:
                    boxes = findAll(mat_box)
                    running = False
                except:
                    print("Nice boat!!!")
                    auto_trader.trade(M, chest_flag)
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
            mat_check(mat)
    else:
################### Potion ############################################################## 
######################################################################################
        if rank == 60:
            print("Potion Rank : 60")
            M = [text_w4_1, text_w5_1, text_w6_1]
            running = True
            while( running ):
                try:
                    boxes = findAll(mat_box)
                    running = False
                except:
                    print("Fuck")
                    auto_trader.trade(M, chest_flag)
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
                print("Match img_w4_1")
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
                        auto_trader.trade([string], chest_flag)
                        # Open Backpack
                        print("Open Backpacks")
                        keyDown(Key.CTRL)
                        keyDown("e")
                        wait(1.0)
                        keyUp(Key.CTRL)
                        keyUp("e")
            elif mat == img_w5_1:
                print("Match img_w5_1")
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
                        auto_trader.trade([string], chest_flag)
                        # Open Backpack
                        print("Open Backpacks")
                        keyDown(Key.CTRL)
                        keyDown("e")
                        wait(1.0)
                        keyUp(Key.CTRL)
                        keyUp("e")
            elif mat ==    img_w6_1:
                print("Match img_6_1")
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
                        auto_trader.trade([string], chest_flag)
                        wait(0.5)
                        # Open Backpack
                        print("Open Backpacks")
                        keyDown(Key.CTRL)
                        keyDown("e")
                        wait(1.0)
                        keyUp(Key.CTRL)
                        keyUp("e")
            else:
                print("Mat_error :  " , mat )
                print( "matType : ", mat)
                print(" imgType : ", img_w5_1)
                print( mat == img_w5_1)
                raise(" Mat error")
    #########################################################################################