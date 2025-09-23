class Solution(object):
    def letterCombinations(self, digits):
        """
        Generates all possible letter combinations for a given digit string.
        :type digits: str
        :rtype: List[str]
        """
        # Edge case: if the input is empty, return an empty list.
        if not digits:
            return []

        # Mapping of digits to letters
        phone_map = {
            "2": "abc",
            "3": "def",
            "4": "ghi",
            "5": "jkl",
            "6": "mno",
            "7": "pqrs",
            "8": "tuv",
            "9": "wxyz"
        }

        result = []

        def backtrack(index, current_combination):
            # Base case: if the combination is complete, add it to the result.
            if index == len(digits):
                result.append(current_combination)
                return

            # Get letters for the current digit
            possible_letters = phone_map[digits[index]]

            # Iterate through the letters and recurse for the next digit
            for letter in possible_letters:
                backtrack(index + 1, current_combination + letter)

        # Start the backtracking process from the first digit (index 0)
        backtrack(0, "")
        
        return result