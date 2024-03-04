# Open the alma-mater.txt file for reading
with open("alma-mater.txt", "r") as file:
    # Read all lines of the file at once and store them in a list
    lines = file.readlines()

# Print the lines in reverse order with a blank line between each line
for line in reversed(lines):
    print(line.strip())  # Use strip() to remove any leading/trailing whitespace
    print()  # Print a blank line between each line
