from sikuli import *
import get_material
import skill_window
def cft(X, method, rank, mat_count, mat_cost, chest_flag):
    valid  = 0
    retry = ("1578224607498.png")
    # Check matericals
    mat_predict = [0]*len(mat_count)
    for i in range (len(mat_count)):
        mat_predict[i] = mat_count[i] - mat_cost[i]
        if mat_predict[i] < 0:
            mat_predict[i] = 1
        else:
            mat_predict[i] = 0
    print(mat_count)
    print(mat_cost)
    print(mat_predict)
    section = 0
    for index, val in enumerate(mat_predict):
        if val == 1:
            if section == 0:
                flag = 0
                while(flag == 0):
                    # Close allwindows
                    print("Close allwindows")
                    if exists("1578248310719.png"):
                        click("1578248310719.png")
                        wait(0.2)
                    else :
                        # Open Backpack
                        print("Open Backpacks")
                        flag = 1
                        wait(0.25)
                        keyDown(Key.CTRL)
                        keyDown("e")
                        wait(1.0)
                        keyUp(Key.CTRL)
                        keyUp("e")
                        section = 1
                get_material.open_box(X[index], rank, method, chest_flag)
                mat_count[index] += 80
            else:
                get_material.open_box(X[index], rank, method, chest_flag)
                mat_count[index] += 80
    if section ==1:
        # Close Backpack
        keyDown(Key.CTRL)
        keyDown("e")
        wait(1)
        keyUp(Key.CTRL)
        keyUp("e")
        hover("1578460436866.png")
        wait(0.25)
        skill_window.workspace(method, rank)
    for i in range(len(mat_count)):
        mat_count[i] -= mat_cost[i]
    mat_count[i]
    print("mat_count:", mat_count) 
    if method == 0:
        trigger = 0.70
    elif method == 1:
        trigger = 0.92
    elif method == 2:
        trigger = 0.75
    while( valid == 0):
        for i in X:
            wait(0.1)
            ronust = 1
            while (ronust):
                try:         
                    hover("1582460794233.png")
                    candidates = findAll(Pattern(i).similar(trigger))
                    ronust = 0
                except:
                    hover("1582460794233.png")
                    wait(0.25)
                    continue
            for j in candidates:
                doubleClick(j)
        try:
            click("1578224068491.png")
            valid = 1
            wait(retry, 60)
            click(retry)
            type("/re" + Key.ENTER)
            wait(0.5)
            return(mat_count)
        except:
            valid = 0