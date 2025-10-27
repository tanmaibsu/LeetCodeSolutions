class Solution:
    def fib(self, n: int) -> int:

        #recursion
        # if n == 0:
        #     return 0
        # if n == 1 or n == 2:
        #     return 1
        
        # return self.fib(n - 1) + self.fib(n - 2)

         # Bottom-up appraoch
        if n <= 1:
            return n

        memo = [0]*(n+1)

        memo[1] = 1

        for i in range(2, n+1):
            memo[i] = memo[i - 1] + memo[i - 2]
        
        return memo[-1]


s = Solution()
print(s.fib(3))