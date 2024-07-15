# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def createBinaryTree(self, descriptions: List[List[int]]) -> Optional[TreeNode]:
        mp = {}
        seen = set()
        for p, c, left in descriptions: 
            if p not in mp: mp[p] = TreeNode(p)
            if c not in mp: mp[c] = TreeNode(c)
            if left: mp[p].left = mp[c]
            else: mp[p].right = mp[c]
            seen.add(c)
        for p, _, _ in descriptions: 
            if p not in seen: return mp[p]