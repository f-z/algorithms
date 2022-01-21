# -*- coding: utf-8 -*-
class Node:
    """
    A class used to represent a node in a tree
    The node has a key, a value, and up to three children
    ...

    Attributes
    ----------
    left : Node
        the child node on the left
    middle : Node
        the child node in the middle
    right : Node
        the child node on the right
    key : object
        the key characterising the node
    value : object
        the value that the node stores

    """
    def __init__(self, key: object, value: object):
        self.left = None
        self.middle = None
        self.right = None
        self.key = key
        self.value = value

def insert(root: Node, node: Node) -> None:
    """
    A method to insert a node in a tree

    Parameters
    ----------
    root : Node
        the starting node of the tree
    node : Node
        the node to be inserted

    Returns
    -------
    None
    """
    if root is None:
        root = node
    else:
        # Inserting to the left
        if node.key < root.key:
            if root.left is None: # If there is no left node
                root.left = node
            else:
                if node.key < root.left.key: # If key < left node
                    insert(root.left, node)
                else:
                    if root.middle is None: # If there is no mid node
                        root.middle = node
                    else:
                        # If key closer to left node than mid
                        if node.key - root.left.key < root.middle.key - node.key:
                            insert(root.left, node)
                        # If key closer to mid node
                        else:
                            insert(root.middle, node)
        # Inserting to the right
        elif node.key > root.key:
            if root.right is None:
                root.right = node
            else:
                if node.key > root.right.key:
                    insert(root.right, node)
                else:
                    if root.middle is None:
                        root.middle = node
                    else:
                        if node.key - root.left.key < root.middle.key - node.key:
                            insert(root.left, node)
                        else:
                            insert(root.middle, node)

def search(root: Node, key: object, direction: str = None) -> Node:
    """
    A method to search a tree for a given key

    Parameters
    ----------
    root : Node
        The starting point of the (sub)tree to search
    key : object
        The key to search for
    direction : str, optional
        The direction to search in.
        Takes values 'left', 'middle' or 'right'.
        The default is None.

    Returns
    -------
    Node
        The node with the given key, if found.
        None if not found.
    """
    
    if root is None:
        return None

    if root.key == key:
        return root
  
    if direction == 'left':
        return search(root.left, key)
    elif direction == 'middle':
        return search(root.middle, key)
    elif direction == 'right':
        return search(root.right, key)
    else:
        if key < root.key:
            node_found = search(root.left, key)
            if node_found is None:
                node_found = search(root.middle, key)
        else:
            node_found = search(root.right, key)
            if node_found is None:
                node_found = search(root.middle, key)
        return node_found

def store_value(root: Node, key: object, value: object, direction:str =None) -> None:
    node = search(root, key, direction)
    if node is not None:
        node.value = value
    else:
        insert(root, Node(key, value))

def retrieve_value(root: Node, key: object, direction: str =None) -> object:
    node = search(root, key, direction)
    if node is not None:
        return node.value
    return node

def in_order_print(root: Node) -> None:
    if not root:
        return
    in_order_print(root.left)
    print(root.value)
    in_order_print(root.right)

def pre_order_print(root: Node) -> None:
    if not root:
        return        
    print(root.value)
    pre_order_print(root.left)
    pre_order_print(root.right)
