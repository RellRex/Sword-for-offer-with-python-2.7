# -*- coding: utf-8 -*-

class Solution:
    def __init__(self):
        self.lst=[]
        
    def FindContinuousSequence(self, tsum):
        # write code here
        if tsum==1 or tsum==2:
            return self.lst
        
        if tsum % 2==0:
            self.even(tsum)
            return sorted(self.lst)
        else:
            n=float(tsum)/2
            self.lst.append([int(n-0.5),int(n+0.5)])
            self.odd(tsum)
            return sorted(self.lst)
            
    def odd(self,tsum):
        for c in range(2,(tsum/2)+1):
            if tsum % c==0 and (tsum/c)>=(c/2)+1:
                ser=[];i=1
                n=tsum/c;ser.append(n)
                while len(ser)<c:
                    ser.append(n-i);ser.append(n+i)
                    i+=1
                ser=sorted(ser)
                self.lst.append(ser)
    
    def even(self,tsum):
        for c in range(3,(tsum/2)+1):
            if c%2==1 and tsum % c ==0 and (tsum/c)>=(c/2)+1:
                ser=[];i=1
                n=tsum/c;ser.append(n)
                while len(ser)<c:
                    ser.append(n-i);ser.append(n+i)
                    i+=1
                ser=sorted(ser)
                self.lst.append(ser)
            elif c % 2==0 and tsum % c==(c/2) and (tsum/c)>=(c/2)+1:
                ser=[];i=0.5
                n=float(tsum)/c
                while len(ser)<c:
                    ser.append(int(n-i));ser.append(int(n+i))
                    i+=1
                ser=sorted(ser)
                self.lst.append(ser)
        
        
            
if __name__=="__main__":
    s=Solution()
    print(s.FindContinuousSequence(100))
