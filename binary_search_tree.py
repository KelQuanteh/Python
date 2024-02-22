
class TreeNode:
    # TreeNode class represents a single node in the binary tree.
    # It holds a key value, and references to its left and right children.
    def __init__(self, key):
        # Constructor initializes the node with a key and sets its left and right children to None.
        self.key = key
        self.left = None
        self.right = None

    def __str__(self):
        # String representation of the node, which returns its key.
        return str(self.key)


class BinarySearchTree:
    # BinarySearchTree class represents the binary search tree data structure.
    # It maintains a reference to the root node of the tree.

    def __init__(self):
        # Constructor initializes an empty binary search tree with no root.
        self.root = None

    def insert(self, key):
        # Public method to insert a new key into the binary search tree.
        # Calls the private _insert method to perform the insertion.
        self.root = self._insert(self.root, key)

    def _insert(self, node, key):
        # Private method to insert a new key into the binary search tree.
        # Recursive function that searches for the appropriate position to insert the new key.
        if node is None:
            # If the node is None, create a new node with the given key.
            return TreeNode(key)
        if key < node.key:
            # If the key is less than the current node's key, insert it into the left subtree.
            node.left = self._insert(node.left, key)
        elif key > node.key:
            # If the key is greater than the current node's key, insert it into the right subtree.
            node.right = self._insert(node.right, key)
        return node

    def search(self, key):
        # Public method to search for a key in the binary search tree.
        # Calls the private _search method to perform the search.
        return self._search(self.root, key)

    def _search(self, node, key):
        # Private method to search for a key in the binary search tree.
        # Recursive function that traverses the tree to find the key.
        if node is None or node.key == key:
            # If the node is None or the key matches the current node's key, return the node.
            return node
        if key < node.key:
            # If the key is less than the current node's key, search in the left subtree.
            return self._search(node.left, key)
        return self._search(node.right, key)

    def delete(self, key):
        # Public method to delete a key from the binary search tree.
        # Calls the private _delete method to perform the deletion.
        self.root = self._delete(self.root, key)

    def _delete(self, node, key):
        # Private method to delete a key from the binary search tree.
        # Recursive function that searches for the key to delete and performs the deletion.
        if node is None:
            # If the node is None, return the node.
            return node
        if key < node.key:
            # If the key is less than the current node's key, delete it from the left subtree.
            node.left = self._delete(node.left, key)
        elif key > node.key:
            # If the key is greater than the current node's key, delete it from the right subtree.
            node.right = self._delete(node.right, key)
        else:
            # If the key is found, perform the deletion.
            if node.left is None:
                # If the left child is None, replace the node with its right child.
                return node.right
            elif node.right is None:
                # If the right child is None, replace the node with its left child.
                return node.left
            # If both children exist, replace the node's key with the minimum value in the right subtree,
            # and recursively delete the minimum value node from the right subtree.
            node.key = self._min_value(node.right)
            node.right = self._delete(node.right, node.key)
        return node

    def _min_value(self, node):
        # Private method to find the minimum value node in a subtree.
        # Traverse left recursively until finding the minimum value node.
        while node.left is not None:
            node = node.left
        return node.key

    def inorder_traversal(self):
        # Public method to perform an inorder traversal of the binary search tree.
        # Calls the private _inorder_traversal method to perform the traversal.
        result = []
        self._inorder_traversal(self.root, result)
        return result

    def _inorder_traversal(self, node, result):
        # Private method to perform an inorder traversal of the binary search tree.
        # Recursive function that traverses the tree in left-root-right order.
        if node:
            self._inorder_traversal(node.left, result)
            result.append(node.key)
            self._inorder_traversal(node.right, result)


# Example usage of the BinarySearchTree class.
bst = BinarySearchTree()
nodes = [50, 30, 20, 40, 70, 60, 80]

# Insert nodes into the binary search tree.
for node in nodes:
    bst.insert(node)

# Print the inorder traversal of the binary search tree.
print("Inorder traversal:", bst.inorder_traversal())

# Search for a key in the binary search tree.
print("Search for 40:", bst.search(40))

# Delete a key from the binary search tree.
bst.delete(40)

# Print the inorder traversal after deleting a key.
print("Inorder traversal after deleting 40:", bst.inorder_traversal())

# Search for the deleted key in the binary search tree.
print("Search for 40:", bst.search(40))
