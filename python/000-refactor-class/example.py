import numpy as np
import matplotlib.pyplot as plt


input_sequence = 0.01*np.pi + 0.001*np.random.standard_normal(10000)
output_sequence = np.zeros_like(input_sequence)

# Memory factor (how much the filter "remembers")
memory_factor = 100

# Actual filter parameter
alpha = 1.0 - 1.0 / memory_factor

# Buffer for accumulator
accum = input_sequence[0] / (1-alpha) # Initialize with first single estimate

for n, input_sample in enumerate(input_sequence):
    accum = alpha * accum + input_sample
    output_sequence[n] = (1-alpha) * accum

plt.figure()
plt.plot(input_sequence)
plt.plot(output_sequence)
plt.title("in v out")
plt.show()

