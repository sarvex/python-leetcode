from collections import defaultdict


class Solution:
    def findDuplicate(self, paths: list[str]) -> list[list[str]]:
        """Group duplicate files by content using a hash map.

        Intuition:
            Parse each path entry to extract file content, then group files
            sharing the same content together. Return groups with duplicates.

        Approach:
            1. For each path string, split into directory and file entries.
            2. Extract filename and content from each file entry.
            3. Use a dictionary mapping content to list of full file paths.
            4. Return only groups with more than one file.

        Complexity:
            Time: O(n * k) where n is number of paths and k is average files per path
            Space: O(n * k)
        """
        content_map = defaultdict(list)
        for path in paths:
            parts = path.split()
            for file_entry in parts[1:]:
                paren_index = file_entry.find("(")
                filename, content = (
                    file_entry[:paren_index],
                    file_entry[paren_index + 1 : -1],
                )
                content_map[content].append(parts[0] + "/" + filename)
        return [files for files in content_map.values() if len(files) > 1]
