import logging

from app import books

logger = logging.getLogger('scraping.menu')


def print_best_books():
    logger.info('Finding best books by rating...')
    best_books = sorted(books, key=lambda x: x.rating * -1)[:10]  # this will give us the top ten books
    for book in best_books:
        print(book)


def print_cheapest_books():
    logger.info('Finding best books by price...')
    cheapest_books = sorted(books, key=lambda x: x.price)[:10]
    for book in cheapest_books:
        print(book)


books_generator = (x for x in books)


def get_next_book():
    logger.info('Getting next book from generator of all books...')
    print(next(books_generator))


menu_choices = {
    'b': print_best_books,
    'c': print_cheapest_books,
    'n': get_next_book
}


def menu():
    user_input = input(USER_CHOICE)
    while user_input != 'q':
        if user_input in ('b','c','n'):
            menu_choices[user_input]()  # see note below
        else:
            print('Unknown command. Please try again.')

        print('\n')
        menu_again = input('Would you like to see the menu again? [y/n] ')
        if menu_again == 'y':
            user_input = input(USER_CHOICE)
        elif menu_again == 'n':
            break
        else:
            print('Unknown command.')
            user_input = input(USER_CHOICE)
    logger.debug('Terminating program...')


USER_CHOICE = """
Please select one of the following:
- 'b' to look for 5-star books
- 'c' to look for the cheapest books
- 'n' to get the next available book on the page
- 'q' To quit

Your Choice: """

menu()


"""
menu_choices[user_input]() will give us the function that is associated 
with the input inside the menu_choices dictionary
"""