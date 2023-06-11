
print("********************  Q1  *************************")
""" Q1. Given an integer `n`, return `true` if it is a power of three. Otherwise, return `false`.
        An integer `n` is a power of three, if there exists an integer `x` such that `n == 3x`.
Example 1:
    Input: n = 27
    Output: true
    Explanation: 27 = 33 
Example 2:
    Input: n = 0
    Output: false
    Explanation: There is no x where 3x = 0.
  
    """

class Solution1:
    def isPowerOfThree(self, n):
        if n <= 0:
            return False
        elif n == 1:
            return True
        elif n % 3 == 0:
            return self.isPowerOfThree(n // 3)
        else:
            return False
    
print(Solution1().isPowerOfThree(27))
print(Solution1().isPowerOfThree(0))


print("\n********************  Q2  *************************\n")
""" Q2. You have a list arr of all integers in the range [1, n] sorted in a strictly increasing order. 
        Apply the following algorithm on arr:
    
        Starting from left to right, remove the first number and every other number afterward until you reach the end of the list.
        Repeat the previous step again, but this time from right to left, remove the rightmost number and every other number from the remaining numbers.
        Keep repeating the steps again, alternating left to right and right to left, until a single number remains.
        Given the integer n, return the last number that remains in arr.

Example 1:
    Input: n = 9
    Output: 6
    Explanation:
        arr = [1, 2,3, 4,5, 6,7, 8,9]
        arr = [2,4, 6,8]
        arr = [2, 6]
        arr = [6]

Example 2:
        Input: n = 1
        Output: 1
 """

class Solution2:
    def lastRemaining(self, n):
        if n == 1:
            return 1
        else:
            return 2 * (n // 2 + 1 - self.lastRemaining(n // 2))



print(Solution2().lastRemaining(9))
print(Solution2().lastRemaining(1))



print("\n********************  Q3  *************************\n")
""" Q3. Given a set represented as a string, write a recursive code to print all subsets of it. The subsets can be printed in any order.
        You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
Example 1:
    Input: set = “abc”
    Output: { “”, “a”, “b”, “c”, “ab”, “ac”, “bc”, “abc”}
Example 2:
    Input: set = “abcd”
    Output: { “”, “a” ,”ab” ,”abc” ,”abcd”, “abd” ,”ac” ,”acd”, “ad” ,”b”, “bc” ,”bcd” ,”bd” ,”c” ,”cd” ,”d” }
      
        """

class Solution3:
    def printSubsets(self, string, current="", index=0):
        if index == len(string):
            print(current)
            return

        self.printSubsets(string, current, index + 1)
        self.printSubsets(string, current + string[index], index + 1)


print(Solution3().printSubsets("abc"))


print("\n********************  Q4  *************************\n")
""" Q4. Given a string calculate length of the string using recursion.
Examples:
    Input : str = "abcd"
    Output :4

    Input : str = "GEEKSFORGEEKS"
    Output :13

       """

class Solution4:
    def calculateLength(self, string):
        if string == "":
            return 0
        else:
            return 1 + self.calculateLength(string[1:])


print(Solution4().calculateLength("abcd"))
print(Solution4().calculateLength("GEEKSFORGEEKS"))



print("\n********************  Q5  *************************\n")
""" Q5.We are given a string S, we need to find count of all contiguous substrings starting and ending with same character.
Examples:
    Input  : S = "abcab"
    Output : 7
    There are 15 substrings of "abcab"
    a, ab, abc, abca, abcab, b, bc, bca
    bcab, c, ca, cab, a, ab, b
    Out of the above substrings, there
    are 7 substrings : a, abca, b, bcab,
    c, a and b.

    Input  : S = "aba"
    Output : 4
    The substrings are a, b, a and aba
       """
class Solution5:
    def countSubstrings(self, S):
        count = 0
        n = len(S)

        for i in range(n):
            count += 1
            left = i - 1
            right = i + 1

            while left >= 0 and right < n and S[left] == S[right]:
                count += 1
                left -= 1
                right += 1

        return count


print(Solution5().countSubstrings("abcab"))
print(Solution5().countSubstrings("aba"))

print("\n********************  Q6  *************************\n")
""" Q6. The tower of Hanoi is a famous puzzle where we have three rods and N disks. 
        The objective of the puzzle is to move the entire stack to another rod. 
        You are given the number of discs N. Initially, these discs are in the rod 1. 
        You need to print all the steps of discs movement so that all the discs reach the 3rd rod. 
        Also, you need to find the total moves.Note: The discs are arranged such that the top disc is numbered 1 and the bottom-most disc is numbered N. 
        Also, all the discs have different sizes and a bigger disc cannot be put on the top of a smaller disc. Refer the provided link to get a better clarity about the puzzle.
Example 1:
    Input:
        N = 2
    Output:
        move disk 1 from rod 1 to rod 2
        move disk 2 from rod 1 to rod 3
        move disk 1 from rod 2 to rod 3
        3
    Explanation:For N=2 , steps will be
        as follows in the example and total
        3 steps will be taken.


Example 2:
    Input:
        N = 3
    Output:
        move disk 1 from rod 1 to rod 3
        move disk 2 from rod 1 to rod 2
        move disk 1 from rod 3 to rod 2
        move disk 3 from rod 1 to rod 3
        move disk 1 from rod 2 to rod 1
        move disk 2 from rod 2 to rod 3
        move disk 1 from rod 1 to rod 3
    7
Explanation:For N=3 , steps will be
    as follows in the example and total
    7 steps will be taken.

    """
class Solution6:
    def towerOfHanoi(self, n, source, destination, auxiliary):
        if n == 1:
            print(f"move disk 1 from rod {source} to rod {destination}")
            return 1
        else:
            count = 0
            count += self.towerOfHanoi(n - 1, source, auxiliary, destination)
            print(f"move disk {n} from rod {source} to rod {destination}")
            count += 1
            count += self.towerOfHanoi(n - 1, auxiliary, destination, source)
            return count


print(Solution6().towerOfHanoi(2, 1, 3, 2))
print(Solution6().towerOfHanoi(3, 1, 3, 2))



print("\n********************  Q7  *************************\n")
""" Q7. Given a string str, the task is to print all the permutations of str. 
        A permutation is an arrangement of all or part of a set of objects, with regard to the order of the arrangement. 
        For instance, the words 'bat' and 'tab' represents two distinct permutation (or arrangements) of a similar three letter word.
Examples:
    Input:  str = “cd”
    Output: cd dc

    Input: str = “abb”
    Output: abb abb bab bba bab bba

       """
class Solution7:
    def permute(self, str):
        # Convert the string to a list of characters
        chars = list(str)
        # Initialize an empty list to store permutations
        permutations = []
        # Call the helper function to generate permutations
        self.generate_permutations(chars, 0, len(chars) - 1, permutations)
        # Return the list of permutations
        return permutations

    def generate_permutations(self, chars, left, right, permutations):
        if left == right:
            # Convert the list of characters back to a string
            permutation = ''.join(chars)
            # Add the permutation to the list
            permutations.append(permutation)
        else:
            for i in range(left, right + 1):
                # Swap characters at indices left and i
                chars[left], chars[i] = chars[i], chars[left]
                # Recursively generate permutations for the remaining characters
                self.generate_permutations(chars, left + 1, right, permutations)
                # Restore the original order of characters
                chars[left], chars[i] = chars[i], chars[left]


print(Solution7().permute( "cd"))
print(Solution7().permute( "abb"))



print("\n********************  Q8  *************************\n")
""" Q8. Given a string, count total number of consonants in it. 
        A consonant is an English alphabet character that is not vowel (a, e, i, o and u). 
        Examples of constants are b, c, d, f, and g.
Example 1:
    Input : abc de
    Output : 3
        There are three consonants b, c and d.

    Input : geeksforgeeks portal
    Output : 12
       """
class Solution8:
    def count_consonants(self, string):
        consonants = 0
        vowels = "aeiouAEIOU"

        for char in string:
            if char.isalpha() and char not in vowels:
                consonants += 1

        return consonants


print(Solution8().count_consonants("abc de"))
print(Solution8().count_consonants("geeksforgeeks portal"))

