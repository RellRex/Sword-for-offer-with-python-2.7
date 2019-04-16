# -*- coding: utf-8 -*-


# 已知条件：后序序列最后一个值为root，二叉树的左子树值
#           都比root小，右子树值都比root大

class Solution:
    def VerifySquenceOfBST(self, sequence):
        # write code here
        if len(sequence)==0:
            return False
        
        root=sequence.pop()
        n=len(sequence);i=0
        while i<n:
            if sequence[i]>root:
                break
            i+=1
        left=sequence[:i];right=sequence[i:]

        if len(left) != 0:
            for node in left:
                if node>root:
                    return False
        if len(right) != 0:
            for node in right:
                if node <root:
                    return False
                
        if len(left) !=0:        
            left_of=self.VerifySquenceOfBST(left)
        else:
            left_of=True
        if len(right) !=0:
            right_of=self.VerifySquenceOfBST(right)
        else:
            right_of=True
        
        return left_of and right_of

    
if __name__=="__main__":
    s=Solution()
    seq=[4,6,8,16,14,10]
    print(s.VerifySquenceOfBST(seq))
    