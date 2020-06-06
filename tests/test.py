import pytest
import pybind_example.compute as m

class TestCompute:
    def test_version(self):
        assert m.__version__ == '0.0.1'
    def test_add(self):
        assert m.add(1, 2) == 3

    def test_subtract(self):
        assert m.subtract(1, 2) == -1
