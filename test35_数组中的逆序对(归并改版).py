# -*- coding: utf-8 -*-

# 归并排序
# 先统计最低层的逆序对数，统计后将对数进行排序
# 然后一层一层向上剥

class Solution:
    def __init__(self):
        self.count=0
        
    def InversePairs(self, data):
        # write code here
        self.merge_sort(data)
        return self.count%1000000007
    
    # 归并排序
    def merge_sort(self,data):
        n=len(data)
        if n==1:
            return data
        mid=n//2
        left_li=self.merge_sort(data[:mid])
        right_li=self.merge_sort(data[mid:])
        
        result=[]
        m,p=len(left_li),len(right_li)
        left_pointer,right_pointer=0,0
        
        while left_pointer<m and right_pointer<p:
            left,right=left_li[left_pointer],right_li[right_pointer]
            if left<=right:
                result.append(left)
                left_pointer+=1
            else:
                result.append(right)
                right_pointer+=1
                self.count+=(m-left_pointer)
        result+=left_li[left_pointer:]
        result+=right_li[right_pointer:]
        return result
        
        
        
if __name__=="__main__":
    s=Solution()
    ss=[364,637,341,406,747,995,234,971,571,219,
        993,407,416,366,315,301,601,650,418,355,
        460,505,360,965,516,648,727,667,465,849,
        455,181,486,149,588,233,144,174,557,67,
        746,550,474,162,268,142,463,221,882,576,
        604,739,288,569,256,936,275,401,497,82,
        935,983,583,523,697,478,147,795,380,973,
        958,115,773,870,259,655,446,863,735,784,
        3,671,433,630,425,930,64,266,235,
        187,284,665,874,80,45,848,38,811,267,575]
    print(s.InversePairs(ss))