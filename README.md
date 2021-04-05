# Election_Analysis

## Project overview
A Colorado Board of Elections employee has given you the following tasks to complete the election audit of a recent local congressional election.

1. Calculate the total number of votes cast.
2. Get a complete list of candidates who received votes and counties where votes were cast.
3. Calculate the total number of votes each candidate and county received.
4. Calculate the percentage of votes each candidate won and percentage of votes from each county.
5. Determine the winner of the election based on popular vote and the largest county.

## Resources
- Data source: election_results.csv
- Software: Python 3.8.5, Visual Studio Code 1.54.3

## Results
The analysis of the election shows that:

- There were 369,711 votes cast in the election
- The Candidates were:
  - Charles Casper Stockham
  - Diana DeGette
  - Raymon Anthony Doane
- The candidate results were:
  - Charles Casper Stockham receieved 23.0% of the vote and 85,213 number of votes.
  - Diana DeGette receieved 73.8% of the vote and 272,892 number of votes.
  - Raymon Anthony Doane receieved 3.1% of the vote and 11,606 number of votes.
- The winner of the election was:
  - Diana DeGette, who receieved 73.8% of the vote and 272,892 number of votes.

- The Counties were:
  - Jefferson
  - Denver
  - Arapahoe
- The county result were:
  - Jefferson county had 10.5% of the vote and 38,855 number of votes.
  - Denver county had 82.8% of the vote and 306,055 number of votes.
  - Arapahoe county had 6.7% of the vote and 24,801 number of votes.
- The largest county of the election was:
  - Denver county, which had 82.8% of the vote and 306,055 number of votes.

![Overview of Results](/Resources/Election_Summary.png)

## Challenge Overview
The challenge asked to find county information in addition to candidate information for this election.

## Challenge Summary (Using the script for other elections)
This script can be used in any election that follows the same format by simply changing the file path on line 9.
`file_to_load = os.path.join("Resources", "election_results.csv")

Another election, for example for governor, could use this script with some modifications. A likely modification would be getting more data than the 3 columns of just voter id, county, and candidate choice. For example, a gubernatorial election may include cities as well as counties.

If cities were added, they could be added as another column in the list of data on the csv received. If cities were the 4th column, they could be added without changing the other data at all. If they were a different column, say between voter id and county, one would only need to change the row number to equal that column from the csv minus 1.

`city_name = row[1]`

Then one would merely add variables for a list of city names, how many votes were from each city, or any other desired information if possible from what is given. After that modify the first for loop to make the list of cities. Finally, make a for loop within `with open(file_to_save, "w") as txt_file:` to get the voting results by city.

City variables:
```
city_options = []
city_votes = {}
```

First for loop:
```
        city_name = row[3]

        if city_name not in city_options:
            city_options.append(city_name)
            city_votes[city_name] = 0
```

within `with open(file_to_save, "w") as txt_file:`
```
    for city_name in city_votes:
        civotes = city_votes.get(city_name)
        civote_percentage = float(civotes) / float(total_votes) * 100
        city_results = (f"{city_name}: {civote_percentage:.1f}% ({civotes:,})\n")
        print(city_results)
        txt_file.write(city_results)
```