"""Python functions for JavaScript Trials 1."""


def output_all_items(items):
    """Print each item in list of items"""
    for item in items:
        print(item)

output_all_items(['no', 'soup', 'for','you'])

def get_all_evens(nums):
    """Given a list of numbers, return a list of all even numbers"""
    even_nums = []

    for num in nums:
        if (num % 2) == 0:
            even_nums.append(num)

    return even_nums

print(get_all_evens([2,5,4,8,8,6,5]))

def get_odd_indices(items):
    """Given a list of elements, return all elements at odd incices"""

    result = []

    for idx in range(len(items)):
        if idx % 2 == 0:
            result.append(items[idx])

    return result        

print(get_odd_indices(['one','two','three','four','five']))

def print_as_numbered_list(items):
    """Given a list, output a numbered list"""

    i = 1

    while i < len(items):
        for item in items:
            print(f'{i}. {item}')
            i = i + 1

print_as_numbered_list(['head','shoulders','knees','toes'])

def get_range(start, stop):
    """Return an list of numbers in a certain range"""

    nums = []

    for num in range(start, stop):
        nums.append(num)

    return nums

print(get_range(13, 32))

def censor_vowels(word):
    """Given a string, return a string where the vowels are replaced with '*'"""

    chars = []

    for letter in word:
        if letter in 'aeiou':
            chars.append('*')
        else:
            chars.append(letter)

    return ''.join(chars)

print(censor_vowels('Hello World'))

def snake_to_camel(string):
    """Given a string in snake case, return a string in upper camel case"""

    camel_case = []

    for word in string.split('_'):
        camel_case.append(f'{word[0].upper()}{word[1:]}')

    return ''.join(camel_case)

print(snake_to_camel('melissa_rauch'))


def longest_word_length(words):
    """Return the length of the longest word in the given list of words"""

    longest = len(words[0])

    for word in words:
        if longest < len(word):
            longest = len(word)

    return longest

print(longest_word_length(['cat','chicken','goat','dog', 'elephant']))

def truncate(string):
    """Truncate repeating characters into one character"""

    result = []

    for char in string:
        if len(result) == 0 or char != result[-1]:
            result.append(char)

    return ''.join(result)

print(truncate('aaaabbbbcccca'))

def has_balanced_parens(string):
    """return true if all parentheses in a given string are balanced"""
    
    parens = 0

    for char in string:
        if char == '(':
            parens = parens + 1
        elif char == ')':
            parens = parens - 1

    if parens != 0:
        return False
    else:
        return True

print(has_balanced_parens("(simple times)"))

def compress(string):
    """Return a compressed version of the given string"""
    
    compressed = []

    curr_char = ''

    char_count = 0

    for char in string:
        if char != curr_char:
            compressed.append(curr_char)

            if char_count > 1:
                compressed.append(str(char_count))

            curr_char = char 
            char_count = 0

        char_count = char_count + 1

    compressed.append(curr_char)
    if char_count > 1:
        compressed.append(str(char_count))

    return ''.join(compressed)
print(compress('Hello World! Cows go moooo'))