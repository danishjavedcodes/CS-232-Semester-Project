from flask import Flask, request, render_template
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy import Column, Integer, String
from sqlalchemy.ext.declarative import declarative_base


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql://postgres:sys@localhost/Wallstreets-Customers-Section'
db=SQLAlchemy(app)
@app.route('/', methods=['GET', "POST"])
def index():
    return render_template('index.html')

Base = declarative_base()
metadata = Base.metadata



class Customer(Base):
    __tablename__ = 'customers'

    f_name = Column(String, nullable=False)
    l_name = Column(String, nullable=False)
    username = Column(Integer, primary_key=True)
    email = Column(String, nullable=False)
    contact = Column(Integer, nullable=False)
    def __init__(self, f_name, l_name,username,email,contact):
        self.f_name = f_name
        self.l_name = l_name
        self.username = username
        self.email = email
        self.contact = contact



@app.route ('/submit', methods=['GET', 'POST'])
def submit():
    if request.method == 'POST':
        f_name = request.form['f_name']
        l_name = request.form['l_name']
        username = request.form['username']
        email = request.form['email']
        contact = request.form['contact']
        newuser = Customer(f_name, l_name, username, email, contact)
        db.session.add(newuser)
        db.session.commit()
    return render_template('index.html')


class Products(Base):
     __tablename__ = 'products'
     catogary = Column(String, nullable=False)
     price = Column(Integer, nullable=False)
     prod_id = Column(Integer, primary_key=True)
     pro_type = Column(String, nullable=False)
     pro_location = Column(String, nullable=False)
     address = Column(String, nullable=False)
     p_size = Column(Integer, nullable=False)
     def __init__(self, catogary, price,prod_id,pro_type,pro_location,address,p_size):
        self.catogary = catogary
        self.price = price
        self.prod_id = prod_id
        self.pro_type = pro_type
        self.pro_location = pro_location
        self.p_size = p_size
        self.address = address

@app.route ('/submit1', methods=['GET', 'POST'])
def submit1():
    if request.method == 'POST':
        catogary = request.form['catogary']
        price = request.form['price']
        prod_id = request.form['prod_id']
        pro_type = request.form['pro_type']
        pro_location = request.form['pro_location']                               
        p_size = request.form['p_size']                               
        address = request.form['address']                               
        newuser1 = Products(catogary, price,prod_id,pro_type,pro_location,address,p_size)
        db.session.add(newuser1)
        db.session.commit()
    return render_template('products.html')



if __name__ == '__main__':
    app.run(debug=True)
    app.run()
