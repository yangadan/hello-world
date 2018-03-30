'''根据模拟结果改变访问及统计值'''
from simulation import *
from Tree import *
def feedback(root,result):
    root.a+=1
    root.v+=result
    while root.parent!=None:
        root=root.parent
        root.a+=1
        root.v+=result
