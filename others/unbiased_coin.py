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

def biased_coin_flip():
    p=0.8 #enforce bias]
    return 1 if random.random()<p else 0

def unbiased_coin_flip():

    while True:
        flip_1=biased_coin_flip()
        flip_2=biased_coin_flip()

        if flip_1!=flip_2:
            return flip_1

        #else continue to flip again





if __name__ == '__main__':
    # print(unbiased_coin_flip())
    results = Counter(biased_coin_flip() for _ in range(6))
    print(f"Biased {results}")
    results = Counter(unbiased_coin_flip() for _ in range(6))
    print(f"Unbiased {results}")