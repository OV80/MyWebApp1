from flask import Flask, render_template, request
import psycopg2
app = Flask(__name__)
conn = psycopg2.connect(database="service_db",
                        user="elizavetapuzyreva",
                        password="",
                        host="localhost",
                        port="5433")
cursor = conn.cursor()

@app.route('/login/', methods=['GET'])
def index():
    return render_template('login.html')

@app.route('/login/', methods=['POST'])
def login():
    #if request.method == 'POST':
    username = request.form.get('username')
    password = request.form.get('password')
    if username != '' or password != '':
        cursor.execute(f"SELECT * FROM service.users WHERE login='<{username}>' AND password='<{password}>'", (str(username), str(password)))
        records = list(cursor.fetchall())
        if records != []:
            return render_template('account.html', full_name=f"Hello, {records[0][1]}!", login=f"Your login:{username}", password=f"Your password:{password}")
        else:
            return render_template('login2.html')
    else:
        return render_template('login1.html')



if __name__ == '__main__':
    app.run()


