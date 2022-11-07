# # # How many votes did you get?
# # my_votes = int(input("How many votes did you get in the election? "))
# # #  Total votes in the election
# # total_votes = int(input("What is the total votes in the election? "))
# # # Calculate the percentage of votes you received.
# # percentage_votes = (my_votes / total_votes) * 100
# # print("I received " + str(percentage_votes)+"% of the total votes.")

# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] != 'Jefferson':
#     print(counties[2])

# #counties = ["Arapahoe","Denver","Jefferson"]
# if "El Paso" in counties:
#     print("El Paso is in the list of counties.")
# else:
#     print("El Paso is not the list of counties.")

# if "Arapahoe" in counties and "El Paso" not in counties:
#    print("Only Arapahoe is in the list of counties.")
# else:
#     print("Arapahoe is in the list of counties and El Paso is not in the list of counties.")

# # for num in range(5):
# #     print(num)

# counties_tuples = ("Arapahoe","Denver","Jefferson")
# for i in range(len(counties_tuples)):

#       print(counties_tuples[i])

# for county in counties_tuples:

#       print(county)

# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

# for county in counties_dict:
#     print(county)
    
# print(f"\n")

# for county in counties_dict.keys():
#     print(county)

# print(f"\n")

# for county in counties_dict.values():
#     print(county)

# print(f"\n")

# for county in counties_dict:
#     print(counties_dict[county])

# print(f"\n")

# for county in counties_dict:
#     print(counties_dict.get(county))

# print(f"\n")
# # Get the Key-Value Pairs of a Dictionary
# for county, voters in counties_dict.items():
#     print(county, "county has", voters, "registered voters")

# voting_data = [{"county":"Arapahoe", "registered_voters": 422829},
#                 {"county":"Denver", "registered_voters": 463353},
#                 {"county":"Jefferson", "registered_voters": 432438}]

# for county_dict in range(len(voting_data)):
#     print(voting_data[county_dict]["county"])

# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# for county_dict in voting_data:
#     print(county_dict['county'])

# for county_dict in voting_data:
#     print(county_dict['registered_voters'])


counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}

for counties, voters in counties_dict.items():
        print(f"{counties} county has {voters:,} regsitered voters")

voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]

#If you use double quotation marks for the f-strings containing the keys, then be sure to use single quotation marks for the keys and values of the dictionary.
for county_dict in voting_data:
        print(f'{county_dict["county"]} has {county_dict["registered_voters"]:,} registered voters')


# import datetime

# now = datetime.datetime.now()

# print(now)

# Import modules and available functions
# import csv

# print(dir('Resourses/election_results.csv'))

# print(dir(int))