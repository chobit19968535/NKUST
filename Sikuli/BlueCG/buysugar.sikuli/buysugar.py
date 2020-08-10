wait(1.5)

rightClick("1579530724475.png")
count = 0
while (count<16):
    click("1579530999705.png")
    flag = 0
    while( flag == 0):
        click(Pattern("1579531357126.png").targetOffset(-84,14))
        if exists(Pattern("1579531138502.png").similar(0.90)):
            flag =1
    click("1579531163177.png")
    click("1579531175780.png")
    wait(0.5)
    count += 1