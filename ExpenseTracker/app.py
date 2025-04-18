import tkinter as tk
from tkinter import messagebox, ttk
import datetime
import os

FILENAME = "expenses.txt"
PASSWORD = "1234"  # You can change this

# ----------- Core Functions -----------
def write_to_file(entry):
    with open(FILENAME, "a") as file:
        file.write(entry + "\n")

def read_all_entries():
    try:
        with open(FILENAME, "r") as file:
            return file.readlines()
    except FileNotFoundError:
        return []

def calculate_summary():
    income = 0
    expense = 0
    entries = read_all_entries()
    for entry in entries:
        _, t_type, amount, _ = entry.strip().split(",")
        amount = float(amount)
        if t_type == "income":
            income += amount
        else:
            expense += amount
    balance = income - expense
    return income, expense, balance

# ----------- GUI Application -----------
class ExpenseTrackerApp:
    def __init__(self, root):
        self.root = root
        self.root.title("Personal Expense Tracker")
        self.root.geometry("600x500")

        self.create_widgets()

    def create_widgets(self):
        # Frame for Entry
        entry_frame = tk.Frame(self.root)
        entry_frame.pack(pady=10)

        tk.Label(entry_frame, text="Type").grid(row=0, column=0)
        self.type_var = tk.StringVar(value="income")
        ttk.Combobox(entry_frame, textvariable=self.type_var, values=["income", "expense"]).grid(row=0, column=1)

        tk.Label(entry_frame, text="Amount").grid(row=1, column=0)
        self.amount_entry = tk.Entry(entry_frame)
        self.amount_entry.grid(row=1, column=1)

        tk.Label(entry_frame, text="Category").grid(row=2, column=0)
        self.category_entry = tk.Entry(entry_frame)
        self.category_entry.grid(row=2, column=1)

        tk.Button(entry_frame, text="Add Transaction", command=self.add_transaction).grid(row=3, columnspan=2, pady=10)

        # Frame for Summary
        self.summary_label = tk.Label(self.root, text="", font=("Arial", 12))
        self.summary_label.pack(pady=5)
        self.update_summary()

        # Frame for History
        self.history_text = tk.Text(self.root, height=15)
        self.history_text.pack(pady=10)
        self.load_history()

    def add_transaction(self):
        t_type = self.type_var.get()
        amount = self.amount_entry.get()
        category = self.category_entry.get()

        if not amount or not category:
            messagebox.showwarning("Input Error", "Please fill all fields.")
            return

        try:
            amount = float(amount)
        except ValueError:
            messagebox.showerror("Error", "Invalid amount.")
            return

        date = datetime.datetime.now().strftime("%Y-%m-%d %H:%M")
        entry = f"{date},{t_type},{amount},{category}"
        write_to_file(entry)

        self.amount_entry.delete(0, tk.END)
        self.category_entry.delete(0, tk.END)
        messagebox.showinfo("Success", "Transaction added!")

        self.load_history()
        self.update_summary()

    def load_history(self):
        entries = read_all_entries()
        self.history_text.delete(1.0, tk.END)
        if not entries:
            self.history_text.insert(tk.END, "No transactions yet.\n")
            return
        for entry in entries:
            date, t_type, amount, category = entry.strip().split(",")
            self.history_text.insert(tk.END, f"{date} | {t_type.upper():<7} | ₹{amount:<8} | {category}\n")

    def update_summary(self):
        income, expense, balance = calculate_summary()
        self.summary_label.config(text=f"Income: ₹{income}   Expense: ₹{expense}   Balance: ₹{balance}")

# ----------- Password Prompt -----------
def password_prompt():
    def check_password():
        if entry.get() == PASSWORD:
            top.destroy()
            app = ExpenseTrackerApp(root)
        else:
            messagebox.showerror("Error", "Incorrect password")

    top = tk.Toplevel()
    top.title("Login")
    top.geometry("250x100")
    tk.Label(top, text="Enter Password:").pack(pady=5)
    entry = tk.Entry(top, show="*")
    entry.pack()
    tk.Button(top, text="Submit", command=check_password).pack(pady=5)

# ----------- Run App -----------
root = tk.Tk()
password_prompt()
root.mainloop()
