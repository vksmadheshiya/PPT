
print("********************  Q1  *************************")
""" Q1. Given two strings s and t, determine if they are isomorphic.
        Two strings s and t are isomorphic if the characters in s can be replaced to get t.
        All occurrences of a character must be replaced with another character while preserving the order of characters. No two characters may map to the same character, but a character may map to itself.
Example 1:
    Input:  s = "egg", t = "add"
    Output: true.    
    """

class Solution1:
    def isIsomorphic(self, s, t):
        if len(s) != len(t):
            return False

        char_map = {}
        used_chars = set()

        for i in range(len(s)):
            char_s = s[i]
            char_t = t[i]

            if char_s in char_map:
                if char_map[char_s] != char_t:
                    return False
            else:
                if char_t in used_chars:
                    return False
                char_map[char_s] = char_t
                used_chars.add(char_t)

        return True
   
print(Solution1().isIsomorphic(s = "egg", t = "add"))


print("\n********************  Q2  *************************\n")
""" Q2. Given a string num which represents an integer, return true if num is a strobogrammatic number.
    - A strobogrammatic number is a number that looks the same when rotated 180 degrees (looked at upside down).
    
Example 1:
    Input: num = "69"
    Output: true """

class Solution2:
    def isStrobogrammatic(self, num):
        strobogrammatic_pairs = {'0': '0', '1': '1', '6': '9', '8': '8', '9': '6'}
        left, right = 0, len(num) - 1

        while left <= right:
            if num[left] not in strobogrammatic_pairs or strobogrammatic_pairs[num[left]] != num[right]:
                return False
            left += 1
            right -= 1

        return True

print(Solution2().isStrobogrammatic(num = "69"))



print("\n********************  Q3  *************************\n")
""" Q3. Given two non-negative integers, num1 and num2 represented as string, return the sum of num1 and num2 as a string.
        You must solve the problem without using any built-in library for handling large integers (such as BigInteger). You must also not convert the inputs to integers directly.
Example 1:
    Input: num1 = "11", num2 = "123"
    Output: "134" """

class Solution3:
    def addStrings(self, num1, num2):
        result = []
        carry = 0
        i, j = len(num1) - 1, len(num2) - 1

        while i >= 0 or j >= 0 or carry:
            digit1 = int(num1[i]) if i >= 0 else 0
            digit2 = int(num2[j]) if j >= 0 else 0
            summation = digit1 + digit2 + carry

            carry = summation // 10
            digit = summation % 10
            result.append(str(digit))

            i -= 1
            j -= 1

        result.reverse()
        return ''.join(result)


print(Solution3().addStrings(num1 = "11", num2 = "123"))


print("\n********************  Q4  *************************\n")
""" Q4. Given a string s, reverse the order of characters in each word within a sentence while still preserving whitespace and initial word order.
Example 1:
    Input: s = "Let's take LeetCode contest"
    Output: "s'teL ekat edoCteeL tsetnoc"
       """

class Solution4:
    def reverseWords(self, s):
        words = s.split()  # Split the sentence into individual words
        reversed_words = [word[::-1] for word in words]  # Reverse each word
        return ' '.join(reversed_words)  # Join the reversed words with whitespace


print(Solution4().reverseWords(s = "Let's take LeetCode contest"))



print("\n********************  Q5  *************************\n")
""" Q5. Given a string s and an integer k, reverse the first k characters for every 2k characters counting from the start of the string.
    If there are fewer than k characters left, reverse all of them. If there are less than 2k but greater than or equal to k characters, then reverse the first k characters and leave the other as original.
    Input: s = "abcdefg", k = 2
    Output: "bacdfeg"
       """
class Solution5:
    def reverseStr(self, s, k):
        n = len(s)
        chars = list(s)  # Convert the string to a list of characters

        for i in range(0, n, 2*k):
            left = i
            right = min(i+k-1, n-1)

            while left < right:
                chars[left], chars[right] = chars[right], chars[left]
                left += 1
                right -= 1

        return ''.join(chars)  # Convert the list of characters back to a string

print(Solution5().reverseStr(s = "abcdefg", k = 2))

print("\n********************  Q6  *************************\n")
""" Q6. Given two strings s and goal, return true if and only if s can become goal after some number of shifts on s.
        A shift on s consists of moving the leftmost character of s to the rightmost position.
        For example, if s = "abcde", then it will be "bcdea" after one shift.
Example 1:
    Input:  s = "abcde", goal = "cdeab"
    Output: true
    """
class Solution6:
    def rotateString(self, s, goal):
        if len(s) != len(goal):
            return False

        return goal in s + s

print(Solution6().rotateString(s = "abcde", goal = "cdeab"))



print("\n********************  Q7  *************************\n")
""" Q7. Given two strings s and t, return true if they are equal when both are typed into empty text editors. '#' means a backspace character.
        Note that after backspacing an empty text, the text will continue empty.
Example 1:
    Input:  s = "ab#c", t = "ad#c"
    Output: true
Explanation: Both s and t become "ac".
       """
class Solution7:
    def backspaceCompare(self, s, t):
        def build_string(string):
            stack = []
            for char in string:
                if char != '#':
                    stack.append(char)
                elif stack:
                    stack.pop()
            return "".join(stack)

        return build_string(s) == build_string(t)


print(Solution7().backspaceCompare( s = "ab#c", t = "ad#c" ))



print("\n********************  Q8  *************************\n")
""" Q8. You are given an array coordinates, coordinates[i] = [x, y], where [x, y] represents the coordinate of a point. Check if these points make a straight line in the XY plane.
Example 1:
    Input: coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]
    Output: true
       """
class Solution8:
    def checkStraightLine(self, coordinates):
        x0, y0 = coordinates[0]
        x1, y1 = coordinates[1]
        for i in range(2, len(coordinates)):
            xi, yi = coordinates[i]
            if (y1 - y0) * (xi - x0) != (yi - y0) * (x1 - x0):
                return False
        return True

print(Solution8().checkStraightLine(coordinates = [[1,2],[2,3],[3,4],[4,5],[5,6],[6,7]]))

