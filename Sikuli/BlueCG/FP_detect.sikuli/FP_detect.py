from sikuli.Sikuli import *
def FP_check(FP_cost):
    #             w
    # (x,y)-----------------
    #     |                |
    #   h |                |
    #     |-----------------
    Settings.OcrTextSearch = True
    Settings.OcrTextRead = True
    res = findBest("1578230566853.png")
    x, y  = res.x, res.y # Get center of "FP" string
    #print(x,y)
    x, y, w, h = x + 20, y+1, 24, 12 # Offset to real Anchor as a ROI
    #x, y, w, h = x, y, x+22, y+6 # Offset to real Anchor as a ROI
    tmp_cap = capture(x,y, w, h)
    img_path = "E:\\CodeTools\\Sikuli\\Scripts\\BlueCG\\FP_detect.png"   
    import shutil
    shutil.move (tmp_cap, img_path) # (old, new)
    FP_remain = int(findBest(Pattern(img_path).similar(0.5)).text())
    print("FP_remain: {}".format(FP_remain))
    return()