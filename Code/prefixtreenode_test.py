#!python3

from prefixtreenode import PrefixTreeNode
import unittest


class PrefixTreeNodeTest(unittest.TestCase):

    def test_init_and_properties(self):
        character = 'a'
        node = PrefixTreeNode(character)
        # Verify node character
        assert isinstance(node.character, str)
        print(node.character)
        assert node.character == 'a'
        # Verify children nodes structure
        assert isinstance(node.children, PrefixTreeNode.CHILDREN_TYPE)
        assert len(node.children) == 26
        assert node.children == [None] * 26
        assert node.num_children() == 0
        # Verify terminal boolean
        assert node.terminal is False
        assert node.is_terminal() is False

    def test_child_methods(self):
        # Create node 'A' and verify it does not have any children
        node_A = PrefixTreeNode('a')
        assert node_A.num_children() == 0
        assert node_A.has_child('b') is False
        # Verify getting child from node 'A' raises error
        with self.assertRaises(ValueError):
            node_A.get_child('b')
        # Create node 'B' and add it as child to node 'A'
        node_B = PrefixTreeNode('b')
        node_A.add_child('b', node_B)
        # Verify node 'A' has node 'B' as child
        assert node_A.num_children() == 1
        assert node_A.has_child('B') is True
        assert node_A.get_child('B') is node_B
        # Verify adding node 'B' as child to node 'A' again raises error
        with self.assertRaises(ValueError):
            node_A.add_child('B', node_B)
        # Create node 'C' and add it as another child to node 'A'
        node_C = PrefixTreeNode('C')
        node_A.add_child('C', node_C)
        # Verify node 'A' has both nodes 'B' and 'C' as children
        assert node_A.num_children() == 2
        assert node_A.has_child('B') is True
        assert node_A.has_child('C') is True
        assert node_A.get_child('C') is node_C
        # Verify adding node 'C' as child to node 'A' again raises error
        with self.assertRaises(ValueError):
            node_A.add_child('C', node_C)
