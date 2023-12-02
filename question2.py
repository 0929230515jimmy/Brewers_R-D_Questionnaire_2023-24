import numpy as np

true_talent_mean = -2
true_talent_std = 1
noise_mean = 0
noise_std = 2

performance_threshold = 0

def prob_true_talent():
  # Calculate the cumulative distribution function (CDF) of the performance distribution
  performance_cdf = np.cumsum(np.exp(-(performance_threshold - true_talent_mean - noise_mean)**2 / (2 * noise_std**2)) * (1 / (np.sqrt(2 * np.pi) * noise_std)))

  # Calculate the CDF of the true talent distribution
  true_talent_cdf = np.cumsum(np.exp(-(true_talent_mean - true_talent_mean)**2 / (2 * true_talent_std**2)) * (1 / (np.sqrt(2 * np.pi) * true_talent_std)))

  # Calculate the probability of a player having a true talent above 0 given a performance above the threshold
  prob_true_talent = performance_cdf[performance_cdf > 0][-1] / true_talent_cdf[true_talent_cdf > 0][-1]

  return prob_true_talent

probability = prob_true_talent()

print(probability)
