class solution:
    def Leveltraversal(self,root):
        if not root:
            return []
        reuslt=[]
        queue=[root]
        while queue:
            Level=[]
            for i in range(len(queue)):
                node=queue.pop(0)
                Level.append(node.val)
                if node.Left:
                    queue.append(node.left)
                if node.Right:
                    queue.append(node.right)
            reuslt.append(Level)
        return reuslt
   
    