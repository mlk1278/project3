import simulab_driver as sd
import math
import matplotlib.pyplot as plt
import numpy as np





def problem_3a():

    N_VALS = [2,6,10]

    master_means = sd.generate_sample_means(N_VALS,100000)

    display_histos(N_VALS,master_means, range(0,200))


def problem_3b():
    t = 100000
    vals = range(2, 32, 2)

    sample_means, normal_sample_means, mad_arr = create_normalized_and_mad(t, vals)


"""
This method displays histograms for variation selections of n values and their distributions

@param n_vals is the set of n values
@param dist is an array (n_vals x trials) in dimension
@param is the range
"""
def display_histos(n_vals, dist, rng):
    N_VALS = n_vals

    figure, axis = plt.subplots(len(N_VALS))

    for i in range(len(N_VALS)):
        axis[i].hist(dist[i], bins=100, range=rng)

        # Histogram plot of frequencies
        axis[i].plot()

        axis[i].set_title('Sample means for n={} trials'.format(N_VALS[i]))
        axis[i].set_xlabel('dist (in)')
        axis[i].set_ylabel('M(x) occurances')
    plt.show()


"""
Creates normalized distributions for various sets

@param trials is the number of independent sample means you are generating
@param n_vals is the set of n values that those sample means were generated for
@return sample_means is the set of sample means (n_vals x trials) in dimension
@return normalized_sample_means is the normalized set of sample means (n_vals x trials) in dimension
@return mad_arr is the MAD between a normal distribution and the normalized sample mean distributions (n_vals) in dimension
"""
def create_normalized_and_mad(trials, n_vals):
    TRIALS = trials
    N_VALS = n_vals
    N_VALS_LEN = len(N_VALS)

    sample_means = sd.generate_sample_means(N_VALS, TRIALS)

    rows, cols = (N_VALS_LEN, TRIALS)
    normalized_sample_means = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0, N_VALS_LEN):
        # Calculates necessary params to normalize distribution
        mean = np.mean(sample_means[i])
        var = np.var(sample_means[i])
        std = math.sqrt(var)

        # Creates and sorts a normalized distribution of the sample means
        normalized_sample_means[i] = np.sort([(sample_means[i][x] - mean) / std for x in range(0, TRIALS)])

    z_intervals = [-1.4, -1, -.5, 0, 0.5, 1, 1.4]

    num_z_intervals = len(z_intervals)

    rows, cols = (N_VALS_LEN, num_z_intervals)
    approx_cdf = [[0 for i in range(cols)] for j in range(rows)]

    trials_flt = float(TRIALS)

    for n in range(0, N_VALS_LEN):
        i = 0
        sum = 0.0
        for z in range(0, num_z_intervals):
            # Itereates through and, while the value is less than the current z interval, accumulates its sum
            while (i < TRIALS and normalized_sample_means[n][i] <= z_intervals[z]):
                sum += 1
                i += 1
            # Assigns cumulative probability for the corresponding z interval
            approx_cdf[n][z] = sum / trials_flt

    proper_normal = [.08076, .15866, .30854, .50000, .69146, .84134, .91924]

    # Calculates  the differences using list comprehension
    normal_differences = [[abs(approx_cdf[n][i] - proper_normal[i]) for i in range(num_z_intervals)] for n in
                          range(N_VALS_LEN)]

    mad_arr = [max(normal_differences[n]) for n in range(N_VALS_LEN)]

    print(mad_arr)

    return sample_means,normalized_sample_means,mad_arr

    """
    Okay, so for all arrays, the row value is the number of trials (corresponding value in N_VALS

    sample_means contains the generated sample means
    mean_mn and var_mn were calculated and used to create the normalized distribution
    the normalized distribution is contained in normalized_sample_means

    approx_cdf holds the calculated CDF for the given values of Z based on the sample normalized distribution of Mn(x)

    normal_differences contains the differences between the sampled CDFs and what the CDF for a normal distribution is.

    """




