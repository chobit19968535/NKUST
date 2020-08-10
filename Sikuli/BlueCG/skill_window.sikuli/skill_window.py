from sikuli import *
def workspace(method, rank):
    icon = "icon.png"
    flag = 0
    keyDown(Key.CTRL)
    keyDown("w")
    wait(1)
    keyUp(Key.CTRL)
    keyUp("w")
    if method == 0:
        click("1578244623720.png")
        hover()
        click("1578244623720.png")
#####################################################
        if rank == 61:
            goal = "C61.png"
            while(flag == 0):
                if exists(goal):
                    flag = 1
                    click(goal)
                else:
                    click("1578244915510.png")
        if rank == 70:
            goal = "goal.png"
            while(flag == 0):
                if exists(goal):
                    flag = 1
                    click(goal)
                else:
                    click("1578244915510.png")
#####################################################
        if rank == 80:
            goal = "C80.png"
            while(flag == 0):
                if exists(goal):
                    flag = 1
                    click(goal)
                else:
                    click("1578244915510.png")
#####################################################
        if rank == 91:
            goal = "C91.png"
            while(flag == 0):
                if exists(goal):
                    flag = 1
                    click(goal)
                else:
                    click("1578244915510.png")
#####################################################
        if rank == 101:
            goal = "goal.png"
            while(flag == 0):
                if exists(goal):
                    flag = 1
                    click(goal)
                else:
                    click("1578244915510.png")
    else:
        # potion.
        if method == 1:
            click("skill_potion.png")
            hover(icon)
            click("skill_potion.png")
################################################################
            if rank == 60:
                goal = Pattern("goal.png").similar(0.90)
                while(flag == 0):
                    if exists(goal):
                        flag = 1
                        click(goal)
                    else:
                        click("1578244915510.png")