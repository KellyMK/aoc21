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
    # Joe's solution: 
    # diffs = x[1:] - x[0:-1]
    # increases = sum(diffs > 0)
    
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
    # Joe's solution:
    # rolling_sum = x[:-2] + x[1:-1] + x[2:]
    
    return task1_1(rolling_sum)

## Get Answer for Task 1.1

day1_input_file = open("aoc-input/day1_input.txt", "r")
day1_input = [int(i) for i in day1_input_file.readlines()]

print("Task 1.1")
print(task1_1(day1_input))


## Get Answer for Task 1.2

print("Task 1.2")
print(task1_2(day1_input))
