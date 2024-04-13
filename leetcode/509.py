class Solution:
    memo = {}
    def fib(self, n: int) -> int:
        answer = 0
        # Got this idea from a solution - to store intermediate results
        if n in self.memo:
            return self.memo[n]
        if n == 0:
            return 0
        elif n == 1:
            return 1
        else:
            answer = self.fib(n-1) + self.fib(n-2)
            self.memo[n] = answer
        return answer
