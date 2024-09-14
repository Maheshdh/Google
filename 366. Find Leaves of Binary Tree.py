# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findLeaves(self, root: Optional[TreeNode]) -> List[List[int]]:
        self.result = [[]]
        self.findDepth(root)
        return self.result
    
    def findDepth(self,root):
        if root == None:
            return -1
        leftHeight = self.findDepth(root.left)
        rightHeight = self.findDepth(root.right)
        depth = max(leftHeight,rightHeight) + 1
        if depth >= len(self.result):
            self.result.append([])
        print("Result ",self.result)
        self.result[depth].append(root.val)
        return depth

        
