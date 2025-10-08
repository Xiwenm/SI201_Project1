

#Problem 1 - What is the profit margin of Technology?
def profit_margin_of_category(cat_dict, category):
    if category not in cat_dict:
        return None
    
    subcats = cat_dict[category]
    total_profit = 0
    total_sales = 0 

    for key, value in cat_dict[category].items():
        profit = value[2]
        sales = value[0]

        total_profit += profit
        total_sales += sales
    if total_sales == 0:
        return 0
    
    profit_margin = (total_profit / total_sales) * 100
    
    finald = {}
    finald[category] = profit_margin

    return finald
    


#Problem 2 What is the most profitable subcategory in Technology?

def most_profitable_subcategory_in_category(cat_dict, category):
    if category not in cat_dict:
        return None
    subcats = cat_dict[category]

    bestsubcat = None
    max_prof = -999999

    for name in subcats:
        records = subcats[name]
        total_profit = 0

        if isinstance(records[0],list):
            for record in records:
                profit = record[0]
                total_profit += profit
        else:
            profit = records[0]
            total_profit += profit

        if total_profit > max_prof:
            max_prof = total_profit
            bestsubcat = name
    return bestsubcat
