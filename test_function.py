# Course: SI 201
# Assignment: Project 1
# Team members: Xiwen Mark, Chih-Hsiang Chang
# Gen AI: Used to understand concepts and fix some code structures


import unittest
from calculation_function_1 import profit_margin_of_category, most_profitable_subcategory_in_category
from calculation_function_2 import calc_average_sales, avg_discount_rate

class TestCalculationFunctions(unittest.TestCase):
    #profit_margin
    def test_profit_margin_general_1(self):
        data = {"Technology": {"Phones": [100.0, 10.0, 20.0], "Laptops": [200.0, 5.0, 40.0]}}
        result = profit_margin_of_category(data, "Technology")
        self.assertEqual(result, 20)

    def test_profit_margin_general_2(self):
        data = {"Technology": {"Tablets": [150.0, 0.0, 30.0]}}
        result = profit_margin_of_category(data, "Technology")
        self.assertEqual(result, 20)

    def test_profit_margin_edge_zero_sales(self):
        data = {"Technology": {"Cables": [0.0, 0.0, 10.0]}}
        result = profit_margin_of_category(data, "Technology")
        self.assertEqual(result, 0)  

    def test_profit_margin_edge_missing_category(self):
        data = {"Furniture": {"Chairs": [100.0, 5.0, 10.0]}}
        result = profit_margin_of_category(data, "Technology")
        self.assertIsNone(result)

    #most_profitable

    def test_most_profitable_general_1(self):
        data = {
            "Technology": {
                "Phones": [[20.0, 100.0, 5.0], [10.0, 50.0, 0.0]],
                "Laptops": [[40.0, 200.0, 0.0]]
            }
        }
        result = most_profitable_subcategory_in_category(data, "Technology")
        self.assertEqual(result, "Laptops")  

    def test_most_profitable_general_2(self):
        data = {"Technology": {"Accessories": [15.0, 50.0, 0.0], "Tablets": [30.0, 80.0, 0.0]}}
        result = most_profitable_subcategory_in_category(data, "Technology")
        self.assertEqual(result, "Tablets")

    def test_most_profitable_edge_tie(self):
        data = {"Technology": {"A": [[10.0, 1.0, 0.0]], "B": [[10.0, 1.0, 0.0]]}}
        result = most_profitable_subcategory_in_category(data, "Technology")
        self.assertEqual(result, "A") 

    def test_most_profitable_edge_missing_category(self):
        data = {"Furniture": {"Chairs": [[10.0, 1.0, 0.0]]}}
        result = most_profitable_subcategory_in_category(data, "Technology")
        self.assertIsNone(result)

class TestCalculationFunction2(unittest.TestCase):
    #calc_average_sales 

    def test_calc_avg_sales_general_1(self):
        cat_total = {
            "Technology": {
                "Phones":  [100.0, 10.0, 20.0],
                "Laptops": [200.0, 5.0, 40.0],
            }
        }
        entries = {"Technology": 4}
        result = calc_average_sales(cat_total, entries, "Technology")
        self.assertEqual(result, 75.0)

    def test_calc_avg_sales_general_2(self):
        cat_total = {"Technology": {"Tablets": [150.0, 0.0, 30.0]}}
        entries = {"Technology": 3}
        result = calc_average_sales(cat_total, entries, "Technology")
        self.assertEqual(result, 50.0)

    def test_calc_avg_sales_edge_zero_sales(self):
        cat_total = {"Technology": {"Cables": [0.0, 0.0, 10.0]}}
        entries = {"Technology": 2}
        result = calc_average_sales(cat_total, entries, "Technology")
        self.assertEqual(result, 0.0)

    def test_calc_avg_sales_edge_rounding(self):
        cat_total = {"Technology": {"A": [100.0, 0.0, 0.0], "B": [70.0, 0.0, 0.0]}}
        entries = {"Technology": 3}
        result = calc_average_sales(cat_total, entries, "Technology")
        self.assertEqual(result, 56.67)

    # avg_discount_rate

    def test_avg_discount_rate_general_1(self):
        cat_total = {
            "Technology": {
                "Phones":  [100.0, 10.0, 20.0],
                "Laptops": [200.0, 5.0, 40.0],
            }
        }
        entries = {"Technology": 4}
        result = avg_discount_rate(cat_total, entries, "Technology")
        self.assertEqual(result, 3.75)

    def test_avg_discount_rate_general_2(self):
        cat_total = {"Technology": {"Tablets": [30.0, 80.0, 0.0]}}
        entries = {"Technology": 3}
        result = avg_discount_rate(cat_total, entries, "Technology")
        self.assertEqual(result, 26.67)

    def test_avg_discount_rate_edge_zero_discount(self):
        cat_total = {"Technology": {"Cables": [40.0, 0.0, 10.0]}}
        entries = {"Technology": 2}
        result = avg_discount_rate(cat_total, entries, "Technology")
        self.assertEqual(result, 0.0)

    def test_avg_discount_rate_edge_rounding(self):
        cat_total = {"Technology": {"A": [10.0, 1.0, 0.0], "B": [10.0, 1.0, 0.0]}}
        entries = {"Technology": 3}
        result = avg_discount_rate(cat_total, entries, "Technology")
        self.assertEqual(result, 0.67)


if __name__ == "__main__":
    unittest.main()
