import day7 

crabs = "16,1,2,0,4,2,7,1,2,14"

def test_day7a_pos():
    end_position = 2
    assert day7.pos7a(crabs) == end_position

def test_day7a_cost_2():
    total_cost = 37
    end_position = 2
    assert day7.cost7a(crabs, end_position) == total_cost
    
def test_day7a_cost_1():
    total_cost = 41
    end_position = 1
    assert day7.cost7a(crabs, end_position) == total_cost
    
def test_day7a_cost_3():
    total_cost = 39
    end_position = 3
    assert day7.cost7a(crabs, end_position) == total_cost
    
def test_day7a_cost_10():
    total_cost = 71
    end_position = 10
    assert day7.cost7a(crabs, end_position) == total_cost