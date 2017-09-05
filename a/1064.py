#coding: utf-8
que = []
res = []
count = 0
nums = []
#思路:构造对应大小的完全二叉树,进行一次中序遍历时将排好序的值填入,再进行一次层序遍历输出答案

class Node(object):
    left = None
    right = None
    value = None
    parent = None
    def __init__(self,value = None):
        self.value = value

    def createNextChild(self,value):
        if(self.left is None):
            self.left = Node(value)
            return self.left
        else:
            self.right = Node(value)
            return self.right

#构造有n个节点的完全二叉树
def createCompleteBinaryTree(n):
    q = []
    i=1
    root = Node(0)
    q.append(root)
    q.append(root)

    while(i<n):
        now = q.pop(0)
        new = now.createNextChild(i)
        q.append(new)
        q.append(new)
        i+=1

    return root


#中序遍历时插入对应数值
def inOrder(Root):

    if(Root.left is not None):
        inOrder(Root.left)
    Root.value = nums.pop(0)
    if (Root.right is not None):
        inOrder(Root.right)

#层序遍历输出
def levelTravelsal(root):
    que.append(root)

    while(len(que)>0):
        Root = que.pop(0)
        if(Root.left is not None):
            que.append(Root.left)
        if (Root.right is not None):
            que.append(Root.right)
        res.append(Root.value)


if(__name__=="__main__"):
    count = int(raw_input())
    nums = [int(x) for x in raw_input().split(' ')]


    if(len(nums)==1):
        print nums[0]
        exit(0)
    if(len(nums)==2):
        print max(nums),min(nums)
        exit(0)


    nums.sort()

    root = createCompleteBinaryTree(count)
    inOrder(root)


    levelTravelsal(root)

    print ' '.join([str(x) for x in res])

