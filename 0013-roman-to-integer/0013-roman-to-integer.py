class Solution:
    def romanToInt(self, s):
        values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000
        }

        total = 0
        for i in range(len(s)):
            if i + 1 < len(s) and values[s[i]] < values[s[i + 1]]:
                total -= values[s[i]]
            else:
                total += values[s[i]]

        return total


# Example runs
sol = Solution()
print(sol.romanToInt("III"))      # 3
print(sol.romanToInt("LVIII"))    # 58
print(sol.romanToInt("MCMXCIV"))  # 1994
