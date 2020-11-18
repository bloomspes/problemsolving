# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def binaryTreePaths(graph, root: TreeNode) -> List[str]:
        if not root:
            return []

        ans = []
        print(ans)

        s = str(root.val)

        def dfs(node, path):
            if node:
                if node.left or node.right:
                    if node.left:
                        dfs(node.left, path+"->{}".format(node.left.val))
                    if node.right:
                        dfs(node.right, path+"->{}".format(node.right.val))
                else:
                    ans.append(path)
                print(node)
        dfs(root, s)
        return ans
