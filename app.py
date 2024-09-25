from flask import Flask, render_template, request, url_for, redirect
from random import sample, choices
import pandas as pd
app = Flask(__name__)

@app.route("/")
def home():
    return render_template("temp.html")
@app.route('/data', methods=['GET', 'POST'])
def display():
    fields = {}
    if request.method == 'POST':
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        age = request.form.get("age")
        if firstname == None:
            print("First name unchecked")
        else:
            with open("firstname.txt", "r") as file:
                firstnames = [line.capitalize().strip() for line in file]
                random_firstnames = sample(firstnames, 1500)
                fields["First Name"] = random_firstnames
        if lastname == None:
            print("Last name unchecked")
        else:
            with open("lastname.txt", "r") as file:
                lastnames = [line.capitalize().strip() for line in file]
                random_lastnames = choices(lastnames, k=1500)
                fields["Last Name"] = random_lastnames
        df = pd.DataFrame(fields)
        print(df)
        # df.to_csv('userdata.csv', index=False)
        return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)