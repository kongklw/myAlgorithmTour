class BTree:
    def __init__(self):
        pass



class Node(object):

    def __init__(self):
        keys = []
        children =[]
        keyNumber=None
        leaf = True #是否是叶子节点
        t = 0  # 最小度. 度表示节点孩子个数。