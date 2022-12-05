import simulab as sl
import numpy as np
from pprint import pprint


"""
@param N_VALS is the set of n_values you would like to generate data for
@param num_of_means is the number of independent sample means you want to generate
"""

def generate_sample_means(N_VALS, num_of_means):
    master_sample_means = [None] * len(N_VALS)
    n_vals_len = len(N_VALS)

    for n in range(n_vals_len):
        sample_means = [0] * num_of_means
        for i in range(0, num_of_means):
            dist = sl.generate_distances(N_VALS[n])
            sample_means[i] = np.mean(dist)
        master_sample_means[n] = sample_means
    return master_sample_means


def main():
    N_VALS =[10, 30, 50, 100, 250, 500, 1000]
    my_sample_means = generate_sample_means(N_VALS, 250)
    pprint(my_sample_means)
    # my_sample_means now has 7 rows, each representing an array holding sample means for an n_value.
    # For example, accessing my_sample_means[2][249] is accessing the 250th mean (index 249)
    # that was generated for an n value of 50 (the n-value at index 2 of the N_VALS array).


if __name__ == "__main__":
    main()


