"""Dictionaries Assessment

**IMPORTANT:** these problems are meant to be solved using
dictionaries and sets.
"""

def count_words(phrase):
    """Count unique words in a string.

    This function should take a single string and return a dictionary
    that has all of the distinct words as keys, and the number of
    times that word appears in the string as values.

    For example::

        >>> print_dict(count_words("each word appears once"))
        {'appears': 1, 'each': 1, 'once': 1, 'word': 1}

    Words that appear more than once should be counted each time::

        >>> print_dict(count_words("rose is a rose is a rose"))
        {'a': 2, 'is': 2, 'rose': 3}

    It's fine to consider punctuation part of a word (e.g., a comma
    at the end of a word can be counted as part of that word) and
    to consider differently-capitalized words as different::

        >>> print_dict(count_words("Porcupine see, porcupine do."))
        {'Porcupine': 1, 'do.': 1, 'porcupine': 1, 'see,': 1}
    """

    # Initialize empty dictionary
    unique_words = {}
    # Create list of words split from input phrase
    splits = phrase.split()

    # Create dictionary entries for each word in splits, using the word as the 
    # key and 1 as its value. If the word appears more than once, incrememnt
    # the key every time we encounter it.
    for word in splits:
        unique_words[word] = unique_words.get(word, 0) + 1

    return unique_words


def get_melon_price(melon_name):
    """Given a melon name, return the price of the melon

    Here are a list of melon names and prices:
    Watermelon 2.95
    Cantaloupe 2.50
    Musk 3.25
    Christmas 14.25
    (it was a bad year for Christmas melons -- supply is low!)

        >>> get_melon_price('Watermelon')
        2.95

        >>> get_melon_price('Musk')
        3.25

        >>> get_melon_price('Tomato')
        'No price found'
    """

    # Create melons dictionary using given values. Keys are the melon names and 
    # values are their prices
    melons = {"Watermelon" : 2.95,
              "Cantaloupe" : 2.50,
              "Musk" : 3.25, 
              "Christmas" : 14.25}

    # If we have an entry for the melon, return its value (price)
    if melon_name in melons: 
        return melons[melon_name]
    # If not, return "No price found"
    else: 
        return "No price found"


def word_length_sorted(words):
    """Return list of word-lengths and words.

    Given a list of words, return a list of tuples, ordered by
    word-length. Each tuple should have two items --- a number that
    is a word-length, and the list of words of that word length.

    In addition to ordering the list by word length, order each
    sub-list of words alphabetically.

    For example::

        >>> word_length_sorted(["ok", "an", "apple", "a", "day"])
        [(1, ['a']), (2, ['an', 'ok']), (3, ['day']), (5, ['apple'])]
    """

    # Initialize empty dictionary and list
    word_lengths_dict = {}
    word_lengths_tuples = []

    # Loop through each item in words
    for word in words:
        # Assign length to each word
        length = len(word) 

        # If we have already recorded a word of this length in the dictionary, 
        # add the word to the value list and sort that list
        if length in word_lengths_dict:
            word_lengths_dict[length].append(word)
            word_lengths_dict[length].sort()
        # If we have never recorded a word of this length, do it now.
        else:
            word_lengths_dict[length] = [word]

    # For each entry in the dicitonary unpack its key and value and store them 
    # as tuples in a list to be returned to the user
    for key, value in word_lengths_dict.iteritems():
        new_tuple = (key, value)
        word_lengths_tuples.append(new_tuple)

    return word_lengths_tuples



def translate_to_pirate_talk(phrase):
    """Translate phrase to pirate talk.

    Given a phrase, translate each word to the Pirate-speak
    equivalent. Words that cannot be translated into Pirate-speak
    should pass through unchanged. Return the resulting sentence.

    Here's a table of English to Pirate translations:

    ----------  ----------------
    English     Pirate
    ----------  ----------------
    sir         matey
    hotel       fleabag inn
    student     swabbie
    man         matey
    professor   foul blaggart
    restaurant  galley
    your        yer
    excuse      arr
    students    swabbies
    are         be
    restroom    head
    my          me
    is          be
    ----------  ----------------

    For example::

        >>> translate_to_pirate_talk("my student is not a man")
        'me swabbie be not a matey'

    You should treat words with punctuation as if they were different
    words::

        >>> translate_to_pirate_talk("my student is not a man!")
        'me swabbie be not a man!'
    """
    # Split original phrase into list of words
    tiny_splits = phrase.split()
    # Initialize empty list that will be used to make final translation
    pirate_out = []

    # Create translation dictionary where keys are English and values are Pirate
    pirate_speak = {"sir":"matey",
                    "hotel":"fleabag inn",
                    "student":"swabbie",
                    "man":"matey",
                    "professor":"foul blaggart",
                    "restaurant":"galley",
                    "your":"yer",
                    "excuse":"arr",
                    "students":"swabbies",
                    "are":"be",
                    "restroom":"head",
                    "my":"me",
                    "is":"be"}

    # Loop through list of words and append each translation to pirate_out if it
    # is in the dictionary. Otherwise, add the original word to pirate_out.
    for word in tiny_splits:
        if word in pirate_speak:
            pirate_out.append(pirate_speak[word])
        else:
            pirate_out.append(word)

    return " ".join(pirate_out)


def kids_game(names):
    """Play a kids' word chain game.

    Given a list of names, like::

      bagon baltoy yamask starly nosepass kalob nicky

    Do the following:

    1. Always start with the first word ("bagon", in this example).

    2. Add it to the results.

    3. Use the last letter of that word to look for the next word.
       Since "bagon" ends with n, find the *first* word starting
       with "n" in our list --- in this case, "nosepass".

    4. Add "nosepass" to the results, and continue. Once a word has
       been used, it can't be used again --- so we'll never get to
       use "bagon" or "nosepass" a second time.

    5. When you can't find an unused word to use, you're done!
       Return the list of output words.

    For example::

        >>> kids_game(["bagon", "baltoy", "yamask", "starly",
        ...            "nosepass", "kalob", "nicky", "booger"])
        ['bagon', 'nosepass', 'starly', 'yamask', 'kalob', 'baltoy']

    (After "baltoy", there are no more y-words, so we end, even
    though "nicky" and "booger" weren't used.)

    Another example:

        >>> kids_game(["apple", "berry", "cherry"])
        ['apple']

    This is a tricky problem. In particular, think about how using
    a dictionary (with the super-fast lookup they provide) can help;
    good solutions here will definitely require a dictionary.
    """

    # Initialize the name_lookup dictionary
    name_lookup = {}
    # Initialize the list of names that will be returned at the end of the game
    game = [names[0]]
    # Remove the first word so it isn't repeated
    del names[0]

    # Create dictionary: Keys are single letters, values are a list of all names
    # that start with that letter
    for word in names:
        first_letter = word[0] 

        # Could have used get here, but it was such a long and convoluted line
        # that I decided to just use if/else in order to add each word starting
        # with each letter to a list value at that letter key
        if first_letter in name_lookup:
            name_lookup[first_letter].append(word)
        else:
            name_lookup[first_letter] = [word]

    keep_playing = True

    # Keep playing as long as there is another word that matches the last character
    while keep_playing == True:
        try:
            # Set the pointer to be the last character of the last word in names
            pointer = game[-1][-1]
            # find pointer in name_lookup and store its last item as next_name
            next_name = name_lookup[pointer][0]
            # Remove next_name from name_lookup so it isn't used twice
            name_lookup[pointer].remove(next_name)
            # Add next_name to game
            game.append(next_name)
        # If there are no more words that start with the pointer, it will throw
        # an exception and stop the game
        except:
            keep_playing = False

    return game


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
