import random as rd
import time
def naive_search(x,y):
    for i in range (len(x)):
        if x[i]==y:
            return i
    return -1

def binary_search(x,y, low=None, high=None):
    if low==None:
        low=0
    if high==None:
        high=len(x)-1
    if high<low:
        return -1    

    midpoint=(low+high)//2     

    if x[midpoint] == y:
        return midpoint
    elif x[midpoint]>y:
        return binary_search(x,y,low,midpoint-1)
    else:
        return binary_search(x,y,midpoint+1,high)
if __name__=='__main__':
    length=10000
    sorted_list=set()
    while len(sorted_list)<length:
        sorted_list.add(rd.randint(-3*length,3*length))
    sorted_list=sorted(list(sorted_list))
    start=time.time()   

    for target in sorted_list:
        naive_search(sorted_list,target) 

    end=time.time()
    print("Naive earch time ", (end-start)/length, "seconds")

    start=time.time()   

    for target in sorted_list:
        binary_search(sorted_list,target) 

    end=time.time()
    print("Binary earch time ", (end-start)/length, "seconds")





