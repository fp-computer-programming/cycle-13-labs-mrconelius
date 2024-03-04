# Open the alma-mater.txt file for reading
with open("alma-mater.txt", "r") as file:
    # Read each line of the file and print it to the console with a blank line between each line
    for line in file:
        print(line.strip())  # Use strip() to remove any leading/trailing whitespace
        print()  # Print a blank line between each line
