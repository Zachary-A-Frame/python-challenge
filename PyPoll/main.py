import os
import csv

election_csv = os.path.join("./", "Resources", "election_data.csv")
output_path = os.path.join("./", "analysis", "analysis.csv")

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
        
        winner = ""
        
        if khanVotes > correyVotes and khanVotes > liVotes and khanVotes > tooleyVotes:
            winner = "Khan"
        elif correyVotes > khanVotes and correyVotes > liVotes and correyVotes > tooleyVotes:
            winner = "Correy"
        elif liVotes > khanVotes and liVotes > correyVotes and liVotes > tooleyVotes:
            winner = "Li"
        else:
            winner = "O'Tooley"
        
        
        
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

    with open(output_path, 'w') as csvfile:
           csvwriter = csv.writer(csvfile, delimiter=',')
            
           csvwriter.writerow(['Total Votes','Khan Votes', 'Khan Percentage Votes', 'Correy Votes', 'Correy Percentage Votes', 'Li Votes',
                               'Li Percentage Votes', "O'Tooley Votes", "O'Tooley Percentage Votes", 'WINNER: ' ])
           csvwriter.writerow([totalVotes, khanVotes, khanPercent, correyVotes, correyPercent, liVotes, liPercent, tooleyVotes, tooleyPercent, winner])
        
        
        
     
