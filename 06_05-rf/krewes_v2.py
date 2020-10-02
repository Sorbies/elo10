# Team Bad Vibes: Winnie Huang, Eric Lo
# SoftDev
# K06 -- Learnination Through Amalgamation
# 2020-09-30
# The approach we chose for the team that the member was being selected from is that the user should specifiy which
# team they're looking to receive a member from.

from random import choice 

KREWES = {
    'orpheus': ['ERIC', 'SAUVE', 'JONATHAN', 'PAK', 'LIAM', 'WINNIE', 'KELLY', 'JEFFREY', 'KARL', 'ISHITA', 'VICTORIA', 'BENJAMIN', 'ARIB', 'AMELIA', 'CONSTANCE', 'IAN'],
    'rex': ['ANYA', 'DUB-Y', 'JESSICA', 'ALVIN', 'HELENA', 'MICHELLE', 'SHENKER', 'ARI', 'STELLA', 'RENEE', 'MADELYN', 'MAC', 'RYAN', 'DRAGOS'],
    'endymion': ['JASON', 'DEAN', 'MADDIE', 'SAQIF', 'CINDY', 'YI LING', 'RUOSHUI', 'FB', 'MATTHEW', 'MAY', 'ERIN', 'MEIRU']
}

#takes a dictionary as a parameter where each value in the dictionary is an array of strings with each string representing
#name of a person on that team
def get_team_name(dic: dict) -> str:
    team_name = input("Please enter the name of the team you'd like to select a member from: ").lower()
    while team_name not in dic:  #ensures team name provided exists
        #ensures we don't encounter a keyError
        team_name = input(
            "Please enter a valid team name. \nAvailable options include orpheus, rex, and endymion: ").lower()

    return team_name  #returns string of the user-chosen team

def main():
    team_name = get_team_name(KREWES)
    team_member = choice(KREWES[team_name])
    print(f"Team member {team_member} chosen.")


main()
