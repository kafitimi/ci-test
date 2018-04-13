import unittest
from cplx import *

class TestCplxMethods(unittest.TestCase):
    
	def test_r(self):
		m = Cplx(1,1)
		self.assertTrue(abs(m.r() - 2**0.5) < 0.0000001)

	def test_arg(self):
		z = Cplx(1,1)
		self.assertTrue(z.arg() == 0.7853981633974483)
		print("end of testing")


if __name__ == '__main__':
	unittest.main()