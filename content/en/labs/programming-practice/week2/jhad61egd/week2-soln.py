def print_n_times(text, n):
    """ Print the value of text n times """
    for i in range(n):
        print(text)

def print_each(lst):
    """ Print each element in a list """
    for item in lst:
        print(item)

def count_times(lst, target):
    """ Count the number of times target appears in a list """
    count = 0
    for item in lst:
        if item == target:
            count += 1
    print(f"{target} appears {count} times in the list.")  # printing an f-string lets you put variables and expressions to be evaluated

# There are a few ways of solving the "first index of" problem. Here are two.
def first_index_of(target, lst):
    """ Print the first index where target occurs in the list. If not in list, print "Not found" """

    for i in range(len(lst)):
        if lst[i] == target:
            print(f"First index of target {target} is {i}")
            return  # returning when found immediately stops the loop and exists the function.
    print(f"Target {target} not found.")  # We only get here if we don't return earlier, meaning the target was not found.

def first_index_of2(target, lst):
    """ Print the first index where target occurs in the list. If not in list, print "Not found" """
    found = False
    i = 0
    while i < len(lst) and not found:
        if lst[i] == target:
            found = True
            # You could print and return at this point like in the previous function, but this is another style
        else:
            i += 1

    if found:
        print(f"First index of target {target} is {i}")
    else:
        print(f"Target {target} not found.")



def count_evens_odds(lst):
    """ Count and print the number of odd and even numbers in the list """
    count = 0
    for item in lst:
        if item % 2 == 0:
            count += 1

    # You could also have an else and two separate counters for even and odd.
    print(f"Even numbers: {count}, Odd numbers: {len(lst)-count}")

if __name__ == '__main__':
    print('-' * 5, "print_n_times", '-' * 5)
    print_n_times("Hello World!", 3)
    print_n_times("Five times", 5)

    print('-' * 5, "print_each", '-' * 5)
    print_each([1, 2, 3, 4, 5])
    print_each(['a', 'b', 'c', 'd', 'e', 'f'])

    print('-' * 5, "count_times", '-' * 5)
    count_times(['a', 'b', 'c', 'd', 'e', 'f'], 2)
    count_times(['a', 'b', 'b', 'b', 'e', 'f'], 'c' )
    count_times([9, 10, 11, 12], 12)

    print('-' * 5, "first_index_of", '-' * 5)
    first_index_of('a', ['b', 'a', 'a'])
    first_index_of('mayo', ['ketchup', 'mustard', 'ranch', 'tajin', 'mayo'])
    first_index_of(4, ['b', 'a', 'a'])

    print('-' * 5, "first_index_of2", '-' * 5)
    first_index_of2('a', ['b', 'a', 'a'])
    first_index_of('mayo', ['ketchup', 'mustard', 'ranch', 'tajin', 'mayo'])
    first_index_of2(4, ['b', 'a', 'a'])

    print('-' * 5, "count_evens_odds", '-' * 5)
    count_evens_odds([1, 2, 3, 4, 5])
    count_evens_odds([0, 1, 1, 1, 1, 1])