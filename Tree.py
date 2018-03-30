class TreeNode():
    '树节点类'
    def __init__(self,max,object=None):#初始化构造函数
        self.parent=object
        self.childnodes=[]
        self.maxchildnode=max
        self.v=0            # 胜利的次数
        self.a=0            # 访问的次数
    def addChildNode(self,maxs):#扩展
        for i in range(self.maxchildnode):
            tree=TreeNode(maxs[i],self)
            self.childnodes.append(tree)

