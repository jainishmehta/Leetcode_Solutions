class Solution:    
    
    def validPalindrome(self, s: str) -> bool:    

        def isValid(s, l, r):
            while l<r:
                if s[l]!=s[r]:                    
                    return False
                l+=1
                r-=1            
            return True
    
        l=0
        r=len(s)-1
        
        while l<r:
            if s[l]!=s[r]:
                if isValid(s, l, r-1): return True  
                if isValid(s, l+1, r): return True
                return False
            l+=1
            r-=1
                    
            
        return True
