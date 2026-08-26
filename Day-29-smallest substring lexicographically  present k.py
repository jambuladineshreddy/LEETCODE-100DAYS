class Solution:
    def shortestBeautifulSubstring(self, s: str, k: int) -> str:
        l=0
        r=0
        count=0
        small=[0,0,0]
        for ch in s:
            r+=1
            if ch=='1':
                count+=1
            while(count>=k and l<r):
                if small[0]==0 or small[0]>(r-l):
                    small[0]=r-l
                    small[1]=l
                    small[2]=r
                elif (r-l)==small[0]:
                    pre_sub=s[small[1]:small[2]]
                    curr_sub=s[l:r]
                    if self.is_curr(pre_sub,curr_sub):
                        small[0]=r-l
                        small[1]=l
                        small[2]=r
                if s[l]=='1':
                   count-=1
                l+=1
        return s[small[1]:small[2]]
    def is_curr(self,pre_sub:str,curr_sub:str)->bool:
        for i in range(len(curr_sub)):
            if pre_sub[i]<curr_sub[i]:
                return False
            elif pre_sub[i]>curr_sub[i]:
                return True
        return True




           