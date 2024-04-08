import sqlite3

# Questions data
questions_data = [
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

# Connect to the database
conn = sqlite3.connect('quiz.db')
c = conn.cursor()

# Create the fin_questions table if not exists
c.execute('''CREATE TABLE IF NOT EXISTS fin_questions
             (id INTEGER PRIMARY KEY, question TEXT, option1 TEXT, option2 TEXT, option3 TEXT, option4 TEXT, answer TEXT)''')

# Insert questions into the fin_questions table
for question_data in questions_data:
    question = question_data["question"]
    options = question_data["options"]
    answer = question_data["correct_answer"]

    c.execute('INSERT INTO fin_questions (question, option1, option2, option3, option4, answer) VALUES (?, ?, ?, ?, ?, ?)',
              (question, options[0], options[1], options[2], options[3], answer))

# Commit changes and close connection
conn.commit()
conn.close()
