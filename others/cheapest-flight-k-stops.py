'''

There are n cities connected by some number of flights. You are given an array flights where flights[i] = [fromi, toi, pricei] indicates that there is a flight from city fromi to city toi with cost pricei.
You are also given three integers src, dst, and k, return the cheapest price from src to dst with at most k stops. If there is no such route, return -1.

Example 1:

Input: n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1
Output: 700
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 3 is marked in red and has cost 100 + 600 = 700.
Note that the path through cities [0,1,2,3] is cheaper but is invalid because it uses 2 stops.

Example 2:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1
Output: 200
Explanation:
The graph is shown above.
The optimal path with at most 1 stop from city 0 to 2 is marked in red and has cost 100 + 100 = 200.

Example 3:

Input: n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 0
Output: 500
Explanation:
The graph is shown above.
The optimal path with no stops from city 0 to 2 is marked in red and has cost 500.


Approach for this Problem

    Initialize an adjacency list with the given flights information, where each index i represents the node i, and the corresponding value is a list of pairs (neighbor, price) representing the edges from node i to its neighboring nodes and the price of the flight.
    Initialize a queue with the source node and its cost (0) and a vector minCost with the same size as the number of nodes, where each index i represents the minimum cost to reach node i and the corresponding value is initialized to INT_MAX.
    Create a variable stops and initialize it to 0.
    Start a while loop until the queue is not empty and stops are less than or equal to k (maximum stops allowed).
    In the while loop, create a variable size equal to the size of the queue.
    Start another while loop with the size of the queue.
    In the inner while loop, pop the front element from the queue and assign it to a variable (currNode, cost).
    Iterate through the neighbors and price of the current node from the adjacency list.
    If the total cost to reach the neighbor is greater than or equal to the minimum cost to reach the neighbor, continue to the next iteration.
    Else, update the minimum cost to reach the neighbor as the total cost and push the neighbor and its cost to the queue.
    End the inner while loop and increment the stops by 1.
    End the outer while loop.
    If the minimum cost to reach the destination is still INT_MAX, return -1, otherwise, return the minimum cost to reach the destination.


'''
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        adj = [ [] for _ in range(n) ]
        for flight in flights:
            adj[flight[0]].append((flight[1], flight[2]))

        q = [(src, 0)]
        minCost = [float('inf') for _ in range(n)]
        stops = 0

        while q and stops <= k:
            size = len(q)
            for i in range(size):
                currNode, cost = q.pop(0)
                for neighbour, price in adj[currNode]:
                    if price + cost >= minCost[neighbour]:
                        continue
                    minCost[neighbour] = price + cost
                    q.append((neighbour, minCost[neighbour]))
            stops += 1

        return -1 if minCost[dst] == float('inf') else minCost[dst]


if __name__=='__main__':
        s = Solution()
        print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))

        print(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))