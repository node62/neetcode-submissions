class Node:
    def __init__(self, key, val, left=None, right=None):
        self.key = key
        self.val = val
        self.left = left
        self.right = right

class TreeMap:
    def __init__(self):
        self.root = None       

    def insert(self, key: int, val: int) -> None:
        if not self.root: self.root = Node(key, val)
        else:
            curr = self.root
            while True:
                if key < curr.key:
                    if curr.left: curr = curr.left
                    else:
                        curr.left = Node(key, val)
                        break
                elif key > curr.key:
                    if curr.right: curr = curr.right
                    else:
                        curr.right = Node(key, val)
                        break
                else:
                    curr.val = val
                    break

    def get(self, key: int) -> int:
        if not self.root: return -1
        curr = self.root
        while curr:
            if key < curr.key:
                curr = curr.left
            elif key > curr.key:
                curr = curr.right
            else:
                return curr.val
        return -1

    def getMin(self) -> int:
        if not self.root: return -1
        curr = self.root
        while curr.left:
            curr = curr.left
        return curr.val

    def getMax(self) -> int:
        if not self.root: return -1
        curr = self.root
        while curr.right:
            curr = curr.right 
        return curr.val

    def remove(self, key: int) -> None:
        def helper(root, key):
            if not root: return None
            curr = root
            if key < curr.key: curr.left = helper(curr.left, key)
            elif key > curr.key: curr.right = helper(curr.right, key)
            else:
                if not curr.left: return curr.right
                elif not curr.right: return curr.left
                else:
                    temp = curr.right
                    while temp.left:
                        temp = temp.left
                    curr.val = temp.val
                    curr.key = temp.key
                    curr.right =  helper(curr.right, temp.key) 
                    return curr
            return root
        self.root = helper(self.root, key)

    def getInorderKeys(self) -> List[int]:
        fin = []
        def helper(root):
            if not root: return None
            helper(root.left)
            fin.append(root.key)
            helper(root.right)
        helper(self.root) 
        return fin
