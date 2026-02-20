# Permutation in String

# You are given two strings s1 and s2.
# Return true if s2 contains a permutation of s1, or false otherwise. That means if a permutation of s1 exists as a substring of s2, then return true.

# Both strings only contain lowercase letters.

# Example 1:

# Input: s1 = "abc", s2 = "lecabee"

# Output: true
# Explanation: The substring "cab" is a permutation of "abc" and is present in "lecabee".

# Example 2:

# Input: s1 = "abc", s2 = "lecaabee"

# Output: false


def PermutationSubstring(s1:str,s2:str)->bool:
    map1={}
    for i in s1:
        map1[i]=map1.get(i,0)+1

    l=0
    r=len(s1)-1

    while r<len(s2):
        map2={}
        for i in range(l,r+1):
            map2[s2[i]]=map2.get(s2[i],0)+1

        
        if map1==map2:
            return True
        
        r+=1
        l+=1
    
    return False



s1="abc"
s2="lecaabee"

ans=PermutationSubstring(s1,s2)

print(ans)