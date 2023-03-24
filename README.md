# python_challenge
PyBank


The first thing that I did was track all the variables that were being asked for in the directions: total months, net amount of profit/losses, greatest increase in profit (date and amount) and greatest decrease in profit (date and amount). I also created two dictionaries for the months adn the profits.

Then, I opened the files and skipped the first header row. I set up the variables so that I could find each of the values I was looking for the analysis. For each row in the file, I appended it to the months dictionary and used that for the Total Months count. In the same for loop, it read through and compared each new value to the previous value and added each difference (change) to the profits dictionary. From there, it was easy to find the maximum profit and minimum profit by using max and min. Lastly, I calculated the average change by averaging all of the values in the profits dictionary together. The outputs display in the terminal as well as in the 'financialanalysis.txt' file.


PyPoll

First, I created the names as a set, candidates as a list and percentages and candidates as a dictionary. Then I opened the csv file and kept track of the votes by reading through the rows and adding each candidate to the list. If the candidate wasn't already on the list, then the name was added by the if function on line 26.

After that, I totaled the votes and found the winner of the election by looking for the max value in the candidate dictionary. I converted the number into a percentage and added the % symbol on line 40. From there, I was able to print the results to the terminal and write the output to a new file titled 'electionresults.txt'.

Sources:
For this assignment, I worked closely with classmates Saroja Shrestha and Taniya Talukdar. I referenced a Git Hub page for the format of the write portion of both projects and the if statement on line 26 of PyPoll. (I have since lost the direct link, apologies.) Additionally, I used the websites Slack Overflow and ChatGBT to check my code syntax and solve some of the problems that I ran into with the dictionary.
