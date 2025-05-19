# 💰 ExpenseWebApp

**ExpenseWebApp** is a personal finance tracking web application built using **Python (Flask)** and **MongoDB**. It allows users to register and log in, add and modify expenses, and view them categorized by cost and description. The application features a clean and responsive interface with modern CSS styling.

---

## 📸 Screenshots

| Login Page with Banner             | Dashboard View with Add/Modify |
|-----------------------------------|--------------------------------|
| ![login](https://github.com/user-attachments/assets/f1fbf6d6-be7f-4aac-be2d-95b8e8787dbe) | ![dashboard](https://github.com/user-attachments/assets/1d2b86bf-0f1d-48a5-b47f-f3921a587469) |
| Modify Expense page with Banner   |
| ![modify](https://github.com/user-attachments/assets/15ae1ac1-651b-4d7f-8bde-e4ab93cbc4b5)  |

## 🔧 Backend (Flask) Details

### Technologies Used
- Python 3
- Flask web framework
- Flask-WTF (for forms)
- MongoDB
- Jinja2 templating

### Key Features
- User authentication (Register, Login)
- Add new expenses (with category, date, and amount)
- Modify or update existing expenses
- Templates with shared layout using `template.html`
- Expense confirmation pages (`expenseAdded.html`)
- Frontend/backend form integration with Flask-WTF

### Key Python Files
- `app.py`: Main Flask application containing route definitions and core logic
- `forms.py`: Defines WTForms used in the app
- `User.py`: Handles MongoDB interactions and user data

---

## 🎨 Frontend (HTML/CSS/JS)

### Features
- Styled with **Tailwind CSS** for modern, responsive UI
- JavaScript interactions via `app.js`
- Clean, accessible design for:
  - Login/Register pages
  - Add/Modify expense forms
  - Main index/dashboard page

### Templates
- `index.html`: Homepage/dashboard
- `addExpenses.html`, `modifyExpenses.html`: Forms for managing expenses
- `login.html`, `register.html`: User authentication
- `template.html`: Base layout used across templates

---

## 📂 Project Structure

```
ExpenseWebApp-main/
├── Project3/
│   ├── app.py                  # Flask app
│   ├── forms.py                # WTForms for input handling
│   ├── User.py                 # User and database logic
│   ├── static/
│   │   ├── css/
│   │   └── js/
│   ├── templates/
│   │   ├── *.html              # All app templates
├── .vs/                        # Visual Studio settings
└── README.md                   # Project overview (this file)
```



---

## 🚀 Getting Started

### 1. Create Virtual Environment & Install Dependencies
```bash
python -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
pip install -r requirements.txt
```

### 2. Run the App
```bash
cd Project3
python app.py
```

> Make sure MongoDB is running locally or update the URI in your database config.

---

## 📌 Future Enhancements

- Add dashboard with charts for expense insights
- Use JWT for enhanced authentication
- Add OCR integration for scanning receipts
- Improve mobile responsiveness with Tailwind utilities
