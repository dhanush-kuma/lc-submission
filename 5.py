class Solution:
    def differenceOfSums(self, n: int, m: int) -> int:
        dsum=0
        ndsum=0
        for i in range(0,n+1):
            if(i%m==0):
                dsum=dsum+i
            else:
                ndsum=ndsum+i
        return ndsum-dsum
        