from flask import Flask, render_template, redirect, session
from app_forms import LoginForm, TransferForm
from flask_wtf.csrf import CSRFProtect
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16) # Required for FlaskWTF
csrf = CSRFProtect(app)

# In-memory users
users = {
    'alice': {'password': 'pass', 'balance': 100}
}

@app.route('/')
def home():
    return render_template('index.html')

# The routes have now changed from using forms in the HTML-page,
# to using the FlaskWTF instead here in Python.
@app.route('/login', methods=['GET', 'POST'])
def login():
    form = LoginForm()
    if form.validate_on_submit():
        user = form.username.data
        pwd = form.password.data

        if user in users and users[user]['password'] == pwd:
            session['user'] = user
            return redirect('/transfer')
        
    return render_template('login.html', form=form)


@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user' not in session:
        return redirect('/login')
    
    form = TransferForm()
    if form.validate_on_submit():
        sender = session['user']
        recipient = form.to.data
        amount = form.amount.data
        users[sender]['balance'] -= amount

        message = f"Transferred ${amount} to {recipient}!"
        return render_template('transfer.html', form=form, balance=users[sender]['balance'], message=message)
    
    balance = users[session['user']]['balance']
    return render_template('transfer.html', form=form, balance=balance)


if __name__ == '__main__':
    app.run(debug=True)
