# Longest Repeating Character Replacement

# You are given a string s consisting of only uppercase english characters and an integer k. You can choose up to k characters of the string and replace them with any other uppercase English character.
# After performing at most k replacements, return the length of the longest substring which contains only one distinct character.

# Example 1:
# Input: s = "XYYX", k = 2
# Output: 4
# Explanation: Either replace the 'X's with 'Y's, or replace the 'Y's with 'X's.

# Example 2:
# Input: s = "AAABABB", k = 1
# Output: 5


def LongestRepeatingSubstring(s:str,k:int)->int:
    freq={}
    left=0
    maxfreq=0
    maxlen=0

    for right in range(len(s)):
        freq[s[right]]=1+freq.get(s[right],0)
        maxfreq=max(maxfreq,freq[s[right]])

        if (right-left+1)-maxfreq>k:
            freq[s[left]]-=1
            left+=1

        maxlen=max(maxlen,right-left+1)
    return maxlen



s='AAABABB'
print(LongestRepeatingSubstring(s,2))