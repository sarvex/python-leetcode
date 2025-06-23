class Solution:
    def maxDistance(self, s: str, k: int) -> int:
        """Maximum Manhattan Distance After K Changes

        Intuition: Track the actual coordinates as we move through the directions,
        then identify opportunities to increase the Manhattan distance by using our
        k changes strategically when the distance decreases.

        Approach: We track (x,y) coordinates as we follow the directions in the string.
        For each step, we calculate the Manhattan distance (|x| + |y|). When the distance
        decreases compared to the previous step, we can use one of our k changes to
        increase the distance by 2 (effectively reversing the direction). We keep track
        of these potential increases and apply them to maximize the overall distance.

        Complexity:
        Time: O(n), where n is the length of string s
        Space: O(n), to store the distances at each step
        """
        # Initialize coordinates and distance list
        x, y = 0, 0
        distances = []

        # Calculate Manhattan distance at each step
        for direction in s:
            if direction == "N":
                y += 1
            elif direction == "W":
                x -= 1
            elif direction == "S":
                y -= 1
            else:  # direction == "E"
                x += 1

            # Add current Manhattan distance to our list
            distances.append(abs(x) + abs(y))

        # Special case: if no changes allowed, return maximum distance
        if k == 0:
            return max(distances)

        n = len(distances)
        if n <= 1:
            return distances[0] if n == 1 else 0

        # Initialize variables for tracking
        cumulative_increase = 0
        max_distance = prev_distance = distances[0]

        # Process each position to maximize distance
        for i in range(1, n):
            # If current distance is less than previous, we can use a change
            # to increase the distance by 2 (reversing direction)
            if distances[i] < prev_distance and k > 0:
                cumulative_increase += 2
                k -= 1

            # Update previous distance for next iteration
            prev_distance = distances[i]

            # Apply the cumulative increase to current distance
            distances[i] += cumulative_increase

            # Update maximum distance seen so far
            max_distance = max(max_distance, distances[i])

        return max_distance
