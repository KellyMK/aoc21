import day3 

def test_day3a():
    report = day3.read_day3("../aoc-input/day3_test_intput.txt")
    
    gamma_bin = "10110"
    gamma_dec = 22
    
    eps_bin = "01001"
    eps_dec = 9
    
    assert day3.day3a(report) == gamma_dec * eps_dec