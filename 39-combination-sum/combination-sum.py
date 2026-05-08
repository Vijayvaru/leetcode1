class Solution:
    def combinationSum(self, candidates, target):
        result = []

        def backtrack(start, path, total):
            # If target is reached
            if total == target:
                result.append(path[:])
                return

            # If total exceeds target
            if total > target:
                return

            # Try all candidates starting from current index
            for i in range(start, len(candidates)):
                path.append(candidates[i])

                # Reuse same element, so pass i again
                backtrack(i, path, total + candidates[i])

                # Remove last element (backtrack)
                path.pop()

        backtrack(0, [], 0)
        return result