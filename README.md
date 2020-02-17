# MonteCarloOR531

This repo presents a python solution to OR531/Module4/Project6 on Monte Carlo Simulation.

## Usage

`python3 run_monte_carlo.py`

## File Structure

- `monte_carlo.py` is a library I built specifically for Project6. It contains all functions needed to execute a simulation of the door-to-door sales campaign problem.
- `params.json` is a configuration file containing all of the probabilities given in the problem, ex: P(someone answers the door).
- `run_monte_carlo.py` reads `params.json`, calls the functions in `monte_carlo.py` to answer the given questions:
	1. Mean amount sold?
	2. Std. Deviation amount sold?
	3. What is the probability of making $750+?
- `answers.png` is a screenshot I took from Spyder after running `run_monte_carlo.py` to get the answers and a histogram of the distribution of amount sold.
- `Trial.csv` shows the results from 1 (of 1,000) simulations. You can look at the aggregate statistics from `Trial.csv` to see that the door is in fact answered ~80% of the time, more often by women.