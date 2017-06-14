"""
Write a function that takes a string as input and reverse only the vowels of a string.

Example 1:
Given s = "hello", return "holle".

Example 2:
Given s = "leetcode", return "leotcede".

This solution uses two pointers and makes a swap if both characters are vowels, otherwise increase/decrease the 
pointer if current character is not a vowel. Strings are immutable so convert to a list first then convert back to string.
"""

class Solution(object):
    def reverseVowels(self, s):
        """
        :type s: str
        :rtype: str
        """
        i , j =0, len(s)-1
        vowels = "aeiouAEIOU"
        ls = list(s)
        
        while i < j:
            if ls[i] in vowels and ls[j] in vowels:
                ls[i] , ls[j] = ls[j], ls[i]
                i +=1
                j -= 1
            elif ls[i] not in vowels:
                i+=1
            elif ls[j] not in vowels:
                j -= 1
        
        return "".join(str(c) for c in ls)
