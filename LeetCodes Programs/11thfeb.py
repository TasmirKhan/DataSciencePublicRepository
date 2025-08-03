class Solution(object):
    def removeOccurrences(self, s, part):
        """
        :type s: str
        :type part: str
        :rtype: str
        """
        
        while part in s:
            s = s.replace(part, "",1)

        return s        

sol = Solution()
print("This is the main part of the program.")
x = input("Enter your string")
y = input("Enter the repeating string.")
print("String after removal of part = ", sol.removeOccurrences(x,y))
