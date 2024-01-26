class Solution:
    def fib(self, n: int) -> int:
        if n<=1: 
            return n

        p1 = 0
        p2 = 1
        current = 0

        for i in range (1, n):
            current = p1+p2
            p1=p2
            p2=current
        return current
        