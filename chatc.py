import numpy as np
import matplotlib.pyplot as plt

# Generate 100,000 samples from a normal distribution
mean = 0
std = 1
num_samples = 100000
samples = np.random.normal(mean, std, num_samples)

# Plot the histogram
plt.hist(samples, bins=500, density=True, alpha=0.7)

# Add labels and title
plt.xlabel('Value')
plt.ylabel('Frequency')
plt.title('Histogram of Normal Distribution')

# Display the plot
plt.show()