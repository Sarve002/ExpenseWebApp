from flask import Flask, render_template, request, redirect, url_for, flash
from flask_login import LoginManager, login_user, login_required, logout_user, current_user
from flask_bcrypt import Bcrypt
from flask_pymongo import PyMongo
from dotenv import load_dotenv
from bson.objectid import ObjectId
from flask_wtf import FlaskForm
from wtforms import StringField, SelectField, DecimalField, DateField, SubmitField
import os

# Import login and registration forms
from forms import LoginForm, RegisterForm

# Import user module and user loader function
import User
from User import User, load_user as user_load_function

# Load variables from .env
load_dotenv()

# Setup of Mongo and start up of flask, and the login manager.
app = Flask(__name__)

login_manager = LoginManager()
bcrypt = Bcrypt()
login_manager.init_app(app)

app.config["SECRET_KEY"] = os.getenv("SECRET_KEY")
app.config["MONGO_URI"] = os.getenv("MONGO_URI")
mongo = PyMongo(app)

print("Connected Collections:", mongo.db.list_collection_names())

# Initialize MongoDB, login manager, and bcrypt for hashing
mongo = PyMongo(app)
login_manager = LoginManager()
bcrypt = Bcrypt(app)
login_manager.init_app(app)
login_manager.login_view = 'login'  # Redirect unauthorized users to login

# User loader function for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    return user_load_function(user_id)# This uses the load_user function from the user.py file

# Flash messages setup (optional but helpful)
login_manager.login_view = 'login'

# Expense form using Flask-WTF
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


# --- Helper Function ---
def get_total_expenses(category):
    """
    Returns the total expense for a specific category,
    filtered by the currently logged-in user.
    """
    myCol = mongo.cx["db"]["expenses"]
    total = sum(
        float(i["cost"])
        for i in myCol.find({"category": category, "user_id": current_user.id})
    )
    return total


# --- Routes ---

@app.route('/')
@login_required
def index():
    """
    Home page showing total expenses and expenses by category for the current user.
    """
    myCol = mongo.cx["db"]["expenses"]
    
    # Get all expenses for the current user
    my_expenses = list(myCol.find({"user_id": current_user.id}))
    
    # Total cost across all categories
    total_cost = sum(float(i["cost"]) for i in my_expenses)
    
    # Cost per category for this user
    expensesByCategory = [(cat, get_total_expenses(cat)) for cat in [
        "rent", "electricity", "water", "insurance", "restaurants",
        "groceries", "gas", "college", "mortgage"
    ]]

    return render_template("index.html", 
                           expenses=total_cost, 
                           expensesByCategory=expensesByCategory,
                           expense_list=my_expenses)


@app.route('/register', methods=["GET", "POST"])
def register():
    """
    Handles user registration, including password hashing and duplicate checks.
    """
    form = RegisterForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            email = form.email.data
            password = form.password.data

            if not username or not password:
                flash("Username and password are required.", "warning")
                return redirect(url_for("register"))

            myCol = mongo.cx["db"]["users"]
            existing_user = myCol.find_one({"username": username})
            if existing_user:
                flash("Username already exists. Try a different one.", "danger")
                return redirect(url_for("register"))

            hashed_password = bcrypt.generate_password_hash(password).decode("utf-8")
            myCol.insert_one({
                "username": username,
                "email": email,
                "password": hashed_password
            })

            flash("Registration successful. Please log in.", "success")
            return redirect(url_for("login"))
        except Exception as e:
            print("Registration error:", e)
            flash("An error occurred during registration.", "danger")
            return redirect(url_for("register"))

    return render_template("register.html", form=form)


@app.route('/login', methods=["GET", "POST"])
def login():
    """
    Authenticates user credentials and starts the user session.
    """
    form = LoginForm()
    if form.validate_on_submit():
        try:
            username = form.username.data
            password = form.password.data

            myCol = mongo.cx["db"]["users"]
            user_data = myCol.find_one({"username": username})

            if user_data and bcrypt.check_password_hash(user_data["password"], password):
                user_obj = User(str(user_data["_id"]), user_data["username"])
                login_user(user_obj)
                flash("Logged in successfully.", "success")
                return redirect(url_for("index"))
            else:
                flash("Invalid username or password.", "danger")
                return redirect(url_for("login"))
        except Exception as e:
            print("Login error:", e)
            flash("An error occurred during login.", "danger")
            return redirect(url_for("login"))

    return render_template("login.html", form=form)

@app.route('/logout')
@login_required
def logout():
    """
    Logs out the user and ends the session.
    """
    logout_user()
    flash("You have been logged out.", "info")
    return redirect(url_for('index'))

# from bson.objectid import ObjectId

@app.route('/deleteExpense/<expense_id>', methods=["POST"])
@login_required
def delete_expense(expense_id):
    """
    Deletes a specific expense belonging to the current user.
    """
    try:
        result = mongo.cx["db"]["expenses"].delete_one({
            "_id": ObjectId(expense_id),
            "user_id": current_user.id
        })

        if result.deleted_count == 1:
            print(f"Deleted expense with ID: {expense_id}")
            flash("Expense deleted successfully.", "success")
        else:
            flash("Expense not found or not authorized.", "danger")

        return redirect(url_for('index'))

    except Exception as e:
        print("Delete error:", e)
        flash("Error deleting expense.", "danger")
        return redirect(url_for('index'))




@app.route('/addExpenses', methods=["GET", "POST"])
@login_required
def addExpenses():
    """
    Route to display and handle the expense submission form.
    """
    expensesForm = Expenses(request.form)
    if request.method == "POST" and expensesForm.validate():
        try:
            data = {
                "description": request.form["description"],
                "category": request.form["category"],
                "cost": float(request.form["cost"]),
                "date": request.form["date"],
                "user_id": current_user.id  # Associate with logged-in user
            }

            mongo.cx["db"]["expenses"].insert_one(data)
            flash("Expense added successfully.", "success")
            return render_template("expenseAdded.html")
        except Exception as e:
            print("Add expense error:", e)
            flash("Failed to add expense. Try again.", "danger")
            return redirect(url_for("addExpenses"))

    return render_template("addExpenses.html", form=expensesForm)

# --- Run App ---
if __name__ == "__main__":
    app.run(debug=True, port=5050)
