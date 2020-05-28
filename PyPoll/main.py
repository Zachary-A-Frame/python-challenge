import os
import csv

election_csv = os.path.join("./", "Resources", "election_data.csv")
# output_path = os.path.join("./", "analysis", "analysis.csv")

with open(election_csv, 'r') as csvfile:

    # Split the data on commas
    csvreader = csv.reader(csvfile, delimiter=',')

    totalVotes = 0    
    
    khanVotes = 0
    correyVotes = 0
    liVotes = 0
    tooleyVotes = 0

    # Loop through the data, after the first row, of course.
    next(csvreader)
    for row in csvreader:
        
        # What we're doing is really simple, we're checking if row[0] exists and adding 1 to our count.
        # In other words we're implictly using a boolean statement. 
        if row[0]:
            totalVotes = totalVotes + 1
            
        if row[2] == "Khan":
            khanVotes = khanVotes + 1
        elif row[2] == "Correy":
            correyVotes = correyVotes + 1
        elif row[2] == 'Li':
            liVotes = liVotes + 1
        else:
            tooleyVotes = tooleyVotes + 1
        
        khanPercent = int(khanVotes / totalVotes * 100)
        correyPercent = int(correyVotes / totalVotes * 100)
        liPercent = int(liVotes / totalVotes * 100)
        tooleyPercent = int(tooleyVotes / totalVotes * 100)
        
        winner = "Khan"
        
        
        
        
        
    print("Election Results")
    print("----------------------------------------------------------------")
    print("This is how many total votes there are: " + str(totalVotes))
    print("----------------------------------------------------------------")
    print("Khan: "  + str(khanPercent) + "% " + "(" + str(khanVotes) + ")")
    print("Correy: "  + str(correyPercent) + "% " + "(" + str(correyVotes) + ")")
    print("Li: "  + str(liPercent) + "% " + "(" + str(liVotes) + ")")
    print("Tooley: "  + str(tooleyPercent) + "% " + "(" + str(tooleyVotes) + ")")
    print("----------------------------------------------------------------")
    print("WINNER: " + winner)


        
        
            
        # Here we're calculating our net total.
        #if row[1]:
        #    netTotal = netTotal + int(row[1])
        
       # if int(row[1]) < smallest:
        #    smallest = int(row[1])
        #    smallestDate = str(row[0])
        
       # if int(row[1]) > largest:
       #     largest = int(row[1])
       #     largestDate = str(row[0])
    
        #minnum = min([row for value in csvreader])
        # Smallest number in a column.
        
    #average = int(netTotal/totalRows)

    #with open(output_path, 'w') as csvfile:
    #    csvwriter = csv.writer(csvfile, delimiter=',')
        
   #    csvwriter.writerow(['Total Months','Total', 'Average Change', 'Greatest Increase in profits', 'Greatest Decrease in profits'])
   #     csvwriter.writerow([totalRows, netTotal, average, largestDate + ':' + str(largest), smallestDate + str(smallest)])
        

    # Python is indent-sensitive; this code executes after our for loop and if statement.    
   # print("Financial Analysis")
   # print("---------------------------------------------------------")
        
   # print("Total Months: " + str(totalRows))
   # print("Net profits / losses: " + str(netTotal))
    #print("Average Change: " + str(average))

    #print("Greatest Increase in Profits: " + " " + largestDate + " ($" + str(largest) + ")")
    #print("Greatest Decrease in Profits: " + " " + smallestDate + " ($" + str(smallest) + ")")


