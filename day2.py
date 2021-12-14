import numpy as np
import requests

def day2a(dirs, start=None):
    """Update the horizontal position and depth

    Args:
        dirs (character list or generator): List of character strings of the form "forward/up/down int"
        start (int, optional): 2-dimensional starting point, where the first
        component represents horizontal distance and the second represents depth.
        Defaults to becomes [0,0].
        
    Returns:
        List containing the final position (horizontal, depth), and the product
    """
    
    if start is None:
        start = [0, 0]
    
    start.append(0)
    
    for dir in dirs:
        comp = dir.split()
        
        if "forward" in comp[0]:
            start[0] += int(comp[1])
        elif "up" in comp[0]:
            start[1] -= int(comp[1])
        else:
            start[1] += int(comp[1])
    
    start[2] = np.prod(start[:-1])
    
    return start



def day2b(dirs, start=None):
    """Update the horizontal position and depth

    Args:
        dirs (character list or generator): List of character strings of the form "forward/up/down int"
        start (int, optional): 2-dimensional starting point, where the first
        component represents horizontal distance and the second represents depth.
        Defaults to becomes [0,0].
        
    Returns:
        List containing the final position (horizontal, depth), and the product
    """
    
    if start is None:
        start = [0, 0, 0]
    
    
    for dir in dirs:
        comp = dir.split()
        
        if "forward" in comp[0]:
            start[0] += int(comp[1])
            start[1] += start[2]*int(comp[1])
        elif "up" in comp[0]:
            start[2] -= int(comp[1])
        else:
            start[2] += int(comp[1])
    
    start.append(np.prod(start[:-1]))
    
    return start



## Get Answer for Task 2.1
day2_input_file = open("aoc-input/day2_input.txt", "r")
day2_input = day2_input_file.readlines()

print("Task 2.1")
print(day2a(day2_input))


## Get Answer for Task 2.2

print("Task 2.2")
print(day2b(day2_input))
