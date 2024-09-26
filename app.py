from flask import Flask, render_template, request, make_response, flash
from io import StringIO
from random import sample, choices, shuffle
import pandas as pd
import csv

app = Flask(__name__)
app.secret_key = b'_5#y2L"F4Q8z\n\xec]/'

@app.route("/")
def home():
    return render_template("temp.html")
@app.route('/data', methods=['POST', 'GET'])
def generate_random_userdata_csv():
    fields = {}
    if request.method == 'POST' or request.method == 'GET':
        firstname = request.form.get("firstname")
        lastname = request.form.get("lastname")
        age = request.form.get("Age")
        state = request.form.get("states")
        number_of_data = int(request.form.get("data"))
        if firstname == None:
            print("First name unchecked")
        else:
            with open("firstname.txt", "r") as file:
                firstnames = [line.capitalize().strip() for line in file]
                random_firstnames = sample(firstnames, number_of_data)
                fields["First Name"] = random_firstnames
        if lastname == None:
            print("Last name unchecked")
        else:
            with open("lastname.txt", "r") as file:
                lastnames = [line.capitalize().strip() for line in file]
                random_lastnames = choices(lastnames, k=number_of_data)
                fields["Last Name"] = random_lastnames
        if age == None:
            print("Age Unchecked")
        else:
            random_age = list(range(18, 60))
            shuffle(random_age)
            random_age.extend(choices(random_age, k=number_of_data-42))
            fields["Age"] = random_age
        if state == None:
            print("State Unchecked")
        else:
            with open("statename.txt", "r") as file:
                statenames = [line.capitalize().strip() for line in file]
                shuffle(statenames)
                random_states = choices(statenames, k=number_of_data)
                fields["State"] = random_states
        df = pd.DataFrame(fields)
        if not df.empty:
            si = StringIO()
            cw = csv.writer(si)
            cw.writerow(df.columns.tolist())
            cw.writerows(df.values.tolist())
            output = make_response(si.getvalue())
            output.headers["Content-Disposition"] = "attachment; filename=userdata.csv"
            output.headers["Content-type"] = "text/csv"
            return output
        else:
            flash('No Parameters Selected')
            return render_template("temp.html")

if __name__ == "__main__":
    app.run(debug=True)