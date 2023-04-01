import os
from flask import Flask, request, redirect, url_for, render_template, session
app = Flask(__name__)

app.secret_key = os.urandom(12)

messages = ["hi", 'aaaa']


@app.route('/')
def hello():
    return redirect(url_for("home"))


@app.route('/home')
def home():
    if 'counter' not in session:
        session['counter'] = 0
    if 'num' not in session:
        session["num"] = len(messages)
    return render_template("homepage.html")


@app.route('/num')
def num():
    if 'num' not in session:
        session["num"] = len(messages)
    else:
        if session["counter"] == 0:
            session["num"] = len(messages)
        else:
            session["num"] = len(messages)
            session["counter"] = 0
    return str(session["num"])


@app.route('/messages')
def get_messages():
    return messages


@app.route('/new_message_counter')
def message_counter():
    if 'counter' not in session:
        session['counter'] = 0
    if 'num' not in session:
        session["num"] = len(messages)
    session["counter"] = len(messages) - session["num"]
    return str(session["counter"])


@app.route('/admin')
def admin():
    return render_template("admin.html")


@app.route('/add', methods=['POST'])
def add():
    messages.append(request.json['message'])
    return "message added"


if __name__ == '__main__':
    app.run(debug=True)
