'''

There are n gas stations along a circular route, where the amount of gas at the ith station is gas[i].

You have a car with an unlimited gas tank and it costs cost[i] of gas to travel from the ith station to its next (i + 1)th station.
You begin the journey with an empty tank at one of the gas stations.

Given two integer arrays gas and cost, return the starting gas station's index if you can travel around the circuit
 once in the clockwise direction, otherwise return -1. If there exists a solution, it is guaranteed to be unique.



Example 1:

Input: gas = [1,2,3,4,5], cost = [3,4,5,1,2]
Output: 3
Explanation:
Start at station 3 (index 3) and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 4. Your tank = 4 - 1 + 5 = 8
Travel to station 0. Your tank = 8 - 2 + 1 = 7
Travel to station 1. Your tank = 7 - 3 + 2 = 6
Travel to station 2. Your tank = 6 - 4 + 3 = 5
Travel to station 3. The cost is 5. Your gas is just enough to travel back to station 3.
Therefore, return 3 as the starting index.

Example 2:

Input: gas = [2,3,4], cost = [3,4,3]
Output: -1
Explanation:
You can't start at station 0 or 1, as there is not enough gas to travel to the next station.
Let's start at station 2 and fill up with 4 unit of gas. Your tank = 0 + 4 = 4
Travel to station 0. Your tank = 4 - 3 + 2 = 3
Travel to station 1. Your tank = 3 - 3 + 3 = 3
You cannot travel back to station 2, as it requires 4 unit of gas but you only have 3.
Therefore, you can't travel around the circuit once no matter where you start.


'''

'''
i, gas[i], cost[i], res=gas[i] + 0

[1,2,3,4,5]
[3,4,5,1,2]

4,5,1,2,3
1,2,3,4,5

4-1+5-2+1-3+2-4+3-5=0

4-1+5-2+1-3+2-4+3= cost[4]

gas[i] - cost[i] + gas[i+1] - cost[i+1]   == cost[last index]

2,3,4
3,4,3 

2-3+3-4+4==3


'''

'''
THE ESSENCE OF THE PROBLEM

You have a circular route with gas stations, each giving you some gas but also charging you to travel to the next station. The trick is to find where to start so you can complete the entire circle without running out of fuel.

Key Insight: Instead of trying every starting point (which would be painfully slow), you can solve this with one smart pass through all stations. The solution lies in tracking two simple balances: one for the whole trip and one for your current attempt.

Think of it like trying to complete a marathon. If you collapse at mile 5, starting at mile 1 or 2 or 3 wouldn't have helped — you still would've collapsed at that same mile 5. The only sensible next try is to start fresh from mile 6.

You just track two running totals. One tells you if a solution exists at all, and the other helps you find where to start.

    We need to check if we can complete the circuit. Instead of simulating from every station, we track the total gas minus cost for the entire route. If that's negative, it's impossible. If it's positive, there's exactly one valid starting point — the one where our running balance never dips below zero.

The real magic happens when you realize you don't need to simulate full circles. Once you've found a starting point that gets you to the end of the array without going negative, that's your answer.

    There's a mathematical guarantee: if the total gas is at least the total cost, there must be exactly one valid starting station. And you'll find it by this greedy approach.

EXAMPLES OF WORK
💠 Example 1:

gas  = [1, 2, 3, 4, 5]
cost = [3, 4, 5, 1, 2]

Analysis:

    At station 0: gain = 1 - 3 = -2 (can't start here)
    At station 1: gain = 2 - 4 = -2 (can't start here)
    At station 2: gain = 3 - 5 = -2 (can't start here)
    At station 3: gain = 4 - 1 = +3 (good candidate)
        Continue: +3 (from 3→4) + (5-2) = +6
        Continue: +6 + (1-3) = +4
        Continue: +4 + (2-4) = +2
        Continue: +2 + (3-5) = 0 (complete circuit!)
    Answer: 3

💠 Example 2:

gas  = [2, 3, 4]
cost = [3, 4, 3]

Analysis:

    Total gain: (2-3) + (3-4) + (4-3) = -1 -1 +1 = -1
    Since total gain is negative, no starting point works
    Answer: -1

LINE-BY-LINE EXPLANATION OF THE CODE
STEP 1: INITIALIZATION AND VARIABLE SETUP

public int canCompleteCircuit(int[] gas, int[] cost) {
    int n = gas.length;
    int total_tank = 0, curr_tank = 0, start_pos = 0;

What's happening here:

    n gets the number of stations (same for both arrays)
    total_tank will accumulate the overall gas balance for the entire circuit
    curr_tank tracks the gas balance for our current attempted starting point
    start_pos remembers where we're trying to start from (initially station 0)

Think of it like this: You're trying to find the right place to start a road trip. total_tank tells you if the trip is even possible overall, while curr_tank is the gas gauge for your current attempt.
STEP 2: THE MAIN LOOP - CHECKING EACH STATION

for (int i = 0; i < n; i++) {
    int gain = gas[i] - cost[i];
    total_tank += gain; 
    curr_tank += gain;

What's happening here:

    For each station i, we calculate the net gain/loss: how much gas we get minus how much we need to leave
    gain could be positive (more gas than needed) or negative (costs more than we get)
    We add this to both counters:
        total_tank tracks the overall balance (ignoring starting point)
        curr_tank tracks the balance for our current starting attempt

The key intuition: Each station either gives you a "profit" or a "loss" of gas relative to what you need to reach the next station. You're essentially looking for a starting point where you never accumulate too many losses before getting profits.
STEP 3: THE GREEDY RESET - WHEN TO ABANDON A STARTING POINT

    if (curr_tank < 0) {
        curr_tank = 0;
        start_pos = i + 1;
    } 
}

What's happening here:

    If curr_tank goes negative at station i, our current starting point start_pos is invalid
    Why? Because if we started at start_pos and ran out of gas by station i, then any station between start_pos and i would have failed even sooner
    We reset curr_tank to 0 and try starting from the next station (i + 1)

The clever part: This is where we avoid checking every starting point. Once we fail at some station i, we know all stations from our current start_pos to i are bad starting points. So we jump straight to i + 1.

'''
class Solution:
    def canCompleteCircuit(self, gas: list[int], cost: list[int]) -> int:
        total_stations = len(gas)
        total_tank = curr_tank = start_pos =0

        for station in range(total_stations):
            gain = gas[station] - cost[station]
            total_tank += gain
            curr_tank += gain

            if curr_tank < 0:
                #reset station, // We need to explore a new start point as the current tank can never go below 0. Rem 0 is fine that means you just reached the station
                curr_tank=0
                start_pos= station + 1

        if total_tank >= 0 :
            return start_pos

        return -1


if __name__ == "__main__":
    s = Solution()
    gas = [1,2,3,4,5]
    cost = [3,4,5,1,2]

    gas=[2,3,4]
    cost=[3,4,3]

    gas=[7, 1, 0, 11, 4]
    cost=[5, 9, 1, 2, 5]


    gas=[2,4,5,9,10,12]
    cost=[10,8,1,20,1,1]


    print(s.canCompleteCircuit(gas,cost))