from main import add_two_numbers

def test_main():
    assert add_two_numbers(1, 2) == 1
    assert add_two_numbers(0, -1) == -1
