from flask import Flask, render_template

app = Flask(__name__)

users_list = [
    {'id': 1, 'name': 'Adam'},
    {'id': 2, 'name': 'Sergii'}
]

@app.route('/')
def index():
    return render_template('index.html', users=users_list)

if __name__ == '__main__':
    app.run(debug=True)