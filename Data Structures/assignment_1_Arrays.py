
print("********************  Q1  *************************")
""" Q1. Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target. 
You may assume that each input would have exactly one solution, and you may not use the same element twice. 
You can return the answer in any order.
Example :
    Input: nums = [2,7,11,15], target = 9
    Output0 [0,1]
    **Explanation:** Because nums[0] + nums[1] == 9, we return [0, 1]["""

class Solution1:
    # brute_force approach
    def two_sum_brute_force(self, nums:list[int], target:int) -> list[int]:
        for i in range(len(nums)):
            for j in range(i, len(nums)-1):
                if nums[i]+nums[j] == target:
                    return [i, j]
                

    # 2nd approach
    def two_sum(self, nums:list[int], target:int) -> list[int]:
        for i, num in enumerate(nums):
            complement = target - num
            if complement in nums:
                return [i, nums.index(complement) ]
        return []  # No solution found


print(Solution1().two_sum_brute_force([2,7,11,15], 9))
print(Solution1().two_sum([2,7,11,15], 9))


print("\n********************  Q2  *************************\n")
"""Q2. Given an integer array nums and an integer val, remove all occurrences of val in nums in-place. 
The order of the elements may be changed. Then return the number of elements in nums which are not equal to val. 
Consider the number of elements in nums which are not equal to val be k, to get accepted, you need to do the following things: 
    Change the array nums such that the first k elements of nums contain the elements which are not equal to val. 
    The remaining elements of nums are not important as well as the size of nums.
    Return k.
Example :
    Input: nums = [3,2,2,3], val = 3
    Output: 2, nums = [2,2,_,_]
    **Explanation:** 2, nums = [2,2,_,_]"""

class Solution2:
    # brute_force approach
    def replace_num_brute_force(self, nums:list[int], val:int) -> list:
        count = 0
        for i in range(len(nums)):
            if nums[i]==val:
                nums.pop(i)
                nums.append("_")
            else:
                count +=1
        return [count, nums]

print(Solution2().replace_num_brute_force([3,2,2,3], 3))
print("\n********************  Q3  *************************\n")

""" Q3. Given a sorted array of distinct integers and a target value, return the index if the target is found.
 If not, return the index where it would be if it were inserted in order. 
 You must write an algorithm with O(log n) runtime complexity.
    Return k.
Example :
    Input: nums = [1,3,5,6], target = 5
    Output: 2 """

class Solution3:
    def search_num(self, nums:list[int], target:int) -> int:
        left = 0
        right = len(nums)-1
        while left <= right:
            mid = left + (right-left) // 2
            if nums[mid] == target:
                return mid
            elif target < nums[mid]:
                right = mid -1
            else :
                left = mid + 1
        return right

print(Solution3().search_num([1, 3, 5, 6, 7, 8, 9], 1))
print("\n********************  Q4  *************************\n")


"""Q4.You are given a large integer represented as an integer array digits, where each digits[i] is the ith digit of the integer. 
The digits are ordered from most significant to least significant in left-to-right order. The large integer does not contain any leading 0's.
Increment the large integer by one and return the resulting array of digits.
Example :
    Input: digits = [1,2,3]
    Output: [1,2,4]
    **Explanation:** The array represents the integer 123. 
        Incrementing by one gives 123 + 1 = 124.
        Thus, the result should be [1,2,4]."""
class Solution4:
    def plus_one(self, digits:list[int]) -> list[int]:
        carry = 1
        for i in range(len(digits)-1, -1, -1):
            digits[i] += carry
            carry = digits[i]//10
            digits[i] %= 10

        if carry > 0:
            digits.insert(0, carry)

        return digits


print(Solution4().plus_one([1,2,3]))
print("\n********************  Q5  *************************\n")



"""Q5.You are given two integer arrays nums1 and nums2, sorted in non-decreasing order, and two integers m and n, 
      representing the number of elements in nums1 and nums2 respectively.
      Merge nums1 and nums2 into a single array sorted in non-decreasing order.
      The final sorted array should not be returned by the function, but instead be stored inside the array nums1. 
      To accommodate this, nums1 has a length of m + n, where the first m elements denote the elements that should be merged, 
      and the last n elements are set to 0 and should be ignored. nums2 has a length of n.
Example :
    Input: nums1 = [1,2,3,0,0,0], m = 3, nums2 = [2,5,6], n = 3
    Output: [1,2,2,3,5,6]
    **Explanation:** The arrays we are merging are [1,2,3] and [2,5,6].
        The result of the merge is [1,2,2,3,5,6] with the underlined elements coming from nums1."""


class Solution5:
    # brute_force approach
    def merge_two_array(self, nums1:list[int], m:int,  nums2:list[int], n:int ) -> list[int]:
        nums1 = self.remove_zeros(nums1)
        nums2 = self.remove_zeros(nums2)
        for each in nums2:
            nums1.append(each)
        return sorted(nums1)
    
    def remove_zeros(self, nums:list[int]) -> list[int]:
        for i in range(len(nums)-1, -1, -1):
            if not nums[i]:
                nums.pop(i)
        return nums


    def merge(self, nums1:list[int], m:int,  nums2:list[int], n:int ) -> list[int]:
        i = m - 1
        j = n - 1
        k = m + n - 1

        while i >= 0 and j >= 0:
            if nums1[i] > nums2[j]:
                nums1[k] = nums1[i]
                i -= 1
            else:
                nums1[k] = nums2[j]
                j -= 1
            k -= 1

        # If there are remaining elements in nums2
        while j >= 0:
            nums1[k] = nums2[j]
            j -= 1
            k -= 1

        return nums1

print(Solution5().merge_two_array([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print(Solution5().merge([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3))
print("\n********************  Q6  *************************\n")

"""Q5.Given an integer array nums, return true if any value appears at least twice in the array, and return false if every element is distinct.
Example :
    Input: nums = [1,2,3,1]
    Output: true """

class Solution6:
    def check_duplicate(self, nums:list[int]) -> bool:
        nums_dict = {}
        for each in nums:
            if each in nums_dict:
                nums_dict[each] += 1
                return True
            else:
                nums_dict[each] = 1

        return False
    
    def contains_duplicate(self, nums:list[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

print(Solution6().check_duplicate([1, 2, 3, 1]))
print(Solution6().contains_duplicate([1, 2, 3, 1]))
print("\n********************  Q7  *************************\n")


"""Q7. Given an integer array nums, move all 0's to the end of it while maintaining the relative order of the nonzero elements. 
    Note that you must do this in-place without making a copy of the array.
Example :
    Input: nums = [0,1,0,3,12]
    Output: [1,3,12,0,0] """

class Solution7:
    def move_zeroes_b_f(self, nums:list[int]) -> bool:
        for i in range(len(nums)-1, -1, -1):
            if not nums[i]:
                nums.pop(i)
                nums.append(0)
        return nums


    def move_zeroes(self, nums):
        n = len(nums)
        j = 0

        for i in range(n):
            if nums[i] != 0:
                nums[j] = nums[i]
                j += 1

        while j < n:
            nums[j] = 0
            j += 1

        return nums

print(Solution7().move_zeroes_b_f([0,1,0,3,12]))
print(Solution7().move_zeroes([0,1,0,3,12]))
print("\n********************  Q8  *************************\n")

"""Q8. You have a set of integers s, which originally contains all the numbers from 1 to n.
       Unfortunately, due to some error, one of the numbers in s got duplicated to another number in the set,
       which results in repetition of one number and loss of another number.
       You are given an integer array nums representing the data status of this set after the error.
       Find the number that occurs twice and the number that is missing and return them in the form of an array.

Example :
    Input: nums = [1,2,2,4]
    Output: [2,3] """

class Solution8:
    # brute_force approach
    def remove_duplicate_with_original(self, s:list[int]) -> bool:
        unique = set()
        missing_list = []

        for i in range(len(s)):
            if s[i] in unique:
                missing_list = [i, (s[i+1] + s[i-1]) // 2]
            else:
                unique.add(s[i])
        return missing_list
    
    def find_error_nums(self, nums):
        n = len(nums)
        num_set = set()
        duplicate = -1

        for num in nums:
            if num in num_set:
                duplicate = num
            else:
                num_set.add(num)

        for i in range(1, n + 1):
            if i not in num_set:
                return [i, duplicate]


print(Solution8().remove_duplicate_with_original([1,2,2,4]))
print(Solution8().find_error_nums([0,1,0,3,4]))