class Solution:
    def distributeCandies(self, candies: int, num_people: int) -> list[int]:
        """Distribute candies in increasing amounts round-robin.

        Intuition:
            Give 1 candy to the first person, 2 to the second, and so on in a
            round-robin fashion until all candies are distributed.

        Approach:
            Iterate with an incrementing counter, giving min(remaining, counter+1)
            candies to each person in round-robin order until no candies remain.

        Complexity:
            Time: O(sqrt(candies)) since we give ~k candies on turn k
            Space: O(num_people) for the result array
        """
        result = [0] * num_people
        turn = 0
        while candies:
            give = min(candies, turn + 1)
            result[turn % num_people] += give
            candies -= give
            turn += 1
        return result
