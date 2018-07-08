"""Given a string, find the length of the longest substring without repeating characters.

Examples:

Given "abcabcbb", the answer is "abc", which the length is 3.

Given "bbbbb", the answer is "b", with the length of 1.

Given "pwwkew", the answer is "wke", with the length of 3. Note that the answer must be a substring, "pwke" is a subsequence and not a substring"""


class Solution:
    def lengthOfLongestSubstring(self, s):
        """
        :type s: str
        :rtype: int
        """
        sub_str = ""
        longest_count = 0
        for ch in s:
            if ch not in sub_str:
                sub_str += ch
            else:
                if len(sub_str) > longest_count:
                    longest_count = len(sub_str)
                sub_str = sub_str[sub_str.find(ch)+1:] + ch
                
        if len(sub_str) > longest_count:
            longest_count = len(sub_str)
            
        return longest_count

