#!python3

from prefixtree import PrefixTree, PrefixTreeNode
import unittest


class PrefixTreeTest(unittest.TestCase):

    def test_init_and_properties(self):
        tree = PrefixTree()
        # Verify tree size property
        assert isinstance(tree.size, int)
        assert tree.size == 0
        # Verify root node
        assert isinstance(tree.root, PrefixTreeNode)
        assert tree.root.character == PrefixTree.START_CHARACTER
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 0

    def test_init_with_string(self):
        tree = PrefixTree(['a'])
        # Verify root node
        assert tree.root.character == PrefixTree.START_CHARACTER
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'A'
        node_A = tree.root.get_child('a')
        assert node_A.character == 'a'
        assert node_A.is_terminal() is True
        assert node_A.num_children() == 0

    def test_insert_with_string(self):
        tree = PrefixTree()
        tree.insert('ab')
        # Verify root node
        assert tree.root.character == PrefixTree.START_CHARACTER
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'A'

        node_A = tree.root.get_child('a')
        print(tree.root.children)
        assert node_A.character == 'a'
        assert node_A.is_terminal() is False
        assert node_A.num_children() == 1
        assert node_A.has_child('b') is True

        # Verify node 'B'
        node_B = node_A.get_child('b')
        assert node_B.character == 'b'
        assert node_B.is_terminal() is True
        assert node_B.num_children() == 0

    def test_insert_with_4_strings(self):
        tree = PrefixTree()
        # Insert new string that starts from root node
        tree.insert('abc')
        # Verify root node
        assert tree.root.character == PrefixTree.START_CHARACTER
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify new node 'A'
        node_A = tree.root.get_child('a')
        assert node_A.character == 'a'
        assert node_A.is_terminal() is False
        assert node_A.num_children() == 1
        assert node_A.has_child('b') is True
        # Verify new node 'B'
        node_B = node_A.get_child('b')
        assert node_B.character == 'b'
        assert node_B.is_terminal() is False
        assert node_B.num_children() == 1
        assert node_B.has_child('c') is True
        # Verify new node 'C'
        node_C = node_B.get_child('c')
        assert node_C.character == 'c'
        assert node_C.is_terminal() is True
        assert node_C.num_children() == 0

        # Insert string with partial overlap so node 'B' has new child node 'D'
        tree.insert('abd')
        # Verify root node again
        assert tree.root.character == PrefixTree.START_CHARACTER
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'A' again
        assert node_A.character == 'a'
        assert node_A.is_terminal() is False
        assert node_A.num_children() == 1
        assert node_A.has_child('b') is True
        # Verify node 'B' again
        assert node_B.character == 'b'
        assert node_B.is_terminal() is False
        assert node_B.num_children() == 2  # Node 'B' now has two children
        assert node_B.has_child('c') is True  # Node 'C' is still its child
        assert node_B.has_child('d') is True  # Node 'D' is its new child
        # Verify new node 'D'
        node_D = node_B.get_child('d')
        assert node_D.character == 'd'
        assert node_D.is_terminal() is True
        assert node_D.num_children() == 0

        # Insert substring already in tree so node 'A' becomes terminal
        tree.insert('A')
        # Verify root node again
        assert tree.root.character == PrefixTree.START_CHARACTER
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 1
        assert tree.root.has_child('a') is True
        # Verify node 'A' again
        assert node_A.character == 'a'
        assert node_A.is_terminal() is True  # Node 'A' is now terminal
        assert node_A.num_children() == 1  # Node 'A' still has one child
        assert node_A.has_child('b') is True  # Node 'B' is still its child

        # Insert new string with no overlap that starts from root node
        tree.insert('xyz')
        # Verify root node again
        assert tree.root.character == PrefixTree.START_CHARACTER
        assert tree.root.is_terminal() is False
        assert tree.root.num_children() == 2  # Root node now has two children
        assert tree.root.has_child('a') is True  # Node 'A' is still its child
        assert tree.root.has_child('x') is True  # Node 'X' is its new child
        # Verify new node 'X'
        node_X = tree.root.get_child('x')
        assert node_X.character == 'x'
        assert node_X.is_terminal() is False
        assert node_X.num_children() == 1
        assert node_X.has_child('y') is True
        # Verify new node 'Y'
        node_Y = node_X.get_child('y')
        assert node_Y.character == 'y'
        assert node_Y.is_terminal() is False
        assert node_Y.num_children() == 1
        assert node_Y.has_child('z') is True
        # Verify new node 'Z'
        node_Z = node_Y.get_child('z')
        assert node_Z.character == 'z'
        assert node_Z.is_terminal() is True
        assert node_Z.num_children() == 0

    def test_size_and_is_empty(self):
        tree = PrefixTree()
        # Verify size after initializing tree
        assert tree.size == 0
        assert tree.is_empty() is True
        # Verify size after first insert
        tree.insert('a')
        assert tree.size == 1
        assert tree.is_empty() is False
        # Verify size after second insert
        tree.insert('abc')
        assert tree.size == 2
        assert tree.is_empty() is False
        # Verify size after third insert
        tree.insert('abd')
        assert tree.size == 3
        assert tree.is_empty() is False
        # Verify size after fourth insert
        tree.insert('xyz')
        assert tree.size == 4
        assert tree.is_empty() is False

    def test_size_with_repeated_insert(self):
        tree = PrefixTree()
        # Verify size after initializing tree
        assert tree.size == 0
        assert tree.is_empty() is True
        # Verify size after first insert
        tree.insert('a')
        assert tree.size == 1
        assert tree.is_empty() is False
        # Verify size after repeating first insert
        tree.insert('a')
        assert tree.size == 1
        # Verify size after second insert
        tree.insert('abc')
        assert tree.size == 2
        # Verify size after repeating second insert
        tree.insert('abc')
        assert tree.size == 2
        # Verify size after third insert
        tree.insert('abd')
        assert tree.size == 3
        # Verify size after repeating third insert
        tree.insert('abd')
        assert tree.size == 3
        # Verify size after fourth insert
        tree.insert('xyz')
        assert tree.size == 4
        # Verify size after repeating fourth insert
        tree.insert('xyz')
        assert tree.size == 4

    def test_contains(self):
        strings = ['abc', 'abd', 'a', 'xyz']
        tree = PrefixTree(strings)
        # Verify contains for all substrings
        assert tree.contains('abc') is True
        assert tree.contains('abd') is True
        assert tree.contains('ab') is False
        assert tree.contains('bc') is False
        assert tree.contains('bd') is False
        assert tree.contains('a') is True
        assert tree.contains('b') is False
        assert tree.contains('b') is False
        assert tree.contains('d') is False
        assert tree.contains('xyz') is True
        assert tree.contains('xy') is False
        assert tree.contains('yz') is False
        assert tree.contains('x') is False
        assert tree.contains('y') is False
        assert tree.contains('z') is False

    def test_complete(self):
        strings = ['abc', 'abd', 'a', 'xyz']
        tree = PrefixTree(strings)
        # Verify completions for all substrings
        assert tree.complete('abc') == ['abc']
        assert tree.complete('abd') == ['abd']
        assert tree.complete('ab') == ['abc', 'abd']
        assert tree.complete('bc') == []
        assert tree.complete('bd') == []
        assert tree.complete('a') == ['a', 'abc', 'abd']
        assert tree.complete('b') == []
        assert tree.complete('c') == []
        assert tree.complete('d') == []
        assert tree.complete('xyz') == ['xyz']
        assert tree.complete('xy') == ['xyz']
        assert tree.complete('yz') == []
        assert tree.complete('x') == ['xyz']
        assert tree.complete('y') == []
        assert tree.complete('z') == []

    def test_strings(self):
        tree = PrefixTree()
        input_strings = []  # Strings that have been inserted into the tree
        for string in ['abc', 'abd', 'a', 'xyz']:  # Strings to be inserted
            # Insert new string and add to list of strings already inserted
            tree.insert(string)
            input_strings.append(string)
            # Verify tree can retrieve all strings that have been inserted
            tree_strings = tree.strings()
            assert len(tree_strings) == len(input_strings)  # Check length only
            self.assertCountEqual(tree_strings, input_strings)  # Ignore order


if __name__ == '__main__':
    unittest.main()
