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
      "title": "Moby-Dick",
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



# Sample user data (assuming user rated book1)
user = {
  "rated_books": ["book13"],
  "preferred_genres": [" Psychological"]  # Can be populated if user specifies preferences
}

# Define a function to calculate genre similarity (simple overlap here)
def genre_similarity(book1, book2):
  return len(set(book1["genre"]) & set(book2["genre"]))

# Recommend similar books for the user
rated_book = user["rated_books"][0]
similar_books = sorted([(book_id, genre_similarity(books[rated_book], books[book_id])) for book_id in books if book_id not in user["rated_books"]], key=lambda x: x[1], reverse=True)[:4]  # Get top 2 most similar books

for book_id, similarity in similar_books:
  print(f"Recommend {books[book_id]['title']} (genre similarity: {similarity})")
