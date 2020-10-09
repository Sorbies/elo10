import random
from flask import Flask
app = Flask(__name__) 

#Create an empty dictionary
jobsPercentages = {}

#Opens and reads the occupations.csv file
occupations = open("occupations.csv")
#Goes through each line of the file one-by-one
for line in occupations:
    #Skips the first and last line
    if line.startswith("Job Class") or line.startswith("Total"): continue
    #Removes whitespace and splits along commas
    line = line.strip().split(",")
    #Joins everything except the percentage (in case job has commas within title)
    jobTitle = "".join(line[:-1])
    #Converts the percentage into a float
    percentage = float(line[-1])
    #Updates dictionary with new key_value pair
    jobsPercentages[jobTitle] = percentage  


@app.route("/")       
def hello_world():   
    #Choose random job
    job = ((random.choices(list(jobsPercentages.keys()), weights=list(jobsPercentages.values()), k=1))[0])
    output = "Team AEI: Alvin Wu, Eric Lo, Ishita Gupta" + "<br/><br/>" + "List of potential jobs:" + "<br/><br/>" + str(list(jobsPercentages.keys())) + "<br/><br>" +  "Job: " + job
    return output

app.run()
