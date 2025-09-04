class Solution:
    def findClosest(self, x: int, y: int, z: int) -> int:
        """Find the closest person to a target position using distance comparison.
        
        Intuition:
        We need to find which person (at position x or y) is closer to the target 
        position z. If they're equidistant, we return 0 to indicate a tie.
        
        Approach:
        Calculate the absolute distance from each person to the target position
        and compare them to determine the closest one.
        
        Complexity:
        Time: O(1) - constant time operations
        Space: O(1) - no extra space needed
        
        Args:
            x: Position of first person
            y: Position of second person  
            z: Target position
            
        Returns:
            0 if equidistant, 1 if first person closer, 2 if second person closer
        """
        distance_x, distance_y = abs(x - z), abs(y - z)
        
        if distance_x == distance_y:
            return 0
        return 1 if distance_x < distance_y else 2
