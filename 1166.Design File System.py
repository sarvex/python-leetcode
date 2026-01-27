class TrieNode:
    """Trie node representing a path component in the file system."""

    def __init__(self, value: int = -1) -> None:
        self.children: dict[str, TrieNode] = {}
        self.value = value

    def insert(self, path: str, value: int) -> bool:
        """Insert a path with value. Returns False if parent missing or path exists."""
        node = self
        parts = path.split("/")
        for part in parts[1:-1]:
            if part not in node.children:
                return False
            node = node.children[part]
        if parts[-1] in node.children:
            return False
        node.children[parts[-1]] = TrieNode(value)
        return True

    def search(self, path: str) -> int:
        """Search for a path and return its value, or -1 if not found."""
        node = self
        for part in path.split("/")[1:]:
            if part not in node.children:
                return -1
            node = node.children[part]
        return node.value


class FileSystem:
    """Design a file system using a trie structure.

    Intuition:
        Paths form a tree structure naturally represented by a trie, where each
        node corresponds to a path component.

    Approach:
        Use a trie where each node stores children as a dictionary and an
        associated value. createPath validates parent existence and path
        uniqueness. get traverses the trie to find the value.

    Complexity:
        Time: O(k) per operation where k is path depth
        Space: O(total path components)
    """

    def __init__(self) -> None:
        self.trie = TrieNode()

    def createPath(self, path: str, value: int) -> bool:
        """Create a new path with the given value."""
        return self.trie.insert(path, value)

    def get(self, path: str) -> int:
        """Get the value associated with the given path."""
        return self.trie.search(path)
