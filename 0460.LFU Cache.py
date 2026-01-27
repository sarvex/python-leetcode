from collections import defaultdict


class Node:
    """Doubly linked list node storing a key-value pair with access frequency."""

    def __init__(self, key: int, value: int) -> None:
        """Initialize node with key, value, frequency 1, and null neighbors."""
        self.key = key
        self.value = value
        self.freq = 1
        self.prev: Node | None = None
        self.next: Node | None = None


class DoublyLinkedList:
    """Doubly linked list with sentinel head and tail for O(1) insertions and removals."""

    def __init__(self) -> None:
        """Initialize with sentinel head and tail nodes."""
        self.head = Node(-1, -1)
        self.tail = Node(-1, -1)
        self.head.next = self.tail
        self.tail.prev = self.head

    def add_first(self, node: Node) -> None:
        """Insert node at the front of the list (most recently used)."""
        node.prev = self.head
        node.next = self.head.next
        self.head.next.prev = node
        self.head.next = node

    def remove(self, node: Node) -> Node:
        """Remove and return the given node from the list."""
        node.next.prev = node.prev
        node.prev.next = node.next
        node.next, node.prev = None, None
        return node

    def remove_last(self) -> Node:
        """Remove and return the least recently used node (before tail)."""
        return self.remove(self.tail.prev)

    def is_empty(self) -> bool:
        """Check if the list contains no data nodes."""
        return self.head.next == self.tail


class LFUCache:
    """Least Frequently Used cache with O(1) get and put operations.

    Uses a hash map for key-to-node lookup and a frequency map of doubly
    linked lists to maintain LRU ordering within each frequency bucket.
    """

    def __init__(self, capacity: int) -> None:
        """Initialize cache with given capacity."""
        self.capacity = capacity
        self.min_freq = 0
        self.map: dict[int, Node] = {}
        self.freq_map: defaultdict[int, DoublyLinkedList] = defaultdict(
            DoublyLinkedList
        )

    def get(self, key: int) -> int:
        """Retrieve value by key, updating access frequency. Returns -1 if absent.

        Intuition:
            Look up the node, increment its frequency, and return the value.

        Approach:
            1. If key not found, return -1.
            2. Increment the node's frequency bucket.
            3. Return the node's value.

        Complexity:
            Time: O(1).
            Space: O(1).
        """
        if self.capacity == 0 or key not in self.map:
            return -1
        node = self.map[key]
        self._increment_freq(node)
        return node.value

    def put(self, key: int, value: int) -> None:
        """Insert or update a key-value pair, evicting LFU entry if at capacity.

        Intuition:
            If key exists, update value and frequency. Otherwise, evict the
            least frequently (and least recently) used entry if full, then insert.

        Approach:
            1. If key exists, update value and increment frequency.
            2. If at capacity, evict from the min-frequency list.
            3. Insert new node with frequency 1 and reset min_freq to 1.

        Complexity:
            Time: O(1).
            Space: O(1).
        """
        if self.capacity == 0:
            return
        if key in self.map:
            node = self.map[key]
            node.value = value
            self._increment_freq(node)
            return
        if len(self.map) == self.capacity:
            evict_list = self.freq_map[self.min_freq]
            evicted = evict_list.remove_last()
            self.map.pop(evicted.key)
        node = Node(key, value)
        self._add_node(node)
        self.map[key] = node
        self.min_freq = 1

    def _increment_freq(self, node: Node) -> None:
        """Move node from its current frequency bucket to the next one."""
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.remove(node)
        if freq_list.is_empty():
            self.freq_map.pop(freq)
            if freq == self.min_freq:
                self.min_freq += 1
        node.freq += 1
        self._add_node(node)

    def _add_node(self, node: Node) -> None:
        """Add node to the front of its frequency bucket's list."""
        freq = node.freq
        freq_list = self.freq_map[freq]
        freq_list.add_first(node)
        self.freq_map[freq] = freq_list
