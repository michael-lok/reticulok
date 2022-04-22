from typing import List, Tuple


def get_nth_highest_sold(
    books: List[Tuple[float, int]], n: int
    ) -> Tuple[float, int]:
    """
    Find the nth highest sold book from a list of books. The first
    element in each tuple represents the price; the second represents
    the number of units sold. If there is a tie in frequency sold,
    then return the book that is the least expensive amongst the tied
    records.

    Args:
        books (list): array of books, with price and units sold
        n (int): nth highest book sold to be returned

    Returns:
        tuple: book price and units sold
    """
    if not books:
        return None

    try:    
        nth_sold = sorted(list(set([x[1] for x in books])), reverse=True)[n-1]
    except IndexError: # input n is out of range
        return None

    matches = [i for i, x in enumerate(books) if x[1] == nth_sold]

    if len(matches) == 1:
        return books[matches[0]]
    else:
        cheapest = min([x[0] for i, x in enumerate(books) if i in matches])
        return [(x, y) for x, y in books if x == cheapest and y == nth_sold][0]
