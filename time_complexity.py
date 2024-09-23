import numpy as np
import matplotlib.pyplot as plt

# Define input sizes (number of digits)
n_values = np.linspace(1, 1000, 1000)

# Define time complexity functions
grade_school_time = n_values**2          # O(n^2)
karatsuba_time = n_values**(np.log2(3))  # O(n^log2(3))

# Plotting the time complexity functions
plt.figure(figsize=(10, 6))

plt.plot(n_values, grade_school_time, label="Grade School (O(n^2))", color='green')
plt.plot(n_values, karatsuba_time, label="Karatsuba (O(n^log2(3)))", color='red')

plt.xlabel('Input Size (Number of Digits)')
plt.ylabel('Time Complexity (arbitrary units)')
plt.title('Time Complexity Comparison of Multiplication Algorithms')
plt.legend()

plt.grid(True)
plt.tight_layout()
plt.show()
