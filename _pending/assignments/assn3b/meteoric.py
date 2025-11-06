"""
    Module for displaying information about meteor data from the NASA Meteorite Landings dataset:
    https://data.nasa.gov/widgets/gh4g-9sfh

    Created by: <put your names here>
"""
import sys
import csv


def load_data():
    """Load meteorite data into a "list of lists".
    Each element in the list corresponds to a single line in the CSV file.
    Each line has 9 elements: name,id,nametype,recclass,mass (g),fall,year,reclat,reclong

    Returns:
        list: a list of lists, where each inner list contains the data for one meteor
    """
    with open('meteorite_landings.csv', encoding='utf-8', newline='') as csvfile:
        next(csvfile)  # skip the header row
        return list(csv.reader(csvfile))


def main():
    """The main function that provides the console interface for the application.
    """
    # attempt to get the command and argument from the CLI or the input() console.
    if len(sys.argv) == 3:
        command = sys.argv[1]
        arg = sys.argv[2]
    else:
        print("Give a command. Options are:")
        command, arg = input("Enter a command: ").split(' ')

    # Read the CSV file data into a list.
    meteors = load_data()

    # Add code here to validate command & arg, and then call the functions to process the data.



if __name__ == "__main__":
    main()
