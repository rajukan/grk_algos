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

        for flight_arr in flights:
            from_i = flight_arr[0]
            to_i=flight_arr[1]
            price_i=flight_arr[2]
            #This is the core operation. It looks up the starting city in the adj structure and adds a tuple containing the destination and the price.
            adj[from_i].append((to_i,price_i))


        '''
        Given flights = [[0, 1, 100], [0, 2, 500], [1, 2, 100]]
        this  adj= [[(1, 100), (2, 500)], [(2, 100)], [], []]
        
        Before (Edge List)= Flights: [[0, 1, 100], [0, 2, 500], [1, 2, 100]]
        After: adj ( simply a list with each index containing 0 or more list of tuples
        {
          0: [(1, 100), (2, 500)],  # From City 0, you can go to 1 (cost 100) or 2 (cost 500)
          1: [(2, 100)],            # From City 1, you can go to 2 (cost 100)
          2: []                     # From City 2, there are no outgoing flights
        }
        '''

        flight_queue = [(src, 0)]
        best_prices_found = [float('inf') for _ in range(n)]
        layovers_count = 0

        # Continue searching as long as we have flights to check
        # and we haven't exceeded the maximum allowed layovers (k).
        while flight_queue and layovers_count <= k:

            # Take a "snapshot" of how many cities are at the current layover level.
            cities_at_current_level = len(flight_queue)

            for _ in range(cities_at_current_level):
                current_city, total_spent_so_far = flight_queue.pop(0)

                # Check all possible direct flights from the current city.
                for destination_city, ticket_price in adj[current_city]:
                    new_total_cost = total_spent_so_far + ticket_price

                    # If this new route is more expensive than a previous route
                    # we've already found, skip it (the gatekeeper).
                    if new_total_cost >= best_prices_found[destination_city]:
                        continue

                    # If we found a new "best price," update our records and
                    # add this city to the queue to explore its connections next.
                    best_prices_found[destination_city] = new_total_cost
                    flight_queue.append((destination_city, new_total_cost))

                    '''
                    if the continue statement is confusing, below is the alternative way
                    '''
                    # WE ONLY ACT IF the new path is strictly cheaper than what we've found before.
                    # if new_total_cost < best_prices_found[destination_city]:
                    #     best_prices_found[destination_city] = new_total_cost
                    #     flight_queue.append((destination_city, new_total_cost))



            layovers_count += 1

        return -1 if best_prices_found[dst] == float('inf') else best_prices_found[dst]


if __name__=='__main__':
        s = Solution()
        print(s.findCheapestPrice(n = 3, flights = [[0,1,100],[1,2,100],[0,2,500]], src = 0, dst = 2, k = 1))
        print(s.findCheapestPrice(n = 4, flights = [[0,1,100],[1,2,100],[2,0,100],[1,3,600],[2,3,200]], src = 0, dst = 3, k = 1))
        print(s.findCheapestPrice(n = 4, flights = [[0, 1, 100], [0, 2, 500], [1, 2, 100]], src = 0, dst = 2, k = 1))

