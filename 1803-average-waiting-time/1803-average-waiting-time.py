class Solution:
    def averageWaitingTime(self, A):
        wait = cur = 0.
        for t, d in A:
            cur = max(cur, t) + d
            wait += cur - t
        return wait / len(A)