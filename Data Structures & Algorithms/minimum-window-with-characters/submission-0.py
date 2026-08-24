from collections import Counter

class Solution:
    def minWindow(self, s: str, t: str) -> str:

        # Count required characters
        required_count = Counter(t)

        # Count characters in current window
        freq = {}

        left = 0
        matched = 0
        required = len(required_count)

        result = ""
        min_length = float("inf")

        # Expand window using right
        for right in range(len(s)):

            char = s[right]

            freq[char] = freq.get(char, 0) + 1

            # Check if this character requirement is satisfied
            if char in required_count:
                if freq[char] == required_count[char]:
                    matched += 1

            # If all required characters are present
            while matched == required:

                # Check if current window is smaller
                window_length = right - left + 1

                if window_length < min_length:
                    min_length = window_length
                    result = s[left:right + 1]

                # Remove left character
                left_char = s[left]
                freq[left_char] -= 1

                # Window is no longer valid
                if left_char in required_count:
                    if freq[left_char] < required_count[left_char]:
                        matched -= 1

                left += 1

        return result