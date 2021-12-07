def task1_1(x):
    """Day 1, Task 1:
    
    Count number of increases in numeric input list.
    https://adventofcode.com/2021/day/1

    Args:
        x (numeric): List of depths
    
    Returns:
        Number of times the values in x increase
    """
    
    n_vals = len(x)
    increases = [1 if x[i] - x[i-1] > 0 else 0 for i in range(1, n_vals)]
    
    return sum(increases)


def task1_2(x):
    """Day 1, Task 2:
    
    Count number of increases in 3-day rolling average of numeric input list.
    https://adventofcode.com/2021/day/1
    

    Args:
        x (numeric): List of depths
    
    Returns:
        Number of times the values in x increases for three-day rolling average
    """
    
    n_vals = len(x)
    rolling_sum = [sum(x[i:i+3]) for i in range(n_vals-2)]
    n_sums = len(rolling_sum)
    increases = [1 if rolling_sum[i] - rolling_sum[i-1] > 0 else 0 for i in range(1, n_sums)]
    
    return sum(increases)

## Get Answer for Task 1.1

day1a_input_file = open("aoc-input/day1_input.txt", "r")
day1a_input = [int(i) for i in day1a_input_file.readlines()]

print("Task 1.1")
print(task1_1(day1a_input))


## Get Answer for Task 1.2

day1b_input_file = open("aoc-input/day1_input.txt", "r")
day1b_input = [int(i) for i in day1b_input_file.readlines()]

print("Task 1.2")
print(task1_2(day1b_input))
