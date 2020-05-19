"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in list of items"""
    for item in items:
        print(item)


def get_all_evens(nums):
    """Given a list of numbers, return a list of all even numbers"""
    even_nums = []

    for num in nums:
        if (num % 2) == 0:
            even_nums.append(num)

    return even_nums


def get_odd_indices(items):
    """Given a list of elements, return all elements at odd incices"""

    result = []

    for i in items:
        if (i % 2) != 0:
            result.append(items(i))

    return result        


def print_as_numbered_list(items):
    """Given a list, output a numbered list"""

    i = 1

    while i < len(items):
        for item in items:
            print(f'{i}. {item}')
            i = i + 1


def get_range(start, stop):
    """Return an array of numbers in a certain range"""

    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums
    
get_range(24, 35)

def censor_vowels(word):
    pass  # TODO: replace this line with your code


def snake_to_camel(string):
    pass  # TODO: replace this line with your code


def longest_word_length(words):
    pass  # TODO: replace this line with your code


def truncate(string):
    pass  # TODO: replace this line with your code


def has_balanced_parens(string):
    pass  # TODO: replace this line with your code


def compress(string):
    pass  # TODO: replace this line with your code
