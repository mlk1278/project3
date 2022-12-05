import random
import math
import numpy as np
from pprint import pprint

# inverse_cdf = sqrt( -6,498 * ln(1-p))
# With the function above, you can give a probability and will get an x value that is aligned with the distribution


"""
@param n is the number of distances you want to generate
"""
def generate_distances(n):
    distances = [None]*n

    for i in range(0,n):
        distances[i] = math.sqrt(-6498 * np.log(1-random.random()))

    return distances

def main():
    n=input("How many sims? (n)\n")
    n = int(n)
    dist = generate_distances(n)
    mean = np.mean(dist)
    print("Values:\n")
    pprint(dist)
    print("Mean: {}".format(mean))

if __name__ == "__main__":
    main()