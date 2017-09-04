#
# res  =[]
#
# def postOrder(root):
#     if(root is not None):
#         postOrder(root.left)
#         postOrder(root.right)
#         if(root.value is not None):
#             res.append(root.value)
#
# class Node:
#     value  = None
#     left = None
#     right = None
#     parent = None
#     def __init__(self,value=None):
#         self.value  =value
#
#     def inAdd(self,value):
#         if(self.value is  None):
#             self.value = value
#             temp = Node()
#             self.left = temp
#             self.left.parent = self
#             return self.left
#         else:
#             if(self.left is not None):
#                 self.right = Node(value)
#                 self.right.parent = self
#                 return self.right
#             else:
#                 self.left = Node(value)
#                 self.left.parent = self
#                 temp  =Node()
#                 self.left.left  =temp
#                 temp.parent = self.left
#                 return temp
#
#
#
#
#
#
# if(__name__=="__main__"):
#
#     num = int(raw_input())
#     _,v = raw_input().split()
#     Root = Node()
#     now = Root.inAdd(int(v))
#     for i in range(2*num-1):
#         s = raw_input()
#         if("Push" in s):
#             o,v = s.split(' ')
#             now = now.inAdd(int(v))
#         else:
#             now = now.parent
#
#
#     postOrder(Root)
#     print ' '.join([str(x) for x in res])

postOrder = []
preOrder = []
inOrder = []

def to_post(preStartIndex,preEndIndex,inStartIndex,inEndIndex):
    preRootValue = preOrder[preStartIndex]
    inRootIndex = inOrder.index(preRootValue)

    leftTreeNum = inRootIndex-inStartIndex
    rightTreeNum = inEndIndex-inRootIndex
    #left

    if(leftTreeNum!=0):
        to_post(preStartIndex = preStartIndex+1,preEndIndex=preStartIndex+1+leftTreeNum-1,inStartIndex = inStartIndex,inEndIndex=inRootIndex-1)
    #right
    if(rightTreeNum!=0):
        to_post(preStartIndex = preStartIndex+1+leftTreeNum,preEndIndex=preStartIndex+1+leftTreeNum+rightTreeNum,inStartIndex=inRootIndex+1,inEndIndex=inEndIndex)
    postOrder.append(preRootValue)


if(__name__=="__main__"):


    stack = []

    num = int(raw_input())

    for i in range(2*num):
        s = raw_input()
        if("Push" in s):
            o,v = s.split(' ')
            preOrder.append(v)
            stack.append(v)
        else:
            t = stack.pop()
            inOrder.append(t)

    to_post(preStartIndex=0,preEndIndex=len(preOrder)-1,inStartIndex=0,inEndIndex=len(inOrder)-1)

    # print preOrder
    # print inOrder
    print ' '.join([str(x) for x in postOrder])



