from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__, static_folder='./static')

# Create an in-memory database for books and users
books = []
users = []

class Book:
    def __init__(self, title, author):
        self.title = title
        self.author = author

class User:
    def __init__(self, name):
        self.name = name

# Define a custom Jinja2 filter for enumerate
@app.template_filter('enumerate')
def jinja2_enumerate(iterable, start=0):
    return enumerate(iterable, start)

@app.route('/')
def index():
    return render_template('index.html', books=books, users=users)

@app.route('/add_book', methods=['POST'])
def add_book():
    title = request.form.get('title')
    author = request.form.get('author')
    book = Book(title, author)
    books.append(book)
    return redirect(url_for('index'))

@app.route('/remove_book/<int:index>')
def remove_book(index):
    if 0 <= index < len(books):
        books.pop(index)
    return redirect(url_for('index'))

@app.route('/add_user', methods=['POST'])
def add_user():
    name = request.form.get('name')
    user = User(name)
    users.append(user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)
