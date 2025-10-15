# Course: SI 201
# Assignment: Project 1
# Team members: Xiwen Mark, Chih-Hsiang Chang
# Gen AI: Used to understand concepts and fix some code structures
# Problems 1 and 2 written by Chih-Hsiang Chang, Problems 3 and 4 written by Xiwen Mark

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

        in_d_list = [sales, discount, profit]

        if category not in out_d:
            out_d[category] = {}

        if subcat not in out_d[category]:
            out_d[category][subcat] = []

        out_d[category][subcat].append(in_d_list)
        

    inFile.close()
    return out_d