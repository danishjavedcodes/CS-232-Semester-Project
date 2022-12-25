from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base
import psycopg2
app = Flask(__name__)

# rout to index.html


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


@app.route('/signupuser', methods=['GET', 'POST'])
def signup():
    if request.method == 'POST':
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        user_id = request.form['user_id']
        user_password = request.form['user_password']
        e_mail = request.form['e_mail']
        contact = request.form['contact']
        query = "'" + f_name + "'" + "," + "'" + l_name + "'" + "," + str(user_id) + "," + "'" + user_password + "'" + "," + "'" + e_mail + "'" + "," + str(
            contact)
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO customers (f_name,l_name,user_id,pass,email,contact) values (" + query + ")")
        conn.commit()
    return render_template('index.html')


@app.route('/registerHOD')
def registerHOD():
    return render_template('register_hod.html')


@app.route('/signup_hod', methods=['GET', 'POST'])
def signup_hod():
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
    return render_template('ceo.html')


@app.route('/registerbranch')
def registerbranch():
    return render_template('open_branch.html')


@app.route('/open_branch', methods=['GET', 'POST'])
def open_branch():
    if request.method == 'POST':
        branch_code = request.form['branch_code']
        city = request.form['city']

        query = str(branch_code) + "," + "'" + city + "'"
        cur = conn.cursor()
        cur.execute(
            "INSERT INTO branch (branch_code, city) values (" + query + ")")
        conn.commit()
    render_template('ceo.html')


@app.route('/signin', methods=['GET', 'POST'])
def signin():
    user_id = request.form['user_id']
    user_password = request.form['user_password']
    # getting password match of user_id
    cur = conn.cursor()
    cur.execute("select GET_customers_PASS("+"'" + str(user_id)+"'"+")")
    result = cur.fetchall()
    conn.commit()

    if (user_password == result[0][0]):
        return render_template('custumer.html')
    else:
        error = "invalid password or user id"
    return render_template('index.html', error=error)


@app.route("/signinadminpg")
def signinadminpg():
    admins = 'signinadmin'
    return render_template('index.html', admins=admins)


@app.route('/signinadmin', methods=['GET', 'POST'])
def signinadmin():
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
        error = "invalid password or user id"
    return render_template('index.html', error=error)


@app.route('/add_products', methods=['GET', 'POST'])
def add_products():
    if (request.method == 'POST'):
        category = request.form['category']
        price = request.form['price']
        pro_type = request.form['pro_type']
        pro_location = request.form['pro_location']
        address = request.form['address']
        p_size = request.form['p_size']
        details = request.form['description']
        query = "CALL add_products("+str(0) + ", '" + category + "', " + str(price) + ", '" + pro_type + \
            "', '" + pro_location + "', '" + address + \
                "', " + str(p_size) + ", '" + details + "')"
        cur = conn.cursor()
        cur.execute(query)
        conn.commit()
    return render_template('upload_products.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
