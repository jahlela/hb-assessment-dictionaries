"""Dictionaries Practice

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""


# def without_duplicates(words):
#     """Given a list of words, return list with duplicates removed.

#     For example::

#         >>> sorted(without_duplicates(
#         ...     ["rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['a', 'is', 'rose']

#     You should treat differently-capitalized words as different:

#         >>> sorted(without_duplicates(
#         ...     ["Rose", "is", "a", "rose", "is", "a", "rose"]))
#         ['Rose', 'a', 'is', 'rose']

#         An empty list should return an empty list::

#         >>> sorted(without_duplicates(
#         ...     []))
#         []

#     The function should work for a list containing integers::

#         >>> sorted(without_duplicates([111111, 2, 33333, 2]))
#         [2, 33333, 111111]
#     """

#     # Return a list of unique words by listifying a set of the original words
#     return list(set(words))


# def find_unique_common_items(items1, items2):
#     """Produce the set of *unique* common items in two lists.

#     Given two lists, return a list of the *unique* common items
#     shared between the lists.

#     **IMPORTANT**: you may not use `'if ___ in ___``
#     or the method `list.index()`.

#     This should find [1, 2]::

#         >>> sorted(find_unique_common_items([1, 2, 3, 4], [2, 1]))
#         [1, 2]

#     However, now we only want unique items, so for these lists,
#     don't show more than 1 or 2 once::

#         >>> sorted(find_unique_common_items([3, 2, 1], [1, 1, 2, 2]))
#         [1, 2]

#     The elements should not be treated as duplicates if they are
#     different data types::

#         >>> sorted(find_unique_common_items(["2", "1", 2], [2, 1]))
#         [2]
#     """

#     # Expanded version, which separately creates a set of each list of items. 
#     # This removes duplicates from each list and allows for set math.
#     set1 = set(items1)
#     set2 = set(items2)

#     # Find the intersection between the two sets.
#     commons = set1.intersection(set2)
#     # Return the intersection, converted into a list
#     return list(commons)

# ###############
#     # An equivalent, more compact way:

#     return list(set(items1).intersection(set(items2)))


# def get_sum_zero_pairs(numbers):
#     """Given list of numbers, return list of pairs summing to 0.

#     Given a list of numbers, add up each individual pair of numbers.
#     Return a list of each pair of numbers that adds up to 0.

#     For example::
#     #     >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1]) )
#     #     [[-2, 2], [-1, 1]]

#     #     >>> sort_pairs( get_sum_zero_pairs([3, -3, 2, 1, -2, -1]) )
#     #     [[-3, 3], [-2, 2], [-1, 1]]

#     # This should always be a unique list, even if there are
#     # duplicates in the input list::

#     #     >>> sort_pairs( get_sum_zero_pairs([1, 2, 3, -2, -1, 1, 1]) )
#     #     [[-2, 2], [-1, 1]]

#     # Of course, if there are one or more zeros to pair together,
#     # that's fine, too (even a single zero can pair with itself)::

#     #     >>> sort_pairs( get_sum_zero_pairs([1, 3, -1, 1, 1, 0]) )
#     #     [[-1, 1], [0, 0]]
#     """

#     # # So, here is one way to do it. 14 lines of code, 
#     # # but not quite as run-time optimized

#     # Initialize empty list and dictionary
#     pair_list = []
#     pair_dict = {}

#     # If numbers has a zero, automatically add [0,0] to pair_list and remove 0
#     # from numbers
#     if 0 in numbers:
#         pair_list.append([0,0])
#         numbers.pop(0)

#     # Loop through all numbers and store the positives and negatives in own lists
#     pos_list = [item for item in pair_dict if item > 0]
#     neg_list = [item for item in pair_dict if item < 0]

#     # Create dictionary entries for all positives and set to True 
#     for number in pos_list:
#         pair_dict[number] = True

#     for key in pair_dict:
#         for neg in neg_list:
#             if key + neg == 0:
#                 pair_list.append([key, neg])

#     return pair_list


#     # ############################

#     # Here's another way. 19 lines of code and slightly more optimized.

#     # Initialize empty list and dictionary
#     pair_list = []
#     pair_dict = {}

#     # Initialize empty sets for positives and negatives
#     pos_set = set()
#     neg_set = set()

#     # Loop through all numbers once and 
#     for number in numbers:
#         # If it's zero and we haven't recorded a zero before, add [0,0] to pairs
#         if number == 0 and checked_zeroes == False:
#             pair_list.append([0,0])
#             # Store that we have recorded a zero
#             checked_zeroes = True
#         # If number is negative, add it to neg_set
#         elif number < 0:
#             neg_set.add(number)
#         # If number is positive, add it to pos_set
#         elif number > 0:
#             pos_set.add(number)

#     # Create dictionary entries for all positive numbers
#     for number in pos_set:
#         pair_dict[number] = True

#     # Loop through each key in dictionary, and see if any of the negative 
#     # numbers and that key sum to zero
#     for key in pair_dict:
#         for neg in neg_set:
#             # If they sum to zero, add the pair to pair_list
#             if key + neg == 0:
#                 pair_list.append([key, neg])

#     return pair_list


# # #############################################

# # And a third way, which is 17 lines, and the most optimized of the three

#     # Initialize empty list and dictionary
#     pair_list = []
#     pair_dict = {}

#    # Initialize empty sets for positives and negatives
#     pos_set = set()
#     neg_set = set()

#     # Loop through all numbers once and 
#     for number in numbers:
#         # If it's zero and we haven't recorded a zero before, add [0,0] to pairs
#         if number == 0 and checked_zeroes == False:
#             pair_list.append([0,0])
#             # Store that we have recorded a zero
#             checked_zeroes = True
#         # If number is negative, add it to neg_set
#         elif number < 0:
#             neg_set.add(number)
#         # If number is positive, add it to pos_set
#         elif number > 0:
#             pos_set.add(number)

#     # Loop through each positive, and see if any of the negative 
#     # numbers and that key sum to zero
#     for pos in pos_set:
#         for neg in neg_set:
#             # If they sum to zero, add the pair to pair_list
#             if key + neg == 0:
#                 pair_list.append([key, neg])

#     return pair_list


def top_chars(phrase):
    """Find most common character(s) in string.

    Given an input string, return a list of character(s) which
    appear(s) the most the input string.

    If there is a tie, the order of the characters in the returned
    list should be alphabetical.

    For example::

        >>> top_chars("The rain in spain stays mainly in the plain.")
        ['i', 'n']

    If there is not a tie, simply return a list with one item.

    For example::

        >>> top_chars("Shake it off, shake it off.")
        ['f']

    Do not count spaces, but count all other characters.

    """

    
    counts = {}
    characters = [phrase]
    modes = []


    for character in characters:
        if character == " ":
            del character

        counts[character] = counts.get(character, 0) + 1
        if counts[character] > all(modes):
            modes = [character]
        elif counts[character] == all(modes):
            pass

    print counts

    print max(counts, key=counts.get)

    # return 

#####################################################################
# You can ignore everything below this.

def print_dict(d):
    # This method is used to print dictionaries in key-alphabetical
    # order, and is only for our doctests. You can ignore it.
    if isinstance(d, dict):
        print "{" + ", ".join(
            "%r: %r" % (k, d[k]) for k in sorted(d)) + "}"
    else:
        print d


def sort_pairs(l):
    # Print sorted list of pairs where the pairs are sorted. This is
    # used only for documentation tests. You can ignore it.
    return sorted(sorted(pair) for pair in l)


if __name__ == "__main__":
    print
    import doctest
    if doctest.testmod().failed == 0:
        print "*** ALL TESTS PASSED ***"
    print
