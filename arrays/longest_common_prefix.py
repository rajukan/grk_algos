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
        word_str = strs[0]
        print(word_str[0:200])
        prefix_len = len(word_str)

        for next_word in strs[1:]:
            #observe the slicing will not throw any exception if it exceeds the word length (circular count)
            while word_str != next_word[0:prefix_len]:
                prefix_len -= 1
                if prefix_len == 0:
                    return ""

                word_str = word_str[0:prefix_len]

        print(word_str)
        return word_str


if __name__ == "__main__":
    s = Solution()
    s.longestCommonPrefix(["flowerpot", "flow", "flower", "flowsbythe"])