import day1

def test_task1_1(x=None):
    if x is None:
        x = [199, 200, 208, 210, 200, 207, 240,269,260,263]
    
    assert day1.task1_1(x) == 7