import random
from collections import Counter
#
# Von Neumann's Solution (1951)
#
# Von Neumann came up with a clever method to eliminate bias without knowing the bias probability p.
#
# Key Insight:
#
# Even though the coin is biased, some sequences of outcomes are equally likely, regardless of the value of p.
#
# Specifically:
#
# The pair (Heads, Tails) has probability:
# P(H then T) = p * (1 - p)
#
# The pair (Tails, Heads) has probability:
# P(T then H) = (1 - p) * p
#
# These two probabilities are equal.
#
# But:
#
# (Heads, Heads) = p * p → biased
#
# (Tails, Tails) = (1 - p) * (1 - p) → biased
#
# Algorithm:
#
# Flip the biased coin twice.
#
# If the outcome is:
#
# Heads, Tails → return 1 (or "heads")
#
# Tails, Heads → return 0 (or "tails")
#
# Heads, Heads or Tails, Tails → discard and repeat
#
# This ensures unbiased outcomes.

'''
More context:

There are many ways to remove the bias from an unfair coin but the most popular method was proposed by the legendary polymath, John “Johnny” Von Neumann. Here is the simple algorithm that von Neumann devised:

    Toss the coin twice
    If the results match, start over, forgetting both results.
    If the results differ, use the first result, forgetting the second.

How it works

Assuming the coin flips are independent and the same coin is used in both tosses, the probability of getting different results across tosses will always be the same. That is, P(HT) = P(TH).

Let’s look at a concrete example to buttress this point. Say we have a biased coin that returns heads 80% of the time (p = 0.8). Obviously, this coin will return tails 20% of the time (q = 1-p = 0.2). On two consecutive coin tosses, we will have 1 of these 4 outcomes, [HH, HT, TH, TT] with corresponding probabilities,

P(HH) = p² = 0.8² = 0.64

P(HT) = pq = 0.8 x 0.2 = 0.16

P(TH) = qp = 0.2 x 0.8 = 0.16

P(TT) = q² = 0.2² = 0.04

Notice how the probability for HEADS followed by TAILS is the same as that of TAILS followed by HEADs .16. This means that we have two equiprobable events, P(HT) = P(TH), 
that can substitute as the event space for tossing an unbiased coin, (P(H) = P(T) = 0.5). Essentially, 
when we get HEADS on the first toss and TAILS on the second, we record that as a fair HEADS event. Similarly, when we get TAILS on the first toss and HEADS on the second, 
we record that as a fair TAILS event.
'''

def biased_coin_flip():
    #enforce bias
    p=0.8

    # return 1 if random.random()<p else 0
    return "H" if random.random() < p else "T"

def unbiased_coin_flip():

    #Flip atleast twice
    while True:
        flip_1=biased_coin_flip()
        flip_2=biased_coin_flip()

        if flip_1!=flip_2:
            return flip_1

        #else continue to flip again





if __name__ == '__main__':
    # print(unbiased_coin_flip())
    # print([biased_coin_flip() for _ in range(3)])
    # print([unbiased_coin_flip() for _ in range(5)])

    results = Counter(biased_coin_flip() for _ in range(1_000_000))
    print(f"Biased {results}")
    results = Counter(unbiased_coin_flip() for _ in range(1_000_000))
    print(f"Unbiased {results}")
