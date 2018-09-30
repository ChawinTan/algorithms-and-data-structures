class Solution(object):
      def partitionDisjoint(self, A):
        B = A[:]
        n = len(A)
        for i in range(n - 1)[::-1]:    #track the minimum value of B at each point from the back, since we know that a partition is guaranteed
            B[i] = min(A[i], B[i + 1])
        # print(B)
        pmax = 0
        for i in range(1,n):           # the moment the max value of A is more than min value of B, partition is set
            pmax = max(pmax, A[i-1])
            if pmax <= B[i]:
                return i
