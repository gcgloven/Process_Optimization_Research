import numpy as np
import matplotlib.pyplot as plt

# Parameters for the exponential distribution: lambda (rate)
lambda_rate = 1.5  # Arbitrary rate chosen for demonstration

# Generate exponential distribution data
t = np.linspace(0, 5, 1000)
print (t)
pdf = lambda_rate * np.exp(-lambda_rate * t)

# Plotting the PDF of the exponential distribution
plt.figure(figsize=(10, 6))
plt.plot(t, pdf, label=f'λ = {lambda_rate}')
plt.title('Probability Density Function of Exponential Distribution')
plt.xlabel('Time')
plt.ylabel('Probability Density')
plt.legend()
plt.grid(True)
plt.show()
