from flask import Flask, jsonify

app = Flask(__name__)

TAX_RATE = 0.05  # 5%

@app.route("/price/<float:price>")
def calculate_price(price):
    tax = round(price * TAX_RATE, 2)
    total = round(price + tax, 2)

    return jsonify({
        "original_price": price,
        "tax_rate": TAX_RATE,
        "tax_amount": tax,
        "total_price": total
    })

if __name__ == "__main__":
    app.run()
