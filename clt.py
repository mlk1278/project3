import simulab_driver as sd
import math
import matplotlib.pyplot as plt
import numpy as np

def problem_3a():

    N_VALS = [2,6,10]

    master_means = sd.generate_sample_means(N_VALS,100000)

    # master_means now contains 3 rows of 100 000 sample means

    # Though not very good coding practice, I will seperate the three rows into their own arrays to make the project easier

    means_2 = master_means[0]
    means_6 = master_means[1]
    means_10 = master_means[2]

    figure, axis = plt.subplots(3)
    axis[0].hist(means_2,bins=100,range=(0,200))

    # Histogram plot of frequencies
    axis[0].plot()

    axis[0].set_title('Sample means for n=2 trials')
    axis[0].set_xlabel('dist (in)')
    axis[0].set_ylabel('M(x) occurances')

    axis[1].hist(means_6,bins=100,range=(0,200))

    # Histogram plot of frequencies
    axis[1].plot()

    axis[1].set_title('Sample means for n=6 trials')
    axis[1].set_xlabel('dist (in)')
    axis[1].set_ylabel('M(x) occurances')

    axis[2].hist(means_10,bins=100,range=(0,200))

    # Histogram plot of frequencies
    axis[2].plot()

    axis[2].set_title('Sample means for n=10 trials')
    axis[2].set_xlabel('dist (in)')
    axis[2].set_ylabel('M(x) occurances')


    plt.show()

def problem_3b():
    TRIALS = 1000
    N_VALS = range(2,32,2)
    N_VALS_LEN = len(N_VALS)

    sample_means = sd.generate_sample_means(N_VALS,TRIALS)

    rows, cols = (N_VALS_LEN, TRIALS)
    normalized_sample_means = [[0 for i in range(cols)] for j in range(rows)]

    for i in range(0,N_VALS_LEN):

        # Calculates necessary params to normalize distribution
        mean = np.mean(sample_means[i])
        var = np.var(sample_means[i])
        std = math.sqrt(var)

        # Creates and sorts a normalized distribution of the sample means
        normalized_sample_means[i] = np.sort([(sample_means[i][x]-mean)/std for x in range(0,TRIALS)])

    z_intervals = [-1.4,-1,-.5,0,0.5,1,1.4]

    rows, cols = (N_VALS_LEN, len(z_intervals))
    approx_cdf = [[0 for i in range(cols)] for j in range(rows)]

    trials_flt = float(TRIALS)

    for n in range(0,N_VALS_LEN):
            i = 0
            sum = 0.0
            for z in range(0,len(z_intervals)):
                # Itereates through and, while the value is less than the current z interval, accumulates its sum
                while(i<TRIALS and normalized_sample_means[n][i]<=z_intervals[z]):
                    sum+=1
                    i+=1
                # Assigns cumulative probability for the corresponding z interval
                approx_cdf[n][z] = sum/trials_flt
    print(approx_cdf)

    proper_normal = [.08076,.15866,.30854,.50000,.69146,.84134,.91924]

    normal_differences = []

    # Calculates  the differences using list comprehension
    normal_differences[n] = [[abs(approx_cdf[n][i]-proper_normal[i]) for i in range(z_intervals)] for n in range(len(N_VALS_LEN))]

    """
    Okay, so for all arrays, the row value is the number of trials (corresponding value in N_VALS
    
    sample_means contains the generated sample means
    mean_mn and var_mn were calculated and used to create the normalized distribution
    the normalized distribution is contained in normalized_sample_means
    
    approx_cdf holds the calculated CDF for the given values of Z based on the sample normalized distribution of Mn(x)
    
    normal_differences contains the differences between the sampled CDFs and what the CDF for a normal distribution is.
    
    """



