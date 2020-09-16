# Program to read a random Mad Lib from a file and print the Mad Lib with the user's response

import random, os.path
# print(os.path.isfile("madlibs.txt")) # True

def read_file(file):

    f = open(file)

    # Read the whole file and store each line in a list
    return f.readlines()

def main():
    file_name = input("File name: ")
    if os.path.isfile(file_name):
        madlibText = read_file(file_name)
        # Choose a random line from the list
        madlib = random.choice(madlibText)

        # Ask the user to input a noun
        noun = input("Enter a noun: ")

        # Replace the blank with the user's input
        madlib = madlib.replace('blank', noun)

        print(madlib)
        
    else:
        print(f"There is no file name {file_name}")

if __name__ == "__main__":
    main()
    