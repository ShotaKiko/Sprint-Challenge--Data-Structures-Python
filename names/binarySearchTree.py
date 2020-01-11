class BinarySearchTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    # Insert the given value into the tree
    def insert(self, value):
        # if inserting we must already have a tree/root
        # if value is less than self.value go right make a new tree/node if empty
        #----> recurse through
        if self.value < value:
            if self.right:
                self.right.insert(value)
            else:
                self.right = BinarySearchTree(value)
        # if greater than or equal to go left making a new tree/node if empty
        # less than or equal values become left child-----> recurse through
        else:
            if self.left:
                self.left.insert(value)
            else:
                self.left = BinarySearchTree(value)



    def contains(self, target):
    # Return True if the tree contains the value or False if it not
        # if target == self.value return it
        if target == self.value:
            return True
        # otherwise go left or right depending on which value is greater.
        if target < self.value:
            if self.left is None:
                return False
            else:
                return self.left.contains(target)
        else:
            if self.right is None:
                return False
            else:
                return self.right.contains(target)

        

    # Return the max value found in bst
    def get_max(self):
        # if right exists go right if not the return self.value
        if self.right:
            return self.right.get_max()
        else:
            return self.value

    # Call the `cb`  on the value of each node and use recursion
    def for_each(self, cb):
        cb(self.value)
        if self.left:
            self.left.for_each(cb)
        if self.right:
            self.right.for_each(cb)