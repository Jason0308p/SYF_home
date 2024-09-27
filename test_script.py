# test_script.py

import script

def test_add():
    assert script.add(1, 2) == 3, "Test failed: 5 + 3 should equal 8"
    assert script.add(-1, 1) == 0, "Test failed: -1 + 1 should equal 0"
    print("All tests passed!")

if __name__ == "__main__":
    test_add()