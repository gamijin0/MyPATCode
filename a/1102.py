nodes = []
nodes_l = []
que = []
res1 = []
res2 = []
class Node(object):
    left = None
    right = None
    value = None
    parent = None
    def __init__(self,value = None):
        self.value = value

def createTree(Root,i):
    l,r = nodes[int(i)]
    if(l!='-'):
        Root.left = Node(l)
        createTree(Root.left,l)
    if(r!='-'):
        Root.right = Node(r)
        createTree(Root.right,r)

def levelTravelsal(Root):
    if(Root.left is not None):
        que.insert(0,Root.left)
    if (Root.right is not None):
        que.insert(0,Root.right)
    res1.append(Root.value)
    if(len(que)>0):
        levelTravelsal(que.pop())

def inOrder(Root):
    if(Root.left is not None):
        inOrder(Root.left)
    res2.append(Root.value)
    if (Root.right is not None):
        inOrder(Root.right)


if(__name__=="__main__"):
    num = int(raw_input())

    for i in range(num):
        r,l = raw_input().split(' ')
        nodes.append([l,r])
        if(r!='-'):
            nodes_l.append(int(r))
        if (l != '-'):
            nodes_l.append(int(l))

    root  = 0
    for i in range(num):
        if(i not in nodes_l):
            root = i
            break

    Root = Node(value = root)
    createTree(Root,root)
    levelTravelsal(Root)
    inOrder(Root)
    print ' '.join([str(x) for x in res1])
    print ' '.join([str(x) for x in res2])