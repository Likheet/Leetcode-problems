class Solution:
    def maximumGain(self, s: str, x: int, y: int) -> int:
        a, b = "a", "b"
        if x < y: 
            x, y = y, x
            a, b = b, a
        ans = cnt0 = cnt1 = 0
        for c in s: 
            if c not in "ab": 
                ans += min(cnt0, cnt1) * y
                cnt0 = cnt1 = 0 
            elif c == b:
                if cnt0: 
                    cnt0 -= 1
                    ans += x
                else: cnt1 += 1
            else: cnt0 += 1
        return ans + min(cnt0, cnt1) * y