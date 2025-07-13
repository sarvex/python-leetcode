from typing import List


class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        """Two-pointer approach to match players with trainers.

        Intuition:
        Sort both arrays and use two pointers to find valid matches efficiently.

        Approach:
        1. Sort both players and trainers arrays in ascending order
        2. Use a two-pointer technique to match each player with the first
           available trainer that has sufficient ability
        3. When a match is found, increment the match count and move to the next trainer

        Complexity:
        Time: O(n log n + m log m) where n is the length of players and m is the length of trainers
        Space: O(1) excluding the input arrays

        Args:
            players: List of player abilities
            trainers: List of trainer abilities

        Returns:
            Maximum number of players that can be matched with trainers
        """
        # Sort both arrays in ascending order
        players.sort()
        trainers.sort()

        matches = 0
        trainer_idx = 0

        # Try to match each player with a suitable trainer
        for player_ability in players:
            # Skip trainers with insufficient ability for current player
            while (trainer_idx < len(trainers) and
                   trainers[trainer_idx] < player_ability):
                trainer_idx += 1

            # If we found a suitable trainer, make a match
            if trainer_idx < len(trainers):
                matches += 1
                trainer_idx += 1  # Move to next trainer

        return matches
