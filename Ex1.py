from flask import Flask, render_template_string
app = Flask(__name__)
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
            <h3><li><a href="/updateproduct">Update Product</a></li><h3>
        </ul>
    </body>
    </html>
    """)

@app.route('/addproduct')
def add():
    return render_template_string("""
    <html>
    <head>
        <title>Add Product</title>
    </head>
    <body>
        <h1>Add Product Page</h1>
        <h1><form action="/addproduct" method="post"></h1>
            <label for="productname">Product Name:</label><br>
            <input type="text" id="productname" name="productname"><br>
            <label for="price">Price:</label><br>
            <input type="text" id="price" name="price"><br><br>
            <input type="submit" value="Add Product">
        </form>
    </body>
    </html>
    """)

@app.route('/removeproduct')
def remove():
    return render_template_string("""
    <html>
    <head>
        <title>Remove Product</title>
    </head>
    <body>
        <h1>Remove Product Page</h1>
        <h1><form action="/removeproduct" method="post"></h1>
            <label for="productid">Product ID:</label><br>
            <input type="text" id="productid" name="productid"><br><br>
            <input type="submit" value="Remove Product">
        </form>
    </body>
    </html>
    """)

@app.route('/updateproduct')
def update():
    return render_template_string("""
    <html>
    <head>
        <title>Update Product</title>
    </head>
    <body>
        <h1>Update Product Page</h1>
        <h1><form action="/updateproduct" method="post"></h1>
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
