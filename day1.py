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

day1_input_file = open("aoc-answers/day1_input.txt", "r")
day1_input = [int(i) for i in day1_input_file.readlines()]

print(task1_1(day1_input))
