# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self, root: Optional[TreeNode], startValue: int, destValue: int) -> str:
        left_path = self.helper(root,startValue,[])
        right_path = self.helper(root,destValue,[])
        ptr = 0
        for i in range(min(len(left_path),len(right_path))):
            if left_path[i] != right_path[i]:
                break
            ptr += 1
        left_path = left_path[ptr:]
        left_path = ["U" for j in range(len(left_path))]
        right_path = right_path[ptr:]
        return "".join(left_path + right_path)
    
    def helper(self, root, dest,path):
        if not root:
            return []
        if root.val == dest:
            return path
        path.append("L")
        left_path = self.helper(root.left,dest,path)
        if left_path:
            return left_path
        path.pop()
        path.append("R")
        right_path = self.helper(root.right,dest,path)
        if right_path:
            return right_path
        path.pop()
        return []
