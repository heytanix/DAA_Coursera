class Node:
    # Implement a node of the binary search tree.
    # Constructor for a node with key and a given parent
    # parent can be None for a root node.
    def __init__(self, key, parent = None):
        self.key = key
        self.parent = parent
        self.left = None # We will set left and right child to None
        self.right = None
        # Make sure that the parent's left/right pointer
        # will point to the newly created node.
        if parent != None:
            if key < parent.key:
                assert(parent.left == None), 'parent already has a left child -- unable to create node'
                parent.left = self
            else:
                assert key > parent.key, 'key is same as parent.key. We do not allow duplicate keys in a BST since it breaks some of the algorithms.'
                assert(parent.right == None), 'parent already has a right child -- unable to create node'
                parent.right = self

    # Utility function that keeps traversing left until it finds
    # the leftmost descendant
    def get_leftmost_descendant(self):
        if self.left != None:
            return self.left.get_leftmost_descendant()
        else:
            return self

    # Search algorithm implementation
    def search(self, key):
        if self.key == key:
            return (True, self)
        elif key < self.key:
            if self.left is None:
                return (False, self)
            return self.left.search(key)
        else:
            if self.right is None:
                return (False, self)
            return self.right.search(key)

    # Insert algorithm implementation
    def insert(self, key):
        found, parent_node = self.search(key)
        if found:
            return None
        return Node(key, parent_node)

    # Height computation implementation
    def height(self):
        left_height = self.left.height() if self.left else 0
        right_height = self.right.height() if self.right else 0
        return 1 + max(left_height, right_height)

    # Delete algorithm implementation
    def delete(self, key):
        found, node_to_delete = self.search(key)
        assert(found == True), f"key to be deleted:{key}- does not exist in the tree"

        # Case 1: Node has no children
        if node_to_delete.left is None and node_to_delete.right is None:
            if node_to_delete.parent:
                if node_to_delete.parent.left == node_to_delete:
                    node_to_delete.parent.left = None
                else:
                    node_to_delete.parent.right = None
            return

        # Case 2: Node has one child
        if node_to_delete.left is None:
            child = node_to_delete.right
        elif node_to_delete.right is None:
            child = node_to_delete.left
        else:
            # Case 3: Node has two children
            successor = node_to_delete.right.get_leftmost_descendant()
            node_to_delete.key = successor.key
            if successor.parent == node_to_delete:
                node_to_delete.right = successor.right
            else:
                successor.parent.left = successor.right
            if successor.right:
                successor.right.parent = successor.parent
            return

        # Complete Case 2 handling
        child.parent = node_to_delete.parent
        if node_to_delete.parent:
            if node_to_delete.parent.left == node_to_delete:
                node_to_delete.parent.left = child
            else:
                node_to_delete.parent.right = child
