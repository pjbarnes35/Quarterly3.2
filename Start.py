import tkinter as tk
from tkinter import messagebox
import sqlite3
import random

# Function to create database and populate it with questions
def create_database():
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()

    # Create table for questions if not exists
    c.execute('''CREATE TABLE IF NOT EXISTS questions
                 (id INTEGER PRIMARY KEY, category TEXT, question TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT, answer TEXT)''')

    # Sample questions for each category
    questions = [
        {
        "question": "What is the primary goal of financial management?",
        "options": ["A. Maximizing profits", "B. Minimizing expenses", "C. Maximizing shareholder wealth", "D. Increasing market share"],
        "correct_answer": "C"
    },
    {
        "question": "What is the formula for calculating Return on Investment (ROI)?",
        "options": ["A. Net Profit / Total Assets", "B. Net Profit / Total Equity", "C. Net Profit / Total Revenue", "D. Net Profit / Investment Cost"],
        "correct_answer": "D"
    },
    {
        "question": "What does GDP stand for?",
        "options": ["A. Gross Domestic Product", "B. Gross Domestic Profit", "C. Government Development Plan", "D. Gross Dollar Price"],
        "correct_answer": "A"
    },
    {
        "question": "What is the role of the Securities and Exchange Commission (SEC)?",
        "options": ["A. Protecting consumers from fraud", "B. Regulating the stock market", "C. Managing international trade agreements", "D. Setting interest rates"],
        "correct_answer": "B"
    },
    {
        "question": "What is a balance sheet used for?",
        "options": ["A. Recording daily transactions", "B. Evaluating profitability", "C. Summarizing a company's financial position", "D. Projecting future revenue"],
        "correct_answer": "C"
    },
    {
        "question": "What is the difference between equity and debt financing?",
        "options": ["A. Equity involves borrowing money, while debt involves selling ownership stake", "B. Equity represents ownership in a company, while debt represents borrowed funds", "C. Equity financing is more risky than debt financing", "D. Debt financing offers higher returns than equity financing"],
        "correct_answer": "B"
    },
    {
        "question": "What is the role of the Federal Reserve in the economy?",
        "options": ["A. Regulating international trade", "B. Managing fiscal policy", "C. Controlling inflation and interest rates", "D. Setting tax rates"],
        "correct_answer": "C"
    },
    {
        "question": "What is the purpose of financial ratios?",
        "options": ["A. Comparing a company's financial performance over time", "B. Evaluating a company's liquidity, profitability, and solvency", "C. Predicting future stock prices", "D. Assessing market trends"],
        "correct_answer": "B"
    },
    {
        "question": "What is the difference between capital expenditure and operating expenditure?",
        "options": ["A. Capital expenditure is for short-term expenses, while operating expenditure is for long-term investments", "B. Capital expenditure is for acquiring fixed assets, while operating expenditure is for day-to-day expenses", "C. Operating expenditure is financed through equity, while capital expenditure is financed through debt", "D. Capital expenditure is tax-deductible, while operating expenditure is not"],
        "correct_answer": "B"
    },
    {
        "question": "What is the concept of present value in finance?",
        "options": ["A. The value of money in the future compared to its value today", "B. The total amount of money an investment will generate over its lifetime", "C. The amount of money needed to start a business", "D. The value of a company's stock on the open market"],
        "correct_answer": "A"
    },
    {
        "question": "What is the purpose of a cash flow statement?",
        "options": ["A. Tracking changes in a company's stock price", "B. Evaluating a company's ability to generate cash", "C. Forecasting future revenue", "D. Assessing market risk"],
        "correct_answer": "B"
    }
    ]

    # Insert sample questions into the database
    c.executemany('INSERT INTO fin_questions (category, question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?, ?)', questions)

    conn.commit()
    conn.close()

# Function to fetch questions from database based on category
def fetch_questions(category):
    conn = sqlite3.connect('quiz.db')
    c = conn.cursor()
    c.execute('SELECT * FROM questions WHERE category=?', (category,))
    questions = c.fetchall()
    conn.close()
    return questions

# Function to start the quiz
def start_quiz(category):
    questions = fetch_questions(category)
    random.shuffle(questions)
    quiz_window(questions)

# Function to display quiz window
def quiz_window(questions):
    # Create a new window for the quiz
    quiz_window = tk.Toplevel(root)
    quiz_window.title("Quiz")
    
    # Variables to track user's score and current question
    score = tk.IntVar()
    current_question = 0

    # Function to check answer
    def check_answer():
        nonlocal current_question
        selected_answer = var.get()
        correct_answer = questions[current_question][7]

        if selected_answer == correct_answer:
            messagebox.showinfo("Result", "Correct!")
            score.set(score.get() + 1)
        else:
            messagebox.showinfo("Result", "Incorrect!")

        current_question += 1
        if current_question < len(questions):
            display_question()
        else:
            messagebox.showinfo("Quiz Finished", f"Your score: {score.get()}")

    # Function to display current question
    def display_question():
        question_label.config(text=questions[current_question][2])
        option1.config(text=questions[current_question][3])
        option2.config(text=questions[current_question][4])
        option3.config(text=questions[current_question][5])
        option4.config(text=questions[current_question][6])

    # Display question and options
    question_label = tk.Label(quiz_window, text="")
    question_label.pack()

    var = tk.StringVar()
    option1 = tk.Radiobutton(quiz_window, text="", variable=var, value="A")
    option1.pack()
    option2 = tk.Radiobutton(quiz_window, text="", variable=var, value="B")
    option2.pack()
    option3 = tk.Radiobutton(quiz_window, text="", variable=var, value="C")
    option3.pack()
    option4 = tk.Radiobutton(quiz_window, text="", variable=var, value="D")
    option4.pack()

    next_button = tk.Button(quiz_window, text="Next", command=check_answer)
    next_button.pack()

    # Display the first question
    display_question()

# Main window
root = tk.Tk()
root.title("Quiz App")

# Create database and populate with questions
# create_database()

# Function to handle start button click
def start_clicked():
    category = category_var.get()
    start_quiz(category)

# Label and dropdown for selecting category
category_label = tk.Label(root, text="Select a category:")
category_label.pack()
category_var = tk.StringVar()
category_dropdown = tk.OptionMenu(root, category_var, "Finance", "Business Communications 2", "Business Applications Development", "Business Analytics Capstone", "Business Strategy")
category_dropdown.pack()

start_button = tk.Button(root, text="Start Quiz Now", command=start_clicked)
start_button.pack()

root.mainloop()
