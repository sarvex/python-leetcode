from collections import defaultdict
from typing import Dict, List, Any


class Solution:
    """Solution for LeetCode 1948: Delete Duplicate Folders in System.

    Tagline: Dictionary-based serialization for duplicate folder detection

    Intuition:
    To identify duplicate folder structures, we need a unique string representation
    of each subtree. By serializing folder structures into strings, we can efficiently
    compare and identify duplicates.

    Approach:
    1. Build a tree using nested dictionaries from the given paths
    2. Serialize each subtree into a unique string representation
    3. Track duplicate subtrees based on their serialized form
    4. Mark duplicate subtrees for deletion (using a special marker)
    5. Collect and return paths that aren't marked as duplicates

    Complexity:
    Time: O(N * L), where N is the number of paths and L is the average path length
    Space: O(N * L) for storing the tree structure and serialized representations
    """

    def deleteDuplicateFolder(self, paths: List[List[str]]) -> List[List[str]]:
        """Delete duplicate folder structures from the file system.

        Args:
            paths: List of paths, where each path is a list of folder names

        Returns:
            List of paths after removing duplicate folder structures
        """
        # Build the directory tree using nested dictionaries
        tree: Dict[str, Any] = {}
        for path in paths:
            node = tree
            for folder in path:
                node = node.setdefault(folder, {})

        # Track duplicate subtrees based on their serialized form
        duplicates = defaultdict(list)

        def serialize(node: Dict[str, Any]) -> str:
            """Serialize a subtree into a unique string representation.

            The serialization format is: (child1(grandchild1)child2(grandchild2)...)
            where children are sorted alphabetically to ensure consistent ordering.

            Args:
                node: Current node in the tree (dictionary of children)

            Returns:
                String representation of the subtree
            """
            if not node:
                return "()"

            # Create serialized strings for each child, sorted by folder name
            child_serializations = "".join(
                child + serialize(child_node)
                for child, child_node in sorted(node.items())
            )

            # Form the complete serialization for this subtree
            serialized = "(" + child_serializations + ")"

            # Track this node in the duplicates map
            duplicates[serialized].append(node)

            return serialized

        # Serialize the entire tree and identify duplicates
        serialize(tree)

        # Mark duplicate subtrees with a special marker
        for nodes in duplicates.values():
            if len(nodes) > 1:  # Found duplicate subtrees
                for node in nodes:
                    node.clear()  # Remove all children
                    node["#"] = True  # Mark as duplicate

        # Collect paths that aren't marked as duplicates
        result: List[List[str]] = []

        def collect_paths(node: Dict[str, Any], current_path: List[str]) -> None:
            """Collect valid paths that don't contain duplicate subtrees.

            Args:
                node: Current node in the tree
                current_path: Path traversed so far
            """
            for folder, child_node in node.items():
                # Skip duplicate subtrees
                if "#" in child_node:
                    continue

                # Add this folder to the path
                new_path = current_path + [folder]
                result.append(new_path)  # Record this path

                # Continue traversal
                collect_paths(child_node, new_path)

        # Collect all valid paths
        collect_paths(tree, [])
        return result
