# Personal Expense Tracker (Tkinter GUI)

A simple yet advanced personal expense tracker built with Python and Tkinter. It allows you to add income and expenses, view transaction history, and see a financial summary — all through a user-friendly GUI.

## 🧩 Features

- Add income and expenses with category and timestamp.
- Real-time summary: Total income, expenses, and balance.
- View all past transactions.
- Password protection on startup.
- Data stored in a local file (`expenses.txt`).

## 🚀 Getting Started

### Prerequisites

Make sure you have Python installed (3.6+). Install the required packages:

```bash
pip install -r requirements.txt
```

### Run the App

```bash
python expense_tracker_gui.py
```

## 🗃 File Structure

- `expense_tracker_gui.py` — main application file.
- `expenses.txt` — stores transaction history.
- `requirements.txt` — required libraries.
- `README.md` — project documentation.

## 🔐 Default Password

The app is protected with a startup password.

**Default Password:** `1234`

You can change it in the code:

```python
PASSWORD = "1234"
```

## 📦 Convert to .exe (Optional)

To create a `.exe` file:

```bash
pip install pyinstaller
pyinstaller --onefile --noconsole expense_tracker_gui.py
```

The executable will be found in the `dist/` folder.

## 📸 Screenshots

GUI screenshot, history log, and summary section can be added here.

## 📜 License

MIT License

---

### 📦 `requirements.txt`

```txt
tk
```

> Tkinter is usually built-in with Python, so the `tk` line is just for reference. No external packages are required unless you modify it further.
