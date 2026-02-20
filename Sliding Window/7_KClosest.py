# Find K Closest Elements

# You are given a sorted integer array arr, two integers k and x, return the k closest integers to x in the array. The result should also be sorted in ascending order.
# An integer a is closer to x than an integer b if:

# |a - x| < |b - x|, or
# |a - x| == |b - x| and a < b
# Example 1:

# Input: arr = [2,4,5,8], k = 2, x = 6
# Output: [4,5]

# Example 2:

# Input: arr = [2,3,4], k = 3, x = 1
# Output: [2,3,4]

def K_Closest(arr:list[int],k:int,x:int)->list[int]:
    arr1=list(map(lambda a: abs(x-a),arr))
    min_sum=float('inf')
    
    l=0
    r=k-1

    upper_bound=0
    lower_bound=0

    while r < len(arr):
        

        s=sum(arr1[l:r+1])
        if min_sum>s:
            min_sum=s
            upper_bound=r
            lower_bound=l
        r+=1
        l+=1
    
    return list(arr[lower_bound:upper_bound+1])
    



arr=[2,4,5,8]
k=2
x=6
ans=K_Closest(arr,k,x)

print(ans)