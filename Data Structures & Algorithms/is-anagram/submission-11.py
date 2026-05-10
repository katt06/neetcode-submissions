class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #initial check of lengths
        if(len(s) != len(t)):
            return False

        #make two sep hash maps
        sFreq, tFreq = {}, {};

        #check
        for i in range(len(s)):
            #1 + getting the count of s[i] letter, if can't find it, return 0
            sFreq[s[i]] = 1 + sFreq.get(s[i], 0)
            tFreq[t[i]] = 1 + tFreq.get(t[i], 0)
        return sFreq == tFreq


        

        



        
        