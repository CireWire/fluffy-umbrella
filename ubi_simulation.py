import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

# Parameters
population_size = 1000  # Size of the population
ubi_amount = 1000  # UBI amount per individual
initial_savings_mean = 5000  # Mean initial savings in dollars
initial_savings_std = 1500  # Standard deviation of initial savings
savings_rate = 0.25  # Proportion of UBI that is saved
consumption_rate = 0.75  # Proportion of UBI that is consumed

# Simulate initial savings for the population
np.random.seed(0)  # For reproducibility
initial_savings = np.random.normal(initial_savings_mean, initial_savings_std, population_size)

# DataFrame to hold simulation data
population_data = pd.DataFrame({
    'individual_id': range(population_size),
    'initial_savings': initial_savings,
    'ubi_received': np.full(population_size, ubi_amount),
    'savings_after_ubi': np.zeros(population_size),
    'consumption_after_ubi': np.zeros(population_size)
})

# Function to simulate the effect of UBI on savings and consumption
def simulate_ubi_effects(data, savings_rate, consumption_rate):
    data['savings_after_ubi'] = data['initial_savings'] + data['ubi_received'] * savings_rate
    data['consumption_after_ubi'] = data['ubi_received'] * consumption_rate
    return data

# Run the simulation
population_data = simulate_ubi_effects(population_data, savings_rate, consumption_rate)

# Output the first few rows of the simulation data
print(population_data.head())

# Plotting the histogram of savings after UBI
plt.figure(figsize=(10, 5))
plt.hist(population_data['savings_after_ubi'], bins=30, color='skyblue', edgecolor='black')
plt.title('Histogram of Savings After UBI')
plt.xlabel('Savings Amount')
plt.ylabel('Frequency')
plt.grid(True)
plt.show()

# Plotting the scatter plot of initial savings vs. savings after UBI
plt.figure(figsize=(10, 5))
plt.scatter(population_data['initial_savings'], population_data['savings_after_ubi'], alpha=0.5)
plt.title('Initial Savings vs. Savings After UBI')
plt.xlabel('Initial Savings')
plt.ylabel('Savings After UBI')
plt.grid(True)
plt.show()
