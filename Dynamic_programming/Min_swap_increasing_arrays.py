class Solution:
    def minSwap(self, A, B):
            N = len(A)
            not_swap, swap = [N] * N, [N] * N
            not_swap[0], swap[0] = 0, 1
            for i in range(1, N):
                if A[i - 1] < A[i] and B[i - 1] < B[i]:  #check againts the given numbers
                    not_swap[i] = not_swap[i - 1]
                    swap[i] = swap[i - 1] + 1
                if A[i - 1] < B[i] and B[i - 1] < A[i]:  #if A[i-1] >= B[i-1], no point swapping
                    not_swap[i] = min(not_swap[i], swap[i - 1])  #smaller choice between dun swap above, swap on previous since we chose not to currently 
                    swap[i] = min(swap[i], not_swap[i - 1] + 1)  #smaller choice between swap already above, not swap previous +1 if chose to swap
            return min(swap[-1], not_swap[-1])
