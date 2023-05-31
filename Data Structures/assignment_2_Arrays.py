
print("********************  Q1  *************************")
""" Q1. Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),..., (an, bn) 
        such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

Example :
    Input:  nums = [1,4,3,2]
    Output: 4
    **Explanation:**  All possible pairings (ignoring the ordering of elements) are:
        1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
        2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
        3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
        So the maximum possible sum is 4 """

class Solution1:
    def arrayPairSum(self, nums):
        nums.sort()  # Sort the array in ascending order
        max_sum = 0
        for i in range(0, len(nums), 2):
            max_sum += nums[i]  # Add the minimum element of each pair to the max_sum
        return max_sum


print(Solution1().arrayPairSum([1, 4, 3, 2]))


print("\n********************  Q2  *************************\n")
"""Q2. Alice has n candies, where the ith candy is of type candyType[i]. Alice noticed that she started to gain weight, so she visited a doctor. 
    The doctor advised Alice to only eat n / 2 of the candies she has (n is always even). Alice likes her candies very much, 
    and she wants to eat the maximum number of different types of candies while still following the doctor's advice. 
    Given the integer array candyType of length n, return the maximum number of different types of candies she can eat if she only eats n / 2 of them.
Example :
    Input: candyType = [1,1,2,2,3,3]
    Output: 3
    **Explanation:**  Alice can only eat 6 / 2 = 3 candies. Since there are only 3 types, she can eat one of each type."""

class Solution2:
    # brute_force approach
    def max_candies(self, candyType:list[int]) -> list:
        candies_count = {}
        unique_candy_count = 0
        for i in range(len(candyType)):
            if candyType[i] not in candies_count:
                candies_count[candyType[i]] = 1
                unique_candy_count +=1
            else:
                candies_count[candyType[i]] += 1
        if unique_candy_count > len(candyType)//2:
            return len(candyType)//2
        else:
            return unique_candy_count
        

    #optimized
    def max_num_types(self, candyType):
        # Calculate the maximum number of candies Alice can eat
        max_candies = len(candyType) // 2
        # Count the number of unique candy types
        unique_types = len(set(candyType))
        # Return the minimum of max_candies and unique_types
        return min(max_candies, unique_types)

print(Solution2().max_candies([1,1,2,2,3,3]))
print(Solution2().max_num_types([1,1,2,2,3,3]))

print("\n********************  Q3  *************************\n")

"""Q3. We define a harmonious array as an array where the difference between its maximum value and its minimum value is exactly 1.
    Given an integer array nums, return the length of its longest harmonious subsequence among all its possible subsequences. 
    A subsequence of an array is a sequence that can be derived from the array by deleting some or no elements without changing the order of the remaining elements.
Example :
    Input: nums = [1,3,2,2,5,2,3,7]
    Output: 5
    **Explanation:**  The longest harmonious subsequence is [3,2,2,2,3]."""

from collections import Counter
class Solution3:
    def findLHS(self, nums:list[int]) -> list:
        # Count the frequency of each number in nums
        num_counts = Counter(nums)
        # Initialize the maximum length to 0
        max_length = 0
        # Iterate over each unique number in nums
        for num in num_counts:
            # Check if the current number and its adjacent numbers form a harmonious subsequence
            if num + 1 in num_counts:
                # Calculate the length of the harmonious subsequence
                length = num_counts[num] + num_counts[num + 1]
                # Update the maximum length if necessary
                max_length = max(max_length, length)
        
        return max_length


print(Solution3().findLHS([1,3,2,2,5,2,3,7]))

print("\n********************  Q4  *************************\n")

"""Q4. You have a long flowerbed in which some of the plots are planted, and some are not. However, flowers cannot be planted in adjacent plots    
    Given an integer array flowerbed containing 0's and 1's, where 0 means empty and 1 means not empty, 
    and an integer n, return true if n new flowers can be planted in the flowerbed without violating the no-adjacent-flowers rule and false otherwise..
Example :
    Input:  flowerbed = [1,0,0,0,1], n = 1
    Output: true """

class Solution4:
    def flowerbed(self, flowerbed:list[int], n) -> list:
        i = 0
        while i < len(flowerbed) and n>0:
            if flowerbed[i] == 1:
                i+=2
                continue
            else:
                if flowerbed[i+1] == 1:
                    return False
                else:
                    n-=1            
            i+=1
        return True
    

    # 2nd Approach
    def canPlaceFlowers(self, flowerbed, n):
        # Initialize variables
        count = 0
        i = 0
        length = len(flowerbed)
        
        while i < length:
            # Check if the current plot and its adjacent plots are empty
            if flowerbed[i] == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == length-1 or flowerbed[i+1] == 0):
                # Plant a flower in the current plot
                flowerbed[i] = 1
                count += 1
                i += 1  # Skip the next plot since it cannot have a flower planted
                # Check if enough flowers have been planted
                if count >= n:
                    return True
            i += 1
        return count >= n

print(Solution4().flowerbed([1,0,0,0,1], 1))
print(Solution4().canPlaceFlowers([1,0,0,0,1], 1))


print("\n********************  Q5  *************************\n")
"""Q5. Given an integer array nums, find three numbers whose product is maximum and return the maximum product. 
Example :
    Input:  nums = [1,2,3]
    Output: 6 """
class Solution5:
    def maximumProduct(self, nums:list[int]) -> int:
        max1 = max2 = max3 = float('-inf')
        for num in nums:
            if num > max1:
                max3=max2
                max2=max1
                max1=num
            elif num > max2:
                max3=max2
                max2=num
            elif num > max3:
                max3=num

        return max1*max2*max3
    
    # 2nd Approach
    def maximumProduct2(self, nums):
        # Initialize the minimum and second minimum values to positive infinity
        min1 = min2 = float('inf')
        
        # Initialize the maximum, second maximum, and third maximum values to negative infinity
        max1 = max2 = max3 = float('-inf')
        
        # Iterate over each number in nums
        for num in nums:
            # Update the maximum values
            if num > max1:
                max3 = max2
                max2 = max1
                max1 = num
            elif num > max2:
                max3 = max2
                max2 = num
            elif num > max3:
                max3 = num
            
            # Update the minimum values
            if num < min1:
                min2 = min1
                min1 = num
            elif num < min2:
                min2 = num
        
        # Return the maximum of two possible products:
        # 1. Product of the three largest numbers (max1, max2, max3)
        # 2. Product of the two smallest numbers (min1, min2) and the largest number (max1)
        return max(max1 * max2 * max3, min1 * min2 * max1)

    # 3rd Approach
    def maximumProduct3(self, nums):
        # Sort the array in ascending order
        nums.sort()

        # Return the maximum of two possible products:
        # 1. Product of the three largest numbers (last three elements)
        # 2. Product of the two smallest numbers (first two elements) and the largest number (last element)
        return max(nums[-1] * nums[-2] * nums[-3], nums[0] * nums[1] * nums[-1])


print(Solution5().maximumProduct([1,2,3]))
print(Solution5().maximumProduct2([1,2,3]))
print(Solution5().maximumProduct3([1,2,3]))



print("\n********************  Q6  *************************\n")
"""Q6. Given an array of integers nums which is sorted in ascending order, and an integer target,
        write a function to search target in nums. If target exists, then return its index. Otherwise,
        return -1
        You must write an algorithm with O(log n) runtime complexity.
.
Example :
    Input:  nums = [-1,0,3,5,9,12], target = 9
    Output:  4
    **Explanation:**  9 exists in nums and its index is 4."""

class Solution6:
    def search_num(self, nums, target):
        left = 0
        right=len(nums) -1
        while left <= right:
            mid = (left+right)//2

            if nums[mid] == target:
                return mid
            
            if nums[mid] > target:
                right = mid - 1
            
            if nums[mid] < target:
                left = mid + 1

        return -1
    
print(Solution6().search_num(nums = [-1,0,3,5,9,12], target = 9))


print("\n********************  Q7  *************************\n")
"""Q7. An array is monotonic if it is either monotone increasing or monotone decreasing.,
        An array nums is monotone increasing if for all i <= j, nums[i] <= nums[j]. An array nums is
        monotone decreasing if for all i <= j, nums[i] >= nums[j].
        Given an integer array nums, return true if the given array is monotonic, or false otherwise.

.
Example :
    Input: nums = [1,2,2,3]
    Output: true"""

class Solution7:
    def monotonic(self, nums):
        if self.monotone_increasing(nums) or self.monotone_decreasing(nums):
            return True
        return False

    # monotone increasing 
    def monotone_increasing(self, nums):
        for i in range(len(nums)-1):
            if not nums[i] <= nums[i+1]:
                return False
        return True
   
    # monotone decreasing
    def monotone_decreasing(self, nums):
        for i in range(len(nums)-1):
            if not nums[i+1] <= nums[i]:
                return False
        return True

    # 2nd and short Method
    def isMonotonic(self, nums):
        increasing = decreasing = True
        for i in range(1, len(nums)):
            if nums[i] < nums[i - 1]:
                increasing = False
            if nums[i] > nums[i - 1]:
                decreasing = False

        return increasing or decreasing



print(Solution7().monotonic(nums = [1,2,2,3]))
print(Solution7().isMonotonic(nums = [1,2,2,3]))


print("\n********************  Q8  *************************\n")
"""Q8. You are given an integer array nums and an integer k.
        In one operation, you can choose any index i where 0 <= i < nums.length and change nums[i] to nums[i] + x where x is an integer from the range [-k, k]. 
        You can apply this operation at most once for each index i.
        The score of nums is the difference between the maximum and minimum elements in nums.
        Return the minimum score of nums after applying the mentioned operation at most once for each index in it.
Example :
    Input: nums = [1], k = 0
    Output: 0 
    **Explanation:**  The score is max(nums) - min(nums) = 1 - 1 = 0."""


class Solution8:
    def minimum_score(self, nums, k):
        min = float("inf")
        max = float("-inf")

        for i in range(len(nums)):
            if nums[i]+k > max:
                max = nums[i]+k

            if nums[i]+k < min:
                min = nums[i]+k

        return max -min
    

    # 2nd Approach
    def minimumScore(self, nums, k):
        # Find the minimum and maximum values in the array
        min_val = min(nums)
        max_val = max(nums)

        # If the difference between the minimum and maximum values is already less than or equal to 2*k,
        # then the minimum score is 0 because no operation is needed
        if max_val - min_val <= 2 * k:
            return 0
        
        # Otherwise, we can reduce the difference by applying the operation to the minimum and maximum values
        # Calculate the new minimum and maximum values after applying the operation
        new_min = min_val + k
        new_max = max_val - k

        # Check if the new minimum and maximum values can be reached within the range [new_min, new_max]
        # If not, we can reduce the difference by applying the operation to any element in the array
        for num in nums:
            if num < new_min or num > new_max:
                return new_max - new_min
        
        # If all elements in the array can be adjusted to the new range, the minimum score is 0
        return 0

    
print(Solution8().minimum_score(nums = [1], k=0))
print(Solution8().minimumScore(nums = [1], k=0))