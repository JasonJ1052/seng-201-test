
def main():
    filename = input("Enter the bird file name: ")
    filename = filename.strip()  # removes any leading or trailing whitespace

    if not filename.endswith('.txt'):
        print("Error: You need to enter a valid filename ending in .txt")

    birds = {}
    # {
    #     'Baltimore Oriole' : 2,
    #     'Cardinal' : 3
    # }

    try: 
        with open(filename) as input_file:
            for line in input_file:
                name = line.strip()  # strip \n at the end of the line
                if name in birds:
                    birds[name] += 1
                else:
                    birds[name] = 1

        if birds == {}:
            print("Error: This file is empty!")
        else: 
            for bird, count in birds.items():
                print(bird, count)
    except FileNotFoundError:
        print("Error: Could not find that file!")
    except UnicodeDecodeError:
        print("Error: Could not read file data. Does not appear to be a valid text file.")


if __name__ == "__main__":
    main()