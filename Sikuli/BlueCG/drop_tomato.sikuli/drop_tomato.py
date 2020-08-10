while(1):
    junk = "junk.png" 
    if exists(junk):
        click(junk)
        hover("tmp.png")
        click("flag.png")
        wait(1.0)