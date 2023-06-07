
print("********************  Q1  *************************")
""" Q1. Given two strings s1 and s2, return the lowest ASCII sum of deleted characters to make two strings equal.

Example 1:
    Input:  s1 = "sea", s2 = "eat"
    Output:  231.
Explanation: Deleting "s" from "sea" adds the ASCII value of "s" (115) to the sum.
    Deleting "t" from "eat" adds 116 to the sum.    
    At the end, both strings are equal, and 115 + 116 = 231 is the minimum sum possible to achieve this.
    """

class Solution1:
   def minimumDeleteSum(self, s1, s2):
        m, n = len(s1), len(s2)
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Initialize the first row and first column
        for i in range(1, m + 1):
            dp[i][0] = dp[i-1][0] + ord(s1[i-1])
        for j in range(1, n + 1):
            dp[0][j] = dp[0][j-1] + ord(s2[j-1])

        # Fill in the remaining cells
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if s1[i-1] == s2[j-1]:
                    dp[i][j] = dp[i-1][j-1]
                else:
                    dp[i][j] = min(dp[i-1][j] + ord(s1[i-1]), dp[i][j-1] + ord(s2[j-1]))

        return dp[m][n]
   
print(Solution1().minimumDeleteSum(s1 = "sea", s2 = "eat"))


print("\n********************  Q2  *************************\n")
""" Q2. Given a string s containing only three types of characters: '(', ')' and '*', return true if s is valid.
        The following rules define a valid string:
        Any left parenthesis '(' must have a corresponding right parenthesis ')'.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        Any right parenthesis ')' must have a corresponding left parenthesis '('.
        '*' could be treated as a single right parenthesis ')' or a single left parenthesis '(' or an empty string "".
    
Example 1:
    Input: s = "()"
    Output: true """

class Solution2:
    def checkValidString(self, s):
        stack = []
        star_stack = []

        for i, char in enumerate(s):
            if char == '(':
                stack.append(i)
            elif char == '*':
                star_stack.append(i)
            else:
                if stack:
                    stack.pop()
                elif star_stack:
                    star_stack.pop()
                else:
                    return False

        while stack and star_stack:
            if stack[-1] > star_stack[-1]:
                return False
            stack.pop()
            star_stack.pop()

        return len(stack) == 0


print(Solution2().checkValidString(s = "()"))



print("\n********************  Q3  *************************\n")
""" Q3. Given two strings word1 and word2, return the minimum number of steps required to make word1 and word2 the same.
    In one step, you can delete exactly one character in either string. 
Example 1:
    Input: word1 = "sea", word2 = "eat"
    Output: 2
     word1 = "sea", word2 = "eat"
Explanation : You need one step to make "sea" to "ea" and another step to make "eat" to "ea". """

class Solution3:
    def minDistance(self, word1, word2):
        m, n = len(word1), len(word2)
        
        # Create a 2D table to store the lengths of LCS for word1[:i] and word2[:j]
        dp = [[0] * (n + 1) for _ in range(m + 1)]

        # Fill in the table
        for i in range(1, m + 1):
            for j in range(1, n + 1):
                if word1[i - 1] == word2[j - 1]:
                    dp[i][j] = dp[i - 1][j - 1] + 1
                else:
                    dp[i][j] = max(dp[i - 1][j], dp[i][j - 1])

        # The minimum number of steps is the sum of the lengths of word1 and word2 minus twice the length of the LCS
        return m + n - 2 * dp[m][n]

print(Solution3().minDistance(word1 = "sea", word2 = "eat"))


print("\n********************  Q4  *************************\n")
""" Q4. You need to construct a binary tree from a string consisting of parenthesis and integers.
        The whole input represents a binary tree. It contains an integer followed by zero, one or two pairs of parenthesis. The integer represents the root's value and a pair of parenthesis contains a child binary tree with the same structure.
        You always start to construct the left child node of the parent first if it exists.
Example 1:
    Input:  s = "4(2(3)(1))(6(5))"
    Output: [4,2,6,3,1,5]
       """


# Solution4
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


def str2tree(s):
    if not s:
        return None

    # Find the index of the first '('
    i = s.find('(')

    # If '(' is not found, the entire string represents the root value
    if i == -1:
        return TreeNode(int(s))

    # Create the root node with the value before '('
    root = TreeNode(int(s[:i]))

    # Count the number of open and close parentheses
    count = 0
    j = i
    for j in range(len(s)):
        if s[j] == '(':
            count += 1
        elif s[j] == ')':
            count -= 1

        # If the count becomes zero, we have found the matching ')' for the first '('
        if count == 0:
            break

    # Recursively construct the left and right subtrees
    root.left = str2tree(s[i + 1:j])
    root.right = str2tree(s[j + 2:-1])

    return root


def inorder_traversal(root):
    if root is None:
        return []

    result = []
    stack = []

    while root or stack:
        while root:
            stack.append(root)
            root = root.left

        node = stack.pop()
        result.append(node.val)
        root = node.right

    return result


# # Example usage:
# s = "4(2(3)(1))(6(5))"
# tree_root = str2tree(s)
# inorder = inorder_traversal(tree_root)
# print(inorder)  # Output: [4, 2, 3, 1, 6, 5]



print("\n********************  Q5  *************************\n")
""" Q5. Given an array of characters chars, compress it using the following algorithm:
    Begin with an empty string s. For each group of consecutive repeating characters in chars:
    If the group's length is 1, append the character to s.
    Otherwise, append the character followed by the group's length.
    The compressed string s should not be returned separately, but instead, be stored in the input character array chars. Note that group lengths that are 10 or longer will be split into multiple characters in chars.
    After you are done modifying the input array, return the new length of the array.
    You must write an algorithm that uses only constant extra space.
Example 1:
    Input: chars = ["a","a","b","b","c","c","c"]
    Output: Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
        Return 6, and the first 6 characters of the input array should be: ["a","2","b","2","c","3"]
Explanation : The groups are "aa", "bb", and "ccc". This compresses to "a2b2c3".
       """
class Solution5:
    def compress(self, chars):
        n = len(chars)
        if n <= 1:
            return n

        anchor = 0  # anchor keeps track of the start position of each group
        write = 0   # write keeps track of the current position in the compressed array

        for read in range(n):
            # If we reach the end of the array or the current character is different from the next one
            if read + 1 == n or chars[read] != chars[read + 1]:
                chars[write] = chars[anchor]  # write the character

                # If the group length is greater than 1, write the count as well
                if read > anchor:
                    count = read - anchor + 1
                    count_str = str(count)
                    chars[write + 1:write + 1 + len(count_str)] = count_str
                    write += len(count_str)

                write += 1
                anchor = read + 1

        return write

print(Solution5().compress(chars = ["a","a","b","b","c","c","c"]))

print("\n********************  Q6  *************************\n")
""" Q6. Given two strings s and p, return an array of all the start indices of p's anagrams in s. You may return the answer in any order.
        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, typically using all the original letters exactly once.
        For example, if s = "abcde", then it will be "bcdea" after one shift.
Example 1:
    Input:  s = "cbaebabacd", p = "abc"
    Output: [0,6]
Explanation: The substring with start index = 0 is "cba", which is an anagram of "abc".
            The substring with start index = 6 is "bac", which is an anagram of "abc".
    """
from collections import Counter
class Solution6:
    def findAnagrams(self, s, p):
        result = []
        p_count = Counter(p)
        window_count = Counter()

        window_start = 0
        for window_end in range(len(s)):
            # Expand the window by adding the rightmost character
            window_count[s[window_end]] += 1

            # Shrink the window if its size is greater than the size of p
            if window_end >= len(p):
                left_char = s[window_start]
                if window_count[left_char] == 1:
                    del window_count[left_char]
                else:
                    window_count[left_char] -= 1
                window_start += 1

            # Check if the current window is an anagram of p
            if window_count == p_count:
                result.append(window_start)

        return result

print(Solution6().findAnagrams(s = "cbaebabacd", p = "abc"))



print("\n********************  Q7  *************************\n")
""" Q7. Given an encoded string, return its decoded string.
        The encoding rule is: k[encoded_string], where the encoded_string inside the square brackets is being repeated exactly k times. Note that k is guaranteed to be a positive integer.
        You may assume that the input string is always valid; there are no extra white spaces, square brackets are well-formed, etc. Furthermore, you may assume that the original data does not contain any digits and that digits are only for those repeat numbers, k. For example, there will not be input like 3a or 2[4].
        The test cases are generated so that the length of the output will never exceed 105.
Example 1:
    Input:  s = "3[a]2[bc]"
    Output: "aaabcbc"
       """
class Solution7:
    def decodeString(self, s):
        stack = []
        current_string = ""
        current_number = 0

        for char in s:
            if char.isdigit():
                current_number = current_number * 10 + int(char)
            elif char == "[":
                stack.append(current_string)
                stack.append(current_number)
                current_string = ""
                current_number = 0
            elif char == "]":
                num = stack.pop()
                prev_string = stack.pop()
                current_string = prev_string + num * current_string
            else:
                current_string += char

        return current_string

print(Solution7().decodeString(  s = "3[a]2[bc]" ))



print("\n********************  Q8  *************************\n")
""" Q8. Given two strings s and goal, return true if you can swap two letters in s so the result is equal to goal, otherwise, return false.
        Swapping letters is defined as taking two indices i and j (0-indexed) such that i != j and swapping the characters at s[i] and s[j].
        For example, swapping at indices 0 and 2 in "abcd" results in "cbad".
Example 1:
    Input: s = "ab", goal = "ba"
    Output: true
Explanation: You can swap s[0] = 'a' and s[1] = 'b' to get "ba", which is equal to goal.
       """
class Solution8:
    def buddyStrings(self, s, goal):
        if len(s) != len(goal):
            return False

        if s == goal and len(set(s)) < len(s):
            return True

        diff_indices = []
        for i in range(len(s)):
            if s[i] != goal[i]:
                diff_indices.append(i)

        if len(diff_indices) == 2:
            i, j = diff_indices
            s = list(s)
            s[i], s[j] = s[j], s[i]
            s = ''.join(s)
            return s == goal

        return False

print(Solution8().buddyStrings(s = "ab", goal = "ba"))

