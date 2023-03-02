# Name:         Emma Bibb
# OSU Email:    bibbe@oregonstate.edu
# Course:       CS261 - Data Structures
# Assignment:   Assignment 1
# Due Date:     January 30th, 2023
# Description:  programming practice with Python


import random
from static_array import *


# ------------------- PROBLEM 1 - MIN_MAX -----------------------------------

def min_max(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    #
    x = StaticArray.length(arr) - 1
    min = StaticArray.get(arr, 0)
    max = StaticArray.get(arr, 0)

    # get min and max values
    while x >= 0:
        if StaticArray.get(arr, x) > max:
            max = StaticArray.get(arr, x)
        elif StaticArray.get(arr, x) < min:
            min = StaticArray.get(arr, x)
        x = x - 1

    # return min and max values
    return [min, max]

    pass

# ------------------- PROBLEM 2 - FIZZ_BUZZ ---------------------------------

def fizz_buzz(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # gets number/length in array
    x = StaticArray.length(arr) - 1
    fuzzBizz = StaticArray(x + 1)

    # takes array string and corresponds it to a string
    # /3 & /5 = fizzbuzz, else if /3 = fizz, else if /5 = buzz, else other = #
    while x >= 0:
        if StaticArray.get(arr, x) % 3 == 0 and StaticArray.get(arr, x) % 5 == 0:
            StaticArray.set(fuzzBizz, x, 'fizzbuzz')
            x = x - 1
        elif StaticArray.get(arr, x) % 3 == 0:
            StaticArray.set(fuzzBizz, x, 'fizz')
            x = x - 1
        elif StaticArray.get(arr, x) % 5 == 0:
            StaticArray.set(fuzzBizz, x, 'buzz')
            x = x - 1
        else:
            StaticArray.set(fuzzBizz, x, StaticArray.get(arr, x))
            x = x - 1

    return fuzzBizz

    pass

# ------------------- PROBLEM 3 - REVERSE -----------------------------------

def reverse(arr: StaticArray) -> None:
    """
    TODO: Write this implementation
    """
    #
    x = StaticArray.length(arr) - 1
    y = 0

    # reverse array
    while x > y:
        pos1 = StaticArray.get(arr, x)
        pos2 = StaticArray.get(arr, y)
        StaticArray.set(arr, x, pos2)
        StaticArray.set(arr, y, pos1)
        x = x - 1
        y = y + 1

    pass

# ------------------- PROBLEM 4 - ROTATE ------------------------------------

def rotate(arr: StaticArray, steps: int) -> StaticArray:
    """
        TODO: Write this implementation
    """
    # Setting max index
    size = StaticArray.length(arr)
    x = size - 1
    rotated = StaticArray(x + 1)
    while x >= 0:
        # Only keep steps after full revolutions around the size of the array
        pos = (x + steps) % size
        StaticArray.set(rotated, pos, StaticArray.get(arr, x))
        x = x-1
    return rotated
    pass


# ------------------- PROBLEM 5 - SA_RANGE ----------------------------------

def sa_range(start: int, end: int) -> StaticArray:
    # Getting range of the array
    o = abs(end - start) + 1
    # Creating new array
    values = StaticArray(o)
    # Just place holders
    x = start
    y = end
    z = 0

    # Filling in the array and incrmenting the placeholders
    while z < o:
        StaticArray.set(values, z, x)
        if x < y:
            x = x + 1
        else:
            x = x - 1
        z = z + 1

    return values
    pass


# ------------------- PROBLEM 6 - IS_SORTED ---------------------------------

def is_sorted(arr: StaticArray) -> int:
    """
    TODO: Write this implementation
    """
    # Using binary esque switches to determin what type of order.
    switch1 = 0 #ascending
    switch2 = 0 #descending
    x = StaticArray.length(arr) - 1
    # Turning on switches based on if they meet the criteria
    if StaticArray.length(arr) == 1:
        switch1 = 1
    else:
        while x > 0:
            next = x - 1
            if StaticArray.get(arr, x) == StaticArray.get(arr, next):
                switch1, switch2 = 1,1
            elif StaticArray.get(arr, x) > StaticArray.get(arr, next):
                switch1 = 1
            elif StaticArray.get(arr, x) < StaticArray.get(arr, next):
                switch2 = 1
            x = x - 1
    # If both switches turned on there would be other sorting returned
    if switch1 == 1 and switch2 == 1:
        return 0
    elif switch1 == 1:
        return 1
    else:
        return -1

    pass


# ------------------- PROBLEM 7 - FIND_MODE -----------------------------------

def find_mode(arr: StaticArray) -> (int, int):
    """
    TODO: Write this implementation
    """
    # Counter
    frequency = 0
    result = StaticArray(2)
    x = StaticArray.length(arr) - 1
    y = 0
    # Counting how many times a certain value shows up
    while x >= y:
        counter = 1
        cursor = StaticArray.get(arr, y)

        for i in range(0, x+1):
            if cursor == StaticArray.get(arr, i) and i != y:
                counter = counter + 1

        y = y + 1
        # if value showed up more than the last one it replaces it.
        if counter > frequency:
            frequency = counter
            mode = cursor
            StaticArray.set(result, 0, mode)
            StaticArray.set(result, 1, frequency)

    return result
    pass


# ------------------- PROBLEM 8 - REMOVE_DUPLICATES -------------------------

def remove_duplicates(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """

    x = StaticArray.length(arr) - 1
    y = 0
    # Setting up a counter to see how many unique values
    counter = 0
    # Filling in only unique values and nulls for the rest
    temp = StaticArray(x + 1)
    while y <= x:
        if y == 0:
            StaticArray.set(temp, y, StaticArray.get(arr, y))
            counter = counter + 1
        elif StaticArray.get(arr, y) != StaticArray.get(arr, y - 1):
            StaticArray.set(temp, y, StaticArray.get(arr, y))
            counter = counter + 1
        y = y + 1
    # new array with only the amount of unique values
    result = StaticArray(counter)

    y=0
    z=0
    # Anywhere an array value is not null we fill it in.
    while y <= x:
        if StaticArray.get(temp, y) != None:
            StaticArray.set(result, z, StaticArray.get(temp, y))
            z = z + 1

        y = y + 1

    return result


    pass


# ------------------- PROBLEM 9 - COUNT_SORT --------------------------------

def count_sort(arr: StaticArray) -> StaticArray:

    ## THIS RUNS REALLY SLOW IM SORRY
    # FORGOT TO MAP THE ITEMS SO IT WOULD BE FASTER
    x = StaticArray.length(arr) - 1
    min = StaticArray.get(arr, 0)
    max = StaticArray.get(arr, 0)
    index = 1
    # get the maximum and min value in the StaticArray
    while index <= x:
        cursor = StaticArray.get(arr, index)
        if cursor > max:
            max = cursor
        elif cursor < min:
            min = cursor

        index = index + 1

    result = StaticArray(x + 1)
    pos = x

    # Goes through every value and then adds em to the array if they exist
    for i in range(min, max + 1):
        index = 0
        while index <= x:
            cursor = StaticArray.get(arr, index)
            if StaticArray.get(arr, index) == i:
                StaticArray.set(result, pos, cursor)
                pos = pos - 1
            index = index + 1

    return result


    pass


# ------------------- PROBLEM 10 - SORTED SQUARES ---------------------------

def sorted_squares(arr: StaticArray) -> StaticArray:
    """
    TODO: Write this implementation
    """
    # Two sided approach due to the nature of negative numbers and squaring them.
    x = StaticArray.length(arr) - 1
    result = StaticArray(x + 1)
    index = x
    # starting position
    tail = 0
    # also a starting position
    head = x
    # How many items in array
    unit = x + 1

    # get starting number which could be negative and then compare it to the ending number (both squared)
    # - on for units anytime we use up a value like a fake pop()
    while unit > 0:
        tail_val = StaticArray.get(arr, tail) ** 2
        head_val = StaticArray.get(arr, head) ** 2
        if unit == 1:
            StaticArray.set(result, index, head_val)
            unit = unit - 1
        elif tail_val == head_val:
            StaticArray.set(result, index, head_val)
            index = index - 1
            unit = unit - 1
            head = head - 1
            StaticArray.set(result, index, tail_val)
            index = index - 1
            unit = unit - 1
            tail = tail + 1
        else:
            if head_val > tail_val:
                StaticArray.set(result,index,head_val)
                head = head - 1
            elif tail_val > head_val:
                StaticArray.set(result, index, tail_val)
                tail = tail + 1
            unit = unit - 1
            index = index - 1

    return result

    pass

# ------------------- BASIC TESTING -----------------------------------------


if __name__ == "__main__":

    print('\n# min_max example 1')
    arr = StaticArray(5)
    for i, value in enumerate([7, 8, 6, -5, 4]):
        arr[i] = value
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]: 3}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 2')
    arr = StaticArray(1)
    arr[0] = 100
    print(arr)
    result = min_max(arr)
    if result:
        print(f"Min: {result[0]}, Max: {result[1]}")
    else:
        print("min_max() not yet implemented")

    print('\n# min_max example 3')
    test_cases = (
        [3, 3, 3],
        [-10, -30, -5, 0, -10],
        [25, 50, 0, 10],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        result = min_max(arr)
        if result:
            print(f"Min: {result[0]: 3}, Max: {result[1]}")
        else:
            print("min_max() not yet implemented")

    print('\n# fizz_buzz example 1')
    source = [_ for _ in range(-5, 20, 4)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(fizz_buzz(arr))
    print(arr)

    print('\n# reverse example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    reverse(arr)
    print(arr)
    reverse(arr)
    print(arr)

    print('\n# rotate example 1')
    source = [_ for _ in range(-20, 20, 7)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr.set(i, value)
    print(arr)
    for steps in [1, 2, 0, -1, -2, 28, -100, 2 ** 28, -2 ** 31]:
        space = " " if steps >= 0 else ""
        print(f"{rotate(arr, steps)} {space}{steps}")
    print(arr)

    print('\n# rotate example 2')
    array_size = 1_000_000
    source = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(source))
    for i, value in enumerate(source):
        arr[i] = value
    print(f'Started rotating large array of {array_size} elements')
    rotate(arr, 3 ** 14)
    rotate(arr, -3 ** 15)
    print(f'Finished rotating large array of {array_size} elements')

    print('\n# sa_range example 1')
    cases = [
        (1, 3), (-1, 2), (0, 0), (0, -3),
        (-95, -89), (-89, -95)]
    for start, end in cases:
        print(f"Start: {start: 4}, End: {end: 4}, {sa_range(start, end)}")

    print('\n# is_sorted example 1')
    test_cases = (
        [-100, -8, 0, 2, 3, 10, 20, 100],
        ['A', 'B', 'Z', 'a', 'z'],
        ['Z', 'T', 'K', 'A', '5'],
        [1, 3, -10, 20, -30, 0],
        [-10, 0, 0, 10, 20, 30],
        [100, 90, 0, -90, -200],
        ['apple']
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        result = is_sorted(arr)
        space = "  " if result and result >= 0 else " "
        print(f"Result:{space}{result}, {arr}")

    print('\n# find_mode example 1')
    test_cases = (
        [1, 20, 30, 40, 500, 500, 500],
        [2, 2, 2, 2, 1, 1, 1, 1],
        ["zebra", "sloth", "otter", "otter", "moose", "koala"],
        ["Albania", "Belgium", "Chile", "Denmark", "Egypt", "Fiji"]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value

        result = find_mode(arr)
        if result:
            print(f"{arr}\nMode: {result[0]}, Frequency: {result[1]}\n")
        else:
            print("find_mode() not yet implemented\n")

    print('# remove_duplicates example 1')
    test_cases = (
        [1], [1, 2], [1, 1, 2], [1, 20, 30, 40, 500, 500, 500],
        [5, 5, 5, 4, 4, 3, 2, 1, 1], [1, 1, 1, 1, 2, 2, 2, 2]
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        print(arr)
        print(remove_duplicates(arr))
    print(arr)

    print('\n# count_sort example 1')
    test_cases = (
        [1, 2, 4, 3, 5], [5, 4, 3, 2, 1], [0, -5, -3, -4, -2, -1, 0],
        [-3, -2, -1, 0, 1, 2, 3], [1, 2, 3, 4, 3, 2, 1, 5, 5, 2, 3, 1],
        [10100, 10721, 10320, 10998], [-100320, -100450, -100999, -100001],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(case):
            arr[i] = value
        before = arr if len(case) < 50 else 'Started sorting large array'
        print(f"Before: {before}")
        result = count_sort(arr)
        after = result if len(case) < 50 else 'Finished sorting large array'
        print(f"After : {after}")

    print('\n# count_sort example 2')
    array_size = 5_000_000
    min_val = random.randint(-1_000_000_000, 1_000_000_000 - 998)
    max_val = min_val + 998
    case = [random.randint(min_val, max_val) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(case):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = count_sort(arr)
    print(f'Finished sorting large array of {array_size} elements')

    print('\n# sorted_squares example 1')
    test_cases = (
        [1, 2, 3, 4, 5],
        [-5, -4, -3, -2, -1, 0],
        [-3, -2, -2, 0, 1, 2, 3],
    )
    for case in test_cases:
        arr = StaticArray(len(case))
        for i, value in enumerate(sorted(case)):
            arr[i] = value
        print(arr)
        result = sorted_squares(arr)
        print(result)

    print('\n# sorted_squares example 2')
    array_size = 5_000_000
    case = [random.randint(-10 ** 9, 10 ** 9) for _ in range(array_size)]
    arr = StaticArray(len(case))
    for i, value in enumerate(sorted(case)):
        arr[i] = value
    print(f'Started sorting large array of {array_size} elements')
    result = sorted_squares(arr)
    print(f'Finished sorting large array of {array_size} elements')
