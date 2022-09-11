import unittest
from project_1 import returnOnInvestment

class testRoi(unittest.TestCase):
    
    def test_income_add(self):
        test_source_income = testRoi()

        test_source_income.add('Interest')
        self.assertIn('Interest', test_source_income)
        self.assertEqual(test_source_income.input['Interest'])



if __name__ == "__main__":
    unittest.main()