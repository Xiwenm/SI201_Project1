# Course: SI 201
# Assignment: Project 1
# Team members: Xiwen Mark, Chih-Hsiang Chang
# Gen AI: Used to understand concepts and fix some code structures
 

# Problem 3: What is the average sales for Technology? (Xiwen mark)

def calc_average_sales(cat_total_dict, total_entires_dict, category):
    """
    Calculating average sales of the category given.
    The average sales tell you how much revenue you earn, on average, per order (or entry) in that category.
    """
    total_sales = 0
    for key, value in cat_total_dict[category].items():
        total_sales += value[0]
    return round(total_sales/total_entires_dict[category], 2)


# Problem 4: What is the average discount rate for Technology? (Xiwen Mark)
def avg_discount_rate(cat_total_dict, total_entires_dict, category):
    """
    Calculating average discount rate of the category given
    How much discount, on average, giving each time someone buys something in that category.
    """
    total_discount = 0
    for key, value in cat_total_dict[category].items():
        total_discount += value[1]
    return round(total_discount/total_entires_dict[category], 2)
