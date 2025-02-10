'''
3174. Clear Digits

You are given a string s.
Your task is to remove all digits by doing this operation repeatedly:
    Delete the first digit and the closest non-digit character to its left.
Return the resulting string after removing all digits.

Example 1:
Input: s = "abc"
Output: "abc"
Explanation:
There is no digit in the staAring.

Example 2:
Input: s = "cb34"
Output: ""
Explanation:
First, we apply the operation on s[2], and s becomes "c4".
Then we apply the operation on s[1], and s becomes "".


Constraints:

    1 <= s.length <= 100
    s consists only of lowercase English letters and digits.
    The input is generated such that it is possible to delete all digits.
'''

class Solution:
    def clearDigits(self, s: str) -> str:
        l = list(s)

        while any(c.isdigit() for c in l):
            idx = -1
            for i in range(len(l)):
                if l[i].isdigit():
                    idx = i
                    break

            if idx != -1:
                charidx = idx-1
                while charidx >= 0 and l[charidx].isdigit():
                    charidx -= 1

                if charidx >= 0:
                    l.pop(idx)
                    l.pop(charidx)
                else:
                    l.pop(idx)
        return ''.join(l)

# testing
sol = Solution()
print(sol.clearDigits("cb34"))
