# -*- coding: utf-8 -*-

class Solution:
    def IsContinuous(self, numbers):
        # write code here
        if len(numbers)<5:
            return False
        count_0=0
        numbers=sorted(numbers)
        for i in range(4):
            if numbers[i]==0: 
                count_0+=1
        num=numbers[count_0]+1
        n=len(numbers);j=count_0+1
        while j<n:
            if num>13:
                return False
            if num != numbers[j]:
                if count_0==0:
                    return False
                count_0-=1;j-=1
            num+=1;j+=1
        return True
        
                
    
if __name__=="__main__":
    s=Solution()
    ss=[1,0,0,5,0]
    print(s.IsContinuous(ss))
    