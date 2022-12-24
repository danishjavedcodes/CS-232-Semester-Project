from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import psycopg2


app = Flask(__name__)


@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')


conn = psycopg2.connect(
    database="Wall-Street-Admin",
    user="postgres",
    password="sys",
    host="localhost",
    port="5432"
)


@app.route('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        user_id = request.form['user_id']
        user_password = request.form['user_password']
        e_mail = request.form['e_mail']
        phone_number = request.form['phone_number']
        branch_code = request.form['branch_code']
        user_type = request.form['user_type']
        query = "'" + f_name + "'" + "," + "'" + l_name + "'" + "," + str(user_id) + "," + "'" + user_password + "'" + "," + "'" + e_mail + "'" + "," + str(
            phone_number) + "," + str(branch_code) + "," + "'" + user_type + "'"
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO adminusers (f_name,l_name,user_id,user_password,e_mail,phone_number,branch_code,user_type) values (" + query + ")")

        conn.commit()
        cur = conn.cursor()
        cur.execute("ROLLBACK")
        conn.commit()
        cur.execute("SELECT * FROM adminusers")
        rows = cur.fetchall()
        for row in rows:
            print('First Name ', row[0])
            print('Last Name ', row[1])
            print('UserName ', row[2])
            print('Password ', row[3])
            print('EMAIL ', row[4])
            print('Phone number ', row[5])
            print('Branch ', row[6])
            print('Type ', row[7])
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
