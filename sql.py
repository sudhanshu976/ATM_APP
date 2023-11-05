import sqlite3

def create_db():
    conn = sqlite3.connect('form_data.db')
    c = conn.cursor()
    c.execute('''
        CREATE TABLE IF NOT EXISTS user_data (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT,
            pin TEXT,
            unique_id TEXT,
            balance REAL
        )
    ''')
    conn.commit()
    conn.close()

def insert_data(name, pin, unique_id,balance):
    conn = sqlite3.connect('form_data.db')
    c = conn.cursor()
    c.execute("INSERT INTO user_data (name, pin, unique_id, balance) VALUES (?, ?, ?,?)", (name, pin, unique_id,balance))
    conn.commit()
    conn.close()


def check_user(unique_id, pin):
    conn = sqlite3.connect('form_data.db')
    c = conn.cursor()
    c.execute("SELECT name FROM user_data WHERE unique_id = ? AND pin = ?", (unique_id, pin))
    user_data = c.fetchone()
    conn.close()
    return user_data

def check_user_pin(pin):
    conn = sqlite3.connect('form_data.db')
    c = conn.cursor()
    c.execute("SELECT name FROM user_data WHERE pin = ?", (pin))
    user_data = c.fetchone()
    conn.close()
    return user_data


def update_balance(unique_id, deposit_amount):
    conn = sqlite3.connect('form_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM user_data WHERE unique_id = ?", (unique_id,))
    current_balance = cursor.fetchone()
    if current_balance is not None:
        current_balance = current_balance[0]
        new_balance = current_balance + deposit_amount
        cursor.execute("UPDATE user_data SET balance = ? WHERE unique_id = ?", (new_balance, unique_id))
        conn.commit()
        conn.close()

def withdraw_balance(unique_id, withdraw_amount):
    conn = sqlite3.connect('form_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM user_data WHERE unique_id = ?", (unique_id,))
    current_balance = cursor.fetchone()
    if current_balance is not None:
        current_balance = current_balance[0]
        new_balance = current_balance - withdraw_amount
        cursor.execute("UPDATE user_data SET balance = ? WHERE unique_id = ?", (new_balance, unique_id))
        conn.commit()
        conn.close()

def update_pin(unique_id, new_pin):
    conn = sqlite3.connect('form_data.db')
    cursor = conn.cursor()
    cursor.execute("UPDATE user_data SET pin = ? WHERE unique_id = ?", (new_pin, unique_id))
    conn.commit()
    conn.close()

def check_balance(unique_id):
    conn = sqlite3.connect('form_data.db')
    cursor = conn.cursor()
    cursor.execute("SELECT balance FROM user_data WHERE unique_id = ?", (unique_id,))
    current_balance = cursor.fetchone()
    conn.close()
    return current_balance[0] if current_balance else 0.0