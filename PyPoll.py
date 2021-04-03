# # The data we need to retrieve.
# import csv
# import random
# import numpy as np
# import os

# # Assign a variable for the file to load and the path
# # file_to_read = 'Resources/election_results.csv'  -  this is a different method
# file_to_load = os.path.join("Resources", "election_results.csv")


# # Open the election results and read the file
# # election_data = open(file_to_read, "r") - this is a differet method
# # election_data.close()
# with open(file_to_load) as election_data:
#     print(election_data)

# # Create a filename variable to a direct or indirect path to the file. Making a file to save analysis.
# file_to_save = os.path.join("analysis", "election_analysis.txt")
# # Using the open() function with the "w" mode we will write data to the file.
# # outfile = open(file_to_save, "w")
# # Write something to the outfile
# # outfile.write("Hello World")
# # outfile.close()

# # Cleaner version of writing to a file
# with open(file_to_save, "w") as txt_file:
#     # txt_file.write("Arapahoe\n")
#     # txt_file.write("Denver\n")
#     # txt_file.write("Jefferson")

#     txt_file.write("Counties in the election\n------------------------\nArapahoe\nDenver\nJefferson")

# Add our dependencies.
import csv
import os
# Assign a variable to load a file from a path.
file_to_load = os.path.join("Resources", "election_results.csv")
# Assign a variable to save the file to a path.
file_to_save = os.path.join("analysis", "election_analysis.txt")

# Open the election results and read the file.
with open(file_to_load) as election_data:

    # To do: read and analyze the data here.
    # Read the file object with the reader function.
    file_reader = csv.reader(election_data)
    # Print the header row.
    headers = next(file_reader)
    print(headers)
    # Print each row in the CSV file.
    # for row in file_reader:
    #     print(row)

# # The total number of votes cast.
# # A complete list of candidates who received votes.
# # The total number of votes each candidate won.
# # The winner of the election based on popular vote.