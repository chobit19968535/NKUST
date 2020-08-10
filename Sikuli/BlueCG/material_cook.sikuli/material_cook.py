from sikuli import *
def getrecipe(rank, half_cost):
#################################################
    # 2B
    if rank == 21:
        x1 = "h1_4.png"
        x2 = "h3_1.png"
        x3 = "h2_2.png"
        X = [x1, x2, x3]
        mat_cost = [20, 20, 20]
        FP_cost = 21
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################
    # 6B
    if rank == 61:
        x1 = "h2_1.png"
        x2 = "h3_1.png"
        x3 = "h3_2.png"
        x4 = "h5_1.png"
        x5 = "h6_1.png"
        X = [x1, x2, x3, x4, x5]
        mat_cost = [20, 20, 20, 20, 20]
        FP_cost = 59
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################
    # 7A
    if rank == 70:
        x1 = "h1_3.png"
        x2 = "h3_1.png"
        x3 = "h5_1.png" 
        x4 = "h6_2.png"
        x5 = "h7_2.png"
        X = [x1, x2, x3, x4, x5]
        mat_cost = [10, 20, 20, 20, 20]
        FP_cost = 69
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################
    # 7B
    if rank == 71:
        x1 = "h6_2.png"
        x2 = "h2_1.png"
        x3 = "h4_4.png"
        x4 =  "h5_5.png"
        x5 = "h7_3.png"
        X = [x1, x2, x3, x4, x5]
        mat_cost = [20, 20, 20, 20, 10]
        FP_cost = 69
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################
    # 8A
    if rank == 80:
        x1 = "h2_1.png"
        x2 = "h3_2.png"
        x3 = "h5_5.png"
        x4 =  "h7_2.png"
        x5 = "h8_1.png"
        X = [x1, x2, x3, x4, x5]
        mat_cost = [20, 20, 20, 20, 10]
        FP_cost = 79
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################
    # 9B
    if rank == 91:
        x1 = "h9_2.png"
        x2 = "h9_1.png"
        x3 = "h4_3.png"
        x4 =  "h3_2.png"
        x5 = "h1_3.png"
        X = [x1, x2, x3, x4, x5]
        mat_cost = [15, 15, 20, 20, 20]
        FP_cost = 89
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)
#################################################
    # 10A
    if rank == 101:
        x1 = "h2_1.png"
        x2 = "h3_1.png"
        x3 = "h1_3.png"
        x4 = "h10_1.png"
        x5 = "h5_4.png"
        X = [x1, x2, x3, x4, x5]
        mat_cost = [20, 20, 20, 20, 20]
        FP_cost = 99
        if (half_cost == True):
            FP_cost = int(FP_cost/2)
        return(X, FP_cost, mat_cost)