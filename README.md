# Universal Basic Income (UBI) Simulation

This repository contains code for simulating the effect of Universal Basic Income (UBI) on a population's savings and consumption behavior.

## Overview

The simulation is implemented in Python using NumPy, pandas, and Matplotlib libraries. It models a population of individuals receiving UBI and examines how it impacts their savings and consumption patterns.

## Parameters

The following parameters can be adjusted to customize the simulation:

- `population_size`: Size of the population.
- `ubi_amount`: Amount of UBI received per individual.
- `initial_savings_mean`: Mean initial savings in dollars.
- `initial_savings_std`: Standard deviation of initial savings.
- `savings_rate`: Proportion of UBI that is saved.
- `consumption_rate`: Proportion of UBI that is consumed.

## Simulation Process

1. **Simulate Initial Savings**: Generate initial savings for each individual in the population based on a normal distribution.
2. **DataFrame Creation**: Create a DataFrame to store simulation data, including individual IDs, initial savings, UBI received, and placeholders for savings and consumption after UBI.
3. **Simulation Function**: Define a function to simulate the effect of UBI on savings and consumption, updating the DataFrame accordingly.
4. **Run Simulation**: Execute the simulation with the specified parameters.
5. **Output**: Display the first few rows of the simulation data.
6. **Visualizations**: Plot histograms and scatter plots to visualize the distribution of savings after UBI and the relationship between initial savings and savings after UBI.

## Usage

To run the simulation with default parameters, simply execute the Python script. You can also modify the parameters according to your preferences.

```bash
python ubi_simulation.py
```

## Dependencies
- NumPy
- pandas
- Matplotlib

## License

This project is licensed under the MIT License. You can find the details in the [LICENSE](LICENSE) file.
