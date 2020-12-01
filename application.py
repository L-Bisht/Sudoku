from flask import Flask, render_template, request
from flask_session import Session
from tempfile import mkdtemp
import extend
from extend import is_solved, sudoku_generator

# Configure application
app = Flask(__name__)

# Ensure templates are auto-reloaded
app.config["TEMPLATES_AUTO_RELOAD"] = True

# Ensure responses aren't cached


@app.after_request
def after_request(response):
    response.headers["Cache-Control"] = "no-cache, no-store, must-revalidate"
    response.headers["Expires"] = 0
    response.headers["Pragma"] = "no-cache"
    return response


# Configure session to use file system (instead of signed cookies)
app.config["SESSION_FILE_DIR"] = mkdtemp()
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)


# Landing Page
@app.route("/")
def index():
    return render_template("index.html")

# Game Page
@app.route("/game")
def game():
    # Generate a sudoku
    puzzle = sudoku_generator()
    return render_template("game.html", puzzle=puzzle)

# Result Page
@app.route("/result", methods=["GET", "POST"])
def result():
    if request.method == "POST":
        puzzle = []

        # Extract the values from the form
        for i in range(0, 9):
            col = []
            for j in range(0, 9):
                """
                    Extracting the fields in accordance with the input names ex: 1_2 will
                    give value at 2nd row 3rd column as 0 based index is used
                """
                val = request.form.get(str(i) + "_" + str(j))
                col.append(int(val))
            puzzle.append(col)

        # Variable for success or failure of puzzle solving
        success = False
        # Check if the puzzle is solved
        if is_solved(puzzle):
            success = True
        return render_template("result.html", success=success)
    return "Invalid request"


if __name__ == "__main__":
    app.run(debug=True)
