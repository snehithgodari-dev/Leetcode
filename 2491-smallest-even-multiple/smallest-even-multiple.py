class Solution:
    def smallestEvenMultiple(self, n: int) -> int:
        sem = (2*n)// (gcd(2,n))
        return sem
    m = 2
    def gcd(m,n):
        while n!= 0:
            m,n = n , (m%n)
        return m




        