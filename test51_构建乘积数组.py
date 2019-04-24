# -*- coding: utf-8 -*-

class Solution:
    def multiply(self, A):
        # write code here
        n=len(A)
        if n==0:
            return []
        B=[1]*n
        for i in range(n):
            for j in range(n):
                if i != j:
                    B[j]*=A[i]
        return B
if __name__=="__main__":
    s=Solution()
    print(s.multiply([1,2,3,4,5,6,7]))