import csv

def get_dict(file):

    out_d = {}
    in_d = {}

    # get the file handler
    inFile = open(file)
    csvFile = csv.reader(inFile)

    # read the header row
    headers = next(csvFile)

    # read the rest of the lines from the file handler
    for row in csvFile:

        category = row[7]
        subcat = row[8]
        sales = float(row[9])
        discount = float(row[11])
        profit = float(row[12])

        
        in_d[subcat] = [sales, discount, profit]

        out_d[category] = in_d

    inFile.close()
    return out_d