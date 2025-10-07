import load_csv


#Problem 1 - What is the profit margin of Technology?
def profit_margin_of_technology(categories, category):
    pass

#Problem 2 What is the most profitable subcategory in Technology?

def most_profitable_subcategory_in_technology(cat_dict, category):
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
