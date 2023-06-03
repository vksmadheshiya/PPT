
print("********************  Q1  *************************")
""" Q1. Given three integer arrays arr1, arr2 and arr3 sorted in strictly increasing order, return a sorted array of only the integers that appeared in all three arrays.

Example :
    Input: arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]
    Output: [1,5]
    **Explanation:**  Only 1 and 5 appeared in the three arrays. """

class Solution1:
    element_array = {}
    def commonElementArray(self, arr1, arr2, arr3):
        common_elements = []
        self.count(arr1)
        self.count(arr2)
        self.count(arr3)
        
        for key, val in self.element_array.items():
            if val == 3:
                common_elements.append(key)

        return common_elements
    
    def count(self, array):
        for each in array:
            if each not in self.element_array:
                self.element_array[each] = 0
            self.element_array[each] += 1


    def arraysIntersection(self, arr1, arr2, arr3):
        result = []
        ptr1, ptr2, ptr3 = 0, 0, 0

        # Iterate until any pointer goes beyond array length
        while ptr1 < len(arr1) and ptr2 < len(arr2) and ptr3 < len(arr3):
            if arr1[ptr1] == arr2[ptr2] == arr3[ptr3]:
                result.append(arr1[ptr1])
                ptr1 += 1
                ptr2 += 1
                ptr3 += 1
            elif arr1[ptr1] <= arr2[ptr2] and arr1[ptr1] <= arr3[ptr3]:
                ptr1 += 1
            elif arr2[ptr2] <= arr1[ptr1] and arr2[ptr2] <= arr3[ptr3]:
                ptr2 += 1
            else:
                ptr3 += 1

        return result
      


print(Solution1().commonElementArray(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]))
print(Solution1().arraysIntersection(arr1 = [1,2,3,4,5], arr2 = [1,2,5,7,9], arr3 = [1,3,4,5,8]))


print("\n********************  Q2  *************************\n")
"""Q2. Given two 0-indexed integer arrays nums1 and nums2, return a list answer of size 2 where:
        answer[0] is a list of all distinct integers in nums1 which are not present in nums2.
        answer[1] *is a list of all **distinct** integers in* nums2 *which are **not** present in* nums1.
            Note that the integers in the lists may be returned in any order.
            nums[a] + nums[b] + nums[c] + nums[d] == target
    You may return the answer in any order.
Example :
    Input: nums1 = [1,2,3], nums2 = [2,4,6]
    Output: [[1,3],[4,6]]."""



class Solution2:
    def findDisjointElements(self, nums1, nums2):
        set1 = set(nums1)
        set2 = set(nums2)

        result = [list(set1 - set2), list(set2 - set1)]
        return result
    

    def findDisjointElements2(elf, nums1, nums2):
        # Create an empty dictionary to store the elements in nums1
        nums1_dict = {}
        # Iterate through nums1 and populate the dictionary with the count of each element
        for num in nums1:
            nums1_dict[num] = nums1_dict.get(num, 0) + 1
        # Create two empty lists to store the disjoint elements
        disjoint_nums1 = []
        disjoint_nums2 = []
        # Iterate through nums2 and check if each element is present in nums1_dict
        for num in nums2:
            if num not in nums1_dict:
                disjoint_nums2.append(num)
        # Iterate through nums1_dict and check if each element is not present in nums2
        for num in nums1_dict:
            if num not in nums2:
                disjoint_nums1.append(num)
        # Return the disjoint elements as a list of lists
        return [disjoint_nums1, disjoint_nums2]


print(Solution2().findDisjointElements(nums1 = [1,2,3], nums2 = [2,4,6]))
print(Solution2().findDisjointElements2(nums1 = [1,2,3], nums2 = [2,4,6]))


print("\n********************  Q3  *************************\n")
"""Q3. Given a 2D integer array matrix, return the transpose of matrix.
        The transpose of a matrix is the matrix flipped over its main diagonal, switching the matrix's row and column indices.
        
Example :
    Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
    Output: [[1,4,7],[2,5,8],[3,6,9]]"""



class Solution3:
    def transpose(self, matrix):
        # Get the number of rows and columns in the matrix
        rows = len(matrix)
        cols = len(matrix[0])

        # Create a new matrix with swapped dimensions
        transposed = [[0] * rows for _ in range(cols)]

        # Iterate through the matrix and swap elements
        for i in range(rows):
            for j in range(cols):
                transposed[j][i] = matrix[i][j]

        return transposed



print(Solution3().transpose(matrix = [[1,2,3],[4,5,6],[7,8,9]]))


print("\n********************  Q4  *************************\n")
"""Q4. Given an integer array nums of 2n integers, group these integers into n pairs
        (a1, b1), (a2, b2), ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.
        
Example :
    Input: nums = [1,4,3,2]
    Output: 4
    
**Explanation:**  All possible pairings (ignoring the ordering of elements) are:
    1. (1, 4), (2, 3) -> min(1, 4) + min(2, 3) = 1 + 2 = 3
    2. (1, 3), (2, 4) -> min(1, 3) + min(2, 4) = 1 + 2 = 3
    3. (1, 2), (3, 4) -> min(1, 2) + min(3, 4) = 1 + 3 = 4
    So the maximum possible sum is 4."""



class Solution4:
    def arrayPairSum(self, nums):
        nums.sort()  # Sort the array in ascending order
        max_sum = 0

        # Iterate through the sorted array by jumping two indices
        for i in range(0, len(nums), 2):
            max_sum += nums[i]  # Add the minimum value in each pair to the max_sum

        return max_sum

print(Solution4().arrayPairSum(nums = [1, 4, 3, 2]))



print("\n********************  Q5  *************************\n")
"""Q4. You have n coins and you want to build a staircase with these coins.
        The staircase consists of k rows where the ith row has exactly i coins.
        The last row of the staircase may be incomplete.
        Given the integer n, return the number of complete rows of the staircase you will build.
Example :
    Input: n = 5
    Output: 2
    
**Explanation:**  Because the 3rd row is incomplete, we return 2."""
class Solution5:
    def arrangeCoins(self, n):
        left = 0  # Starting index of the binary search range
        right = n  # Ending index of the binary search range

        while left <= right:
            mid = left + (right - left) // 2  # Calculate the midpoint

            # Calculate the number of coins required to form mid rows
            coins_required = (mid * (mid + 1)) // 2

            if coins_required == n:
                return mid  # Found the exact number of coins required for mid rows
            elif coins_required < n:
                left = mid + 1  # Increase the number of rows and search in the right half
            else:
                right = mid - 1  # Decrease the number of rows and search in the left half

        return right  # Return the maximum number of complete rows


print(Solution5().arrangeCoins(n = 5))


print("\n********************  Q6  *************************\n")
"""Q6. Given an integer array nums sorted in non-decreasing order, return an array of the squares of each number sorted in non-decreasing order.
Example :
    Input: nums = [-4,-1,0,3,10]
    Output: [0,1,9,16,100]
    
**Explanation:**  
    After squaring, the array becomes [16,1,0,9,100].
    After sorting, it becomes [0,1,9,16,100]."""

class Solution6:
    def sortedSquares(self, nums):
        n = len(nums)
        result = [0] * n  # Initialize an array to store the squared numbers
        left = 0  # Pointer for the leftmost element in the original array
        right = n - 1  # Pointer for the rightmost element in the original array
        i = n - 1  # Pointer for the result array, starting from the end

        while left <= right:
            if abs(nums[left]) > abs(nums[right]):
                result[i] = nums[left] * nums[left]
                left += 1
            else:
                result[i] = nums[right] * nums[right]
                right -= 1
            i -= 1

        return result

print(Solution6().sortedSquares(nums = [-4, -1, 0, 3, 10]))




print("\n********************  Q7  *************************\n")
"""Q7. You are given an m x n matrix M initialized with all 0's and an array of operations ops,
        where ops[i] = [ai, bi] means M[x][y] should be incremented by one for all 0 <= x < ai and 0 <= y < bi.
        Count and return the number of maximum integers in the matrix after performing all the operations
Example :
    Input: m = 3, n = 3, ops = [[2,2],[3,3]]
    Output: 4
    
**Explanation:**  
    The maximum integer in M is 2, and there are four of it in M. So return 4."""

class Solution7:
    def maxCount(self, m, n, ops):
        if not ops:
            return m * n

        min_row = float('inf')
        min_col = float('inf')

        for op in ops:
            min_row = min(min_row, op[0])
            min_col = min(min_col, op[1])

        return min_row * min_col


print(Solution7().maxCount(m = 3, n = 3, ops = [[2,2],[3,3]]))



print("\n********************  Q8  *************************\n")
"""Q8. Given the array nums consisting of 2n elements in the form [x1,x2,...,xn,y1,y2,...,yn].
Example :
    Input: nums = [2,5,1,3,4,7], n = 3
    Output: [2,3,5,4,1,7]
    
**Explanation:**  
    Since x1=2, x2=5, x3=1, y1=3, y2=4, y3=7 then the answer is [2,3,5,4,1,7]."""

class Solution8:
    def shuffle(self, nums, n):
        result = []
        p1, p2 = 0, n

        while p1 < n and p2 < 2 * n:
            result.append(nums[p1])
            result.append(nums[p2])
            p1 += 1
            p2 += 1

        return result


print(Solution8().shuffle(nums = [2,5,1,3,4,7], n = 3))


exit()