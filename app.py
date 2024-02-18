from flask import Flask, render_template, request, redirect, url_for
from classes import User

app = Flask(__name__)

users_list = [
    User('Adam', '1@mail.com'),
    User('Sergii', '2@gmail.com')
]

def find_user(user_id):
    for user in users_list:
        if user.id == int(user_id):
            return user

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
    user = User(name, email)
    users_list.append(user)
    return redirect(url_for('index'))

@app.route('/edit-user', methods=['POST'])
def update_user():
    user_id = request.args.get('user_id')
    name = request.form.get('username')
    email = request.form.get('email')
    user = find_user(user_id)
    if user:
        user.name.value = name
        user.email.value = email
    return redirect(url_for('index'))

@app.route('/delete-user')
def delete_user():
    global users_list
    user_id = request.args.get('user_id')
    users_list = [user for user in users_list if user.id != int(user_id)]
    return redirect(url_for('index'))


@app.route('/edit-user/<user_id>')
def edit_user(user_id):
    user = find_user(user_id)
    if user:
        return render_template('edit_user.html', user=user)
    return redirect(url_for('index'))

if __name__ == '__main__':
    (app.run(debug=True))