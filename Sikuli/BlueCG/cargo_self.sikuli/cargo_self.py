from sikuli import *
import skill_window

def package(method, rank):
    running = 1
    while (running):
        icon = "close.png"
        if exists (icon):
            click(icon)
        else:
            running = 0
    # Open Backpack
    print("Open Backpacks")
    keyDown(Key.CTRL)
    keyDown("e")
    wait(1.0)
    keyUp(Key.CTRL)
    keyUp("e")
    type("/re" + Key.ENTER)
    wait(1.5)
    doubleClick("Box-1.png")
    wait(0.1)
    # Open Backpack
    print("Open Backpacks")
    keyDown(Key.CTRL)
    keyDown("e")
    wait(1.0)
    keyUp(Key.CTRL)
    keyUp("e")
    type("/re" + Key.ENTER)
    skill_window.workspace(method, rank)
    return(0)