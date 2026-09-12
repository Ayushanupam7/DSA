class Solution:
    def inorderTraversal(self, root):
        stack = []
        result = []
        current = root

        while current or stack:
            # Go as left as possible
            while current:
                stack.append(current)
                current = current.left
            
            # Visit the node
            current = stack.pop()
            result.append(current.val)
            
            # Move to right
            current = current.right
            
        return result