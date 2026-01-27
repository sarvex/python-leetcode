class TrieNode:
    def __init__(self) -> None:
        self.name: str | None = None
        self.is_file: bool = False
        self.content: list[str] = []
        self.children: dict[str, TrieNode] = {}

    def insert(self, path: str, is_file: bool) -> "TrieNode":
        node = self
        parts = path.split("/")
        for part in parts[1:]:
            if part not in node.children:
                node.children[part] = TrieNode()
            node = node.children[part]
        node.is_file = is_file
        if is_file:
            node.name = parts[-1]
        return node

    def search(self, path: str) -> "TrieNode | None":
        node = self
        if path == "/":
            return node
        parts = path.split("/")
        for part in parts[1:]:
            if part not in node.children:
                return None
            node = node.children[part]
        return node


class FileSystem:
    """In-memory file system using a trie structure for path storage.

    Intuition:
        A file system is naturally a tree structure. Using a trie where each
        node represents a directory or file allows efficient path traversal.

    Approach:
        1. Use a trie with each node storing children directories/files.
        2. For ls: search the path and return sorted children or file name.
        3. For mkdir: insert path creating nodes as needed.
        4. For file operations: insert as file node and append/read content.

    Complexity:
        Time: O(L) per operation where L is the path length
        Space: O(total characters stored across all paths and file contents)
    """

    def __init__(self) -> None:
        self.root = TrieNode()

    def ls(self, path: str) -> list[str]:
        node = self.root.search(path)
        if node is None:
            return []
        if node.is_file:
            return [node.name]
        return sorted(node.children.keys())

    def mkdir(self, path: str) -> None:
        self.root.insert(path, False)

    def addContentToFile(self, filePath: str, content: str) -> None:
        node = self.root.insert(filePath, True)
        node.content.append(content)

    def readContentFromFile(self, filePath: str) -> str:
        node = self.root.search(filePath)
        return "".join(node.content)
