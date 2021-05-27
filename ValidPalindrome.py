class Solution:
    def isPalindrome(self, s: str) -> bool:
        newString = re.sub('[^0-9|a-z|A-Z]', '', s).lower()
        return newString[::-1] == newString
