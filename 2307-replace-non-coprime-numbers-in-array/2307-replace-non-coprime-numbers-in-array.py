class Solution:
    def replaceNonCoprimes(self, nums):
        def gcd(a, b):
            while b:
                a, b = b, a % b
            return a

        stack = []
        for num in nums:
            stack.append(num)
            # keep merging while last two numbers are not coprime
            while len(stack) > 1:
                a, b = stack[-2], stack[-1]
                g = gcd(a, b)
                if g > 1:  # not coprime
                    lcm = (a * b) // g
                    stack.pop()
                    stack[-1] = lcm
                else:
                    break
        return stack
