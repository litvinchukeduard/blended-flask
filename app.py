from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

users_list = [
    {'id': 1, 'name': 'Adam', 'email': '1@mail.com'},
    {'id': 2, 'name': 'Sergii', 'email': '2@gmail.com'}
]

@app.route('/')
def index():
    return render_template('index.html', users=users_list)

@app.route('/create-user')
def create_user_page():
    return render_template('create_user.html')

@app.route('/user', methods=['POST'])
def create_user():
    name = request.form.get('username')
    email = request.form.get('email')
    user = {'id': len(users_list) + 1, 'name': name, 'email': email}
    users_list.append(user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    app.run(debug=True)