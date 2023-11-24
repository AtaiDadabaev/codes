import csv
import json

def process_data(books_file, users_file):
    def get_book_data(book):
        return {
            "title": book['Title'],
            "author": book['Author'],
            "pages": book['Pages'],
            "genre": book['Genre']
        }

    def get_user_data(user, user_books):
        return {
            "name": user['name'],
            "gender": user['gender'],
            "address": user['address'],
            "age": user['age'],
            "books": [get_book_data(book) for book in user_books]
        }

    with open(books_file, newline='') as csvfile:
        books = list(csv.DictReader(csvfile))

    with open(users_file) as jsonfile:
        users = json.load(jsonfile)

    count_users = len(users)
    count_books = len(books)

    books_per_user = count_books // count_users
    remainder = count_books % count_users

    users_with_books = []

    for i in range(count_users):
        user = users[i]
        user_books = books[i * books_per_user:(i + 1) * books_per_user]

        if i < remainder:
            extra_book = books[count_users * books_per_user + i]
            user_books.append(extra_book)

        user_data = get_user_data(user, user_books)
        users_with_books.append(user_data)

    return users_with_books

if __name__ == "__main__":
    result_data = process_data("books.csv", "users.json")
    print(result_data)
