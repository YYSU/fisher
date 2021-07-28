
def is_isbn_or_key(word):
    """Identify what kind of word that user send, is it ISBN or KeyWord.
    :param word:
    :return isbn_or_key:
    """
    # isbn -> (1) isbn13 13個0到9的數字組成 or (2) isbn10 10個0到9的數字組成，含有-
    isbn_or_key = 'key'  # default
    if len(word) == 13 and word.isdigit():
        isbn_or_key = 'isbn'

    short_word = word.replace('-', '')
    if '-' in word and len(short_word) == 10 and short_word.isdigit():
        isbn_or_key = 'isbn'

    return isbn_or_key