from flask import Flask, request, redirect, render_template, session
import secrets

app = Flask(__name__)
app.secret_key = secrets.token_urlsafe(16)

# In-memory user data
users = {
    'alice': {'password': 'pass', 'balance': 100}
}

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/login', methods=['GET', 'POST'])
def login():
    if request.method == 'POST':
        user = request.form['username']
        pwd = request.form['password']

        if user in users and users[user]['password'] == pwd:
            session['user'] = user
            return redirect('/transfer')
        
    return render_template('login.html')

@app.route('/transfer', methods=['GET', 'POST'])
def transfer():
    if 'user' not in session:
        return redirect('/login')
    
    if request.method == 'POST':
        target = request.form['to']
        amount = int(request.form['amount'])
        users[session['user']]['balance'] -= amount

        balance = users[session['user']]['balance']
        return render_template('transfer.html', message=f"Transferred ${amount} to {target}!", balance=balance)
    
    balance = users[session['user']]['balance']
    return render_template('transfer.html', balance=balance)

if __name__ == '__main__':
    app.run(debug=True)
