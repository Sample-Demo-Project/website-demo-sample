from flask import Flask

app = Flask(__name__)

@app.route("/product/<int:product_id>")
def show_product(product_id):
    return f"Product ID is {product_id}"

if __name__ == "__main__":
    app.run(debug=True)
