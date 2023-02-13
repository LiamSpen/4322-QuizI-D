'''
Due the outstanding performance of the Customer Service Represetatives (CSRs) in the marketing department, management
has decided to reward them with a 10% increase in their salary. To evaluate the impact on the budget, you have been
asked to run a report on the employee file and display the results of BEFORE AND AFTER the salary increase.

You will create a dictionary that has the full employee name as the key and ONLY their new salary as the value.

Iternate through the dictionary to print out their name and thier new salary (as in image)
'''

import csv

# open the file

infile = open("employee_data.csv", "r")
infile = csv.reader(infile)


# create an empty dictionary

dict = {}
print()

# use a loop to iterate through the csv file

for i in infile:
    if i[3] == "Marketing":
        if i[4] == "CSR":
            new = int(i[5])*1.1
            new = format(new, ",.2f")
            dict[f"{i[1]} {i[2]}"] = new
            print(
                f"Manager Name: {i[1]} {i[2]} Current Salary: ${format(float(i[5]), ',.2f')}")

# check if the employee fits the search criteria


print()
print('=========================================')
print()

# iternate through the dictionary and print out the key and value as per printout

for i in dict:
    print(f"Manager Name: {i} New salary: ${dict[i]}")
print()
