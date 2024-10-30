from flask import Flask, render_template

app = Flask(__name__)


# Root URL ('/') displays the homepage message.
# Example: Visiting http://www.xyz.com/ will trigger this function.
@app.route("/")
def index():
    return "This is the homepage. I am excited to learn Flask."


# URL '/hello' displays a generic greeting. URL '/hello/<name>' displays a personalized greeting.
# Example: Visiting http://www.xyz.com/hello/Andrew will trigger this function with 'Andrew' as the name.
@app.route("/hello")
@app.route("/hello/<name>")
def hello(name=None):
    if name is not None:
        # return f'<h1 style="color:red">Hello, {name}!</h1><p style="color:blue">I am also excited to learn Flask.</p>'
        return render_template("hello.html", name=name)
    return "Hello world!"


# Task: Create a new route /square/<number> that calculates and displays the square of <number> when the user visits this URL. If <number> is not provided or is invalid, display an appropriate message.


# Example: Visiting http://www.xyz.com/square/3 will return '9.0'.
@app.route("/square")
@app.route("/square/<number>")
def square(number=None):
    if number is not None:
        try:
            return str(float(number) ** 2)
        except ValueError as e:
            print(e)
            return "Invalid input. Please provide a valid number after /square/"
    return "You need to provide a number."


# Task: Create a route that returns weather information for a specific location.
# Example: '/weather/Wellesley' could return current weather details for Wellesley.

if __name__ == "__main__":
    app.run(debug=True)
