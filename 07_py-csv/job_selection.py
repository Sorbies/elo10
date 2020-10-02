"""
 Team Bad Vibes: Winnie Huang, Eric Lo
 SoftDev
 K07 -- StI/O: Divine your Destiny!
 2020-09-30
 
 Our Approach: We interpretted the problem step by step given the directions. First, we learned
 to download a file from github, how to read a csv file, and how to generate a dictionary based
 off of the responses on the csv file. Lastly, we learned to choose a random job occupation with
 the given weighted probability.
"""

import csv
import random

reader = csv.DictReader(open('occupations.csv'))  #allows us to read the csv file
dictionary = {                                    #sets up a destination for the contents of the csv file
    'job occupation': [],
    'percentage': []
}

for row in reader:                                #stores the contents of the csv file into the dictionary by iterating line by line
    dictionary['job occupation'].append(row['Job Class'])      
    dictionary['percentage'].append(float(row['Percentage']))  

dictionary['job occupation'].pop()                #gets rid of the 'Total' entry
dictionary['percentage'].pop()                    #gets rid of the 99.8 entry

dictionary['job occupation'].append('None')       #creates an option for missing percentage
dictionary['percentage'].append(0.2)              #missing percentage out of 100% probability

print(random.choices(dictionary['job occupation'], weights=dictionary['percentage'], k=1)[0])    #returns a randomly selected occupation where the results are weighted by the percentage given 
