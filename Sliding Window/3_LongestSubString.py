# Longest Substring Without Repeating Characters

# Given a string s, find the length of the longest substring without duplicate characters.
# A substring is a contiguous sequence of characters within a string.

# Example 1:

# Input: s = "zxyzxyz"

# Output: 3
# Explanation: The string "xyz" is the longest without duplicate characters.

# Example 2:

# Input: s = "xxxx"

# Output: 1

def LongestSubstring(s):
    map={}
    left=0
    max_length=0
    for right in range(len(s)):
        if s[right] in map and map[s[right]]>=left:
            left=max(left,map[s[right]]+1)

        map[s[right]]=right
        max_length=max(max_length,right-left+1)

    return max_length

s="dvdf"
ans=LongestSubstring(s)
print(ans)