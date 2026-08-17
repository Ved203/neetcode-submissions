class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        s1=s.lower()
        t1=t.lower()

        freq= {}
        for i in s1:
            freq[i] = freq.get(i,0)+1

        for i in t1:
            freq[i]= freq.get(i,0)-1
        
        for value in freq.values():
            if value != 0:
                return False
        return True
        