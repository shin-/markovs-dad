from collections import Counter
from random import choice


class WeightedGraphNode(object):
    """
        Represents a node inside a WeightedGraph. It references
        its followers inside a collections.Counter object to allow
        counting the number of times a given follower appears in
        the base corpus.
    """
    def __init__(self, word):
        self.word = word
        self.followers = Counter()

    def add_follower(self, node):
        """
            Add a follower reference from this node to the provided node.
            If already present, the counter will simply be incremented.
        """
        self.followers.update([node])

    def pick_follower(self):
        """
            Pick and return a random follower node. More frequent followers
            are more likely to be picked. If this node has no followers, this
            method returns None.
        """
        elements = list(self.followers.elements())
        if not elements:
            return None
        return choice(elements)


class WeightedGraph(object):
    """
        This graph object holds n instances of WeightedGraphNode.
        It maintains an index, which is a (word -> node) mapping,
        to avoid creating duplicate nodes for a given word. It
        also maintains a set of possible sentence starters that can
        be picked from to initiate a generated chain.
    """
    def __init__(self):
        self.index = {}
        self.starters = set()

    def add_word(self, word, after=None):
        """
            Add the given word to the graph. If no record of this word
            currently exists, a new node is created and stored. If the
            `after` parameter is None, the word is a viable sentence starter
            and added to the `starters` set. Otherwise, the node for `word` is
            added as a follower to the node in `after`.
        """
        if word in self.index:
            node = self.index[word]
        else:
            node = WeightedGraphNode(word)
            self.index[word] = node

        if after is None:
            self.starters.add(node)
        else:
            after.add_follower(node)

        return node
