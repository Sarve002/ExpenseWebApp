from flask import Flask, render_template, request, url_for
from flask_pymongo import PyMongo
from flask_wtf import FlaskForm
from wtforms import StringField, DecimalField, SelectField, DateField, SubmitField

app = Flask(__name__)
app.config["SECRET_KEY"] = "cop4813Project3"
app.config[
    "MONGO_URI"] = "mongodb+srv://newUser123:newuser123@cluster0.6ux25.mongodb.net/myFirstDatabase?ssl=true&ssl_cert_reqs=CERT_NONE"
mongo = PyMongo(app)
print(mongo.db)


class Expenses(FlaskForm):
    description = StringField('description')
    category = SelectField("category", choices=[
        ("rent", "Rent"),
        ("electricity", "Electricity"),
        ("water", "Water"),
        ("insurance", "Insurance"),
        ("restaurants", "Restaurants"),
        ("groceries", "Groceries"),
        ("gas", "Gas"),
        ("college", "College"),
        ("mortgage", "Mortgage")
    ])
    cost = DecimalField("cost")
    date = DateField('date')
    submit = SubmitField("Submit")


def get_total_expenses(category):
    myDb = mongo.cx["db"]
    myCol = myDb["expenses"]
    total_by_category = myCol.find(({"category":f"{category}"}))
    total_category = 0

    for i in total_by_category:
        total_category += float(i["cost"])

    return total_category
    # TO BE COMPLETED (please delete the word pass above)


@app.route('/')
def index():
    mydb = mongo.cx["db"]
    myCol = mydb["expenses"]
    my_expenses = myCol.find()
    total_cost = 0

    for i in my_expenses:
        total_cost += float(i["cost"])

    expensesByCategory = [
        ("rent", get_total_expenses("rent")),
        ("electricity", get_total_expenses("electricity")),
        ("water", get_total_expenses("water")),
        ("insurance", get_total_expenses("insurance")),
        ("restaurants", get_total_expenses("restaurants")),
        ("groceries", get_total_expenses("groceries")),
        ("gas", get_total_expenses("gas")),
        ("college", get_total_expenses("college")),
        ("mortgage", get_total_expenses("mortgage"))]
    # expensesByCategory is a list of tuples
    # each tuple has two elements:
    ## a string containing the category label, for example, insurance
    ## the total cost of this category
    return render_template("index.html", expenses=total_cost, expensesByCategory=expensesByCategory)


@app.route('/addExpenses', methods=["GET", "POST"])
def addExpenses():
    # INCLUDE THE FORM
    expensesForm = Expenses(request.form)
    if request.method == "POST":
        # INSERT ONE DOCUMENT TO THE DATABASE
        # CONTAINING THE DATA LOGGED BY THE USER
        # REMEMBER THAT IT SHOULD BE A PYTHON DICTIONARY
        chosen_desc = request.form["description"]
        chosen_cate = request.form["category"]
        chosen_cost = request.form["cost"]
        chosen_date = request.form['date']

        mydb = mongo.cx["db"]
        myCol = mydb["expenses"]

        data = {"description": chosen_desc, "category": chosen_cate, "cost": float(chosen_cost), 'date': chosen_date}

        insert_data = myCol.insert_one(data)
        print(insert_data.inserted_id)
        print(insert_data)

        return render_template("expenseAdded.html")
    return render_template("addExpenses.html", form=expensesForm)


app.run(debug=True, port=5050)
