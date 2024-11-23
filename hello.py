from flask import Flask, render_template


app = Flask(__name__)

@app.route('/')
# def index():
#     return "<h1>Hello World!</h1>"
def index():
    first_name = "Ankit"
    stuff = "This is bold text"
    favourite_colour = ["red", "blue", "green", 26]
    return render_template("index.html",
                           first_name=first_name,
                           stuff=stuff,
                           favourite_colour=favourite_colour)

#something like this localhost:5000/Ankit
@app.route("/user/<name>")
def user(name):
    return render_template("user.html", user_name=name)

#create custom error page

#Invalid URL
@app.errorhandler(404)

def page_not_found(e):
    return render_template("404.html"), 404

#Internal server error
@app.errorhandler(500)

def page_not_found(e):
    return render_template("500.html"), 500

if __name__ == "__main__":
    app.run(debug=True)