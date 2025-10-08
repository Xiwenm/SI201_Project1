# Course: SI 201
# Assignment: Project 1
# Team members: Xiwen Mark, Chih-Hsiang Chang 

import load_csv
import get_function

# Problem 3: What is the average sales for Technology?
def calc_average_sales(cat_total_dict, category):
    total_sales = 0
    count = 0
    for key, value in cat_total_dict[category].items():
        total_sales += value[1]
        count += 1
    return round(total_sales/count, 2)


# Problem 4: What is the average discount rate for Technology?
def avg_discount_rate(cat_total_dict, category):
    total_discount = 0
    count = 0
    for key, value in cat_total_dict[category].items():
        total_discount += value[1]
        count += 1
    return round(total_discount/count, 2)

def main():
    data = get_function.get_total_sales_discount_profits(load_csv.get_dict('/Users/xiwenm/Documents/SI201/SI201_Project1/SampleSuperstore.csv'))

    print(avg_discount_rate(data, 'Technology'))

main()