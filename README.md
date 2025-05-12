# 💸 ExpenseWebApp

A full-stack expense tracking application built with Flask, MongoDB, and Tailwind CSS. Users can add, view, and delete their expenses in a clean, responsive dashboard.

---

## 📌 Description

The ExpenseWebApp allows users to:

- Input and track daily expenses
- Categorize expenses by type (e.g., Food, Utilities, Travel, etc.)
- Add descriptions and timestamps to entries
- View all expenses in a clean, responsive UI
- Automatically calculate total expenses

---

## 🛠️ Tools & Technologies Used

- **Frontend**: HTML, CSS (Webflow-generated), Bootstrap
- **Backend**: Python, Flask, WTForms
- **Database**: MongoDB Atlas (NoSQL)
- **Other Tools**: PyCharm, GitHub, Git

---

## ✅ Features

- User input for expenses with date, cost, category, and description
- Expenses stored in MongoDB and displayed dynamically
- Responsive layout
- UI enhancements using Tailwind UI (CSS updates and visual improvements)
- Git-based version control and deployment workflow
- Replaced Bootstrap and Webflow with Tailwind CSS
- Mobile-friendly, clean layouts and consistent button styling
- Darker striped table rows for clarity

### 🖼️ Dynamic Page Banners
Each page now includes a unique banner:
- **Login/Register** → `login-banner.jpg`
- **Dashboard** → `dashboard-bg.jpg`
- **Add/Modify Expenses** → `expenses.jpg`

### 🧩 Modify Expenses Page
- New `modifyExpenses.html` page to review and delete expenses
- Back button to dashboard
- Stays on page after deleting

### 🧭 Navigation Improvements
- Added `Modify Expenses` to the navbar and dashboard buttons
- Removed redundant expense table from dashboard

---
### Future Improvements
- Edit expense functionality
- Charts for spending by category
- User profile settings
- Deployment to Render or Fly.io
---

## 📸 Screenshots

| Login Page with Banner             | Dashboard View with Add/Modify |
|-----------------------------------|--------------------------------|
| ![login](https://github.com/user-attachments/assets/f1fbf6d6-be7f-4aac-be2d-95b8e8787dbe) | ![dashboard](https://github.com/user-attachments/assets/1d2b86bf-0f1d-48a5-b47f-f3921a587469) |

| ![modify](https://github.com/user-attachments/assets/15ae1ac1-651b-4d7f-8bde-e4ab93cbc4b5) | 


---

## ⚙️ Setup Instructions

```bash
git clone https://github.com/yourusername/ExpenseWebApp.git
cd ExpenseWebApp
pip install -r requirements.txt
flask run
