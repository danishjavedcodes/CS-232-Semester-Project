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


@app.route('/signup', methods=['GET', 'POST'])
def signup():
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
    return render_template('index.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    user_id = request.form['user_id']
    user_password = request.form['user_password']
    # getting password match of user_id
    cur = conn.cursor()
    cur.execute("select Get_PASS("+str(user_id)+")")
    result = cur.fetchall()
    conn.commit()

    # getting user_type

    cur = conn.cursor()
    cur.execute("select GET_type("+str(user_id)+")")
    u_type = cur.fetchall()
    u_types = [('CEO', 'HOD')]

    if (user_password == result[0][0] and u_type[0][0] == u_types[0][0]):
        return render_template('ceo.html')
    elif (user_password == result[0][0] and u_type[0][0] == u_types[0][1]):
        return render_template('hod.html')
    else:
        print("password not matched")
        return render_template('custumer.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
