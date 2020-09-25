'''
Victoria Gao, Ishita Gupta, Eric Lo
SoftDev
K05 -- Teamwork, but Better This Time
2020-09-25

We interpreted the assignment to require no user input, so we picked a random team and then a random member of that team.
'''

#Write a program that will print the name of a randomly-selected student from team (orpheus, rex, or endymion).
import random 
KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

"""
We chose a team randomly by picking a random integer from [0,3).
This integer is the index of a team name from a list containing the KREWES dictionary's keys.
"""
team_index = random.randrange(3)
team_name = list(KREWES)[team_index]

"""
After picking a team randomly, we found the number of names in that team to determine the
end value of an interval.
A random integer between 0 and that end value will be generated to represent the
index of a student in a team.
"""

team_size = random.randrange(len(team_name))
student = KREWES[team_name][team_size]
print(student)
