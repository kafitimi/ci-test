import unittest
from cplx import *

class TestCplxMethods(unittest.TestCase):
    
	def test_r(self):
		m = Cplx(1,1)
		self.assertTrue(abs(m.r() - 2**0.5) < 0.0000001)

	def test_arg(self):
		z = Cplx(3,5)
		self.assertTrue(z.arg() == 1.0303768265243124)
		
	def test_arg(self):
		z = Cplx(-3,5)
		self.assertTrue(z.arg() == 2.1112158270654807)
		
	def test_arg(self):
		z = Cplx(-3,-5)
		self.assertTrue(z.arg() == -2.1112158270654807)

	def test_arg(self):
		z = Cplx(0,5)
		self.assertTrue(z.arg() == 1.5707963267948966)
		
	def test_arg(self):
		z = Cplx(0,-5)
		self.assertTrue(z.arg() == -1.5707963267948966)
		print("end of testing")


if __name__ == '__main__':
	unittest.main()