# Add our dependencies.
import csv
import os
# Add a variable to load a file from a path.
file_to_load = os.path.join("Resources", "/Users/darrenlemyacrawford/Desktop/Class folder/Election_Analysis/Resources/election_results.csv")
# Add a variable to save the file to a path.
file_to_save = os.path.join("analysis", "/Users/darrenlemyacrawford/Class/Election_Analysis/analysis/election_analysis.txt")
# Initialize a total vote counter.
total_votes = 0
# Candidate Options and candidate votes.
candidate_options = []
candidate_votes = {}
# Track the winning candidate, vote count and percentage.
winning_candidate = ""
winning_count = 0
winning_percentage = 0
# Open the election results and read the file
with open(file_to_load) as election_data:
   file_reader = csv.reader(election_data)
   # Read the header row.
   headers = (next(file_reader))
   # Print each row in the CSV file.
   for row in file_reader:
       # Add to the total vote count.
       total_votes += 1


# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "/Users/darrenlemyacrawford/Class/Election_Analysis/analysis/election_analysis.txt"
# Use the open statement to open the file as a text file.
outfile = open(file_to_save, "w")
# Write some data to the file.
outfile.write("Hello World")

# Close the file
outfile.close()

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write some data to the file.
    txt_file.write("Hello World")

# Create a filename variable to a direct or indirect path to the file.
file_to_save = os.path.join("analysis", "election_analysis")

# Using the with statement open the file as a text file.
with open(file_to_save, "w") as txt_file:

    # Write three counties to the file.
     txt_file.write("Counties in the Election\n-----------------\nArapahoe\nDenver\nJefferson")

