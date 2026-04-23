
from flask import (
    Flask, render_template, request, redirect, url_for
)
from datetime import datetime
from models import Message

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        Message.create(text=request.form["message"])
        return redirect(url_for('index'))
    messages = [(message.create_at, message.text) for message in Message.select()]

    return render_template(
        'index.html',
        messages=messages)

if __name__ == '__main__':
    app.run(debug=True)
