# counties = ["Arapahoe","Denver","Jefferson"]
# if counties[1] == 'Denver':
#     print(counties[1])

# voting_data = [{'county': 'El Paso', 'registered_voters': 461149}, {'county': 'Jefferson', 'registered_voters': 432438}, {'county': 'Denver', 'registered_voters': 463353}, {'county': 'Arapahoe', 'registered_voters': 422829}]

# # just get the county names(value) but there's a simpler way below
# for i in range(len(voting_data)):
#       print(voting_data[i]["county"])

# # get the values of both counties and voters
# for county_dict in voting_data:
#     for value in county_dict.values():
#         print(value)

# # just get the counties(1st value) from counties
# for county_dict in voting_data:
#     print(county_dict['county'])

# # just get the voters(2nd value) from registered voters
# for county_dict in voting_data:
    #  print(county_dict['registered_voters'])
    #  print(f"{county_dict['registered_voters']}")

# # using f strings
# candidate_votes = int(input("How many votes did the candidate get in the election? "))
# total_votes = int(input("What is the total number of votes in the election? "))
# message_to_candidate = (
#     f"You received {candidate_votes} number of votes. "
#     f"The total number of votes in the election was {total_votes}. "
#     f"You received {candidate_votes / total_votes * 100}% of the total votes.")

# print(message_to_candidate)

# # added thousands separator in first 2 messages and 2 decimal place for 3rd message
# message_to_candidate = (
#     f"You received {candidate_votes:,} number of votes. "
#     f"The total number of votes in the election was {total_votes:,}. "
#     f"You received {candidate_votes / total_votes * 100:.2f}% of the total votes.")

# print(message_to_candidate)

# # skill drill - print each county and registered voters from a dictionary
# counties_dict = {"Arapahoe": 422829, "Denver": 463353, "Jefferson": 432438}
# for county, voters in counties_dict.items():
#     print(f'{county} county has {voters:,} registered voters.')

# # print each count and its registered voters from a list of dictionaries
# voting_data = [{"county":"Arapahoe", "registered_voters": 422829}, {"county":"Denver", "registered_voters": 463353}, {"county":"Jefferson", "registered_voters": 432438}]
# for county_data in voting_data: 
#     print(f'{county_data["county"]} county has {county_data["registered_voters"]:,} registered voters.') 

# Import the datetime class from the datetime module.
import datetime
# Use the now() attribute on the datetime class to get the present time.
now = datetime.datetime.now()
# Print the present time.
print("The time right now is ", now)