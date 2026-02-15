# Minimum Size Subarray Sum

# You are given an array of positive integers nums and a positive integer target, return the minimal length of a subarray whose sum is greater than or equal to target. If there is no such subarray, return 0 instead.

# A subarray is a contiguous non-empty sequence of elements within an array.

# Example 1:

# Input: target = 10, nums = [2,1,5,1,5,3]

# Output: 3
# Explanation: The subarray [5,1,5] has the minimal length under the problem constraint.

# Example 2:

# Input: target = 5, nums = [1,2,1]

# Output: 0

def MinimumSubArraySum(nums,target):
    i=0
    length=float('inf')
    s=0
    for j in range(len(nums)):
        s+=nums[j]
        while(s>=target):
            length=min(length,j-i+1)
            s-=nums[i]
            i+=1

    if length>len(nums):
        return 0
    else:
        return length
    
nums= [2,1,5,1,5,3]

ans=MinimumSubArraySum(nums,10)

print(ans)
