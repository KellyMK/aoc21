import day2


def test_day2a(start = None):
    if start is None:
        start = [0, 0]
    
    dirs = ["forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"]
    
    horiz = 15
    vert = 10
    prod = 150
    
    assert day2.day2a(dirs, start) == [horiz, vert, prod]


def test_day2b(start = None):
    
    dirs = ["forward 5",
            "down 5",
            "forward 8",
            "up 3",
            "down 8",
            "forward 2"]
    
    horiz = 15
    vert = 60
    aim = 10
    prod = 900
    
    assert day2.day2b(dirs, start) == [horiz, vert, aim, prod]