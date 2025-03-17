from flask import Flask, render_template, flash, request
from functions import writeToFile, fromFileToLst, findAverage
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)


savefile = "numbersFile.txt"

@app.route("/", methods = ["GET", "POST"])
def home():
    if request.method == "POST":
        # Handle the POST request (add number)
        try:
            number = request.form["number_input"]
            writeToFile(int(number), savefile)
            flash("Thank you!")
            flash("You are welcome to add more numbers!")
        except:
            flash("Please enter an integer (number without decimal, e.g., 12, 23, 65....)")
            flash("You are welcome to try again!")

    #Whether its GET or POST, we want to show the list and the average
    numberLst = fromFileToLst(savefile)
    average = findAverage(numberLst)

    return render_template("index.html", average=format(average, ".2f"), total_of_numbers=len(numberLst))


if __name__ == '__main__':
    app.run(debug=True)
