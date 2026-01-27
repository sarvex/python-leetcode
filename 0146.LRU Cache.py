class Node:
    """Doubly linked list node for LRU Cache."""

    def __init__(self, key: int = 0, val: int = 0) -> None:
        self.key = key
        self.val = val
        self.prev: Node | None = None
        self.next: Node | None = None


class LRUCache:
    """LRU Cache using doubly linked list and hash map.

    Intuition:
        Use a hash map for O(1) lookups and a doubly linked list to maintain
        access order, with most recently used items near the head.

    Approach:
        Maintain a doubly linked list with sentinel head and tail nodes.
        On get, move the accessed node to the head. On put, add new nodes
        to the head and evict the tail node when capacity is exceeded.

    Complexity:
        Time: O(1) for both get and put operations
        Space: O(capacity) for storing the cache entries
    """

    def __init__(self, capacity: int) -> None:
        """Initialize LRU cache with given capacity."""
        self.cache: dict[int, Node] = {}
        self.head = Node()
        self.tail = Node()
        self.capacity = capacity
        self.size = 0
        self.head.next = self.tail
        self.tail.prev = self.head

    def get(self, key: int) -> int:
        """Return value for key and mark as recently used, or -1 if not found."""
        if key not in self.cache:
            return -1
        node = self.cache[key]
        self.move_to_head(node)
        return node.val

    def put(self, key: int, value: int) -> None:
        """Insert or update key-value pair, evicting LRU entry if at capacity."""
        if key in self.cache:
            node = self.cache[key]
            node.val = value
            self.move_to_head(node)
        else:
            node = Node(key, value)
            self.cache[key] = node
            self.add_to_head(node)
            self.size += 1
            if self.size > self.capacity:
                node = self.remove_tail()
                self.cache.pop(node.key)
                self.size -= 1

    def move_to_head(self, node: Node) -> None:
        """Move existing node to head of list."""
        self.remove_node(node)
        self.add_to_head(node)

    def remove_node(self, node: Node) -> None:
        """Remove node from its current position."""
        node.prev.next = node.next
        node.next.prev = node.prev

    def add_to_head(self, node: Node) -> None:
        """Insert node right after the sentinel head."""
        node.next = self.head.next
        node.prev = self.head
        self.head.next = node
        node.next.prev = node

    def remove_tail(self) -> Node:
        """Remove and return the least recently used node."""
        node = self.tail.prev
        self.remove_node(node)
        return node
