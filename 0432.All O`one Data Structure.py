class Node:
    """Doubly linked list node holding a set of keys with the same count."""

    def __init__(self, key: str = "", count: int = 0) -> None:
        """Initialize node with a key, count, and neighbor pointers."""
        self.prev: Node | None = None
        self.next: Node | None = None
        self.count = count
        self.keys = {key}

    def insert(self, node: "Node") -> "Node":
        """Insert a new node immediately after this node."""
        node.prev = self
        node.next = self.next
        node.prev.next = node
        node.next.prev = node
        return node

    def remove(self) -> None:
        """Remove this node from the doubly linked list."""
        self.prev.next = self.next
        self.next.prev = self.prev


class AllOne:
    """All O(1) data structure supporting increment, decrement, and min/max key queries.

    Intuition:
        A doubly linked list ordered by count allows O(1) access to min and
        max keys at the head and tail. A hash map from keys to their bucket
        nodes enables O(1) lookups for increment and decrement.

    Approach:
        Maintain a circular doubly linked list of count buckets, each holding
        a set of keys with that count. A sentinel root node simplifies edge
        cases. On increment, move the key to the next higher bucket (creating
        one if needed). On decrement, move to the next lower bucket or remove
        the key if count reaches zero. Empty buckets are removed immediately.

    Complexity:
        Time: O(1) per inc, dec, getMaxKey, and getMinKey
        Space: O(n) where n is the number of distinct keys
    """

    def __init__(self) -> None:
        """Initialize with a sentinel root node forming a circular list."""
        self.root = Node()
        self.root.next = self.root
        self.root.prev = self.root
        self.nodes: dict[str, Node] = {}

    def inc(self, key: str) -> None:
        """Increment the count of key by 1, creating it if absent."""
        root, nodes = self.root, self.nodes
        if key not in nodes:
            if root.next == root or root.next.count > 1:
                nodes[key] = root.insert(Node(key, 1))
            else:
                root.next.keys.add(key)
                nodes[key] = root.next
        else:
            current = nodes[key]
            next_node = current.next
            if next_node == root or next_node.count > current.count + 1:
                nodes[key] = current.insert(Node(key, current.count + 1))
            else:
                next_node.keys.add(key)
                nodes[key] = next_node
            current.keys.discard(key)
            if not current.keys:
                current.remove()

    def dec(self, key: str) -> None:
        """Decrement the count of key by 1, removing it if count reaches 0."""
        root, nodes = self.root, self.nodes
        current = nodes[key]
        if current.count == 1:
            nodes.pop(key)
        else:
            prev_node = current.prev
            if prev_node == root or prev_node.count < current.count - 1:
                nodes[key] = prev_node.insert(Node(key, current.count - 1))
            else:
                prev_node.keys.add(key)
                nodes[key] = prev_node
        current.keys.discard(key)
        if not current.keys:
            current.remove()

    def getMaxKey(self) -> str:
        """Return any key with the maximum count."""
        return next(iter(self.root.prev.keys))

    def getMinKey(self) -> str:
        """Return any key with the minimum count."""
        return next(iter(self.root.next.keys))
