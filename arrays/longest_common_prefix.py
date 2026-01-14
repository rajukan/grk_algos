'''
Write a function to find the longest common prefix string amongst an array of strings.

If there is no common prefix, return an empty string "".



Example 1:

Input: strs = ["flower","flow","flight"]
Output: "fl"

Example 2:

Input: strs = ["dog","racecar","car"]
Output: ""
Explanation: There is no common prefix among the input strings.

'''

class Solution:
    def longestCommonPrefix(self, strs: list[str]) -> str:
        any_word_from_list = strs[0]
        print(any_word_from_list[0:200])
        first_word_len = len(any_word_from_list)

        for next_word in strs[1:]:
            while any_word_from_list != next_word[0:first_word_len]:
                first_word_len -= 1
                if first_word_len == 0:
                    return ""

                any_word_from_list = any_word_from_list[0:first_word_len]

        print(any_word_from_list)
        return any_word_from_list


if __name__ == "__main__":
    s = Solution()
    s.longestCommonPrefix(["flower", "flow", "flower", "flowsbythe"])