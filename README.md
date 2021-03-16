# TSK-ITW

### Requirments
- Postgres empty database called 'db'
- Username: postgres
- Password: 

### Python Dependencies
- Flask
- Flask-SQLAlchemy
- Psycopg2-binary

### Future work
- Deleting product
- Updating product
- Add validations on input values
- Use Money data type instead of Flaot in Prices
- Show sizes+prices and colors on index.html

### Design
```
Product: { 
  id: int primary key,
  name: string
}
```
```
Size: {
  id: int primary key,
  product_id: int foreign key (Product.id)
  product_size: string,
  product_price: money
}
```
```
Color: {
  id: int primary key,
  product_id: int foreign key (Product.id)
  product_color: string
}
```
