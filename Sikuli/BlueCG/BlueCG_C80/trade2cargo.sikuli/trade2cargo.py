from sikuli import *
import skill_window

def cargo(method, rank):
    cargo_locate = Location(177, 394)
    maker_locate = Location(152, 91)
    if rank == 61:
        item = "item_C60.png"
    elif rank == 70:
        item = "item_C70.png"
    elif rank == 71:
        item = "item.png"
    elif rank == 80:
        item = "item_C80.png"
    cargo =  "1579265714735.png" 
    click("1579265672127.png")
    click(cargo)
    results = findAll(item)
    for i in results:
        hover(i)
        doubleClick(i)
    click("1579265850844.png")
    hover("1579265872331.png")
    wait(2)
    click(cargo_locate) # Click Cargo_account
    click("1579265850844.png")
    click("1579265996503.png")
    hover("1579265872331.png")
    wait(2)
    click(maker_locate) # Click Maker_account
    click("1579265996503.png")

    ##### Packge Items #######
    hover("1579265872331.png")
    wait(2)
    click(cargo_locate) # Click Cargo_account
    hover("1579266260703.png")
    wait(0.5)
    # Open Backpack
    print("Open Backpacks")
    keyDown(Key.CTRL)
    keyDown("e")
    wait(1.0)
    keyUp(Key.CTRL)
    keyUp("e")
    type("/re" + Key.ENTER)
    wait(1.5)
    doubleClick(Pattern("1579266242987.png").similar(0.90))
    hover("1579265872331.png")
    wait(2)
    click(maker_locate) # Click Maker_account
    wait(0.3)
    ###### Close All windows
    flag = 0
    while(flag == 0):
        # Close allwindows
        print("Close allwindows")
        if exists("1578248310719.png"):
            click("1578248310719.png")
            wait(0.2)
        else :
            flag = 1
    hover("1579266260703.png")
    skill_window.workspace(method, rank)
    return()