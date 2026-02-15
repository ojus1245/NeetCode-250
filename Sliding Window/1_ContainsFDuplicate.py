# Contains Duplicate II

# You are given an integer array nums and an integer k, return true if there are two distinct indices i and j in the array such that nums[i] == nums[j] and abs(i - j) <= k, otherwise return false.

# Example 1:
# Input: nums = [1,2,3,1], k = 3
# Output: true

# Example 2:
# Input: nums = [2,1,2], k = 1
# Output: false



def ContainsDuplicate(nums,k):
    # map={}
    # j=0
    # for i,num in enumerate(nums):
    #     if num in map and i-map[num]<=k:
    #             return True
    #     map[num]=i


        
    # return False
    x=set()
    l=0
    
    for i,num in enumerate(nums):
        if i-l>k:
            x.remove(nums[l])
            l+=1

        if num in x:
            return True

        x.add(num)

    return False

nums=[1,2,3,1]
k=3
ans=ContainsDuplicate(nums,k)

print(ans)