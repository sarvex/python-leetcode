class Solution:
    def countTriplets(self, arr: list[int]) -> int:
        """Count triplets (i,j,k) where XOR of arr[i..j-1] equals XOR of arr[j..k].

        Intuition:
            Use prefix XOR to efficiently compute XOR of any subarray. Two
            subarrays have equal XOR iff their combined XOR is zero.

        Approach:
            Build a prefix XOR array. Enumerate all triplets (i, j, k) and
            check if prefix[j] ^ prefix[i] equals prefix[k+1] ^ prefix[j],
            which simplifies to prefix[i] == prefix[k+1].

        Complexity:
            Time: O(n^3) with three nested loops
            Space: O(n) for prefix XOR array
        """
        length = len(arr)
        prefix_xor = [0] * (length + 1)
        for i in range(length):
            prefix_xor[i + 1] = prefix_xor[i] ^ arr[i]

        result = 0
        for i in range(length - 1):
            for j in range(i + 1, length):
                for k in range(j, length):
                    xor_a = prefix_xor[j] ^ prefix_xor[i]
                    xor_b = prefix_xor[k + 1] ^ prefix_xor[j]
                    if xor_a == xor_b:
                        result += 1
        return result
