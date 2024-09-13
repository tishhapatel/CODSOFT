# Sample book data
books = {
    "book1": {
        "title": "Pride and Prejudice",
        "author": "Jane Austen",
        "genre": ["Romance", "Classic"]
    },
    "book2": {
        "title": "The Lord of the Rings",
        "author": "J.R.R. Tolkien",
        "genre": ["Fantasy", "Adventure"]
    },
    "book3": {
        "title": "To Kill a Mockingbird",
        "author": "Harper Lee",
        "genre": ["Fiction", "Classic"]
    },
    "book4": {
        "title": "1984",
        "author": "George Orwell",
        "genre": ["Dystopian", "Science Fiction"]
    },
    "book5": {
        "title": "The Brothers Karamazov",
        "author": "Fyodor Dostoevsky",
        "genre": ["Philosophical", "Classic"]
    },
    "book6": {
        "title": "The Great Gatsby",
        "author": "F. Scott Fitzgerald",
        "genre": ["Fiction", "Classic"]
    },
    "book7": {
        "title": "Moby-Duck",
        "author": "Herman Melville",
        "genre": ["Adventure", "Classic"]
    },
    "book8": {
        "title": "War and Peace",
        "author": "Leo Tolstoy",
        "genre": ["Historical", "Classic"]
    },
    "book9": {
        "title": "The Catcher in the Rye",
        "author": "J.D. Salinger",
        "genre": ["Fiction", "Classic"]
    },
    "book10": {
        "title": "Brave New World",
        "author": "Aldous Huxley",
        "genre": ["Dystopian", "Science Fiction"]
    },
    "book11": {
        "title": "The Hobbit",
        "author": "J.R.R. Tolkien",
        "genre": ["Fantasy", "Adventure"]
    },
    "book12": {
        "title": "Fahrenheit 451",
        "author": "Ray Bradbury",
        "genre": ["Dystopian", "Science Fiction"]
    },
    "book13": {
        "title": "Crime and Punishment",
        "author": "Fyodor Dostoevsky",
        "genre": ["Psychological", "Classic"]
    },
    "book14": {
        "title": "The Alchemist",
        "author": "Paulo Coelho",
        "genre": ["Fantasy", "Philosophical"]
    },
    "book15": {
        "title": "Jane Eyre",
        "author": "Charlotte Brontë",
        "genre": ["Romance", "Classic"]
    },
    "book16": {
        "title": "The Road",
        "author": "Cormac McCarthy",
        "genre": ["Post-Apocalyptic", "Fiction"]
    },
    "book17": {
        "title": "The Odyssey",
        "author": "Homer",
        "genre": ["Epic", "Adventure"]
    },
    "book18": {
        "title": "The Count of Monte Cristo",
        "author": "Alexandre Dumas",
        "genre": ["Adventure", "Historical"]
    },
    "book19": {
        "title": "Frankenstein",
        "author": "Mary Shelley",
        "genre": ["Horror", "Science Fiction"]
    },
    "book20": {
        "title": "The Picture of Dorian Gray",
        "author": "Oscar Wilde",
        "genre": ["Philosophical", "Classic"]
    },
    "book21": {
        "title": "One Hundred Years of Solitude",
        "author": "Gabriel Garcia Marquez",
        "genre": ["Magical Realism", "Fiction"]
    },
    "book22": {
        "title": "Dracula",
        "author": "Bram Stoker",
        "genre": ["Horror", "Gothic"]
    },
}

# Define a function to calculate genre similarity (simple overlap here)
def genre_similarity(book1, book2):
    return len(set(book1["genre"]) & set(book2["genre"]))

# Take input from the user for a rated book and preferred genre
rated_book_title = input("Enter the title of the book you've read: ")
preferred_genres_input = input("Enter your preferred genres (comma separated, if any): ").split(",")

# Find the rated book ID based on the title input
rated_book_id = None
for book_id, book_data in books.items():
    if book_data["title"].lower() == rated_book_title.lower():
        rated_book_id = book_id
        break

# Handle the case if the book title is not found
if not rated_book_id:
    print("Book not found!")
else:
    # Recommend similar books for the user
    similar_books = sorted(
        [(book_id, genre_similarity(books[rated_book_id], books[book_id]))
         for book_id in books if book_id != rated_book_id],
        key=lambda x: x[1], reverse=True
    )[:2]  # Get top 2 most similar books

    # Display recommended books
    print("\nRecommended books based on genre similarity:")
    for book_id, similarity in similar_books:
        print(f"{books[book_id]['title']} (genre similarity: {similarity})")

    # If preferred genres are provided, find additional matches
    if preferred_genres_input:
        preferred_genres = [genre.strip().lower() for genre in preferred_genres_input]
        genre_match_books = [
            book_id for book_id, book_data in books.items()
            if any(genre.lower() in preferred_genres for genre in book_data["genre"])
        ]
        print("\nAdditional recommendations based on preferred genres:")
        for book_id in genre_match_books:
            if book_id != rated_book_id:
                print(books[book_id]["title"])
