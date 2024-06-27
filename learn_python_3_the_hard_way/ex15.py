from sys import argv

script, filename = argv

with open(filename, "r") as txt:
    print(f"Here's your file {filename}:")
    print(txt.read())

print("Type the filename again:")
file_again = input("> ")

with open(file_again, "r") as txt:
    print(txt.read())
