class Solution:
    def romanToInt(self, s: str) -> int:
        rom={
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }
        value=0
        for i in range(len(s)):
            if(s[i]=='I' or s[i]=='X' or s[i]=='C'):
                if(i<len(s)-1 and rom[s[i]]<rom[s[i+1]]):
                    value=value-rom[s[i]]
                else:
                    value=value+rom[s[i]]
            else:
                value=value+rom[s[i]]
        return value