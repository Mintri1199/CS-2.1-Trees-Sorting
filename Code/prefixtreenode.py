#!python3


class PrefixTreeNode:
    """PrefixTreeNode: A node for use in a prefix tree that stores a single
    character from a string and a structure of children nodes below it, which
    associates the next character in a string to the next node along its path from
    the tree's root node to a terminal node that marks the end of the string."""

    # Choose a type of data structure to store children nodes in
    # Hint: Choosing list or dict affects implementation of all child methods
    CHILDREN_TYPE = list

    def __init__(self, character=None):
        """Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property."""
        # Character that this node represents
        self.character = character.lower()
        # Data structure to associate character keys to children node values
        self.children = [None] * 26
        # Marks if this node terminates a string in the prefix tree
        self.terminal = False

    def is_terminal(self):
        """Return True if this prefix tree node terminates a string."""
        return self.terminal

    def num_children(self):
        """Return the number of children nodes this prefix tree node has."""
        return len([x for x in self.children if x is not None])

    def has_child(self, character):
        """Return True if this prefix tree node has a child node that
        represents the given character amongst its children."""
        index = ord(character.lower()) - 97
        return self.children[index] is not None

    def get_child(self, character):
        """Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not."""
        if self.has_child(character):
            index = ord(character) - 97
            return self.children[index]
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def add_child(self, character, child_node):
        """Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children."""
        if not self.has_child(character):
            index = ord(character) - 97
            self.children[index] = child_node
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def __repr__(self):
        """Return a code representation of this prefix tree node."""
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""
        return f'({self.character})'
