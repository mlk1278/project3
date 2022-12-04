import simulab_driver as sd

N_VALS = [2,6,10]

master_means = sd.generate_sample_means(N_VALS,100000)

# master_means now contains 3 rows of 100 000 sample means

# Though not very good coding practice, I will seperate the three rows into their own arrays to make the project easier

means_2 = master_means[0]
means_6 = master_means[1]
means_10 = master_means[2]

