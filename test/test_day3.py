import day3
from io import StringIO
import pandas as pd

def test_open(mocker):
    m = mocker.patch('builtins.open', mocker.mock_open(read_data='bibble'))
    with open('foo') as h:
        result = h.read()

    m.assert_called_once_with('foo')
    assert result == 'bibble'




def test_day3a():
    
    test_data = StringIO("""
00100
11110
10110
10111
10101
01111
00111
11100
10000
11001
00010
01010
""")
    
    
    gamma_bin = "10110"
    gamma_dec = 22
    
    eps_bin = "01001"
    eps_dec = 9
    
    print(f"gamma: {gamma_bin}; epsilon: {eps_bin}")

    
    assert day3.day3a(test_data) == gamma_dec * eps_dec
