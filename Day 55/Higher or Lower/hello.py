from flask import Flask


app = Flask(__name__)


@app.route('/')
def hello_world():
    return '<h1 style="text-align:center">Hello, World!</h1> <p>This is a paragraph.</p>'

# Different routes using the app.route decorator
@app.route('/bye')
def hello_world():
    return 'Bye'

# Creating variable paths and cinverting the path to a specified data type.
@app.route('/username/<name>/<int:number>')
def hello_world(name, number):
    return f'Hello there {name}, you are {number} years old!'


if __name__ == "__main__":
    #Run the app in debug mode to auto-reload
    app.run(debug=True)

