from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
# The user is default (postgres), no passowrd.
app.config['SQLALCHEMY_DATABASE_URI'] = 'postgresql:///db'
db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    name = db.Column(db.String(), nullable = False)

class Size(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer,  db.ForeignKey('product.id'))
    product_size = db.Column(db.String(), nullable = False)
    # TODO: This should be replaced by flask-currency object, Doubles are not safe
    product_price = db.Column(db.Float(), nullable = False)

class Color(db.Model):
    id = db.Column(db.Integer, primary_key = True)
    product_id = db.Column(db.Integer,  db.ForeignKey('product.id'))
    product_color = db.Column(db.String(), nullable = False)

db.create_all()


if __name__ == 'main':
    app.run()

@app.route('/')
def index():
    all_products = Product.query.all();
    return render_template('index.html', navigation = all_products)


@app.route('/create')
def create():
    return render_template('create.html')


@app.route('/product', methods = ['POST', 'GET'])
def handle_products():
    if request.method == 'POST':
        product_name = request.form['product_name']
        # if the product already exists, update
        product = Product.query.filter_by(name = product_name).first()
        if product is None:
            # Create
            new_product = Product(name=request.form['product_name'])
            db.session.add(new_product)
            db.session.commit()
            colors = request.form['product_color'].split(',')
            if request.form['product_price_small'] != '':
                new_small_size = Size(product_id = new_product.id, product_size = 'small',product_price = request.form['product_price_small'])
                db.session.add(new_small_size)
                db.session.commit()
            if request.form['product_price_medium'] != '':
                new_medium_size = Size(product_id = new_product.id, product_size = 'medium',product_price = request.form['product_price_medium'])
                db.session.add(new_medium_size)
                db.session.commit()
            if request.form['product_price_large'] != '':
                new_large_size = Size(product_id = new_product.id, product_size = 'large',product_price = request.form['product_price_large'])
                db.session.add(new_large_size)
                db.session.commit()
            # Assume colors has no duplicates
            for c in colors:
                new_color = Color(product_id = new_product.id, product_color = c)
                db.session.add(new_color)
                db.session.commit()
        else:
            # Update
            pass       
        
    return redirect(url_for('index'))


