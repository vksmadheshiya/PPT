
print("********************  Q1  *************************")
""" Q1. Given an integer array nums of length n and an integer target, find three integers
        in nums such that the sum is closest to the target.
        Return the sum of the three integers
        You may assume that each input would have exactly one solution.
Example :
    Input: nums = [-1,2,1,-4], target = 1
    Output: 2
    **Explanation:**  The sum that is closest to the target is 2. (-1 + 2 + 1 = 2). """

class Solution1:
    def threeSumClosest(self, nums, target):
        nums.sort()  # Sort the array in ascending order
        closest_sum = float('inf')  # Initialize closest sum with infinity

        for i in range(len(nums)-2):
            left = i + 1  # Left pointer
            right = len(nums) - 1  # Right pointer

            while left < right:
                current_sum = nums[i] + nums[left] + nums[right]
                if current_sum == target:
                    return current_sum  # Found an exact match, return the sum
                elif abs(current_sum - target) < abs(closest_sum - target):
                    closest_sum = current_sum  # Update the closest sum

                if current_sum < target:
                    left += 1  # Move the left pointer to increase the sum
                else:
                    right -= 1  # Move the right pointer to decrease the sum

        return closest_sum

print(Solution1().threeSumClosest(nums = [-1,2,1,-4], target = 1))



print("\n********************  Q2  *************************\n")
"""Q2. Given an array nums of n integers, return an array of all the unique quadruplets
        [nums[a], nums[b], nums[c], nums[d]] such that:
            0 <= a, b, c, d < n
            a, b, c, and d are distinct.
            nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.
Example :
    Input: nums = [1,0,-1,0,-2,2], target = 0
    Output: [[-2,-1,1,2],[-2,0,0,2],[-1,0,0,1]]."""



class Solution2:
    def fourSum(self, nums, target):
        nums.sort()  # Sort the array in ascending order
        quadruplets = []  # Store the unique quadruplets

        for i in range(len(nums)-3):
            if i > 0 and nums[i] == nums[i-1]:
                continue  # Skip duplicates for the first element
            for j in range(i+1, len(nums)-2):
                if j > i+1 and nums[j] == nums[j-1]:
                    continue  # Skip duplicates for the second element

                left = j + 1  # Left pointer
                right = len(nums) - 1  # Right pointer
                while left < right:
                    current_sum = nums[i] + nums[j] + nums[left] + nums[right]
                    if current_sum == target:
                        quadruplets.append([nums[i], nums[j], nums[left], nums[right]])
                        left += 1
                        right -= 1
                        while left < right and nums[left] == nums[left-1]:
                            left += 1  # Skip duplicates for the third element
                        while left < right and nums[right] == nums[right+1]:
                            right -= 1  # Skip duplicates for the fourth element

                    elif current_sum < target:
                        left += 1
                    else:
                        right -= 1

        return quadruplets

print(Solution2().fourSum(nums = [1,0,-1,0,-2,2], target = 0))

print("\n********************  Q3  *************************\n")

"""Q3. A permutation of an array of integers is an arrangement of its members into a
        sequence or linear order.

        For example, for arr = [1,2,3], the following are all the permutations of arr:
        [1,2,3], [1,3,2], [2, 1, 3], [2, 3, 1], [3,1,2], [3,2,1].

        The next permutation of an array of integers is the next lexicographically greater
        permutation of its integer. More formally, if all the permutations of the array are
        sorted in one container according to their lexicographical order, then the next
        permutation of that array is the permutation that follows it in the sorted container.

        If such an arrangement is not possible, the array must be rearranged as the
        lowest possible order (i.e., sorted in ascending order).

        ● For example, the next permutation of arr = [1,2,3] is [1,3,2].
        ● Similarly, the next permutation of arr = [2,3,1] is [3,1,2].
        ● While the next permutation of arr = [3,2,1] is [1,2,3] because [3,2,1] does not
        have a lexicographical larger rearrangement.

        Given an array of integers nums, find the next permutation of nums.
        The replacement must be in place and use only constant extra memory.

**Example 1:**
    Input: nums = [1,2,3]
    Output: [1,3,2] """
class Solution3:
    def nextPermutation(self, nums):
        # Find the first pair of adjacent elements in descending order
        i = len(nums) - 2
        while i >= 0 and nums[i] >= nums[i+1]:
            i -= 1

        if i >= 0:
            # Find the smallest element in the subarray nums[i+1:] that is larger than nums[i]
            j = len(nums) - 1
            while j > i and nums[j] <= nums[i]:
                j -= 1
            # Swap nums[i] and nums[j]
            nums[i], nums[j] = nums[j], nums[i]

        # Reverse the subarray nums[i+1:] to make it in ascending order
        left = i + 1
        right = len(nums) - 1
        while left < right:
            nums[left], nums[right] = nums[right], nums[left]
            left += 1
            right -= 1

        return nums
print(Solution3().nextPermutation(nums = [1,2,3]))

print("\n********************  Q4  *************************\n")
"""Q4. Given a sorted array of distinct integers and a target value, return the index if the
    target is found. If not, return the index where it would be if it were inserted in
    order.

    You must write an algorithm with O(log n) runtime complexity.


**Example 1:**
    Input: nums = [1,3,5,6], target = 5
    Output: 2 """


class Solution4:
    def searchInsert(self, nums, target):
        left = 0
        right = len(nums) - 1

        while left <= right:
            mid = (left + right) // 2

            if nums[mid] == target:
                return mid
            elif nums[mid] < target:
                left = mid + 1
            else:
                right = mid - 1

        return left


print(Solution4().searchInsert(nums = [1,3,5,6], target = 5))


print("\n********************  Q5  *************************\n")

"""Q5. You are given a large integer represented as an integer array digits, where each
        digits[i] is the ith digit of the integer. The digits are ordered from most significant
        to least significant in left-to-right order. The large integer does not contain any
        leading 0's.
        Increment the large integer by one and return the resulting array of digits.

        Given an array of integers nums, find the next permutation of nums.
        The replacement must be in place and use only constant extra memory.

**Example 1:**
    Input: digits = [1,2,3]
    Output: [1,2,4]
     
**Explanation:**   The array represents the integer 123.
    Incrementing by one gives 123 + 1 = 124.
    Thus, the result should be [1,2,4]. """


class Solution5:
    def plusOne(self, digits):
        carry = 1  # Initialize the carry to 1

        for i in range(len(digits) - 1, -1, -1):
            digits[i] += carry  # Add the carry to the current digit

            if digits[i] < 10:
                carry = 0  # No carry required
                break
            else:
                digits[i] = 0  # Set the current digit to 0
                carry = 1  # Update the carry to 1

        if carry == 1:
            digits.insert(0, 1)  # Insert 1 at the beginning if carry is still 1

        return digits


print(Solution5().plusOne(digits = [1, 2, 3]))

print("\n********************  Q6  *************************\n")

"""Q6.  Given a non-empty array of integers nums, every element appears twice except
        for one. Find that single one.

        You must implement a solution with a linear runtime complexity and use only
        constant extra space.

**Example 1:**
    Input:  nums = [2,2,1]
    Output: 1
     """


class Solution6:

    def singleNumber(self, nums):
        seen = set()  # Initialize an empty set to store the seen elements

        # Iterate through each element in the array
        for num in nums:
            if num in seen:  # Check if the element is already in the set
                seen.remove(num)  # If it is, remove it from the set
            else:
                seen.add(num)  # If it is not, add it to the set

        # At the end, the set will contain the single element that appears only once
        return seen.pop()  # Return the single element from the set
    

    def singleNumber2(self, nums):
        result = 0  # Initialize a variable to store the XOR result

        # Iterate through each element in the array
        for num in nums:
            result ^= num  # Perform XOR operation with the result

        return result  # Return the single element that appears only once


print(Solution6().singleNumber(nums = [2, 2, 1]))
print(Solution6().singleNumber2(nums = [2, 2, 1]))



print("\n********************  Q7  *************************\n")
"""Q7.  You are given an inclusive range [lower, upper] and a sorted unique integer array
        nums, where all elements are within the inclusive range.
        A number x is considered missing if x is in the range [lower, upper] and x is not in
        nums.Return the shortest sorted list of ranges that exactly covers all the missing
        numbers. That is, no element of nums is included in any of the ranges, and each
        missing number is covered by one of the ranges.

**Example 1:**
    Input: nums = [0,1,3,50,75], lower = 0, upper = 99
    Output: [[2,2],[4,49],[51,74],[76,99]]
**Explanation** : The ranges are: 
            [2,2]
            [4,49]
            [51,74]
            [76,99] """

class Solution7:
    def findMissingRanges(self, nums, lower, upper):
        result = []
        prev = lower - 1
        # Helper function to add range to the result
        def addRange(start, end):
            result.append([str(start), str(end)])

        for num in nums + [upper + 1]:
            if prev + 1 <= num - 1:
                addRange(prev + 1, num - 1)
            prev = num

        return result

print(Solution7().findMissingRanges(nums = [0,1,3,50,75], lower = 0, upper = 99))


print("\n********************  Q8  *************************\n")
"""Q8.  Given an array of meeting time intervals where intervals[i] = [starti, endi],
        determine if a person could attend all meetings.

**Example 1:**
    Input: intervals = [[0,30],[5,10],[15,20]]
    Output: false """

class Solution8:
    
    def canAttendMeetings(self, intervals):
        # Sort the intervals based on the start time
        intervals.sort(key=lambda x: x[0])

        # Check for overlapping intervals
        for i in range(1, len(intervals)):
            if intervals[i][0] < intervals[i-1][1]:
                return False

        return True



print(Solution8().canAttendMeetings(intervals = [[0,30],[5,10],[15,20]]))
