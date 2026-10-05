class Solution:
    def findContentChildren(self, g, s):
        g.sort()
        s.sort()
        
        i = 0
        n = len(g)
        for cookie in s:
            if i == n:
                break
            if cookie >= g[i]:
                i += 1
                
        return i