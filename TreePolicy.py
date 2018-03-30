import Tree
import math
import random
import time
def count(node,parentnode):#此函数用来返回单个节点的ucb1计算值
    return node.v/node.a +(2*math.log(parentnode.a)/node.a)**0.5
 
def SubTreePolicy(node):#选择下一步的动作
    max=j=0;
    for i,childnode in enumerate(node.childnodes):
        temp=count(childnode,node)
        if temp>max:
            max=temp
            j=i
    return node.childnodes[j]
def TreePolicy(root):#执行搜索策略
    if len(root.childnodes)==0:
        return root
    else:
        childnode=SubTreePolicy(root)
        TreePolicy(childnode)

def createaction(node):#产生当前结点的子节点所能拥有的最大子节点个数序列
    maxs=[]
    print(node.maxchildnode)
    for i in range(node.maxchildnode):
        maxs.append(random.randint(1,5))
        
    return maxs
