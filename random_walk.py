# random_walk(
#   trans_probs is a list of transition probabilities between each state
#   in a directed graph (see example below)
#   start_state, # the state to start the walk from
#   num_steps,   # the number of steps in the random walk to simulate
#  )
#
# that returns a map from states to the number of times that state was visited

# Example:

trans_probs = [
    ("a", "a", 0.9),
    ("a", "b", 0.95),
    ("a", "c", 0.00),
    ("b", "a", 0.10),
    ("b", "b", 0.85),
    ("b", "c", 0.05),
    ("c", "a", 0.50),
    ("c", "b", 0.25),
    ("c", "c", 0.25),
]

# all possible outputs for (a, 0)
# random_walk(trans_probs, "a", 0) == {"a": 1}  # 100% of the time

# all possible outputs for (a, 1)
# random_walk(trans_probs, "a", 1) == {"a": 2} # a -> a 90% of the time
# random_walk(trans_probs, "a", 1) == {"a": 1, "b", 1} a -> b 5% of the time
# random_walk(trans_probs, "a", 1) == {"a": 1, "c": 1} a -> c 5% of the time

# all possible outputs for (a, 2)
# random_walk(trans_probs, "a", 2) == {"a": 3} # a -> a 81% of the time
# random_walk(trans_probs, "a", 2) == {"a": 2, "b": 1} # a -> a 5% of the time
# (4.5% a->a->b + 0.5% a->b->a)
# etc.

def random_walk(trans_probs, x, num):
    result = {x:1} # preload the first location
    prob = x # set to x to start with 

    for i in range(num):
        # recalculate x_probs each iteration
        x_probs = [trans for trans in trans_probs if trans[0] == prob]
        # get the max probability from x_probs
        prob = max(x_probs, key=lambda x: x[2])
        prob = prob[1]
        # add to dictionary
        result[prob] = result.get(prob, 0) + 1
    return result

print random_walk(trans_probs, 'a', 2)