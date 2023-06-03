
print("********************  Q1  *************************")
""" Q1. Convert 1D Array Into 2D Array, You are given a 0-indexed 1-dimensional (1D) integer array original, and two integers, m and n.
        You are tasked with creating a 2-dimensional (2D) array with  m rows and n columns using all the elements from original.
        The elements from indices 0 to n - 1 (inclusive) of original should form the first row of the constructed 2D array,
        the elements from indices n to 2 * n - 1 (inclusive) should form the second row of the constructed 2D array, and so on.
        Return an m x n 2D array constructed according to the above procedure, or an empty 2D array if it is impossible.

Example :
    Input: original = [1,2,3,4], m = 2, n = 2
    Output: [[1,2],[3,4]]
**Explanation:** The constructed 2D array should contain 2 rows and 2 columns. 
        The first group of n=2 elements in original, [1,2], becomes the first row in the constructed 2D array. 
        The constructed 2D array should contain 2 rows and 2 columns. """

class Solution1:
    def construct2D(self, original, m, n):
        if len(original) != m*n:
            return []
        
        result = []
        temp_List = []
        col_count = 0
        
        for i in range(len(original)):
            temp_List.append(original[i])
            col_count +=1
            if col_count == m:
                result.append(temp_List)
                n -= 1
                col_count = 0
                temp_List = []
                
        return result
    
    #2nd 
    def construct2DArray(self, original, m, n):
        if m * n != len(original):
            return []

        return [original[i * n: (i + 1) * n] for i in range(m)]
      


print(Solution1().construct2D(original = [1,2,3,4], m = 2, n = 2))
print(Solution1().construct2DArray(original = [1,2,3,4], m = 2, n = 2))


print("\n********************  Q2  *************************\n")
""" Q2. The constructed 2D array should contain 2 rows and 2 columns.
        Given the integer n, return the number of complete rows of the staircase you will build.
        You may return the answer in any order.
Example :
    Input: n = 5
    Output: 2.
**Explanation:** Because the 3rd row is incomplete, we return 2. """

class Solution2:
    def buildStairCase(self, n):
        if n <= 0:
            return 0
        result = 0
        for i in range(n):
            if n >= i+1:
                n -= i+1
                result +=1
        return result
    
    #2nd 
    def arrangeStairCase(self, n):
        left, right = 0, n

        while left <= right:
            k = (left + right) // 2
            StairCase_needed = k * (k + 1) // 2

            if StairCase_needed == n:
                return k
            elif StairCase_needed < n:
                left = k + 1
            else:
                right = k - 1

        return right


print(Solution2().buildStairCase(n = 5))
print(Solution2().arrangeStairCase(n = 5))


print("\n********************  Q3  *************************\n")
""" Q3. Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example :
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
**Explanation:** 
    After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100]. """

class Solution3:
    def squares(self, nums):
        for i in range(len(nums)):
            nums[i] *= nums[i]
        sorted_nums = sorted(nums)
        return sorted_nums

    #2nd Method
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n  # Initialize the result array with zeros
        left = 0  # Pointer for the left end of the array
        right = n - 1  # Pointer for the right end of the array
        index = n - 1  # Pointer for filling the result array from right to left

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[index] = nums[left] * nums[left]
                left += 1
            else:
                result[index] = nums[right] * nums[right]
                right -= 1
            index -= 1

        return result

print(Solution3().squares(nums=  [-4,-1,0,3,10]))
print(Solution3().sortedSquares(nums=  [-4,-1,0,3,10]))



print("\n********************  Q4  *************************\n")
""" Q4. Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
        answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
        answer[1] is a list of all distinct integers in nums2 which are not present in nums1.
        Note that the integers in the lists may be returned in any order.

Example :
    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]
**Explanation:** 
    For nums1, nums1[1] = 2 is present at index 0 of nums2, whereas nums1[0] = 1 and nums1[2] = 3 are not present in nums2. Therefore, answer[0] = [1,3].
    For nums2, nums2[0] = 2 is present at index 1 of nums1, whereas nums2[1] = 4 and nums2[2] = 6 are not present in nums2. Therefore, answer[1] = [4,6]. """

class Solution4:
    def disjoints(self, nums1, nums2):
        nums1 = set(nums1)
        nums2 = set(nums2)
        return [list(nums1-nums2), list(nums2-nums1)]

    #2nd Method
    def disjoints2(self, nums1, nums2):
        num1_dict = {}

        for each in nums1:
            num1_dict[each]=num1_dict.get(each, 0) + 1
        
        disjoint_num2 = []
        disjoint_num1 = []
        for num in nums2:
            if num not in num1_dict:
                disjoint_num2.append(num)
        
        for num in num1_dict.keys():
            if num not in nums2:
                print(num1_dict[num])
                disjoint_num1.append(num)

        return disjoint_num1, disjoint_num2

print(Solution4().disjoints(nums1 = [1,2,3], nums2 = [2,4,6]))
print(Solution4().disjoints2(nums1 = [1,2,3], nums2 = [2,4,6]))


print("\n********************  Q5  *************************\n")
""" Q5. Given two integer arrays arr1 and arr2, and the integer d, return the distance value between the two arrays.
        The distance value is defined as the number of elements arr1[i] such that there is not any element arr2[j] where |arr1[i]-arr2[j]| <= d.

Example :
    Input: arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2
    Output:  2
**Explanation:** 
    For arr1[0]=4 we have:
    |4-10|=6 > d=2
    |4-9|=5 > d=2
    |4-1|=3 > d=2
    |4-8|=4 > d=2
    For arr1[1]=5 we have:
    |5-10|=5 > d=2
    |5-9|=4 > d=2
    |5-1|=4 > d=2
    |5-8|=3 > d=2
    For arr1[2]=8 we have:
    |8-10|=2 <= d=2
    |8-9|=1 <= d=2
    |8-1|=7 > d=2
    |8-8|=0 <= d=2 """

class Solution5:
    def distanceValue(self, arr1, arr2, d):
        distance = 0
        for num1 in arr1:
            valid = True
            for num2 in arr2:
                if abs(num1 - num2) <= d:
                    valid = False
                    break
            if valid:
                distance += 1
        return distance


print(Solution5().distanceValue(arr1 = [4,5,8], arr2 = [10,9,1,8], d = 2))




print("\n********************  Q6  *************************\n")
""" Q6. Given an integer array nums of length n where all the integers of nums are in the range [1, n] 
        and each integer appears once or twice, return an array of all the integers that appears twice.
        You must write an algorithm that runs in O(n) time and uses only constant extra space.


Example :
    Input: nums = [4,3,2,7,8,2,3,1]
    Output:  [2,3] """

class Solution6:
    def findDuplicates(self, nums):
        duplicates = []
        for num in nums:
            # Take the absolute value of the number to handle negative values
            index = abs(num) - 1
            if nums[index] < 0:
                duplicates.append(abs(num))
            else:
                nums[index] *= -1
        return duplicates

print(Solution6().findDuplicates(nums = [4,3,2,7,8,2,3,1]))

print("\n********************  Q7  *************************\n")
""" Q7. Suppose an array of length n sorted in ascending order is rotated between 1 and n times.
        For example, the array nums = [0,1,2,4,5,6,7] might become:
        [4,5,6,7,0,1,2] if it was rotated 4 times.
        [0,1,2,4,5,6,7] if it was rotated 7 times.
        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].
        Given the sorted rotated array nums of unique elements, return the minimum element of this array.
        You must write an algorithm that runs in O(log n) time.
Example :
    Input: nums = [3,4,5,1,2]
    Output:  1
**Explanation:** 
    The original array was [1,2,3,4,5] rotated 3 times. 
       """

class Solution7:
    def findMin(self, nums):
        left = 0
        right = len(nums) - 1

        while left < right:
            mid = left + (right - left) // 2

            # Check if the mid element is greater than the rightmost element
            if nums[mid] > nums[right]:
                left = mid + 1
            # Check if the mid element is smaller than the rightmost element
            elif nums[mid] < nums[right]:
                right = mid
            # If the mid element is equal to the rightmost element, decrement the right pointer
            else:
                right -= 1

        # The left pointer will be pointing to the minimum element
        return nums[left]

print(Solution7().findMin(nums = [3,4,5,1,2]))


print("\n********************  Q8  *************************\n")
""" Q8. An integer array original is transformed into a doubled array changed by appending twice the value of every element in original,
         and then randomly shuffling the resulting array.
        Given an array changed, return original if changed is a doubled array.
        If changed is not a doubled array, return an empty array. The elements in* original *may be returned in any order.

Example :
    Input: changed = [1,3,4,2,6,8]
    Output:  [1,3,4]
**Explanation:** 
    One possible original array could be [1,3,4]:
    Twice the value of 1 is 1 * 2 = 2.
    Twice the value of 3 is 3 * 2 = 6.
    Twice the value of 4 is 4 * 2 = 8.
    Other original arrays could be [4,3,1] or [3,1,4].
       """

from collections import defaultdict
class Solution8:
    def findOriginalArray(self, changed):
        counter = defaultdict(int)

        for num in changed:
            counter[num] += 1

        original = []
        for num in changed:
            if counter[num] > 0:
                if counter[num/2] > 0:
                    counter[num/2] -= 1
                    original.append(num/2)
                else:
                    return []

        return original

print(Solution8().findOriginalArray(changed = [1,3,4,2,6,8]))
