from flask import Flask, render_template, request, redirect
import sqlite3

app = Flask(__name__)

DATABASE = "employees.db"

def init_db():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute("""
        CREATE TABLE IF NOT EXISTS employees(
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    """)

    conn.commit()
    conn.close()

@app.route('/')
def index():
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute("SELECT * FROM employees")
    employees = cur.fetchall()

    conn.close()
    return render_template('index.html', employees=employees)

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']

    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute("INSERT INTO employees (name) VALUES (?)", (name,))
    conn.commit()
    
    conn.close()
    return redirect('/')

@app.route('/delete/<int:id>')
def delete_employee(id):
    conn = sqlite3.connect(DATABASE)
    cur = conn.cursor()

    cur.execute("DELETE FROM employees WHERE id=?", (id,))
    conn.commit()
    
    conn.close()
    return redirect('/')

if __name__ == '__main__':
    init_db()
    app.run(debug=True)