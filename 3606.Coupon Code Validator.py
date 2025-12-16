from typing import List


class Solution:
    def validateCoupons(
        self, code: List[str], businessLine: List[str], isActive: List[bool]
    ) -> List[str]:
        # Map business lines to their sort order index
        business_order = {
            "electronics": 0,
            "grocery": 1,
            "pharmacy": 2,
            "restaurant": 3,
        }

        valid_coupons = []
        n = len(code)

        for i in range(n):
            c = code[i]
            b = businessLine[i]
            active = isActive[i]

            # Condition 3: Must be active
            if not active:
                continue

            # Condition 2: Must be a valid business line
            if b not in business_order:
                continue

            # Condition 1: Code non-empty and valid chars
            if not c:
                continue

            is_valid_code = True
            for char in c:
                if not (char.isalnum() or char == "_"):
                    is_valid_code = False
                    break

            if not is_valid_code:
                continue

            # Store tuple of (sort_index, code_string)
            # Tuple comparison handles the sorting requirements:
            # 1. Primary: Business line order (via index)
            # 2. Secondary: Code lexicographical order
            valid_coupons.append((business_order[b], c))

        # Sort and extract codes
        valid_coupons.sort()
        return [vc[1] for vc in valid_coupons]
