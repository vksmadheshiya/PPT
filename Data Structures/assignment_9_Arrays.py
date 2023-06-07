
print("********************  Q1  *************************")
""" Q1. Given an integer n, return true if it is a power of two. Otherwise, return false.
        An integer n is a power of two, if there exists an integer x such that n == 2x.
Example 1:
    Input:  n = 1 
    Output: true.    
Example 2:
    Input:  n = 16 
    Output: true. 
Example 3:
    Input:  n = 3 
    Output: false.    
    """

class Solution1:
    def isPowerOfTwo(self, n):
        if n == 1:
            return True
        elif n <= 0 or n % 2 != 0:
            return False
        else:
            return self.isPowerOfTwo(n // 2)

   
print(Solution1().isPowerOfTwo(1))
print(Solution1().isPowerOfTwo(2))
print(Solution1().isPowerOfTwo(3))


print("\n********************  Q2  *************************\n")
""" Q2. Given a number n, find the sum of the first natural numbers.
    
Example 1:
    Input: N = 3 
    Output: 6
Example 1:
    Input: N = 5
    Output: 15
      """

class Solution2:
    def sumOfNaturalNumbers(self, n):
        if n == 1:
            return 1
        else:
            return n + self.sumOfNaturalNumbers(n - 1)


print(Solution2().sumOfNaturalNumbers(3))
print(Solution2().sumOfNaturalNumbers(5))



print("\n********************  Q3  *************************\n")
""" Q3. Given a positive integer, N. Find the factorial of N. 
        You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
Example 1:
    Input: N = 5
    Output: 120
Example 1:
    Input: N = 4
    Output: 24
      """

class Solution3:
    def factorial(self, N):
        if N == 0 or N == 1:
            return 1
        else:
            return N * self.factorial(N - 1)

print(Solution3().factorial(5))
print(Solution3().factorial(4))


print("\n********************  Q4  *************************\n")
""" Q4. Given a number N and a power P, the task is to find the exponent of this number raised to the given power, i.e. N^P.
Example 1:
    Input: N = 5, P = 2
    Output: 25
Example 2:
    Input: N = 2, P = 5
    Output: 32
       """

class Solution4:
    def exponentiation(self, N, P):
        if P == 0:
            return 1
        else:
            return N * self.exponentiation(N, P - 1)


print(Solution4().exponentiation(5, 2))
print(Solution4().exponentiation(2, 5))



print("\n********************  Q5  *************************\n")
""" Q5. Given an array of integers arr, the task is to find maximum element of that array using recursion.
Example 1:
    Input: arr = {1, 4, 3, -5, -4, 8, 6};
    Output: 8
Example 2:
    Input: arr = {1, 4, 45, 6, 10, -8};
    Output: 45
       """
class Solution5:
    def findMax(self, arr):
        if len(arr) == 1:
            return arr[0]
        else:
            return max(arr[0], self.findMax(arr[1:]))


print(Solution5().findMax(arr = [1, 4, 3, -5, -4, 8, 6]))
print(Solution5().findMax(arr = [1, 4, 45, 6, 10, -8]))

print("\n********************  Q6  *************************\n")
""" Q6. Given first term (a), common difference (d) and a integer N of the Arithmetic Progression series, the task is to find Nth term of the series.
        For example, if s = "abcde", then it will be "bcdea" after one shift.
Example 1:
    Input:  a = 2 d = 1 N = 5
    Output: 6
Explanation : The 5th term of the series is : 6
Example 2:
    Input:  a = 5 d = 2 N = 10
    Output: 23
Explanation : The 10th term of the series is : 23
    """
class Solution6:
    def findNthTerm(self, a, d, N):
        if N == 1:
            return a
        else:
            return self.findNthTerm(a + d, d, N - 1)


print(Solution6().findNthTerm(2, 1, 5))
print(Solution6().findNthTerm(5, 2, 10))



print("\n********************  Q7  *************************\n")
""" Q7. Given a string S, the task is to write a program to print all permutations of a given string.
Example 1:
    Input: S = “ABC”
    Output: “ABC”, “ACB”, “BAC”, “BCA”, “CBA”, “CAB”
Example 1:
    Input: S = “XY”
    Output: “XY”, “YX”
       """
class Solution7:
    def permute(self, S, l, r):
        if l == r:
            print(''.join(S))
        else:
            for i in range(l, r + 1):
                S[l], S[i] = S[i], S[l]
                self.permute(S, l + 1, r)
                S[l], S[i] = S[i], S[l]  # backtrack





# Test cases
S1 = "ABC"
n1 = len(S1)
S2 = "XY"
n2 = len(S2)
print(Solution7().permute(list(S1), 0, n1 - 1))
print(Solution7().permute(list(S2), 0, n2 - 1))



print("\n********************  Q8  *************************\n")
""" Q8. Given an array, find a product of all array elements.

Example 1:
    Input: arr[] = {1, 2, 3, 4, 5}
    Output: 120
Example 2:
    Input: arr[] = {1, 6, 3}
    Output: 18
        """
class Solution8:
    def arrayProduct(self, arr):
        if len(arr) == 0:
            return 1
        else:
            return arr[0] * self.arrayProduct(arr[1:])


arr1 = [1, 2, 3, 4, 5]
arr2 = [1, 6, 3]
print(Solution8().arrayProduct(arr1))
print(Solution8().arrayProduct(arr2))

