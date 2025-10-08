import load_csv
from calculation_function_1 import profit_margin_of_category, most_profitable_subcategory_in_category
from calculation_function_2 import avg_discount_rate, calc_average_sales
import get_function

def main():
    category_dict = load_csv.get_dict('SampleSuperstore.csv')
    total_sales_dict = get_function.get_total_sales_discount_profits(category_dict)
    total_entries_dict = get_function.get_total_entires(category_dict)

    # Call problem 1
    problem_1 = profit_margin_of_category(total_sales_dict, "Technology")

    # Call problem 2
    problem_2 = most_profitable_subcategory_in_category(category_dict, "Technology")

    # Call problem 3
    problem_3 = avg_discount_rate(total_sales_dict, total_entries_dict, "Technology")

    # Call problem 4
    problem_4 = calc_average_sales(total_sales_dict, total_entries_dict, "Technology")

    with open("output.txt", "w") as file:
        file.write("=== Analysis Results ===\n\n")
        file.write(f"1. Profit margin of Technology: {problem_1}\n")
        file.write(f"2. Most profitable subcategory in Technology: {problem_2}\n")
        file.write(f"4. Average sales in Technology: {problem_4}\n")
        file.write(f"3. Average discount rate in Technology: {problem_3}\n")


    print("Results have been written to 'output.txt'")

main()