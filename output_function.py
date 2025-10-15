# Course: SI 201
# Assignment: Project 1
# Team members: Xiwen Mark, Chih-Hsiang Chang
# Gen AI: Used to understand concepts and fix some code structures
# Problems 1 and 2 written by Chih-Hsiang Chang, Problems 3 and 4 written by Xiwen Mark


def output_function(problem_1, problem_2, problem_3, problem_4):
    with open("output.txt", "w") as file:
            file.write("=== Analysis Results ===\n\n")
            file.write(f"1. Profit margin of Technology: {problem_1}\n")
            file.write(f"2. Most profitable subcategory in Technology: {problem_2}\n")
            file.write(f"4. Average sales in Technology: {problem_4}\n")
            file.write(f"3. Average discount rate in Technology: {problem_3}\n")


    print("Results have been written to 'output.txt'")