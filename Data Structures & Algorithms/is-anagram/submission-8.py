class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        #make two sep hash maps
        sFreq = {};
        tFreq = {};

        for i in s:
            #if letter is not in sFreq
            if i in sFreq:
                sFreq[i] += 1;
            else :
                sFreq[i] = 1;

        for i in t:
            #if letter is not in sFreq
            if i in tFreq:
                tFreq[i] += 1;
            else :
                tFreq[i] = 1;

        if sFreq != tFreq:
            return False
        
        return True

        

        



        
        