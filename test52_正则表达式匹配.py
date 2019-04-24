# -*- coding: utf-8 -*-

class Solution:
    # s, pattern都是字符串
    def match(self, s, pattern):
        # write code here
        if pattern==".*":
            return True
        n,m=len(s),len(pattern)
        if n==0 and m==2 and ("*" in pattern):
            return True
        if n==1 and pattern==".":
            return True
        
        i,j=0,0
        while i<n and j<m:
            print(i,j)
            if j==(m-1):
                if s[i] != pattern[j]:
                    return False
                i+=1;j+=1
            else:
                if pattern[j+1]!="*":
                    if pattern[j]!="." and s[i]!=pattern[j]:
                        return False
                    else:
                        i+=1;j+=1
                else:
                    # *表示0的情况
                    if pattern[j]!="." and s[i]!=pattern[j]:
                        j+=2
                    # .*的情况
                    elif pattern[j]==".":
                        if (j+1)==(m-1):
                            return True
                        while i<n and s[i]!=pattern[j+2]:
                            i+=1
                        if i==n: return False
                        j+=1
                    # x*且存匹配的情况
                    else:
                        while i<n and n-i>m-j+2 and s[i]==pattern[j]:
                            i+=1
                        j+=2
                        
                        
        if i!=n: 
            return False
        elif j!=m:
            if len(pattern[j:])==2 and ("*" in pattern[j:]):
                return True
            else:
                return False
        return True
if __name__=="__main__":
    s=Solution()
    print(s.match("aaa","a*a"))
    
    