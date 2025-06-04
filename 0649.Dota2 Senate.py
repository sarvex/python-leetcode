from collections import deque


class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        """Determine which party will win the Dota2 Senate.

        Intuition: Use queues to simulate the voting process, where senators take turns
        banning the next opposing senator.

        Approach:
        1. Create separate queues for Radiant and Dire senators, storing their positions
        2. Simulate the voting process where the senator with smaller index bans the next
           opposing senator and gets to vote again in the next round
        3. Continue until one party has no senators left

        Complexity:
        Time: O(n), where n is the length of the senate string
        Space: O(n), for storing the senator positions in queues

        Args:
            senate: A string representing the initial senate state ('R' for Radiant, 'D' for Dire)

        Returns:
            The name of the winning party: "Radiant" or "Dire"
        """
        radiant = deque()
        dire = deque()

        # Store initial positions of each senator
        for position, senator in enumerate(senate):
            if senator == 'R':
                radiant.append(position)
            else:
                dire.append(position)

        senate_size = len(senate)

        # Simulate the voting process
        while radiant and dire:
            radiant_position = radiant.popleft()
            dire_position = dire.popleft()

            # Senator with smaller index bans the other and votes again in the next round
            if radiant_position < dire_position:
                radiant.append(radiant_position + senate_size)
            else:
                dire.append(dire_position + senate_size)

        return 'Radiant' if radiant else 'Dire'
