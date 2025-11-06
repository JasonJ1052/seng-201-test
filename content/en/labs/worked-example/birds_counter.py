def count_birds(filename):
    # This function's job is to compute a dictionary of bird species and counts
    # It raises an exception if the filename 
    #   - does not end in .txt
    #   - if the file is not found
    #   - if the file is in a bad text format

    filename = filename.strip()  # removes any leading or trailing whitespace

    if not filename.endswith('.txt'):
        raise ValueError("You need to enter a valid filename ending in .txt")

    birds = {}

    with open(filename) as input_file:
        for line in input_file:
            name = line.strip()  # strip \n at the end of the line
            if name in birds:
                birds[name] += 1
            else:
                birds[name] = 1
    
    return birds       


def main():
    # The main() function mostly handles user input and user output (printing)
    filename = input("Enter the bird file name: ")
   
    try:
        birds = count_birds(filename)
        if birds == {}:
            print("Error: Text file is empty")
        else: 
            for bird, count in birds.items():
                print(bird, count) 
    except FileNotFoundError:
        print("Error: Could not find that file!")
    except UnicodeDecodeError:
        print("Error: Could not read file data. Does not appear to be a valid text file.")
    except ValueError as verr:
        print(f"Error: {verr}")


if __name__ == "__main__":
    main()