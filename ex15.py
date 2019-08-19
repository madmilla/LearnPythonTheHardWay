# Import the argv from the sys library
from sys import argv
#
# # the 2 parameters from argv you get is argv[0] mapped to script
# # Which will be the script
# # argv[1] file be the filename you want to open
script, filename = argv

# Open a file based on the filename
txt = open(filename)

print the filename title
print(f"Here's your file {filename}:")
# print out what it can be read from the file
print(txt.read())

# print("Type the filename again:")
# file_again = input("> ")
#
# txt_again = open(file_again)
# print(txt_again.read())
# txt_again.close()
