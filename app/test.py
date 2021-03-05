import unittest
from convert import CidrMaskConvert, IpValidate

class TestStringMethods(unittest.TestCase):
  def setUp(self):
      self.convert = CidrMaskConvert()
      self.validate = IpValidate()

  def test_valid_cidr_to_mask(self):
      self.assertEqual('128.0.0.0', self.convert.cidr_to_mask('1'))

if __name__ == '__main__':
   unittest.main()
