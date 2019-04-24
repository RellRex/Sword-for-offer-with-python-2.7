# -*- coding: utf-8 -*-

class Solution:
    # s字符串
    def isNumeric(self, s):
        # write code here
        num_lst=["0","1","2","3","4","5","6","7","8","9"]
        str_lst=["+","-"]
        sci_lst=["e","E"]
        dot=["."]
        scn=num_lst+str_lst+sci_lst+dot
        n=len(s);i=0;count=0;count_e=0
        if n==0:
            return False
        while i<n:
            num=s[i]
            if num not in scn:
                return False
            elif num in str_lst+sci_lst+dot:
                if i==(n-1):
                    return False
                elif num in str_lst:
                    if s[i+1] in str_lst+sci_lst:
                        return False
                    elif i!=0 and s[i-1] not in sci_lst:
                        return False
                elif num in sci_lst:
                    count_e+=1
                    if i==0:
                        return False
                    elif s[i+1] in sci_lst+dot:
                        return False
                elif num in dot:
                    count+=1
                    if s[i+1] in sci_lst+dot:
                        return False
                    elif count>1 or count_e>0:
                        return False
            i+=1
        return True   
            
if __name__=="__main__":
    s=Solution()
    print(s.isNumeric("12e+4.3"))
    