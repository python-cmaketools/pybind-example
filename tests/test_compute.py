import pybind_example.compute as m

def test_version(): # version of the PYD file
    assert m.__version__ == 'dev' or m.__version__ == '0.1.0'
def test_add():
    assert m.add(1, 2) == 3

def test_subtract():
    assert m.subtract(1, 2) == -1
