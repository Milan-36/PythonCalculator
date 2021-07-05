import unittest
from Calculator import Calculator
from CsvReader import CsvReader
# from pprint import pprint


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        # fetch the data from csv and place in test_addition_data
        test_addition_data = CsvReader('/src/csv/Unit_Test_Addition.csv').data
        for row in test_addition_data:
            self.assertEqual(self.calculator.add(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_subtract_method_calculator(self):
        test_subtraction_data = CsvReader('/src/csv/Unit_Test_Subtraction.csv').data
        for row in test_subtraction_data:
            self.assertEqual(self.calculator.subtract(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_multiple_method_calculator(self):
        test_multiplication_data = CsvReader('/src/csv/Unit_Test_Multiplication.csv').data
        for row in test_multiplication_data:
            self.assertEqual(self.calculator.multiple(row['Value 1'], row['Value 2']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

    def test_divide_method_calculator(self):
        test_division_data = CsvReader('/src/csv/Unit_Test_Division.csv').data
        for row in test_division_data:
            self.assertAlmostEqual(self.calculator.divide(row['Value 1'], row['Value 2']), float(row['Result']))
            self.assertAlmostEqual(self.calculator.result, float(row['Result']))

    def test_square_method_calculator(self):
        test_square_data = CsvReader('/src/csv/Unit_Test_Square.csv').data
        for row in test_square_data:
            self.assertEqual(self.calculator.sq(row['Value 1']), int(row['Result']))
            self.assertEqual(self.calculator.result, int(row['Result']))

if __name__ == '__main__':
    unittest.main()