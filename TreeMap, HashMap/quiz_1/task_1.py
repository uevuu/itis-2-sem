"""rewrite quiz 1"""


class VersionedTree:
    """VersionedTree"""

    def __init__(self, zero_version=None):
        self.trees = [zero_version]

    def add(self, value: int) -> None:
        """add new version of tree"""
        curr_tree = self.trees[-1]
        self.trees.append(add_(curr_tree, value))

    def contains(self, version: int, value: int) -> bool:
        """checking for availability"""
        curr_tree = self.trees[version]
        return contains_(curr_tree, value)

    def height(self, version: int) -> int:
        """get height"""
        curr_version = self.trees[version]
        return tree_lenght(curr_version)


def add_(tree: tuple, value: int) -> tuple:
    """add value in tree"""
    if not (tree, tuple):
        return tuple((value, None, None))
    if value < tree[0]:
        return tuple((tree[0], add_(tree[1], value), tree[2]))
    if value > tree[0]:
        return tuple((tree[0], tree[1], add_(tree[2], value)))


def contains_(tree: tuple, value: int) -> bool:
    """checking for availability"""
    if not isinstance(tree, tuple):
        return False
    if value < tree[0]:
        return contains_(tree[1], value)
    if value > tree[0]:
        return contains_(tree[2], value)
    return True


def tree_lenght(tree: tuple) -> int:
    """get lenght"""
    if not isinstance(tree, tuple):
        return 0
    return 1 + max(tree_lenght(tree[1]), tree_lenght(tree[2]))
