from flask import Flask, request, render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('login.html')

@app.route('/login', methods=['POST'])
def login():
    email = request.form['email']
    password = request.form['password']
    
    print(f'Email: {email}, Senha: {password}')

    return 'Login realizado com sucesso!'

if __name__ == '__main__':
    app.run(debug=True)
