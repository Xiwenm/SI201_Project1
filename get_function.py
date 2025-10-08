# Course: SI 201
# Assignment: Project 1
# Team members: Xiwen Mark, Chih-Hsiang Chang 

def get_total_sales_discount_profits(cat_dict):
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
    """
    out_d = {}
    
    for category, subcats in cat_dict.items():
        total_entries = 0
        for subcat, values in subcats.items():
            total_entries += len(values)  
        out_d[category] = total_entries 

    return out_d