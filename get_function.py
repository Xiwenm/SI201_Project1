# Course: SI 201
# Assignment: Project 1
# Team members: Xiwen Mark, Chih-Hsiang Chang
# Gen AI: Used to understand concepts and fix some code structures
# Problems 1 and 2 written by Chih-Hsiang Chang, Problems 3 and 4 written by Xiwen Mark

def get_total_sales_discount_profits(cat_dict):
    """
    Creates a dictionary containing all categories with their total sales, total profit, and total discount

    Input: cat_dict (list of dictionaries)
    Output: total(dictionary)

    """
    out_d = {}
    
    for category, subcats in cat_dict.items():
        for subcat, values in subcats.items():
            total_sales = 0
            total_discount = 0
            total_profit = 0

            for entry in values:
                total_sales += entry[0]
                total_discount += entry[1]
                total_profit += entry[2]

            totals = [round(total_sales, 2), round(total_discount, 2), round(total_profit, 2)]

            if category not in out_d:
                out_d[category] = {}

            out_d[category][subcat] = totals

    return out_d

def get_total_entires(cat_dict):
    """
    Takes a dictionary, then count the number of entries in that dictionary, then return the total entries
    Input: cat_dict (list of dictionaries)
    Output: total (dictionary)

    """
    out_d = {}
    
    for category, subcats in cat_dict.items():
        total_entries = 0
        for subcat, values in subcats.items():
            total_entries += len(values)  
        out_d[category] = total_entries 

    return out_d