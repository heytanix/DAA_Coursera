import random

# 1. make list of  numbers from 0 to n-1
# 2. randomly shuffle the list
# 3. insert the random list elements in order into a tree.
# 4. return the height of the resulting tree.
def run_single_experiment(n):
    # Create list of numbers 0 to n-1
    numbers = list(range(n))
    # Randomly shuffle the list
    random.shuffle(numbers)
    
    # Create binary search tree and insert numbers
    class Node:
        def __init__(self, val):
            self.val = val
            self.left = None
            self.right = None
            
    def insert(root, val):
        if root is None:
            return Node(val)
        if val < root.val:
            root.left = insert(root.left, val)
        else:
            root.right = insert(root.right, val)
        return root
        
    def height(root):
        if root is None:
            return 0
        return 1 + max(height(root.left), height(root.right))
    
    # Build tree
    root = None
    for num in numbers:
        root = insert(root, num)
        
    # Return height
    return height(root)
    
def run_multiple_trials(n, numTrials):
    lst_of_depths = [run_single_experiment(n) for j in range(numTrials)]
    return (sum(lst_of_depths)/len(lst_of_depths), lst_of_depths)
