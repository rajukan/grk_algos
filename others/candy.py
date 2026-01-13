'''

There are n children standing in a line. Each child is assigned a rating value given in the integer array ratings.

You are giving candies to these children subjected to the following requirements:

    Each child must have at least one candy.
    Children with a higher rating get more candies than their neighbors.

Return the minimum number of candies you need to have to distribute the candies to the children.



Example 1:

Input: ratings = [1,0,2]
Output: 5
Explanation: You can allocate to the first, second and third child with 2, 1, 2 candies respectively.

Example 2:

Input: ratings = [1,2,2]
Output: 4
Explanation: You can allocate to the first, second and third child with 1, 2, 1 candies respectively.
The third child gets 1 candy because it satisfies the above two conditions.

Trick: Instead of hashmap use candies array
Trick: Instead of hashmap use candies array
'''


class Solution(object):
    def candy(self, ratings):
        n = len(ratings)
        #initialize all kids get atleast 1
        candies = [1] * n
        #compare with previous kid
        for i in range(1, n):
            if ratings[i] > ratings[i - 1]:
                candies[i] = candies[i - 1] + 1
        #right to left and compare,
        for i in range(n - 1, 0, -1):
            if ratings[i - 1] > ratings[i]:
                # As the previous kid has better ratings meaning  either he has to get 1 more  than i ( candies[i]+1) or whatever he holds currently, whichever is maximum
                candies[i - 1] = max(candies[i] + 1, candies[i - 1])
        print(ratings)
        print(candies)
        return sum(candies)


if __name__ == '__main__':
    solution = Solution()
    ratings=[1,2,0,4,10]

    print(solution.candy(ratings))

