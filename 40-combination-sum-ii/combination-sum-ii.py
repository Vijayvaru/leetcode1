class Solution:
    def combinationSum2(self, candidates, target):
        result = []

        # Sort to handle duplicates
        candidates.sort()

        def backtrack(start, path, total):
            # Target reached
            if total == target:
                result.append(path[:])
                return

            # If total exceeds target
            if total > target:
                return

            for i in range(start, len(candidates)):

                # Skip duplicates
                if i > start and candidates[i] == candidates[i - 1]:
                    continue

                # If current number exceeds target
                if total + candidates[i] > target:
                    break

                path.append(candidates[i])

                # Move to next index (each number used once)
                backtrack(i + 1, path, total + candidates[i])

                # Backtrack
                path.pop()

        backtrack(0, [], 0)

        return result