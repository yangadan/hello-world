from  Tree import *
import TreePolicy
from  random import *
from simulation import *
from feedback import *
##def test_select():
##    t=random.randint(1,5)
##    root=TreeNode(t)
##    maxs=TreePolicy.createaction(root)
##    root.addChildNode(maxs)
##    for i in range(root.maxchildnode):
##        print(root.childnodes[i].v)
##if "__filename__"=="main":
##    test_select()
##    
##test_select()  
##def simulation_test():
##    for i in range(10):
##        print(simulation())
##simulation_test()
def mcts_test():
     t=randint(1,5)
     root=TreeNode(t)
     i=10
     while i>0:
         node=TreePolicy.TreePolicy(root)
         print(node,node.maxchildnode)
         maxs=TreePolicy.createaction(node)
         node.addChildNode(maxs)
         for e in node.childnodes:
             r=simulation()
             feedback(e,r)
         i-=1
     print("acess{},victory{}".format(root.a,root.v))
mcts_test()
         
     
    
