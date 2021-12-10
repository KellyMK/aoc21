import day3 

def test_day3a():
    report = ["00100",
"11110",
"10110",
"10111",
"10101",
"01111",
"00111",
"11100",
"10000",
"11001",
"00010",
"01010"]
    
    gamma_bin = "10110"
    gamma_dec = 22
    
    eps_bin = "01001"
    eps_dec = 9
    
    assert day3.day3a(report) == gamma_dec * eps_dec