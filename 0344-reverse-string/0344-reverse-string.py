class Solution:
    def reverseString(self, s: List[str]) -> None:
        """
        Do not return anything, modify s in-place instead.
        """
        start=0
        end=len(s)-1
        while start<end:
            self.swap(start,end,s)
            start+=1
            end-=1
    def swap(self,i,j,s):
        s[i],s[j]=s[j],s[i]