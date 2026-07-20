class Solution:
    def countDigits(self, num: int) -> int:
        n=num
        count=0
        while n:
            digit=n%10
            if num%digit==0:
                count+=1
            n//=10
        return count