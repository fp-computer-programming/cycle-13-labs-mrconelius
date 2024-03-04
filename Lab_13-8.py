# Open the file for writing
with open("my_file.txt", "w") as file:
    # Write the first line
    file.write("MRC, 03-03-2024\n")
    
    # Write the second line
    file.write("Hello World!\n")
    
    # Write the third line
    file.write("I've been playing rugby for fun!\n")

# No need to close the file explicitly when using the with statement
