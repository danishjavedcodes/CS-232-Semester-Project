from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sys@localhost/Wall-Street-Admin'
db=SQLAlchemy(app)
@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')

Base = declarative_base()
metadata = Base.metadata



class Adminuser(Base):
    __tablename__ = 'adminusers'

    f_name = Column(String, nullable=False)
    l_name = Column(String)
    user_id = Column(Integer, primary_key=True)
    user_password = Column(String, nullable=False)
    e_mail = Column(String, nullable=False)
    phone_number = Column(Integer, nullable=False)
    branch_code = Column(Integer, nullable=False)
    user_type = Column(String, nullable=False)
    def __init__(self, f_name, l_name, user_id, user_password, e_mail, phone_number, branch_code, user_type):
        self.f_name = f_name
        self.l_name = l_name
        self.user_id = user_id
        self.e_mail = e_mail
        self.user_password = user_password
        self.phone_number = phone_number
        self.branch_code = branch_code
        self.user_type = user_type
    
@app.route ('/submit', methods=['GET', 'POST'])
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
        newuser = Adminuser(f_name, l_name, user_id, user_password, e_mail, phone_number, branch_code, user_type)
        db.session.add(newuser)
        db.session.commit()
    return render_template('index.html')


if __name__ == '__main__':
    app.run(debug=True)
    app.run()
