from flask import Flask, render_template

app = Flask(__name__)

# Главная страница — сразу таблица
@app.route("/")
def show_table():
    data = [
        {"id": 1, "name": "Alice", "age": 25},
        {"id": 2, "name": "Bob", "age": 30},
        {"id": 3, "name": "Charlie", "age": 22},
    ]
    return render_template("table.html", data=data)

if __name__ == "__main__":
    app.run(debug=True)
