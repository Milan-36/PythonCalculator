import unittest
from Calculator import Calculator
from CsvReader import CsvReader
from pprint import pprint
from StaticVariables import StaticVariables


class MyTestCase(unittest.TestCase):
    def setUp(self) -> None:
        self.calculator = Calculator()

    def test_instantiate_calculator(self):
        self.assertIsInstance(self.calculator, Calculator)

    def test_results_property_calculator(self):
        self.assertEqual(self.calculator.result, 0)

    def test_add_method_calculator(self):
        # fetch the data from csv and place in test_addition_data
        test_addition_data = CsvReader(StaticVariables.Addition_csv).data
        for row in test_addition_data:
            self.assertEqual(self.calculator.add(row[StaticVariables.val1], row[StaticVariables.val2]), int(row[StaticVariables.result]))
            self.assertEqual(self.calculator.result, int(row[StaticVariables.result]))

    def test_subtract_method_calculator(self):
        test_subtraction_data = CsvReader('/src/csv/Unit_Test_Subtraction.csv').data
        for row in test_subtraction_data:
            self.assertEqual(self.calculator.subtract(row[StaticVariables.val1], row[StaticVariables.val2]), int(row[StaticVariables.result]))
            self.assertEqual(self.calculator.result, int(row[StaticVariables.result]))

    def test_multiple_method_calculator(self):
        test_multiplication_data = CsvReader('/src/csv/Unit_Test_Multiplication.csv').data
        for row in test_multiplication_data:
            self.assertEqual(self.calculator.multiple(row[StaticVariables.val1], row[StaticVariables.val2]), int(row[StaticVariables.result]))
            self.assertEqual(self.calculator.result, int(row[StaticVariables.result]))

    def test_divide_method_calculator(self):
        test_division_data = CsvReader('/src/csv/Unit_Test_Division.csv').data
        for row in test_division_data:
            self.assertAlmostEqual(self.calculator.divide(row[StaticVariables.val1], row[StaticVariables.val2]), float(row[StaticVariables.result]))
            self.assertAlmostEqual(self.calculator.result, float(row[StaticVariables.result]))

    def test_square_method_calculator(self):
        test_square_data = CsvReader('/src/csv/Unit_Test_Square.csv').data
        for row in test_square_data:
            self.assertEqual(self.calculator.sq(row[StaticVariables.val1]), int(row[StaticVariables.result]))
            self.assertEqual(self.calculator.result, int(row[StaticVariables.result]))

    def test_square_root_method_calculator(self):
        test_square_root_data = CsvReader('/src/csv/Unit_Test_Square_Root.csv').data
        for row in test_square_root_data:
            self.assertAlmostEqual(self.calculator.sqrt(row[StaticVariables.val1]), float(row[StaticVariables.result]))
            self.assertAlmostEqual(self.calculator.result, float(row[StaticVariables.result]))

if __name__ == '__main__':
    unittest.main()