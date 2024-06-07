from flask import Flask, render_template_string, request, redirect, url_for
import sqlite3

app = Flask(__name__)

def get_db_connection():
    conn = sqlite3.connect('products.db')
    conn.row_factory = sqlite3.Row
    return conn

@app.route('/')
@app.route('/home')
def home():
    return render_template_string("""
    <html>
    <head>
        <title>Home</title>
    </head>
    <body>
        <h1>Welcome to the Home Page</h1>
        <ul>
            <h3><li><a href="/addproduct">Add Product</a></li></h3>
            <h3><li><a href="/removeproduct">Remove Product</a></li></h3>
            <h3><li><a href="/updateproduct">Update Product</a></li></h3>
        </ul>
    </body>
    </html>
    """)

@app.route('/addproduct', methods=['GET', 'POST'])
def add():
    if request.method == 'POST':
        product_name = request.form['productname']
        product_price = request.form['price']
        conn = get_db_connection()
        conn.execute('INSERT INTO products (name, price) VALUES (?, ?)', (product_name, product_price))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template_string("""
    <html>
    <head>
        <title>Add Product</title>
    </head>
    <body>
        <h1>Add Product Page</h1>
        <form action="/addproduct" method="post">
            <label for="productname">Product Name:</label><br>
            <input type="text" id="productname" name="productname"><br>
            <label for="price">Price:</label><br>
            <input type="text" id="price" name="price"><br><br>
            <input type="submit" value="Add Product">
        </form>
    </body>
    </html>
    """)

@app.route('/removeproduct', methods=['GET', 'POST'])
def remove():
    if request.method == 'POST':
        product_id = request.form['productid']
        conn = get_db_connection()
        conn.execute('DELETE FROM products WHERE id = ?', (product_id,))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template_string("""
    <html>
    <head>
        <title>Remove Product</title>
    </head>
    <body>
        <h1>Remove Product Page</h1>
        <form action="/removeproduct" method="post">
            <label for="productid">Product ID:</label><br>
            <input type="text" id="productid" name="productid"><br><br>
            <input type="submit" value="Remove Product">
        </form>
    </body>
    </html>
    """)

@app.route('/updateproduct', methods=['GET', 'POST'])
def update():
    if request.method == 'POST':
        product_id = request.form['productid']
        new_name = request.form['productname']
        new_price = request.form['price']
        conn = get_db_connection()
        conn.execute('UPDATE products SET name = ?, price = ? WHERE id = ?', (new_name, new_price, product_id))
        conn.commit()
        conn.close()
        return redirect(url_for('home'))
    return render_template_string("""
    <html>
    <head>
        <title>Update Product</title>
    </head>
    <body>
        <h1>Update Product Page</h1>
        <form action="/updateproduct" method="post">
            <label for="productid">Product ID:</label><br>
            <input type="text" id="productid" name="productid"><br>
            <label for="productname">New Product Name:</label><br>
            <input type="text" id="productname" name="productname"><br>
            <label for="price">New Price:</label><br>
            <input type="text" id="price" name="price"><br><br>
            <input type="submit" value="Update Product">
        </form>
    </body>
    </html>
    """)

if __name__ == "__main__":
    app.run(debug=True)
