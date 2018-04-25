from flask import Flask, jsonify, request

app = Flask(__name__)

orders = [
    {
        "name" : "Coconut Rice",
        "price" : "300",
        "Quantity" : "2"
        
    },
    {
    
        "name" : "Coconut Rice"
        "price" : "300",
        "Quantity" : "3"

    
    }

]

@app.route('/meals/api/v1.0/meals', methods=['GET'])
def get_oders():
    return jsonify({'orders': orders})

@app.route('/meals/api/v1.0/meals', methods=['POST'])
def add_to_cart():
    cart = {"name":request.json["name"], "price":request.json["price"], "quantity":request.json["quantity"]}
    new_cart.append(cart)
    return jsonify({'orders':orders})


if __name__ == '__main__':
    app.run(debug=True)