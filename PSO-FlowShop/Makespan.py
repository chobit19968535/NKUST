

def makespan(job_list):
    """
    Makespan()
   
    Parameters
    ==========
    job_list : list
        job_list
   
    Optional
    ========
    None
   
    Returns
    =======
    tmp_list : list
        Result of Makespan from front two Job_list
   
    """
    tmp_list=[]
    for i in range (len(job_list[0])):
        if (i == 0):
            tmp = [job_list[0][i]]
            tmp_list.append(tmp)
            
            tmp = [job_list[1][i] + tmp_list[0][i]]
            tmp_list.append(tmp)
            continue
        else:
            tmp = job_list[0][i] + tmp_list[0][i-1]
            tmp_list[0].append(tmp)
            if (tmp_list[1][i-1] < tmp_list[0][i]):
                tmp = tmp_list[0][i] + job_list[1][i]
                tmp_list[1].append(tmp)
                continue
            
            if(tmp_list[1][i-1] >= tmp_list[0][i]):
                tmp = job_list[1][i] + tmp_list[1][i-1]
                tmp_list[1].append(tmp)
                continue
                
            else: 
                assert tmp_list[0][i] == tmp_list[1][i-1],'tmp_list[0][%s] =/= tmp_list[1][%s]'
                tmp = job_list[1][i] + tmp_list [0][i]
                tmp_list[1].append(tmp)
                continue
    return(tmp_list)