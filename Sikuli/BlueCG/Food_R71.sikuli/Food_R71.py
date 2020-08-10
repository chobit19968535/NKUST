#Initialize
set = 1
#######################################################################
def trade(set):
    hover("1548956531799.png")
    wait(1)
    click(Location(1713, 263)) # Middle Character
    wait(0.3)
    click("1548999253261.png") #click trade icon
    wait("1548999302748.png",100)
    click("1548999302748.png")
    wait(0.3)
    if exists("1548999358195.png"):
        tmp = 0
        for checkBox in findAll("1548999358195.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    if exists("1548999692602.png"):
        tmp = 0
        for checkBox in findAll("1548999692602.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    if exists("1548999722051.png"):
        tmp = 0
        for checkBox in findAll("1548999722051.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    if exists("1548999749092.png"):
        tmp = 0
        for checkBox in findAll("1548999749092.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    click("1549000339846.png")
    wait(0.1)
    for i in range(2):
        hover("1548956531799.png")
        wait(1)
        click(Location(1709, 109)) # First character
        if (i==0):
            click("1549000339846.png")
            wait(0.1)
            hover("1548956531799.png")
            wait(1)
            click(Location(1713, 263)) # Middle Character
            wait(0.1)
            click("1549000700402.png")
            wait(0.1)
        if (i==1):
            wait("1549000700402.png",15)
            click("1549000927248.png")
    # Trade to Last character ########################!!
    hover("1548956531799.png")
    wait(1)
    click(Location(1708, 417)) # Last Character
    wait(0.3)
    click("1548999253261.png") #click trade icon
    wait("1548999302748.png",100)
    click("1548999302748.png")
    wait(1.0)
    if exists("1548999358195.png",):
        tmp = 0
        for checkBox in findAll("1548999358195.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    if exists("1548999692602.png",1):
        tmp = 0
        for checkBox in findAll("1548999692602.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    if exists("1548999722051.png",1):
        tmp = 0
        for checkBox in findAll("1548999722051.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    if exists("1548999749092.png",1):
        tmp = 0
        for checkBox in findAll("1548999749092.png"):
            doubleClick(checkBox)
            tmp = tmp + 1
            if (tmp == set):
                break
            wait(0.1)
    click("1549000339846.png")
    wait(0.1)
    for i in range(2):
        hover("1548956531799.png")
        wait(1)
        click(Location(1709, 109)) # First character
        wait(0.1)
        if (i==0):
            wait(Pattern("1549000339846.png").similar(0.50),10)
            click(Pattern("1549000339846.png").similar(0.50))
            wait(0.1)
            hover("1548956531799.png")
            wait(1)
            click(Location(1708, 417)) # Last Character
            wait(0.1)
            click("1549000700402.png")
            wait(0.1)
        if (i==1):
            wait("1549000700402.png",15)
            click("1549000927248.png")
            wait(0.1)
            click(Pattern("1548941574755.png").similar(0.75))
            wait(0.3)
#######################################################################      
def cook(clock):
    wait("1548937550686.png",10)
    doubleClick("1548937550686.png") #
    wait(0.1)
    
    wait("1548937591797.png",10)
    doubleClick("1548937591797.png")
    wait(0.1)
    wait("1548937601131.png",10)
    doubleClick("1548937601131.png")
    wait(0.1)

    wait("1548937609247.png",10)
    doubleClick("1548937609247.png")
    wait(0.1)

    wait("1548937616371.png",10)
    doubleClick("1548937616371.png")
    wait(0.1)
    click("1548937647215.png")
    wait("1548937716443.png",100)
    click("1548937716443.png")
    type(Key.UP + Key.ENTER)
    clock = clock +1
    return(clock)
#######################################################################    
def init():
   clock = 0
   return(clock)
#######################################################################
def ini_itter():
    itter = 0
    return(itter)
 
#######################################################################   
def recover():
    wait("1548938910092.png",20)
    click("1548938910092.png")
    rightClick("1549039719897.png")
    if find("1548939702668.png"):
        click("1548939982892.png")
        wait(Pattern("1548940015159.png").similar(0.80),10)
        click(Pattern("1548940015159.png").similar(0.80))
        wait("1548940051619.png",10)
        click("1548940051619.png")
        wait("1548940185945.png",10)
        click("1548940196970.png")
        clock = init()
        click(Pattern("1548941574755.png").similar(0.75))
        wait(0.3)
#######################################################################

# Main()
clock = init()
itter = ini_itter()
while(1):
    if (clock == 4):
        recover()
        itter = itter + 1
        clock = 0
    if (itter == 1):
        trade(set)
        itter = 0
        wait(0.2)
    clock = cook(clock)
    wait(0.5)
    