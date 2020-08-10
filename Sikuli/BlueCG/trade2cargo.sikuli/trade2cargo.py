from sikuli import *
import skill_window

def cargo(method, rank):
    cargo_locate = Location(230, 424)
    maker_locate = Location(229, 100)
    game_icon = "game_icon.png"
    if rank == 61:
        item = "item_C61.png"
    elif rank == 70:
        item = "item_C70.png"
    elif rank == 71:
        item = "item_C71.png"
    elif rank == 80:
        item = "item_C80.png"
    elif rank == 91:
        item = "item_C91.png"
    elif rank == 101:
        item = "item.png"
    cargo =  "1579265714735.png" 
    click("1579265672127.png")
    click(cargo)
    results = findAll(item)
    for i in results:
        hover(i)
        doubleClick(i)
    click("1579265850844.png")
    hover(game_icon)
    wait(2)
    click(cargo_locate) # Click Cargo_account
    wait(0.5)
    click("1579265850844.png")
    wait(0.25)
    click("1579265996503.png")
    wait(0.25)
    hover(game_icon)
    wait(2)
    click(maker_locate) # Click Maker_account
    wait(0.25)
    click("1579265996503.png")

    ##### Packge Items #######
    hover(game_icon)
    wait(2)
    click(cargo_locate) # Click Cargo_account
    hover("1594962398602.png")
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
    hover(game_icon)
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
    hover("1594962398602.png")
    skill_window.workspace(method, rank)
    return()