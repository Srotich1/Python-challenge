#Import and read Pybank data file to include header row
import os
import csv

#Path to CSV file
csvpath = os.path.join('..', 'PYTHON', 'budget.csv')

#variables for Pybank csvfile
total_months = 0
total_pl = 0
value = 0
change = 0
dates = []
profits = []

#Open csv file data then reading the CSV file
with open('budget.csv', newline = "") as csvfile:
    csvreader = csv.reader(csvfile, delimiter = ",")
    csv_header = next(csvreader)
    first_row = next(csvreader)
    
#the first task is calculate the total number of rows which is in turn gives us the total number of months
    total_months += 1
    total_pl += int(first_row[1])
    value = int(first_row[1])
    
#Going through each row of data after the header & first row 
    for row in csvreader:
        dates.append(row[0])
        
#the next tasks is to calculate the change in net and its total net amount of "Profit/Losses over entire period
# To find change over entire period individual month to month change has to be factored in.
#The true change is the difference between current and previous, for this data value will represent that change.
        change = int(row[1])-value
        profits.append(change)
        value = int(row[1])
        total_months += 1

        total_pl = total_pl + int(row[1])

#Next on the task is calculating the greatest increase in profits (date and amount) over the entire period
    greatest_increase = max(profits)
    greatest_index = profits.index(greatest_increase)
    greatest_date = dates[greatest_index]

#Lastly,calculate the greatest decrease in profits (date and amount) over the entire period 
    greatest_decrease = min(profits)
    bad_index = profits.index(greatest_decrease)
    bad_date = dates[bad_index]

#With the total net calculated the Average change therefore is the sum of its profit over the total number.
    avg_change = sum(profits)/len(profits)
    

#Displaying information
print("Financial Analysis")
print("---------------------")
print(f"Total Months: {str(total_months)}")
print(f"Total: ${str(total_pl)}")
print(f"Average Change: ${str(round(avg_change,2))}")
print(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
print(f"Greatest Decrease in Profits: {bad_date} (${str(greatest_decrease)})")


#Exporing to .txt file
output = open("output.txt", "w")

line1 = "Financial Analysis"
line2 = "---------------------"
line3 = str(f"Total Months: {str(total_months)}")
line4 = str(f"Total: ${str(total_pl)}")
line5 = str(f"Average Change: ${str(round(avg_change,2))}")
line6 = str(f"Greatest Increase in Profits: {greatest_date} (${str(greatest_increase)})")
line7 = str(f"Greatest Decrease in Profits: {bad_date} (${str(greatest_decrease)})")
output.write('{}\n{}\n{}\n{}\n{}\n{}\n{}\n'.format(line1,line2,line3,line4,line5,line6,line7))
