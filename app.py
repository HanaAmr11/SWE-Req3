from flask import Flask, jsonify, request

app = Flask(__name__)
books = [
    {"id": 1, "title": "The Great Gatsby", "author": "F. Scott Fitzgerald"},
    {"id": 2, "title": "1984", "author": "George Orwell"},
    {"id": 3, "title": "To Kill a Mockingbird", "author": "Harper Lee"},
    {"id": 4, "title": "The Catcher in the Rye", "author": "J.D. Salinger"},
    {"id": 5, "title": "Moby Dick", "author": "Herman Melville"},
]
# Middleware to log requests
@app.before_request
def log_request():
    print(f"Request: {request.method} {request.path}")
@app.route('/books', methods=['GET'])
def get_books():
    return jsonify(books), 200

@app.route('/books/<int:book_id>', methods=['GET'])
def get_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books', methods=['POST'])
def create_book():
    new_book = request.get_json()
    new_book['id'] = len(books) + 1
    books.append(new_book)
    return jsonify(new_book), 201

@app.route('/books/<int:book_id>', methods=['PUT'])
def update_book(book_id):
    book = next((book for book in books if book['id'] == book_id), None)
    if book:
        data = request.get_json()
        book.update(data)
        return jsonify(book)
    return jsonify({"error": "Book not found"}), 404

@app.route('/books/<int:book_id>', methods=['DELETE'])
def delete_book(book_id):
    global books
    books = [book for book in books if book['id'] != book_id]
    return '', 204

if __name__ == '__main__':
    app.run(debug=True)
