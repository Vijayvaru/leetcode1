class Solution:
    def isMatch(self, s, p):
        s_ptr = 0
        p_ptr = 0
        star = -1
        match = 0

        while s_ptr < len(s):

            # Match character or '?'
            if p_ptr < len(p) and (p[p_ptr] == s[s_ptr] or p[p_ptr] == '?'):
                s_ptr += 1
                p_ptr += 1

            # If pattern has '*'
            elif p_ptr < len(p) and p[p_ptr] == '*':
                star = p_ptr
                match = s_ptr
                p_ptr += 1

            # Backtrack to last '*'
            elif star != -1:
                p_ptr = star + 1
                match += 1
                s_ptr = match

            else:
                return False

        # Skip remaining '*'
        while p_ptr < len(p) and p[p_ptr] == '*':
            p_ptr += 1

        return p_ptr == len(p)