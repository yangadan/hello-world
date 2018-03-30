'''结果的仿真'''
from random import *
from time import *
def Subsimulation():
    #日后可填充更为复杂的函数
    seed(time()+3)
    return randint(0,1)
def simulation():
    time1=time()
    i=sum1=0
    while time()-0.05<time1:
        sum1+=Subsimulation()
        i+=1
    return int(2*(sum1/i))
        

    
    
    
