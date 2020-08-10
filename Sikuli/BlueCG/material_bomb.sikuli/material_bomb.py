from sikuli import *
def getrecipe(rank, half_cost):
#################################################
    # 6A
    if rank == 50:
        x1 = "cloth5.png"
        x2 = "flower5.png"
        x3 = "flower4.png"
        x4 = "mine5.png"
        x5 = "mine4.png"
        X = [x1, x2, x3, x4, x5]
        mat_cost = [8, 20, 20, 10, 10]
        FP_cost = 79
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################