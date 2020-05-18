# PyBank 

### Must be able to do the following

### Calculate: The total number of months included in the dataset
### Net total amount of profit / losses over entire period
### Average of changes in Profit/Losses over the entire period 
### The greatest increase in profits (date and amount) over the entire period
### The greatest decerease in losses (date and amount) over the entire period.


import os
import csv

budget_csv = os.path.join("./", "Resources", "budget.csv")

with open(budget_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')
    
    totalRows = 0
    netTotal = 0
    average = 0
    
    largest = 0
    largestDate = ""
    
    smallest = 0
    smallestDate = ""
    
    # Loop through the data, after the first row, of course.
    next(csvreader)
    for row in csvreader:
        
        # What we're doing is really simple, we're checking if row[0] exists and adding 1 to our count.
        # In other words we're implictly using a boolean statement. 
        if row[0]:
            totalRows = totalRows + 1
            
        # Here we're calculating our net total.
        if row[1]:
            netTotal = netTotal + int(row[1])
        
        if int(row[1]) < smallest:
            smallest = int(row[1])
            smallestDate = str(row[0])
        
        if int(row[1]) > largest:
            largest = int(row[1])
            largestDate = str(row[0])
    
        #minnum = min([row for value in csvreader])
        # Smallest number in a column.
        
    average = int(netTotal/totalRows)


    # Python is indent-sensitive; this code executes after our for loop and if statement.    
    print("Financial Analysis")
    print("---------------------------------------------------------")
        
    print("Total Months: " + str(totalRows))
    print("Net profits / losses: " + str(netTotal))
    print("Average Change: " + str(average))

    print("Greatest Increase in Profits: " + " " + largestDate + " ($" + str(largest) + ")")
    print("Greatest Decrease in Profits: " + " " + smallestDate + " ($" + str(smallest) + ")")

