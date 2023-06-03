
print("********************  Q1  *************************")
""" Q1. A permutation perm of n + 1 integers of all the integers in the range [0, n] can be represented as a string s of length n where:
        - s[i] == 'I' if perm[i] < perm[i + 1], and
        - s[i] == 'D' if perm[i] > perm[i + 1].
        Given a string s, reconstruct the permutation perm and return it. If there are multiple valid permutations perm, return any of them.
Example 1:
    Input: s = "IDID"
    Output: [0,4,1,3,2]. """

class Solution1:
    def reconstructPermutation(self, s):
        perm = []
        low, high = 0, len(s)

        for ch in s:
            if ch == 'I':
                perm.append(low)
                low += 1
            else:
                perm.append(high)
                high -= 1

        perm.append(low)
        return perm
   
print(Solution1().reconstructPermutation(s = "IDID"))


print("\n********************  Q2  *************************\n")
""" Q2. You are given an m x n integer matrix matrix with the following two properties:
    - Each row is sorted in non-decreasing order.
    - The first integer of each row is greater than the last integer of the previous row.
    Given an integer target, return true if target is in matrix or false otherwise*.
    You must write a solution in O(log(m * n)) time complexity.
Example 1:
    Input: matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3
    Output: true """

class Solution2:
    def searchMatrix(self, matrix, target):
        if not matrix or not matrix[0]:
            return False
        
        m, n = len(matrix), len(matrix[0])
        left, right = 0, m * n - 1
        
        while left <= right:
            mid = (left + right) // 2
            row, col = mid // n, mid % n
            if matrix[row][col] == target:
                return True
            elif matrix[row][col] < target:
                left = mid + 1
            else:
                right = mid - 1
        
        return False



print(Solution2().searchMatrix(matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,60]], target = 3))



print("\n********************  Q3  *************************\n")
""" Q3. Given an array of integers arr, return true if and only if it is a valid mountain array.
        Recall that arr is a mountain array if and only if:
        - arr.length >= 3
        - There exists some i with 0 < i < arr.length - 1 such that:
            - arr[0] < arr[1] < ... < arr[i - 1] < arr[i]
            - arr[i] > arr[i + 1] > ... > arr[arr.length - 1]
Example 1:
    Input: arr = [2,1]
    Output: false """

class Solution3:
    def validMountainArray(self, arr):
        n = len(arr)
        if n < 3:
            return False
        
        left, right = 0, n - 1
        
        while left < right:
            if arr[left] < arr[left + 1]:
                left += 1
            elif arr[right] < arr[right - 1]:
                right -= 1
            else:
                break
        
        return left == right and left != 0 and right != n - 1


print(Solution3().validMountainArray(arr = [2,1]))


print("\n********************  Q4  *************************\n")
""" Q4. Given a binary array nums, return the maximum length of a contiguous subarray with an equal number of 0 and 1.
Example 1:
    Input: nums = [0,1]
    Output: 2
Explanation: [0, 1] is the longest contiguous subarray with an equal number of 0 and 1.
     
       """

class Solution4:
    def findMaxLength(self, nums):
        max_length = 0
        count = 0
        count_dict = {0: -1}

        for i, num in enumerate(nums):
            if num == 0:
                count -= 1
            else:
                count += 1

            if count in count_dict:
                length = i - count_dict[count]
                max_length = max(max_length, length)
            else:
                count_dict[count] = i

        return max_length



print(Solution4().findMaxLength(nums = [0,1]))

print("\n********************  Q5  *************************\n")
""" Q5. The product sum of two equal-length arrays a and b is equal to the sum of a[i] * b[i] for all 0 <= i < a.length (0-indexed).
    - For example, if a = [1,2,3,4] and b = [5,2,3,1], the product sum would be 1*5 + 2*2 + 3*3 + 4*1 = 22.
    Given two arrays nums1 and nums2 of length n, return the minimum product sum if you are allowed to rearrange the order of the elements in nums1.Example 1:
    Input: nums1 = [5,3,4,2], nums2 = [4,2,2,5]
    Output: 40
Explanation: We can rearrange nums1 to become [3,5,4,2]. The product sum of [3,5,4,2] and [4,2,2,5] is 3*4 + 5*2 + 4*2 + 2*5 = 40.

       """
class Solution5:
    def minProductSum(self, nums1, nums2):
        nums1.sort()  # Sort nums1 in non-decreasing order
        nums2.sort()  # Sort nums2 in non-decreasing order

        product_sum = 0
        for i in range(len(nums1)):
            product_sum += nums1[i] * nums2[-i - 1]  # Multiply the corresponding elements from both arrays
        return product_sum

print(Solution5().minProductSum(nums1 = [5,3,4,2], nums2 = [4,2,2,5]))

print("\n********************  Q6  *************************\n")
""" Q6. An integer array original is transformed into a doubled array changed by appending twice the value of every element in original, 
        and then randomly shuffling the resulting array.
        Given an array changed, return original if changed is a doubled array.
        If changed is not a doubled array, return an empty array. The elements in original may be returned in any order.
Example 1:
    Input: changed = [1,3,4,2,6,8]
    Output: [1,3,4]
Explanation: One possible original array could be [1,3,4]:
    - Twice the value of 1 is 1 * 2 = 2.
    - Twice the value of 3 is 3 * 2 = 6.
    - Twice the value of 4 is 4 * 2 = 8.
    Other original arrays could be [4,3,1] or [3,1,4].

       """
class Solution6:
    def findOriginalArray(self, changed):
        if len(changed) % 2 != 0:
            return []  # If the length of changed is odd, it can't be a valid doubled array

        original_set = set(changed)
        original_array = []

        for num in changed:
            if num % 2 == 0 and num // 2 in original_set:
                original_set.remove(num // 2)
                original_array.append(num // 2)
            else:
                return []  # If the value doesn't match the expected condition, changed is not a valid doubled array

        if len(original_set) == 0:
            return original_array

        return []

print(Solution6().findOriginalArray(changed = [1,3,4,2,6,8]))



print("\n********************  Q7  *************************\n")
""" Q7. Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
Example 1:
    Input: n = 3

    Output: [[1,2,3],[8,9,4],[7,6,5]]
       """
class Solution7:
    def generateMatrix(self, n):
        matrix = [[0] * n for _ in range(n)]  # Create an n x n matrix filled with zeros
        num = 1  # Initialize the starting value

        # Define the boundaries of the spiral
        top, bottom = 0, n - 1
        left, right = 0, n - 1

        while num <= n*n:
            # Traverse from left to right
            for i in range(left, right + 1):
                matrix[top][i] = num
                num += 1
            top += 1

            # Traverse from top to bottom
            for i in range(top, bottom + 1):
                matrix[i][right] = num
                num += 1
            right -= 1

            # Traverse from right to left
            for i in range(right, left - 1, -1):
                matrix[bottom][i] = num
                num += 1
            bottom -= 1

            # Traverse from bottom to top
            for i in range(bottom, top - 1, -1):
                matrix[i][left] = num
                num += 1
            left += 1

        return matrix


print(Solution7().generateMatrix( n = 3))



print("\n********************  Q8  *************************\n")
""" Q8. Given two sparse matrices mat1 of size m x k and mat2 of size k x n, return the result of mat1 x mat2. You may assume that multiplication is always possible.
Example 1:
    Input: mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]
    Output: [[7,0,0],[-7,0,3]]
       """
class Solution8:
    def multiplySparseMatrices(self, mat1, mat2):
        m, k = len(mat1), len(mat1[0])
        k, n = len(mat2), len(mat2[0])

        result = [[0] * n for _ in range(m)]

        for i in range(m):
            for j in range(n):
                for p in range(k):
                    result[i][j] += mat1[i][p] * mat2[p][j]

        return result


print(Solution8().multiplySparseMatrices(mat1 = [[1,0,0],[-1,0,3]], mat2 = [[7,0,0],[0,0,0],[0,0,1]]))

