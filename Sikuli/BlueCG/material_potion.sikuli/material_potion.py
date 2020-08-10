from sikuli import *
def getrecipe(rank, half_cost):
#################################################
    # 6A
    if rank == 60:
        x1 = "w4_1.png"
        x2 = "w5_1.png"
        x3 = "w6_1.png"
        X = [x1, x2, x3]
        mat_cost = [10, 15, 15]
        FP_cost = 59
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################