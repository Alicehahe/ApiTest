import pytest

from python.cal import Cal


class Testcal(object):

    def setup(self):
        self.cal = Cal()

    def test_add_01(self):
        result = self.cal.add(3,4)
        assert 7 == result

    def test_minus_01(self):
        result = self.cal.minus(-1,0)
        assert -1 == result

    def test_div_01(self):
        result = self.cal.div(-1,0)
        assert "divdend can't be 0" == result


    def test_mul_01(self):
        result = self.cal.mul(10,0)
        assert 0 == result







# pytest.main(['-vs'])
# pytest.main(['-vk','add'])