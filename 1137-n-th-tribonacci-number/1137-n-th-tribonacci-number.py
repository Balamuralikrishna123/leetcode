class Solution:
    def tribonacci(self, n: int) -> int:
        t0=0
        t1=1
        t2=1
        current = 0
        if n<=1:
            return n
        elif n==2:
            return 1
        else:
            for i in range(2,n):
                current = t0+t1+t2
                t0 = t1
                t1= t2
                t2 = current
        return current
        

        