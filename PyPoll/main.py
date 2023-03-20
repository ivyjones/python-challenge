import os
import csv

election_data = os.path.join(".", "Resources", "election_data.csv")

#declare variables
candidate_list=[]
votes_per_candidate =[]
votes=[]
percentage=[]

#open csv file
with open(election_data) as csvfile:
    csvreader=csv.reader(csvfile, delimiter=",")
    
    #skip header
    csv_reader=next(csvreader)
    #total votes cast
    data=list(csvreader)
    total_votes=len(data)

    #read through every row after header
    for i in range (0, total_votes):
        candidate=data[i][2]
        votes_per_candidate.append(candidate)
        #find candidates
        if candidate not in candidate_list :
            candidate_list.append(candidate)
    count_of_candidates=len(candidate_list)       

    #The percentage/total of votes each candidate had
    for j in range (0,count_of_candidates):
        name=candidate_list[j]
        votes.append(votes_per_candidate.count(name))
        vpcert = votes[j]/total_votes
        percentage.append(vpcert)
    
    #Winner
    winner=votes.index(max(votes))
    
    #print statements
    print("Election Results")
    print("-------------------------")
    #total number of months included in the dataset
    print("Total Votes: " + str(total_votes))
    print("-------------------------")  
    #print candidates, percentage, and totals
    for k in range (0,count_of_candidates): 
        print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})")
    #The winner of the election based on popular vote.
    print("Winner: " + candidate_list[winner])
    print("-------------------------")

#export results to analysis folder
f=open("./analysis/pybank_poll.txt", "w") 
print("Election Results", file=f)
print("-------------------------", file=f)
#total number of months included in the dataset
print("Total Votes: " + str(total_votes), file=f)
print("-------------------------", file=f)  
#print candidates, percentage, and totals
for k in range (0,count_of_candidates): 
    print(f"{candidate_list[k]}: {percentage[k]:.3%} ({votes[k]:,})", file=f)
#The winner of the election based on popular vote.
print("Winner: " + candidate_list[winner], file=f)
print("-------------------------", file=f)
f.close()

