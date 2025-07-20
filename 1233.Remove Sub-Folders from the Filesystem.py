from typing import List


class Solution:
    def removeSubfolders(self, folder: List[str]) -> List[str]:
        """Sort and filter approach to remove subfolders from a filesystem.

        Intuition:
        When folders are sorted lexicographically, any subfolder will appear after its parent.
        By checking if the current folder starts with a previous folder + '/', we can identify subfolders.

        Approach:
        1. Sort the folder list lexicographically
        2. Add the first folder to our result list
        3. For each subsequent folder, check if it's a subfolder of the last added folder
           - A folder is a subfolder if it starts with the parent folder path + '/'
        4. Only add folders that are not subfolders of any previously added folder

        Complexity:
        Time: O(n log n) where n is the number of folders (dominated by sorting)
        Space: O(n) for storing the result and sorting
        """
        if not folder:
            return []

        folder.sort()
        result = [folder[0]]

        for current_folder in folder[1:]:
            last_folder = result[-1]
            last_folder_len = len(last_folder)

            # Check if current folder is a subfolder of the last added folder
            is_subfolder = (
                last_folder_len < len(current_folder) and
                current_folder.startswith(last_folder) and
                current_folder[last_folder_len] == '/'
            )

            if not is_subfolder:
                result.append(current_folder)

        return result
