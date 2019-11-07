
class TrieNode(object):

    def __init__(self, data):
        """Initialize the Trie node with the given data"""
        self.data = data
        self.next = [None] * 26

    def __repr__(self):
        return "TrieNode({!r})".format(self.data)

    def is_leaf(self):
        """Return True if this node is a leaf (has no children)."""
        return self.next == [None] * 26

    def is_branch(self):
        """Return True if this node is a branch (has at least one child)."""
        return self.next != [None] * 26

    def height(self):
        """Return the height of this node (the number of edges on the longest
           downward path from this node to a descendant leaf node).
           Best and worst case running time: O(n) where n is the number of nodes in the tree"""

        if self.is_leaf():
            return 0

        all_path = [0] * 26

        for i in range(26):
            if self.next[i] is not None:
                all_path[i] += self.next[i].height()

        return max(all_path) + 1


class Trie(object):

    def __init__(self, vocabulary=None):
        self.root = TrieNode(None)
        self.size = 0

        if vocabulary is not None:
            for word in vocabulary:
                self.insert(word)

    def __repr__(self):
        """Return a string representation of this Trie."""
        return 'Trie({} nodes)'.format(self.size)

    def height(self):
        """Return the height of this trie (the number of edges on the longest
           downward path from this tree's root node to a descendant leaf node).
           Best and worst case running time: O(n) where n is the number nodes in the tree"""
        return self.root.height()

    def insert(self, word):
        """
        :param word: A string of the word that will be use to create a path and the data store at the end.
        """
        self._insert(word.lower(), word, self.root)

    def autocomplete(self, word):
        """Find the end of the given word, then do in order traversal to find other words with matching prefix"""
        end_node = self.search(word)

        if end_node is None:
            return []

        result = []

        if end_node.data is not None:
            result.append(end_node.data)

        self.in_order_traversal(end_node, result.append)

        return result

    def all_words(self):
        result = []
        self.in_order_traversal(self.root, result.append)
        return result

    def search(self, word):
        """
        :param word: A string that will use as the path of for this Trie
        :return: The end node of the
        """
        node = self._find_node_recursive(word, self.root)
        return node

    def _find_node_recursive(self, word, node):
        """
        :param word: A string that will be use as the path when traversing
        :param node: The current node when traversing the Trie
        :return: The node at the end of the word or None if the path doesn't exist
        """
        if len(word) == 0:
            return node

        index = ord(word[0]) - 97
        remainder = word[1:]

        if node.next[index] is not None:
            node = self._find_node_recursive(remainder, node.next[index])
            return node
        else:
            return None

    def in_order_traversal(self, root, visit):
        """Traverse the trie in order with the given root node"""
        for child in root.next:
            if child is not None:
                self.in_order_traversal(child, visit)
                if child.data is not None:
                    visit(child.data)

    def _insert(self, word, data, node):
        """
        :param word: A string of the word that will be use to create a path
        :param data: A string that will be store at the end of the path
        :param node: The current Trie node along the path

        This function will call itself recursively until it put the data at the end of the path made from word
        """
        if len(word) == 0:
            node.data = data
            self.size += 1
            return

        if word[0] == '-':
            word = word[1:]

        index = ord(word[0]) - 97  # Get the ordinal value of the first character
        remainder = word[1:]  # Reduce the word

        if node.next[index] is None:
            node.next[index] = TrieNode(None)

        self._insert(remainder, data, node.next[index])


if __name__ == "__main__":
    file_name = 'prefixes15.txt'
    word_list = []
    with open(file_name) as file:
        word_list = [line.strip() for line in file]

    trie = Trie(word_list)
    print(trie.all_words())
    print(trie.autocomplete('math'))
