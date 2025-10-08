import load_csv
from calculation_function_1 import profit_margin_of_category
import get_function

def main():
    data = load_csv.get_dict('SampleSuperstore.csv')
    data = get_function.get_total_sales_discount_profits(data)
    final = profit_margin_of_category(data,"Technology")
    print(final)

    

main()